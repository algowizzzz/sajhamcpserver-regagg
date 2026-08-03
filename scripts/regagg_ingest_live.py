#!/usr/bin/env python3
"""
LIVE ingestion across the 30 regulators (real network). Fetches each regulator's
verified sources, samples up to --max-docs documents, normalizes to markdown,
versions them into the corpus, and enriches. Writes into the server's SQLite DB
so the dashboard reflects real pulls.

    python scripts/regagg_ingest_live.py --max-docs 3 --rps 1.0

Polite by design: descriptive User-Agent, per-domain rate limit, sample cap,
resilient (a failed source is skipped, never aborts the regulator). Sources that
did not pass verify_sources simply yield nothing.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sajha.db.base import Base
import sajha.db.models  # noqa: F401
from sajha.core.storage import LocalStorageBackend
from sajha.regagg.config_loader import load_all
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.regagg.enrichment import Enricher, MockLLM, load_taxonomy
from sajha.regagg.fetch import Fetcher, RateLimiter
from sajha.regagg.models import Document, Regulator, Run
from sajha.regagg.pipeline import run_regulator

DB = f"sqlite:///{REPO / 'data' / 'sajha.db'}"
UA = "BMO-RegIntel/1.0 (+regintel-ops@example.com)"


def make_openers(rps: float, timeout: int):
    sess = requests.Session()
    sess.headers["User-Agent"] = UA

    def source_opener(url: str) -> bytes:
        try:
            r = sess.get(url, timeout=timeout, allow_redirects=True)
            return r.content if r.status_code == 200 else b""
        except Exception:  # noqa: BLE001 — a dead source must not abort the run
            return b""

    def doc_opener(url: str):
        r = sess.get(url, timeout=timeout, allow_redirects=True)
        r.raise_for_status()
        return r.content, r.headers.get("Content-Type", ""), r.url

    fetcher = Fetcher(opener=doc_opener, rate_limiter=RateLimiter(rps))
    return source_opener, fetcher


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-docs", type=int, default=3)
    ap.add_argument("--rps", type=float, default=1.0)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--only", help="comma-separated regulator ids")
    args = ap.parse_args()

    engine = create_engine(DB, connect_args={"timeout": 30})  # wait out server write-locks
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    storage = CorpusStorage(LocalStorageBackend(str(REPO)))
    configs = load_all(REPO / "config" / "regulators")
    if args.only:
        want = set(args.only.split(","))
        configs = {k: v for k, v in configs.items() if k in want}

    for cfg in configs.values():
        session.merge(Regulator(regulator_id=cfg.id, name=cfg.name, jurisdiction=cfg.jurisdiction,
                                connector=cfg.connector, config={}, active=cfg.active,
                                staleness_alert_days=cfg.staleness_alert_days))
    session.commit()

    source_opener, fetcher = make_openers(args.rps, args.timeout)
    logical = date.today().isoformat()
    now = datetime.now(timezone.utc)
    totals = {"docs": 0, "errors": 0}

    for cfg in configs.values():
        run_id = f"{logical}_{cfg.id}_live"
        try:
            m = run_regulator(session, storage, cfg, source_opener, fetcher, run_id,
                              logical, trigger="schedule", now=now, max_docs=args.max_docs)
            totals["docs"] += m.ingested
            totals["errors"] += m.errors
            print(f"  {cfg.id:9s} {m.status:14s} detected={m.detected:3d} "
                  f"ingested={m.ingested:2d} errors={m.errors}", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"  {cfg.id:9s} FATAL {e}", flush=True)

    # enrich everything ingested (MockLLM — swap AnthropicBackend when a key is set)
    tax = load_taxonomy(str(REPO / "config" / "regulators" / "_taxonomy.yaml"))
    enr = Enricher(session, storage, MockLLM(), tax)
    enriched = 0
    for doc in session.query(Document).all():
        try:
            enr.enrich_document(doc, default_tags=list(configs.get(doc.regulator_id).default_tags)
                                if doc.regulator_id in configs else [])
            enriched += 1
        except Exception:  # noqa: BLE001
            pass

    print(f"\nLIVE: {session.query(Document).count()} total docs in corpus, "
          f"{totals['docs']} ingested this run, {totals['errors']} fetch errors, "
          f"{enriched} enriched, {session.query(Run).count()} total runs")
    print("dashboard: http://localhost:3002/api/regagg/ui")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
