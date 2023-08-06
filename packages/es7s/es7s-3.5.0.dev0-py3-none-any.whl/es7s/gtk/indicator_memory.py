# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import random

from pytermor import format_auto_float, format_bytes_human

from ._base import _BaseIndicator, _BoolState, _MenuItemConfig
from ..shared import SocketMessage
from ..shared.dto import MemoryInfo


class IndicatorMemory(_BaseIndicator[MemoryInfo]):
    def __init__(self):
        self._show_perc = _BoolState(value=False)
        self._show_bytes = _BoolState(value=True)

        super().__init__(
            "memory",
            icon_name_default="memory-0",
            icon_path_dynamic_tpl="memory-%d.svg",
            icon_thresholds=[
                95,
                *range(90, 0, -10),
            ],
            label="RAM usage",
        )

    def _init_state(self):
        self._state_map.update({
            _MenuItemConfig("Current (%)"): self._show_perc,
            _MenuItemConfig("Current (kB/MB/GB)"): self._show_bytes,
        })

    def _render(self, msg: SocketMessage[MemoryInfo]):
        virtual_ratio = msg.data.virtual_used / msg.data.virtual_total
        warning = msg.data.swap_used / msg.data.swap_total > 0.70  # @todo
        self._render_result(
            self._format_result(msg.data.virtual_used, msg.data.virtual_total),
            self._format_result(1e10, 1e10),
            warning,
            self._select_icon(100 * virtual_ratio),
        )

    def _format_result(self, used: float, total: float) -> str:
        parts = []
        if self._show_perc:
            parts += [f"{100 * used / total:3.0f}% "]
        if self._show_bytes:
            parts += ["".join(self._format_used_value(round(used)))]
        return " ".join(parts)

    def _format_used_value(self, used: int) -> tuple[str, str]:
        used_kb = used / 1024
        used_mb = used / 1024**2
        used_gb = used / 1024**3
        if used_kb < 1000:
            return format_auto_float(used_kb, 4, False), "k"
        if used_mb < 10000:
            return format_auto_float(used_mb, 4, False), "M"
        return format_auto_float(used_gb, 4, False), "G"
