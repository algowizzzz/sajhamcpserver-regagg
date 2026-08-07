"""
Ask: the chat may only say what the sources say.

These pin the contract that lets a bank switch it on: grounded, cited, honest
when it cannot answer, and silent rather than wrong when the model misbehaves.
"""

from __future__ import annotations

import json

import pytest

from sajha.regagg import ask as A


class FakeClient:
    """Returns whatever answer the test wants, in the model's own envelope."""

    def __init__(self, payload):
        self.payload = payload
        self.calls = []

    def complete(self, system, user, max_tokens=700):
        self.calls.append({"system": system, "user": user})
        return json.dumps(self.payload)


PACK = {
    "kind": "story cluster",
    "title": "Goodfood creditor protection",
    "context": {"event": "credit_event", "corroboration": 2},
    "sources": [
        {"n": 1, "title": "Goodfood seeks creditor protection",
         "publisher": "BNN", "published": "2026-08-05",
         "regulator_id": "wire_a", "doc_id": "d1", "url": "https://x/d1"},
        {"n": 2, "title": "Court grants Goodfood creditor protection",
         "publisher": "CBC", "published": "2026-08-05",
         "regulator_id": "wire_b", "doc_id": "d2", "url": "https://x/d2"},
    ],
}


def test_a_grounded_cited_answer_is_returned():
    client = FakeClient({"answer": "The court granted protection [2] after the "
                                   "company sought it [1].",
                         "used": [1, 2], "answerable": True})
    out = A.answer_question("What happened?", PACK, client=client)
    assert out["ok"] is True
    assert "[1]" in out["answer"] and "[2]" in out["answer"]
    assert len(out["sources"]) == 2


def test_the_model_only_ever_sees_the_pack():
    """No free retrieval: the prompt carries the sources and nothing else."""
    client = FakeClient({"answer": "Protection was granted [2].", "used": [2]})
    A.answer_question("What happened?", PACK, client=client)
    sent = client.calls[0]["user"]
    assert "Goodfood seeks creditor protection" in sent
    assert "ONLY from the numbered sources" in client.calls[0]["system"]


def test_an_uncited_answer_is_withheld():
    client = FakeClient({"answer": "The company is in serious trouble.", "used": []})
    out = A.answer_question("What happened?", PACK, client=client)
    assert out["ok"] is False and out["generator"] == "rejected"
    assert "could not be verified" in out["answer"]
    assert out["sources"], "the evidence is still handed over"


def test_an_invented_figure_is_withheld():
    client = FakeClient({"answer": "Losses reached 450 million dollars [1].",
                         "used": [1]})
    out = A.answer_question("How big?", PACK, client=client)
    assert out["ok"] is False
    assert any("450" in p for p in out["problems"])


def test_a_citation_that_does_not_exist_is_withheld():
    client = FakeClient({"answer": "A filing was made [7].", "used": [7]})
    out = A.answer_question("What happened?", PACK, client=client)
    assert out["ok"] is False
    assert any("[7]" in p for p in out["problems"])


def test_quoting_a_figure_from_the_sources_is_allowed():
    pack = json.loads(json.dumps(PACK))
    pack["sources"][0]["title"] = "Goodfood owes 45 million to creditors"
    client = FakeClient({"answer": "It owes 45 million [1].", "used": [1]})
    out = A.answer_question("How much?", pack, client=client)
    assert out["ok"] is True          # faithful quoting, not invention


def test_a_provider_failure_degrades_to_the_evidence():
    class Broken:
        def complete(self, *a, **k):
            raise RuntimeError("provider down")
    out = A.answer_question("What happened?", PACK, client=Broken())
    assert out["ok"] is False and out["generator"] == "error"
    assert len(out["sources"]) == 2    # the analyst still gets the sources


def test_no_sources_means_no_answer_attempt():
    out = A.answer_question("What happened?", {"kind": "x", "title": "x",
                                               "sources": []})
    assert out["ok"] is False
    assert "nothing to answer from" in out["answer"]


def test_an_empty_question_is_not_sent_to_the_model():
    client = FakeClient({"answer": "irrelevant", "used": [1]})
    out = A.answer_question("   ", PACK, client=client)
    assert out["ok"] is False and client.calls == []


def test_validation_accepts_a_faithful_summary():
    ok, problems = A.validate_answer(
        "Two wires reported the filing [1][2].", [1, 2], PACK)
    assert ok, problems
