"""
MCP retrieval tools for the Regulatory Intelligence Aggregator (Feature 7 / Epic 6).

Five stateless, read-only tools registered through the normal SAJHA config-driven
dynamic-discovery path (config/tools/reg_*.json -> these classes). They obtain a
DB session + corpus storage per call via sajha.regagg.runtime, so they hold no
state between invocations.

    reg_search     BM25-style search with SQL pre-filters
    reg_read       document read (summary | full | meta | historical version)
    reg_tags       tag browse with counts + taxonomy category
    reg_whats_new  documents ingested in the last N days, grouped by regulator
    reg_graph      cross-reference graph traversal (depth<=3, cycle-safe)
"""

from __future__ import annotations

from typing import Any, Dict

from sajha.tools.base_mcp_tool import BaseMCPTool
from sajha.regagg import queries, runtime


class _RegToolBase(BaseMCPTool):
    """Shared plumbing: fetch (session, storage) per call from the runtime."""

    def _ctx(self):
        return runtime.get_session(), runtime.get_storage()

    def get_output_schema(self) -> Dict:
        return {"type": "object"}


class RegSearchTool(_RegToolBase):
    def execute(self, arguments: Dict[str, Any]) -> Any:
        session, storage = self._ctx()
        return {"results": queries.reg_search(
            session, storage, arguments.get("query", ""),
            jurisdiction=arguments.get("jurisdiction"),
            regulator_id=arguments.get("regulator_id"),
            doc_type=arguments.get("doc_type"), tags=arguments.get("tags"),
            date_from=arguments.get("date_from"), date_to=arguments.get("date_to"),
            status=arguments.get("status"), limit=int(arguments.get("limit", 10)))}

    def get_input_schema(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Full-text query"},
                "jurisdiction": {"type": "array", "items": {"type": "string"}},
                "regulator_id": {"type": "array", "items": {"type": "string"}},
                "doc_type": {"type": "array", "items": {"type": "string"}},
                "tags": {"type": "array", "items": {"type": "string"}},
                "date_from": {"type": "string", "description": "YYYY-MM-DD"},
                "date_to": {"type": "string", "description": "YYYY-MM-DD"},
                "status": {"type": "array", "items": {"type": "string"}},
                "limit": {"type": "integer", "default": 10},
            },
            "required": ["query"],
        }


class RegReadTool(_RegToolBase):
    def execute(self, arguments: Dict[str, Any]) -> Any:
        session, storage = self._ctx()
        return queries.reg_read(
            session, storage, arguments["doc_id"],
            mode=arguments.get("mode", "summary"),
            regulator_id=arguments.get("regulator_id"),
            version_ts=arguments.get("version_ts"))

    def get_input_schema(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "doc_id": {"type": "string"},
                "regulator_id": {"type": "string", "description": "Disambiguates doc_id"},
                "mode": {"type": "string", "enum": ["summary", "full", "meta"],
                         "default": "summary"},
                "version_ts": {"type": "string", "description": "Read a historical version"},
            },
            "required": ["doc_id"],
        }


class RegTagsTool(_RegToolBase):
    def execute(self, arguments: Dict[str, Any]) -> Any:
        session, _ = self._ctx()
        return {"tags": queries.reg_tags(session, prefix=arguments.get("prefix"),
                                         taxonomy=runtime.get_taxonomy())}

    def get_input_schema(self) -> Dict:
        return {"type": "object",
                "properties": {"prefix": {"type": "string"}}}


class RegWhatsNewTool(_RegToolBase):
    def execute(self, arguments: Dict[str, Any]) -> Any:
        session, _ = self._ctx()
        return queries.reg_whats_new(
            session, days=int(arguments.get("days", 7)),
            jurisdiction=arguments.get("jurisdiction"),
            doc_type=arguments.get("doc_type"),
            deadlines_within=arguments.get("deadlines_within"))

    def get_input_schema(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "days": {"type": "integer", "default": 7},
                "jurisdiction": {"type": "array", "items": {"type": "string"}},
                "doc_type": {"type": "array", "items": {"type": "string"}},
                "deadlines_within": {"type": "integer",
                                     "description": "Only docs with a comment deadline within N days"},
            },
        }


class RegGraphTool(_RegToolBase):
    def execute(self, arguments: Dict[str, Any]) -> Any:
        session, _ = self._ctx()
        return queries.reg_graph(
            session, arguments["doc_id"], edge_types=arguments.get("edge_types"),
            depth=int(arguments.get("depth", 1)), direction=arguments.get("direction", "both"),
            regulator_id=arguments.get("regulator_id"))

    def get_input_schema(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "doc_id": {"type": "string"},
                "regulator_id": {"type": "string"},
                "edge_types": {"type": "array", "items": {"type": "string"}},
                "depth": {"type": "integer", "default": 1, "maximum": 3},
                "direction": {"type": "string", "enum": ["in", "out", "both"],
                              "default": "both"},
            },
            "required": ["doc_id"],
        }
