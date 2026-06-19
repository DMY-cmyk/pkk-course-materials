# Pert. 11 Canva Template PDF → Self-Contained HTML Deck Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert `Presentation Template Pert. 11 Canva.pdf` (10 pages) into a single self-contained, offline HTML slide show that is pixel-faithful to the source PDF, by generalizing the existing proven build pipeline.

**Architecture:** Reuse `analysis/build_pert11_html.py` (renders each PDF page to a vector SVG with `text_as_path=True`, namespaces ids, assembles into the existing shell template + controls JS). Generalize it from hardcoded constants to CLI parameters (`--source`/`--output`/`--pages`) while keeping the module constants as backward-compatible 18-page defaults so the existing deck, tests, and fidelity verifier remain green. Then build the 10-page deck and verify fidelity page-by-page via the existing browser-render harness.

**Tech Stack:** Python 3.12, PyMuPDF (`fitz`), Pillow + numpy (fidelity check only), headless Chromium/Edge, pytest. Vanilla HTML/CSS/JS for the deck (no build tooling, no network).

## Global Constraints

- **Fidelity is paramount** — every slide must render visually identical to the source PDF page.
- **Self-contained** — one `.html` file, opens by double-click, works fully offline (no fonts, CDNs, network).
- **No edits to source content; the original PDF is never modified.**
- **The existing `presentasi-pert11.html` (18-page deck) must never be overwritten or regressed** — the no-argument build path must stay byte-identical.
- **Determinism** — re-running any build produces byte-identical output (no timestamps/random ids).
- Render mode is `text_as_path=True` (vector paths, zero font dependency). On-slide text is intentionally not selectable — accepted trade-off, same as the existing deck.
- Output filename for this task: `presentation-template-pert11.html` (project root).
- Source PDF for this task: `Presentation Template Pert. 11 Canva.pdf` (10 pages, 1440×810).

---

### Task 1: Generalize the build script to CLI parameters

**Files:**
- Modify: `analysis/build_pert11_html.py` (functions `load_pages`, `build_html`, `main`)
- Test: `tests/test_build_pert11_html.py` (add new tests; keep all existing tests green)

**Interfaces:**
- Consumes: `analysis/pert11_shell_template.html`, `analysis/pert11_controls.js` (unchanged), `namespace_svg_ids(svg, page_index)` (unchanged).
- Produces:
  - Module constants retained: `SOURCE_PDF: str = "Presentasi PKK Pert. 11 - Kelompok 3.pdf"`, `EXPECTED_PAGES: int = 18`, `OUTPUT: str` (absolute path to `presentasi-pert11.html`).
  - `load_pages(pdf_path: str, expected_pages: int = EXPECTED_PAGES) -> list[str]`
  - `build_html(pdf_path: str, expected_pages: int = EXPECTED_PAGES) -> str`
  - `main(argv: list[str] | None = None) -> None` — parses `--source` (str, default `SOURCE_PDF`), `--output` (str, default `OUTPUT`), `--pages` (int, default `EXPECTED_PAGES`); resolves `--source` and a relative `--output` against project root; writes the deck.

- [ ] **Step 1: Write the failing tests**

Add to the end of `tests/test_build_pert11_html.py`:

```python
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
```

- [ ] **Step 2: Run the new tests to verify they fail**

Run: `python -m pytest tests/test_build_pert11_html.py -k "expected_pages or template_has_10 or main_writes" -v`
Expected: FAIL — `load_pages()`/`build_html()` reject the `expected_pages` keyword (TypeError) and `main()` rejects arguments (TypeError) / wrong page count.

- [ ] **Step 3: Generalize `load_pages` and `build_html`**

In `analysis/build_pert11_html.py`, change the `import` block to add `argparse` and update the two functions' signatures (keep the module constants `SOURCE_PDF`, `EXPECTED_PAGES`, `OUTPUT` exactly as they are):

```python
import argparse
import os
import re
import fitz  # PyMuPDF
```

```python
def load_pages(pdf_path: str, expected_pages: int = EXPECTED_PAGES) -> list[str]:
    """Return one SVG string per PDF page (text as vector paths)."""
    doc = fitz.open(pdf_path)
    try:
        if doc.page_count != expected_pages:
            raise ValueError(
                f"expected {expected_pages} pages, got {doc.page_count}"
            )
        svgs = []
        for i in range(doc.page_count):
            svg = doc[i].get_svg_image(text_as_path=True)
            if not svg or len(svg.strip()) < 1000:
                raise ValueError(f"page {i} produced empty/too-small SVG")
            svgs.append(svg)
        return svgs
    finally:
        doc.close()
```

