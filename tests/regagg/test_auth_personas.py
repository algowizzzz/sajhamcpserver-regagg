"""
Sprint 1 — identity and personas (the Python side of what Playwright covers).

These test the contracts the UI depends on: password hashing, session signing,
tamper rejection, persona versioning and the DERIVED layout rule.
"""

from __future__ import annotations

import time

import pytest

from sajha.regagg import auth, personas
from sajha.regagg.models import Persona, PersonaEntity, RegUser


def _user(session, email="a@bank.test", pw="correct-horse-9"):
    u, err = auth.create_user(session, email, pw, "Tester")
    assert err is None
    return u


def test_password_is_salted_and_never_stored_plain(session):
    u = _user(session)
    assert "correct-horse-9" not in u.password_hash
    assert u.password_hash.startswith("scrypt$")
    other, _ = auth.create_user(session, "b@bank.test", "correct-horse-9")
    assert u.password_hash != other.password_hash      # per-user salt


def test_password_rules_and_duplicate_emails(session):
    assert auth.create_user(session, "c@bank.test", "short")[1] is not None
    assert auth.create_user(session, "not-an-email", "correct-horse-9")[1] is not None
    _user(session, "d@bank.test")
    # email match is case-insensitive: no shadow accounts
    assert auth.create_user(session, "D@BANK.TEST", "correct-horse-9")[1] is not None


def test_authenticate_is_indistinguishable_for_unknown_and_wrong(session):
    _user(session, "e@bank.test")
    _, err_wrong = auth.authenticate(session, "e@bank.test", "nope-nope-nope")
    _, err_unknown = auth.authenticate(session, "ghost@bank.test", "nope-nope-nope")
    assert err_wrong == err_unknown          # never leak account existence


def test_sessions_are_signed_expiring_and_tamper_evident(session):
    u = _user(session, "f@bank.test")
    token = auth.issue_session(u.user_id)
    assert auth.read_session(token) == u.user_id
    assert auth.read_session(token[:-4] + "AAAA") is None      # bad signature
    assert auth.read_session("garbage") is None
    assert auth.read_session(auth.issue_session(u.user_id, ttl=-1)) is None  # expired


def test_persona_layout_is_derived_from_scope_not_chosen(session):
    u = _user(session, "g@bank.test")
    beat = personas.save_persona(session, owner_id=u.user_id, name="Beat",
                                 lane="news", entities=[{"canonical": "Suncor"}])
    assert personas.persona_dict(session, beat)["layout"] == "narrative_first"

    book = personas.save_persona(
        session, owner_id=u.user_id, name="Book", lane="news",
        entities=[{"canonical": f"Ob {i}"} for i in range(60)])
    assert personas.persona_dict(session, book)["layout"] == "exception_first"

    rules = personas.save_persona(session, owner_id=u.user_id, name="Rules",
                                  lane="regulatory", entities=[],
                                  config={"scope": {"rule_families": ["osfi-car"]}})
    assert personas.persona_dict(session, rules)["layout"] == "change_first"


def test_saving_snapshots_a_version(session):
    u = _user(session, "h@bank.test")
    p = personas.save_persona(session, owner_id=u.user_id, name="V", lane="news",
                              entities=[{"canonical": "Alpha"}])
    assert p.version_n == 1
    p = personas.save_persona(session, owner_id=u.user_id, name="V", lane="news",
                              entities=[{"canonical": "Alpha"}, {"canonical": "Beta"}],
                              persona_id=p.persona_id)
    assert p.version_n == 2
    from sajha.regagg.models import PersonaVersion
    snaps = session.query(PersonaVersion).filter_by(persona_id=p.persona_id).all()
    assert {s.version_n for s in snaps} == {1, 2}
    assert {s.entity_count for s in snaps} == {1, 2}     # history is answerable


def test_entity_paste_dedups_and_skips_headers(session):
    rows = personas.parse_entities("name,sector\nGoodfood,consumer\ngoodfood\n\nWestJet")
    assert [r["canonical"] for r in rows] == ["Goodfood", "WestJet"]
    assert rows[0]["meta"]["sector"] == "consumer"


def test_personas_are_private_but_shareable(session):
    owner = _user(session, "i@bank.test")
    other = _user(session, "j@bank.test")
    p = personas.save_persona(session, owner_id=owner.user_id, name="Mine",
                              lane="news", entities=[])
    assert personas.list_personas(session, other.user_id) == []
    assert personas.get_persona(session, p.persona_id, other.user_id)[1] is not None

    personas.save_persona(session, owner_id=owner.user_id, name="Mine", lane="news",
                          persona_id=p.persona_id, shared_with=[other.user_id])
    shared = personas.list_personas(session, other.user_id)
    assert len(shared) == 1 and shared[0]["can_edit"] is False


def test_a_thousand_names_is_one_indexed_join(session):
    """Scale check: a 1,000-name book stores cleanly and reads back whole."""
    u = _user(session, "k@bank.test")
    ents = [{"canonical": f"Obligor {i}", "meta": {"sector": "consumer"}}
            for i in range(1000)]
    p = personas.save_persona(session, owner_id=u.user_id, name="Big", lane="news",
                              entities=ents)
    assert personas.entity_count(session, p.persona_id) == 1000
    assert len(personas.entity_names(session, p.persona_id)) == 1000
    # a re-save replaces rather than accumulating duplicates
    personas.save_persona(session, owner_id=u.user_id, name="Big", lane="news",
                          entities=ents[:10], persona_id=p.persona_id)
    assert personas.entity_count(session, p.persona_id) == 10
