# Browser suite — 75 tests

(73 `test()` declarations; two are parameterised over two viewports, so 75 run.)

```bash
bash tests/ui/run_suite.sh                    # all, ~4 min
bash tests/ui/run_suite.sh --headed           # watch it
PG=1 bash tests/ui/run_suite.sh               # against PostgreSQL
```

## How the harness works

`tests/ui/run_suite.sh`:

1. Boots a server on **its own port** (3011) against **its own database copy**
   (`data/sajha_uitest.db`). A UI run must never mutate the live corpus.
2. Takes that copy with `sqlite3 .backup`, **not `cp`** — copying a live SQLite
   file while a server writes captures a torn page and yields
   `database disk image is malformed`. That happened once; the live database
   was fine and the copy was not.
3. Truncates only the people tables, so every run starts with the real 7,018-
   document corpus but no users or personas.
4. Waits for `/auth/me` to answer, then runs Playwright.
5. `PG=1` runs the identical suite against PostgreSQL — the on-prem target.
   Requires the corpus already loaded (`scripts/regagg_pg_load.py`).

Each test signs up a fresh account (`helpers.js: newUser()`), so tests never
collide and can run in any order.

## The specs

### `01-auth.spec.js` — 8
Signup, login, logout, session persistence, the gate blocking unauthenticated
access, password rules.

### `02-personas.spec.js` — 7
Create, edit, entity paste (CSV and one-per-line), duplicate collapse,
**personas are private to their owner**.

### `03-navigation.spec.js` — 7
Two-level navigation: home shows both lane cards with live counts; entering a
lane reveals its subtopics; shared pages scope to the lane they were entered
from; the coverage tree shows only the current lane's regions; pages retitle
per lane; deep links from charts land filtered, not unfiltered; **hash routing
survives a reload**.

### `04-myday.spec.js` — 15
The generated page: builds from real corpus data with a coverage ledger; a
credit event outranks market noise and is marked serious; the page is read-only
and stable across reopening; **a regulatory persona reports rule families as
unchanged, not silent**; cards open their evidence; a big book gets exception
framing.
Health: leads with a verdict; judges each category against its own window;
states that the counters are not a partition; every quality check says what it
breaks.
Ask: offers starting questions; an answer is grounded or withheld; opening a
card pins it as chat context.
Ambiguous matches: a possible mention is shown and flagged, never silently
dropped.

### `05-onboarding.spec.js` — 7
A new user is offered starters instead of a blank form; a starter prefills a
working persona in one click; the rules starter produces a regulatory persona;
two personas can be switched between on My Day; one persona shows no switcher —
no controls without a choice; a phone-sized viewport works; **a failed API call
is reported, not left spinning**.

### `06-maintenance.spec.js` — 29
The largest spec, and the newest.

**Collection (7)** — the today bar names the date and what the schedule expects
of it; an unscheduled day is drawn as expected, never as a fault; a cell opens
the list of sources that did not run; trend panels name the day their figures
belong to; sources are bucketed for rerun; selecting sources changes what the
run button will do; a bucket filter narrows without losing the count.

**Auto-fit (7)** — Collection and Health each fit 1920×1080 and 1440×900
without the window scrolling; below the breakpoint the page stacks and is
*allowed* to scroll; **no page traps its content behind a letterbox** (walks all
eleven views; fails if any holds more than a screenful in a panel while the
window will not scroll); a page whose primary content is a list lets the window
scroll; density is remembered across a reload.

**Chat panel resize (6)** — dragging widens the panel and the page follows;
bounds hold at both ends; the chosen width survives a reload; **a narrow window
borrows the width back rather than overwriting it**; keyboard resizing and
double-click reset; the grip is only reachable while the panel is open.

**Chat sources (9)** — a doc-id citation and its chip share one number; ids
grouped in one bracket each get their own marker; a chip links to the article
and opens in a new tab; the title leads the chip, not the publisher; one shared
publisher is stated once; only cited sources are shown; an answer that cites
nothing still shows its evidence; an unresolvable citation degrades instead of
disappearing; each answer keeps its own sources as the thread grows.

## Traps

- **Selectors are the contract.** When a UI change breaks a spec, update the
  selector to the element that now carries the meaning — do not loosen the
  assertion until it passes.
- **Two components must not share a class.** `#etSummary` reused `.mdlede` and
  made a locator ambiguous ("resolved to 2 elements"). Give a new component its
  own class even when it looks identical.
- **Cached pages hide new fields.** My Day is cached per persona per day; a test
  asserting a new dossier field needs `refresh=true`.
- **Do not run two UI suites at once.** They share the test database path.
