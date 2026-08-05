"""
Manual document interjection — the human override lane.

When a document was missed (bot-block, dead link, odd format) or needs a
hand-corrected markdown, an operator can add/update it directly. The manual
path goes through the SAME versioning pipeline as automated ingestion, so
nothing bypasses governance:

  * same folder layout (raw + content.md + meta.json),
  * same version/archive semantics (updating an existing doc archives v(n)),
  * provenance records `manual: true` + the operator's identity,
  * a run row (trigger='rerun', operator=<name>) so it shows on the Runs page,
  * the document is tagged `manual` (source='manual') for filtering/audit.

Three input modes:
  1. url only            -> fetch it now (works when the miss was transient)
  2. url + file bytes    -> operator supplies the artifact (e.g. downloaded PDF)
  3. url + markdown text -> operator supplies corrected/authored markdown

Exposed as POST /api/regagg/documents and scripts/regagg_add_doc.py.
"""

from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Optional

from sajha.regagg import ids, rules
from sajha.regagg.fetch import Fetcher, html_to_md, pdf_to_md
from sajha.regagg.models import Document, DocumentTag, Run
from sajha.regagg.versioning import CorpusVersioning, IngestInput


def add_document(
    session, storage, *,
    regulator_id: str,
    url: str,
    operator: str,
    title: Optional[str] = None,
    doc_type: str = "guidance",
    reference_number: Optional[str] = None,
    markdown: Optional[str] = None,
    file_bytes: Optional[bytes] = None,
    published_date: Optional[str] = None,
) -> dict:
    now = datetime.now(timezone.utc)
    run_id = f"{now.date().isoformat()}_{regulator_id}_manual{now:%H%M%S}"

    # ── obtain content by mode ──────────────────────────────────────────────
    if markdown is not None:
        content_md, raw, raw_ext, ocr = markdown, markdown.encode(), "md", False
        fetch_method = "manual_markdown"
    elif file_bytes is not None:
        if file_bytes[:1024].lstrip()[:4] == b"%PDF":
            content_md, ocr = pdf_to_md(file_bytes)
            raw, raw_ext, fetch_method = file_bytes, "pdf", "manual_pdf"
        else:
            content_md, t = html_to_md(file_bytes.decode("utf-8", "replace"))
            title = title or t
            raw, raw_ext, ocr, fetch_method = file_bytes, "html", False, "manual_html"
    else:
        fr = Fetcher().fetch(url)
        content_md, raw, raw_ext, ocr = fr.content_md, fr.raw, fr.raw_ext, fr.ocr
        title = title or fr.title
        fetch_method = fr.fetch_method

    ref = reference_number or rules.extract_reference_number(title or "")
    pub = date.fromisoformat(published_date) if published_date else None

    # stable identity: reference -> existing seen mapping -> URL hash
    from sajha.regagg.models import SeenUrl
    seen = session.get(SeenUrl, {"regulator_id": regulator_id, "url": url})
    doc_id = ids.stable_doc_id(ref, url, existing=seen.doc_id if seen else None)

    v = CorpusVersioning(session, storage)
    result = v.ingest(IngestInput(
        regulator_id=regulator_id, doc_type=doc_type,
        title=title or url, content_md=content_md, source_url=url,
        raw=raw, raw_ext=raw_ext, reference_number=ref,
        published_date=pub, ocr=ocr, doc_id=doc_id,
        source_kind="policy_pdf" if raw_ext == "pdf" else "web",
        meta_extra={"manual": True, "added_by": operator,
                    "fetch_method": fetch_method}),
        run_id=run_id, now=now)

    doc = session.get(Document, {"regulator_id": regulator_id, "doc_id": result.doc_id})
    if doc is not None:
        rules.apply_rules(session, doc, content_md)
        session.merge(DocumentTag(regulator_id=regulator_id, doc_id=result.doc_id,
                                  tag="manual", source="manual"))
        from sajha.regagg import projection
        from sajha.regagg.pipeline import _apply_materiality
        _apply_materiality(session, doc, content_md,
                           "revised" if result.action == "updated" else "new")
        projection.project_doc(storage, doc)   # keep agent-stack mirror current

    # run row so the interjection is visible on the Runs page + audit trail
    session.merge(Run(run_id=run_id, regulator_id=regulator_id,
                      logical_date=now.date(), trigger="rerun", status="success",
                      detected=1, fetched=1, ingested=1,
                      archived=1 if result.action == "updated" else 0,
                      errors=0, operator=operator, started_at=now, finished_at=now))
    # record seen mapping for future automated runs
    from sajha.regagg.pipeline import _record_seen
    _record_seen(session, regulator_id, url, ids.content_hash(content_md),
                 result.doc_id, now)
    session.commit()
    return {"action": result.action, "doc_id": result.doc_id,
            "version_n": result.version_n, "run_id": run_id,
            "regulator_id": regulator_id}
