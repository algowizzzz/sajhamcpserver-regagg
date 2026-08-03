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
