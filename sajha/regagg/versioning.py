"""
Atomic override + archive protocol (the hardest invariant — TRD §4).

Guarantees, across crashes at any step:
  * exactly one ``current`` version per document,
  * the previous version is preserved in an append-only archive,
  * zero data loss for anything whose *intent* was committed (the staged DB row).

Object storage (MinIO/S3) has no atomic cross-prefix rename, so correctness is
carried by **step ordering + a reconcile pass**, not by storage atomicity:

    1. write new version to  staging/{doc_id}/{run_id}/     (idempotent)
    2. INSERT reg_document_versions (state='staged')        [tx A]
    3. COPY current/ -> archive/{version_ts}/
    4. UPDATE old version row -> state='archived'           [tx B]
    5. COPY staging -> current/ ; DELETE staging
    6. UPDATE new row -> 'current'; UPDATE reg_documents     [tx C]

``reconcile()`` deterministically rolls a partially-applied update *forward*
(the new content is already in staging), converging to one current + archived
history. If step 2 never committed (crash after step 1), there is no staged row,
the old version stays current, and the orphan staging tree is cleaned — the next
scheduled run re-detects the change.

The service takes a SQLAlchemy Session and a CorpusStorage; the caller owns the
outer connection. ``_crash_after`` is a test hook that raises after step N.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import Dict, List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from sajha.regagg import ids
from sajha.regagg.corpus_storage import CorpusStorage, DocArtifacts
from sajha.regagg.models import Document, DocumentVersion


class CrashInjected(Exception):
    """Raised by the _crash_after test hook to simulate a mid-protocol crash."""


@dataclass
class IngestInput:
    regulator_id: str
    doc_type: str
    title: str
    content_md: str
    source_url: str
    raw: Optional[bytes] = None
    raw_ext: str = "html"
    reference_number: Optional[str] = None
    published_date: Optional[date] = None
    effective_date: Optional[date] = None
    comment_deadline: Optional[date] = None
    status: str = "final"
    language: str = "en"
    ocr: bool = False
    summary_md: str = ""
    tags: List[str] = field(default_factory=list)
    meta_extra: Dict = field(default_factory=dict)
    doc_id: Optional[str] = None   # explicit stable id; else derived from ref/content
    source_kind: str = "web"       # web | policy_pdf (set from fetched artifact)

    @property
    def content_hash(self) -> str:
        return ids.content_hash(self.content_md)


@dataclass
class IngestResult:
    action: str            # 'created' | 'updated' | 'unchanged'
    doc_id: str
    version_n: int
    current_prefix: str
    archived_prefix: Optional[str] = None


class CorpusVersioning:
    def __init__(self, session: Session, storage: CorpusStorage):
        self.s = session
        self.st = storage

    # ── public API ──────────────────────────────────────────────────────────

    def ingest(self, inp: IngestInput, run_id: str,
               now: Optional[datetime] = None, _crash_after: Optional[int] = None) -> IngestResult:
        now = now or datetime.now(timezone.utc)
        chash = inp.content_hash
        doc_id = inp.doc_id or ids.assign_doc_id(inp.reference_number, chash)
        existing = self.s.get(Document, {"regulator_id": inp.regulator_id, "doc_id": doc_id})

        if existing is None:
            return self._create(inp, doc_id, chash, run_id, now)
        if existing.content_hash == chash:
            return IngestResult("unchanged", doc_id, existing.version_n,
                                self._doc_current_prefix(existing))
        return self._update(existing, inp, doc_id, chash, run_id, now, _crash_after)

    # ── create (new document) ───────────────────────────────────────────────

    def _create(self, inp: IngestInput, doc_id: str, chash: str,
                run_id: str, now: datetime) -> IngestResult:
        year = ids.published_year(inp.published_date, now)
        cur = self.st.current_prefix(inp.regulator_id, inp.doc_type, year, doc_id)
        version_ts = ids.now_version_ts(now)
        meta = self._build_meta(inp, doc_id, chash, version_ts, 1, run_id, cur, now)
        self.st.write_artifacts(cur, DocArtifacts(
            raw=inp.raw, raw_ext=inp.raw_ext, content_md=inp.content_md,
            meta=meta, summary_md=inp.summary_md))
        doc = Document(
            regulator_id=inp.regulator_id, doc_id=doc_id, doc_type=inp.doc_type,
            title=inp.title, language=inp.language, reference_number=inp.reference_number,
            published_date=inp.published_date, effective_date=inp.effective_date,
            comment_deadline=inp.comment_deadline, status=inp.status,
            source_kind=inp.source_kind,
            content_hash=chash, s3_prefix=cur, source_url=inp.source_url,
            version_n=1, ocr=inp.ocr)
        self.s.add(doc)
        self.s.add(DocumentVersion(
            regulator_id=inp.regulator_id, doc_id=doc_id, version_ts=version_ts,
            version_n=1, content_hash=chash, state="current", run_id=run_id))
        self.s.commit()
        return IngestResult("created", doc_id, 1, cur)

    # ── update (override + archive) ─────────────────────────────────────────

    def _update(self, existing: Document, inp: IngestInput, doc_id: str, chash: str,
                run_id: str, now: datetime, _crash_after: Optional[int]) -> IngestResult:
        year = ids.published_year(existing.published_date or inp.published_date, now)
        doc_type = existing.doc_type
        cur = self.st.current_prefix(inp.regulator_id, doc_type, year, doc_id)
        version_ts = ids.now_version_ts(now)            # ts of the OLD version being archived
        arch = self.st.archive_prefix(inp.regulator_id, doc_type, year, doc_id, version_ts)
        stg = self.st.staging_prefix(inp.regulator_id, doc_id, run_id)
        new_n = existing.version_n + 1

        def crash(step: int):
            if _crash_after == step:
                raise CrashInjected(f"crash after step {step}")

        # 1 — stage new version
        meta = self._build_meta(inp, doc_id, chash, version_ts, new_n, run_id, cur, now)
        self.st.write_artifacts(stg, DocArtifacts(
            raw=inp.raw, raw_ext=inp.raw_ext, content_md=inp.content_md,
            meta=meta, summary_md=inp.summary_md))
        crash(1)

        # 2 — record intent (staged) [tx A]
        staged = DocumentVersion(
            regulator_id=inp.regulator_id, doc_id=doc_id, version_ts=version_ts,
            version_n=new_n, content_hash=chash, state="staged",
            staging_prefix=stg, archive_prefix=arch, run_id=run_id)
        self.s.add(staged)
        self.s.commit()
        crash(2)

        # 3 — copy current -> archive
        self.st.copy_tree(cur, arch)
        crash(3)

        # 4 — mark old version archived [tx B]
        old = self._current_version_row(inp.regulator_id, doc_id, exclude_n=new_n)
        if old is not None:
            old.state = "archived"
            old.archive_prefix = arch
        self.s.commit()
        crash(4)

        # 5 — promote staging -> current
        self.st.delete_tree(cur)
        self.st.copy_tree(stg, cur)
        self.st.delete_tree(stg)
        crash(5)

        # 6 — finalize [tx C]
        staged.state = "current"
        staged.staging_prefix = None
        self._apply_doc_fields(existing, inp, chash, cur, new_n)
        self.s.commit()
        return IngestResult("updated", doc_id, new_n, cur, arch)

    # ── reconciliation (crash recovery + invariant repair) ──────────────────

    def reconcile(self, regulator_id: Optional[str] = None,
                  clean_orphan_staging: bool = True) -> Dict:
        """Repair any document not in a clean state. Deterministic roll-forward.
        Returns a report dict."""
        report = {"repaired": [], "orphan_staging_cleaned": [], "checked": 0}
        # documents that have a staged row OR != 1 current row
        stmt = select(Document.regulator_id, Document.doc_id).distinct()
        if regulator_id:
            stmt = stmt.where(Document.regulator_id == regulator_id)
        for reg, doc_id in self.s.execute(stmt).all():
            report["checked"] += 1
            versions = self._versions(reg, doc_id)
            currents = [v for v in versions if v.state == "current"]
            staged = [v for v in versions if v.state == "staged"]
            if len(currents) == 1 and not staged:
                continue  # clean
            self._repair_doc(reg, doc_id, versions)
            report["repaired"].append(f"{reg}/{doc_id}")

        if clean_orphan_staging:
            report["orphan_staging_cleaned"] = self._clean_orphan_staging(regulator_id)
        return report

    def _repair_doc(self, reg: str, doc_id: str, versions: List[DocumentVersion]) -> None:
        latest = max(versions, key=lambda v: v.version_n)
        doc = self.s.get(Document, {"regulator_id": reg, "doc_id": doc_id})
        # Archive every non-latest row still marked current. The intended archive
        # destination was recorded on the *staged* (latest) row at step 2; the old
        # row itself has no archive_prefix yet, so inherit it. Ensure the live
        # content is physically in the archive before we overwrite current/.
        old_currents = [v for v in versions if v is not latest and v.state == "current"]
        if old_currents:
            dest = latest.archive_prefix
            if dest and not self.st.exists_tree(dest):
                self.st.copy_tree(doc.s3_prefix, dest)  # preserve current (old) content
            for v in old_currents:
                v.state = "archived"
                v.archive_prefix = v.archive_prefix or dest
        # promote latest: prefer staging content if present, else whatever is in current/
        if latest.state in ("staged", "current"):
            if latest.staging_prefix and self.st.exists_tree(latest.staging_prefix):
                self.st.delete_tree(doc.s3_prefix)
                self.st.copy_tree(latest.staging_prefix, doc.s3_prefix)
                self.st.delete_tree(latest.staging_prefix)
            latest.state = "current"
            latest.staging_prefix = None
            # sync documents row to the promoted version
            meta = self.st.read_meta(doc.s3_prefix) or {}
            doc.content_hash = latest.content_hash
            doc.version_n = latest.version_n
            doc.s3_prefix = doc.s3_prefix
            if meta.get("title"):
                doc.title = meta["title"]
            doc.updated_at = datetime.now(timezone.utc)
        self.s.commit()

    def _clean_orphan_staging(self, regulator_id: Optional[str]) -> List[str]:
        """Staging trees with no staged DB row are crash remnants of a step-1
        crash (intent never committed). List them (caller may prune >48h)."""
        cleaned: List[str] = []
        staged_prefixes = {
            v.staging_prefix for v in self.s.scalars(
                select(DocumentVersion).where(DocumentVersion.state == "staged")
            ).all() if v.staging_prefix
        }
        regs = [regulator_id] if regulator_id else [
            r for (r,) in self.s.execute(select(Document.regulator_id).distinct()).all()
        ]
        for reg in regs:
            staging_root = f"{self.st.reg_root(reg)}/staging"
            for path in self.st.list_tree(staging_root):
                # path like .../staging/{doc_id}/{run_id}/file
                parts = path[len(staging_root) + 1:].split("/")
                if len(parts) < 2:
                    continue
                stg_prefix = f"{staging_root}/{parts[0]}/{parts[1]}"
                if stg_prefix not in staged_prefixes and stg_prefix not in cleaned:
                    self.st.delete_tree(stg_prefix)
                    cleaned.append(stg_prefix)
        return cleaned

    # ── invariant check (used by reconcile job + tests) ─────────────────────

    def check_invariants(self, regulator_id: Optional[str] = None) -> List[str]:
        violations: List[str] = []
        stmt = select(Document.regulator_id, Document.doc_id).distinct()
        if regulator_id:
            stmt = stmt.where(Document.regulator_id == regulator_id)
        for reg, doc_id in self.s.execute(stmt).all():
            versions = self._versions(reg, doc_id)
            currents = [v for v in versions if v.state == "current"]
            if len(currents) != 1:
                violations.append(f"{reg}/{doc_id}: {len(currents)} current versions (expected 1)")
            staged = [v for v in versions if v.state == "staged"]
            if staged:
                violations.append(f"{reg}/{doc_id}: {len(staged)} staged rows left over")
            doc = self.s.get(Document, {"regulator_id": reg, "doc_id": doc_id})
            if currents and doc.content_hash != currents[0].content_hash:
                violations.append(f"{reg}/{doc_id}: documents.content_hash != current version hash")
        return violations

    # ── helpers ─────────────────────────────────────────────────────────────

    def _versions(self, reg: str, doc_id: str) -> List[DocumentVersion]:
        return list(self.s.scalars(
            select(DocumentVersion)
            .where(DocumentVersion.regulator_id == reg, DocumentVersion.doc_id == doc_id)
            .order_by(DocumentVersion.version_n)).all())

    def _current_version_row(self, reg: str, doc_id: str,
                             exclude_n: Optional[int] = None) -> Optional[DocumentVersion]:
        for v in self._versions(reg, doc_id):
            if v.state == "current" and v.version_n != exclude_n:
                return v
        return None

    def _doc_current_prefix(self, doc: Document) -> str:
        return doc.s3_prefix

    def _apply_doc_fields(self, doc: Document, inp: IngestInput, chash: str,
                          cur: str, new_n: int) -> None:
        doc.content_hash = chash
        doc.version_n = new_n
        doc.s3_prefix = cur
        doc.title = inp.title
        doc.status = inp.status
        if inp.effective_date is not None:
            doc.effective_date = inp.effective_date
        if inp.comment_deadline is not None:
            doc.comment_deadline = inp.comment_deadline
        doc.ocr = inp.ocr
        doc.updated_at = datetime.now(timezone.utc)

    def _build_meta(self, inp: IngestInput, doc_id: str, chash: str, version_ts: str,
                    version_n: int, run_id: str, s3_prefix: str, now: datetime) -> Dict:
        meta = {
            "doc_id": doc_id,
            "regulator_id": inp.regulator_id,
            "doc_type": inp.doc_type,
            "title": inp.title,
            "language": inp.language,
            "source_url": inp.source_url,
            "reference_number": inp.reference_number,
            "published_date": inp.published_date.isoformat() if inp.published_date else None,
            "effective_date": inp.effective_date.isoformat() if inp.effective_date else None,
            "comment_deadline": inp.comment_deadline.isoformat() if inp.comment_deadline else None,
            "status": inp.status,
            "content_hash": chash,
            "version_ts": version_ts,
            "version_n": version_n,
            "ingested_at": now.isoformat(),
            "run_id": run_id,
            "ocr": inp.ocr,
            "s3_prefix": s3_prefix,
            "tags": inp.tags,
        }
        meta.update(inp.meta_extra or {})
        return meta
