# On-prem deployment

Verified path: PostgreSQL + JSONB, native signup/login, one server process.
Everything below has been executed end-to-end — the full UI suite (31 specs)
runs green against PostgreSQL, not only against the development SQLite file.

## 1. Prerequisites

- Python 3.11+ and PostgreSQL 14+ (the product uses JSONB and GIN indexes)
- A service account that owns the database
- Outbound HTTPS to the configured sources (or an allow-listed proxy)

## 2. Database

```bash
createdb regagg
```

Set the connection (the app reads `SAJHA_*` environment variables):

```bash
export SAJHA_DB_TYPE=postgresql
export SAJHA_DB_HOST=db.internal   SAJHA_DB_PORT=5432
export SAJHA_DB_NAME=regagg
export SAJHA_DB_USER=regagg_app    SAJHA_DB_PASSWORD='…'
```

Create/upgrade the schema — **idempotent, run it on every deploy**:

```bash
python scripts/regagg_migrate.py
```

It is model-driven: it creates missing tables, adds any column the models have
that the database lacks (so a schema that drifted from an older SQL DDL
converges), and ensures the GIN indexes that make JSONB containment queries
index lookups rather than scans.

Bringing an existing corpus over from a pilot install:

```bash
python scripts/regagg_pg_load.py --from data/sajha.db     # idempotent upsert
```

## 3. Secrets — set these before the first user signs up

| Variable | Why |
|---|---|
| `REGAGG_SECRET` | signs session cookies. **Unset means sessions die on every restart** (the server warns loudly at boot). Use 32+ random bytes. |
| `REGAGG_COOKIE_SECURE=1` | sets the `Secure` flag — required once TLS is terminated in front. |
| `DEEPSEEK_API_KEY` | *optional*. Switches extraction and the My Day lede from the deterministic engine to DeepSeek (~1,000 stories/minute at 12 workers, cents per day). Everything works without it. |
| `ANTHROPIC_API_KEY` | *optional*. Same role; used if DeepSeek is not set. |
| `DEEPSEEK_BASE_URL` / `DEEPSEEK_MODEL` | *optional*. Point at a self-hosted OpenAI-compatible endpoint (vLLM, Ollama) to keep inference inside the bank. |
| `REGAGG_AGENT_URL` | *optional*. Address of the LangGraph agent platform for the Ask tab. |

```bash
export REGAGG_SECRET="$(python -c 'import secrets;print(secrets.token_hex(32))')"
export REGAGG_COOKIE_SECURE=1
```

## 4. Harden the inherited defaults

The upstream SAJHA server ships demo credentials (`admin/admin123`) and ~500
unrelated tools. This product removed the tools; **change the default admin
password before exposing the host**, and keep the server bound to localhost
behind the reverse proxy:

```bash
python run_server.py --host 127.0.0.1 --port 3005
```

## 5. Run it as a service

`/etc/systemd/system/regagg.service`:

```ini
[Unit]
Description=Market & Regulatory Intelligence
After=network.target postgresql.service

[Service]
User=regagg
WorkingDirectory=/opt/regagg
EnvironmentFile=/etc/regagg/env          # the variables from sections 2 and 3
ExecStart=/opt/regagg/.venv/bin/python run_server.py --host 127.0.0.1 --port 3005
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Reverse proxy (nginx), TLS terminated here:

```nginx
location / {
    proxy_pass http://127.0.0.1:3005;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

## 6. Scheduled collection

```cron
# full pass — all sources, versioning, reconcile, markdown resync
0 2 * * *  cd /opt/regagg && .venv/bin/python scripts/regagg_daily_poll.py >> logs/daily.log 2>&1

# intraday news — cheap (feeds only, no article fetches); keeps the 50/source
# cap per-poll so a busy news day cannot scroll past the collector
0 6-22/2 * * *  cd /opt/regagg && .venv/bin/python scripts/regagg_news_poll.py >> logs/news.log 2>&1

# morning generation — every persona's page, cached before the desk arrives
30 5 * * *  cd /opt/regagg && .venv/bin/python scripts/regagg_generate_pages.py >> logs/pages.log 2>&1

# nightly backup
0 1 * * *  cd /opt/regagg && ./scripts/regagg_backup.sh >> logs/backup.log 2>&1
```

## 7. Seeding a pilot

Nine desk personas — corporate credit, CCR, market risk, FX, equity,
underwriting, real estate, hedge funds & FIs, and a prudential rules owner —
with watchlists drawn from companies the corpus actually reports on:

```bash
python scripts/regagg_seed_desks.py --email desk@bank.test
python scripts/regagg_extract_backfill.py --lane news --workers 12   # if a key is set
python scripts/regagg_generate_pages.py
```

Sign in as that user and open **Desks** to see all nine side by side. Each is a
starting point for a real analyst to edit, not a fixed template.

## 8. First run

1. Open `https://your-host/api/regagg/ui`
2. **The first account created becomes the administrator** — create it
   immediately after deploying, before the host is reachable by others.
3. Create a persona (Personas tab): paste the names you follow, set weights.
4. My Day is generated at 05:30; until the first generation it builds on demand.

## 9. Verifying a deployment

```bash
pytest tests/regagg/ -q                       # 137 backend tests
PG=1 SAJHA_DB_NAME=regagg ./tests/ui/run_suite.sh    # 44 UI tests, real browser
python scripts/verify_sources.py              # every source answers and is fresh
```

Then open **Health** in the app: pass rate, pipeline conservation, sources
needing attention, and generation health are all on one page.

## 10. Operational notes

- **Backups**: the database holds documents, versions, personas and generated
  pages. `data/web_aggregator/` holds the raw archive; both must be backed up.
- **Bot-blocked sources** are escalated through official channels, never
  evaded — `amf_qc` sits BLOCKED by design until whitelisted.
- **Licensed feeds** (Bloomberg, Reuters, ratings actions) plug into the news
  lane with a config file and no code change.
- **Sizing**: the corpus is ~2 GB on disk today; personas and generated pages
  are small. One process serves the read-only app comfortably; the pool is
  configured for the server's threadpool (a mismatch there was a real outage
  cause during development).
