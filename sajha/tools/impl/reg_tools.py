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


class RegCoverageTool(_RegToolBase):
    """Coverage tree: regions -> institutions with doc counts (web/PDF), new-in-window,
    freshness/staleness, last run, and coverage %. The trust map of the corpus."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        from sajha.regagg import queries_ui
        session, _ = self._ctx()
        return queries_ui.coverage_tree(session, days=int(arguments.get("days", 7)))

    def get_input_schema(self) -> Dict:
        return {"type": "object",
                "properties": {"days": {"type": "integer", "default": 7}}}


class RegBrowseTool(_RegToolBase):
    """Metadata listing of the corpus (NO content — pair with your own RAG for text):
    filter by continent/region, institution, file type, doc_type, status, date, text
    on title/reference. Returns facet counts + document metadata rows."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        from sajha.regagg import queries_ui
        session, _ = self._ctx()
        return queries_ui.corpus_browse(
            session, region=arguments.get("region"),
            regulator_ids=arguments.get("regulator_id"),
            kind=arguments.get("source_kind"), doc_type=arguments.get("doc_type"),
            status=arguments.get("status"), q=arguments.get("q"),
            date_from=arguments.get("date_from"), date_to=arguments.get("date_to"),
            limit=min(int(arguments.get("limit", 50)), 200),
            offset=int(arguments.get("offset", 0)))

    def get_input_schema(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "region": {"type": "string",
                           "enum": ["Canada", "United States", "EU & UK", "APAC", "International"]},
                "regulator_id": {"type": "array", "items": {"type": "string"}},
                "source_kind": {"type": "string", "enum": ["web", "policy_pdf"]},
                "doc_type": {"type": "string"},
                "status": {"type": "string",
                           "enum": ["proposed", "final", "superseded", "withdrawn"]},
                "q": {"type": "string", "description": "title/reference contains"},
                "date_from": {"type": "string"}, "date_to": {"type": "string"},
                "limit": {"type": "integer", "default": 50},
                "offset": {"type": "integer", "default": 0},
            },
        }


class RegChangesTool(_RegToolBase):
    """Delta feed: new / revised / superseded documents and upcoming comment
    deadlines in a window, filterable by region, institution, file type, dates."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        from sajha.regagg import queries_ui
        session, _ = self._ctx()
        return queries_ui.changes(
            session, days=int(arguments.get("days", 7)),
            region=arguments.get("region"),
            regulator_ids=arguments.get("regulator_id"),
            source_kind=arguments.get("source_kind"),
            kinds=arguments.get("kinds"),
            date_from=arguments.get("date_from"), date_to=arguments.get("date_to"))

    def get_input_schema(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "days": {"type": "integer", "default": 7},
                "region": {"type": "string"},
                "regulator_id": {"type": "array", "items": {"type": "string"}},
                "source_kind": {"type": "string", "enum": ["web", "policy_pdf"]},
                "kinds": {"type": "array", "items": {
                    "type": "string", "enum": ["new", "revised", "superseded", "deadline"]}},
                "date_from": {"type": "string"}, "date_to": {"type": "string"},
            },
        }


class RegDiffTool(_RegToolBase):
    """Unified diff between a document's current and previous archived version —
    'what exactly changed', line by line, with added/removed counts."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        from sajha.regagg import queries_ui
        session, storage = self._ctx()
        return queries_ui.version_diff(session, storage,
                                       arguments["regulator_id"], arguments["doc_id"])

    def get_input_schema(self) -> Dict:
        return {"type": "object",
                "properties": {"regulator_id": {"type": "string"},
                               "doc_id": {"type": "string"}},
                "required": ["regulator_id", "doc_id"]}


class RegInventoryTool(_RegToolBase):
    """Expected-inventory reconciliation: does the corpus hold every item the
    regulator's official index says should exist (e.g. all 9 OSFI CAR chapters)?
    Returns per-series present/missing."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        from sajha.regagg import queries_ui
        session, _ = self._ctx()
        return queries_ui.inventory(session, arguments["regulator_id"])

    def get_input_schema(self) -> Dict:
        return {"type": "object",
                "properties": {"regulator_id": {"type": "string"}},
                "required": ["regulator_id"]}


class RegRunsStatusTool(_RegToolBase):
    """Collection health: active runs with live counters, recent run history,
    daily delta (new/archived/errors + pass rate) and today's failing runs."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        from sajha.regagg import queries_ui
        session, _ = self._ctx()
        return queries_ui.runs_overview(session)

    def get_input_schema(self) -> Dict:
        return {"type": "object", "properties": {}}


class RegTriggerRunTool(_RegToolBase):
    """Trigger a collection run (all regulators or a subset). Spawns the same
    audited ingest as the UI Run buttons; refuses if a run is already active.
    MUTATING — disable in config/tools/reg_trigger_run.json or exclude it from
    an agent's key scope if agents must stay read-only."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        from sajha.regagg import runtime as _rt
        ids_ = arguments.get("regulator_id")
        return _rt.get_rerun_trigger()(
            scope="ids" if ids_ else "all", logical_date=None, ids=ids_,
            operator=arguments.get("operator", "mcp-agent"),
            max_docs=arguments.get("max_docs"), include=arguments.get("include"))

    def get_input_schema(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "regulator_id": {"type": "array", "items": {"type": "string"},
                                 "description": "omit = all active regulators"},
                "max_docs": {"type": "integer"},
                "include": {"type": "string",
                            "description": "URL regex scope (targeted gap-fill)"},
                "operator": {"type": "string", "default": "mcp-agent"},
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
