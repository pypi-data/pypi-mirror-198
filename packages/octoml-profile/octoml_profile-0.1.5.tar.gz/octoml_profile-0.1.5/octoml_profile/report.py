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

import functools
import sys
from dataclasses import dataclass
from typing import Dict, Sequence, OrderedDict, Optional, List

from .log_util import LOGFILE


__all__ = ['PerBackendResult', 'Segment', 'TotalPerBackendResult', 'Profile', 'ProfileReport']

# The maximum number of displayed compiled segments in the summary. When this
# threshold is crossed, an abridged summary is displayed.
MAX_COMPILED_SEGMENTS_DISPLAYED_DEFAULT = 3


@dataclass
class PerBackendResult:
    mean_ms: Optional[float]
    num_samples: int
    num_failures: int

    def total_ms(self):
        return self.mean_ms * self.num_samples


@dataclass
class Segment:
    graph_id: Optional[int]  # None if segment is uncompiled
    results_per_backend: OrderedDict[str, PerBackendResult]

    def add(self, segment: 'Segment'):
        # We should only ever aggregate compiled segments per graph id when we have
        # more compiled segments than MAX_COMPILED_SEGMENTS_DISPLAYED_DEFAULT.
        assert self.graph_id and self.graph_id == segment.graph_id
        for backend, update in segment.results_per_backend.items():
            total = self.results_per_backend[backend]
            total_samples = total.num_samples + update.num_samples

            if total.mean_ms and update.mean_ms:
                total.mean_ms = (total.total_ms() + update.total_ms()) / total_samples
            elif total.mean_ms is None:
                total.mean_ms = update.mean_ms

            total.num_samples = total_samples
            total.num_failures += update.num_failures

    def total_ms(self):
        runtimes = [v.total_ms() for v in self.results_per_backend.values() if v.mean_ms]
        return functools.reduce(lambda x, y: x + y, runtimes, 0.0)


@dataclass
class PerBackendError:
    graph_id: int
    error_messages_to_count: Dict[str, int]


@dataclass
class TotalPerBackendResult:
    estimated_total_ms: Optional[float]
    errors: List[PerBackendError]


