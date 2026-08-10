"""Reading a long document to the end, and keeping notes while you do.

The bug behind all of this: a 104,508-character OSFI capital guideline was
delivered to the worker 5,500 characters at a time, and the worker told a user
"the corpus does not contain the risk-weight tables". It did. They start at
character 27,519. The read was truncated, the corpus was complete, and nothing
in the tool result made those two distinguishable.

So the properties are: a window says how much of the document it is, paging
reaches the end, the harness says when IT dropped something, and the notepad
lets a long pass record findings instead of holding everything in the window.
"""

from __future__ import annotations

import json

import pytest

from sajha.regagg import notepad as NP


# ── the notepad ─────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def pad(tmp_path, monkeypatch):
    monkeypatch.setattr(NP, "root", lambda: tmp_path / "notepads")
    NP.set_owner("desk@bank.test")
    yield


def test_a_note_survives_and_reads_back():
    NP.write("OSFI caps Group 2 at 5% of Tier 1 [doc cdacb487].", section="crypto")
    assert "5% of Tier 1" in NP.read(section="crypto")["content"]


def test_appending_is_the_default_so_a_long_pass_cannot_erase_itself():
    """A worker that overwrites at document 30 of 40 loses the whole pass."""
    NP.write("first finding", section="crypto")
    NP.write("second finding", section="crypto")
    body = NP.read(section="crypto")["content"]
    assert "first finding" in body and "second finding" in body


def test_replace_has_to_be_asked_for_by_name():
    NP.write("draft", section="crypto")
    NP.write("consolidated", section="crypto", mode="replace")
    body = NP.read(section="crypto")["content"]
    assert body.strip() == "consolidated"


def test_an_unknown_mode_is_refused_rather_than_guessed():
    NP.write("x", section="a")
    out = NP.write("y", section="a", mode="overwrite")
    assert out["ok"] is False and "append" in out["error"]
    assert NP.read(section="a")["content"] == "x"      # nothing was lost


def test_sections_stay_separate():
    NP.write("about capital", section="capital")
    NP.write("about liquidity", section="liquidity")
    assert NP.read(section="capital")["content"] == "about capital"
    assert {s["section"] for s in NP.index()} == {"capital", "liquidity"}


def test_reading_with_no_section_returns_the_index_not_the_contents():
    """The whole point: the index costs tens of characters, the notes cost
    thousands. Returning everything each step is the cost this avoids."""
    NP.write("x" * 5000, section="long")
    out = NP.read()
    assert "content" not in out
    assert out["index"][0]["chars"] >= 5000


def test_a_heading_inside_a_note_cannot_split_the_notepad():
    """Caught live. The worker wrote a tidy '## OSFI guideline' at the top of
    its note; on the next read that line was a section boundary, so the section
    it had NAMED came back empty and the content sat under a phantom heading.
    A note that reads back as lost is worse than no notepad."""
    NP.write("## OSFI guideline\nGroup 2b is a CET1 deduction [doc abc].",
             section="crypto")
    assert [s["section"] for s in NP.index()] == ["crypto"]
    body = NP.read(section="crypto")["content"]
    assert "Group 2b" in body
    assert "### OSFI guideline" in body          # kept, just demoted


def test_a_single_hash_heading_is_demoted_too():
    NP.write("# Title\nbody", section="s")
    assert [x["section"] for x in NP.index()] == ["s"]
    assert "### Title" in NP.read(section="s")["content"]


def test_a_hash_that_is_not_a_heading_is_left_alone():
    NP.write("weight #1 and #hashtag", section="s")
    assert NP.read(section="s")["content"] == "weight #1 and #hashtag"


def test_a_missing_section_names_the_ones_that_exist():
    NP.write("x", section="capital")
    out = NP.read(section="nope")
    assert out["ok"] is False and out["sections"] == ["capital"]


def test_an_empty_notepad_says_so_rather_than_erroring():
    out = NP.read()
    assert out["ok"] is True and out["empty"] is True


