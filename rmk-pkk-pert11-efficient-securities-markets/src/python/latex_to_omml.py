"""latex_to_omml.py — LaTeX → Word OMML (native equation) with a PNG fallback.
Python exception #4: no Rust crate emits Word OMML. Route: latex2mathml → MathML →
OMML via Microsoft's shipped MML2OMML.XSL (lxml). Fallback: 300-DPI matplotlib PNG.
Imported by build_docx.py; not a standalone CLI.

NOTE: latex2mathml.convert() is lenient — it does NOT raise on malformed LaTeX,
it wraps unrecognized tokens as <mi> identifiers. So a typo yields a valid-but-wrong
oMath rather than None. Transcribe each equation's LaTeX carefully and eyeball the
rendered result in the built .docx.
"""
import glob
import latex2mathml.converter
from lxml import etree  # type: ignore[attr-defined]  # lxml C-ext lacks Pyright stubs


def _find_xsl():
    pats = [
        r"C:\Program Files\Microsoft Office\root\Office*\MML2OMML.XSL",
        r"C:\Program Files (x86)\Microsoft Office\root\Office*\MML2OMML.XSL",
        r"C:\Program Files\Microsoft Office\Office*\MML2OMML.XSL",
        r"C:\Program Files (x86)\Microsoft Office\Office*\MML2OMML.XSL",
    ]
    for pat in pats:
        hits = glob.glob(pat)
        if hits:
            return hits[0]
    return None


def latex_to_omath(latex):
    """Return an lxml <m:oMath>/<m:oMathPara> element, or None if conversion is unavailable."""
    xsl = _find_xsl()
    if not xsl:
        return None
    try:
        mathml = latex2mathml.converter.convert(latex)
        mml_tree = etree.fromstring(mathml.encode("utf-8"))
        transform = etree.XSLT(etree.parse(xsl))
        return transform(mml_tree).getroot()
    except Exception:
        return None


def render_eq_png(latex, out_path, dpi=300):
    """Render a centered equation to a high-DPI PNG (fallback path)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(6, 1))
    fig.text(0.5, 0.5, f"${latex}$", fontsize=18, ha="center", va="center")
    fig.savefig(out_path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out_path