@dataclass
class Profile:
    segments: Sequence[Segment]
    total_uncompiled_ms: float
    total_per_backend: OrderedDict[str, TotalPerBackendResult]
    compilation_occurred: bool

    def _should_abridge(self, verbose):
        return not verbose and \
               len(self._compiled_segments()) > MAX_COMPILED_SEGMENTS_DISPLAYED_DEFAULT

    def _compiled_segments(self):
        return [s for s in self.segments if s.graph_id is not None]

    def print(self, *, file=sys.stdout, verbose=False):
        abridge = self._should_abridge(verbose)
        self._print_segments(file, abridge=abridge)
        self._print_totals(file, abridge=abridge)
        self._print_errors(file)

    def _print_segments(self, file, abridge):
        if abridge:
            graphs = {}
            for segment in self._compiled_segments():
                gid = segment.graph_id
                if gid not in graphs:
                    graphs[gid] = segment
                else:
                    graphs[gid].add(segment)

            # 'segments' is a bit of a misnomer now, as it contains aggregated
            # segments per graph instead of just individual segments.
            segments = sorted(graphs.values(), key=lambda x: x.total_ms(), reverse=True)
            segments = segments[:MAX_COMPILED_SEGMENTS_DISPLAYED_DEFAULT]
            segment_header = "Top subgraph"
        else:
            segments = self.segments
            segment_header = "Segment"

        table = [
            ("", segment_header, "Runs", "Mean ms", "Failures"),
            "="
        ]
        for segment_idx, segment in enumerate(segments):
            if segment.graph_id is None:
                if self.compilation_occurred:
                    continue
                r = segment.results_per_backend["Uncompiled"]
                table.append((segment_idx, "Uncompiled", r.num_samples, f"{r.mean_ms:.3f}"))
            else:
                table.append('')
                table.append((segment_idx, f"Graph #{segment.graph_id}",))
                for backend, result in segment.results_per_backend.items():
                    mean_ms = "N/A" if result.mean_ms is None else f"{result.mean_ms:.3f}"
                    table.append(("", "  " + backend,
                                  result.num_samples, mean_ms, result.num_failures))
                table.append('')
        table.append('-')
        _print_table(table, "><>>>", file)

    def _print_totals(self, file, abridge):
        if self.compilation_occurred:
            print(f'Total times (compiled + uncompiled) is not available '
                  f'because compilation has occurred.', file=file)
            print(f'Please run the function multiple times to get total '
                  f'times.', file=file)
        else:
            print(f'Total uncompiled code run time: {self.total_uncompiled_ms:.3f} ms', file=file)
            print(f'Total times (compiled + uncompiled) per backend, ms:', file=file)
            table = []
            for backend, total_res in self.total_per_backend.items():
                if total_res.estimated_total_ms is None:
                    estimated_total_ms = "N/A"
                else:
                    estimated_total_ms = f"{total_res.estimated_total_ms:.3f}"
                table.append(("  ", backend, estimated_total_ms))
            table.append('')
            _print_table(table, "<<>", file)

        if abridge:
            print(file=file)
            compiled = self._compiled_segments()
            print(f"{len(set(s.graph_id for s in compiled))} total graphs compiled", file=file)
            print(f"{len(compiled)} total compiled segments run", file=file)

            print(f"More than {MAX_COMPILED_SEGMENTS_DISPLAYED_DEFAULT} compiled segments "
                  "were run, so only graphs with the highest aggregate runtimes are shown. "
                  "To display a verbose profile see "
                  "https://github.com/octoml/octoml-profile#the-profile-report", file=file)
            print(file=file)

    def _print_errors(self, file):
        if any([total.errors for total in self.total_per_backend.values()]):
            print('Errors occurred running this model, per backend:', file=file)
            for backend, total_res in self.total_per_backend.items():
                if not total_res.errors:
                    continue
                print(f'    {backend}', file=file)
                for error in total_res.errors:
                    graph_str = f'       Graph #{error.graph_id} - '
                    print(graph_str, end='', file=file)
                    for i, (error, count) in enumerate(error.error_messages_to_count.items()):
                        if i > 0:
                            print('\n', ' ' * (len(graph_str) - 1), end='', file=file)
                        print(f'{count} errors: {error}', end='', file=file)
                    print(file=file)
            print(f'For full client-side error traces see {LOGFILE}', file=file)


@dataclass
class ProfileReport:
    profiles: List[Profile]
    num_discarded_runs: int
    compile_errors: List[str]

    def print(self, *, file=sys.stdout, verbose=False):
        print(f'Runs discarded because compilation occurred: {self.num_discarded_runs}', file=file)
        if len(self.profiles) == 0:
            print('Profiling was enabled but no results were recorded', file=file)
        for i, profile in enumerate(self.profiles):
            print(f'Profile {i + 1}/{len(self.profiles)}:', file=file)
            profile.print(file=file, verbose=verbose)
        for e in self.compile_errors:
            print("WARNING: " + e, file=file)
        if len(self.compile_errors) > 0:
            print(f"See full client-side trace at {LOGFILE}")


def _string_width(s):
    # FIXME: use wcwidth if we need to display non-latin characters
    return len(str(s))


_align = {
    '<': lambda s, width: s + ' ' * max(0, width - _string_width(s)),
    '>': lambda s, width: ' ' * max(0, width - _string_width(s)) + s
}


def _print_table(rows, column_alignment: str, file):
    col_spacing = 2
    col_spacing_str = ' ' * col_spacing
    num_cols = len(column_alignment)
    column_alignment = tuple(_align[a] for a in column_alignment)

    col_width = [0] * num_cols
    for row in rows:
        if not isinstance(row, str):
            for i, cell in enumerate(row):
                col_width[i] = max(col_width[i], _string_width(cell))

    total_width = sum(col_width) + col_spacing * (num_cols - 1)
    for row in rows:
        if isinstance(row, str):
            num_reps = 1 if _string_width(row) == 0 else total_width // _string_width(row)
            print(row * num_reps, file=file)
        else:
            print(*(align(str(cell), width)
                    for cell, width, align in zip(row, col_width, column_alignment)),
                  file=file,
                  sep=col_spacing_str)
