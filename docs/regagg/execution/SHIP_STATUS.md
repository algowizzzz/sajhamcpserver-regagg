# Ship execution log

## Sprint S1 — Identity & Personas ✅ COMPLETE

| Story | Status | Evidence |
|---|---|---|
| S1.1 users + signup/login/logout | done | `sajha/regagg/auth.py`; scrypt + HMAC session cookie |
| S1.2 personas + entities + versioning | done | `sajha/regagg/personas.py`; JSONFlex config, indexed entities |
| S1.3 auth + persona API | done | `/auth/*`, `/personas*` in `admin.py` |
| S1.4 login gate + Personas tab UI | done | `ui_dashboard.html` |
| S1.5 Playwright harness + suites | done | `tests/ui/` — 22 specs green |

**Tests: 118 pytest + 22 Playwright, all green.**

### Bugs found and fixed this sprint (all by the new tests)

1. **Mapper collision** — a second class named `User` on the shared declarative
   Base broke string relationship resolution for *every* model (500s across the
   app). Renamed to `RegUser`; table name unchanged.
2. **DB pool exhaustion (production-breaking)** — thread-scoped sessions pinned
   one pooled connection per threadpool thread forever; FastAPI's threadpool is
   larger than the pool, so the server wedged for 30s per request under load.
   Fixed with contextvar-scoped sessions released per request + a pool sized to
   the concurrency. Runtime for the suite: 2.2m → 59s, pool errors 27 → 0.
4. **Auth error messages swallowed** — the host app rewrites 4xx bodies, so
   "Email or password is incorrect" never reached the user. Expected user
   outcomes now return 200 with `ok:false` and a message.
5. **Deep links raced the data load** — setting a `<select>` before the options
   existed silently did nothing, so "Financial News" showed the whole corpus.
   Boot now resolves a READY promise the jumps await.
6. **Hash deep-links ignored after login, and the app fought its own hash** —
   added `hashchange` routing plus a guard so the app's own updates don't
   re-route (which was resetting the lane from news to regulatory).
7. **Lane-blind deep links returned 0 rows** — "Financial News" + regulatory
   scope intersect to nothing; jumps now carry their lane, and Home's band
   chart pins the regulatory lane.
8. **No fetch timeout or retry** — one slow first response left every panel on
   "loading…" forever. Fetches now have a deadline and one retry; a failed
   first load is surfaced instead of swallowed behind the sign-in screen.

## Sprint S2 — Extraction & Distillation ✅ COMPLETE

| Story | Status | Evidence |
|---|---|---|
| S2.1 ingest-time extraction | done | `extraction.py` — deterministic always on, LLM when keyed, same shape, attributable |
| S2.2 dossier builder | done | `dossier.py` — matching, clustering, salience, conserving ledger |
| S2.3 My Day + validation | done | `myday.py` — 3 gates, deterministic fallback, cached per persona/day |
| S2.4 schema migration | done | `scripts/regagg_migrate.py` — model-driven, SQLite + Postgres |

**Bug found by tests:** clustering keyed on wording left one event from two
wires as two items, so corroboration always read 1 — the exact signal that
separates a real credit event from chatter. Now keyed on entity + event type.

## Sprint S3 — Product surfaces ✅ COMPLETE

| Story | Status | Evidence |
|---|---|---|
| S3.1 My Day tab | done | ledger, quiet counts, per-card reasons, evidence drill-through |
| S3.2 Health tab | done | pass rate, conservation, sources needing attention, generation health |
| S3.3 Ask tab | done | context chip; honest panel when chat is unconfigured |
| S3.4 intraday + generation scripts | done | `regagg_news_poll.py`, `regagg_generate_pages.py` |
| S3.5 UI suite | done | 12 more specs (My Day, Health, Ask) |

**Bug found by tests:** opening the app before the morning run showed an empty
page, implying a quiet market. It now falls back to the latest day with data
and says so.

## Sprint S4 — Ship hardening ✅ COMPLETE

| Story | Status | Evidence |
|---|---|---|
| S4.1 PostgreSQL path | done | migration + GIN indexes + `regagg_pg_load.py`; **full UI suite green against Postgres** |
| S4.2 deployment guide | done | `DEPLOY_ONPREM.md` — systemd, nginx, secrets, cron, verification |
| S4.3 full regression | done | 132 pytest + 31 Playwright, on SQLite **and** PostgreSQL |