def test_a_long_section_pages_like_a_document():
    NP.write("y" * 1000, section="big")
    first = NP.read(section="big", max_chars=400)
    assert first["truncated"] is True and first["next_offset"] == 400
    second = NP.read(section="big", max_chars=400, offset=first["next_offset"])
    assert second["offset"] == 400 and len(second["content"]) == 400


def test_the_summary_line_is_one_line_and_empty_when_there_is_nothing():
    assert NP.summary_line() == ""
    NP.write("x", section="capital")
    line = NP.summary_line()
    assert "capital" in line and "\n" not in line


# ── ownership and safety ────────────────────────────────────────────────────

def test_two_people_do_not_share_a_notepad():
    """The second person sees an empty pad — not the first person's notes, and
    not an error either, because an empty notepad is a normal state."""
    NP.set_owner("a@bank.test")
    NP.write("mine", section="s")
    NP.set_owner("b@bank.test")
    assert NP.read() == {"ok": True, "notepad": "scratch", "sections": [],
                         "empty": True,
                         "hint": "Nothing written yet. Use notepad_write as you read."}
    NP.set_owner("a@bank.test")
    assert NP.read(section="s")["content"] == "mine"      # still there


def test_a_traversing_name_cannot_escape_the_notepad_directory(tmp_path):
    """The name arrives from a model, and a model can be talked into '../'."""
    NP.write("x", section="s", name="../../../../etc/passwd")
    written = list((tmp_path / "notepads").rglob("*.md"))
    assert len(written) == 1
    assert (tmp_path / "notepads") in written[0].parents


def test_a_section_that_would_grow_past_the_cap_is_refused_not_silently_cut():
    NP.write("x" * 100, section="s")
    out = NP.write("y" * (NP.MAX_SECTION_CHARS + 1), section="s")
    assert out["ok"] is False and "summarise" in out["error"]
    assert NP.read(section="s")["content"] == "x" * 100


def test_writing_nothing_is_refused():
    assert NP.write("   ", section="s")["ok"] is False


# ── paging a document ───────────────────────────────────────────────────────

class _Index:
    """A stand-in corpus holding one long document."""

    def __init__(self, body):
        self.body = body

    def get(self, doc_id=None, path=None):
        if doc_id != "long":
            return None
        return {"doc_id": "long", "path": "p.md", "title": "T", "source": "osfi",
                "doc_type": "guidance", "published": None, "source_url": "u",
                "status": "active", "version": 1, "body": self.body}


@pytest.fixture()
def reader(monkeypatch):
    from sajha.tools.impl import corpus_tools as CT
    body = "A" * 20000 + "RISK WEIGHT TABLE" + "B" * 20000
    monkeypatch.setattr(CT._CorpusTool, "_index", lambda self: _Index(body))
    t = CT.CorpusReadTool.__new__(CT.CorpusReadTool)
    return t, body


def test_a_window_says_how_much_of_the_document_it_is(reader):
    tool, body = reader
    out = tool.execute({"doc_id": "long", "max_chars": 10000})
    assert out["total_chars"] == len(body)
    assert out["chars_returned"] == 10000
    assert out["pct_of_document"] < 30
    assert out["next_offset"] == 10000


def test_the_note_tells_the_model_not_to_call_it_a_gap_in_the_corpus(reader):
    """The exact failure: 'truncated: true' was reported to a user as missing data."""
    tool, _ = reader
    out = tool.execute({"doc_id": "long", "max_chars": 100})
    assert "offset=100" in out["note"]
    assert "NOT" in out["note"] and "corpus" in out["note"]


def test_paging_reaches_content_the_first_window_could_never_show(reader):
    """The risk-weight tables sat at character 27,519 of 104,508."""
    tool, body = reader
    seen, offset, guard = "", 0, 0
    while offset is not None and guard < 50:
        out = tool.execute({"doc_id": "long", "max_chars": 5000, "offset": offset})
        seen += out["markdown"]
        offset = out["next_offset"]
        guard += 1
    assert "RISK WEIGHT TABLE" in seen
    assert seen == body


def test_the_last_window_is_not_truncated(reader):
    tool, body = reader
    out = tool.execute({"doc_id": "long", "offset": len(body) - 10, "max_chars": 5000})
    assert out["truncated"] is False
    assert out["next_offset"] is None
    assert out["pct_of_document"] == 100.0
    assert "note" not in out