```python
def build_html(pdf_path: str, expected_pages: int = EXPECTED_PAGES) -> str:
    svgs = load_pages(pdf_path, expected_pages)
    sections = []
    for idx, svg in enumerate(svgs, start=1):
        ns = namespace_svg_ids(svg, idx)
        sections.append(
            f'<section class="slide" data-index="{idx}">{ns}</section>'
        )
    slides = "\n".join(sections)
    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()
    with open(CONTROLS, encoding="utf-8") as f:
        js = f.read()
    html = (tpl.replace("{{SLIDE_COUNT}}", str(len(svgs)))
               .replace("{{CONTROLS_JS}}", js)
               .replace("{{SLIDES}}", slides))
    return html
```

- [ ] **Step 4: Replace `main` with an argparse entry point**

```python
def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Build a self-contained HTML slide deck from a Canva PDF export."
    )
    parser.add_argument("--source", default=SOURCE_PDF,
                        help="source PDF path, relative to project root")
    parser.add_argument("--output", default=OUTPUT,
                        help="output HTML path (absolute, or relative to project root)")
    parser.add_argument("--pages", type=int, default=EXPECTED_PAGES,
                        help="expected page count (build aborts on mismatch)")
    args = parser.parse_args(argv)

    output = args.output if os.path.isabs(args.output) \
        else os.path.join(_ROOT, args.output)
    html = build_html(os.path.join(_ROOT, args.source), args.pages)
    with open(output, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"wrote {output} ({len(html.encode('utf-8'))} bytes)")
```

(`if __name__ == "__main__": main()` at the bottom stays unchanged.)

- [ ] **Step 5: Run the full test file to verify all tests pass**

Run: `python -m pytest tests/test_build_pert11_html.py -v`
Expected: PASS — all existing 18-page tests AND the four new template tests pass.

- [ ] **Step 6: Verify the existing deck still builds byte-identically (no regression)**

Run:
```bash
python analysis/build_pert11_html.py
git status --porcelain "presentasi-pert11.html"
```
Expected: the `git status` line is **empty** (no modification) — the no-argument build reproduces the committed 18-page deck exactly.

- [ ] **Step 7: Commit**

```bash
git add analysis/build_pert11_html.py tests/test_build_pert11_html.py
git commit -m "refactor(pert11-html): parameterize build script via CLI (source/output/pages)"
```

---

### Task 2: Parameterize the fidelity verifier

**Files:**
- Modify: `analysis/verify_pert11_fidelity.py` (function `main`)

**Interfaces:**
- Consumes: `b.SOURCE_PDF`, `b.EXPECTED_PAGES`, `b.load_pages(pdf_path, expected_pages)` from Task 1.
- Produces: `main(argv: list[str] | None = None) -> None` — parses `--source` (default `b.SOURCE_PDF`) and `--pages` (int, default `b.EXPECTED_PAGES`); renders/compares that PDF vs. its SVGs page-by-page; exits 0 on PASS, 1 on REVIEW NEEDED, 2 if no browser.

- [ ] **Step 1: Update the verifier's `main` to accept CLI args**

In `analysis/verify_pert11_fidelity.py`, add `import argparse` at the top, then change the start of `main()` from the argless body to:

```python
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Page-by-page fidelity check: source PDF vs. deck SVGs (browser render)."
    )
    parser.add_argument("--source", default=b.SOURCE_PDF,
                        help="source PDF path, relative to project root")
    parser.add_argument("--pages", type=int, default=b.EXPECTED_PAGES,
                        help="expected page count")
    args = parser.parse_args(argv)

    os.makedirs(OUT, exist_ok=True)
    browser = find_browser()
    if not browser:
        print("NO BROWSER FOUND - install Chrome or Edge to run the fidelity check")
        sys.exit(2)
    print("browser:", browser)
    pdf_path = os.path.join(ROOT, args.source)
    doc = fitz.open(pdf_path)
    svgs = b.load_pages(pdf_path, args.pages)
```

