# Python suites — 371 tests

```bash
./.venv/bin/python -m pytest tests/regagg -q        # all, ~7s
./.venv/bin/python -m pytest tests/regagg/test_focus.py -q -v
```

Fixtures live in `tests/regagg/conftest.py`: in-memory SQLite with only the
`reg_*` tables, plus a tmp-dir corpus storage. Network is always injected.

## Collection layer

### `test_versioning.py` — 10
The 6-step atomic ingest protocol: create, update, archive. **Chaos test: a
crash is injected after every step and `reconcile()` must restore the
invariants with zero loss.** Idempotent reconcile.
*Protects:* the one place data can actually be lost.

### `test_connectors_pipeline.py` — 6
All three detection engines against the real repo configs. OSFI end-to-end
including a forced update → archive. Same-day rerun idempotency.

### `test_recorded_fixtures.py` — 30
Every source's connector parses its **real recorded payload**. Parameterised
over `tests/fixtures/`.
*Protects:* a source silently changing its HTML and yielding zero documents
while the run still reports success.

### `test_fetch.py` — 4
html→md; **PDF detected by magic bytes** (a bot block page served as `.pdf`
regressed this once); URL-title humaniser.

### `test_rules_and_capture.py` — 8
Reference grammars (B-13, SR 26-3, CAR-Ch4, NI 31-103). Sentence-scoped
supersede detection. PDF harvest and `source_kind`. Meta-source dedup. Backfill
cutoff. Markdown projection layout and frontmatter. Plus: **a run records
when it actually finished**, not the caller's fleet-wide timestamp.

### `test_orchestrator.py` — 2
Fleet fan-out with failure isolation; rerun subset with operator audit.

### `test_verify_sources.py` — 6
pass / warn(stale) / fail(content-type, 404, thin, unreachable); sitemap-index
support.

### `test_enrichment.py` — 3
The LLM slot: taxonomy tags, dates, supersedes flip, pending edges, and
invalid JSON → `enrichment_pending` rather than a crash.

### `test_materiality.py` — 7
Deterministic scoring and the `reason` string that justifies every score.

## Selection layer

### `test_extraction_dossier.py` — 19
Entity index, event classification, the dossier's scoring and `why` string, and
**ledger conservation** — nothing may vanish without appearing in a counter.

### `test_entity_recall.py` — 9
`RECALL_FLOOR = 1.0` over 22 name variants; 8 confusable pairs that must never
confirm; 7 cosmetic-only differences that must.
*Protects:* the 68%-recall regression. **If you touch `matching.py`, also watch
the suite's wall clock** — the first fix was 80× slower.

### `test_schedule.py` — 19
The six-state machine: weekend, skip date, missed, due, grace boundary
(inclusive then flips), running, partial-by-three-causes, manual run on an
unscheduled day, next-run-skips-weekend, DST handled by the zone, missing or
broken config does not take the page down, and **with no declaration nothing is
ever late**.

### `test_collection_health.py` — 31
Coverage matrix (weekend ≠ failure; a category that did not run is missed even
when the other did; a cell names who is missing; a rerun clears an earlier
failure). Today bar (never claims "complete" over a partial day; duration
omitted rather than wrong). Rerun buckets (silent, never-run, fail streak, each
category against its own window). Health (**reliability and the matrix cannot
disagree**; nothing is late before the first run ever recorded; the funnel
reports what holds without inventing an identity; quality percentages use the
right population; **only a real impossibility is flagged** — `ingested +
archived > fetched` is legitimate and flagging it manufactured a defect).

### `test_scheduler_install.py` — 19
The unit is generated from the declaration, never typed. The timezone
conversion is real (06:00 Toronto → 05:00 on a Chicago host, and a conversion
that crosses midnight reports the day shift). The plist uses the venv
interpreter, carries no empty secrets, and fires only on declared days.
`status()` separates installed from loaded, and reports the absence of a
scheduler rather than guessing. The daily and intraday jobs use different
labels and paths, so installing one never disturbs the other.
*Protects:* the host had no scheduler at all while the app reported missed runs
against the declaration.

### `test_runqueue.py` — 20
Every click is accepted: one arriving mid-run is queued rather than dropped,
the same source clicked twice is reported rather than run twice, and an empty
submission is refused instead of quietly starting the fleet. Pending ids are
**coalesced into one batch** (eight processes would mean eight enrichment
sweeps against one SQLite writer) but submissions with different options are
never merged. Outcomes are read back from `reg_runs`: a run older than the
batch does not count, a `failed` status is not `ok`, a source the runner never
recorded is failed rather than done, and an unreadable database says so. One
exploding batch does not kill the worker.
*Protects:* the refusal that existed at every layer except the one an operator
could see. Verified to fail on the original bug — ignoring `started:false`
makes a refused source report `done`.

