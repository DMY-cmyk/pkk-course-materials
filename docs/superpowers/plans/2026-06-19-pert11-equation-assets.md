# Pert. 11 Equation Assets Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Render the 5 Pert. 11 chapter equations to `assets/equations/` (PNG + SVG) and wire the 3 CAPM-family equations into slide deck S13–S15.

**Architecture:** A standalone Python script (`render_equations.py`) renders each LaTeX equation (copied verbatim from `content/A_cornell.md`) to a 300-DPI transparent PNG and an SVG via matplotlib mathtext — the same engine already used by `latex_to_omml.py:render_eq_png`. PNGs are gitignored (regenerable); SVGs are committed (durable record). The slide-deck Markdown then references the PNGs. The script is independent of the docx build pipeline.

**Tech Stack:** Python 3.12, matplotlib (mathtext), PIL/Pillow, pytest. All already in `requirements.txt`.

## Global Constraints

- Work from project root: `rmk-pkk-pert11-efficient-securities-markets/`.
- Equation LaTeX is copied VERBATIM from `content/A_cornell.md` `@eq` lines 60/64/71/75/82; only `Cov`/`Var` are wrapped `\mathrm{}` for upright rendering — no other symbol change.
- The 5 ids, in order: `eq-return-expost`, `eq-return-exante`, `eq-capm`, `eq-beta`, `eq-market-model`.
- Output: `assets/equations/<id>.png` (300 DPI, transparent, gitignored) and `assets/equations/svg/<id>.svg` (committed).
- Do NOT edit `content/A_cornell.md`, any `input/` file, or `build_docx.py`.
- No new third-party dependencies.
- Commit script + test + the 5 SVGs to branch `content/pert11-slide-presentation-draft`; never commit the PNGs (gitignored).
- Slide wiring: S13→`eq-capm.png`, S14→`eq-beta.png`, S15→`eq-market-model.png`; keep each slide's on-slide equation text as caption; leave headlines/scripts/design-hints/Tracker lines unchanged.

---

### Task 1: Equation renderer + tests + generated assets

**Files:**
- Create: `src/python/render_equations.py`
- Test: `src/python/test_render_equations.py`
- Produces (run output): `assets/equations/*.png` (5), `assets/equations/svg/*.svg` (5)

**Interfaces:**
- Produces: `EQUATIONS` (ordered dict `{id: latex}`, 5 entries); `render_equation(latex, png_path, svg_path, dpi=300) -> (png_path, svg_path)`; `main() -> None`; module constants `PNG_DIR`, `SVG_DIR` (absolute paths under the repo root).

- [ ] **Step 1: Write the failing test**

Create `src/python/test_render_equations.py`:

```python
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


def test_main_writes_all_ten_files():
    main()
    for eq_id in EXPECTED_IDS:
        assert os.path.getsize(os.path.join(PNG_DIR, f"{eq_id}.png")) > 0
        assert os.path.getsize(os.path.join(SVG_DIR, f"{eq_id}.svg")) > 0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd "d:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat/rmk-pkk-pert11-efficient-securities-markets" && python -m pytest src/python/test_render_equations.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'render_equations'`.

- [ ] **Step 3: Write the implementation**

Create `src/python/render_equations.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd "d:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat/rmk-pkk-pert11-efficient-securities-markets" && python -m pytest src/python/test_render_equations.py -v`
Expected: PASS (3 passed). `test_main_writes_all_ten_files` also generates the real assets.

- [ ] **Step 5: Generate the assets explicitly and verify count**

Run: `cd "d:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat/rmk-pkk-pert11-efficient-securities-markets" && python src/python/render_equations.py && ls assets/equations/*.png && ls assets/equations/svg/*.svg`
Expected: 5 PNGs listed and 5 SVGs listed (eq-return-expost, eq-return-exante, eq-capm, eq-beta, eq-market-model).

- [ ] **Step 6: Visually confirm one render is correct**

Open `assets/equations/eq-capm.png` and confirm it reads `E(R_jt) = R_f(1 − β_j) + β_j E(R_Mt)` with upright Cov/Var in `eq-beta.png`. (If a symbol is wrong, fix the LaTeX in `EQUATIONS` against `content/A_cornell.md` and re-run.)

---

### Task 2: Wire equation images into slide deck S13–S15

