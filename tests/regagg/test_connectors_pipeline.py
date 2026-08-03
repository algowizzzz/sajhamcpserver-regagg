"""
Epic 3 — connectors + fetch, and the OSFI end-to-end pipeline (Epic 2 gate:
"OSFI end-to-end; a forced content change correctly archives the old version").

Runs entirely offline against inline fixtures and the *real* repo configs in
config/regulators/.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from sajha.regagg.config_loader import load_one
from sajha.regagg.connectors import get_connector
from sajha.regagg.events import DetectionEvent
from sajha.regagg.fetch import Fetcher, fixture_opener
from sajha.regagg.models import Document, DocumentVersion, Run, SeenUrl
from sajha.regagg.pipeline import build_api_url, run_regulator

REPO = Path(__file__).resolve().parents[2]
CONFIGS = REPO / "config" / "regulators"

T0 = datetime(2026, 7, 5, 6, 0, tzinfo=timezone.utc)
T1 = datetime(2026, 7, 20, 6, 0, tzinfo=timezone.utc)


def _cfg(name):
    return load_one(CONFIGS / f"{name}.yaml")


# ── inline fixtures ─────────────────────────────────────────────────────────

def _sitemap(entries):
    body = "".join(
        f"<url><loc>{u}</loc><lastmod>{lm}</lastmod></url>" for u, lm in entries)
    return (f'<?xml version="1.0"?><urlset '
            f'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>').encode()


def _doc_html(title, body):
    return f"<html><head><title>{title}</title></head><body><main><h1>{title}</h1><p>{body}</p></main></body></html>".encode()


OSFI = "https://www.osfi-bsif.gc.ca"
G_B13 = f"{OSFI}/en/guidance/guideline-b-13"
N_X = f"{OSFI}/en/news/osfi-announces-x"
G_E21 = f"{OSFI}/en/guidance/guideline-e-21"


# ── connector unit tests ────────────────────────────────────────────────────

def test_sitemap_connector_detects_and_maps_doc_type():
    cfg = _cfg("osfi")
    payloads = {
        "sitemap": _sitemap([(G_B13, "2026-07-01"), (N_X, "2026-07-02")]),
        "listings": [f'<a href="{G_E21}">E-21</a>'.encode()],
        "listing_base": f"{OSFI}/en/guidance",
    }
    events = get_connector(cfg, "run1").detect(payloads)
    by_url = {e.url: e for e in events}
    assert set(by_url) == {G_B13, N_X, G_E21}
    assert by_url[G_B13].doc_type_hint == "guidance"     # /guidance/ rule
    assert by_url[N_X].doc_type_hint == "announcement"   # /news/ rule


def test_sitemap_lastmod_fast_path_skips_unchanged():
    cfg = _cfg("osfi")
    seen = {G_B13: "2026-07-01"}  # already seen at this lastmod
    payloads = {"sitemap": _sitemap([(G_B13, "2026-07-01")])}
    events = get_connector(cfg, "r", seen).detect(payloads)
    assert events == []  # not advanced -> skipped


def test_rss_connector_dedups_and_parses(tmp_path):
    cfg = _cfg("frb")
    feed = b"""<?xml version="1.0"?><rss version="2.0"><channel>
      <item><title>SR 26-1</title><link>https://www.federalreserve.gov/srletters/sr2601.htm</link>
        <guid>sr2601</guid><pubDate>Wed, 01 Jul 2026 00:00:00 GMT</pubDate></item>
      <item><title>Press X</title><link>https://www.federalreserve.gov/pressreleases/x.htm</link>
        <guid>pr-x</guid><pubDate>Thu, 02 Jul 2026 00:00:00 GMT</pubDate></item>
      <item><title>Dup</title><link>https://www.federalreserve.gov/srletters/sr2601.htm</link>
        <guid>sr2601</guid></item>
    </channel></rss>"""
    events = get_connector(cfg, "r").detect({"feeds": [feed]})
    urls = [e.url for e in events]
    assert len(urls) == 2  # duplicate guid collapsed
    sr = [e for e in events if "srletters" in e.url][0]
    assert sr.doc_type_hint == "guidance" and sr.title == "SR 26-1"


def test_api_connector_federal_register():
    cfg = _cfg("fedreg")
    assert "conditions[agencies][]" in build_api_url(cfg)
    data = {"results": [
        {"document_number": "2026-100", "title": "Capital Rule",
         "publication_date": "2026-07-01", "type": "RULE",
         "html_url": "https://www.federalregister.gov/d/2026-100"},
        {"document_number": "2026-101", "title": "Proposed X",
         "publication_date": "2026-07-02", "type": "PRORULE",
         "html_url": "https://www.federalregister.gov/d/2026-101"},
    ]}
    events = get_connector(cfg, "r").detect({"api": data})
    kinds = {e.reference_number: e.doc_type_hint for e in events}
    assert kinds == {"2026-100": "final_rule", "2026-101": "consultation"}


# ── OSFI end-to-end pipeline (create -> update -> archive) ───────────────────

@pytest.fixture()
def osfi_openers():
    """Source opener (sitemap+listings) and a doc Fetcher, both from fixtures."""
    def make(sitemap_entries, doc_bodies):
        source_map = {
            f"{OSFI}/sitemap.xml": _sitemap(sitemap_entries),
            f"{OSFI}/en/guidance": b"<html></html>",
            f"{OSFI}/en/news": b"<html></html>",
        }
        source_opener = lambda url: source_map[url]  # noqa: E731
        doc_map = {url: (_doc_html(url.rsplit("/", 1)[-1], body), "text/html")
                   for url, body in doc_bodies.items()}
        return source_opener, Fetcher(fixture_opener(doc_map))
    return make


def test_osfi_end_to_end_create_then_forced_update_archives(session, storage, seed_regulator, osfi_openers):
    cfg = _cfg("osfi")
    seed_regulator("osfi", "CA", "sitemap_diff")

    # Run 1 — two docs, both new
    entries = [(G_B13, "2026-07-01"), (N_X, "2026-07-02")]
    bodies = {G_B13: "B-13 original text", N_X: "news original"}
    src, fetcher = osfi_openers(entries, bodies)
    m1 = run_regulator(session, storage, cfg, src, fetcher,
                       run_id="2026-07-05_osfi_a1", logical_date="2026-07-05", now=T0)
    assert (m1.detected, m1.ingested, m1.archived, m1.errors) == (2, 2, 0, 0)
    assert m1.status == "success"
    assert session.query(Document).count() == 2
    assert session.query(SeenUrl).count() == 2

    # Run 2 — B-13 content changed AND its lastmod advanced -> update + archive
    entries2 = [(G_B13, "2026-07-19"), (N_X, "2026-07-02")]  # N_X unchanged lastmod
    bodies2 = {G_B13: "B-13 REVISED cyber text", N_X: "news original"}
    src2, fetcher2 = osfi_openers(entries2, bodies2)
    m2 = run_regulator(session, storage, cfg, src2, fetcher2,
                       run_id="2026-07-20_osfi_b2", logical_date="2026-07-20", now=T1)
    # Only B-13 gets re-detected (N_X skipped by lastmod fast-path); it's an update.
    assert m2.ingested == 1 and m2.archived == 1 and m2.errors == 0

    from sajha.regagg import ids
    b13_id = ids.stable_doc_id(None, G_B13)  # sitemap has no reference number -> URL-stable id
    b13 = session.get(Document, {"regulator_id": "osfi", "doc_id": b13_id})
    assert b13.version_n == 2 and b13.doc_type == "guidance"
    versions = session.query(DocumentVersion).filter_by(doc_id=b13_id).all()
    states = sorted(v.state for v in versions)
    assert states == ["archived", "current"]
    # current holds revised text; archive holds the original
    cur = [v for v in versions if v.state == "current"][0]
    arch = [v for v in versions if v.state == "archived"][0]
    assert "REVISED" in storage.read_content(b13.s3_prefix)
    assert "original" in storage.read_content(arch.archive_prefix)

    # run rows recorded, manifest persisted to _state
    assert session.query(Run).count() == 2
    manifest_txt = storage.backend.read_text(
        f"{storage.state_prefix('osfi')}/run_manifests/2026-07-20_osfi_b2.json")
    assert json.loads(manifest_txt)["ingested"] == 1


def test_rerun_same_day_is_idempotent(session, storage, seed_regulator, osfi_openers):
    cfg = _cfg("osfi")
    seed_regulator("osfi", "CA", "sitemap_diff")
    entries = [(G_B13, "2026-07-01")]
    bodies = {G_B13: "text"}
    src, fetcher = osfi_openers(entries, bodies)
    run_regulator(session, storage, cfg, src, fetcher, run_id="r1",
                  logical_date="2026-07-05", now=T0)
    # rerun (same logical date, new run id) -> content unchanged -> no new versions
    src2, fetcher2 = osfi_openers(entries, bodies)
    m = run_regulator(session, storage, cfg, src2, fetcher2, run_id="r2",
                      logical_date="2026-07-05", trigger="rerun", now=T1)
    assert m.ingested == 0
    assert session.query(DocumentVersion).count() == 1  # still just v1
