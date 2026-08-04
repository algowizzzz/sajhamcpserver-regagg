"""
Phase A (data-layer completion): deterministic rules, PDF harvesting,
meta-source dedup, backfill cutoff, source_kind.
"""

from __future__ import annotations

import io
from datetime import date, datetime, timezone
from pathlib import Path

from sajha.regagg import rules
from sajha.regagg.config_loader import load_one
from sajha.regagg.fetch import Fetcher, fixture_opener
from sajha.regagg.models import Document, DocumentEdge, PendingEdge
from sajha.regagg.pipeline import run_regulator
from sajha.regagg.versioning import CorpusVersioning, IngestInput

REPO = Path(__file__).resolve().parents[2]
CONFIGS = REPO / "config" / "regulators"
NOW = datetime(2026, 8, 2, 6, 0, tzinfo=timezone.utc)
OSFI = "https://www.osfi-bsif.gc.ca"


# ── rules: reference extraction ─────────────────────────────────────────────

def test_extract_reference_number_patterns():
    cases = {
        "Guideline B-13: Technology and Cyber Risk": "B-13",
        "CAR Guideline, Chapter 4 — Credit Risk": "CAR-Ch4",
        "SR 26-3: Third-Party Risk Management": "SR 26-3",
        "OCC Bulletin 2026-18: Operational resilience": "2026-18",
        "National Instrument 31-103 amendments": "31-103",
        "APS 220 Credit Risk Management": "APS 220",
        "PS 12/26 — Own funds": "PS 12/26",
        "Plain press release with no id": None,
    }
    for title, want in cases.items():
        assert rules.extract_reference_number(title) == want, title


def test_extract_citations_supersede_vs_reference():
    content = ("This guideline supersedes Guideline B-10 in its entirety. "
               "Institutions should also consult SR 23-4 for interagency context.")
    cits = {c.reference: c.edge_type for c in rules.extract_citations(content)}
    assert cits["B-10"] == "supersedes"
    assert cits["SR 23-4"] == "references"


def test_apply_rules_creates_edges_and_pending(session, storage, seed_regulator):
    seed_regulator("osfi", "CA", "sitemap_diff")
    v = CorpusVersioning(session, storage)
    v.ingest(IngestInput(regulator_id="osfi", doc_type="guidance", title="Guideline B-10 — Outsourcing",
                         content_md="# old", source_url="https://osfi/b10",
                         reference_number="B-10"), run_id="r", now=NOW)
    v.ingest(IngestInput(regulator_id="osfi", doc_type="guidance",
                         title="Guideline B-13: Technology and Cyber Risk",
                         content_md="This supersedes Guideline B-10. See also Guideline E-21.",
                         source_url="https://osfi/b13"), run_id="r", now=NOW)
    doc = session.query(Document).filter_by(regulator_id="osfi").filter(
        Document.title.like("%B-13%")).one()
    rep = rules.apply_rules(session, doc, "This supersedes Guideline B-10. See also Guideline E-21.")
    session.commit()
    assert rep["reference_number"] == "B-13"          # filled from title
    assert rep["edges"] == 1 and rep["pending"] == 1  # B-10 resolved, E-21 pending
    edge = session.query(DocumentEdge).one()
    assert edge.edge_type == "supersedes" and edge.to_doc == "b-10"
    b10 = session.get(Document, {"regulator_id": "osfi", "doc_id": "b-10"})
    assert b10.status == "superseded"
    # resolver: ingest E-21 later, pending edge resolves
    v.ingest(IngestInput(regulator_id="osfi", doc_type="guidance", title="Guideline E-21",
                         content_md="# e21", source_url="https://osfi/e21",
                         reference_number="E-21"), run_id="r", now=NOW)
    assert rules.resolve_pending(session) == 1
    assert session.query(PendingEdge).count() == 0


# ── pipeline: PDF harvest + source_kind ─────────────────────────────────────

def _valid_pdf_bytes() -> bytes:
    import pypdf
    w = pypdf.PdfWriter()
    w.add_blank_page(width=612, height=792)
    buf = io.BytesIO()
    w.write(buf)
    return buf.getvalue()


def test_pdf_harvest_and_source_kind(session, storage, seed_regulator):
    cfg = load_one(CONFIGS / "osfi.yaml")
    seed_regulator("osfi", "CA", "sitemap_diff")
    page = f"{OSFI}/en/guidance/guideline-b-13"
    pdf = f"{OSFI}/docs/b13.pdf"
    html = (f'<html><head><title>B-13</title></head><body><main><h1>B-13</h1>'
            f'<a href="{pdf}">Download PDF</a></main></body></html>').encode()
    sitemap = (f'<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
               f'<url><loc>{page}</loc><lastmod>2026-08-01</lastmod></url></urlset>').encode()
    src = {f"{OSFI}/sitemap.xml": sitemap, f"{OSFI}/en/guidance": b"<html></html>",
           f"{OSFI}/en/news": b"<html></html>"}
    fetcher = Fetcher(fixture_opener({page: (html, "text/html"),
                                      pdf: (_valid_pdf_bytes(), "application/pdf")}))
    m = run_regulator(session, storage, cfg, lambda u: src[u], fetcher,
                      run_id="r1", logical_date="2026-08-02", now=NOW)
    # the HTML page AND its harvested PDF were both ingested
    assert m.ingested == 2 and m.errors == 0
    kinds = {d.source_kind for d in session.query(Document).all()}
    assert kinds == {"web", "policy_pdf"}
    pdf_doc = session.query(Document).filter_by(source_kind="policy_pdf").one()
    assert pdf_doc.ocr is True   # blank page -> no text layer -> flagged