def test_an_offset_past_the_end_returns_empty_rather_than_wrapping(reader):
    tool, body = reader
    out = tool.execute({"doc_id": "long", "offset": len(body) + 500})
    assert out["markdown"] == "" and out["truncated"] is False


def test_read_many_reports_each_document_s_real_size(reader):
    from sajha.tools.impl import corpus_tools as CT
    tool = CT.CorpusReadManyTool.__new__(CT.CorpusReadManyTool)
    tool._index = reader[0]._index
    out = tool.execute({"doc_ids": ["long"], "max_chars_each": 500})
    doc = out["documents"][0]
    assert doc["total_chars"] == len(reader[1])
    assert doc["truncated"] is True and doc["next_offset"] == 500
    # comparing two documents on their opening paragraphs must not pass silently
    assert "corpus_read with offset" in out["note"]


# ── the harness budget ──────────────────────────────────────────────────────

def test_the_harness_says_when_it_was_the_one_that_truncated(monkeypatch):
    """A silent cut is what turned a 5% read into a claim about the corpus."""
    from sajha.regagg import agent as A

    monkeypatch.setattr(A, "MAX_TOOL_CHARS", 300)
    monkeypatch.setattr(A, "_run_tool", lambda n, a: {"markdown": "Z" * 5000})

    class Client:
        def __init__(self):
            self.seen = []

        def chat(self, messages, tools=None):
            self.seen = messages
            if len(self.seen) < 4:
                return {"tool_calls": [{"id": "1", "function":
                        {"name": "corpus_read", "arguments": "{}"}}]}
            return {"content": "done"}

    c = Client()
    out = A.answer("q", client=c, owner="t@bank.test")
    tool_msg = [m for m in c.seen if m.get("role") == "tool"][0]
    assert "TRUNCATED BY THE HARNESS" in tool_msg["content"]
    assert "NOT a gap in the corpus" in tool_msg["content"]
    assert out["steps"][0]["dropped_chars"] > 0


def test_the_budget_is_spent_across_the_run_not_per_call(monkeypatch):
    from sajha.regagg import agent as A

    monkeypatch.setattr(A, "_run_tool", lambda n, a: {"markdown": "Z" * 2000})

    class Client:
        def __init__(self):
            self.calls = 0

        def chat(self, messages, tools=None):
            self.calls += 1
            if self.calls <= 3:
                return {"tool_calls": [{"id": str(self.calls), "function":
                        {"name": "corpus_read", "arguments": "{}"}}]}
            return {"content": "done"}

    out = A.answer("q", client=Client(), owner="t@bank.test", budget=3000)
    left = [s["budget_left"] for s in out["steps"]]
    assert left == sorted(left, reverse=True)      # monotonically consumed
    assert min(left) >= 0                          # and never goes negative
    assert left[-1] == 0                           # and it really runs out
    # the budget bounds corpus text, not the harness's own bookkeeping lines
    assert sum(s["content_chars"] for s in out["steps"]) <= 3000


def test_once_the_budget_is_gone_the_tool_is_not_even_run(monkeypatch):
    """Running a tool to return an apology spends the provider's tokens and
    reads nothing. The only useful move left is to write the answer."""
    from sajha.regagg import agent as A

    ran = []
    monkeypatch.setattr(A, "_run_tool",
                        lambda n, a: ran.append(n) or {"markdown": "Z" * 4000})

    class Client:
        def __init__(self):
            self.calls = 0

        def chat(self, messages, tools=None):
            self.calls += 1
            if self.calls <= 4:
                return {"tool_calls": [{"id": str(self.calls), "function":
                        {"name": "corpus_read", "arguments": "{}"}}]}
            return {"content": "done"}

    out = A.answer("q", client=Client(), owner="t@bank.test", budget=2000)
    skipped = [s for s in out["steps"] if s.get("skipped")]
    assert skipped, "later calls should be refused, not served an apology"
    assert len(ran) < 4                       # the tool really was not invoked
