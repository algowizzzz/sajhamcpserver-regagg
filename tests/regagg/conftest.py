"""Shared fixtures for the regagg test suite — SQLite session + local corpus."""

from __future__ import annotations

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from sajha.db.base import Base
import sajha.regagg.models as regmodels  # noqa: F401 — registers reg_* tables
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.core.storage import LocalStorageBackend


@pytest.fixture()
def session() -> Session:
    """In-memory SQLite with only the reg_* corpus tables created."""
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    # create just the regagg tables (core models aren't imported here)
    Base.metadata.create_all(engine, tables=[m.__table__ for m in regmodels.REGAGG_MODELS])
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    s = SessionLocal()
    try:
        yield s
    finally:
        s.close()
        engine.dispose()


@pytest.fixture()
def storage(tmp_path) -> CorpusStorage:
    return CorpusStorage(LocalStorageBackend(base_dir=str(tmp_path)),
                         corpus_prefix="data/web_aggregator")


@pytest.fixture()
def seed_regulator(session):
    """Insert a regulator row (satisfies FK-shaped inserts in realistic tests)."""
    from sajha.regagg.models import Regulator

    def _seed(regulator_id="osfi", jurisdiction="CA", connector="sitemap_diff"):
        reg = Regulator(regulator_id=regulator_id, name=regulator_id.upper(),
                        jurisdiction=jurisdiction, connector=connector, config={})
        session.add(reg)
        session.commit()
        return reg
    return _seed
