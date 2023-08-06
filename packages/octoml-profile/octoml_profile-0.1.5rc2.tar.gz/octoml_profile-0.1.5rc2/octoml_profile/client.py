# Copyright 2023 OctoML, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os
import sys
import threading
import traceback
import weakref
from collections import defaultdict
from contextlib import ExitStack
from typing import Iterator, List, Mapping, Optional, Sequence, Tuple, Union, Iterable
from uuid import UUID

import grpc

from .conversion_util import numpy_to_proto, proto_to_backend_str
from .errors import LoadModelError, CreateSessionError
from .inference_session import (BackendSpec, InferenceSession, ModelRunner,
                                RunResult, FileDescription)
from .interceptors.auth import AuthInterceptor, StreamAuthInterceptor
from .interceptors.cookie import CookieInterceptor, StreamCookieInterceptor
from .log_util import LOGFILE, get_file_logger
from .protos import remote_inference_pb2 as pb, remote_inference_pb2_grpc as rpc

BackendSpecType = Union[str, BackendSpec, Sequence[Union[str, BackendSpec,
                                                         pb.BackendSpec]]]

MODEL_FORMAT_ONNX = pb.MODEL_FORMAT_ONNX
MODEL_FORMAT_FXPROTO = pb.MODEL_FORMAT_FXPROTO


MAX_GRPC_MESSAGE_SIZE = 1024 * 1024 * 1024   # 1GiB


class RemoteModelRunner(ModelRunner):
    def __init__(self,
                 session: 'RemoteInferenceSession',
                 model_id: int,
                 input_map_per_backend: Sequence[pb.InputMap]):
        self._session = weakref.ref(session)
        self._model_id = model_id
        self._input_map_per_backend = input_map_per_backend

    def run(self, inputs, num_repeats=None) -> Mapping[BackendSpec, RunResult]:
        session = self._session()
        input_protos = [numpy_to_proto(x) for x in inputs]
        request = pb.RunRequest(session_uuid=session._session_uuid.bytes,
                                model_id=self._model_id,
                                inputs=input_protos,
                                num_repeats=num_repeats,
                                input_map_per_backend=self._input_map_per_backend)
        reply = session._stub.Run(request)
        assert len(reply.result_per_backend) == len(session._backends)
        return {
            backend: RunResult.from_pb(result)
            for backend, result in zip(session._backends, reply.result_per_backend)
        }


def _get_backend_specs(backends: Optional[BackendSpecType] = None)\
        -> Sequence[BackendSpec]:
    if backends is None:
        return []
    if isinstance(backends, str):
        return BackendSpec.parse(backends),
    elif isinstance(backends, BackendSpec):
        return backends
    else:
        ret = []
        for backend in backends:
            if isinstance(backend, str):
                ret.append(BackendSpec.parse(backend))
            elif isinstance(backend, BackendSpec):
                ret.append(backend)
            elif isinstance(backend, pb.BackendSpec):
                ret.append(BackendSpec(backend.hardware_platform, backend.software_backend))
            else:
                raise TypeError(f'Expected a string or a BackendSpec, got {type(backend)}')
        return ret


def _heartbeat_thread(stub: rpc.RemoteInferenceStub,
                      session_uuid: UUID,
                      quit_event: threading.Event,
                      logger: logging.Logger):
    HEARTBEAT_PERIOD_SECONDS = 10
    RETRY_TIMEOUT_SECONDS = 1

    next_timeout = HEARTBEAT_PERIOD_SECONDS
    prev_future = None

    while True:
        if quit_event.wait(timeout=next_timeout):
            break

        if prev_future is not None:
            if not prev_future.done():
                next_timeout = RETRY_TIMEOUT_SECONDS
                continue

            try:
                prev_future.result()
            except grpc.RpcError as e:
                if e.code() in {grpc.StatusCode.FAILED_PRECONDITION,
                                grpc.StatusCode.PERMISSION_DENIED}:
                    logger.error(e, exc_info=True)
                    print(f"\nReceived GRPC error {e.code()}, stopping the heartbeat thread",
                          file=sys.stderr)
                    print(f"For full client-side error traces see {LOGFILE}", file=sys.stderr)
                    return

        try:
            prev_future = stub.Heartbeat.future(
                pb.HeartbeatRequest(session_uuid=session_uuid.bytes))
        except grpc.RpcError:
            # TODO: log?
            next_timeout = RETRY_TIMEOUT_SECONDS
            prev_future = None
            continue

        next_timeout = HEARTBEAT_PERIOD_SECONDS


