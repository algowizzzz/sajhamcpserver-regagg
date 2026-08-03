#!/usr/bin/env python3
"""
Seed DEMO data for the regagg dashboard (offline fixtures — NOT live regulator
pulls). Populates the server's SQLite DB + local corpus so /api/regagg/ui shows a
real coverage matrix, documents, versions, and enrichment.

    python scripts/regagg_seed_demo.py

Safe to re-run (idempotent-ish: unchanged docs are skipped by the versioning
layer). Uses 6 BMO-relevant regulators over 3 days to exercise green / yellow /
red / update+archive cells.
"""

from __future__ import annotations

import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sajha.db.base import Base
import sajha.db.models  # noqa: F401 - registers all tables incl reg_*
from sajha.core.storage import LocalStorageBackend
from sajha.regagg.config_loader import load_one
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.regagg.enrichment import Enricher, MockLLM, load_taxonomy
from sajha.regagg.fetch import Fetcher, fixture_opener
from sajha.regagg.models import Document, Regulator
from sajha.regagg.orchestrator import run_daily

DB = f"sqlite:///{REPO / 'data' / 'sajha.db'}"
TAX = load_taxonomy(str(REPO / "config" / "regulators" / "_taxonomy.yaml"))

TODAY = date.today()
D = {i: (TODAY - timedelta(days=i)).isoformat() for i in range(3)}  # D[2],D[1],D[0]

# (regulator_id, base_url, [(path, title, markers)])
SEED = {
    "osfi": ("https://www.osfi-bsif.gc.ca", [
        ("/en/guidance/b-13-cyber", "Guideline B-13: Technology and Cyber Risk",
         "TYPE:guidance STATUS:final PUBLISHED:{pub} EFFECTIVE:2027-01-01 cyber capital"),
        ("/en/news/osfi-consults-climate", "OSFI consults on climate risk",
         "TYPE:consultation STATUS:proposed PUBLISHED:{pub} DEADLINE:2026-10-01 climate"),
    ]),
    "boc": ("https://www.bankofcanada.ca", [
        ("/press-releases/rate-decision", "Bank of Canada rate decision",
         "TYPE:announcement STATUS:final PUBLISHED:{pub} liquidity"),
    ]),
    "frb": ("https://www.federalreserve.gov", [
        ("/srletters/sr26-3", "SR 26-3: Third-party risk management",
         "TYPE:guidance STATUS:final PUBLISHED:{pub} REF:interprets:B-13 aml"),
        ("/pressreleases/enforce-x", "Enforcement action against Bank X",
         "TYPE:enforcement STATUS:final PUBLISHED:{pub} aml"),
    ]),
    "occ": ("https://www.occ.gov", [
        ("/news/bulletin-2026-18", "OCC Bulletin 2026-18: Operational resilience",
         "TYPE:guidance STATUS:final PUBLISHED:{pub} operational"),
    ]),
    "sec": ("https://www.sec.gov", [
        ("/rules/final/cyber-disclosure", "Final rule: Cybersecurity disclosure",
         "TYPE:final_rule STATUS:final PUBLISHED:{pub} cyber disclosure"),
    ]),
    "ecb_ssm": ("https://www.bankingsupervision.europa.eu", [
        ("/press/guidance-crypto", "ECB guidance on crypto-asset exposures",
         "TYPE:guidance STATUS:final PUBLISHED:{pub} crypto"),
    ]),
}


def doc_html(title, markers, pub):
    body = markers.format(pub=pub)
    return (f"<html><head><title>{title}</title></head><body><main>"
            f"<h1>{title}</h1><p>{body}</p></main></body></html>".encode(), "text/html")


