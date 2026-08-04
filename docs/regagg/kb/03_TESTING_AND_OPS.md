# 03 — Testing Inventory & Operations Runbook

## Test suite — 92 tests, all offline/deterministic
Run: `./.venv/bin/python -m pytest tests/regagg/ -q`   (~3s)
Fixtures: in-memory SQLite (reg_* tables only) + tmp-dir corpus storage
(`tests/regagg/conftest.py`). Network is ALWAYS injected (fixture openers).

| File | Covers |
|---|---|
| test_versioning.py (10) | create/update/archive; **chaos: crash injected after every protocol step → reconcile restores invariants, zero loss**; idempotent reconcile |
| test_connectors_pipeline.py (7) | 3 connector engines vs real repo configs; OSFI e2e incl. forced update→archive; same-day rerun idempotency |
| test_orchestrator.py (2) | fleet fan-out failure isolation; rerun subset + operator audit |
| test_enrichment.py (3) | LLM-slot enrichment: taxonomy tags, dates, supersedes flip, pending edges, invalid-JSON → enrichment_pending |
| test_rules_and_capture.py (8) | reference grammars; sentence-scoped supersede detection; PDF harvest+source_kind; meta-source dedup; backfill cutoff; **markdown projection layout+frontmatter** |
| test_mcp_tools.py (8) | all 12 tools against seeded corpus; generated configs valid; trigger uses runtime stub |
| test_ui_endpoints.py (10) | tree/browse/changes/diff/runs/inventory; **filter-before-LIMIT regression**; manual add+update (v2); multipart PDF upload; fs jail (path traversal → 400) |
| test_admin.py (5) | coverage matrix, drill-down, audited rerun/toggle, integrity |
| test_fetch.py (4) | html→md; **PDF by magic bytes** (block-page-as-.pdf regression); URL-title humanizer |
| test_verify_sources.py (6) | pass/warn(stale)/fail(content-type/404/thin/unreachable); sitemap-index support |
| test_recorded_fixtures.py (2, ×29 params) | every regulator's connector parses its REAL recorded payload (tests/fixtures/, 9.6MB) |
| Foundation gate | `scripts/regagg_verify_foundation.py` — 30/30 configs parse, taxonomy sync, tables register |

## Scripts (scripts/regagg_*)
| Script | Purpose |
|---|---|
| **regagg_daily_poll.py** | THE scheduler entrypoint: fleet delta ingest (giants capped 500/day; `--deep` weekly 3000) → pending-edge resolve → reconcile → projection resync → one-line summary; exit≠0 on invariant violations |
| regagg_ingest_live.py | manual/targeted ingest: `--only ids --max-docs N --include <url-regex> --giants --giant-cap --skip --operator` |
| regagg_backup.sh | nightly: consistent sqlite .backup + hardlink-incremental rsync of data/ + configs; 7-day retention; dest ~/Backups/regagg |
| verify_sources.py | live source verification (the trust gate; run before onboarding any source) |
| regagg_add_doc.py | manual doc add (URL fetch / --file PDF / --md corrected markdown) |
| regagg_backfill_rules.py | re-run deterministic enrichment over whole corpus |
| regagg_gen_tool_configs.py | regenerate config/tools/reg_*.json from tool classes |
| regagg_record_fixtures.py | re-record per-regulator test fixtures (network, once) |
| regagg_purge_demo.py / migrate_001 / seed_demo | historical one-offs; read before reusing |

## Cron lines to register (user's scheduler)
```
0 6 * * *   cd <repo> && ./.venv/bin/python scripts/regagg_daily_poll.py >> logs/regagg_daily.log 2>&1
0 2 * * 6   cd <repo> && ./.venv/bin/python scripts/regagg_daily_poll.py --deep >> logs/regagg_daily.log 2>&1
30 5 * * *  cd <repo> && ./scripts/regagg_backup.sh >> logs/backup.log 2>&1
```

## Common operations
- Start server: `./.venv/bin/python run_server.py --port 3005`
- Rerun one regulator from UI (▶ Run) or:
  `POST /api/regagg/rerun {"scope":"ids","ids":["osfi"]}` (spawns detached; refuses if one active)
- Gap-fill a section: `regagg_ingest_live.py --only osfi --include "/en/guidance"`
- Integrity check/repair: GET /api/regagg/integrity (runs reconcile)
- Restore drill: copy ~/Backups/regagg/<date>/ over data/ + sajha.db, start server
- Add regulator #31: write config/regulators/{id}.yaml → verify_sources.py
  --regulator id → fix per report → it joins the next daily run
- Rotate an agent key: insert new ApiKey row (sha256 hash) in DB, disable old
  (see BUILD_LOG session 3; NEVER commit keys)
