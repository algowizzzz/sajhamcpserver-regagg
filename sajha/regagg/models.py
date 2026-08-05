"""
Regulatory Intelligence Aggregator — SQLAlchemy corpus models.

Mirrors the handover data schema (04_DATA_SCHEMA_DESIGN §3) but embedded in the
SAJHA database: every table is defined on the shared ``sajha.db.base.Base`` and
namespaced with a ``reg_`` prefix so it coexists with the core schema (which
already owns generic names like ``audit_log``, ``runs``-free, etc.).

Table-name mapping vs. the handover DDL:
    documents           -> reg_documents
    document_versions   -> reg_document_versions
    document_tags       -> reg_document_tags
    document_edges      -> reg_document_edges
    pending_edges       -> reg_pending_edges
    seen_urls           -> reg_seen_urls
    regulators          -> reg_regulators
    runs                -> reg_runs
    watermarks          -> reg_watermarks
(The handover's generic ``audit_log`` is satisfied by the existing core
 ``AuditLog`` model — operator actions on reruns/toggles log there.)

Because the engine calls ``Base.metadata.create_all()`` at startup, importing
this module (done from ``sajha/db/models/__init__.py``) is enough to provision
these tables on both SQLite (dev) and PostgreSQL (prod). A hand-authored
PostgreSQL script is also shipped at
``db/scripts/postgresql/003_regagg_schema.sql`` for the ``psql -f`` path.

Invariants enforced by application logic + the reconcile job (not all
expressible as constraints):
  * exactly one reg_document_versions row with state='current' per (regulator, doc_id)
  * reg_document_edges / archive rows are append-only (no delete path)
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import (
    Boolean, CheckConstraint, Column, Date, DateTime, Float, ForeignKeyConstraint,
    Index, Integer, String, Text, UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import JSON

from sajha.db.base import Base


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


# JSON that becomes JSONB on PostgreSQL and plain JSON on SQLite/others.
JSONFlex = JSON().with_variant(JSONB, "postgresql")

# Controlled enums (kept as CHECK constraints; app validates against configs).
_CONNECTORS = ("api", "rss", "sitemap_diff")
_DOC_STATUS = ("proposed", "final", "superseded", "withdrawn")
_VERSION_STATE = ("staged", "current", "archived", "rolled_back")
_TAG_SOURCE = ("config", "llm", "rule", "manual")
_EDGE_TYPES = ("implements", "supersedes", "interprets", "references", "consults_on")
_RUN_TRIGGER = ("schedule", "rerun", "backfill")
_RUN_STATUS = ("running", "success", "success_empty", "failed")


def _in(col: str, allowed: tuple[str, ...]) -> str:
    vals = ", ".join(f"'{v}'" for v in allowed)
    return f"{col} IN ({vals})"


# ── regulators ──────────────────────────────────────────────────────────────

class Regulator(Base):
    __tablename__ = "reg_regulators"

    regulator_id = Column(String(64), primary_key=True)
    name = Column(String(255), nullable=False)
    jurisdiction = Column(String(16), nullable=False)  # CA, US, EU, UK, SG, HK, AU, JP, IN, INTL
    connector = Column(String(20), nullable=False)
    config = Column(JSONFlex, nullable=False)          # full parsed YAML
    active = Column(Boolean, nullable=False, default=True)
    staleness_alert_days = Column(Integer, nullable=False, default=14)
    created_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow, onupdate=_utcnow)

    __table_args__ = (
        CheckConstraint(_in("connector", _CONNECTORS), name="ck_reg_regulators_connector"),
    )


# ── seen_urls (change detection) ────────────────────────────────────────────

class SeenUrl(Base):
    __tablename__ = "reg_seen_urls"

    regulator_id = Column(String(64), primary_key=True)
    url = Column(Text, primary_key=True)
    content_hash = Column(String(80))
    etag = Column(String(255))
    last_modified = Column(String(64))
    doc_id = Column(String(128))
    first_seen = Column(DateTime(timezone=True), nullable=False, default=_utcnow)
    last_checked = Column(DateTime(timezone=True))
    http_status = Column(Integer)

    __table_args__ = (
        ForeignKeyConstraint(["regulator_id"], ["reg_regulators.regulator_id"],
                             name="fk_reg_seen_urls_regulator"),
        Index("ix_reg_seen_urls_doc", "doc_id"),
    )


# ── documents (one current row per doc) ─────────────────────────────────────

class Document(Base):
    __tablename__ = "reg_documents"

    regulator_id = Column(String(64), primary_key=True)
    doc_id = Column(String(128), primary_key=True)
    doc_type = Column(String(32), nullable=False)
    title = Column(Text, nullable=False)
    language = Column(String(8), nullable=False, default="en")
    reference_number = Column(String(128))
    published_date = Column(Date)
    effective_date = Column(Date)
    comment_deadline = Column(Date)
    status = Column(String(16), nullable=False, default="final")
    source_kind = Column(String(16), nullable=False, default="web")  # web | policy_pdf
    # materiality: deterministic, explainable priority (see regagg/materiality.py)
    materiality_score = Column(Integer, nullable=False, default=0)
    materiality_band = Column(String(16), nullable=False, default="Informational")
    materiality_reason = Column(Text)
    content_hash = Column(String(80), nullable=False)
    s3_prefix = Column(Text, nullable=False)           # current/ prefix in object storage
    source_url = Column(Text, nullable=False)
    version_n = Column(Integer, nullable=False, default=1)
    ocr = Column(Boolean, nullable=False, default=False)
    ingested_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow, onupdate=_utcnow)

    __table_args__ = (
        ForeignKeyConstraint(["regulator_id"], ["reg_regulators.regulator_id"],
                             name="fk_reg_documents_regulator"),
        CheckConstraint(_in("status", _DOC_STATUS), name="ck_reg_documents_status"),
        Index("ix_reg_documents_pub", "published_date"),
        Index("ix_reg_documents_type", "doc_type", "published_date"),
        Index("ix_reg_documents_materiality", "materiality_score"),
    )


# ── document_versions (full history) ────────────────────────────────────────

class DocumentVersion(Base):
    __tablename__ = "reg_document_versions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    regulator_id = Column(String(64), nullable=False)
    doc_id = Column(String(128), nullable=False)
    version_ts = Column(String(32), nullable=False)     # UTC basic e.g. 2026-07-29T06-15-00Z
    version_n = Column(Integer, nullable=False)
    content_hash = Column(String(80), nullable=False)
    state = Column(String(16), nullable=False)
    staging_prefix = Column(Text)
    archive_prefix = Column(Text)
    run_id = Column(String(128), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow)

    __table_args__ = (
        UniqueConstraint("regulator_id", "doc_id", "version_n",
                         name="uq_reg_doc_versions_n"),
        ForeignKeyConstraint(["regulator_id", "doc_id"],
                             ["reg_documents.regulator_id", "reg_documents.doc_id"],
                             name="fk_reg_doc_versions_document", ondelete="RESTRICT"),
        CheckConstraint(_in("state", _VERSION_STATE), name="ck_reg_doc_versions_state"),
        Index("ix_reg_doc_versions_doc", "regulator_id", "doc_id"),
        Index("ix_reg_doc_versions_state", "state"),
    )


# ── document_tags ───────────────────────────────────────────────────────────

class DocumentTag(Base):
    __tablename__ = "reg_document_tags"

    regulator_id = Column(String(64), primary_key=True)
    doc_id = Column(String(128), primary_key=True)
    tag = Column(String(64), primary_key=True)
    source = Column(String(16), nullable=False, default="llm")

    __table_args__ = (
        ForeignKeyConstraint(["regulator_id", "doc_id"],
                             ["reg_documents.regulator_id", "reg_documents.doc_id"],
                             name="fk_reg_doc_tags_document", ondelete="CASCADE"),
        CheckConstraint(_in("source", _TAG_SOURCE), name="ck_reg_doc_tags_source"),
        Index("ix_reg_doc_tags_tag", "tag"),
    )


# ── document_edges (cross-reference graph) ──────────────────────────────────

class DocumentEdge(Base):
    __tablename__ = "reg_document_edges"

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_regulator = Column(String(64), nullable=False)
    from_doc = Column(String(128), nullable=False)
    to_regulator = Column(String(64), nullable=False)
    to_doc = Column(String(128), nullable=False)
    edge_type = Column(String(20), nullable=False)
    confidence = Column(Float, nullable=False, default=1.0)
    created_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow)

    __table_args__ = (
        UniqueConstraint("from_regulator", "from_doc", "to_regulator", "to_doc", "edge_type",
                         name="uq_reg_doc_edges"),
        CheckConstraint(_in("edge_type", _EDGE_TYPES), name="ck_reg_doc_edges_type"),
        Index("ix_reg_doc_edges_from", "from_regulator", "from_doc"),
        Index("ix_reg_doc_edges_to", "to_regulator", "to_doc"),
    )


# ── pending_edges (unresolved references) ───────────────────────────────────

class PendingEdge(Base):
    __tablename__ = "reg_pending_edges"

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_regulator = Column(String(64), nullable=False)
    from_doc = Column(String(128), nullable=False)
    raw_reference = Column(Text, nullable=False)
    edge_type = Column(String(20), nullable=False)
    attempts = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow)


# ── runs (per-regulator ingestion runs) ─────────────────────────────────────

class Run(Base):
    __tablename__ = "reg_runs"

    run_id = Column(String(128), primary_key=True)      # {date}_{regulator}_{short}
    regulator_id = Column(String(64), nullable=False)
    logical_date = Column(Date, nullable=False)
    trigger = Column(String(16), nullable=False)
    status = Column(String(16), nullable=False)
    detected = Column(Integer, default=0)
    fetched = Column(Integer, default=0)
    ingested = Column(Integer, default=0)
    archived = Column(Integer, default=0)
    errors = Column(Integer, default=0)
    started_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow)
    finished_at = Column(DateTime(timezone=True))
    manifest_path = Column(Text)
    operator = Column(String(128))                      # set for reruns (audit)

    __table_args__ = (
        ForeignKeyConstraint(["regulator_id"], ["reg_regulators.regulator_id"],
                             name="fk_reg_runs_regulator"),
        CheckConstraint(_in("trigger", _RUN_TRIGGER), name="ck_reg_runs_trigger"),
        CheckConstraint(_in("status", _RUN_STATUS), name="ck_reg_runs_status"),
        Index("ix_reg_runs_matrix", "logical_date", "regulator_id"),
    )


# ── watermarks (API poller position) ────────────────────────────────────────

class Watermark(Base):
    __tablename__ = "reg_watermarks"

    regulator_id = Column(String(64), primary_key=True)
    watermark = Column(JSONFlex, nullable=False)        # e.g. {"last_published": "2026-07-29"}
    updated_at = Column(DateTime(timezone=True), nullable=False, default=_utcnow, onupdate=_utcnow)

    __table_args__ = (
        ForeignKeyConstraint(["regulator_id"], ["reg_regulators.regulator_id"],
                             name="fk_reg_watermarks_regulator"),
    )


# Every corpus table, in dependency order (used by verify + reconcile jobs).
REGAGG_MODELS = [
    Regulator, SeenUrl, Document, DocumentVersion, DocumentTag,
    DocumentEdge, PendingEdge, Run, Watermark,
]

__all__ = [m.__name__ for m in REGAGG_MODELS] + ["REGAGG_MODELS", "JSONFlex"]
