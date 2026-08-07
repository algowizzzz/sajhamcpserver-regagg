#!/usr/bin/env python3
"""
Run the configured extractor over documents that have none yet.

Extraction happens at ingest going forward; this backfills a corpus collected
before the extractor existed (or re-runs it after a model change). Concurrent
because each document is independent and the call is short.

    python scripts/regagg_extract_backfill.py --lane news --workers 8
"""
from __future__ import annotations

import argparse
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sqlalchemy import select                              # noqa: E402
from sqlalchemy.orm import sessionmaker                    # noqa: E402

from sajha.core.config import get_settings                 # noqa: E402
from sajha.db.engine import get_engine, init_db            # noqa: E402
from sajha.regagg import extraction as X                   # noqa: E402
from sajha.regagg.models import Document, Regulator        # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=("news", "regulatory", "all"), default="all")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--redo", action="store_true", help="re-extract existing rows")
    args = ap.parse_args()

    init_db(get_settings())
    engine = get_engine()
    session = sessionmaker(bind=engine, expire_on_commit=False)()

    extractor = X.get_extractor(X.build_index_from_watchlists(session))
    print(f"extractor: {extractor.backend} ({getattr(extractor, 'version', '')})")

    regs = {r.regulator_id: r for r in session.scalars(select(Regulator)).all()}
    ids = [rid for rid, r in regs.items()
           if args.lane == "all"
           or getattr(r, "category", "regulatory") == args.lane]
    docs = session.scalars(select(Document).where(
        Document.regulator_id.in_(ids or [""]))).all()
    todo = [d for d in docs if args.redo or not (d.extraction or {}).get("event_type")]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(todo):,} document(s) to extract of {len(docs):,}")
    if not todo:
        return 0

    start = time.time()
    results = {}

    def work(doc):
        try:
            return doc.regulator_id, doc.doc_id, extractor.extract(doc.title or "", "")
        except Exception as e:  # noqa: BLE001
            return doc.regulator_id, doc.doc_id, None

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for n, (rid, did, ex) in enumerate(pool.map(work, todo), 1):
            if ex:
                results[(rid, did)] = ex
            if n % 50 == 0:
                print(f"  {n:,}/{len(todo):,} ({time.time()-start:.0f}s)", flush=True)

    for (rid, did), ex in results.items():
        doc = session.get(Document, {"regulator_id": rid, "doc_id": did})
        if doc is not None:
            doc.extraction = ex
    session.commit()

    llm_errors = sum(1 for e in results.values() if e.get("llm_error"))
    named = sum(1 for e in results.values() if e.get("entities"))
    print(f"extracted {len(results):,} in {time.time()-start:.0f}s · "
          f"{named:,} named a company · {llm_errors} provider errors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
