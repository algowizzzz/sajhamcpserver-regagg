#!/usr/bin/env python3
"""Add reg_documents.source_kind (web | policy_pdf) and backfill from the raw
artifact extension. Idempotent; safe while the server/crawl hold the DB (waits
on locks)."""
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from sqlalchemy import create_engine, text

e = create_engine(f"sqlite:///{REPO/'data'/'sajha.db'}", connect_args={"timeout": 60})
with e.begin() as c:
    cols = [r[1] for r in c.execute(text("PRAGMA table_info(reg_documents)"))]
    if "source_kind" not in cols:
        c.execute(text("ALTER TABLE reg_documents ADD COLUMN source_kind VARCHAR(16) NOT NULL DEFAULT 'web'"))
        print("added column source_kind")
    else:
        print("column already present")
# backfill: docs whose current folder holds raw.pdf
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.core.storage import LocalStorageBackend
st = CorpusStorage(LocalStorageBackend(str(REPO)))
with e.begin() as c:
    rows = c.execute(text("SELECT regulator_id, doc_id, s3_prefix FROM reg_documents")).all()
    n = 0
    for reg, did, prefix in rows:
        if st.backend.exists(f"{prefix}/raw.pdf"):
            c.execute(text("UPDATE reg_documents SET source_kind='policy_pdf' "
                           "WHERE regulator_id=:r AND doc_id=:d"), {"r": reg, "d": did})
            n += 1
    print(f"backfilled {n} policy_pdf docs of {len(rows)} total")
