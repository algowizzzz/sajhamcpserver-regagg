#!/usr/bin/env python3
"""
Blackout every MCP tool except the regulatory/news aggregator's reg_* tools.

The server ships ~500 upstream tools (config/tools/*.json). For the regagg
project only the 12 reg_* tools matter, so this flips `"enabled": false` on
everything else — the registry's own mechanism, honored by tools/list and
tools/call. Fully reversible:

    python scripts/regagg_tool_blackout.py            # keep only reg_*
    python scripts/regagg_tool_blackout.py --restore  # put back original flags

The first run saves every tool's original enabled state to
scripts/tool_enabled_backup.json so --restore is exact, not "enable all".
Restart the server after either operation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TOOLS = REPO / "config" / "tools"
BACKUP = Path(__file__).resolve().parent / "tool_enabled_backup.json"
KEEP_PREFIX = "reg_"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--restore", action="store_true",
                    help="restore the enabled flags saved by the first blackout run")
    args = ap.parse_args()

    configs = sorted(TOOLS.glob("*.json"))
    if args.restore:
        if not BACKUP.exists():
            print(f"no backup at {BACKUP} — nothing to restore")
            return 1
        original = json.loads(BACKUP.read_text())
        restored = 0
        for p in configs:
            cfg = json.loads(p.read_text())
            want = original.get(cfg.get("name", p.stem))
            if want is not None and cfg.get("enabled") != want:
                cfg["enabled"] = want
                p.write_text(json.dumps(cfg, indent=2) + "\n")
                restored += 1
        print(f"restored original enabled flags on {restored} tools — restart the server")
        return 0

    if not BACKUP.exists():
        BACKUP.write_text(json.dumps(
            {json.loads(p.read_text()).get("name", p.stem):
             json.loads(p.read_text()).get("enabled", True) for p in configs},
            indent=2, sort_keys=True) + "\n")

    kept, disabled = [], 0
    for p in configs:
        cfg = json.loads(p.read_text())
        keep = cfg.get("name", p.stem).startswith(KEEP_PREFIX)
        if keep:
            kept.append(cfg.get("name", p.stem))
        if cfg.get("enabled", True) != keep:
            cfg["enabled"] = keep
            p.write_text(json.dumps(cfg, indent=2) + "\n")
            if not keep:
                disabled += 1
    print(f"kept {len(kept)} reg_* tools enabled: {', '.join(sorted(kept))}")
    print(f"disabled {disabled} others — restart the server to apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
