# 04 — API Reference

All routes are defined in `sajha/regagg/admin.py` under prefix **`/api/regagg`**.
47 endpoints. Auth is a signed session cookie from `POST /auth/login`; mutating
routes also take an `X-Operator` header and write an audit row.

## Identity

| Method | Path | Notes |
|---|---|---|
| POST | `/auth/signup` | creates a user in `reg_users` |
| POST | `/auth/login` | sets the session cookie |
| POST | `/auth/logout` | |
| GET | `/auth/me` | current user, or 401 |

## Personas

| Method | Path | Notes |
|---|---|---|
| GET | `/personas` | the caller's personas, plus shared ones |
| GET | `/personas/{persona_id}` | one persona, with entity count |
| POST | `/personas` | create or update; bumps `version_n`, writes a `reg_persona_versions` row |
| GET | `/personas/starters` | the four starter templates |
| GET | `/desks` | every persona at a glance |

## My Day

| Method | Path | Notes |
|---|---|---|
| GET | `/myday` | `?persona_id=&day=&refresh=true` — cached per persona per day; `refresh` rebuilds |
| GET | `/myday/item/{cluster_key}` | one card's full evidence |
| POST | `/myday/focus` | **ephemeral** filtered view; never writes. Body: `{persona_id, day, prompt, entities[], sources[]}` |
| POST | `/ask` | grounded chat. `mode:"agent"` runs the tool loop; otherwise answers from a pinned artifact |

`refresh=true` is how you pick up a code change that alters the dossier — the
page is cached, so a new field will not appear until the page is rebuilt.

## Entity table

| Method | Path | Notes |
|---|---|---|
| GET | `/entities/table` | `?persona_id=&day=&status=&q=&summary=true` — **reads cache only, spends nothing** |
| POST | `/entities/sweep` | **costs money.** Body: `{persona_id, day, budget, depth, days, refresh, classify}` |

The split is deliberate: page load must never trigger a billed search.

## Collection and Health

| Method | Path | Notes |
|---|---|---|
| GET | `/collection/overview` | `?lane=&days=7&trend_days=30` — today bar, matrix, trends, arrived, candidates. One call so every panel shares a clock |
| GET | `/health/overview` | verdict, freshness, funnel, quality, reliability, attention |
| GET | `/schedule` | the declared schedule and the next run time |
| GET | `/runs-overview` | active + recent runs, daily delta |
| GET | `/runs-trend` | `?days=14&category=` |
| GET | `/runs/{run_id}` | one run, with its manifest |
| GET | `/regulators/{id}/runs` | run history for one source |
| POST | `/rerun` | `{scope:"all"\|"ids", ids[], date, max_docs, include}` — spawns a detached run, refuses if one is active |
| POST | `/regulators/{id}/toggle` | activate / deactivate a source |
| GET | `/integrity` | runs reconcile and reports |

## Corpus reads

| Method | Path | Notes |
|---|---|---|
| GET | `/tree` | `?days=7` — coverage tree: region → source, with freshness |
| GET | `/coverage` | coverage matrix |
| GET | `/corpus` | full-corpus browse with facets and filters |
| GET | `/browse/{regulator_id}` | one source's documents |
| GET | `/changes` | `?days=&region=&category=&kinds=&min_band=&date_from=&date_to=` |
| GET | `/whats-new` | shorthand change feed |
| GET | `/overview` | lane overview numbers |
| GET | `/news` | the news dashboard read model |
| GET | `/exec/summary` · `/exec/regulatory` · `/exec/news` | executive read models |
| GET | `/inventory/{regulator_id}` | expected-inventory reconciliation |
| GET | `/review-queue` | documents flagged `enrichment_pending` |
| GET | `/corpus/doc/{doc_id}` | resolve a bare doc_id to its source |
| GET | `/documents/{reg}/{doc}/content` | `?mode=summary\|full\|meta\|raw` |
| GET | `/documents/{reg}/{doc}/diff` | unified diff v(n-1) → v(n) |

## Documents in, files out

| Method | Path | Notes |
|---|---|---|
| POST | `/documents` | manual add by URL or pasted markdown |
| POST | `/documents/upload` | multipart PDF/HTML |
| GET | `/fs` | file tree — read-only, jailed to the corpus root |
| GET | `/fs/file` | one file; path traversal returns 400 |
| GET | `/ui` | the dashboard itself |

## Conventions

**Read models are assembled server-side.** `/collection/overview` and
`/health/overview` each return everything their page needs in one response.
This is not premature optimisation — the panels make claims about the same
instant, and a today bar reading "not scheduled" beside a matrix that had
already rolled over is worse than either alone.

**Failures are values, not exceptions.** Endpoints that depend on an LLM or an
external service return a payload with the reason (`generator: "unconfigured"`,
`ranked: false, reason: "…"`) rather than a 500. The page then shows the
deterministic content and states what is missing.

**Nothing mutates on a GET.** `/entities/table` will not sweep;
`/myday/focus` is a POST only because it carries a free-text body.
