"""The dashboard markup has to be structurally sound.

A single stray ``</div>`` closed the page container early and hoisted two
sections out of their view, so they rendered on *every* tab — thousands of
pixels of phantom scroll that no functional test noticed, because every element
still existed and every API still answered. Structure is not covered by asking
"is the text on screen?", so it gets its own check.
"""

from __future__ import annotations

import re
from pathlib import Path

DASHBOARD = Path(__file__).resolve().parents[2] / "sajha" / "regagg" / "ui_dashboard.html"
DIV = re.compile(r"<(/?)div\b[^>]*>", re.S)
IDENT = re.compile(r'(?:id|class)="([^"]+)"')


def _body() -> str:
    src = DASHBOARD.read_text(encoding="utf-8")
    return src[src.index("<body>"):src.index("<script>")]


def test_every_div_is_balanced():
    """No stray closer, no unclosed opener — the two ways a layout silently rots."""
    stack = []
    for m in DIV.finditer(_body()):
        if m.group(1):
            assert stack, f"stray </div> at offset {m.start()}"
            stack.pop()
        else:
            ident = IDENT.search(m.group(0))
            stack.append(ident.group(1) if ident else "")
    assert not stack, f"unclosed <div>: {stack}"


def test_every_view_lives_inside_the_page_container():
    """A view outside .page escapes `display:none` switching and shows always."""
    body = _body()
    depth, page_depth, views_in_page, views_seen = 0, None, [], []
    for m in DIV.finditer(body):
        if m.group(1):
            depth -= 1
            if depth == page_depth:
                page_depth = None
            continue
        ident = IDENT.search(m.group(0))
        name = ident.group(1) if ident else ""
        depth += 1
        if name == "page":
            page_depth = depth - 1
        elif name.startswith("view"):
            vid = re.search(r'id="([^"]+)"', m.group(0))
            vid = vid.group(1) if vid else "?"
            views_seen.append(vid)
            if page_depth is not None:
                views_in_page.append(vid)

    assert views_seen, "no .view elements found — did the markup change shape?"
    orphans = sorted(set(views_seen) - set(views_in_page))
    assert not orphans, f"views rendered outside .page (always visible): {orphans}"


def test_content_containers_keep_their_layout_class_when_filled():
    """`className=""` wipes `scrollbox` and the page grows without bound."""
    src = DASHBOARD.read_text(encoding="utf-8")
    assert '.className="";' not in src, (
        "use classList.remove('empty') — assigning className='' also strips "
        "scrollbox/halfgrid and lets a feed grow to any height"
    )


def test_the_dashboard_does_not_block_on_the_integrity_reconcile():
    """`/integrity` runs a full reconcile over every document — 24 seconds at
    10,277 of them, and it grows with the corpus.

    `loadAll` used to `await` it before loading anything else, so the whole
    dashboard sat blank behind it. Once the corpus outgrew `j()`'s 15s timeout
    every page load stalled the full 30s (two attempts) and the browser suite
    began timing out on unrelated auth tests. A status pill must never gate
    the page.
    """
    src = DASHBOARD.read_text(encoding="utf-8")
    body = src[src.index("async function loadAll"):]
    body = body[:body.index("\n}")]
    assert "integrity" not in body or "await" not in body.split("integrity")[0][-40:], (
        "loadAll must not await /integrity — fire it and fill the pill in later"
    )
    assert "loadIntegrity()" in body, "the pill should still be requested, just not awaited"
