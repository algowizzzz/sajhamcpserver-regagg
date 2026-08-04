# 01 — Architecture, Data Flow, Schema

## Design lineage
Original spec: the handover doc set (BRD/PRD/TRD/data-schema/UX/source-map)
written for a standalone Postgres+MinIO+Redis+Prefect stack. **Deliberate
deviation (owner-approved):** built *embedded* in the SAJHA MCP server instead,
reusing its tool registry (config-driven dynamic discovery), storage
abstraction, and auth. Scheduling/LLM/chatbot are owned by the user's external
stack; this system is the **data layer + tracking UI + MCP surface**.

## End-to-end data flow (one regulator, one run)
```
YAML config ──► connector.detect(payloads)          # stateless; 3 engines:
                 │   sitemap_diff | rss | api        #  - lastmod fast-path skip
                 ▼                                   #  - backfill_cutoff filter
             DetectionEvents (url, title, date, ref, fetch_url, fallback_text)
                 │  meta-source dedup (fedreg vs agency copy, by reference)
                 ▼
             Fetcher (rate-limited, UA'd) ──► html_to_md | pdf_to_md(pypdf)
                 │   PDF detection by %PDF magic bytes (never trust extension)
                 │   bot-block guard → API abstract / metadata stub fallback
                 ▼
             CorpusVersioning.ingest()               # THE critical path:
                 │   new → current/, v1               #  6-step atomic protocol
                 │   changed → archive old, v(n+1)    #  crash-safe (chaos-tested)
                 │   same hash → no-op                #  reconcile() repairs
                 ▼
             rules.apply_rules()                     # deterministic enrichment:
                 │   reference numbers (B-13, SR 26-3, CAR-Ch4, NI 31-103…)
                 │   citation mining → graph edges (supersedes flips status)
                 ▼
             projection.project_doc()                # write-through md mirror
                 ▼
             seen_urls + reg_runs updated (mid-run counter flush every 10 docs)
```
PDF harvesting: HTML pages yield same-domain PDF links (3/page, 40/run) which
enter the same queue as `source_kind=policy_pdf` documents.

## Storage layout (canonical — data/web_aggregator/)
```
{regulator}/
  _state/run_manifests/{run_id}.json      # per-URL log of every run
  current/{doc_type}/{year}/{doc_id}/
    raw.html|raw.pdf                      # original bytes, immutable
    content.md                           # normalized markdown
    meta.json                            # full provenance (see below)
    summary.md                           # empty until LLM layer fills it
  archive/{doc_type}/{year}/{doc_id}/{version_ts}/   # append-only history
  staging/                               # transient; reconcile cleans crashes
```
meta.json carries: doc_id, title, reference_number, source_url, final_url,
fetch_method, content_source (api_abstract|metadata_stub when bot-gated),
content_hash (sha256), version_ts/version_n, ingested_at, run_id, ocr, tags.

## Markdown projection (agent consumption — data/markdown/)
```
web/{regulator}/{doc_type}/{doc_id}.md      # HTML-converted
policy/{regulator}/{doc_type}/{doc_id}.md   # PDF-converted
```
YAML frontmatter (title/regulator/reference/source_url/published/version) on
every file. Maintained by write-through at ingest + nightly `resync()`
self-heal. This is a PROJECTION of current/ only — history lives in canonical.

## Database (SQLite data/sajha.db; Postgres DDL ready in
## db/scripts/postgresql/003_regagg_schema.sql)
9 tables, all prefixed `reg_`, defined in `sajha/regagg/models.py` on the
shared SQLAlchemy Base (auto-created at startup):
| Table | Role |
|---|---|
| reg_regulators | registry (jurisdiction, connector, active, staleness) |
| reg_seen_urls | change detection (url → hash, lastmod, doc_id) |
| reg_documents | ONE current row per doc (source_kind web/policy_pdf, status) |
| reg_document_versions | full history; invariant: exactly one state='current' |
| reg_document_tags | config/llm/rule/manual-sourced tags |
| reg_document_edges | citation graph (implements/supersedes/…, confidence) |
| reg_pending_edges | unresolved citations, retried nightly |
| reg_runs | every run: counts, status, trigger, operator (audit) |
| reg_watermarks | API poller position |

Run status semantics: `failed` ONLY when nothing landed or >20% errored;
scattered per-URL errors (regulator-side 404s/429s) = `success` + error count.

## Key modules (sajha/regagg/)
config_models/config_loader (pydantic, strict) · connectors · fetch ·
pipeline · versioning (+reconcile/chaos) · rules (no-LLM enrichment) ·
projection · enrichment (LLM slot; MockLLM used) · queries/queries_ui ·
admin (API + dashboard) · runtime (thread-scoped session providers, rerun
spawner) · manual (human override lane) · verify_sources · orchestrator.

## Security model (current)
- MCP `tools/call` REQUIRES auth; per-key tool allowlists ENFORCED at the
  route (both were upstream gaps we closed). Discovery stays open.
- Agent key: DB-only, allowlist `reg_*`. Rotated 2026-08-03; never commit keys.
- Server is localhost-only; SAJHA admin still has default creds — HARDEN
  (password, TLS, bind) before any non-local exposure.
- Explorer/fs endpoints are read-only and jailed to the corpus root.
