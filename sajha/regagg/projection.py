"""
Markdown projection — the agent-stack's consumption layer.

The canonical governed store stays at data/web_aggregator/ (raw originals,
meta.json, versions, append-only archive — everything the reg_* index tools
and governance depend on). This module maintains a PROJECTION of the *current*
markdown corpus in the layout the user's md-based agent tools (RAG / BM25 /
read) consume:

    data/markdown/
      web/{regulator}/{doc_type}/{doc_id}.md      # HTML-converted pages
      policy/{regulator}/{doc_type}/{doc_id}.md   # PDF-converted policy docs

Each file carries a small YAML frontmatter (title, regulator, reference,
source_url, published, version) so RAG chunks retain citation context.

Write-through: the pipeline calls ``project_doc`` after every ingest, so the
projection is always current — one file per document, updated in place on
revisions (history lives in the canonical archive, not here). ``resync``
rebuilds the whole projection from the canonical store (used once for the
existing corpus and as a nightly self-heal in the daily poller).
"""

from __future__ import annotations

from typing import Optional

from sqlalchemy import select

from sajha.regagg.models import Document

MARKDOWN_ROOT = "data/markdown"

_KIND_DIR = {"web": "web", "policy_pdf": "policy"}


def projection_path(doc: Document) -> str:
    kind = _KIND_DIR.get(doc.source_kind or "web", "web")
    return f"{MARKDOWN_ROOT}/{kind}/{doc.regulator_id}/{doc.doc_type}/{doc.doc_id}.md"


def _frontmatter(doc: Document) -> str:
    def esc(v):
        return str(v).replace('"', "'") if v is not None else ""
    lines = ["---"]
    for k, v in (
        ("title", doc.title), ("regulator", doc.regulator_id),
        ("doc_type", doc.doc_type), ("reference", doc.reference_number),
        ("status", doc.status), ("source_kind", doc.source_kind),
        ("source_url", doc.source_url),
        ("published", doc.published_date), ("version", doc.version_n),
    ):
        if v not in (None, ""):
            lines.append(f'{k}: "{esc(v)}"')
    lines.append("---")
    return "\n".join(lines)


def project_doc(storage, doc: Document) -> Optional[str]:
    """Write/refresh one document's projection file. Returns the path."""
    content = storage.read_content(doc.s3_prefix)
    if content is None:
        return None
    path = projection_path(doc)
    storage.backend.write_text(path, _frontmatter(doc) + "\n\n" + content)
    return path


def remove_doc(storage, doc: Document) -> None:
    """Drop a projection file (e.g. purged/withdrawn doc)."""
    try:
        storage.backend.delete(projection_path(doc))
    except Exception:  # noqa: BLE001
        pass


def resync(session, storage, wipe: bool = False) -> dict:
    """Rebuild the whole projection from the canonical store. Idempotent."""
    if wipe:
        for p in storage.backend.list_files(MARKDOWN_ROOT, "*"):
            storage.backend.delete(p)
    n = skipped = 0
    for doc in session.scalars(select(Document)).all():
        if project_doc(storage, doc):
            n += 1
        else:
            skipped += 1
    return {"projected": n, "skipped_no_content": skipped, "root": MARKDOWN_ROOT}
