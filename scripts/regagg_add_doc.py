#!/usr/bin/env python3
"""Manually add/update one document in the corpus (human override lane).

    python scripts/regagg_add_doc.py --regulator osfi --url https://... [--operator saad]
    python scripts/regagg_add_doc.py --regulator osfi --url https://... --file guideline.pdf
    python scripts/regagg_add_doc.py --regulator osfi --url https://... --md corrected.md --title "Guideline X"

Goes through the same versioning/provenance pipeline as automated runs
(update -> prior version archived; tagged 'manual'; run row recorded)."""
import argparse, sys
from pathlib import Path
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sajha.db.models  # noqa
from sajha.core.storage import LocalStorageBackend
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.regagg import manual

ap = argparse.ArgumentParser()
ap.add_argument("--regulator", required=True)
ap.add_argument("--url", required=True)
ap.add_argument("--operator", default="cli")
ap.add_argument("--title"); ap.add_argument("--doc-type", default="guidance")
ap.add_argument("--reference"); ap.add_argument("--published")
ap.add_argument("--file", help="local PDF/HTML artifact to ingest for this URL")
ap.add_argument("--md", help="local markdown file with corrected content")
a = ap.parse_args()

session = sessionmaker(bind=create_engine(f"sqlite:///{REPO/'data'/'sajha.db'}",
                       connect_args={"timeout": 60}), expire_on_commit=False)()
storage = CorpusStorage(LocalStorageBackend(str(REPO)))
res = manual.add_document(
    session, storage, regulator_id=a.regulator, url=a.url, operator=a.operator,
    title=a.title, doc_type=a.doc_type, reference_number=a.reference,
    published_date=a.published,
    markdown=Path(a.md).read_text() if a.md else None,
    file_bytes=Path(a.file).read_bytes() if a.file else None)
print(res)