# ── pipeline: meta-source dedup ─────────────────────────────────────────────

def test_meta_source_dedup_skips_agency_duplicates(session, storage, seed_regulator):
    cfg = load_one(CONFIGS / "fedreg.yaml")
    assert cfg.meta_source is True
    seed_regulator("occ", "US", "rss")
    seed_regulator("fedreg", "US", "api")
    # agency (OCC) already holds this reference
    CorpusVersioning(session, storage).ingest(
        IngestInput(regulator_id="occ", doc_type="final_rule", title="Capital rule",
                    content_md="# rule", source_url="https://occ/rule",
                    reference_number="2026-100"), run_id="r", now=NOW)
    api = {"results": [
        {"document_number": "2026-100", "title": "Capital rule",
         "publication_date": "2026-08-01", "type": "RULE",
         "html_url": "https://www.federalregister.gov/d/2026-100"},
        {"document_number": "2026-101", "title": "Fresh rule",
         "publication_date": "2026-08-01", "type": "RULE",
         "html_url": "https://www.federalregister.gov/d/2026-101"},
    ]}
    import json
    src = lambda url: json.dumps(api).encode()  # noqa: E731
    fetcher = Fetcher(fixture_opener({
        "https://www.federalregister.gov/d/2026-101":
            (b"<html><head><title>Fresh rule</title></head><body><main>text</main></body></html>",
             "text/html")}))
    m = run_regulator(session, storage, cfg, src, fetcher, run_id="r2",
                      logical_date="2026-08-02", now=NOW)
    assert m.deduped == 1 and m.ingested == 1     # 2026-100 skipped, 2026-101 ingested
    assert session.query(Document).filter_by(regulator_id="fedreg").count() == 1


# ── connectors: backfill cutoff ─────────────────────────────────────────────

def test_rss_backfill_cutoff_skips_old_items():
    cfg = load_one(CONFIGS / "frb.yaml")   # backfill_cutoff: 2024-08-01
    feed = b"""<?xml version="1.0"?><rss version="2.0"><channel>
      <item><title>Old</title><link>https://www.federalreserve.gov/old.htm</link>
        <pubDate>Wed, 01 Jan 2020 00:00:00 GMT</pubDate></item>
      <item><title>New</title><link>https://www.federalreserve.gov/new.htm</link>
        <pubDate>Wed, 01 Jul 2026 00:00:00 GMT</pubDate></item>
    </channel></rss>"""
    from sajha.regagg.connectors import get_connector
    events = get_connector(cfg, "r").detect({"feeds": [feed]})
    assert [e.title for e in events] == ["New"]


# ── markdown projection (agent-stack consumption layer) ─────────────────────

def test_projection_write_through_and_layout(session, storage, seed_regulator):
    from sajha.regagg import projection
    cfg = load_one(CONFIGS / "osfi.yaml")
    seed_regulator("osfi", "CA", "sitemap_diff")
    page = f"{OSFI}/en/guidance/guideline-b-13"
    pdf = f"{OSFI}/docs/b13.pdf"
    html = (f'<html><head><title>B-13</title></head><body><main><h1>B-13</h1>'
            f'<a href="{pdf}">PDF</a><p>web body</p></main></body></html>').encode()
    sitemap = (f'<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
               f'<url><loc>{page}</loc><lastmod>2026-08-01</lastmod></url></urlset>').encode()
    src = {f"{OSFI}/sitemap.xml": sitemap, f"{OSFI}/en/guidance": b"<html></html>",
           f"{OSFI}/en/news": b"<html></html>"}
    fetcher = Fetcher(fixture_opener({page: (html, "text/html"),
                                      pdf: (_valid_pdf_bytes(), "application/pdf")}))
    run_regulator(session, storage, cfg, lambda u: src[u], fetcher,
                  run_id="r1", logical_date="2026-08-02", now=NOW)
    # web doc landed under markdown/web/..., harvested PDF under markdown/policy/...
    files = storage.backend.list_files("data/markdown", "*.md")
    kinds = {f.split("/")[2] for f in files}
    assert kinds == {"web", "policy"}, files
    web_file = [f for f in files if "/web/osfi/guidance/" in f][0]
    text = storage.backend.read_text(web_file)
    assert text.startswith("---") and 'source_url:' in text and "web body" in text
    # resync is idempotent and covers everything with content
    rep = projection.resync(session, storage)
    assert rep["projected"] >= 1