**Files:**
- Modify: `rmk-pkk-pert11-efficient-securities-markets/presentation-guidance/slide-presentation-draft-pert11.md` (S13, S14, S15 Visual fields only)

**Interfaces:**
- Consumes: the PNG asset paths produced by Task 1 (`assets/equations/eq-capm.png`, `eq-beta.png`, `eq-market-model.png`).

- [ ] **Step 1: Read the current S13–S15 blocks**

Read the file and locate slides S13 (CAPM), S14 (beta), S15 (market model). Note each one's current `**Visual:**` line (currently a `build:` equation description) and its on-slide equation text.

- [ ] **Step 2: Update S13 Visual**

Set S13's `**Visual:**` line to:

```
**Visual:** `assets/equations/eq-capm.png` — caption: Sharpe–Lintner CAPM (Scott, 2015) · render dari content/A_cornell.md. Visual pendukung tersedia: `assets/equations/eq-return-expost.png` & `assets/equations/eq-return-exante.png` untuk setup ex-post/ex-ante.
```

Leave S13's headline, on-slide equation text (keep as caption/fallback), speaker script, design hint, and Tracker line unchanged.

- [ ] **Step 3: Update S14 Visual**

Set S14's `**Visual:**` line to:

```
**Visual:** `assets/equations/eq-beta.png` — caption: Beta = Cov(j,M)/Var(M) (Scott, 2015)
```

Leave the rest of S14 unchanged.

- [ ] **Step 4: Update S15 Visual**

Set S15's `**Visual:**` line to:

```
**Visual:** `assets/equations/eq-market-model.png` — caption: Market model (Scott, 2015)
```

Leave the rest of S15 unchanged.

- [ ] **Step 5: Verify the wiring**

Run: `cd "d:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat/rmk-pkk-pert11-efficient-securities-markets/presentation-guidance" && grep -n "assets/equations/" slide-presentation-draft-pert11.md`
Expected: at least 3 references — `eq-capm.png` (S13), `eq-beta.png` (S14), `eq-market-model.png` (S15) (S13 also lists the two return PNGs). Confirm no other slide was altered.

---

### Task 3: Commit and push (updates PR #1)

**Files:** none changed — git only.

- [ ] **Step 1: Stage script + test + SVGs + deck (NOT the PNGs)**

Run:
```bash
cd "d:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat"
git add rmk-pkk-pert11-efficient-securities-markets/src/python/render_equations.py \
        rmk-pkk-pert11-efficient-securities-markets/src/python/test_render_equations.py \
        rmk-pkk-pert11-efficient-securities-markets/assets/equations/svg/ \
        "rmk-pkk-pert11-efficient-securities-markets/presentation-guidance/slide-presentation-draft-pert11.md" \
        docs/superpowers/specs/2026-06-19-pert11-equation-assets-design.md \
        docs/superpowers/plans/2026-06-19-pert11-equation-assets.md
git status --short
```
Expected: the script, test, 5 SVGs, the deck file, spec, and plan staged. NO `.png` staged (gitignored — confirm none appear).

- [ ] **Step 2: Commit**

```bash
git commit -m "content(pert11): render 5 chapter equations to assets + wire into S13-S15

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

- [ ] **Step 3: Push**

Run: `cd "d:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat" && git push`
Expected: branch `content/pert11-slide-presentation-draft` updated on origin; PR #1 reflects the new files.

---

## Self-Review (plan vs spec)

- **Spec coverage:** 5 equations rendered → Task 1 (`EQUATIONS`, `main`); PNG+SVG output dirs → Task 1 constants + Step 5; verbatim LaTeX w/ `\mathrm` Cov/Var → Task 1 `EQUATIONS`; PNG valid + SVG `<svg` → Task 1 tests; pytest passes → Task 1 Step 4; S13/S14/S15 wiring → Task 2; SVG+script+test committed, PNG gitignored → Task 3 Step 1. All 6 acceptance criteria covered.
- **Placeholder scan:** every step has concrete code/commands; no TBD/TODO. Clean.
- **Type consistency:** `EQUATIONS`, `render_equation(latex, png_path, svg_path, dpi=300)`, `main()`, `PNG_DIR`, `SVG_DIR` referenced identically in the script and the test; the 5 ids match across script, test (`EXPECTED_IDS`), and Task 2 wiring. Consistent.
