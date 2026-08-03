"""
Epic 2 — versioning/storage: correctness + chaos.

Proves the atomic override->archive invariant survives a crash at *every* step
of the protocol (PRD US-3.2 / US-3.3): after reconcile there is always exactly
one current version, the prior version is archived, and no committed data is
lost.
"""

from __future__ import annotations

from datetime import date, datetime, timezone

import pytest

from sajha.regagg.models import Document, DocumentVersion
from sajha.regagg.versioning import (
    CorpusVersioning, CrashInjected, IngestInput,
)

T0 = datetime(2026, 7, 1, 6, 0, 0, tzinfo=timezone.utc)
T1 = datetime(2026, 7, 16, 6, 10, 0, tzinfo=timezone.utc)


def _inp(content: str, **kw) -> IngestInput:
    base = dict(
        regulator_id="osfi", doc_type="guidance",
        title=kw.pop("title", "Guideline B-13"),
        content_md=content, source_url="https://osfi.example/b-13",
        raw=content.encode(), reference_number=kw.pop("reference_number", "B-13"),
        published_date=date(2026, 7, 1), status="final",
    )
    base.update(kw)
    return IngestInput(**base)


def _counts(session, reg="osfi", doc_id="b-13"):
    versions = session.query(DocumentVersion).filter_by(regulator_id=reg, doc_id=doc_id).all()
    return {
        "current": sum(v.state == "current" for v in versions),
        "archived": sum(v.state == "archived" for v in versions),
        "staged": sum(v.state == "staged" for v in versions),
        "total": len(versions),
    }


# ── happy path ──────────────────────────────────────────────────────────────

def test_create_then_update_archives_previous(session, storage, seed_regulator):
    seed_regulator()
    v = CorpusVersioning(session, storage)

    r1 = v.ingest(_inp("# B-13 v1\noriginal"), run_id="run1", now=T0)
    assert r1.action == "created" and r1.version_n == 1
    assert storage.read_content(r1.current_prefix).strip() == "# B-13 v1\noriginal"

    r2 = v.ingest(_inp("# B-13 v2\nrevised"), run_id="run2", now=T1)
    assert r2.action == "updated" and r2.version_n == 2

    # exactly one current, one archived, current holds v2, archive holds v1
    assert _counts(session) == {"current": 1, "archived": 1, "staged": 0, "total": 2}
    assert "revised" in storage.read_content(r2.current_prefix)
    assert storage.exists_tree(r2.archived_prefix)
    assert "original" in storage.read_content(r2.archived_prefix)
    assert not v.check_invariants()


def test_unchanged_content_is_noop(session, storage, seed_regulator):
    seed_regulator()
    v = CorpusVersioning(session, storage)
    v.ingest(_inp("# same"), run_id="r1", now=T0)
    r = v.ingest(_inp("# same"), run_id="r2", now=T1)
    assert r.action == "unchanged"
    assert _counts(session)["total"] == 1


def test_documents_row_tracks_current(session, storage, seed_regulator):
    seed_regulator()
    v = CorpusVersioning(session, storage)
    v.ingest(_inp("# v1"), run_id="r1", now=T0)
    v.ingest(_inp("# v2"), run_id="r2", now=T1)
    doc = session.get(Document, {"regulator_id": "osfi", "doc_id": "b-13"})
    assert doc.version_n == 2
    cur = [x for x in session.query(DocumentVersion).all() if x.state == "current"][0]
    assert doc.content_hash == cur.content_hash


# ── chaos: crash after each protocol step, then reconcile ───────────────────

@pytest.mark.parametrize("crash_step", [1, 2, 3, 4, 5])
def test_crash_then_reconcile_restores_invariant(session, storage, seed_regulator, crash_step):
    seed_regulator()
    v = CorpusVersioning(session, storage)
    v.ingest(_inp("# B-13 v1\noriginal"), run_id="run1", now=T0)

    with pytest.raises(CrashInjected):
        v.ingest(_inp("# B-13 v2\nrevised"), run_id="run2", now=T1, _crash_after=crash_step)

    # Before reconcile, state may be inconsistent. After reconcile it must be clean.
    report = v.reconcile()
    violations = v.check_invariants()
    assert violations == [], f"crash@{crash_step}: {violations} (report={report})"

    c = _counts(session)
    assert c["current"] == 1 and c["staged"] == 0

    # No committed data lost: the old version's content is always still readable
    # (either as current, if the update didn't commit intent, or in archive).
    doc = session.get(Document, {"regulator_id": "osfi", "doc_id": "b-13"})
    cur_content = storage.read_content(doc.s3_prefix)
    all_archived = " ".join(
        storage.read_content(x.archive_prefix) or ""
        for x in session.query(DocumentVersion).filter_by(state="archived").all()
        if x.archive_prefix)
    corpus_text = (cur_content or "") + " " + all_archived
    assert "original" in corpus_text, f"crash@{crash_step}: lost the v1 content"


def test_crash_after_step1_keeps_old_current_and_cleans_staging(session, storage, seed_regulator):
    """Step-1 crash: intent (staged row) never committed -> old stays current,
    orphan staging is cleaned; the change will be re-detected next run."""
    seed_regulator()
    v = CorpusVersioning(session, storage)
    v.ingest(_inp("# v1\noriginal"), run_id="run1", now=T0)
    with pytest.raises(CrashInjected):
        v.ingest(_inp("# v2\nrevised"), run_id="run2", now=T1, _crash_after=1)

    report = v.reconcile()
    assert v.check_invariants() == []
    assert _counts(session) == {"current": 1, "archived": 0, "staged": 0, "total": 1}
    doc = session.get(Document, {"regulator_id": "osfi", "doc_id": "b-13"})
    assert "original" in storage.read_content(doc.s3_prefix)
    assert report["orphan_staging_cleaned"]  # the staged tree was removed


def test_reconcile_is_idempotent(session, storage, seed_regulator):
    seed_regulator()
    v = CorpusVersioning(session, storage)
    v.ingest(_inp("# v1"), run_id="r1", now=T0)
    v.ingest(_inp("# v2"), run_id="r2", now=T1)
    first = v.reconcile()
    second = v.reconcile()
    assert v.check_invariants() == []
    assert second["repaired"] == []  # nothing left to fix on the second pass
