#!/usr/bin/env python3
"""Backfill/refresh materiality scores across the corpus (idempotent).
Run after changing config/regulators/_materiality.yaml to re-prioritise."""
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from collections import Counter
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import sajha.db.models  # noqa
from sajha.core.storage import LocalStorageBackend
from sajha.regagg import materiality
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.regagg.models import Document, DocumentTag

e = create_engine(f"sqlite:///{REPO/'data'/'sajha.db'}", connect_args={"timeout": 60})
s = sessionmaker(bind=e, expire_on_commit=False)()
st = CorpusStorage(LocalStorageBackend(str(REPO)))
cfg = materiality.load_config(str(REPO / materiality.CONFIG_PATH))

tags_by = {}
for reg, did, tag in s.execute(select(DocumentTag.regulator_id, DocumentTag.doc_id, DocumentTag.tag)).all():
    tags_by.setdefault((reg, did), []).append(tag)

bands = Counter()
docs = s.query(Document).all()
for i, d in enumerate(docs, 1):
    text = st.read_content(d.s3_prefix) or ""
    m = materiality.score_document(d, text=text, tags=tags_by.get((d.regulator_id, d.doc_id), []), cfg=cfg)
    d.materiality_score, d.materiality_band, d.materiality_reason = m.score, m.band, m.reason
    bands[m.band] += 1
    if i % 500 == 0:
        s.commit(); print(f"  {i}/{len(docs)}…", flush=True)
s.commit()
print(f"\nscored {len(docs)} documents:")
for b in materiality.BAND_ORDER:
    if bands[b]:
        print(f"  {b:14s} {bands[b]:5d}  ({100*bands[b]//len(docs)}%)")
