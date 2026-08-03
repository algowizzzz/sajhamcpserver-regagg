-- ============================================================================
-- SAJHA MCP Server — Regulatory Intelligence Aggregator (regagg) schema
-- Copyright All rights Reserved 2025-2030, Ashutosh Sinha
-- Companion to 001_schema.sql. Tables are namespaced `reg_*` and mirror the
-- SQLAlchemy models in sajha/regagg/models.py (single source of truth).
-- Run AFTER 001_schema.sql:  psql -d sajha -f 003_regagg_schema.sql
--
-- Data model reference: handover 04_DATA_SCHEMA_DESIGN §3.
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- ── reg_regulators ──────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS reg_regulators (
    regulator_id          VARCHAR(64)   PRIMARY KEY,
    name                  VARCHAR(255)  NOT NULL,
    jurisdiction          VARCHAR(16)   NOT NULL,   -- CA, US, EU, UK, SG, HK, AU, JP, IN, INTL
    connector             VARCHAR(20)   NOT NULL,
    config                JSONB         NOT NULL,   -- full parsed YAML
    active                BOOLEAN       NOT NULL DEFAULT TRUE,
    staleness_alert_days  INTEGER       NOT NULL DEFAULT 14,
    created_at            TIMESTAMPTZ   NOT NULL DEFAULT now(),
    updated_at            TIMESTAMPTZ   NOT NULL DEFAULT now(),
    CONSTRAINT ck_reg_regulators_connector
        CHECK (connector IN ('api','rss','sitemap_diff'))
);

-- ── reg_seen_urls (change detection) ────────────────────────────────────────
CREATE TABLE IF NOT EXISTS reg_seen_urls (
    regulator_id   VARCHAR(64)  NOT NULL REFERENCES reg_regulators(regulator_id),
    url            TEXT         NOT NULL,
    content_hash   VARCHAR(80),
    etag           VARCHAR(255),
    last_modified  VARCHAR(64),
    doc_id         VARCHAR(128),
    first_seen     TIMESTAMPTZ  NOT NULL DEFAULT now(),
    last_checked   TIMESTAMPTZ,
    http_status    INTEGER,
    PRIMARY KEY (regulator_id, url)
);
CREATE INDEX IF NOT EXISTS ix_reg_seen_urls_doc ON reg_seen_urls (doc_id);

-- ── reg_documents (exactly one current row per doc) ─────────────────────────
CREATE TABLE IF NOT EXISTS reg_documents (
    regulator_id      VARCHAR(64)  NOT NULL REFERENCES reg_regulators(regulator_id),
    doc_id            VARCHAR(128) NOT NULL,
    doc_type          VARCHAR(32)  NOT NULL,
    title             TEXT         NOT NULL,
    language          VARCHAR(8)   NOT NULL DEFAULT 'en',
    reference_number  VARCHAR(128),
    published_date    DATE,
    effective_date    DATE,
    comment_deadline  DATE,
    status            VARCHAR(16)  NOT NULL DEFAULT 'final'
                      CHECK (status IN ('proposed','final','superseded','withdrawn')),
    content_hash      VARCHAR(80)  NOT NULL,
    s3_prefix         TEXT         NOT NULL,   -- current/ prefix in object storage
    source_url        TEXT         NOT NULL,
    version_n         INTEGER      NOT NULL DEFAULT 1,
    ocr               BOOLEAN      NOT NULL DEFAULT FALSE,
    ingested_at       TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at        TIMESTAMPTZ  NOT NULL DEFAULT now(),
    PRIMARY KEY (regulator_id, doc_id)
);
CREATE INDEX IF NOT EXISTS ix_reg_documents_pub  ON reg_documents (published_date DESC);
CREATE INDEX IF NOT EXISTS ix_reg_documents_type ON reg_documents (doc_type, published_date DESC);
CREATE INDEX IF NOT EXISTS ix_reg_documents_title_trgm
    ON reg_documents USING gin (title gin_trgm_ops);

-- ── reg_document_versions (full history) ────────────────────────────────────
CREATE TABLE IF NOT EXISTS reg_document_versions (
    id              BIGSERIAL    PRIMARY KEY,
    regulator_id    VARCHAR(64)  NOT NULL,
    doc_id          VARCHAR(128) NOT NULL,
    version_ts      VARCHAR(32)  NOT NULL,     -- e.g. 2026-07-29T06-15-00Z
    version_n       INTEGER      NOT NULL,
    content_hash    VARCHAR(80)  NOT NULL,
    state           VARCHAR(16)  NOT NULL
                    CHECK (state IN ('staged','current','archived','rolled_back')),
    staging_prefix  TEXT,
    archive_prefix  TEXT,
    run_id          VARCHAR(128) NOT NULL,
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT now(),
    CONSTRAINT uq_reg_doc_versions_n UNIQUE (regulator_id, doc_id, version_n),
    CONSTRAINT fk_reg_doc_versions_document
        FOREIGN KEY (regulator_id, doc_id)
        REFERENCES reg_documents (regulator_id, doc_id) ON DELETE RESTRICT
);
CREATE INDEX IF NOT EXISTS ix_reg_doc_versions_doc   ON reg_document_versions (regulator_id, doc_id);
CREATE INDEX IF NOT EXISTS ix_reg_doc_versions_state ON reg_document_versions (state);
-- INVARIANT: at most one 'current' version per document (enforced in the DB).
CREATE UNIQUE INDEX IF NOT EXISTS uq_reg_doc_versions_one_current
    ON reg_document_versions (regulator_id, doc_id) WHERE state = 'current';

