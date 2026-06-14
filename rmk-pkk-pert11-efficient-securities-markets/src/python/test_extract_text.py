import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_text import segment, page_numbers  # noqa: E402


# ── copied from pert9 (content-agnostic helpers) ──────────────────────────────

def test_segments_in_order_with_preamble():
    secs = [("Section A", "02_section_a"), ("Section B", "04_section_b")]
    lines = ["[[page:1]]", "Title preamble", "Section A", "body A",
             "[[page:2]]", "Section B", "body B"]
    segs = segment(lines, secs)
    assert [s for s, _ in segs] == ["00_preamble", "02_section_a", "04_section_b"]
    assert "body A" in segs[1][1] and "body B" in segs[2][1]


def test_substring_decoy_does_not_cut():
    # "Summary indicator was coined..." must NOT match the "Summary" heading.
    secs = [("Section A", "02_section_a"), ("Summary", "14_summary")]
    lines = ["Section A", "The term Summary indicator was coined",
             "more body", "Summary", "the real summary"]
    segs = segment(lines, secs)
    assert [s for s, _ in segs] == ["02_section_a", "14_summary"]
    assert "Summary indicator" in segs[0][1]      # decoy stayed in prior section
    assert "the real summary" in segs[1][1]


def test_empty_when_nothing_matches():
    assert segment(["nothing", "here"], SECTIONS_NONE) == []


SECTIONS_NONE = [("Zzz Heading", "x")]


def test_page_numbers():
    assert page_numbers("[[page:305]] a [[page:307]] b [[page:305]]") == [305, 307]


# ── Ch.4-specific tests ───────────────────────────────────────────────────────
# Replaced Ch.13 (Wolk) headings with Ch.4 (Scott) headings.
# Test intent is identical: verify segment() correctly splits on real chapter
# headings, preserves preamble, and places body in the right bucket.

def test_segment_splits_on_ch4_headings():
    lines = ["[[page:2]]", "preamble text",
             "4.2  EFFICIENT SECURITIES MARKETS", "esm body",
             "4.6  INFORMATION ASYMMETRY", "asymm body"]
    sections = [("4.2  EFFICIENT SECURITIES MARKETS", "02_efficient_markets"),
                ("4.6  INFORMATION ASYMMETRY", "06_asymmetry")]
    out = dict(segment(lines, sections))
    assert "00_preamble" in out
    assert "esm body" in out["02_efficient_markets"]
    assert "asymm body" in out["06_asymmetry"]


def test_page_numbers_parses_markers():
    assert page_numbers("a [[page:3]] b [[page:5]] c") == [3, 5]