### `test_spawn_ingest.py` — 10
The command line the UI actually launches. Three parameters were accepted,
documented and then dropped: `--date` (so a backfill for a missed day filed
under today), `--max-docs`, and `wait` (which is how the queue knows a batch
finished). Also pins that `scope:"all"` does not narrow the fleet, the operator
is attributed, and the concurrent-fleet guard reports the pids it found.
*Protects:* the class of bug where the API signature and the subprocess argv
disagree. Verified to fail on the original bug — dropping the `--date` line
makes the backfill test fail.

### `test_notepad_and_paging.py` — 26
Reading a long document to the end, and keeping notes while you do.

*Paging:* a window reports `total_chars`, `pct_of_document` and `next_offset`;
looping on `next_offset` reconstructs the document exactly; the last window is
not truncated; an offset past the end returns empty rather than wrapping;
`corpus_read_many` reports each document's real size and names the ones that
need a full read.

*The harness:* when it truncates it says so **in the payload**, in words that
forbid reading it as missing data; the budget is spent across the run, never
goes negative, and once exhausted the tool is **not run at all** rather than
served an apology.

*The notepad:* notes survive and read back; append is the default so a long
pass cannot erase itself; `replace` must be asked for by name; an unknown mode
is refused without losing anything; reading with no section returns the index
only; two people never share a pad; a traversing name cannot escape the
directory; an oversized section is refused rather than silently cut. And —
found live — **a `##` heading inside a note cannot split the notepad**: the
worker wrote its own heading, the section it had named came back empty, and
the notes read as lost.

*Protects:* the failure that started this. 5,500 of 104,508 characters reached
the model, and the worker told a user "the corpus does not contain the
risk-weight tables". It did; they start at character 27,519.

### `test_date_recovery.py` — 20
Dates from URL paths and from the opening of a document. The refusals matter
more than the finds: an effective date, a comment deadline, a "last updated"
line, a date past today, and anything below the opening are all rejected.
*Protects:* a wrong date files a document in the wrong week and is never
questioned again; a missing one merely excludes it from a window.

### `test_excerpt.py` — 13
Letterhead is never the preview; a labelled `Subject:` beats a guess; a table
of contents is not a summary; subscribe boilerplate is skipped; no prose → no
preview; news shows the publisher's summary and never the boilerplate note; a
headline-only feed yields nothing rather than the headline twice; bounded and
never cut mid-word; **long prose without a full stop does not hang**.

## Narration layer

### `test_ask.py` — 10
Grounded chat: citations must exist, no invented numbers, refusal paths
(uncited → rejected, provider down → error, no sources, no key).

### `test_focus.py` — 18
Filtering is deterministic (entity, source, AND-combination, ambiguous matches
kept). The prompt may reorder and narrate and nothing else: an invented item
voids the ranking, an invented figure withholds the note while the order
survives, a provider failure degrades to deterministic order, **focus never
mutates the page it was given**, and a prompt can never reintroduce a
filtered-out card.

### `test_entity_table.py` — 24
The column schema (YAML and JSON, a value outside the set becomes `unknown`,
reserved names, broken schema reports why, the prompt fragment is generated
from the schema so the two cannot drift). The sweep (every name gets a row; a
re-run does not pay twice; refresh re-searches; the budget stops and names what
it missed; one failing name does not end the sweep; an `error` row is retried
but a `none` row is not). Demo mode is marked at every level and costs nothing.
Classification and the headline.

## Surfaces

### `test_mcp_tools.py` — 15
All tools against a seeded corpus; generated configs valid; trigger uses the
runtime stub. Plus the contract guard: **an argument the tool does not
implement is rejected, not ignored**; a schema may opt out of strictness; the
agent surfaces the rejection to the model; every configured tool declares its
parameters; `corpus_changes` honours and advertises `source`.

### `test_ui_endpoints.py` — 13
tree / browse / changes / diff / runs / inventory. **Filter-before-LIMIT
regression.** Manual add and update (v2). Multipart PDF upload. **fs jail —
path traversal returns 400.**

### `test_admin.py` — 7
Coverage matrix, drill-down, audited rerun and toggle, integrity, and
**"Run all" on a lane page runs only that lane**.

### `test_auth_personas.py` — 9
Signup, login, password rules, persona ownership and sharing.

### `test_news_lane.py` — 8
The news dashboard read model and the credit-analyst ranking lens.

### `test_dashboard_markup.py` — 4
Structural, not functional: **every `<div>` balanced**, **every view inside
`.page`**, and `className=""` never used (it strips layout classes).
Plus: **`loadAll` must not await `/integrity`**. That endpoint reconciles every
document — 24s at 10,277 — and awaiting it left the dashboard blank behind it;
once the corpus outgrew `j()`'s 15s timeout, every load stalled 30s and the
browser suite started failing on unrelated auth tests.
*Protects:* the class of bug where every element exists and every endpoint
answers, and the page is still broken. Verified to fail on the exact stray
`</div>` that caused it, and on restoring the awaited integrity call.

## Foundation gate

```bash
./.venv/bin/python scripts/regagg_verify_foundation.py
```
All source configs parse, taxonomy in sync, every model registers.
