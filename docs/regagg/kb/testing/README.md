# Testing — index

**434 automated tests: 358 Python + 76 browser.** Everything offline and
deterministic; network is always injected.

| Suite | Count | Command | Time |
|---|---|---|---|
| Python | 358 | `./.venv/bin/python -m pytest tests/regagg -q` | ~7s |
| Browser | 76 | `bash tests/ui/run_suite.sh` | ~4 min |
| Foundation gate | — | `./.venv/bin/python scripts/regagg_verify_foundation.py` | ~2s |

Run both before any commit that touches `sajha/regagg/` or the dashboard.

## Files here

| File | Contents |
|---|---|
| `01_PYTEST_SUITES.md` | all 25 Python files: what each covers and what it protects against |
| `02_UI_SUITE.md` | the 6 browser specs, and how the harness works |
| `03_RESULTS.md` | recorded results, coverage measurements, live acceptance runs |
| `04_HOW_TO_TEST.md` | writing a new test, fixtures, common traps |

## The philosophy, in one paragraph

Every test here exists because something was wrong, or because something could
go wrong *invisibly*. The bar is not "does it render" but **"does it mislead"** —
a weekend that reads as an outage, a source list that shows evidence the answer
did not use, a generated column that quietly widened its own vocabulary. Those
all look fine in a screenshot and cost someone an afternoon. Where a test was
written in response to a specific bug, the bug is named in the test's docstring
so the intent survives the next refactor.

## What is deliberately not tested

- **Live network.** Connectors are tested against recorded fixtures
  (`tests/fixtures/`, 9.6 MB, one payload per source). Re-record with
  `scripts/regagg_record_fixtures.py` — rarely, and never in CI.
- **Live LLM output.** Every generated surface is tested with an injected fake
  client. What is asserted is the *validation*, not the prose: that an invented
  figure is withheld, that an unknown card voids a ranking, that a value
  outside its enum becomes `unknown`.
- **Live Tavily.** `DemoNews` is deterministic per (name, day) and is what the
  tests use.
- **The upstream SAJHA suite** (`test/`, 18 files) covers tools this product
  does not register. It is not part of this system's gate.

## Quick triage when something fails

| Symptom | Look at |
|---|---|
| `no such table: reg_*` | run `./.venv/bin/python -m scripts.regagg_migrate` |
| Python suite suddenly takes minutes | the entity matcher — see war story 2 |
| UI suite fails on selectors after a UI change | the spec names the element; update the spec, do not loosen the assertion |
| `database disk image is malformed` | two UI suites ran concurrently; the live DB is fine |
| A My Day test sees stale fields | pages are cached — the test needs `refresh=true` |
