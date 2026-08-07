#!/usr/bin/env bash
# Boot an isolated server (own port + own database copy) and run Playwright.
# Never touches data/sajha.db — a UI run must not mutate the live corpus.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PORT="${PORT:-3011}"
TESTDB="$REPO/data/sajha_uitest.db"

cd "$REPO"

# PG=1 runs the whole suite against PostgreSQL — the on-prem target. The
# database must already hold the corpus (scripts/regagg_pg_load.py).
if [ "${PG:-0}" = "1" ]; then
  export SAJHA_DB_TYPE=postgresql
  export SAJHA_DB_HOST="${SAJHA_DB_HOST:-localhost}" SAJHA_DB_PORT="${SAJHA_DB_PORT:-5432}"
  export SAJHA_DB_NAME="${SAJHA_DB_NAME:-regagg_verify}"
  export SAJHA_DB_USER="${SAJHA_DB_USER:-$(whoami)}" SAJHA_DB_PASSWORD="${SAJHA_DB_PASSWORD:-}"
  export REGAGG_SECRET="ui-test-secret-not-for-production"
  psql -d "$SAJHA_DB_NAME" -qc \
    "TRUNCATE reg_users, reg_personas, reg_persona_entities, reg_persona_versions,
              reg_page_specs CASCADE" >/dev/null 2>&1 || true
  lsof -ti :$PORT | xargs kill 2>/dev/null || true
  ./.venv/bin/python run_server.py --port "$PORT" > /tmp/regagg_uitest.log 2>&1 &
  SERVER_PID=$!
  trap 'kill $SERVER_PID 2>/dev/null || true' EXIT
  for i in $(seq 1 40); do
    curl -sf "http://127.0.0.1:$PORT/api/regagg/auth/me" >/dev/null 2>&1 && break
    sleep 1
  done
  cd tests/ui
  BASE_URL="http://127.0.0.1:$PORT" npx playwright test "$@"
  exit $?
fi

rm -f "$TESTDB"
# A plain cp of a live SQLite file can capture a torn page while a server is
# writing ("database disk image is malformed"). The backup API takes a
# transactionally consistent snapshot instead.
sqlite3 data/sajha.db ".backup '$TESTDB'"       # real corpus, consistent copy
python3 - "$TESTDB" <<'PY'
import sqlite3, sys                              # start with no accounts
db = sqlite3.connect(sys.argv[1])
for t in ("reg_users", "reg_personas", "reg_persona_entities",
          "reg_persona_versions", "reg_page_specs"):
    try: db.execute(f"delete from {t}")
    except sqlite3.OperationalError: pass
db.commit()
PY

export SAJHA_DB_PATH="$TESTDB"   # settings key db.path
export REGAGG_SECRET="ui-test-secret-not-for-production"
lsof -ti :$PORT | xargs kill 2>/dev/null || true
./.venv/bin/python run_server.py --port "$PORT" > /tmp/regagg_uitest.log 2>&1 &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null || true' EXIT

for i in $(seq 1 40); do
  if curl -sf "http://127.0.0.1:$PORT/api/regagg/auth/me" >/dev/null 2>&1; then break; fi
  sleep 1
done

cd tests/ui
BASE_URL="http://127.0.0.1:$PORT" npx playwright test "$@"
