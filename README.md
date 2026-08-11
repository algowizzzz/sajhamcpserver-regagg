# riskGPT — financial web data aggregator

An on-prem system that watches **30 financial regulators and 25 news wires**,
versions everything they publish into a governed corpus (26k+ documents), and
serves it through an analyst dashboard, a grounded AI worker, and MCP tools.

> **Read this first on a new machine.** The full documentation lives in
> **[docs/regagg/kb/00_START_HERE.md](docs/regagg/kb/00_START_HERE.md)** — it is
> written for the next developer or coding agent and verified against the
> running system.

## Quickstart on a fresh clone

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
./.venv/bin/python -m scripts.regagg_migrate          # create the reg_* tables
REGAGG_SECRET=<pick-any-secret> ./.venv/bin/python run_server.py --port 3005
```

Then open **http://localhost:3005/api/regagg/ui**

- **There are no accounts on a fresh machine.** The user database
  (`data/sajha.db`) is deliberately not in git. Click **"Create one"** and sign
  up — **the first account created becomes the admin.**
- `REGAGG_SECRET` signs the session cookie; without it, login cannot work.
- `DEEPSEEK_API_KEY` is optional — without it, chat and narration degrade to
  deterministic output; nothing breaks.

## What to expect on first boot

- **Chat and document reading work immediately** — the markdown corpus
  (`data/markdown/`, 20k+ files) is tracked in git and the corpus tools read it
  directly.
- **Dashboard counts start near zero** — they read the SQLite index, which is
  not in git. They fill as collection runs: press **▶ Run all** on the
  Collection page (capped at 200 docs/source by default), or install the daily
  schedule from the Health page.
- The raw HTML/PDF archive (`data/web_aggregator/`, ~5 GB) is **not** in git;
  it rebuilds by re-collecting. A clone cannot serve raw originals until then.

## ⚠️ Two login pages — use the right one

| URL | What it is | Credentials |
|---|---|---|
| `/api/regagg/ui` | **The application.** Everything in this repo's docs refers to this | Your own signup (above) |
| `/` (root, and the legacy MCP pages) | Leftover upstream SAJHA shell this app is embedded in | `config/users.json` (admin/admin123) — **not the app; ignore it** |

If you found yourself at a login accepting `admin` / `admin123`, you are on the
legacy shell, not riskGPT.

## Credits

Built on the SAJHA MCP Server by Ashutosh Sinha
([upstream](https://github.com/ajsinha/sajhamcpserver)) — this fork keeps its
FastAPI runtime, DB engine, and tool registry, and replaces the rest with the
aggregator. Never push to the upstream remote.
