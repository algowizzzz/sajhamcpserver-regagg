# 07 — Scheduling, Runbooks, Operations

## The schedule is declared, not owned

The scheduler is **external** — a host cron or cloud task calls
`scripts/regagg_daily_poll.py`. The app therefore only ever sees runs that
happened, which made an empty day ambiguous: a quiet Saturday and a dead
scheduler looked identical.

`config/regagg_schedule.yaml` closes that gap. It is a **declaration, not a
trigger** — nothing in it starts anything:

```yaml
enabled: true
at: "06:00"
timezone: "America/Toronto"     # a zone, not UTC — DST shifts on its own
days: [mon, tue, wed, thu, fri]
grace_minutes: 90               # slow scheduler ≠ missed run
skip_dates: []                  # holidays, planned maintenance
```

`schedule.py` resolves every day to exactly one state:

| State | Meaning |
|---|---|
| `not_scheduled` | weekend, holiday, or feature off — **expected, never a fault** |
| `due` | expected later today, inside the grace window |
| `running` | in flight |
| `complete` | every active source reported cleanly |
| `partial` | it ran, but some failed, returned nothing, or never started |
| `missed` | expected, grace passed, nothing recorded |

**Keep this file and the installed job in step.** They cannot drift when the
job is installed from the UI, because the unit is generated from this file —
but a hand-written crontab elsewhere can. If they drift the missed count climbs
and the Health page says so. With no declaration, nothing is ever called late —
silence about the schedule must not become an accusation.

## Installing it — from the UI

Health → Schedule reliability has one row per job with an Enable/Disable
button. `sajha/regagg/scheduler_install.py` detects launchd or systemd and
writes a **user-level** unit (no sudo) **generated from the declaration above**,
so the two cannot drift; there is no field anywhere for a raw cron string.

Two jobs, independent — enable either, both or neither:

| Job | Script | When |
|---|---|---|
| `daily` | `regagg_daily_poll.py` | the declared `at` / `days`, all 55 sources |
| `intraday` | `regagg_news_poll.py` | the `intraday` block; news lane only, skips the corpus sweep |

**Timezones.** launchd fires in host-local time and has no concept of a zone,
so the declared time is converted at render and the panel says so — `06:00
America/Toronto` installs as `05:00` on a host set to `America/Chicago`. Check
that line after installing; a silent one-hour error only shows up as a run
arriving late.

`status()` asks the operating system, not a flag of ours, so
installed-but-unloaded and never-installed are different answers.

Endpoints: `GET /scheduler/status`, `POST /scheduler/install?job=`,
`POST /scheduler/uninstall?job=`.

## Cron lines, if you prefer to do it by hand

```cron
0 6 * * 1-5  cd <repo> && ./.venv/bin/python scripts/regagg_daily_poll.py >> logs/regagg_daily.log 2>&1
0 2 * * 6    cd <repo> && ./.venv/bin/python scripts/regagg_daily_poll.py --deep >> logs/regagg_daily.log 2>&1
30 5 * * *   cd <repo> && ./scripts/regagg_backup.sh >> logs/backup.log 2>&1
```

Prefer **systemd timers** over cron on the server: failures land in
`journalctl` instead of a mail spool nobody reads.

## Scripts

