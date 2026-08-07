# Ship Plan — Market & Regulatory Intelligence (final build)

Goal: ship the two-app product (🏛️ Regulatory / 📰 Financial News), on-prem,
native signup/login, Postgres+JSONB storage model, everything from the design
sessions in scope. Loop: build → test (pytest + Playwright UI) → document →
review → next sprint, until PMF-ready.

Storage decision: **PostgreSQL + JSONB is the system of record.** Code is
written against SQLAlchemy with JSON columns (JSONB on Postgres, JSON-as-text
on SQLite for dev), so the same code runs in dev and on-prem.

## Sprint S1 — Identity & Personas (foundation)
- S1.1 `reg_users` table: signup/login/logout, scrypt password hashes (stdlib),
  HMAC-signed session cookie (httpOnly). No plaintext secrets in git.
- S1.2 `reg_personas` (config as JSON) + `reg_persona_entities` (indexed names)
  + versioning on every save.
- S1.3 CRUD API: /auth/signup /auth/login /auth/logout /auth/me,
  /personas GET/POST/PUT, entity CSV paste-upload.
- S1.4 UI: login/signup overlay; Personas tab (form + entity upload + preview).
- S1.5 Playwright harness + first UI suite (signup → login → create persona).
- AC: a new user can sign up, log in, create a persona with 1,000+ entities,
  and see it persisted across sessions. All existing 109 tests still green.

## Sprint S2 — Extraction & Distillation (the intelligence)
- S2.1 Ingest-time extraction: AnthropicBackend behind ANTHROPIC_API_KEY env;
  deterministic extractor (classifier + entity scan) as always-on fallback;
  results stored as JSON on the document row; model-version stamped.
- S2.2 Dossier builder: entity/class/topic/rule-family matching, headline
  clustering + corroboration, persona-weighted salience, coverage ledger.
- S2.3 /myday endpoint: dossier → spec (template composer; LLM composer when
  key present) → validated → cached in `reg_page_specs` per persona/day.
- AC: dossier for a seeded persona surfaces a credit event above market noise,
  with a ledger whose counts satisfy the conservation law. Tests prove it.

## Sprint S3 — The two-app UI (My Day · Explore · Ask · Personas · Health)
- S3.1 App shell: two apps over the existing lane model; 5 tabs; switcher.
- S3.2 My Day renderer: component palette bound to live queries; updated-strip.
- S3.3 Health tab: runs + integrity + per-source table + drop counters +
  generation health, consolidated.
- S3.4 Ask tab: context-chip handoff to the agent platform (env AGENT_URL),
  honest setup panel when unconfigured.
- S3.5 Intraday: scripts/regagg_news_poll.py (no full-corpus enrich sweep);
  cron lines documented.
- AC: full Playwright journey — login → My Day renders persona page → drill
  to Explore → Personas edit → Health shows green pipeline.

## Sprint S4 — Ship hardening
- S4.1 Postgres deploy path: DATABASE_URL env, schema DDL, JSONB verified.
- S4.2 DEPLOY_ONPREM.md: uvicorn service, nginx, cron, backups, key setup,
  default-cred hardening.
- S4.3 Full regression: pytest + complete Playwright suite; TEST_CASES + STATUS
  docs regenerated.
- S4.4 PMF review → next sprint list.

Execution log lives in docs/regagg/execution/SHIP_STATUS.md (one line per
story: done/tested/doc'd).