class RemoteInferenceSession(InferenceSession):
    def __init__(self,
                 backends: Optional[BackendSpecType] = None,
                 server_addr: str = 'dynamite.prod.aws.octoml.ai',
                 insecure: bool = False,
                 access_token: Optional[str] = None):
        super().__init__()
        self._supported_backends = None
        self._channel = None
        self._stub = None
        self._session_uuid = None
        self._heartbeat_thread = None
        self._heartbeat_quit_event = threading.Event()
        self._logger = get_file_logger(__name__)
        self._backends = _get_backend_specs(backends)
        self._last_component_id_by_model_id = defaultdict(int)
        backend_protos = [
            pb.BackendSpec(hardware_platform=b.hardware_platform,
                           software_backend=b.software_backend) for b in self._backends
        ]
        access_token = os.environ.get("OCTOML_PROFILE_API_TOKEN", None) or access_token
        server_addr = os.environ.get("OCTOML_PROFILE_ENDPOINT", None) or server_addr

        with ExitStack() as guard:
            if insecure:
                self._channel = grpc.insecure_channel(
                    server_addr,
                    options=(
                        ('grpc.max_send_message_length', MAX_GRPC_MESSAGE_SIZE),
                        ('grpc.max_receive_message_length', MAX_GRPC_MESSAGE_SIZE),
                    ),
                )
            else:
                credentials = grpc.ssl_channel_credentials()
                self._channel = grpc.secure_channel(
                    server_addr,
                    credentials,
                    options=(
                        ('grpc.max_send_message_length', MAX_GRPC_MESSAGE_SIZE),
                        ('grpc.max_receive_message_length', MAX_GRPC_MESSAGE_SIZE),
                    ),
                )
                if access_token is not None:
                    self._channel = grpc.intercept_channel(self._channel,
                                                           AuthInterceptor(access_token),
                                                           StreamAuthInterceptor(access_token))

            def reset_channel():
                self._channel.close()
                # Set _channel to None so that __del__ doesn't try to send any messages over it
                # or to close it again
                self._channel = None

            guard.callback(reset_channel)

            self._stub = rpc.RemoteInferenceStub(self._channel)

            try:
                # Before creating the session, check that requested backends are valid
                supported_backends = self._get_supported_backends()
                if len(backend_protos) == 0:
                    backend_protos = self._get_default_supported_backends()
                    self._backends = _get_backend_specs(backend_protos)
                    requested_backends = list(map(proto_to_backend_str, backend_protos))
                    print(f'No backends were requested, using defaults: {requested_backends}',
                          file=sys.stderr)
                unsupported = [b for b in backend_protos if b not in supported_backends.backends]
                if len(unsupported) > 0:
                    unsupported_str = ', '.join(map(proto_to_backend_str, unsupported))
                    message = f'Some of the requested backends ({unsupported_str})' \
                              f' are not supported.\n'
                    message += self._make_supported_backends_message()
                    raise ValueError(message)

                request = pb.CreateSessionRequest(backends=backend_protos)
                reply, call = self._stub.CreateSession.with_call(request)

                # Set cookie for sticky sessions
                for item in call.initial_metadata():
                    if item.key == 'set-cookie':
                        cookie = item.value
                        self._channel = grpc.intercept_channel(self._channel,
                                                               CookieInterceptor(cookie),
                                                               StreamCookieInterceptor(cookie))
                        self._stub = rpc.RemoteInferenceStub(self._channel)

                if reply.WhichOneof('result') == 'error_value':
                    raise ValueError(f"Error starting a remote inference session:"
                                     f" {reply.error_value.message}")

            except grpc.RpcError as rpc_error:
                # Extract the details of the gRPC error
                if hasattr(rpc_error, "debug_error_string"):
                    status_debug_string = f" [debug_error_string: {rpc_error.debug_error_string()}]"
                else:
                    status_debug_string = ""

                self._logger.error("An error occurred in CreateSession RPC:"
                                   f" {status_debug_string}", exc_info=True)

                # TODO(yuanjing_octoml): handle more status code types
                status_code = rpc_error.code()
                status_details = rpc_error.details()
                if status_code == grpc.StatusCode.UNAVAILABLE:
                    status_details = "Connection can't be established between client and server. " \
                                     "This could be caused by incorrect ip addresses or port " \
                                     "numbers"
                elif status_code == grpc.StatusCode.INTERNAL:
                    status_details = "An internal error ocurred, typically due to starting " \
                                     "the remote session with wrong configuration(s)"

                # use from None to suppress stack trace from rpc_error
                raise CreateSessionError(f"Error {status_code.name}:"
                                         f" {status_details}. See full client-side"
                                         f" trace at {LOGFILE}") from None

            reply = reply.result_value
            self._session_uuid = UUID(bytes=reply.session_uuid)
            self._logger.info(f"Created session with uuid {self._session_uuid}")

            # If we get a KeyboardInterrupt or another exception before returning from __init__,
            # we want to attempt to send a CloseSession() request if possible.
            # This is most likely to happen when the user gives up on waiting for the session
            # to start and hits Ctrl-C.
            guard.callback(self._send_close_session_message_silently)

            if not reply.ready:
                print('Waiting for an available remote worker...', file=sys.stderr)
                while True:
                    reply = self._stub.WaitUntilSessionReady(
                        pb.WaitUntilSessionReadyRequest(session_uuid=self._session_uuid.bytes))

                    if reply.ready:
                        print('Acquired all workers, session is now ready.', file=sys.stderr)
                        break

            guard.pop_all()

        self._heartbeat_thread = threading.Thread(
            target=_heartbeat_thread,
            kwargs=dict(
                stub=self._stub,
                session_uuid=self._session_uuid,
                quit_event=self._heartbeat_quit_event,
                logger=self._logger,
            ),
            daemon=True
        )
        self._heartbeat_thread.start()

    def _send_close_session_message_silently(self):
        try:
            self._stub.CloseSession(
                pb.CloseSessionRequest(session_uuid=self._session_uuid.bytes))
        except grpc.RpcError:
            # We've done our part. In the worst case, the session
            # will time out on the server.
            pass

    @property
    def backends(self) -> Sequence[BackendSpec]:
        return tuple(self._backends)

    def _get_supported_backends(self) -> pb.ListSupportedBackendsReply:
        if self._supported_backends is None:
            reply = self._stub.ListSupportedBackends(pb.ListSupportedBackendsRequest())
            self._supported_backends = reply
        return self._supported_backends

    def _get_default_supported_backends(self) -> List[pb.BackendSpec]:
        for p in self._get_supported_backends().presets:
            if p.preset_name == "default":
                return p.backends
        raise ValueError("The server did not provide a list of default backends to use")

    def _make_supported_backends_message(self):
        allowed_backend_strs = list(map(proto_to_backend_str,
                                        self._get_supported_backends().backends))
        allowed_backends_rep = '\n\t'.join(allowed_backend_strs)
        return (f'The supported, valid backends are:\n\t{allowed_backends_rep}\n'
                'Please create your remote inference session with valid backends;\n'
                f'e.g. session = RemoteInferenceSession(["{allowed_backend_strs[0]}"])')

    def close(self):
        if self._heartbeat_thread is not None:
            self._heartbeat_quit_event.set()
            self._heartbeat_thread = None

        if self._channel is not None:
            if self._session_uuid is not None and self._stub is not None:
                self._send_close_session_message_silently()
                self._session_uuid = None
                self._stub = None

            self._channel.close()
            self._channel = None

    def load_model(self,
                   model_id: int,
                   backend_ids: Sequence[int],
                   model_format: pb.ModelFormat,
                   model_files: Sequence[FileDescription],
                   input_names: Sequence[str],
                   output_names: Sequence[str]):
        backend_skip_mask = self._make_backend_skip_mask(backend_ids)
        base_component_id = self._last_component_id_by_model_id[model_id] + 1

        for model_component_id, file_desc in enumerate(model_files, base_component_id):
            sha256 = file_desc.sha256()
            req = pb.LoadCachedModelComponentRequest(session_uuid=self._session_uuid.bytes,
                                                     model_id=model_id,
                                                     model_component_id=model_component_id,
                                                     sha256_hash=sha256,
                                                     filename=file_desc.name(),
                                                     backends_to_skip_bitmask=backend_skip_mask)

            try:
                reply = self._stub.LoadCachedModelComponent(req)
            except grpc.RpcError as e:
                if e.code() == grpc.StatusCode.NOT_FOUND:
                    request_iter = _request_stream_from_file(
                            file_desc, self._session_uuid, model_id,
                            model_component_id, backend_skip_mask)
                    reply = self._stub.LoadModelComponent(request_iter)
                else:
                    raise LoadModelError("Error in load cached component: "
                                         "graph {}, component {}, {}"
                                         .format(model_id, model_component_id, str(e)))

            all_errors, error_messages = self._load_error_info(model_id,
                                                               model_component_id,
                                                               self._backends,
                                                               reply.result_per_backend)

            if all_errors:
                raise LoadModelError("Error in load component: "
                                     "graph {}, component {}, {}"
                                     .format(model_id, model_component_id,
                                             str(error_messages)))

            self._last_component_id_by_model_id[model_id] = model_component_id

        req = pb.LoadModelRequest(session_uuid=self._session_uuid.bytes,
                                  model_id=model_id,
                                  model_format=model_format,
                                  input_names=input_names,
                                  output_names=output_names,
                                  backends_to_skip_bitmask=backend_skip_mask)
        reply = self._stub.LoadModel(req)

        all_errors, error_messages = self._load_error_info(model_id,
                                                           None,  # component id
                                                           self._backends,
                                                           reply.result_per_backend)

        if all_errors:
            raise LoadModelError(f"Error in load graph: graph {model_id}, {str(error_messages)}")

    def create_runner(self, model_id: int,
                      input_map_per_backend: Sequence[Sequence[int]]) -> ModelRunner:
        assert len(input_map_per_backend) == len(self._backends)
        input_map_proto = tuple(pb.InputMap(input_value_indices=indices)
                                for indices in input_map_per_backend)
        return RemoteModelRunner(self, model_id, input_map_proto)

    def _make_backend_skip_mask(self, selected_backends: Iterable[int]) -> bytes:
        mask = (1 << len(self._backends)) - 1
        for idx in selected_backends:
            mask &= ~(1 << idx)
        return mask.to_bytes((len(self._backends) + 7) // 8, "little")

    def _load_error_info(
        self,
        model_id: int,
        model_component_id: Optional[int],
        backends: Sequence[BackendSpec],
        result_per_backend: Union[Sequence[pb.LoadModelComponentResult],
                                  Sequence[pb.LoadModelResult]]) \
            -> Tuple[bool, Sequence[str]]:
        all_errors = True
        error_messages = []
        for backend, result in zip(backends, result_per_backend):
            if result.HasField("error_value"):
                if model_component_id is None:
                    self._logger.error("Error in load graph %d on backend %s: %s",
                                       model_id, str(backend), result.error_value.message)
                else:
                    self._logger.error("Error in load graph %d "
                                       "component %d on "
                                       "backend %s: %s",
                                       model_id, model_component_id,
                                       str(backend), result.error_value.message)
                error_messages.append(result.error_value.message)
            else:
                all_errors = False
        return all_errors, error_messages


def _request_stream_from_file(file: FileDescription,
                              session_uuid: UUID,
                              model_id: int,
                              model_component_id: int,
                              backend_skip_mask: bytes) -> Iterator[pb.LoadModelComponentRequest]:
    try:
        req = pb.LoadModelComponentRequest(session_uuid=session_uuid.bytes,
                                           model_id=model_id,
                                           model_component_id=model_component_id,
                                           filename=file.name(),
                                           backends_to_skip_bitmask=backend_skip_mask)
        interactive_progress = hasattr(sys.stderr, "fileno") and os.isatty(sys.stderr.fileno())
        MAX_CHUNK_LEN = 1024 * 1024
        num_chunks = 0
        bytes_sent = 0

        with file.open(MAX_CHUNK_LEN) as (total_size, chunks):
            total_size_mb = total_size / (1024 * 1024)
            upload_message = f"Uploading {total_size_mb} MB" \
                             f" [item {model_component_id} of graph {model_id}]"
            if not interactive_progress:
                print(f"{upload_message}...", file=sys.stderr)
            for chunk in chunks:
                req.chunk = chunk
                yield req
                bytes_sent += len(chunk)
                percent_done = int(100 * bytes_sent / total_size)
                if interactive_progress:
                    print(f"{upload_message}... {percent_done}%\r", flush=True,
                          end='', file=sys.stderr)
                req = pb.LoadModelComponentRequest()
                num_chunks += 1

            if num_chunks == 0:
                yield req

            if total_size != bytes_sent:
                raise RuntimeError(f"File size mismatch: originally determined as"
                                   f" {total_size} bytes but only read {bytes_sent} bytes")

        if interactive_progress:
            print(f"{upload_message}... 100%", file=sys.stderr)
    except Exception:
        # GRPC hides exceptions that are raised in the request iterator, so we print it here
        traceback.print_exc()
        raise
