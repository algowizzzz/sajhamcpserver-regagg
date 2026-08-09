# Results — recorded runs and measurements

Everything below was executed against the running system. Where a number is
quoted, it came from that run.

## Automated suites — last full run 2026-08-09

```
./.venv/bin/python -m pytest tests/regagg -q      →  299 passed in 7.5s
bash tests/ui/run_suite.sh                        →   76 passed in 6.6m
./.venv/bin/python scripts/regagg_verify_foundation.py  →  gate green
```

## Backfills, measured

| | Before | After | How |
|---|---|---|---|
| Documents with an extraction | 1,089 (15%) | **7,353 (100%)** | `regagg_extract_backfill.py`, 6,264 in 799s at 8 workers, 2 provider errors |
| Naming a watchlist company | 464 | **1,306** | consequence of the above |
| Documents with a publication date | 26% | **63%** | `regagg_backfill_dates.py` — 932 from URL paths, 1,815 from text; 2,472 have none anywhere |
| Runs with a usable duration | 17 of 127 | **47 of 157** | the timestamp fix; the 30 new runs all correct |
| Corpus | 7,018 | **7,353** | regulatory recovery run, 438 documents across 30 sources |

The first extraction attempt **lost all 5,929 results** to `database is locked`
— a collection run held the SQLite write lock and the script committed once at
the end. It commits every 200 rows with backoff now, and the re-run completed.

Python tests by file:

| File | n | | File | n |
|---|---|---|---|---|
| test_recorded_fixtures | 30 | | test_entity_recall | 9 |
| test_entity_table | 24 | | test_auth_personas | 9 |
| test_schedule | 19 | | test_news_lane | 8 |
| test_extraction_dossier | 19 | | test_rules_and_capture | 7 |
| test_focus | 18 | | test_materiality | 7 |
| test_collection_health | 17 | | test_verify_sources | 6 |
| test_mcp_tools | 15 | | test_connectors_pipeline | 6 |
| test_ui_endpoints | 13 | | test_admin | 5 |
| test_excerpt | 13 | | test_fetch | 4 |
| test_versioning | 10 | | test_enrichment | 3 |
| test_ask | 10 | | test_dashboard_markup | 3 |
| | | | test_orchestrator | 2 |

Browser tests: `01-auth` 8 · `02-personas` 7 · `03-navigation` 7 ·
`04-myday` 15 · `05-onboarding` 7 · `06-maintenance` 29.

## Measurements taken against the real corpus

### Entity matching (`test_entity_recall.py`)

| | Before rewrite | After |
|---|---|---|
| Recall on 22 name variants | 68% | **100%** |
| False confirmations on 8 confusable pairs | 1 | **0** |
| Suite wall clock | 4s | 4.9s (first attempt: 5.5 min) |

### Excerpt coverage (300-document sample per lane)

| Lane | Preview produced | Median length |
|---|---|---|
| News | 249 of 300 (**83%**) | 142 chars |
| Regulatory | 229 of 300 (**76%**) | 195 chars |

Blanks are correct: a Yahoo feed carrying headline only, or a JFSA file that is
a list of statute names, genuinely has no prose to preview.

### Corpus index

7,353 documents indexed in ~4s. Rebuilt when file count or newest mtime
changes, so a poll is picked up without a restart.

### Data quality — before the backfills (2026-08-09, morning)

Kept as the baseline the numbers above are measured against.

| Check | Count | Of |
|---|---|---|
| No publication date | 5,219 | 7,018 (74%) |
| No extraction | 5,969 | 7,018 (85%) |
| Runs with `finished_at < started_at` | 110 | 127 (87%) |
| ~~Runs where `ingested + archived > fetched`~~ | 6 | 127 — **not a defect**; event counters may exceed the whole |
| Sources with spelled-out jurisdiction | 10 | 55 |
| Orphaned versions / untitled / missing hash | 0 | — |

### Run-counter invariants (all 127 runs)

| Claim | Holds? |
|---|---|
| `fetched <= detected` | ✅ always |
| `errors <= detected` | ✅ always |
| `ingested + archived <= fetched` | ❌ 6 violations |
| `detected == fetched + errors` | ❌ 23 violations |

This is why the Health funnel presents a funnel and not a balancing identity.

## Live acceptance runs — the digital worker

Against the real corpus, through the UI chat, with DeepSeek configured.

| Question | Calls | Result |
|---|---|---|
| "what changed in OSFI recently" | 20 → **8** after the `corpus_changes` filter fix | DSB cut to 3.0%; open consultations with closing dates |
| "what are the major changes happening at OSFI" | 25 | DSB 3.0%, CET1 expectation 11%, banks averaging 13.5% |
| "can you tell me the latest news about SoftBank" | 5 | three stories via entity lookup then read |
| "what is SpaceX going through" | 4 | post-IPO earnings, 7× capex on AI |
| "I'm a credit risk analyst — what should I be worried about?" | 25 | CRE as top risk; OSFI's open Credit Risk Management consultation (closes 2026-07-29) |

The worker also self-reported a corpus defect unprompted: *"the OSFI documents
in this corpus do not carry populated publication dates… so I could not run a
clean 'what's new in the last N days' query."* That is issue 1 in
`08_KNOWN_ISSUES_AND_ROADMAP.md`, found by the worker rather than by us.

### Focus bar, live

Prompt *"which of these could hit deposit funding or bank capital"* over 16
items: all 16 preserved, Warren/OCC and the CRA proposal ranked to the top,
note validated and shown. Source-only filter `american_banker`: 16 → 4 cards,
with `dropped_no_source_match: 12` reported.

### Entity table, live (demo mode)

12 entities → 12 rows: 5 with news, 7 explicitly quiet. Declared columns
`event / rating_impact / action` filled and coerced. Headline generated and
validated. `credits: 0`, `mode: demo`, banner shown.

## Layout verification (1440×900)

Measured `scrollHeight - innerHeight` per view after the auto-fit work:

| View | Page scroll | Note |
|---|---|---|
| Collection | 0 | fits, panels scroll internally |
| Health | 0 | fits |
| My Day | 0 | fits |
| Entity table | 0 | fits |
| What changed | 16,031 | list page — the window scrolls, correctly |
| Today's stories | 26,093 | list page |
| Documents | 2,623 | list page |
| Regulators | 0 | fits |

Before the `mainlist` fix those same list pages showed **0 page scroll with
16,238px trapped** inside a 340px box.

## Regression tests verified to fail on the original bug

Not vacuous — each was run against the broken state:

| Test | Reproduced by |
|---|---|
| `test_dashboard_markup` balance + containment | re-injecting the stray `</div>` → both fail |
| letterbox test | re-imposing the 340px cap on `#chgFeed` → 16,238px hidden, page frozen, check fires |
| `corpus_changes` source filter | schema without `source` → rejection message names the accepted parameters |
| `test_content_containers_keep_their_layout_class` | passes on the pre-fix file only because that file predates the bug; the other two do not |