-- ── reg_document_tags ───────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS reg_document_tags (
    regulator_id  VARCHAR(64)  NOT NULL,
    doc_id        VARCHAR(128) NOT NULL,
    tag           VARCHAR(64)  NOT NULL,
    source        VARCHAR(16)  NOT NULL DEFAULT 'llm'
                  CHECK (source IN ('config','llm','rule','manual')),
    PRIMARY KEY (regulator_id, doc_id, tag),
    CONSTRAINT fk_reg_doc_tags_document
        FOREIGN KEY (regulator_id, doc_id)
        REFERENCES reg_documents (regulator_id, doc_id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS ix_reg_doc_tags_tag ON reg_document_tags (tag);

-- ── reg_document_edges (cross-reference graph) ──────────────────────────────
CREATE TABLE IF NOT EXISTS reg_document_edges (
    id              BIGSERIAL    PRIMARY KEY,
    from_regulator  VARCHAR(64)  NOT NULL,
    from_doc        VARCHAR(128) NOT NULL,
    to_regulator    VARCHAR(64)  NOT NULL,
    to_doc          VARCHAR(128) NOT NULL,
    edge_type       VARCHAR(20)  NOT NULL
                    CHECK (edge_type IN ('implements','supersedes','interprets','references','consults_on')),
    confidence      REAL         NOT NULL DEFAULT 1.0,
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT now(),
    CONSTRAINT uq_reg_doc_edges
        UNIQUE (from_regulator, from_doc, to_regulator, to_doc, edge_type)
);
CREATE INDEX IF NOT EXISTS ix_reg_doc_edges_from ON reg_document_edges (from_regulator, from_doc);
CREATE INDEX IF NOT EXISTS ix_reg_doc_edges_to   ON reg_document_edges (to_regulator, to_doc);

-- ── reg_pending_edges (unresolved references) ───────────────────────────────
CREATE TABLE IF NOT EXISTS reg_pending_edges (
    id              BIGSERIAL    PRIMARY KEY,
    from_regulator  VARCHAR(64)  NOT NULL,
    from_doc        VARCHAR(128) NOT NULL,
    raw_reference   TEXT         NOT NULL,
    edge_type       VARCHAR(20)  NOT NULL,
    attempts        INTEGER      NOT NULL DEFAULT 0,
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT now()
);

-- ── reg_runs (per-regulator ingestion runs) ─────────────────────────────────
CREATE TABLE IF NOT EXISTS reg_runs (
    run_id         VARCHAR(128) PRIMARY KEY,          -- {date}_{regulator}_{short}
    regulator_id   VARCHAR(64)  NOT NULL REFERENCES reg_regulators(regulator_id),
    logical_date   DATE         NOT NULL,
    trigger        VARCHAR(16)  NOT NULL CHECK (trigger IN ('schedule','rerun','backfill')),
    status         VARCHAR(16)  NOT NULL CHECK (status IN ('running','success','success_empty','failed')),
    detected       INTEGER      DEFAULT 0,
    fetched        INTEGER      DEFAULT 0,
    ingested       INTEGER      DEFAULT 0,
    archived       INTEGER      DEFAULT 0,
    errors         INTEGER      DEFAULT 0,
    started_at     TIMESTAMPTZ  NOT NULL DEFAULT now(),
    finished_at    TIMESTAMPTZ,
    manifest_path  TEXT,
    operator       VARCHAR(128)                       -- set for reruns (audit)
);
CREATE INDEX IF NOT EXISTS ix_reg_runs_matrix ON reg_runs (logical_date DESC, regulator_id);

-- ── reg_watermarks (API poller position) ────────────────────────────────────
CREATE TABLE IF NOT EXISTS reg_watermarks (
    regulator_id  VARCHAR(64)  PRIMARY KEY REFERENCES reg_regulators(regulator_id),
    watermark     JSONB        NOT NULL,              -- e.g. {"last_published":"2026-07-29"}
    updated_at    TIMESTAMPTZ  NOT NULL DEFAULT now()
);

-- Note: operator audit for reruns/toggles uses the existing core `audit_log`
-- table (see sajha/db/models AuditLog) — no separate reg_audit_log.
