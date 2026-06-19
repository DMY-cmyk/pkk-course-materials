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

def test_controls_js_defines_all_behaviors():
    import os
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    js = open(os.path.join(ROOT, "analysis", "pert11_controls.js"),
              encoding="utf-8").read()
    # keyboard
    assert "keydown" in js
    for key in ("ArrowRight", "ArrowLeft", "Home", "End", " "):
        assert key in js
    # fullscreen + overview + click zones + progress
    assert "requestFullscreen" in js
    assert "Escape" in js and "overview" in js
    assert "clientX" in js  # left/right click-zone logic
    assert "progress" in js and "cur" in js

def test_build_html_is_complete_and_self_contained():
    import os
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html = b.build_html(os.path.join(ROOT, b.SOURCE_PDF))
    assert html.count('class="slide"') == 18
    assert "{{SLIDES}}" not in html and "{{CONTROLS_JS}}" not in html \
        and "{{SLIDE_COUNT}}" not in html
    assert "/ 18" in html  # counter total substituted
    # Self-contained: the only http(s) URIs allowed are XML namespace
    # declarations (e.g. xmlns="http://www.w3.org/2000/svg"), which are
    # identifiers, not network loads. Strip them, then require no real
    # external references remain.
    import re
    non_ns = re.sub(r'\sxmlns(?::\w+)?="[^"]*"', '', html)
    for bad in ("http://", "https://", "<link", "@import", 'src="//'):
        assert bad not in non_ns, f"external reference found: {bad}"
    # ids unique across whole document
    ids = re.findall(r'id="([^"]+)"', html)
    assert len(ids) == len(set(ids))

def test_build_html_deterministic():
    import os
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p = os.path.join(ROOT, b.SOURCE_PDF)
    assert b.build_html(p) == b.build_html(p)


TEMPLATE_PDF = "Presentation Template Pert. 11 Canva.pdf"

def test_load_pages_accepts_expected_pages_param():
    svgs = b.load_pages(os.path.join(ROOT, TEMPLATE_PDF), expected_pages=10)
    assert len(svgs) == 10
    for i, s in enumerate(svgs):
        assert "<svg" in s and "</svg>" in s, f"page {i} missing svg tags"
        assert len(s) > 1000, f"page {i} suspiciously small"

def test_load_pages_wrong_expected_count_raises():
    with pytest.raises(ValueError):
        b.load_pages(os.path.join(ROOT, TEMPLATE_PDF), expected_pages=18)

def test_build_html_template_has_10_slides():
    html = b.build_html(os.path.join(ROOT, TEMPLATE_PDF), expected_pages=10)
    assert html.count('class="slide"') == 10
    assert "/ 10" in html
    assert "{{SLIDES}}" not in html and "{{SLIDE_COUNT}}" not in html \
        and "{{CONTROLS_JS}}" not in html

def test_main_writes_named_output(tmp_path):
    out = tmp_path / "deck.html"
    b.main(["--source", TEMPLATE_PDF, "--output", str(out), "--pages", "10"])
    html = out.read_text(encoding="utf-8")
    assert html.count('class="slide"') == 10
    assert "/ 10" in html
