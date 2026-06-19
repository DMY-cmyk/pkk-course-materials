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

def test_namespace_svg_ids_prefixes_ids_and_refs():
    svg = (
        '<svg><clipPath id="clip_1"><rect/></clipPath>'
        '<g clip-path="url(#clip_1)"><image id="img_2" href="#img_2"/></g></svg>'
    )
    out = b.namespace_svg_ids(svg, 3)
    assert 'id="p03_clip_1"' in out
    assert 'url(#p03_clip_1)' in out
    assert 'href="#p03_img_2"' in out
    assert 'id="clip_1"' not in out  # no bare id remains

def test_namespace_no_collisions_across_pages():
    svg = '<svg><clipPath id="clip_1"/><g clip-path="url(#clip_1)"/></svg>'
    combined = b.namespace_svg_ids(svg, 1) + b.namespace_svg_ids(svg, 2)
    # each page's id appears, and they differ
    assert 'id="p01_clip_1"' in combined and 'id="p02_clip_1"' in combined
    assert combined.count('id="p01_clip_1"') == 1

def test_template_has_required_placeholders_and_no_external_refs():
    tpl = open(os.path.join(ROOT, "analysis", "pert11_shell_template.html"),
               encoding="utf-8").read()
    for token in ("{{SLIDE_COUNT}}", "{{SLIDES}}", "{{CONTROLS_JS}}"):
        assert token in tpl, f"missing placeholder {token}"
    # self-contained: no external resource loads
    for bad in ("http://", "https://", "src=\"//", "<link", "@import"):
        assert bad not in tpl, f"external reference found: {bad}"
    assert "aspect-ratio" in tpl  # 16:9 stage present
