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

## 2026-08-05 — Financial News lane (category: news)

20 verified world financial-news sources added as a second, distinct category
alongside the 30 regulators. Design decisions:

- **Copyright-safe by construction**: `fetch: feed_summary` builds each document
  from the publisher's own RSS feed (headline + summary + attribution link).
  The pipeline NEVER fetches article pages — `test_news_lane.py` proves it with
  a fetcher that raises on contact. Full text = a licensed feed (e.g. Factiva),
  which is a procurement conversation, not a crawler feature.
- **~50 stories/source/day**: `max_docs_per_run: 50` in config, honored by the
  pipeline when no explicit cap is passed (bnn 99→50, globe 91→50 on first run).
- **Distinct lanes everywhere**: `category: regulatory|news` on config + DB row;
  Coverage tree groups news under a "Financial News" section; Overview headline
  and tiles report "29/30 regulators and 20/20 news sources" separately.
- **Materiality**: `news_story` base 6 × `news_wire` tier 1.0 — headlines land
  Low/Medium and can never outrank binding rules from primary regulators.
- Sources: CBC, Globe & Mail, Financial Post, BNN Bloomberg, WSJ Markets, CNBC,
  MarketWatch, NYT Business, Yahoo Finance, Fortune, Business Insider Markets,
  American Banker, BBC, Guardian, FT, Economist, France 24 (Reuters retired its
  public feed), Nikkei Asia, SCMP, Economic Times. All 20 verified live
  2026-08-05; first ingest 536 stories, 0 errors. Suite: 105 tests green.

---

## Sessions 2026-08-07 → 2026-08-09 — the product layer

The corpus was done; these sessions built what sits on top of it. Every item
below has tests; the war stories are in `08_KNOWN_ISSUES_AND_ROADMAP.md`.

### Entity matching rewritten (three-tier confidence)
Recall was 68% with a false positive — "Meta", "Uber", "AMD", "JP Morgan"
missed while "Apple Hospitality REIT" matched "Apple Inc.". Rewritten as
confirmed / possible / none, so ambiguity is an outcome rather than a coin
flip. 100% recall on 22 variants, 0 false confirmations on 8 confusable pairs.
The first version was 80× slower; candidate indexes by first token and
name-head fixed it.

### `corpus_*` tools and the digital worker
Ten tools over the markdown projection — list, read, read-many, keyword, BM25,
TF-IDF similar, changes, entity lookup, stats — with no embedding service
required. `agent.py` runs an agentic loop over them; `w-riskgpt` registered in
the agent platform with all 22 tools, discovered from the registry rather than
hard-coded.

### Tool contracts validated from their own schemas
`corpus_changes` accepted a `source` filter and ignored it; the worker noticed
and reconstructed the answer by hand. Now an argument a tool does not implement
is rejected with a message naming the accepted parameters, driven by each
tool's `inputSchema`. Building the guard surfaced four more tools whose
implemented filters were never advertised.

### The schedule declared to the app
`config/regagg_schedule.yaml`. The scheduler is external, so an empty day was
ambiguous — a quiet Saturday and a dead scheduler looked identical. Six states
now, and an unscheduled gap is drawn as expected rather than as a fault.

### Collection and Health rebuilt
Built for the person accountable for freshness. Building them against real data
contradicted three things the old pages claimed: the run counters are not a
partition, run duration is unusable (87% of runs finish before they start), and
reliability disagreed with the coverage matrix because it pooled both
categories. It immediately surfaced that regulatory collection had been down
for three scheduled days.

### My Day rebuilt as three columns
Persona chips → a dropdown; five stat tiles → one line; stacked sections →
serious / watch / not-on-this-page, each scrolling in place. Every card gained
a preview from its own document, which needed a lane-aware excerpt extractor:
the news lane stores only the publisher's summary, and the first 300 characters
of an OSFI guideline is a postal address.

### The focus bar
Entities and sources filter deterministically; a prompt may only reorder and
narrate. A focused view is ephemeral and never overwrites the cached daily
page, which is a record someone may already have acted on.

### The entity table
One row per watched name — 500 entities, 500 rows, including the quiet ones.
Columns declared by the desk in YAML, filled by the model, coerced against the
declared set so a near-miss becomes `unknown`. Reading spends nothing; the
sweep is an explicit click with the credit count shown first. Without a Tavily
key it produces demo rows marked at three levels plus an undismissable banner.

### Layout and chat polish
Auto-fit pages that never scroll the window, with the `mainlist` / `scrollbox`
split after 16,238px of change feed was found trapped behind a 340px box. A
resizable chat dock whose stored width survives a narrow window. Chat sources
moved into the answer bubble as links to the article — which exposed that the
sources shown were not the sources used.

### Documentation and cleanup (2026-08-09)
This knowledge base rewritten from `docs/regagg/kb/`'s 2026-08-04 state, plus a
`testing/` subfolder. Removed 520 KB of superseded material: 11 design mockups,
the stale sprint/status PM pack and its generator, an old verification report.
Deliberately **not** removed: 31 orphaned tool implementations under
`sajha/tools/impl/`, because `tools_registry.py` and the studio import several
directly.

**State at close:** 257 Python + 75 browser tests green; 7,018 documents;
55 sources; 22 MCP tools.
