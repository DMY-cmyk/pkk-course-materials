import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from render_equations import EQUATIONS, render_equation, main, PNG_DIR, SVG_DIR
from PIL import Image

EXPECTED_IDS = ["eq-return-expost", "eq-return-exante", "eq-capm", "eq-beta", "eq-market-model"]


def test_equation_map_has_five_expected_ids():
    assert list(EQUATIONS.keys()) == EXPECTED_IDS


def test_render_equation_writes_valid_png_and_svg(tmp_path):
    png = os.path.join(tmp_path, "eq-capm.png")
    svg = os.path.join(tmp_path, "eq-capm.svg")
    render_equation(EQUATIONS["eq-capm"], png, svg)
    assert os.path.getsize(png) > 0
    with Image.open(png) as im:
        assert im.width > 0 and im.height > 0
    with open(svg, encoding="utf-8") as fh:
        assert "<svg" in fh.read()


def test_svg_output_is_deterministic(tmp_path):
    # Same equation rendered twice must produce byte-identical SVG (no embedded timestamp).
    png = os.path.join(tmp_path, "x.png")
    svg_a = os.path.join(tmp_path, "a.svg")
    svg_b = os.path.join(tmp_path, "b.svg")
    render_equation(EQUATIONS["eq-capm"], png, svg_a)
    render_equation(EQUATIONS["eq-capm"], png, svg_b)
    with open(svg_a, "rb") as fa, open(svg_b, "rb") as fb:
        assert fa.read() == fb.read()


def test_main_writes_all_ten_files():
    main()
    for eq_id in EXPECTED_IDS:
        assert os.path.getsize(os.path.join(PNG_DIR, f"{eq_id}.png")) > 0
        assert os.path.getsize(os.path.join(SVG_DIR, f"{eq_id}.svg")) > 0
