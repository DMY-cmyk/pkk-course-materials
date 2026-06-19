"""render_equations.py — render the chapter's 5 equations to PNG + SVG assets.

LaTeX is copied verbatim from content/A_cornell.md @eq markers (Cov/Var wrapped
\\mathrm{} for upright operator rendering). PNGs are 300-DPI transparent (gitignored,
regenerable); SVGs are committed as the durable source-of-record. Standalone — NOT
part of the docx build pipeline.

Run:  python src/python/render_equations.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# repo root = three levels up: src/python/<file> -> src/python -> src -> repo root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PNG_DIR = os.path.join(REPO_ROOT, "assets", "equations")
SVG_DIR = os.path.join(REPO_ROOT, "assets", "equations", "svg")

# Ordered id -> LaTeX. Verbatim from content/A_cornell.md; Cov/Var -> \mathrm for upright.
EQUATIONS = {
    "eq-return-expost": r"R_{jt} = \frac{P_{jt} + D_{jt} - P_{j,t-1}}{P_{j,t-1}} = \frac{P_{jt} + D_{jt}}{P_{j,t-1}} - 1",
    "eq-return-exante": r"E(R_{jt}) = \frac{E(P_{jt} + D_{jt})}{P_{j,t-1}} - 1",
    "eq-capm": r"E(R_{jt}) = R_f(1 - \beta_j) + \beta_j E(R_{Mt})",
    "eq-beta": r"\beta_j = \frac{\mathrm{Cov}(j, M)}{\mathrm{Var}(M)}",
    "eq-market-model": r"R_{jt} = \alpha_j + \beta_j R_{Mt} + \varepsilon_{jt}",
}


def render_equation(latex, png_path, svg_path, dpi=300):
    """Render one LaTeX equation to a transparent PNG and an SVG. Returns the paths."""
    fig = plt.figure(figsize=(6, 1))
    fig.text(0.5, 0.5, f"${latex}$", fontsize=18, ha="center", va="center")
    fig.savefig(png_path, dpi=dpi, bbox_inches="tight", transparent=True)
    fig.savefig(svg_path, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    return png_path, svg_path


def main():
    os.makedirs(PNG_DIR, exist_ok=True)
    os.makedirs(SVG_DIR, exist_ok=True)
    for eq_id, latex in EQUATIONS.items():
        png = os.path.join(PNG_DIR, f"{eq_id}.png")
        svg = os.path.join(SVG_DIR, f"{eq_id}.svg")
        render_equation(latex, png, svg)
        print(f"wrote {png} + {svg}")


if __name__ == "__main__":
    main()
