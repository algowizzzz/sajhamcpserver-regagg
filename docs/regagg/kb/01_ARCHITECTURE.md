# 01 — Architecture

## Design lineage

The original spec described a standalone Postgres + MinIO + Redis + Prefect
stack. **Deliberate, owner-approved deviation:** this was built *embedded* in
the SAJHA MCP server, reusing its tool registry (config-driven dynamic
discovery), storage abstraction and auth. That decision is why there is no
separate service to deploy and why `JSONFlex` exists.

## The one idea that shapes everything

**Selection is deterministic; narration is generated.**

Code decides what appears — which documents matched, which are serious, which
sources are stale. The model only writes prose *about* that selection, and
every generated sentence is validated against the evidence before it renders.
When validation fails the system falls back to a deterministic template and
says so.

This is why the product is usable in a bank. An analyst can ask "why is this
here?" of any card and get a mechanical answer (`why` on every dossier item:
`credit event +55; 2 sources +10`). And it is why the failure mode of a bad LLM
day is a plainer page, never a wrong one.

## End-to-end data flow (one source, one run)

```
YAML config ──► connector.detect(payloads)          # stateless; 3 engines:
                 │   sitemap_diff | rss | api        #  - lastmod fast-path skip
                 ▼                                   #  - backfill_cutoff filter
             DetectionEvents (url, title, date, ref, fetch_url, fallback_text)
                 │  meta-source dedup (fedreg vs agency copy, by reference)
                 ▼
             Fetcher (rate-limited, UA'd) ──► html_to_md | pdf_to_md(pypdf)
                 │   PDF detected by %PDF magic bytes, never by extension
                 │   bot-block guard → API abstract / metadata stub fallback
                 ▼
             CorpusVersioning.ingest()               # THE critical path:
                 │   new      → current/, v1         #  6-step atomic protocol
                 │   changed  → archive old, v(n+1)  #  crash-safe, chaos-tested
                 │   same hash→ no-op                #  reconcile() repairs
                 ▼
             rules.apply_rules()                     # deterministic enrichment:
                 │   reference numbers (B-13, SR 26-3, CAR-Ch4, NI 31-103…)
                 │   citation mining → graph edges (supersedes flips status)
                 ▼
             materiality.score()                     # deterministic priority
                 ▼
             projection.project_doc()                # write-through md mirror
                 ▼
             seen_urls + reg_runs updated (counter flush every 10 docs)
```

PDF harvesting: HTML pages yield same-domain PDF links (3/page, 40/run) which
enter the same queue as `source_kind=policy_pdf`.

## Two lanes, one pipeline

`reg_regulators.category` is `regulatory` or `news`. The same pipeline serves
both; the lane changes three things and nothing else:

| | regulatory | news |
|---|---|---|
| What is stored | full document text, PDFs, versions | headline + the publisher's own feed summary + link |
| Staleness window | 14 days | 3 days |
| Persona matching | entities **and** rule families | entities only |

**The news lane never stores article bodies.** That is a deliberate copyright
position, not a gap. It is why `excerpt.py` has a separate branch per lane and
why a news preview can be blank when a feed carries no summary.

## Layer map

```
┌─ collection ─────────────────────────────────────────────────────────┐
│ connectors · fetch · versioning · rules · materiality · projection   │
│ orchestrator · pipeline · verify_sources                             │
└──────────────────────────────────────────────────────────────────────┘
┌─ selection (deterministic) ──────────────────────────────────────────┐
│ extraction (entities, events) · matching (3-tier confidence)         │
│ dossier (what goes on a page + why) · materiality · schedule         │
└──────────────────────────────────────────────────────────────────────┘
┌─ narration (generated, validated) ───────────────────────────────────┐
│ myday.compose · ask · agent · focus.rank_by_prompt                   │
│ entity_table.classify/summarise                                      │
└──────────────────────────────────────────────────────────────────────┘
┌─ surfaces ───────────────────────────────────────────────────────────┐
│ admin.py (47 endpoints) · ui_dashboard.html · MCP tools · digital    │
│ worker                                                               │
└──────────────────────────────────────────────────────────────────────┘
```

## Modules, by job

Line counts are a rough guide to where the weight is.

**Collection**
| Module | Job |
|---|---|
| `connectors.py` (231) | three detection engines: sitemap_diff, rss, api |
| `fetch.py` (137) | rate-limited fetch; html→md; pdf→md by magic bytes |
| `versioning.py` (346) | the 6-step atomic ingest protocol + reconcile |
| `rules.py` (189) | reference grammars, citation mining, supersede edges |
| `materiality.py` (178) | deterministic priority score with a stated reason |
| `projection.py` (88) | write-through markdown mirror |
| `pipeline.py` (435) | wires the above into one run |
| `orchestrator.py` (110) | fleet fan-out with failure isolation |
| `verify_sources.py` (186) | the trust gate — run before onboarding a source |

**Selection**
| Module | Job |
|---|---|
| `extraction.py` (315) | entity index, event classification |
| `matching.py` (247) | watchlist matching, three-tier confidence |
| `dossier.py` (296) | what goes on a My Day page, and the `why` string |
| `schedule.py` (240) | when a run was expected — the six-state machine |
| `collection.py` (422) | coverage matrix, trends, rerun candidates |
| `health.py` (324) | freshness, funnel, quality checks, reliability |
| `corpus_index.py` (301) | lazily built BM25/TF-IDF index over the markdown |
| `excerpt.py` (221) | the first thing in a document worth reading |

**Narration**
| Module | Job |
|---|---|
| `myday.py` (361) | compose + validate the daily page spec |
| `ask.py` (224) | pinned-artifact chat, no-citation-no-claim |
| `agent.py` (257) | the agentic loop over corpus tools |
| `focus.py` (221) | filter deterministically, reorder by prompt |
| `entity_table.py` (313) | the sweep, classification, headline |
| `table_schema.py` (204) | user-declared columns and their coercion |
| `tavily.py` (215) | external news search + labelled stand-in |

**Surfaces**
| Module | Job |
|---|---|
| `admin.py` (1001) | every endpoint, plus the UI route |
| `ui_dashboard.html` | the entire front end — one file, no build step |
| `queries_ui.py` (928) | the read models the pages are built from |
| `runtime.py` (172) | contextvar-scoped session providers |
| `auth.py` (157) | sessions, users, persona ownership |

## Why the UI is one file

`ui_dashboard.html` is a single self-contained file with no build step and no
CDN dependencies. On-prem installs are frequently offline and frequently behind
a proxy that will not fetch a script. It is served fresh per request, so
editing it and reloading the browser is the whole dev loop.

The cost is that it is large. The mitigation is that it is organised in the same
order as the product: CSS grouped by page, then markup per view, then one
`load*()` per view. If you are adding a page, copy the shape of `v-hea`.

## Concurrency and sessions

`runtime.py` provides **contextvar-scoped** sessions, not thread-locals.
FastAPI runs sync endpoints in a threadpool, and thread-locals do not propagate
into it — that combination exhausted the connection pool once. Every tool call
and endpoint gets a session from `runtime.get_session()`.

## Security posture

- MCP `tools/call` requires auth; per-key tool allowlists are enforced at the
  route. Both were upstream gaps that were closed here.
- The agent key is DB-only with allowlist `["reg_*", "corpus_*"]`, stored as a
  JSON **string**. Never commit keys.
- The server is localhost-only. The SAJHA admin app still ships default
  credentials — **harden before any non-local exposure**.
- Explorer/`fs` endpoints are read-only and jailed to the corpus root; path
  traversal returns 400 and there is a test for it.
