"""
Object-storage layout for the corpus, layered over the SAJHA storage backend
(``sajha.core.storage.get_storage`` — local | s3/minio | azure | gcs).

Normalized layout (identical for all 30 regulators; never mirrors source sites):

    {corpus_prefix}/{regulator_id}/
        _state/...
        staging/{doc_id}/{run_id}/            (transient)
        current/{doc_type}/{year}/{doc_id}/   (exactly one live version)
            raw.{html|pdf}  content.md  meta.json  summary.md
        archive/{doc_type}/{year}/{doc_id}/{version_ts}/   (append-only)

All writes go through the backend so the same code runs on local disk in dev and
S3/MinIO in prod. "COPY" is implemented via read+write because MinIO has no
atomic cross-prefix rename (the versioning protocol + reconcile carry
correctness, see versioning.py).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Dict, List, Optional

DEFAULT_CORPUS_PREFIX = "data/web_aggregator"
ARTIFACTS = ("raw", "content.md", "meta.json", "summary.md")


@dataclass
class DocArtifacts:
    """The four (five) files that make up one document version."""
    raw: Optional[bytes] = None
    raw_ext: str = "html"          # html | pdf
    content_md: str = ""
    meta: Optional[Dict] = None
    summary_md: str = ""
    raw_secondary: Optional[bytes] = None
    raw_secondary_ext: Optional[str] = None


class CorpusStorage:
    """Path builder + artifact IO for one corpus. Stateless over the backend."""

    def __init__(self, backend=None, corpus_prefix: str = DEFAULT_CORPUS_PREFIX):
        if backend is None:
            from sajha.core.storage import get_storage
            backend = get_storage()
        self.backend = backend
        self.prefix = corpus_prefix.rstrip("/")

    # ── path builders ───────────────────────────────────────────────────────

    def reg_root(self, regulator_id: str) -> str:
        return f"{self.prefix}/{regulator_id}"

    def state_prefix(self, regulator_id: str) -> str:
        return f"{self.reg_root(regulator_id)}/_state"

    def current_prefix(self, regulator_id: str, doc_type: str, year: int, doc_id: str) -> str:
        return f"{self.reg_root(regulator_id)}/current/{doc_type}/{year}/{doc_id}"

    def archive_prefix(self, regulator_id: str, doc_type: str, year: int,
                       doc_id: str, version_ts: str) -> str:
        return f"{self.reg_root(regulator_id)}/archive/{doc_type}/{year}/{doc_id}/{version_ts}"

    def staging_prefix(self, regulator_id: str, doc_id: str, run_id: str) -> str:
        return f"{self.reg_root(regulator_id)}/staging/{doc_id}/{run_id}"

    # ── artifact IO ─────────────────────────────────────────────────────────

    def write_artifacts(self, dest_prefix: str, arts: DocArtifacts) -> List[str]:
        """Write the artifact set under dest_prefix (idempotent overwrite).
        Returns the list of written paths."""
        written: List[str] = []
        if arts.raw is not None:
            p = f"{dest_prefix}/raw.{arts.raw_ext}"
            self.backend.write_bytes(p, arts.raw)
            written.append(p)
        if arts.raw_secondary is not None and arts.raw_secondary_ext:
            p = f"{dest_prefix}/raw_secondary.{arts.raw_secondary_ext}"
            self.backend.write_bytes(p, arts.raw_secondary)
            written.append(p)
        p = f"{dest_prefix}/content.md"
        self.backend.write_text(p, arts.content_md)
        written.append(p)
        p = f"{dest_prefix}/meta.json"
        self.backend.write_text(p, json.dumps(arts.meta or {}, indent=2, default=str))
        written.append(p)
        p = f"{dest_prefix}/summary.md"
        self.backend.write_text(p, arts.summary_md or "")
        written.append(p)
        return written

    def read_meta(self, prefix: str) -> Optional[Dict]:
        p = f"{prefix}/meta.json"
        if not self.backend.exists(p):
            return None
        return json.loads(self.backend.read_text(p))

    def read_content(self, prefix: str) -> Optional[str]:
        p = f"{prefix}/content.md"
        if not self.backend.exists(p):
            return None
        return self.backend.read_text(p)

    def read_summary(self, prefix: str) -> Optional[str]:
        p = f"{prefix}/summary.md"
        if not self.backend.exists(p):
            return None
        return self.backend.read_text(p)

    # ── tree ops (COPY = read+write; append-only archive never overwrites) ──

    def list_tree(self, prefix: str) -> List[str]:
        try:
            files = self.backend.list_files(prefix, "*")
        except Exception:
            return []
        # backend.list_files returns paths relative to base; keep those under prefix
        return [f for f in files if f == prefix or f.startswith(prefix + "/")]

    def exists_tree(self, prefix: str) -> bool:
        return bool(self.list_tree(prefix))

    def copy_tree(self, src_prefix: str, dst_prefix: str) -> int:
        """Copy every file under src to the mirrored path under dst. Returns count."""
        n = 0
        for src in self.list_tree(src_prefix):
            rel = src[len(src_prefix):].lstrip("/")
            dst = f"{dst_prefix}/{rel}" if rel else dst_prefix
            self.backend.write_bytes(dst, self.backend.read_bytes(src))
            n += 1
        return n

    def delete_tree(self, prefix: str) -> int:
        n = 0
        for p in self.list_tree(prefix):
            if self.backend.delete(p):
                n += 1
        return n
