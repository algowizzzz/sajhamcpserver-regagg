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
