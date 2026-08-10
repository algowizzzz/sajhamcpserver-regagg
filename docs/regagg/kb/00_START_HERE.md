# START HERE — riskGPT, financial web data aggregator

**Audience:** the next developer or AI coding agent picking this up. Read this
file, then the numbered files in order. You are **not** starting from scratch —
this is a working, tested system holding 7,353 real documents.

Everything here was verified against the running system on **2026-08-09**. Where
a number appears, it came from the database or a test run, not from memory. If
you find a claim that no longer holds, the claim is wrong — fix it here.

---

## What this is, in four sentences

An automated aggregator that collects what 30 financial regulators publish
(web pages + policy PDFs) and what 25 financial news wires report, normalises it
into a governed, versioned markdown corpus, and serves it three ways: a
four-tab operator/analyst dashboard, a set of MCP tools for an agent stack, and
a per-person daily briefing built from a **persona** (the names, topics and rule
families you are responsible for). A source is a YAML file, never code. Nothing
is ever deleted; every document carries full provenance. Every number on screen
traces to a row you can open.

## State of the system

| Dimension | Value |
|---|---|
| Corpus | **7,353** documents · 100% extracted · 63% carry a publication date |
| Sources | **55** — 30 regulators + 25 news wires |
| Versions on file | 7,536 (append-only history) |
| Collection runs recorded | 157 |
| Personas | 12 |
| Database tables | 15 `reg_*` tables, SQLite dev / Postgres on-prem |
| Python tests | **371**, `./.venv/bin/python -m pytest tests/regagg -q` (~8s) |
| Browser tests | **76**, `bash tests/ui/run_suite.sh` (~7 min) |
| MCP tools | 24 — 12 `reg_*` + 10 `corpus_*` + 2 `notepad_*` |
| Server | `./.venv/bin/python run_server.py --port 3005` → UI at `/api/regagg/ui` |
| Branch | `feat/regagg-aggregator`, pushed · remote `mine` = algowizzzz/sajhamcpserver-regagg |
| Last pushed | `1c37f559` — 2026-08-09. `main` on the fork tracks the same commit |

> **Two remotes.** `mine` is the fork this work lives on. `origin` is the
> upstream SAJHA project (ajsinha/sajhamcpserver) — **never push there**; this
> branch is ~80 commits of a different product on top of it.

## The 60-second mental model

```
config/regulators/*.yaml          →  what to collect (55 files, 1 per source)
config/regagg_schedule.yaml       →  when a run is EXPECTED (declaration only)
sajha/regagg/pipeline.py          →  detect → fetch → version → enrich → project
data/web_aggregator/              →  canonical store (raw, meta, versions, archive)
data/markdown/{web|policy}/       →  agent-consumable projection
data/sajha.db  (reg_* tables)     →  the index: documents, versions, edges, runs
sajha/regagg/ui_dashboard.html    →  the whole UI, one file, served at /api/regagg/ui
sajha/tools/impl/{reg,corpus}_*   →  22 MCP tools
sajha/regagg/agent.py             →  the digital worker (agentic loop over those tools)
scripts/regagg_daily_poll.py      →  THE daily entrypoint
```

## Read next

| File | What it answers |
|---|---|
| `01_ARCHITECTURE.md` | design decisions, data flow, the invariants |
| `02_DATA_AND_SCHEMA.md` | storage layout, every table, what each column means |
| `03_UI_PAGES.md` | every page and panel, and why it looks like that |
| `04_API_REFERENCE.md` | all 49 endpoints, grouped by job |
| `05_AGENT_AND_MCP_TOOLS.md` | the 22 tools, the agent loop, the grounding rules |
| `06_PERSONAS_AND_MYDAY.md` | how a persona shapes a page; regulatory vs news |
| `07_SCHEDULING_AND_OPS.md` | the schedule declaration, runbooks, backups |
| `08_KNOWN_ISSUES_AND_ROADMAP.md` | honest gaps, war stories, what to build next |
| `09_BUILD_HISTORY.md` | chronological — how it got here |
| `10_DEPLOYMENT.md` | on-prem deployment |
| `testing/` | every test: what it protects, how to run it, results |

---

## Five invariants. Violating any of them is a failed review.

1. **A source is config.** Adding #56 is a YAML file, never code.
2. **The archive is append-only.** An update archives the prior version.
   Nothing is deleted — the only exception ever made was purging our own
   synthetic fixtures, never collected data.
3. **Selection is code; narration is the model.** What appears on a page is
   decided deterministically. The LLM only writes prose about what the code
   already chose, and its output is validated before it renders.
4. **No claim without a citation.** Any generated sentence names a document the
   reader can open. A number that is not in the evidence means the sentence is
   withheld — see `sajha/regagg/ask.py`, `focus.py`, `entity_table.py`.
5. **Tools and connectors are stateless.** All state in DB + storage; every run
   idempotent and safe to re-execute.

## Cardinal rules, learned the hard way

Each of these cost a real bug. `08_KNOWN_ISSUES_AND_ROADMAP.md` has the stories.

- **Never fabricate.** No placeholder headline, no invented figure, no demo row
  that is not labelled as one. The Tavily stand-in marks itself at three levels
  and the page shows an undismissable banner.
- **Absence is a finding, and it has a cause.** "Not scheduled", "no news",
  "search failed" and "over budget" are four different facts. A blank cell
  states none of them.
- **Show the denominator.** "16 of 338 matched" beats "16".
- **Filter in SQL before LIMIT.** Shipped that bug once; there is a test.
- **A near-miss is a miss.** A generated value outside its declared set becomes
  `unknown`, never the closest match.
- **Costs are shown before the click, not after.** Anything that spends money
  states the number first and caches so a re-run does not re-spend.
- **Status colour must mean something.** Red = act, amber = aware, green = fine.

## Getting running in five minutes

```bash
cd <repo>
./.venv/bin/python -m scripts.regagg_migrate          # ensure reg_* tables
DEEPSEEK_API_KEY=<key> REGAGG_SECRET=<secret> \
  ./.venv/bin/python run_server.py --port 3005
open http://localhost:3005/api/regagg/ui
```

Then `./.venv/bin/python -m pytest tests/regagg -q` should print **371 passed**.

Environment variables that matter:

| Variable | Effect if missing |
|---|---|
| `DEEPSEEK_API_KEY` | narration, chat and classification degrade to deterministic output; nothing breaks |
| `REGAGG_SECRET` | session signing; required for login |
| `TAVILY_API_KEY` | the entity table falls back to **clearly labelled** demo data |
| `REGAGG_MARKDOWN_ROOT` | defaults to `data/markdown` |
