#!/bin/bash
# Nightly backup: consistent SQLite snapshot + corpus + configs.
# Usage: ./scripts/regagg_backup.sh [dest_root]     (default ~/Backups/regagg)
# Cron:  30 5 * * * ./scripts/regagg_backup.sh >> logs/backup.log 2>&1
set -euo pipefail
cd "$(dirname "$0")/.."
DEST_ROOT="${1:-$HOME/Backups/regagg}"
STAMP=$(date +%Y-%m-%d)
DEST="$DEST_ROOT/$STAMP"
mkdir -p "$DEST"

# 1. DB: online-consistent snapshot (safe while server/crawls run)
sqlite3 data/sajha.db ".backup '$DEST/sajha.db'"

# 2. Corpus (canonical store + markdown projection) — incremental via hardlinks
#    against the previous day's backup, so unchanged files cost no extra disk.
PREV=$(ls -1d "$DEST_ROOT"/20* 2>/dev/null | grep -v "$STAMP" | tail -1 || true)
LINKARG=""
[ -n "$PREV" ] && LINKARG="--link-dest=$PREV/data"
rsync -a --delete $LINKARG data/web_aggregator data/markdown "$DEST/data/"

# 3. Configs (regulators, tools, keys) — small but essential to restore
rsync -a config "$DEST/"

# 4. Retention: keep last 7 dailies (portable — macOS head lacks -n -7)
COUNT=$(ls -1d "$DEST_ROOT"/20* | wc -l | tr -d ' ')
if [ "$COUNT" -gt 7 ]; then
  ls -1d "$DEST_ROOT"/20* | head -n $((COUNT - 7)) | xargs rm -rf
fi

echo "[backup] $STAMP -> $DEST  ($(du -sh "$DEST" | cut -f1))  retained: $(ls -1d "$DEST_ROOT"/20* | wc -l | tr -d ' ')"