| Script | Purpose |
|---|---|
| **`regagg_daily_poll.py`** | THE scheduler entrypoint: fleet delta ingest (giants capped 500/day, `--deep` weekly 3000) → pending-edge resolve → reconcile → projection resync → one-line summary. Exit ≠ 0 on invariant violations |
| `regagg_news_poll.py` | the news-wire lane equivalent |
| `regagg_ingest_live.py` | targeted ingest: `--only ids --max-docs N --include <url-regex> --giants --skip --operator` |
| `regagg_migrate.py` | **run after every model change and every deploy** — creates missing tables and columns |
| `regagg_backup.sh` | nightly consistent SQLite `.backup` + hardlink-incremental rsync of `data/`; 7-day retention |
| `verify_sources.py` | live source verification — the trust gate, run before onboarding any source |
| `regagg_add_doc.py` | manual add (URL / `--file` PDF / `--md`) |
| `regagg_backfill_rules.py` | re-run deterministic enrichment over the corpus |
| `regagg_extract_backfill.py` | backfill entity extraction; commits in batches and retries a lock |
| `regagg_backfill_dates.py` | recover publication dates from URL paths and document text |
| `regagg_refresh_pages.py` | rebuild cached My Day pages after a dossier change |
| `regagg_score_materiality.py` | re-score after editing `_materiality.yaml` |
| `regagg_gen_tool_configs.py` | regenerate `config/tools/reg_*.json` |
| `regagg_create_worker.py` | register the `w-riskgpt` digital worker |
| `regagg_generate_pages.py` | pre-build My Day pages for all personas |
| `regagg_record_fixtures.py` | re-record per-source test fixtures (network, rarely) |
| `regagg_verify_foundation.py` | foundation gate: configs parse, taxonomy sync, tables register |
| `regagg_bootstrap.py` · `regagg_seed_demo.py` · `regagg_seed_desks.py` · `regagg_purge_demo.py` · `regagg_pg_load.py` · `regagg_migrate_001_source_kind.py` | setup and historical one-offs — read before reusing |

## Common operations

**Start the server**
```bash
DEEPSEEK_API_KEY=<key> REGAGG_SECRET=<secret> \
  ./.venv/bin/python run_server.py --port 3005
```

**Rerun one source** — Collection page ▶ Run, or:
```bash
curl -X POST localhost:3005/api/regagg/rerun \
  -H 'content-type: application/json' -d '{"scope":"ids","ids":["osfi"]}'
```
Spawns detached; refuses if a run is already active.

**Gap-fill a section**
```bash
./.venv/bin/python scripts/regagg_ingest_live.py --only osfi --include "/en/guidance"
```

**Integrity check and repair** — `GET /api/regagg/integrity` runs reconcile.

**Add source #56** — write `config/regulators/{id}.yaml`, run
`verify_sources.py --regulator id`, fix what the report says, and it joins the
next daily run. No code change.

**Rotate an agent key** — insert a new `ApiKey` row (sha256 hash) with
`tool_access_list` as `json.dumps(["reg_*","corpus_*"])`, disable the old one.
Never commit keys.

**Restore drill** — copy `~/Backups/regagg/<date>/` over `data/` and
`sajha.db`, start the server, check `/integrity`.

**Backfills** — both are idempotent and dry-run by default:
```bash
./.venv/bin/python scripts/regagg_backfill_dates.py --apply     # publication dates
./.venv/bin/python scripts/regagg_extract_backfill.py --workers 8
./.venv/bin/python scripts/regagg_refresh_pages.py --apply      # rebuild cached My Day
```

> **Never run a backfill while a collection run is active.** SQLite allows one
> writer. A run holding the lock cost the extraction pass ten minutes of paid
> LLM calls before it learned to commit in batches. Check with
> `pgrep -f regagg_ingest_live` first.

## After a deploy, in order

1. `./.venv/bin/python -m scripts.regagg_migrate`
2. `./.venv/bin/python -m pytest tests/regagg -q` → 299 passed
3. Start the server, open `/api/regagg/ui`, check the Health verdict
4. Enable the scheduler from Health, or confirm the host's own timer matches
   `config/regagg_schedule.yaml`

## Backups

`regagg_backup.sh` nightly to `~/Backups/regagg`. Uses the SQLite **backup
API**, not `cp` — copying a live database captures a torn page and produces
`database disk image is malformed`. That happened once; the live database was
fine and the copy was not.

Canonical storage is the thing that must survive. The index and the projection
are both rebuildable.

## Cost control

| What | When it spends | Guard |
|---|---|---|
| Tavily entity sweep | only on `POST /entities/sweep` | explicit click, credits shown first, per-entity daily cache, hard budget |
| LLM narration | page generation, chat, classification | cached per persona/day; degrades to deterministic output |
| Collection | scheduled runs | per-source daily caps; `--deep` weekly only |

Nothing bills on a page load. If you add something that does, it belongs behind
an explicit action with the number shown before the click.
