# Regulatory Intelligence Aggregator — Build Log (epic by epic)

An on-prem pipeline that tracks ~30 financial regulators, keeps a normalized,
versioned document corpus current daily, enriches each document
(tags/summary/cross-reference graph), and serves it to the chatbot through
stateless MCP tools. **Built embedded in this SAJHA repo** (not a separate
stack), following the repo's own conventions.

Spec source: the handover doc set (`00_INDEX` … `06_SOURCE_MAP` + 30 regulator
YAMLs). This log records what was implemented against each epic.

## Build decisions (2026-08-02)
| Decision | Choice | Why |
|---|---|---|
| Topology | **Embedded** in `sajhamcpserver` | reuse tool registry (dynamic discovery / REQ-14), storage backend, web-crawler primitives, cache/circuit-breaker, `sajha/ai` |
| Scheduler | **Prefect** (sidecar) | repo had no scheduler; Prefect gives flows/retries/rerun API |
| Datastore | **PostgreSQL** | relational versioning/edges/FKs; repo already had psycopg2 + `db.type` switch |

Deliberate deviations from the literal spec (all documented in code):
- Dropped the parallel Postgres+MinIO+Redis+Prefect *stack*; build lives inside the repo.
- Corpus tables namespaced `reg_*` on the shared SQLAlchemy `Base` (repo's "models are the single source of truth"), so `create_all()` provisions them; a hand-authored `db/scripts/postgresql/003_regagg_schema.sql` covers the `psql` path.
- `doc_id` fallback is a hash of the **URL**, not the content hash — the spec's literal "first 16 hex of content hash" would change on every edit and break versioning (URL is the stable identity; content hash stays the change-detection signal).

## Test status — all deterministic gates green
```
38 passed   (tests/regagg/)         + Foundation gate GREEN
```
Run: `./.venv/bin/python -m pytest tests/regagg/ -q`

Gates that need **live infrastructure** (network to regulators, LLM keys, running
Postgres/Prefect, human eval labels) are marked **READY — needs infra** below:
the code + deterministic offline tests are done; the live sign-off can't be
produced from a dev box.

---

## Epic 1 — Foundation ✅ gate GREEN
- **Code:** `sajha/regagg/config_models.py` (pydantic v2, strict), `config_loader.py`,
  `models.py` (9 `reg_*` SQLAlchemy tables), `config/regulators/*.yaml` (30) +
  `_taxonomy.yaml` + `_settings.yaml`, `db/scripts/postgresql/003_regagg_schema.sql`,
  one-line registration in `sajha/db/models/__init__.py`.
- **Gate:** `scripts/regagg_verify_foundation.py` → 30/30 configs parse & validate,
  taxonomy matches code `DOC_TYPES`, 9 `reg_*` tables create on a real DB.

## Epic 2 — Versioning / storage (hardest invariant first) ✅
- **Code:** `ids.py`, `corpus_storage.py` (layout over `get_storage()`),
  `versioning.py` — the 6-step atomic override→archive protocol + `reconcile()` +
  `check_invariants()`.
- **Tests (`test_versioning.py`, 10):** create→update archives previous; unchanged
  is a no-op; **chaos: crash injected after every step 1–5 → reconcile restores
  "exactly one current + prior archived + zero committed-data loss"**; reconcile
  idempotent.

## Epic 3 — Connectors + fetch ✅
- **Code:** `events.py`, `fetch.py` (HTML/PDF→md, hashing, rate limiter, injectable
  opener), `connectors.py` (`sitemap_diff` / `rss` / `api` + factory),
  `pipeline.py` (`run_regulator`: detect→fetch→version→seen_urls→manifest, with
  sitemap-index recursion + lastmod fast-path).
- **Tests (`test_connectors_pipeline.py`, 7):** each connector's detection & doc_type
  mapping; **OSFI end-to-end on fixtures incl. a forced content change that archives
  v1** (the Epic-2/3 gate); same-day rerun idempotent.
- **Live gate — READY, needs infra:** live OSFI/Fed/FedReg e2e (network).

## Epic 4 — Scheduling / orchestration ✅
- **Code:** `orchestrator.py` (`run_daily` fan-out with per-regulator failure
  isolation, `rerun`, `reconcile`), `flows_prefect.py` (thin optional Prefect
  wrapper; core stays pure-Python so it's testable without Prefect).
- **Tests (`test_orchestrator.py`, 2):** one regulator's failure doesn't affect
  others; rerun subset idempotent + operator recorded; reconcile clean.
- **Live gate — READY, needs infra:** 5 consecutive unattended daily Prefect runs.

## Epic 5 — Enrichment ✅
- **Code:** `enrichment.py` — strict pydantic output schemas, `LLMBackend`
  abstraction (`MockLLM` deterministic for tests; `AnthropicBackend` wires
  `sajha/ai` in prod), `Enricher` (classify → summarize+dates → graph extract →
  reference resolution → edges/pending_edges; `supersedes` flips target status;
  invalid JSON → 1 retry → `enrichment_pending`).
- **Tests (`test_enrichment.py`, 3):** classification/taxonomy-tags/date
  extraction/supersedes edge + status flip; unresolved ref → `pending_edges`;
  bad LLM output → `enrichment_pending`.
- **Live gate — READY, needs infra:** 150-doc golden-set eval (tagging ≥90 %,
  doc_type ≥92 %, dates ≥95 %) — needs human labels (Durga/Archana) + a real model.

## Epic 6 — MCP retrieval tools ✅
- **Code:** `sajha/tools/impl/reg_tools.py` (`reg_search / reg_read / reg_tags /
  reg_whats_new / reg_graph` on `BaseMCPTool`), `queries.py` (shared read layer),
  `runtime.py` (per-request providers), `config/tools/reg_*.json` (generated by
  `scripts/regagg_gen_tool_configs.py`).
- **Tests (`test_mcp_tools.py`, 6):** each tool against a seeded, enriched corpus;
  generated configs valid; **all 5 resolve via the registry's dynamic-discovery
  path** (importlib smoke).
- **Note:** search ranking uses a portable filter-then-rank fallback; prod delegates
  ranking to the existing SAJHA BM25 tool (same filter stage).

## Epic 7 — Admin API ✅
- **Code:** `admin.py` — FastAPI router: coverage matrix, regulator drill-down +
  staleness, run manifest, `rerun` (audited, Prefect-triggered), `toggle` (audited),
  review queue, integrity/reconcile. Mount with `app.include_router(create_admin_router())`.
- **Tests (`test_admin.py`, 5):** coverage matrix, drill-down/runs, rerun & toggle
  write to the core `audit_log` with operator identity, integrity OK.
- **UI:** the HTMX/Jinja screens (05_ADMIN_UX) render on these JSON endpoints (the
  endpoints are the tested contract).

## Epic 9 — Source verification harness ✅
- **Code:** `verify_sources.py` (reachability + content-type + parseability +
  freshness per source; report + onboarding gate), CLI `scripts/verify_sources.py`
  (real HTTP; the only network-touching step).
- **Tests (`test_verify_sources.py`, 6):** pass/warn(stale)/fail(content-type,
  unreachable, 404, thin listing) across sitemap/feed/api/listing; report render.
- **Live gate — READY, needs infra:** run across all 30 live sites; all ship
  `verified: false` until it passes them (invariant #4). Failures escalate to Saad.

---

## Session 2 (2026-08-02, evening) — data-layer completion + live v2 UI

Scope narrowed by Saad: **data layer + tracking UI only** (scheduling, MCP
registration, chatbot, LLM enrichment, enterprise deploy owned elsewhere).
Retrieval tools remain as built. 83 tests green.

### Phase A — capture completeness (data layer)
- `reg_documents.source_kind` (web | policy_pdf) + migration `regagg_migrate_001_source_kind.py`
- **PDF harvesting**: same-domain PDF links on ingested HTML pages are enqueued
  (3/page, 40/run) and ingested as `policy_pdf` docs; PDF detection by `%PDF`
  magic bytes; blank/scanned PDFs flagged `ocr: true`
- **Meta-source dedup** (`meta_source: true` on fedreg): agency copy canonical,
  Federal Register duplicate skipped + counted (`manifest.deduped`)
- **Federal Register API pagination** (next_page_url, ≤5 pages) + **backfill
  cutoff** enforced in RSS + API connectors (US-1.2 AC4)
- **Deterministic enrichment** (`rules.py`, no LLM): reference-number grammar
  for OSFI/CAR/LAR/SR/OCC/FIL/NI/APS/PS-CP-SS/RTS-ITS/BCBS/SEC; citation mining
  with sentence-scoped supersede detection; edges @0.8 confidence;
  `supersedes` flips target status; pending-edge resolver
- **Live run counters**: `reg_runs` row flushed every 10 docs (UI polls it)

### Phase B — source fixes (29/30 verified)
- Verifier now recognizes **sitemap indexes** (un-blocked CSA: 266 docs)
- FDIC feed moved → `/rss.xml` (found by discovery probe)
- HKMA RSS dead → switched to `sitemap_diff` scoped by include_patterns
- AMF Québec 403 bot-block: escalated, not evaded — the one open source issue

### Phase C — live v2 dashboard (replaces raw v1 page)
- `queries_ui.py` + endpoints: `/tree` (region→institution→source-kind roll-ups),
  `/browse/{id}` (facets + filters + search), `/changes` (new/revised/superseded/
  deadline feed), `/documents/{r}/{d}/diff` (unified diff vN-1→vN),
  `/documents/{r}/{d}/content`, `/runs-overview` (active + recent + daily delta),
  `/inventory/{id}`
- `ui_dashboard.html` served at `/api/regagg/ui`: Coverage tree / Changes feed /
  Collection-runs monitor (5s polling while active), document drawer
  (markdown/summary/provenance), diff viewer, per-scope Run buttons, dark mode
- Route lesson: `/runs/{run_id}` captures `/runs/overview` → `/runs-overview`

### Phase D — completeness proof + fixtures
- **Expected-inventory reconciliation**: `config/regulators/_inventories/osfi.yaml`
  (CAR 9 · LAR 5 · B-series 8 · E-series 8; `verified_against_site: false` until
  human-confirmed) + `/inventory/{id}` — answers "do we have every chapter?"
- **Recorded fixtures for 29/30** (`scripts/regagg_record_fixtures.py`, 9.6MB)
  + parametrized connector tests over the real payloads
- `scripts/regagg_backfill_rules.py`: post-crawl rules + source_kind backfill

## Not yet built (remaining spec scope)
- **Epic 8 hardening:** 50k-doc load test, backup+restore drill, egress allow-list
  submission — all need the live stack.
- **Admin HTML/HTMX** screens on top of the JSON endpoints.
- **PDF/OCR fetch path** (`pdf_to_md` stubbed behind optional `pypdf`; tesseract OCR TODO).
- **BM25 wiring** to the SAJHA index (fallback ranker in place).

## How to run
```bash
cd sajhamcpserver
python -m venv .venv && ./.venv/bin/pip install -r requirements.txt feedparser markdownify
./.venv/bin/python scripts/regagg_verify_foundation.py     # Foundation gate
./.venv/bin/python -m pytest tests/regagg/ -q              # 38 tests
./.venv/bin/python scripts/verify_sources.py --regulator osfi   # live source check (network)
```

## Wiring into the running server (prod)
1. `db.type: postgresql` in `config/application.yml`; run `db/scripts/postgresql/001_schema.sql` then `003_regagg_schema.sql` (or let `create_all()` provision).
2. At startup call `sajha.regagg.runtime.wire_from_app()`.
3. `app.include_router(sajha.regagg.admin.create_admin_router())`.
4. `pip install prefect` and `python -m sajha.regagg.flows_prefect deploy` for the 06:00 daily fan-out.
5. Choose the LLM backend in `config/regulators/_settings.yaml` and wire `AnthropicBackend` to `sajha/ai`.
6. Run `scripts/verify_sources.py`, review the report, flip verified sources, then activate regulators.
