"""
Epic 7 — admin API. Coverage matrix, drill-down, run manifest, rerun (audited),
toggle (audited), review queue, integrity — via FastAPI TestClient.
"""

from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from sajha.db.base import Base
from sajha.db.models import AuditLog  # ensure core audit_log table is available
from sajha.regagg import runtime
from sajha.regagg.admin import create_admin_router
from sajha.regagg.fetch import Fetcher, fixture_opener
from sajha.regagg.config_loader import load_one

REPO = Path(__file__).resolve().parents[2]
CONFIGS = REPO / "config" / "regulators"
NOW = datetime(2026, 7, 10, 6, 0, tzinfo=timezone.utc)
OSFI = "https://www.osfi-bsif.gc.ca"


def _drain(queue, timeout=5.0):
    """A rerun is queued, not run inline — wait for the worker before asserting."""
    import time
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if not queue.snapshot()["active"]:
            return
        time.sleep(0.02)
    raise AssertionError(f"run queue did not drain: {queue.snapshot()}")
G_B13 = f"{OSFI}/en/guidance/guideline-b-13"


def _sitemap(entries):
    body = "".join(f"<url><loc>{u}</loc><lastmod>{lm}</lastmod></url>" for u, lm in entries)
    return (f'<?xml version="1.0"?><urlset '
            f'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>').encode()


def _doc(t, b):
    return (f"<html><head><title>{t}</title></head><body><main><h1>{t}</h1>"
            f"<p>{b}</p></main></body></html>".encode(), "text/html")


@pytest.fixture()
def client(session, storage, seed_regulator):
    # core audit_log lives on the shared Base; create it alongside reg_* tables
    Base.metadata.create_all(session.get_bind(), tables=[AuditLog.__table__])
    seed_regulator("osfi", "CA", "sitemap_diff")

    # produce one run + one document via the pipeline
    from sajha.regagg.orchestrator import run_daily
    cfg = load_one(CONFIGS / "osfi.yaml")
    src = {f"{OSFI}/sitemap.xml": _sitemap([(G_B13, "2026-07-01")]),
           f"{OSFI}/en/guidance": b"<html></html>", f"{OSFI}/en/news": b"<html></html>"}
    # anchor the run to "today" so it falls inside the coverage window
    run_daily(session, storage, {"osfi": cfg},
              lambda c: (lambda u: src[u]),
              lambda c: Fetcher(fixture_opener({G_B13: _doc("B-13", "text")})),
              date.today().isoformat(), now=NOW)

    # stub the rerun trigger so tests never spawn a real ingest subprocess
    runtime.set_providers(session=lambda: session, storage=lambda: storage,
                          rerun_trigger=lambda **kw: {"started": False, "stub": True, **kw})
    app = FastAPI()
    app.include_router(create_admin_router())
    yield TestClient(app)
    runtime.set_providers(session=lambda: None)


def test_coverage_matrix(client):
    r = client.get("/api/regagg/coverage?days=7")
    assert r.status_code == 200
    body = r.json()
    assert len(body["days"]) == 7
    today = date.today().isoformat()
    assert body["matrix"]["osfi"][today]["status"] == "success"


def test_regulator_detail_and_runs(client):
    d = client.get("/api/regagg/regulators/osfi").json()
    assert d["connector"] == "sitemap_diff" and d["latest_documents"]
    runs = client.get("/api/regagg/regulators/osfi/runs").json()["runs"]
    assert runs and runs[0]["status"] == "success"


def test_rerun_is_audited(client):
    r = client.post("/api/regagg/rerun", json={"scope": "ids", "ids": ["osfi"], "date": "2026-07-11"},
                    headers={"X-Operator": "alice"})
    assert r.status_code == 200 and r.json()["operator"] == "alice"
    # audit row written
    session = runtime.get_session()
    from sajha.db.models import AuditLog
    logs = session.query(AuditLog).filter_by(action="regagg.rerun").all()
    assert logs and logs[0].user_id == "alice"


def test_toggle_flips_active_and_audits(client):
    before = client.get("/api/regagg/regulators/osfi").json()["active"]
    r = client.post("/api/regagg/regulators/osfi/toggle", headers={"X-Operator": "bob"})
    assert r.json()["active"] == (not before)
    session = runtime.get_session()
    from sajha.db.models import AuditLog
    assert session.query(AuditLog).filter_by(action="regagg.toggle").count() == 1


def test_integrity_ok(client):
    body = client.get("/api/regagg/integrity").json()
    assert body["ok"] is True and body["invariant_violations"] == []


def test_run_all_on_a_lane_page_runs_only_that_lane(client, session, seed_regulator):
    """The Regulatory page's "Run all" was re-polling the 25 news wires too.

    A button on a lane page reads as lane-scoped; sending scope:"all" with no
    filter made it mean the whole fleet.
    """
    from sajha.regagg.models import Regulator
    seed_regulator("wsj", "US", "sitemap_diff")     # the client fixture seeds osfi
    session.get(Regulator, "wsj").category = "news"
    session.commit()

    seen = {}

    def fake_trigger(**kw):
        seen.update(kw)
        return {"started": True}

    from sajha.regagg import runqueue, runtime
    runtime.set_providers(rerun_trigger=lambda **kw: fake_trigger(**kw))
    try:
        # the response names the sources synchronously; the batch itself runs on
        # the queue's worker, so drain before asserting what the trigger saw
        r = client.post("/api/regagg/rerun", json={"scope": "all", "lane": "regulatory"})
        assert r.status_code == 200
        assert r.json()["queued"] == ["osfi"]           # the wire is not touched
        _drain(runqueue.get_queue())
        assert seen["ids"] == ["osfi"]

        seen.clear()
        r = client.post("/api/regagg/rerun", json={"scope": "all"})
        # no lane: still the whole fleet, but resolved to concrete ids so every
        # source gets a state the page can draw
        assert sorted(r.json()["queued"]) == ["osfi", "wsj"]
        _drain(runqueue.get_queue())
        assert sorted(seen["ids"]) == ["osfi", "wsj"]
    finally:
        runtime.set_providers(rerun_trigger=None)
