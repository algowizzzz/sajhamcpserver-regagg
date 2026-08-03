#!/usr/bin/env python3
"""Purge SYNTHETIC demo-seed documents (regagg_seed_demo.py fixtures) from the
corpus. Identified by the MockLLM marker pattern in content.md — real regulator
documents never contain it. Removes DB rows (docs/versions/tags/edges/seen) and
their storage trees. The append-only invariant protects real regulatory data,
not our own test fixtures."""
import re, sys
from pathlib import Path
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import sajha.db.models  # noqa
from sajha.core.storage import LocalStorageBackend
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.regagg.models import Document, DocumentVersion, DocumentTag, DocumentEdge, SeenUrl

MARKER = re.compile(r"TYPE:\w+ STATUS:\w+")
e = create_engine(f"sqlite:///{REPO/'data'/'sajha.db'}", connect_args={"timeout": 60})
s = sessionmaker(bind=e, expire_on_commit=False)()
st = CorpusStorage(LocalStorageBackend(str(REPO)))

victims = []
for d in s.query(Document).all():
    content = st.read_content(d.s3_prefix) or ""
    if MARKER.search(content):
        victims.append(d)
print(f"found {len(victims)} synthetic demo docs:")
for d in victims:
    print(f"  {d.regulator_id}/{d.doc_id}  {d.title[:50]}")
    for v in s.query(DocumentVersion).filter_by(regulator_id=d.regulator_id, doc_id=d.doc_id):
        if v.archive_prefix: st.delete_tree(v.archive_prefix)
        s.delete(v)
    s.query(DocumentTag).filter_by(regulator_id=d.regulator_id, doc_id=d.doc_id).delete()
    s.query(DocumentEdge).filter((DocumentEdge.from_doc==d.doc_id)|(DocumentEdge.to_doc==d.doc_id)).delete()
    s.query(SeenUrl).filter_by(regulator_id=d.regulator_id, doc_id=d.doc_id).delete()
    st.delete_tree(d.s3_prefix)
    s.delete(d)
s.commit()
print(f"purged. corpus now: {s.query(Document).count()} real documents")
