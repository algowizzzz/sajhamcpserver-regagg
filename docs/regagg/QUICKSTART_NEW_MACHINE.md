# Regulatory Intelligence — new-machine quickstart

Everything ships in this repo: code, all 50 source configs (30 regulators +
20 financial-news sources), the collected corpus (raw archive + markdown
projection), a seed database, tests with recorded fixtures, and the 12 reg_*
MCP tools (all other upstream tools are disabled — restore with
`python scripts/regagg_tool_blackout.py --restore`).

```bash
git clone https://github.com/algowizzzz/sajhamcpserver-regagg.git
cd sajhamcpserver-regagg
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/regagg_bootstrap.py     # puts the seed db in place, sanity-checks data
python run_server.py --port 3005
```

- Dashboard: http://localhost:3005/api/regagg/ui
- MCP endpoint: http://localhost:3005/mcp (X-API-Key auth; keys are DB-backed
  and NOT in the seed — mint a fresh key via the admin UI, scope it to `reg_*`)
- Daily collection: `python scripts/regagg_daily_poll.py`
- Tests: `pytest tests/regagg/ -q`

The live db (`data/sajha.db`) stays out of git; `data/seed/regagg_seed.sql.gz`
is the committed snapshot (reg_* corpus tables only — no users or API keys;
the server builds its own auth on first boot). After significant collection,
refresh it with:

    sqlite3 data/sajha.db ".dump reg_regulators reg_document_edges reg_pending_edges reg_seen_urls reg_documents reg_runs reg_watermarks reg_document_versions reg_document_tags" | gzip > data/seed/regagg_seed.sql.gz
