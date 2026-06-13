import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_text import segment, page_numbers  # noqa: E402


# ── copied from pert9 (content-agnostic helpers) ──────────────────────────────

def test_segments_in_order_with_preamble():
    secs = [("Income Definitions", "02_income"), ("Revenue Recognition", "04_rev")]
    lines = ["[[page:1]]", "Title preamble", "Income Definitions", "body A",
             "[[page:2]]", "Revenue Recognition", "body B"]
    segs = segment(lines, secs)
    assert [s for s, _ in segs] == ["00_preamble", "02_income", "04_rev"]
    assert "body A" in segs[1][1] and "body B" in segs[2][1]


def test_substring_decoy_does_not_cut():
    # "Summary indicator was coined..." must NOT match the "Summary" heading.
    secs = [("Income Definitions", "02_income"), ("Summary", "14_summary")]
    lines = ["Income Definitions", "The term Summary indicator was coined",
             "more body", "Summary", "the real summary"]
    segs = segment(lines, secs)
    assert [s for s, _ in segs] == ["02_income", "14_summary"]
    assert "Summary indicator" in segs[0][1]      # decoy stayed in prior section
    assert "the real summary" in segs[1][1]


def test_empty_when_nothing_matches():
    assert segment(["nothing", "here"], SECTIONS_NONE) == []


SECTIONS_NONE = [("Zzz Heading", "x")]


def test_page_numbers():
    assert page_numbers("[[page:305]] a [[page:307]] b [[page:305]]") == [305, 307]


# ── Ch.13-specific tests ──────────────────────────────────────────────────────

def test_segment_splits_on_ch13_headings():
    lines = ["[[page:1]]", "preamble text",
             "Statement of Changes in Financial Position", "scfp body",
             "Free Cash Flow", "fcf body"]
    sections = [("Statement of Changes in Financial Position", "02_scfp"),
                ("Free Cash Flow", "10_fcf")]
    out = dict(segment(lines, sections))
    assert "00_preamble" in out
    assert "scfp body" in out["02_scfp"]
    assert "fcf body" in out["10_fcf"]


def test_page_numbers_parses_markers():
    assert page_numbers("a [[page:3]] b [[page:5]] c") == [3, 5]
