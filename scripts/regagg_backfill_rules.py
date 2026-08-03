#!/usr/bin/env python3
"""
Post-crawl backfill: apply the deterministic rules pass (reference numbers,
rule-based edges, pending-edge resolution) + source_kind to every document
already in the corpus. Needed once for documents ingested before the Phase-A
pipeline changes; safe to re-run any time (idempotent).

    python scripts/regagg_backfill_rules.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sajha.db.models  # noqa: F401
from sajha.core.storage import LocalStorageBackend
from sajha.regagg import rules
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.regagg.models import Document, DocumentEdge, PendingEdge


def main() -> int:
    engine = create_engine(f"sqlite:///{REPO/'data'/'sajha.db'}",
                           connect_args={"timeout": 60})
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    storage = CorpusStorage(LocalStorageBackend(str(REPO)))

    docs = session.query(Document).all()
    stats = {"docs": len(docs), "refs_filled": 0, "edges": 0, "pending": 0,
             "pdf_kind": 0}
    for n, doc in enumerate(docs, 1):
        content = storage.read_content(doc.s3_prefix) or ""
        # source_kind from the stored raw artifact
        if doc.source_kind != "policy_pdf" and storage.backend.exists(f"{doc.s3_prefix}/raw.pdf"):
            doc.source_kind = "policy_pdf"
            stats["pdf_kind"] += 1
        rep = rules.apply_rules(session, doc, content)
        stats["refs_filled"] += bool(rep["reference_number"])
        stats["edges"] += rep["edges"]
        stats["pending"] += rep["pending"]
        if n % 100 == 0:
            session.commit()
            print(f"  {n}/{len(docs)} …", flush=True)
    session.commit()
    resolved = rules.resolve_pending(session)
    print(f"\nbackfill: {stats['docs']} docs · {stats['refs_filled']} reference numbers filled"
          f" · {stats['edges']} edges + {resolved} resolved from pending"
          f" · {session.query(PendingEdge).count()} still pending"
          f" · {stats['pdf_kind']} re-flagged policy_pdf"
          f" · {session.query(DocumentEdge).count()} total edges in graph")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
