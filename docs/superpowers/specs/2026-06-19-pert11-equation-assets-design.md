# Design — Equation Assets for Pert. 11 (Efficient Securities Markets)

**Date:** 2026-06-19
**Status:** Approved (brainstorming) → pending spec review → writing-plans
**Branch:** `content/pert11-slide-presentation-draft` (extends PR #1)

## Purpose

Export the 5 mathematical equations from the Pert. 11 RMK chapter into the
`assets/equations/` folder as image files, so every equation delivered in the
presentation is documented and preserved alongside the other cropped exhibits and
diagrams. Then wire the 3 CAPM-family equations into the slide deck (S13–S15) so the
presentation renders crisp math instead of plain text.

## Source of truth (read-only)

Equations are copied **verbatim** (LaTeX) from `content/A_cornell.md` `@eq` markers.
Never alter a symbol; the LaTeX in the renderer must match these lines exactly:

| id (filename) | LaTeX (verbatim from A_cornell.md) | source line |
|---|---|---|
| `eq-return-expost` | `R_{jt} = \frac{P_{jt} + D_{jt} - P_{j,t-1}}{P_{j,t-1}} = \frac{P_{jt} + D_{jt}}{P_{j,t-1}} - 1` | :60 |
| `eq-return-exante` | `E(R_{jt}) = \frac{E(P_{jt} + D_{jt})}{P_{j,t-1}} - 1` | :64 |
| `eq-capm` | `E(R_{jt}) = R_f(1 - \beta_j) + \beta_j E(R_{Mt})` | :71 |
| `eq-beta` | `\beta_j = \frac{Cov(j, M)}{Var(M)}` | :75 |
| `eq-market-model` | `R_{jt} = \alpha_j + \beta_j R_{Mt} + \varepsilon_{jt}` | :82 |

For matplotlib mathtext rendering, `Cov` and `Var` are wrapped `\mathrm{Cov}` /
`\mathrm{Var}` so they render upright (operator names), not italic identifiers. This
is a rendering nicety, NOT a change to the equation's meaning — the symbols stay the
same.

## Output layout (follows the existing `assets/diagrams/` convention)

- `assets/equations/<id>.png` — 300 DPI, transparent background. **Gitignored**
  (`.gitignore` already has `/assets/equations/*.png`) — regenerable build artifact.
- `assets/equations/svg/<id>.svg` — vector. **Committed** — the durable source-of-record
  (mirrors `assets/diagrams/svg/*.svg`, which are tracked).

Rationale: the repo treats PNGs as regenerable and SVGs as committed source. The
slide deck references the PNGs (consistent with S5 referencing `efficiency-forms.png`);
the committed SVGs preserve the equations in version control and in PR #1.

## Components

### `src/python/render_equations.py` (new, standalone — NOT part of the docx pipeline)
- An ordered mapping `EQUATIONS = {id: latex}` for the 5 equations above (LaTeX
  verbatim; `Cov`/`Var` wrapped `\mathrm{}`).
- `render_equation(latex, png_path, svg_path, dpi=300)` — renders the LaTeX once and
  writes both a 300-DPI transparent PNG and an SVG, using the matplotlib-mathtext
  approach already proven in `latex_to_omml.py:render_eq_png` (extended with
  `format="svg"` for the vector output and `transparent=True`).
- `main()` — creates `assets/equations/` and `assets/equations/svg/`, loops the 5
  equations, writes all 10 files, prints what it wrote.
- Run from the project root (`rmk-pkk-pert11-efficient-securities-markets/`); paths
  resolved relative to the repo root so it is deterministic regardless of CWD.

### `src/python/test_render_equations.py` (new, pytest — follows existing test pattern)
- Runs the renderer into a temp output dir (or the real dirs) and asserts:
  - all 5 PNGs and all 5 SVGs exist and are non-empty;
  - each PNG opens via PIL with width > 0 and height > 0 (valid raster);
  - each SVG file contains the literal `<svg` tag (valid vector);
  - the `EQUATIONS` map has exactly 5 entries with the expected ids.

### Slide-deck wiring — `presentation-guidance/slide-presentation-draft-pert11.md`
- **S13** Visual → `assets/equations/eq-capm.png`; note that `eq-return-expost` and
  `eq-return-exante` are available as supporting visuals for the ex-post/ex-ante setup.
- **S14** Visual → `assets/equations/eq-beta.png`.
- **S15** Visual → `assets/equations/eq-market-model.png`.
- The on-slide equation TEXT stays (acts as caption/fallback); the image becomes the
  crisp focal render. Headlines, scripts, design hints, and Tracker lines unchanged.

## Constraints / non-goals

- Do NOT edit `content/A_cornell.md` or any `input/` file.
- Do NOT alter the docx build pipeline (`build_docx.py`) — this renderer is independent.
- Do NOT change equation symbols; LaTeX traces verbatim to the chapter.
- Do NOT commit the PNGs (gitignored, regenerable); DO commit the SVGs, the script,
  and the test.
- No new third-party dependencies beyond what `requirements.txt` already provides
  (matplotlib + PIL are already used by the pipeline).

## Acceptance criteria

1. `src/python/render_equations.py` exists and, when run, writes 5 PNGs to
   `assets/equations/` and 5 SVGs to `assets/equations/svg/` with the ids above.
2. Each PNG is a valid 300-DPI transparent image (opens via PIL, dims > 0); each SVG
   contains `<svg`.
3. The LaTeX for all 5 equations matches `content/A_cornell.md` verbatim (symbols
   identical; only `Cov`/`Var` wrapped `\mathrm{}` for upright rendering).
4. `pytest src/python/test_render_equations.py` passes.
5. S13/S14/S15 Visual fields reference `eq-capm.png` / `eq-beta.png` /
   `eq-market-model.png` respectively; the rest of those slides is unchanged.
6. SVGs + script + test committed to the branch; PNGs remain gitignored.
