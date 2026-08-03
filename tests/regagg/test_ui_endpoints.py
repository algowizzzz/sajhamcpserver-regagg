"""
Phase C — UI data endpoints: /tree, /browse, /changes, /diff, /runs/overview.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from sajha.regagg import runtime
from sajha.regagg.admin import create_admin_router
from sajha.regagg.versioning import CorpusVersioning, IngestInput

REPO = Path(__file__).resolve().parents[2]
NOW = datetime(2026, 8, 2, 6, 0, tzinfo=timezone.utc)


@pytest.fixture()
def client(session, storage, seed_regulator):
    seed_regulator("osfi", "CA", "sitemap_diff")
    seed_regulator("frb", "US", "rss")
    v = CorpusVersioning(session, storage)
    v.ingest(IngestInput(regulator_id="osfi", doc_type="guidance",
                         title="Guideline B-13", content_md="# v1 original cyber",
                         source_url="https://osfi/b13", reference_number="B-13"),
             run_id="r1", now=NOW)
    v.ingest(IngestInput(regulator_id="osfi", doc_type="guidance",
                         title="Guideline B-13", content_md="# v2 REVISED cyber",
                         source_url="https://osfi/b13", reference_number="B-13"),
             run_id="r2", now=NOW)
    v.ingest(IngestInput(regulator_id="frb", doc_type="report",
                         title="Stress test results", content_md="# results",
                         source_url="https://frb/st", source_kind="policy_pdf"),
             run_id="r3", now=NOW)
    runtime.set_providers(session=lambda: session, storage=lambda: storage)
    app = FastAPI()
    app.include_router(create_admin_router())
    yield TestClient(app)
    runtime.set_providers(session=lambda: None)


def test_tree_rollups_and_source_kind_split(client):
    t = client.get("/api/regagg/tree?days=7").json()
    regions = {r["region"]: r for r in t["regions"]}
    assert set(regions) == {"Canada", "United States"}
    osfi = regions["Canada"]["institutions"][0]
    assert osfi["web"]["docs"] == 1 and osfi["pdf"]["docs"] == 0
    frb = regions["United States"]["institutions"][0]
    assert frb["pdf"]["docs"] == 1          # source_kind split works
    assert t["totals"]["documents"] == 2


def test_browse_facets_and_filter(client):
    b = client.get("/api/regagg/browse/osfi").json()
    assert b["total"] == 1
    assert b["facets"]["doc_type"] == {"guidance": 1}
    assert b["documents"][0]["version_n"] == 2
    empty = client.get("/api/regagg/browse/osfi?kind=policy_pdf").json()
    assert empty["documents"] == []
    q = client.get("/api/regagg/browse/osfi?q=B-13").json()
    assert q["documents"]


def test_changes_feed_marks_revision(client):
    c = client.get("/api/regagg/changes?days=7").json()
    kinds = {x["doc"]["doc_id"]: x["kind"] for x in c["changes"]}
    assert kinds["b-13"] == "revised"
    rev = [x for x in c["changes"] if x["doc"]["doc_id"] == "b-13"][0]
    assert rev["has_diff"] is True


def test_version_diff(client):
    d = client.get("/api/regagg/documents/osfi/b-13/diff").json()
    assert d["from_version"] == 1 and d["to_version"] == 2
    assert d["added_lines"] >= 1 and d["removed_lines"] >= 1
    assert "REVISED" in d["diff"] and "original" in d["diff"]
    # single-version doc has no diff
    nd = client.get("/api/regagg/documents/frb/stress-test-results/diff").json()
    assert "error" in nd or nd.get("from_version") is None


def test_runs_overview_shape(client):
    o = client.get("/api/regagg/runs-overview").json()
    assert "active" in o and "recent" in o and "daily_delta" in o


def test_changes_filters(client):
    # region: only Canada -> osfi doc, not the frb one
    ca = client.get("/api/regagg/changes?days=7&region=Canada").json()
    regs = {c["regulator_id"] for c in ca["changes"]}
    assert regs == {"osfi"}
    # institution filter
    frb = client.get("/api/regagg/changes?days=7&regulators=frb").json()
    assert {c["regulator_id"] for c in frb["changes"]} == {"frb"}
    # source_kind filter: only the frb policy_pdf doc qualifies
    pdf = client.get("/api/regagg/changes?days=7&source_kind=policy_pdf").json()
    assert len(pdf["changes"]) == 1
    assert pdf["changes"][0]["doc"]["source_kind"] == "policy_pdf"
    assert pdf["changes"][0]["regulator_id"] == "frb"
    # kind chips: only revisions
    rev = client.get("/api/regagg/changes?days=7&kinds=revised").json()
    assert all(c["kind"] == "revised" for c in rev["changes"])
    assert rev["counts"].get("new", 0) >= 1   # counts stay pre-kind-filter
    # explicit date range excluding everything
    none = client.get(
        "/api/regagg/changes?date_from=2020-01-01&date_to=2020-01-02").json()
    assert none["changes"] == []


def test_doc_content_endpoint(client):
    full = client.get("/api/regagg/documents/osfi/b-13/content?mode=full").json()
    assert "REVISED" in full["content"]
    meta = client.get("/api/regagg/documents/osfi/b-13/content?mode=meta").json()
    assert meta["meta"]["reference_number"] == "B-13"
