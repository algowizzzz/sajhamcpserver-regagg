"""Notepad tools — where the worker keeps what it has worked out so far.

The other tools read the corpus. These two are the only ones that write
anything, and what they write is the worker's own reasoning, never collected
data: the notepad lives under `data/notepads/`, nowhere near the archive.

Ownership is not an argument. It is bound per request by the caller
(`notepad.set_owner`), because a model that could name the owner could name
somebody else's.
"""

from __future__ import annotations

from typing import Any, Dict

from sajha.tools.base_mcp_tool import BaseMCPTool


class _NotepadTool(BaseMCPTool):
    def get_input_schema(self) -> Dict:
        cfg = getattr(self, "config", None) or {}
        return cfg.get("inputSchema") or {"type": "object", "properties": {}}

    def get_output_schema(self) -> Dict:
        return {"type": "object"}

    @staticmethod
    def _np():
        from sajha.regagg import notepad
        return notepad


class NotepadWriteTool(_NotepadTool):
    """Record a finding. Appends by default so a long pass cannot erase itself."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        np = self._np()
        return np.write(note=arguments.get("note", ""),
                        section=arguments.get("section") or np.DEFAULT_SECTION,
                        mode=arguments.get("mode", "append"),
                        name=arguments.get("notepad", "scratch"))


class NotepadReadTool(_NotepadTool):
    """Read one section back, or the index when no section is named."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        np = self._np()
        return np.read(section=arguments.get("section"),
                       name=arguments.get("notepad", "scratch"),
                       max_chars=int(arguments.get("max_chars", 40000)),
                       offset=int(arguments.get("offset", 0)))
