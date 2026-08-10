"""
Epic 6 — MCP retrieval tools. Exercises the actual tool classes (execute +
schemas) against a seeded corpus, wired via runtime.set_providers, and confirms
the generated config/tools/reg_*.json are valid & discoverable.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from sajha.regagg import runtime
from sajha.regagg.enrichment import Enricher, MockLLM, load_taxonomy
from sajha.regagg.versioning import CorpusVersioning, IngestInput
from sajha.tools.impl.reg_tools import (
    RegGraphTool, RegReadTool, RegSearchTool, RegTagsTool, RegWhatsNewTool,
)

REPO = Path(__file__).resolve().parents[2]
TAXONOMY = str(REPO / "config" / "regulators" / "_taxonomy.yaml")
NOW = datetime(2026, 7, 20, 6, 0, tzinfo=timezone.utc)


@pytest.fixture()
def corpus(session, storage, seed_regulator):
    """Seed two enriched, cross-referenced documents and wire the runtime."""
    seed_regulator("osfi", "CA", "sitemap_diff")
    v = CorpusVersioning(session, storage)
    v.ingest(IngestInput(regulator_id="osfi", doc_type="guidance", title="Guideline B-10",
                         content_md="# B-10\nold liquidity guidance", source_url="https://osfi/b-10",
                         reference_number="B-10"), run_id="r", now=NOW - timedelta(days=1))
    v.ingest(IngestInput(regulator_id="osfi", doc_type="guidance",
                         title="Guideline B-13 Cyber Risk",
                         content_md="# B-13\nTYPE:guidance STATUS:final PUBLISHED:2026-07-20 "
                                     "REF:supersedes:B-10 cyber risk management",
                         source_url="https://osfi/b-13", reference_number="B-13",
                         tags=["canada", "banking"]), run_id="r", now=NOW)
    tax = load_taxonomy(TAXONOMY)
    from sajha.regagg.models import Document
    for did in ("b-10", "b-13"):
        doc = session.get(Document, {"regulator_id": "osfi", "doc_id": did})
        Enricher(session, storage, MockLLM(), tax).enrich_document(
            doc, default_tags=["canada", "banking"])

    runtime.set_providers(session=lambda: session,
                          storage=lambda: storage,
                          taxonomy=tax)
    yield
    runtime.set_providers(session=lambda: None)  # reset


def test_reg_search_ranks_and_filters(corpus):
    out = RegSearchTool(config={"name": "reg_search"}).execute({"query": "cyber"})
    assert out["results"] and out["results"][0]["doc_id"] == "b-13"
    assert out["results"][0]["snippet"]
    # tag filter narrows the set
    only_canada = RegSearchTool(config={"name": "reg_search"}).execute(
        {"query": "guidance", "tags": ["canada"]})
    assert all("b-1" in r["doc_id"] for r in only_canada["results"])


def test_reg_read_modes_and_version(corpus):
    t = RegReadTool(config={"name": "reg_read"})
    summ = t.execute({"doc_id": "b-13", "regulator_id": "osfi", "mode": "summary"})
    assert "Summary:" in summ["content"]
    full = t.execute({"doc_id": "b-13", "regulator_id": "osfi", "mode": "full"})
    assert "cyber" in full["content"]
    meta = t.execute({"doc_id": "b-13", "regulator_id": "osfi", "mode": "meta"})
    assert meta["meta"]["reference_number"] == "B-13"


def test_reg_tags_counts_and_category(corpus):
    tags = RegTagsTool(config={"name": "reg_tags"}).execute({})["tags"]
    by = {t["tag"]: t for t in tags}
    assert by["cyber_risk"]["category"] == "topic"
    assert by["canada"]["category"] == "jurisdiction"


def test_reg_whats_new_window(corpus):
    out = RegWhatsNewTool(config={"name": "reg_whats_new"}).execute({"days": 2})
    # only b-13 ingested "now"; b-10 ingested a day earlier still within 2 days
    assert out["count"] >= 1 and "osfi" in out["by_regulator"]


def test_reg_graph_traverses_supersedes(corpus):
    out = RegGraphTool(config={"name": "reg_graph"}).execute(
        {"doc_id": "b-13", "regulator_id": "osfi", "direction": "out", "depth": 2})
    assert "osfi/b-10" in out["nodes"]
    assert any(e["type"] == "supersedes" for e in out["edges"])


def test_generated_tool_configs_are_valid():
    for name in ("reg_search", "reg_read", "reg_tags", "reg_whats_new", "reg_graph"):
        cfg = json.loads((REPO / "config" / "tools" / f"{name}.json").read_text())
        assert cfg["name"] == name
        assert cfg["implementation"].startswith("sajha.tools.impl.reg_tools.")
        assert cfg["inputSchema"]["type"] == "object"
        assert cfg["metadata"]["readOnly"] is True


def test_index_plane_tools(corpus, session):
    """The non-content MCP tools: coverage, browse, changes, diff, inventory, runs."""
    from sajha.tools.impl.reg_tools import (
        RegBrowseTool, RegChangesTool, RegCoverageTool, RegDiffTool,
        RegInventoryTool, RegRunsStatusTool)
    cov = RegCoverageTool(config={"name": "reg_coverage"}).execute({"days": 7})
    assert cov["totals"]["documents"] == 2 and cov["regions"]
    br = RegBrowseTool(config={"name": "reg_browse"}).execute(
        {"regulator_id": ["osfi"], "q": "B-13"})
    assert br["total"] >= 1 and br["facets"]["doc_type"]
    ch = RegChangesTool(config={"name": "reg_changes"}).execute({"days": 7})
    assert ch["changes"]
    # b-13 has a supersedes -> b-10 (v1 only), so diff b-13? b-13 is v1 here; expect error dict
    df = RegDiffTool(config={"name": "reg_diff"}).execute(
        {"regulator_id": "osfi", "doc_id": "b-13"})
    assert "error" in df or "diff" in df
    inv = RegInventoryTool(config={"name": "reg_inventory"}).execute(
        {"regulator_id": "osfi"})
    assert inv["available"] is True
    rs = RegRunsStatusTool(config={"name": "reg_runs_status"}).execute({})
    assert "daily_delta" in rs and "active" in rs


def test_trigger_tool_uses_runtime_trigger(corpus):
    from sajha.regagg import runtime
    from sajha.tools.impl.reg_tools import RegTriggerRunTool
    calls = {}
    runtime.set_providers(rerun_trigger=lambda **kw: calls.update(kw) or {"started": False, "stub": True})
    out = RegTriggerRunTool(config={"name": "reg_trigger_run"}).execute(
        {"regulator_id": ["osfi"], "max_docs": 5})
    assert out["stub"] and calls["ids"] == ["osfi"] and calls["max_docs"] == 5


def test_corpus_changes_honours_the_source_filter(corpus, seed_regulator, session, storage):
    """A source filter that does nothing turns a wrong answer into an empty one.

    The agent asked corpus_changes for OSFI and got fedreg and news items back,
    then had to reconstruct the answer by hand and say so. An ignored filter is
    worse than a missing one: the caller believes the result is scoped.
    """
    from sajha.tools.impl.corpus_tools import CorpusChangesTool

    seed_regulator("fedreg", "US", "sitemap_diff")
    CorpusVersioning(session, storage).ingest(
        IngestInput(regulator_id="fedreg", doc_type="final_rule", title="A US rule",
                    content_md="# rule\nunrelated", source_url="https://fedreg/1"),
        run_id="r", now=NOW)

    tool = CorpusChangesTool(config={"name": "corpus_changes"})
    everything = tool.execute({"days": 30})
    assert {c["regulator_id"] for c in everything["changes"]} >= {"osfi", "fedreg"}

    scoped = tool.execute({"days": 30, "source": "osfi"})
    assert scoped["changes"], "OSFI has changes in the window"
    assert {c["regulator_id"] for c in scoped["changes"]} == {"osfi"}
    assert scoped["source"] == ["osfi"]

    # a list of sources works, and an unknown source returns nothing, not everything
    both = tool.execute({"days": 30, "source": ["osfi", "fedreg"]})
    assert {c["regulator_id"] for c in both["changes"]} == {"osfi", "fedreg"}
    assert tool.execute({"days": 30, "source": "nosuchsource"})["changes"] == []


def test_corpus_changes_advertises_the_source_filter():
    """The model can only use a filter the schema tells it about."""
    cfg = json.loads(Path("config/tools/corpus_changes.json").read_text())
    assert "source" in cfg["inputSchema"]["properties"]


def test_an_argument_the_tool_does_not_implement_is_rejected_not_ignored():
    """The mechanism that should have caught the corpus_changes bug.

    corpus_changes accepted `source` and ignored it. The worker asked for OSFI,
    got fedreg and news back, and only noticed because it happened to read the
    results closely. Validation is driven by each tool's own schema, so the
    guard covers every tool without per-tool code.
    """
    from sajha.tools.impl.corpus_tools import CorpusStatsTool

    schema = {"type": "object", "properties": {"days": {"type": "integer"}}}
    tool = CorpusStatsTool(config={"name": "corpus_stats", "inputSchema": schema})

    tool.validate_arguments({"days": 7})  # declared — fine

    with pytest.raises(ValueError) as e:
        tool.validate_arguments({"days": 7, "source": "osfi"})
    msg = str(e.value)
    assert "source" in msg                      # names what was wrong
    assert "days" in msg                        # and what it could have used
    assert "ignored" in msg.lower()             # and why it matters


def test_a_schema_may_opt_out_of_strictness():
    """Strictness is configuration, not a rule hard-coded in the base class."""
    from sajha.tools.impl.corpus_tools import CorpusStatsTool

    open_schema = {"type": "object", "properties": {"days": {"type": "integer"}},
                   "additionalProperties": True}
    tool = CorpusStatsTool(config={"name": "corpus_stats", "inputSchema": open_schema})
    assert tool.validate_arguments({"days": 7, "anything": 1}) is True


def test_the_agent_surfaces_a_rejected_argument_to_the_model():
    """A rejection the model never sees is the same as a silent drop."""
    from sajha.regagg import agent

    out = agent._run_tool("corpus_read", {"source": "osfi"})
    assert out.get("arguments_rejected") is True
    assert "source" in out["error"] and "doc_id" in out["error"]


def test_every_tool_the_agent_asks_for_can_actually_be_instantiated():
    """A config file is not proof the tool loads.

    Two notepad tools shipped with a config, a valid schema and passing unit
    tests, and were rejected at startup — the base class has an abstract
    `get_output_schema` neither implemented. The registry logged it and carried
    on, so the agent simply had a smaller toolset than its prompt described.
    Nothing failed; a capability was quietly absent.
    """
    import importlib

    from sajha.regagg.agent import DEFAULT_TOOLSET

    broken = {}
    for name in DEFAULT_TOOLSET:
        cfg_path = Path(f"config/tools/{name}.json")
        if not cfg_path.exists():
            broken[name] = "no config file — it would not be registered at all"
            continue
        cfg = json.loads(cfg_path.read_text())
        dotted = cfg.get("implementation", "")
        mod, _, cls = dotted.rpartition(".")
        try:
            tool = getattr(importlib.import_module(mod), cls)()
            tool.get_input_schema()
            tool.get_output_schema()
        except Exception as e:  # noqa: BLE001
            broken[name] = f"{type(e).__name__}: {e}"
    assert not broken, f"tools the agent expects but cannot load: {broken}"


def test_every_configured_tool_declares_the_parameters_it_accepts():
    """A schema with no properties cannot reject anything — the same hole."""
    import glob
    open_tools = []
    for f in sorted(glob.glob("config/tools/*.json")):
        cfg = json.loads(Path(f).read_text())
        schema = cfg.get("inputSchema") or {}
        # `{}` is a real contract ("takes nothing"); a missing key is not
        if schema.get("properties") is None and schema.get("type") == "object":
            open_tools.append(cfg.get("name") or Path(f).stem)
    assert not open_tools, (
        f"these tools accept anything and can silently drop filters: {open_tools}"
    )


def test_corpus_schemas_declare_the_filters_their_search_paths_apply():
    """The two contracts must not drift apart in either direction.

    A filter the code applies but the schema hides is a capability nobody can
    reach; a filter the schema promises but the code ignores is the bug that
    started this. corpus_search_* pass **self._filters(arguments) straight into
    the index, so everything _filters reads has to be declared.

    corpus_changes is deliberately excluded: it only reaches _filters on its
    fallback path, so declaring those keys would promise filtering that does
    not happen on the normal path.
    """
    import glob
    import re

    src = Path("sajha/tools/impl/corpus_tools.py").read_text()
    filter_keys = set(re.findall(r'a\.get\("([a-z_]+)"\)', src.split("def _filters")[1]
                                 .split("class ")[0]))
    filter_keys |= set(re.findall(r'for k in \("([^)]+)"\)',
                                  src.split("def _filters")[1].split("class ")[0])[0]
                       .replace('"', "").split(", ")) if "for k in (" in src else set()
    assert {"source", "doc_type", "stage", "date_from", "date_to"} <= filter_keys

    cfgs = {}
    for f in glob.glob("config/tools/*.json"):
        c = json.loads(Path(f).read_text())
        cfgs[c["implementation"].rsplit(".", 1)[-1]] = c

    gaps = {}
    for cls in ("CorpusKeywordSearchTool", "CorpusBM25SearchTool", "CorpusSimilarTool"):
        declared = set((cfgs[cls].get("inputSchema") or {}).get("properties") or {})
        missing = sorted(filter_keys - declared)
        if missing:
            gaps[cfgs[cls]["name"]] = missing
    assert not gaps, f"implemented but undeclared filters (unreachable): {gaps}"
