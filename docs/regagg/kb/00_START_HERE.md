# START HERE — Regulatory Intelligence Aggregator

**Audience:** the next AI coding agent or developer picking this up. Read this
file, then the numbered files in order. You are NOT starting from scratch —
this is a working, tested system with ~6,000 real documents.

## What this is, in three sentences
An automated aggregator that collects everything ~30 financial regulators
publish (web pages + policy PDFs), normalizes it into a governed, versioned
markdown corpus, and serves it two ways: a 5-page operator/analyst dashboard,
and 12 stateless MCP tools for an agent stack. Regulator = YAML config, never
code. Nothing is ever deleted; every document carries full provenance
(source URL, sha256, timestamps, run attribution, raw original).

## State at handover (2026-08-04)
| Dimension | Value |
|---|---|
| Corpus | ~5,970 documents · ~4,800 web + ~770 policy PDFs · 269MB markdown |
| Regulators | 29/30 verified & collecting (amf_qc bot-blocked, escalated) |
| Tests | 92 passing (`tests/regagg/`, run: `./.venv/bin/python -m pytest tests/regagg/ -q`) |
| Server | `./.venv/bin/python run_server.py --port 3005` → UI at `/api/regagg/ui` |
| Remote | github.com/algowizzzz/sajhamcpserver-regagg, branch `feat/regagg-aggregator` |
| OSFI completeness | 30/30 expected guideline items reconciled (CAR 9/9, LAR 5/5, B 8/8, E 8/8) |

## The 60-second mental model
```
config/regulators/*.yaml        →  what to collect (30 files, 1 per regulator)
sajha/regagg/pipeline.py        →  detect → fetch → version → enrich → project
data/web_aggregator/            →  canonical store (raw, meta, versions, archive)
data/markdown/{web|policy}/     →  agent-consumable projection (frontmatter + md)
data/sajha.db  (reg_* tables)   →  the index: documents, versions, edges, runs
sajha/regagg/ui_dashboard.html  →  the dashboard (served at /api/regagg/ui)
sajha/tools/impl/reg_tools.py   →  12 MCP tools (reg_*)
scripts/regagg_daily_poll.py    →  THE daily entrypoint (delta ingest + resync)
```

## Read next
1. `01_ARCHITECTURE.md` — design decisions, data flow, schema, invariants
2. `02_UI_AND_TOOLS.md` — every UI page, endpoint, and MCP tool
3. `03_TESTING_AND_OPS.md` — test inventory, scripts/runbooks, backups
4. `04_KNOWN_ISSUES_ROADMAP.md` — honest gaps + what to build next
5. `../BUILD_LOG.md` — chronological build history (how we got here)
6. `../CHATBOT_GUIDE.md` — how the agent/chatbot layer consumes this

## The four architectural invariants (violating any = failed review)
1. **Regulator is config** — adding #31 is a YAML file, never code.
2. **Tools/connectors are stateless** — all state in DB + storage; every run
   idempotent and safe to re-execute.
3. **Archive is append-only** — updates archive the prior version; nothing is
   ever deleted (the only exception ever made: purging OUR OWN synthetic test
   fixtures, never regulator data).
4. **No source URL is trusted** until `scripts/verify_sources.py` passes it.

## Cardinal rules learned the hard way (see 04 for stories)
- Never fabricate/guess data — every number on the UI traces to a DB row.
- Bot-blocks are handled by official channels (APIs, abstracts, stubs,
  escalation) — never by evasion.
- Status colors must mean something: red = act, amber = aware, green = fine.
- Filter in SQL *before* LIMIT (we shipped that bug once; test exists now).
- Close DB sessions / use thread-scoped sessions (pool-exhaustion bug, fixed).
