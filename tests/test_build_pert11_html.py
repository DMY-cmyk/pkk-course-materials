# tests/test_build_pert11_html.py
import os
import pytest
import analysis.build_pert11_html as b

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_load_pages_returns_18_nonempty_svgs():
    svgs = b.load_pages(os.path.join(ROOT, b.SOURCE_PDF))
    assert len(svgs) == b.EXPECTED_PAGES == 18
    for i, s in enumerate(svgs):
        assert s.strip().startswith("<"), f"page {i} not SVG"
        assert "<svg" in s and "</svg>" in s, f"page {i} missing svg tags"
        assert len(s) > 1000, f"page {i} suspiciously small"

def test_load_pages_is_deterministic():
    p = os.path.join(ROOT, b.SOURCE_PDF)
    assert b.load_pages(p) == b.load_pages(p)
