"""
Load and validate regulator configs from ``config/regulators/*.yaml``.

Files whose names start with ``_`` are treated as non-regulator config
(``_taxonomy.yaml``, ``_settings.yaml``) and skipped by the regulator loader.

The loader is deliberately dependency-light (pathlib + yaml + pydantic) so it
can run in CI as the Foundation gate without booting the full server.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, List, Tuple

import yaml
from pydantic import ValidationError

from sajha.regagg.config_models import DOC_TYPES, RegulatorConfig

logger = logging.getLogger(__name__)

DEFAULT_REGULATORS_DIR = "config/regulators"


def _regulators_dir(base: str | Path | None = None) -> Path:
    d = Path(base) if base else Path(DEFAULT_REGULATORS_DIR)
    if not d.is_absolute():
        d = Path.cwd() / d
    return d


def iter_config_paths(base: str | Path | None = None) -> List[Path]:
    """Regulator YAML files (sorted), excluding ``_*`` meta files."""
    d = _regulators_dir(base)
    if not d.is_dir():
        raise FileNotFoundError(f"regulators config dir not found: {d}")
    return sorted(
        p for p in d.glob("*.yaml")
        if not p.name.startswith("_")
    )


def load_one(path: str | Path) -> RegulatorConfig:
    """Parse and validate a single regulator config. Raises on error."""
    path = Path(path)
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{path.name}: top-level YAML is not a mapping")
    cfg = RegulatorConfig.model_validate(raw)
    # Filename must match the declared id (keeps config/{id}.yaml discoverable).
    if cfg.id != path.stem:
        raise ValueError(f"{path.name}: id '{cfg.id}' != filename stem '{path.stem}'")
    return cfg


def load_all(base: str | Path | None = None) -> Dict[str, RegulatorConfig]:
    """Load every regulator config. Raises on the first invalid file.

    Use :func:`validate_all` for a non-throwing report over the whole set.
    """
    out: Dict[str, RegulatorConfig] = {}
    for path in iter_config_paths(base):
        cfg = load_one(path)
        if cfg.id in out:
            raise ValueError(f"duplicate regulator id '{cfg.id}'")
        out[cfg.id] = cfg
    return out


def validate_all(
    base: str | Path | None = None,
) -> Tuple[Dict[str, RegulatorConfig], List[Tuple[str, str]]]:
    """Load every config, collecting errors instead of raising.

    Returns ``(valid_by_id, errors)`` where ``errors`` is a list of
    ``(filename, message)``. Used by the Foundation verify script.
    """
    valid: Dict[str, RegulatorConfig] = {}
    errors: List[Tuple[str, str]] = []
    for path in iter_config_paths(base):
        try:
            cfg = load_one(path)
        except ValidationError as e:
            errors.append((path.name, _fmt_validation_error(e)))
            continue
        except Exception as e:  # noqa: BLE001 — surface any load failure verbatim
            errors.append((path.name, str(e)))
            continue
        if cfg.id in valid:
            errors.append((path.name, f"duplicate regulator id '{cfg.id}'"))
            continue
        valid[cfg.id] = cfg
    return valid, errors


def _fmt_validation_error(e: ValidationError) -> str:
    parts = []
    for err in e.errors():
        loc = ".".join(str(x) for x in err["loc"])
        parts.append(f"{loc}: {err['msg']}")
    return "; ".join(parts)


__all__ = [
    "DOC_TYPES",
    "DEFAULT_REGULATORS_DIR",
    "iter_config_paths",
    "load_one",
    "load_all",
    "validate_all",
]
