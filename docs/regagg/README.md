# riskGPT — financial web data aggregator

The documentation for this product lives in **[`kb/`](kb/)**.

## → Start at [`kb/00_START_HERE.md`](kb/00_START_HERE.md)

It is written for the next developer or AI coding agent, and everything in it
was verified against the running system rather than recalled.

```
kb/
  00_START_HERE.md              what this is, state, invariants, five-minute start
  01_ARCHITECTURE.md            design decisions, data flow, module map
  02_DATA_AND_SCHEMA.md         storage layout, 15 tables, known data-quality state
  03_UI_PAGES.md                every page and panel, and why it looks like that
  04_API_REFERENCE.md           49 endpoints grouped by job
  05_AGENT_AND_MCP_TOOLS.md     24 tools, the digital worker, grounding rules
  06_PERSONAS_AND_MYDAY.md      how a persona shapes a page; regulatory vs news
  07_SCHEDULING_AND_OPS.md      schedule declaration, runbooks, backups, costs
  08_KNOWN_ISSUES_AND_ROADMAP.md  honest gaps, 14 war stories, what to build next
  09_BUILD_HISTORY.md           chronological, epic by epic
  10_DEPLOYMENT.md              on-prem deployment
  testing/
    README.md                   index — 453 tests, how to run them
    01_PYTEST_SUITES.md         all 28 Python files, what each protects
    02_UI_SUITE.md              6 browser specs and the harness
    03_RESULTS.md               recorded runs and measurements
    04_HOW_TO_TEST.md           writing a new test; traps that cost time
```

## Anything else in this repo

As of the 2026-08-10 cleanup, there is no "anything else": the upstream SAJHA
scaffolding this fork carried (examples, IR scrapers, OLAP engines, the studio,
29 unregistered tool implementations, upstream docs/tests/clientsdk/deployment
— 97 unreachable modules in all, measured by AST reachability from the server
entrypoint) has been deleted. What remains is the webagg application plus the
SAJHA runtime it actually uses: the FastAPI app, live routes, DB engine, tool
registry, and `sajha/web/` templates (used by filesystem path, not import).