**Bug found on Postgres:** the SQL DDL had drifted from the models
(`source_kind` missing), so a Postgres install would 500 on first query. The
migration is now model-driven and converges any drifted schema.

## Test totals

| Suite | Count | Where |
|---|---|---|
| Backend (pytest) | 132 | `tests/regagg/` |
| UI (Playwright, real browser) | 31 | `tests/ui/specs/` |
| Databases proven | 2 | SQLite (dev) and PostgreSQL (on-prem) |


## Sprint S5 — PMF gaps found by reviewing as a user ✅ COMPLETE

Walking the product as a new analyst surfaced three gaps that testing alone
would not have: a blank form on day one, no way to switch between personas,
and a promised intraday feature that was dead code.

| Story | Status | Evidence |
|---|---|---|
| S5.1 starter personas | done | 3 starters; a working page is two clicks from signup |
| S5.2 persona switcher | done | shown only when there is a choice |
| S5.3 intraday updates wired | done | `refresh_intraday()` called by the news poll; announces, never rewrites |
| S5.4 responsive | done | phone viewport spec — zero horizontal overflow |
| S5.5 scale proof | done | 6,000-name page builds in under 5s (asserted) |

### Bugs found this sprint

9. **"New persona" silently became "edit persona"** — the list loader
   auto-selected the first persona while the user was creating a new one, so
   the second persona was never created. Found by the switcher test.
10. **761px of horizontal overflow on a phone** — the app was desktop-only.
    Now collapses to one column, tables scroll inside their own box.
11. **`iif()` is SQLite-only** — the regulatory lane page 500'd on PostgreSQL.
    Replaced with portable `case()`. Found by running the UI suite on Postgres.
12. **Fresh PostgreSQL installs had an incomplete schema** — the host app
    queries tables the regagg migration never created, and on Postgres those
    errors abort the request's transaction. The migration now creates every
    mapped table (31), not only the reg_* ones.

## Final state

| Suite | Count | Databases |
|---|---|---|
| Backend (pytest) | 135 | SQLite + PostgreSQL |
| UI (Playwright, real browser) | 38 | **SQLite and PostgreSQL, both green** |

Twelve real defects were found and fixed by these suites, two of which would
have taken production down (connection-pool exhaustion, PostgreSQL schema).

## Entity matching, done properly (the scary one)

The token-subset fix shipped in S6 was a heuristic checked against seven
hand-picked cases. Measured against how companies are actually written, it
scored **68% recall with a false positive** — seven silent misses including
"Meta", "Uber", "AMD" and "JP Morgan", and "Apple Hospitality REIT" wrongly
matched to "Apple Inc."

Rewritten as `sajha/regagg/matching.py` with three outcomes instead of two:

| Outcome | Meaning | Example |
|---|---|---|
| **confirmed** | the difference is provably cosmetic | `HSBC Holdings plc` ← `HSBC`; `Advanced Micro Devices` ← `AMD` |
| **possible** | plausible but undecidable from the text — shown, flagged "verify" | `Apple Inc.` ← `Apple Hospitality REIT`; `Goodfood` ← `Goodfood Market Corp.` |
| **none** | nothing links them | `Bank of America` ← `Bank of Montreal` |

The middle row is the point. A matcher forced to choose between missing and
over-claiming will do both; making "I am not sure" a first-class, visible
outcome is what keeps this honest at 6,000 names.

**Now: 100% recall on the adversarial set, zero false confirmations**, pinned
by `tests/regagg/test_entity_recall.py` (a floor that fails the build rather
than drifting). Also caught while rewriting: `acronym("Goodfood Market Corp.")`
was generating `"GM"` — which would have matched General Motors. Acronyms now
require three words and three letters.

Effect on the live desks: items that were being missed now appear —
Underwriting 2 → 8 matched, Hedge funds & FIs 11 → 16, Real estate 8 → 10.

## Final totals

| Suite | Count | Databases |
|---|---|---|
| Backend (pytest) | 146 | SQLite + PostgreSQL |
| UI (Playwright) | 45 | SQLite **and** PostgreSQL, both green |
