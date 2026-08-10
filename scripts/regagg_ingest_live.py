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
    limiter = RateLimiter(rps)

    def source_opener(url: str) -> bytes:
        # Detection went through the same host as the documents but bypassed
        # the limiter entirely: sitemaps and listing pages were fetched back to
        # back at whatever speed the network allowed, which is a large part of
        # why FINRA answered with 429s even after the per-document rate was
        # honoured. A host cannot tell our sitemap request from our document
        # request, and neither should we.
        limiter.wait(url)
        try:
            r = sess.get(url, timeout=timeout, allow_redirects=True)
            return r.content if r.status_code == 200 else b""
        except Exception:  # noqa: BLE001 — a dead source must not abort the run
            return b""

    def doc_opener(url: str):
        r = sess.get(url, timeout=timeout, allow_redirects=True)
        r.raise_for_status()
        return r.content, r.headers.get("Content-Type", ""), r.url

    fetcher = Fetcher(opener=doc_opener, rate_limiter=limiter)
    return source_opener, fetcher, limiter


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-docs", type=int, default=None,
                    help="per-regulator cap (default: uncapped)")
    ap.add_argument("--rps", type=float, default=1.0,
                    help="fleet-wide CEILING on request rate. Each source is "
                         "polled at its own declared rate_limit_rps, or this, "
                         "whichever is slower — a source's politeness setting "
                         "is not something a run may override upward")
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--only", help="comma-separated regulator ids")
    ap.add_argument("--skip", help="comma-separated regulator ids to exclude")
    ap.add_argument("--giants", default="",
                    help="ids run LAST with --giant-cap (huge sitemaps)")
    ap.add_argument("--giant-cap", type=int, default=None,
                    help="max docs for --giants regulators this run")
    ap.add_argument("--include", default="",
                    help="override include_patterns (comma-separated regex) — "
                         "used for targeted gap-fill passes, e.g. '/en/guidance/'")
    ap.add_argument("--operator", default=None, help="audit attribution for the run")
    ap.add_argument("--date", dest="logical_date", default=None,
                    help="logical date to file this run under (default: today). "
                         "Used to backfill a missed day: the documents are whatever "
                         "the source publishes now, but the run closes the gap in "
                         "the coverage matrix. started_at still records the real "
                         "wall-clock time, so the two are never confused.")
    ap.add_argument("--enrich-all", action="store_true",
                    help="re-enrich the whole corpus, not just the sources in this "
                         "run (slow: a full sweep over every document)")
    args = ap.parse_args()

    engine = create_engine(DB, connect_args={"timeout": 30})  # wait out server write-locks
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    storage = CorpusStorage(LocalStorageBackend(str(REPO)))
    configs = load_all(REPO / "config" / "regulators")
    if args.only:
        want = set(args.only.split(","))
        configs = {k: v for k, v in configs.items() if k in want}
    if args.skip:
        skip = set(args.skip.split(","))
        configs = {k: v for k, v in configs.items() if k not in skip}
    # fast regulators first; giants (huge sitemaps) last, optionally capped
    giants = [g for g in (args.giants.split(",") if args.giants else []) if g in configs]
    ordered = ([k for k in configs if k not in giants] + giants)
    configs = {k: configs[k] for k in ordered}
    caps = {k: (args.giant_cap if k in giants else args.max_docs) for k in configs}
    if args.include:  # targeted gap-fill: narrow detection to matching URLs
        pats = args.include.split(",")
        configs = {k: v.model_copy(update={"include_patterns": pats})
                   for k, v in configs.items()}

    for cfg in configs.values():
        session.merge(Regulator(regulator_id=cfg.id, name=cfg.name, jurisdiction=cfg.jurisdiction,
                                connector=cfg.connector, config={}, active=cfg.active,
                                category=getattr(cfg, 'category', 'regulatory'),
                                staleness_alert_days=cfg.staleness_alert_days))
    session.commit()

    source_opener, fetcher, limiter = make_openers(args.rps, args.timeout)
    logical = args.logical_date or date.today().isoformat()
    now = datetime.now(timezone.utc)
    if args.logical_date and args.logical_date != date.today().isoformat():
        print(f"backfill: filing this run under {logical} "
              f"(collected {now:%Y-%m-%d %H:%M} UTC)", flush=True)
    totals = {"docs": 0, "errors": 0}

    for cfg in configs.values():
        # Politeness is declared per source and must be honoured. This used to
        # poll every source at one global --rps: FINRA declares 0.5 and was
        # being hit at 3, which earned 141 consecutive HTTP 429s and a failed
        # run. --rps is a ceiling now, never a licence to go faster.
        effective_rps = min(cfg.rate_limit_rps, args.rps)
        limiter.set_rate(effective_rps)
        if effective_rps < args.rps:
            print(f"  {cfg.id:9s} rate {effective_rps} rps (its own limit, "
                  f"below the --rps {args.rps} ceiling)", flush=True)

        # distinct run_id per UI-triggered rerun so history rows aren't merged
        suffix = f"ui{now:%H%M%S}" if args.operator else "live"
        run_id = f"{logical}_{cfg.id}_{suffix}"
        try:
            m = run_regulator(session, storage, cfg, source_opener, fetcher, run_id,
                              logical, trigger="rerun" if args.operator else "schedule",
                              operator=args.operator, now=now, max_docs=caps[cfg.id])
            totals["docs"] += m.ingested
            totals["errors"] += m.errors
            print(f"  {cfg.id:9s} {m.status:14s} detected={m.detected:3d} "
                  f"ingested={m.ingested:2d} errors={m.errors}", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"  {cfg.id:9s} FATAL {e}", flush=True)

    # Enrich the sources this run touched (MockLLM — swap AnthropicBackend when a
    # key is set). This used to sweep `Document.all()` regardless of scope, so
    # rerunning ONE source re-enriched all 7,400 documents and took ~6 minutes;
    # it is also why concurrent runs were unsafe. --enrich-all restores the sweep.
    tax = load_taxonomy(str(REPO / "config" / "regulators" / "_taxonomy.yaml"))
    enr = Enricher(session, storage, MockLLM(), tax)
    enriched = 0
    q = session.query(Document)
    if not args.enrich_all:
        q = q.filter(Document.regulator_id.in_(list(configs.keys())))
    for doc in q.all():
        try:
            enr.enrich_document(doc, default_tags=list(configs.get(doc.regulator_id).default_tags)
                                if doc.regulator_id in configs else [])
            enriched += 1
        except Exception:  # noqa: BLE001
            pass

    scope = "whole corpus" if args.enrich_all else f"{len(configs)} source(s) in this run"
    print(f"\nLIVE: {session.query(Document).count()} total docs in corpus, "
          f"{totals['docs']} ingested this run, {totals['errors']} fetch errors, "
          f"{enriched} enriched ({scope}), {session.query(Run).count()} total runs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
