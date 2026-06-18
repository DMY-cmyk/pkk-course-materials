"""
test_build_docx.py — pure-function unit tests for build_docx.py (pert10).
Run: python -m pytest src/python/test_build_docx.py -q
# These are pure-function unit tests only; build() is exercised by the Task 8 end-to-end run.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_docx import (  # noqa: E402
    parse_inline_runs, parse_blocks, split_caption, group_cornell, split_cue_tag,
)


# --- parse_inline_runs -------------------------------------------------------

def test_inline_runs_bold_italic():
    assert parse_inline_runs("a **b** *c*") == [
        ("a ", False, False), ("b", True, False), (" ", False, False), ("c", False, True)
    ]


def test_inline_runs_plain():
    runs = parse_inline_runs("plain text")
    assert runs == [("plain text", False, False)]


def test_inline_runs_bold_only():
    runs = parse_inline_runs("**bold**")
    assert runs == [("bold", True, False)]


def test_inline_runs_italic_only():
    runs = parse_inline_runs("*italic*")
    assert runs == [("italic", False, True)]


# --- split_caption -----------------------------------------------------------

def test_split_caption_with_pipe():
    t, s = split_caption("Tabel 1. Judul | Sumber: diolah dari Wolk et al. (2017)")
    assert t.startswith("Tabel 1.") and s.startswith("Sumber:")


def test_split_caption_without_pipe():
    t, s = split_caption("Gambar 2. Arus Kas")
    assert t == "Gambar 2. Arus Kas"
    assert s is None


# --- parse_blocks ------------------------------------------------------------

def test_parse_blocks_subheading_and_table():
    md = "## I. Judul\n\n### Sub Bagian\n\npara satu\n\n@table(../assets/tables/tabel1.toml)\n\n- butir\n"
    kinds = [k for k, _ in parse_blocks(md)]
    assert kinds == ["heading", "subheading", "para", "table", "bullet"]


def test_parse_blocks_emits_cue_and_notes():
    md = "@cue Apa itu SCF?\n@notes *Statement of cash flows* menyajikan arus kas.\n"
    blocks = parse_blocks(md)
    assert ("cue", "Apa itu SCF?") in blocks
    assert blocks[1][0] == "notes"


def test_parse_blocks_image():
    md = "![Gambar 1. Arus Kas | Sumber: INDF 2024](images/fig1.png)\n"
    blocks = parse_blocks(md)
    assert len(blocks) == 1
    kind, payload = blocks[0]
    assert kind == "image"
    assert payload[1] == "images/fig1.png"


def test_parse_blocks_heading_sets_in_refs_for_referensi():
    md = "## Daftar Referensi\n\nWolk, H. I. (2001). Something.\n"
    blocks = parse_blocks(md)
    assert blocks[0] == ("heading", "Daftar Referensi")
    assert blocks[1][0] == "ref"


def test_parse_blocks_h1_skipped():
    md = "# Judul Utama\n\nisi paragraf\n"
    blocks = parse_blocks(md)
    assert all(k != "heading" or "Judul Utama" not in p for k, p in blocks)


# --- group_cornell -----------------------------------------------------------

def test_group_cornell_pairs_consecutive_rows():
    blocks = [
        ("cue", "Q1"), ("notes", "A1"),
        ("cue", "Q2"), ("notes", "A2"),
        ("image", ("Exhibit 13.2 | Sumber: x", "p.png")),
        ("cue", "Q3"), ("notes", "A3"),
    ]
    grouped = group_cornell(blocks)
    assert grouped[0] == ("cornell", [("Q1", "A1"), ("Q2", "A2")])
    assert grouped[1][0] == "image"
    assert grouped[2] == ("cornell", [("Q3", "A3")])


# --- split_cue_tag -----------------------------------------------------------

def test_split_cue_tag_with_tag():
    assert split_cue_tag("§4.2.1 | Apa definisi efisiensi?") == ("§4.2.1", "Apa definisi efisiensi?")


def test_split_cue_tag_section_level():
    assert split_cue_tag("§4.5 | Apa itu market model?") == ("§4.5", "Apa itu market model?")


def test_split_cue_tag_without_tag():
    assert split_cue_tag("Apa definisi efisiensi?") == (None, "Apa definisi efisiensi?")


def test_group_cornell_single_pair():
    blocks = [("cue", "Q"), ("notes", "A")]
    grouped = group_cornell(blocks)
    assert grouped == [("cornell", [("Q", "A")])]


def test_group_cornell_non_cornell_passthrough():
    blocks = [("heading", "Heading"), ("para", "Body text")]
    grouped = group_cornell(blocks)
    assert grouped == blocks


def test_group_cornell_mixed_interleaved():
    """cue+notes, then a para, then cue+notes — produces 2 cornell groups."""
    blocks = [
        ("cue", "Q1"), ("notes", "A1"),
        ("para", "some text"),
        ("cue", "Q2"), ("notes", "A2"),
    ]
    grouped = group_cornell(blocks)
    assert grouped[0] == ("cornell", [("Q1", "A1")])
    assert grouped[1] == ("para", "some text")
    assert grouped[2] == ("cornell", [("Q2", "A2")])


def test_group_cornell_empty():
    assert group_cornell([]) == []


def test_group_cornell_cue_without_notes_is_dropped():
    """A trailing @cue with no subsequent @notes is silently ignored (no crash)."""
    blocks = [("cue", "Orphan cue")]
    grouped = group_cornell(blocks)
    # orphan cue: no notes block appended → nothing flushed → empty
    assert grouped == []


def test_group_cornell_dangling_cue_before_block_is_dropped():
    # a cue with no notes, then a non-cornell block, then a real pair:
    blocks = [("cue", "Q1"),
              ("heading", "H"),
              ("cue", "Q2"), ("notes", "A2")]
    grouped = group_cornell(blocks)
    # Q1 must NOT pair with A2; Q1 is dropped, heading passes through, then (Q2,A2)
    assert ("heading", "H") in grouped
    assert ("cornell", [("Q2", "A2")]) in grouped
    assert all(not (k == "cornell" and any(c == "Q1" for c, _ in rows))
               for k, rows in grouped if k == "cornell")


def test_group_cornell_orphan_notes_produces_empty_cue():
    grouped = group_cornell([("notes", "Answer with no question")])
    assert grouped == [("cornell", [("", "Answer with no question")])]


def test_parse_blocks_emits_eq():
    md = "@eq \\beta_j = \\frac{Cov(R_j,R_M)}{Var(R_M)}\n"
    blocks = parse_blocks(md)
    assert blocks[0][0] == "eq"
    assert blocks[0][1].startswith("\\beta_j")


def test_parse_blocks_emits_section():
    md = "@section §4.2 — Pasar Sekuritas Efisien\n"
    blocks = parse_blocks(md)
    assert blocks[0] == ("section", "§4.2 — Pasar Sekuritas Efisien")


def test_group_cornell_section_passthrough_flushes_pending():
    blocks = [("cue", "Q1"), ("notes", "A1"),
              ("section", "§4.3 — Implikasi"),
              ("cue", "Q2"), ("notes", "A2")]
    grouped = group_cornell(blocks)
    assert grouped[0] == ("cornell", [("Q1", "A1")])
    assert grouped[1] == ("section", "§4.3 — Implikasi")
    assert grouped[2] == ("cornell", [("Q2", "A2")])
