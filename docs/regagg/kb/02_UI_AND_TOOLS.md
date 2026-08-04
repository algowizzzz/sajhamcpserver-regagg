# 02 — UI Pages, Endpoints, MCP Tools

## Dashboard (sajha/regagg/ui_dashboard.html → GET /api/regagg/ui)
Single-file app (no build step, no CDN deps — self-contained for on-prem),
hash-routed pages, dark/light aware, served fresh per request (edit → reload).

| Page (hash) | Job | Backed by |
|---|---|---|
| Coverage `/ui` | trust map: region → institution rows with web/PDF counts, new-in-window, last run, status pill, **coverage % vs advertised**, per-row ▶ Run | `/tree` |
| Corpus `#corpus` | full-corpus browser: continent/institution/file-type/doc-type/status/date/search filters, facet counts, excerpt+title rows, Published+Added columns, pagination, ＋Add document | `/corpus` |
| Explorer `#exp` | nested file tree mirroring disk (regulator→current\|archive→doc_type→year→doc→artifacts); md renders rich, raw.* downloads | `/fs`, `/fs/file` |
| Changes `#chg` | analyst delta feed: NEW/REVISED/SUPERSEDED/DEADLINE cards, region/institution/file-type/kind-chip/date filters, **View diff** | `/changes`, `/documents/{r}/{d}/diff` |
| Collection runs `#run` | ops: **Today's delta banner (pass-rate headline)**, live run w/ 5s polling + progress, recent runs, daily delta table | `/runs-overview` |

Shared: document drawer (Document=rich md / Summary / Provenance / Raw tabs),
diff viewer (green/red unified), add-document modal (URL fetch \| paste md \|
upload PDF), toasts. UX journeys: analyst = Coverage→drill→doc→diff;
operator = Runs→red row→manifest→rerun.

## Admin/API endpoints (sajha/regagg/admin.py, prefix /api/regagg)
Read: `/tree` `/corpus` `/browse/{reg}` `/changes` `/whats-new`
`/documents/{r}/{d}/content|diff` `/inventory/{reg}` `/runs-overview`
`/regulators/{id}` `/runs/{run_id}` `/coverage` `/review-queue` `/integrity`
`/fs` `/fs/file`.
Mutating (audited, X-Operator header): `POST /rerun` (spawns real ingest,
single-run guard) · `POST /regulators/{id}/toggle` · `POST /documents`
(manual add via URL/markdown) · `POST /documents/upload` (multipart PDF/HTML).

## MCP tools (sajha/tools/impl/reg_tools.py + config/tools/reg_*.json)
Registered via SAJHA's config-driven dynamic discovery; regenerate configs with
`scripts/regagg_gen_tool_configs.py`. All stateless (thread-scoped session per
call via sajha/regagg/runtime.py). Auth: X-API-Key; key allowlist `reg_*`.

**Index plane (unique to this system — the user's RAG/BM25 owns content):**
| Tool | Answers |
|---|---|
| reg_coverage | corpus trust map: counts, freshness, coverage % by institution |
| reg_browse | metadata listing w/ full filters + facets (NO content) |
| reg_changes | new/revised/superseded/deadlines in a window, filtered |
| reg_diff | unified diff v(n-1)→v(n) of any revised document |
| reg_inventory | expected-inventory reconciliation ("all 9 CAR chapters?") |
| reg_runs_status | collection health: active runs, history, daily delta |
| reg_trigger_run | **MUTATING**: start a run (all/subset/capped/URL-scoped) |

**Content plane (kept; user's md tools may supersede):**
reg_search (filter-then-rank keyword) · reg_read (summary|full|meta|version) ·
reg_tags · reg_whats_new · reg_graph (citation traversal, depth≤3).

MCP endpoint: POST /mcp (SSE /mcp/sse, WS /mcp/ws). tools/call requires auth;
per-key allowlist enforced in sajha/routes/api_routes.py.

## Design language (if extending the UI)
Neutral bank palette (--blue #0f5aa9 accents only), status = pill + icon +
text (never color alone), tabular numerals for counts, progressive disclosure
(region → institution → source → doc), every count clickable to its evidence,
"honesty strips" show denominators (X of Y) rather than bare successes.
