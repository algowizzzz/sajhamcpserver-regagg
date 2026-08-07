#!/usr/bin/env bash
# Boot an isolated server (own port + own database copy) and run Playwright.
# Never touches data/sajha.db — a UI run must not mutate the live corpus.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PORT="${PORT:-3011}"
TESTDB="$REPO/data/sajha_uitest.db"

cd "$REPO"
rm -f "$TESTDB"
cp data/sajha.db "$TESTDB"                      # real corpus, throwaway copy
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
