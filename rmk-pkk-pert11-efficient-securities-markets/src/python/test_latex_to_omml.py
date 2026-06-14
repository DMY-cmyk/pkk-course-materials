import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from latex_to_omml import latex_to_omath, render_eq_png

def test_omath_tag_or_none():
    el = latex_to_omath(r"\beta_j = \frac{Cov(R_j, R_M)}{Var(R_M)}")
    # If Office's MML2OMML.XSL is present, we get an oMath/oMathPara element; else None.
    assert el is None or el.tag.endswith("}oMath") or el.tag.endswith("}oMathPara")

def test_png_fallback_writes_file(tmp_path):
    out = os.path.join(tmp_path, "eq.png")
    render_eq_png(r"R_{jt} = \alpha_j + \beta_j R_{Mt} + \varepsilon_{jt}", out)
    assert os.path.exists(out) and os.path.getsize(out) > 0