def build_openers(cfg, base, specs, pub, lastmod, changed_suffix=""):
    urls = [base + p for (p, _t, _m) in specs]
    doc_map = {u: doc_html(t, m + changed_suffix, pub) for u, (_p, t, m) in zip(urls, specs)}
    if cfg.connector == "sitemap_diff":
        sm = ('<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
              + "".join(f"<url><loc>{u}</loc><lastmod>{lastmod}</lastmod></url>" for u in urls)
              + "</urlset>").encode()
        src = {cfg.sources.sitemap.url: sm}
        for lp in cfg.sources.listing_pages:
            src[lp.url] = b"<html></html>"
    else:  # rss
        items = "".join(
            f"<item><title>{t}</title><link>{u}</link><guid>{u}</guid>"
            f"<pubDate>{pub}T00:00:00Z</pubDate></item>"
            for u, (_p, t, _m) in zip(urls, specs))
        feed = (f'<?xml version="1.0"?><rss version="2.0"><channel>{items}</channel></rss>').encode()
        src = {f.url: feed for f in cfg.sources.feeds}
    return (lambda url: src[url]), Fetcher(fixture_opener(doc_map))


def main() -> int:
    engine = create_engine(DB)
    Base.metadata.create_all(engine)   # ensure reg_* tables exist
    S = sessionmaker(bind=engine, expire_on_commit=False)
    session = S()
    storage = CorpusStorage(LocalStorageBackend(str(REPO)))
    configs = {rid: load_one(REPO / "config" / "regulators" / f"{rid}.yaml") for rid in SEED}

    # upsert regulator rows
    for rid, cfg in configs.items():
        session.merge(Regulator(regulator_id=rid, name=cfg.name, jurisdiction=cfg.jurisdiction,
                                connector=cfg.connector, config={}, active=True,
                                staleness_alert_days=cfg.staleness_alert_days))
    session.commit()

    def run(rids, logical, pub, lastmod, changed="", now=None):
        for rid in rids:
            cfg = configs[rid]
            base, specs = SEED[rid]
            src, fetch = build_openers(cfg, base, specs, pub, lastmod, changed)
            run_daily(session, storage, {rid: cfg}, lambda c: src, lambda c: fetch,
                      logical, now=now or datetime.now(timezone.utc))

    # Day -2: everyone ingests fresh (green)
    run(SEED.keys(), D[2], pub=D[2], lastmod=D[2])
    # Day -1: OSFI B-13 revised (update+archive, green); others unchanged (yellow); OCC "fails"
    run(["osfi"], D[1], pub=D[1], lastmod=D[1], changed=" REVISED third-party")
    run(["boc", "frb", "sec", "ecb_ssm"], D[1], pub=D[2], lastmod=D[2])  # same lastmod -> 0 new
    _fail_run(session, "occ", D[1])
    # Day 0: SEC posts a new doc (green); rest unchanged (yellow)
    run(["sec"], D[0], pub=D[0], lastmod=D[0], changed=" amended")
    run(["osfi", "boc", "frb", "occ", "ecb_ssm"], D[0], pub=D[2], lastmod=D[2])

    # enrich everything
    enr = Enricher(session, storage, MockLLM(), TAX)
    for doc in session.query(Document).all():
        enr.enrich_document(doc, default_tags=list(configs[doc.regulator_id].default_tags))

    n_docs = session.query(Document).count()
    from sajha.regagg.models import Run, DocumentEdge
    print(f"seeded: {len(SEED)} regulators, {session.query(Run).count()} runs, "
          f"{n_docs} documents, {session.query(DocumentEdge).count()} graph edges")
    print("open the dashboard at  http://localhost:3002/api/regagg/ui")
    return 0


def _fail_run(session, rid, logical):
    """Record a failed run row so the matrix shows a red cell."""
    from sajha.regagg.models import Run
    from sajha.regagg import ids
    run_id = ids.make_run_id(logical, rid, ids.short_hash(logical + rid, 4))
    session.merge(Run(run_id=run_id, regulator_id=rid, logical_date=date.fromisoformat(logical),
                      trigger="schedule", status="failed", detected=3, fetched=1, errors=2,
                      started_at=datetime.now(timezone.utc), finished_at=datetime.now(timezone.utc)))
    session.commit()


if __name__ == "__main__":
    raise SystemExit(main())
