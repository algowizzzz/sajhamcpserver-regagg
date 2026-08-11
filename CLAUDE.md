# riskGPT web aggregator — agent orientation

This repo is **riskGPT, a financial/regulatory web data aggregator** — NOT a
generic MCP server. It is embedded in a fork of the SAJHA MCP server, but the
product is the aggregator. When in doubt, the aggregator's needs win.

## Read before doing anything

`docs/regagg/kb/00_START_HERE.md` — then the numbered KB files as needed.
`docs/regagg/kb/08_KNOWN_ISSUES_AND_ROADMAP.md` holds the open items and the
war stories; do not regress them.

## The trap every new agent falls into

There are **two login systems**. The application is at
**`/api/regagg/ui`** with its own signup (`reg_users` table; on a fresh
machine there are no accounts — sign up, first account is admin, and
`REGAGG_SECRET` must be set or login fails). The root `/` pages and
`config/users.json` (admin/admin123) are the **legacy SAJHA shell** — never
point a user there.

## Ground rules (the KB has the full versions)

1. A source is a YAML file in `config/regulators/`, never code.
2. The archive is append-only; nothing collected is ever deleted.
3. Selection is deterministic code; the model only narrates what code chose,
   and narration is validated before it renders. Never fabricate; a near-miss
   becomes `unknown`, never the closest match.
4. Every generated claim cites a doc_id the reader can open.
5. Honour each source's declared `rate_limit_rps`. Never evade a bot block.

## Commands

```bash
./.venv/bin/python -m pytest tests/regagg -q     # 377 tests, ~10s — must stay green
bash tests/ui/run_suite.sh                       # 76 Playwright tests, ~2-4 min
./.venv/bin/python scripts/regagg_verify_foundation.py
./.venv/bin/python run_server.py --port 3005     # UI at /api/regagg/ui
```

Run both suites if you touch `sajha/regagg/` or the dashboard. When a test
comes from a bug, its docstring names the bug — keep that convention, and
prove new regression tests fail on the original defect before trusting them.

## State lives in

- `data/sajha.db` (SQLite, not in git) — the index: documents, versions, runs,
  users, personas. Single writer: never run two writers concurrently.
- `data/markdown/` (in git) — the agent-consumable corpus projection.
- `data/web_aggregator/` (NOT in git, ~5 GB) — raw archive; rebuilds by
  re-collecting.
- `config/regagg_schedule.yaml` — when collection is expected; installable as
  a launchd/systemd job from the Health page.

Update `docs/regagg/kb/` in the same commit as any behaviour change — the KB's
rule is that a stale claim is a bug.