The rest of `main()` (the per-page render/compare loop, worst-diff print, `RESULT:` line, and `sys.exit`) is unchanged. The `if __name__ == "__main__": main()` line stays.

- [ ] **Step 2: Smoke-test the verifier's argument parsing (no full run yet)**

Run: `python -m analysis.verify_pert11_fidelity --help`
Expected: usage text listing `--source` and `--pages` (exit 0). This confirms argparse wiring without needing the browser.

- [ ] **Step 3: Commit**

```bash
git add analysis/verify_pert11_fidelity.py
git commit -m "refactor(pert11-fidelity): accept --source/--pages so any deck can be verified"
```

---

### Task 3: Build the template deck and verify fidelity

**Files:**
- Create: `presentation-template-pert11.html` (project root — the deliverable)

**Interfaces:**
- Consumes: generalized `build_pert11_html.py` (Task 1) and `verify_pert11_fidelity.py` (Task 2).
- Produces: the deliverable HTML file + page-by-page fidelity evidence surfaced to the user.

- [ ] **Step 1: Build the 10-page template deck**

Run:
```bash
python analysis/build_pert11_html.py \
  --source "Presentation Template Pert. 11 Canva.pdf" \
  --output "presentation-template-pert11.html" \
  --pages 10
```
Expected: prints `wrote .../presentation-template-pert11.html (<N> bytes)` with no error.

- [ ] **Step 2: Sanity-check the deliverable (count + self-contained)**

Run:
```bash
python -c "import re,io; h=open('presentation-template-pert11.html',encoding='utf-8').read(); print('slides=',h.count('class=\"slide\"')); print('counter_total=','/ 10' in h); ns=re.sub(r'\sxmlns(?::\w+)?=\"[^\"]*\"','',h); print('no_external=', not any(x in ns for x in('http://','https://','<link','@import','src=\"//')))"
```
Expected: `slides= 10`, `counter_total= True`, `no_external= True`.

- [ ] **Step 3: Run the page-by-page fidelity verification**

Run:
```bash
python -m analysis.verify_pert11_fidelity \
  --source "Presentation Template Pert. 11 Canva.pdf" --pages 10
```
Expected: ten `page NN: mean_abs_diff=… pct>20=… OK` lines and a final `RESULT: PASS` (exit 0). If the result is `REVIEW NEEDED`, inspect the flagged page's `analysis/_pert11_fidelity/pdf_NN.png` vs. `chrome_NN.png`, diagnose with systematic-debugging, and do NOT claim completion.

> Note: if no Chromium/Edge browser is installed the verifier exits 2 ("NO BROWSER FOUND"). In that case, report that fidelity could not be auto-verified and ask the user to open `presentation-template-pert11.html` and eyeball it against the PDF before sign-off — do not silently skip.

- [ ] **Step 4: Confirm no regression to the existing deck**

Run: `git status --porcelain "presentasi-pert11.html"`
Expected: empty output (the 18-page deck file is untouched by this task).

- [ ] **Step 5: Commit the deliverable**

```bash
git add "presentation-template-pert11.html"
git commit -m "build(pert11-template-html): faithful 10-page Canva template deck"
```

---

## Self-Review

**Spec coverage:**
- Faithful conversion of the 10-page template PDF → Task 3 build + `text_as_path=True` (carried unchanged in Task 1). ✓
- Self-contained / offline → existing template + Task 3 Step 2 check. ✓
- Source PDF never modified → no task writes to the source. ✓
- Existing `presentasi-pert11.html` never overwritten/regressed → Task 1 Step 6 + Task 3 Step 4 byte-identity checks; module-constant defaults preserved. ✓
- Generalize one script via CLI → Task 1. ✓
- Output named `presentation-template-pert11.html` → Task 3 Step 1. ✓
- Page-by-page fidelity verification → Task 3 Step 3. ✓
- Determinism → existing build logic carried verbatim; covered by existing `test_build_html_deterministic`. ✓

**Placeholder scan:** No TBD/TODO; every code step shows complete code; every command shows expected output. ✓

**Type consistency:** `load_pages(pdf_path, expected_pages=EXPECTED_PAGES)` and `build_html(pdf_path, expected_pages=EXPECTED_PAGES)` defined in Task 1 and consumed with matching keyword/positional usage in Tasks 1–3; verifier calls `b.load_pages(pdf_path, args.pages)`; `main(argv)` signature consistent across build script and verifier. ✓
