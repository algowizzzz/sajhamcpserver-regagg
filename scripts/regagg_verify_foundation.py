#!/usr/bin/env python3
"""
Foundation gate for the Regulatory Intelligence Aggregator (Epic 1).

Checks, with real data, that the Foundation is sound:
  1. All regulator configs under config/regulators/ parse and validate.
  2. Every doc_type in every config is in the controlled taxonomy.
  3. The reg_* corpus models register on the shared SQLAlchemy Base.metadata.
  4. The taxonomy file is loadable and internally consistent with the models.

Exit code 0 = green (gate passes), 1 = red. No network, no DB connection —
this is safe to run in CI on every commit.

Usage:
    python scripts/regagg_verify_foundation.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Run from repo root regardless of CWD.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import yaml  # noqa: E402

from sajha.regagg.config_loader import iter_config_paths, validate_all  # noqa: E402
from sajha.regagg.config_models import DOC_TYPES  # noqa: E402


GREEN = "\033[92m"
RED = "\033[91m"
DIM = "\033[2m"
RESET = "\033[0m"


def _tick(ok: bool) -> str:
    return f"{GREEN}PASS{RESET}" if ok else f"{RED}FAIL{RESET}"


def check_configs() -> tuple[bool, dict]:
    base = REPO_ROOT / "config" / "regulators"
    paths = iter_config_paths(base)
    valid, errors = validate_all(base)
    ok = not errors
    return ok, {"paths": paths, "valid": valid, "errors": errors}


def check_taxonomy() -> tuple[bool, dict]:
    tax_path = REPO_ROOT / "config" / "regulators" / "_taxonomy.yaml"
    tax = yaml.safe_load(tax_path.read_text(encoding="utf-8"))
    tax_doc_types = set(tax.get("doc_types", []))
    # taxonomy doc_types must match the code-level controlled set exactly.
    match = tax_doc_types == set(DOC_TYPES)
    return match, {"tax_doc_types": tax_doc_types, "code_doc_types": set(DOC_TYPES)}


def check_models() -> tuple[bool, dict]:
    # Importing registers the models on Base.metadata via create_all path.
    from sajha.db.base import Base
    from sajha.regagg.models import REGAGG_MODELS

    expected = {m.__tablename__ for m in REGAGG_MODELS}
    registered = set(Base.metadata.tables.keys())
    missing = expected - registered
    ok = not missing
    return ok, {"expected": expected, "missing": missing,
                "reg_tables": sorted(t for t in registered if t.startswith("reg_"))}


def main() -> int:
    print(f"\n{'='*70}\nRegAgg Foundation Verification (Epic 1)\n{'='*70}")

    all_ok = True

    # 1 + 2 — configs & doc_types --------------------------------------------
    cfg_ok, cfg = check_configs()
    all_ok &= cfg_ok
    n_paths = len(cfg["paths"])
    n_valid = len(cfg["valid"])
    print(f"\n[{_tick(cfg_ok)}] Regulator configs: {n_valid}/{n_paths} parsed & validated")
    if cfg["errors"]:
        for name, msg in cfg["errors"]:
            print(f"        {RED}{name}{RESET}: {msg}")

    if cfg["valid"]:
        by_conn: dict[str, int] = {}
        by_jur: dict[str, int] = {}
        verified_total = 0
        source_total = 0
        for c in cfg["valid"].values():
            by_conn[c.connector] = by_conn.get(c.connector, 0) + 1
            by_jur[c.jurisdiction] = by_jur.get(c.jurisdiction, 0) + 1
            verified_total += c.verified_source_count
            source_total += c.total_source_count
        print(f"        {DIM}connectors: "
              + ", ".join(f"{k}={v}" for k, v in sorted(by_conn.items()))
              + f"  |  jurisdictions: {len(by_jur)}"
              + f"  |  sources verified: {verified_total}/{source_total}{RESET}")
        print(f"        {DIM}(all sources verified=false by design until "
              f"verify_sources runs — Epic 5){RESET}")

    # 3 — taxonomy ------------------------------------------------------------
    tax_ok, tax = check_taxonomy()
    all_ok &= tax_ok
    print(f"\n[{_tick(tax_ok)}] Taxonomy doc_types match code DOC_TYPES "
          f"({len(tax['tax_doc_types'])} types)")
    if not tax_ok:
        print(f"        only-in-taxonomy: {tax['tax_doc_types'] - tax['code_doc_types']}")
        print(f"        only-in-code:     {tax['code_doc_types'] - tax['tax_doc_types']}")

    # 4 — models --------------------------------------------------------------
    mdl_ok, mdl = check_models()
    all_ok &= mdl_ok
    print(f"\n[{_tick(mdl_ok)}] Corpus models registered on shared Base "
          f"({len(mdl['reg_tables'])} reg_* tables)")
    print(f"        {DIM}{', '.join(mdl['reg_tables'])}{RESET}")
    if mdl["missing"]:
        print(f"        {RED}missing: {mdl['missing']}{RESET}")

    print(f"\n{'='*70}")
    if all_ok:
        print(f"{GREEN}FOUNDATION GATE: GREEN{RESET} — Epic 1 ready.\n")
        return 0
    print(f"{RED}FOUNDATION GATE: RED{RESET} — fix the failures above.\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
