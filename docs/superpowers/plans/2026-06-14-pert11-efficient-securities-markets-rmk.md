# RMK Pertemuan 11 — Efficient Securities Markets — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce the graded group `.docx` `output/01079_Kelompok 3_RMK Pert. 11.docx` — a Cornell-Notes RMK of Scott, *Financial Accounting Theory* (7th ed.), Ch. 4 (Efficient Securities Markets) — by cloning and adapting the shipped pert10 pipeline.

**Architecture:** A reproducible Rust-first pipeline with three documented Python exceptions (PyMuPDF text/crop, python-docx assembly), cloned from `rmk-pkk-pert10-statement-of-cash-flows`. New vs pert10: a native-Word equation step (LaTeX→MathML→OMML, with a matplotlib-PNG fallback) for Eq 4.1–4.4, and a group identity block. Content is authored in `content/*.md` (the `@cue`/`@notes` Cornell convention) then run through a Humanize → Simplify language pass.

**Tech Stack:** Rust (`lopdf`, `clap`, `serde`, `resvg`); Python 3.12 (`PyMuPDF`, `Pillow`, `python-docx`, `latex2mathml`, `lxml`, `matplotlib`); Word OMML via Office `MML2OMML.XSL`.

---

## Source Facts (confirmed by probing the inputs)

- Chapter PDF: `Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf` (repo root) — **33 pages, 0 embedded raster images** on every page (figures/tables are vector/text → crop-by-rectangle).
- Required visuals & rough locations: **Figure 4.1** (chapter organization) ≈ p.1; **Table 4.1** (football forecasting) ≈ p.5; **Theory in Practice 4.1** box (Malkiel/dartboard) ≈ p.6; **Figure 4.2** (role of financial reporting) ≈ p.22. Exact rectangles tuned in Task 3.
- Equations 4.1–4.4 cluster in §4.5 (≈ pp. 8–17).
- The five source files (chapter, rules PNG, Cornell pedoman PDF, syllabus, group photo) already exist in the repo (root + `03-Course-Admin/`).

## File Structure (new project: `rmk-pkk-pert11-efficient-securities-markets/`)

| Path | Responsibility |
|------|----------------|
| `CLAUDE.md` | Governing rules verbatim; Rust→Python exception log; group identity |
| `README.md` | Deterministic run order |
| `Cargo.toml` + `src/rust/pdf_probe/`, `src/rust/visual_gen/` | Rust stages (probe, SVG→PNG) |
| `requirements.txt` | Python deps (adds `latex2mathml`, `matplotlib`) |
| `input/chapter/`, `input/syllabus/`, `input/rules/` | Read-only sources |
| `extraction/` | `chapter-range.json`, `page-map.json`, `text/*.md`, `verification-report.md` |
| `assets/exhibits/` | Cropped Fig 4.1, Table 4.1, ToP 4.1 box, Fig 4.2 |
| `assets/diagrams/svg/` + `assets/diagrams/` | Authored concept SVGs → PNG |
| `assets/equations/` | PNG fallbacks for any equation whose OMML fails |
| `content/00_identitas.md … F_referensi.md` | Document content |
| `src/python/extract_text.py`, `crop_exhibits.py`, `latex_to_omml.py`, `build_docx.py` | Python stages |
| `src/python/test_*.py` | Unit tests |
| `output/01079_Kelompok 3_RMK Pert. 11.docx` | Deliverable |

---

## Task 0: Scaffold the pert11 project from pert10

**Files:**
- Create: `rmk-pkk-pert11-efficient-securities-markets/` (clone of pert10, artifacts cleaned)
- Modify: its `CLAUDE.md`, `README.md`, `Cargo.toml` paths, `input/*`

- [ ] **Step 1: Clone the pert10 tree, excluding regenerable artifacts**

Run (from repo root, Git Bash):
```bash
SRC="rmk-pkk-pert10-statement-of-cash-flows"
DST="rmk-pkk-pert11-efficient-securities-markets"
rsync -a --exclude target --exclude build --exclude output \
  --exclude 'assets/exhibits/*' --exclude 'assets/diagrams/*.png' \
  --exclude 'assets/diagrams/svg/*' --exclude 'extraction' \
  --exclude '__pycache__' --exclude '.pytest_cache' --exclude 'Cargo.lock' \
  "$SRC/" "$DST/"
mkdir -p "$DST/input/chapter" "$DST/input/syllabus" "$DST/input/rules" \
  "$DST/extraction/text" "$DST/assets/exhibits/tmp" "$DST/assets/diagrams/svg" \
  "$DST/assets/equations" "$DST/build" "$DST/output"
```
(If `rsync` is unavailable on this Windows box, use `cp -r` then `rm -rf` the excluded dirs.)

- [ ] **Step 2: Copy the five read-only sources into `input/`**

```bash
DST="rmk-pkk-pert11-efficient-securities-markets"
cp "Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf" "$DST/input/chapter/"
cp "03-Course-Admin/Silabus_Pelaporan Keuangan Korporat_25-26.pdf" "$DST/input/syllabus/"
cp "Ketentuan Pembuatan RMK.png" "$DST/input/rules/"
cp "Pedoman Penyusunan Resume Cornell Notes.pdf" "$DST/input/rules/"
cp "Grup 3 PKK Pasca UTS.jpeg" "$DST/input/rules/"
```

- [ ] **Step 3: Empty the pert10 content files** so we author fresh (keep the filenames):

```bash
DST="rmk-pkk-pert11-efficient-securities-markets"
for f in A_cornell B_ringkasan C_refleksi D_kesimpulan E_review F_referensi; do
  : > "$DST/content/$f.md"
done
```
Leave `content/00_identitas.md` to be rewritten in Task 8.

- [ ] **Step 4: Rewrite `CLAUDE.md`** — change Project Purpose to group/Pert. 11/Scott Ch. 4, set the output filename to `01079_Kelompok 3_RMK Pert. 11.docx`, update the Source-of-Truth chapter path, and add a 4th exception entry for `latex_to_omml.py`. Keep the Governing Rules block (Ketentuan + Pedoman + Rubrik) verbatim. Add the group identity table from the spec (§3).

The new exception entry to append to the Rust→Python Fallback Log:
```markdown
### Exception 4: `src/python/latex_to_omml.py` + equation step in `build_docx.py` — uses latex2mathml + lxml (+ matplotlib fallback)

**Justification:** Word equations are OMML (Office Math Markup). There is no Rust crate that
produces Word-native OMML; the reproducible route is LaTeX → MathML (`latex2mathml`) → OMML via
Microsoft's shipped `MML2OMML.XSL` stylesheet (applied with `lxml`). If the stylesheet is absent or
a transform fails, that single equation falls back to a 300-DPI `matplotlib` mathtext PNG. Both are
Python-only; no Rust equivalent exists.
```

- [ ] **Step 5: Update `Cargo.toml` member crates' default PDF paths**

In `src/rust/pdf_probe/src/main.rs`, change the two defaults:
```rust
    #[arg(long, default_value = "input/chapter/Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf")]
    pdf: String,
```
and the `print_pages` default to the chapter's authoritative print range (read from the PDF footer in Task 1; leave the pert10 default string in place until Task 1 sets the real range). Leave `visual_gen` unchanged.

- [ ] **Step 6: Update `README.md`** — title "RMK Pertemuan 11 — Efficient Securities Markets", author line "Kelompok 3", source "Scott, *Financial Accounting Theory* (7th ed.), Ch. 4", output filename, and the same Deterministic Run Order plus the new equation note. Add `latex2mathml` and `matplotlib` to the prerequisites.

- [ ] **Step 7: Add Python deps to `requirements.txt`**
```
python-docx==1.2.0
PyMuPDF
Pillow
latex2mathml
matplotlib
lxml
```

- [ ] **Step 8: Install deps and commit the scaffold**
```bash
cd rmk-pkk-pert11-efficient-securities-markets
pip install -r requirements.txt
git add -A && git commit -m "scaffold(rmk-pert11): clone pert10 pipeline, swap Scott Ch.4 sources + group identity"
```

---

## Task 1: Adapt & run the Rust PDF probe

**Files:**
- Modify: `src/rust/pdf_probe/src/main.rs` (defaults only; logic unchanged)
- Test: `src/rust/pdf_probe/src/main.rs` (existing `#[cfg(test)]` unit tests)

- [ ] **Step 1: Confirm the existing unit tests still pass**

Run: `cargo test -p pdf_probe`
Expected: PASS (`print_range_inclusive`, `single_page_range`).

- [ ] **Step 2: Read the chapter's printed page range** from the PDF footer (first & last body pages) to set `print_pages`. Quick check:
```bash
python -c "import fitz;d=fitz.open('input/chapter/Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf');print(repr(d[0].get_text()[:120]));print(repr(d[-1].get_text()[-200:]))"
```
Set the `print_pages` default in `main.rs` to the observed range (e.g. `"105-137"` — use the actual printed numbers).

- [ ] **Step 3: Run the probe**

Run: `cargo run --release -p pdf_probe`
Expected stdout: `pdf_probe: 33 pages, print range <X-Y>, 0 total image XObjects → extraction/chapter-range.json | extraction/verification-report.md`

- [ ] **Step 4: Verify outputs exist and report 33 pages**

Run: `cat extraction/chapter-range.json`
Expected: `{ "start_page": 1, "end_page": 33, "print_pages": "<X-Y>" }`

- [ ] **Step 5: Commit**
```bash
git add src/rust/pdf_probe/src/main.rs extraction/chapter-range.json extraction/verification-report.md
git commit -m "feat(rmk-pert11): probe Scott Ch.4 PDF (33 pages, print range)"
```

---

## Task 2: Adapt & run text extraction (Python — PyMuPDF exception)

**Files:**
- Modify: `src/python/extract_text.py` (PDF path + `SECTIONS` list)
- Test: `src/python/test_extract_text.py`

- [ ] **Step 1: Update the PDF path** in `extract_text.py` (the `pdf_path = os.path.join(...)` line) to `"Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf"`.

- [ ] **Step 2: Survey the real headings.** Dump the chapter text once to discover exact standalone heading lines:
```bash
python -c "import fitz;d=fitz.open('input/chapter/Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf');[print(f'--p{p+1}--');print(d[p].get_text()) for p in range(33)]" > /tmp/ch4_dump.txt
grep -nE '^\s*4\.[0-9]' /tmp/ch4_dump.txt | head -40
```
Record the exact heading strings as they appear on their own line (e.g. `4.2 The Meaning of Efficiency`, `4.5 A Model of Cost of Capital`, `4.6 Information Asymmetry`, etc.).

- [ ] **Step 3: Replace the `SECTIONS` list** with Scott Ch. 4's headings → slugs, in source order, e.g.:
```python
SECTIONS = [
    ("4.1 Overview", "01_overview"),
    ("4.2 The Meaning of Efficiency", "02_meaning"),
    ("4.3 Implications of Efficiency for Financial Reporting", "03_reporting"),
    ("4.4 The Informativeness of Price", "04_informativeness"),
    ("4.5 A Model of Cost of Capital", "05_capm"),
    ("4.6 Information Asymmetry", "06_asymmetry"),
    ("4.7 The Social Significance of Securities Markets That Work Well", "07_social"),
    ("4.8 Conclusions", "08_conclusions"),
]
```
Adjust each string to match the survey exactly (capitalization/spacing as printed).

- [ ] **Step 4: Run extraction**

Run: `python src/python/extract_text.py`
Expected stdout: `wrote N segment files, page-map.json, verification-report.md (total images: 0)` with N ≈ 9.

- [ ] **Step 5: Spot-check the segmentation**

Run: `head -5 extraction/text/05_capm.md && echo '---' && cat extraction/page-map.json`
Expected: `05_capm.md` begins at the §4.5 heading; page-map maps slugs → page lists.

- [ ] **Step 6: Run the extractor unit tests** (update any pert10-specific heading assertions in `test_extract_text.py` to the Ch.4 `segment()` cases first if present)

Run: `python -m pytest src/python/test_extract_text.py -q`
Expected: PASS.

- [ ] **Step 7: Commit**
```bash
git add src/python/extract_text.py src/python/test_extract_text.py extraction/text extraction/page-map.json extraction/verification-report.md
git commit -m "feat(rmk-pert11): extract & segment Scott Ch.4 text (PyMuPDF)"
```

---

## Task 3: Crop the four chapter visuals (Python — PyMuPDF+PIL exception)

**Files:**
- Modify: `src/python/crop_exhibits.py` (PDF path, `SURVEY_PAGES`, `EXHIBITS`)
- Create: `assets/exhibits/fig-4-1.png`, `table-4-1.png`, `tip-4-1.png`, `fig-4-2.png`

- [ ] **Step 1: Point the script at the Ch.4 PDF** (`PDF = os.path.join(... "Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf")`) and set `SURVEY_PAGES = [1, 5, 6, 22]` (plus neighbours 2, 7, 23 in case a visual spills over).

- [ ] **Step 2: Render survey pages**

Run: `python src/python/crop_exhibits.py --pages`
Expected: `assets/exhibits/tmp/page-01.png` etc. written.

- [ ] **Step 3: Find tight rectangles** for each visual using text-block bounds (figures here are vector/text, not raster):
```bash
python - <<'PY'
import fitz
d=fitz.open('input/chapter/Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf')
for p in (1,5,6,22):
    print(f"=== page {p} ===")
    for b in d[p-1].get_text("blocks"):
        x0,y0,x1,y1,txt,*_ = b
        print(round(y0),round(y1),repr(txt[:60]))
PY
```
Use the printed y-bounds (caption line through the last figure/table row) to set each `fitz.Rect(x0, y0, x1, y1)`.

- [ ] **Step 4: Replace the `EXHIBITS` dict** with the four targets (tune coordinates from Step 3; stitch across pages only if a visual spills over):
```python
EXHIBITS = {
    "fig-4-1":  [(1,  fitz.Rect(48, 0, 550, 0))],   # Figure 4.1 — chapter organization
    "table-4-1":[(5,  fitz.Rect(48, 0, 550, 0))],   # Table 4.1 — football forecasting
    "tip-4-1":  [(6,  fitz.Rect(48, 0, 550, 0))],   # Theory in Practice 4.1 box
    "fig-4-2":  [(22, fitz.Rect(48, 0, 550, 0))],   # Figure 4.2 — role of financial reporting
}
```
(Replace the `0` y-values with the real bounds.)

- [ ] **Step 5: Crop**

Run: `python src/python/crop_exhibits.py`
Expected: four PNGs in `assets/exhibits/`, each printed with its WxH.

- [ ] **Step 6: Eyeball each crop** — open the four PNGs; confirm no page header/footer bleed and nothing clipped. Re-tune Step 4 and re-run if needed.

- [ ] **Step 7: Commit**
```bash
git add src/python/crop_exhibits.py assets/exhibits/fig-4-1.png assets/exhibits/table-4-1.png assets/exhibits/tip-4-1.png assets/exhibits/fig-4-2.png
git commit -m "feat(rmk-pert11): crop Fig 4.1, Table 4.1, ToP 4.1 box, Fig 4.2"
```

---

## Task 4: Author two concept diagrams (Rust visual_gen)

**Files:**
- Create: `assets/diagrams/svg/efficiency-forms.svg`, `assets/diagrams/svg/adverse-selection.svg`
- Output: `assets/diagrams/efficiency-forms.png`, `adverse-selection.png`

- [ ] **Step 1: Author `efficiency-forms.svg`** — a three-rung ladder (weak ⊂ semi-strong ⊂ strong) at **1712 px width** (14.5 cm @ 300 DPI), labelling what information set each form reflects. Use `font-family="Calibri"`. Match the structure of an existing pert10 SVG (`viewBox="0 0 1712 H"`, `width="1712"`).

- [ ] **Step 2: Author `adverse-selection.svg`** — a small flow: inside information → information asymmetry → adverse selection (lemons) → market thins, with "full disclosure" as the mitigating arrow. Same 1712 px width.

- [ ] **Step 3: Confirm the visual_gen unit test still passes**

Run: `cargo test -p visual_gen`
Expected: PASS (`rasterizes_simple_svg`).

- [ ] **Step 4: Rasterize**

Run: `cargo run --release -p visual_gen`
Expected: `rendered assets/diagrams/efficiency-forms.png (1712x…)` and likewise for adverse-selection; `done: 2 diagrams`.

- [ ] **Step 5: Commit**
```bash
git add assets/diagrams/svg/*.svg assets/diagrams/efficiency-forms.png assets/diagrams/adverse-selection.png
git commit -m "feat(rmk-pert11): add efficiency-forms + adverse-selection concept diagrams"
```

---

## Task 5: Equation → OMML module (NEW — TDD)

**Files:**
- Create: `src/python/latex_to_omml.py`
- Test: `src/python/test_latex_to_omml.py`

- [ ] **Step 1: Write the failing test**
```python
# src/python/test_latex_to_omml.py
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
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python -m pytest src/python/test_latex_to_omml.py -q`
Expected: FAIL with `ModuleNotFoundError: latex_to_omml`.

- [ ] **Step 3: Implement `latex_to_omml.py`**
```python
"""latex_to_omml.py — LaTeX → Word OMML (native equation) with a PNG fallback.
Python exception #4: no Rust crate emits Word OMML. Route: latex2mathml → MathML →
OMML via Microsoft's shipped MML2OMML.XSL (lxml). Fallback: 300-DPI matplotlib PNG.
"""
import glob
import latex2mathml.converter
from lxml import etree

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
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python -m pytest src/python/test_latex_to_omml.py -q`
Expected: PASS (both tests).

- [ ] **Step 5: Commit**
```bash
git add src/python/latex_to_omml.py src/python/test_latex_to_omml.py
git commit -m "feat(rmk-pert11): LaTeX→OMML equation module with PNG fallback (TDD)"
```

---

## Task 6: Wire equations + group identity into the docx builder

**Files:**
- Modify: `src/python/build_docx.py`
- Test: `src/python/test_build_docx.py`

- [ ] **Step 1: Write the failing test** for the new `@eq` block parser
Add to `test_build_docx.py`:
```python
def test_parse_blocks_emits_eq():
    md = "@eq \\beta_j = \\frac{Cov(R_j,R_M)}{Var(R_M)}\n"
    blocks = parse_blocks(md)
    assert blocks[0][0] == "eq"
    assert blocks[0][1].startswith("\\beta_j")
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python -m pytest src/python/test_build_docx.py::test_parse_blocks_emits_eq -q`
Expected: FAIL (no `eq` kind yet).

- [ ] **Step 3: Add `@eq` handling to `parse_blocks`** — insert before the final `else:` branch:
```python
        elif stripped.startswith("@eq "):
            flush()
            blocks.append(("eq", stripped[4:].strip()))
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python -m pytest src/python/test_build_docx.py::test_parse_blocks_emits_eq -q`
Expected: PASS.

- [ ] **Step 5: Add the equation renderer and group identity.** In `build_docx.py`:

Replace the identity constants:
```python
FONT = "Calibri"
OUT_NAME = "01079_Kelompok 3_RMK Pert. 11.docx"
```
(Remove the single-student `STUDENT`/`NIM` constants — the group block now lives entirely in `content/00_identitas.md`, which the existing identity loop already renders line-by-line.)

Add the equation paragraph helper (uses Task 5 module):
```python
import os as _os
from latex_to_omml import latex_to_omath, render_eq_png

_EQ_COUNTER = {"n": 0}

def add_equation(doc, latex, root):
    """Append a centered native Word equation; fall back to a PNG on failure."""
    omath = latex_to_omath(latex)
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.paragraph_format.space_before = Pt(4)
    para.paragraph_format.space_after = Pt(4)
    if omath is not None:
        para._p.append(omath)          # native OMML equation
        return para
    _EQ_COUNTER["n"] += 1              # fallback: high-DPI PNG
    png = _os.path.join(root, "assets", "equations", f"eq-{_EQ_COUNTER['n']}.png")
    _os.makedirs(_os.path.dirname(png), exist_ok=True)
    render_eq_png(latex, png)
    run = para.add_run()
    run.add_picture(png, width=Cm(10))
    return para
```

Wire it into the block loop in `build()` (add a branch alongside `image`/`table`):
```python
            elif kind == "eq":
                add_equation(doc, payload, root)
```

- [ ] **Step 6: Run the full builder unit-test suite**

Run: `python -m pytest src/python/test_build_docx.py -q`
Expected: PASS (all existing tests + the new `eq` test).

- [ ] **Step 7: Commit**
```bash
git add src/python/build_docx.py src/python/test_build_docx.py
git commit -m "feat(rmk-pert11): group identity + native @eq equations in docx builder"
```

---

## Task 7: Author Bagian A — Cornell Notes (the substantive core)

> Use a content-authoring subagent (subagent-driven-development). Voice = the shipped pert10 register: graduate-depth, natural Bahasa Indonesia, every English term glossed in *italic* with a parenthetical Indonesian gloss on first use, each `@notes` ending with a `(Scott, 2015)` style citation. Source = `extraction/text/*.md` ONLY; never fabricate.

**Files:**
- Modify: `content/A_cornell.md`

- [ ] **Step 1: Write Section A** as `@cue` / `@notes` pairs walking Ch. 4 in source order, covering every item in the spec §3 map. One `@cue` (a question/key term) + one `@notes` (the graduate-level answer) per concept. Begin the file with `## Bagian A — Cornell Notes`. Required coverage, in order:
  1. 4.1 — rational investors → prices "fully reflect" info; *information content* not *form/location* → full disclosure.
  2. 4.2 — semi-strong (Fama 1970) vs strong; four points (public-info-relative → insider trading; relative not omniscient → 2007–08; fair game / CAPM benchmark; *random walk*); informed investors + arbitrage.
  3. 4.2.2 — Beaver football example (embed **Table 4.1**), independence, forecasters→investors analogy; **Theory in Practice 4.1** (embed `tip-4-1.png`): Malkiel, dartboard, Reg FD.
  4. 4.3 — Beaver (1973): no-cash-flow-effect policy choices don't move price; efficiency ↔ full disclosure; naïve investor price-protected; accountants compete; decision usefulness.
  5. 4.4 — Grossman (1976) inconsistency; noise traders + rational expectations → partially informative; voluntary disclosure, conservatism as signal, MD&A.
  6. 4.5 — CAPM & market model: insert **Eq 4.1–4.4** via `@eq` with variable definitions beneath each; three uses of the market model; CAPM critique (estimation risk, common knowledge, transaction costs, rationality; 2007–08).
  7. 4.6 — adverse selection vs moral hazard; estimation risk; lemons/used-car (Akerlof 1970), pooling; JLT (2011) blackout study.
  8. 4.6.2 — fundamental value; embed **Figure 4.2** (`fig-4-2.png`); SOX 2002; Maffett 2012; Enron/WorldCom.
  9. 4.7 — capital allocation; lemons → under/over-investment; depth vs thinness; Wurgler 2000, FHKP 2009, BHV 2009; carrots vs sticks.
  10. 4.8 — conclusions.

Embed visuals/equations with the existing markdown conventions, e.g.:
```markdown
@cue Bagaimana harga "fully reflect" informasi: pelajaran dari ramalan sepak bola Beaver?
@notes ... penjelasan ...

![Table 4.1 — Hasil Ramalan Sepak Bola (konsensus mengungguli tiap individu) | Sumber: Scott (2015)](../assets/exhibits/table-4-1.png)

@cue Bagaimana CAPM menautkan risiko dengan biaya modal?
@notes Model pasar (*market model*) menautkan return ke return pasar:

@eq R_{jt} = \alpha_j + \beta_j R_{Mt} + \varepsilon_{jt}

dengan *R_{jt}* = return saham j pada periode t; *β_j* = *beta* (ukuran risiko sistematis, yaitu kepekaan saham terhadap gerak pasar); ... (Scott, 2015).
```
Transcribe Eq 4.1–4.4 exactly from §4.5 of the PDF (do not invent forms).

- [ ] **Step 2: Verify the build consumes Section A without error**

Run: `python src/python/build_docx.py`
Expected: `Saved: …/output/01079_Kelompok 3_RMK Pert. 11.docx` (no traceback; equations + images resolve).

- [ ] **Step 3: Coverage self-check** — confirm every spec §3 bullet (4.1–4.8, Table 4.1, ToP 4.1, Eq 4.1–4.4, Fig 4.2) appears:
```bash
grep -cE '@cue' content/A_cornell.md          # expect ~18-25 cue/notes pairs
grep -E 'table-4-1|tip-4-1|fig-4-2|@eq' content/A_cornell.md
```
Expected: all four asset references present; ≥4 `@eq` lines.

- [ ] **Step 4: Commit**
```bash
git add content/A_cornell.md && git commit -m "content(rmk-pert11): author Bagian A Cornell Notes (Scott Ch.4 full coverage)"
```

---

## Task 8: Author identity + Bagian B–F

**Files:**
- Modify: `content/00_identitas.md`, `B_ringkasan.md`, `C_refleksi.md`, `D_kesimpulan.md`, `E_review.md`, `F_referensi.md`

- [ ] **Step 1: Write `00_identitas.md`** — group block (first line bold-rendered title). Read Dosen & tanggal from the syllabus; use a clearly-marked `[—]` placeholder if absent:
```
RINGKASAN MATERI KULIAH (RMK) — PERTEMUAN 11
Mata Kuliah: Pelaporan Keuangan Korporat (MNK202)
Topik: Efficient Securities Markets
Dosen Pengampu: [— baca dari silabus]
Kelompok 3 — Anggota: Odisiana Manek (122501041), Efri Nurmalinda (122501049), Prasetya Adhi Surya Gumilang (122501068), Dzaki Muhammad Yusfian (122501079), Adinda Putri Dewi (122501086), Kunthi Talibrata (122501097)
Program Studi: Pascasarjana — Magister Akuntansi / Magister Manajemen, STIE YKPN
Tanggal: [—] (Pertemuan 11, sesuai jadwal silabus)
Sumber: Scott, W. R. (2015), Financial Accounting Theory (7th ed.), Bab 4 — Efficient Securities Markets
```

- [ ] **Step 2: Write `B_ringkasan.md`** — `## Bagian B — Ringkasan`, 1–2 paragraphs in own words, ≤ 15–20% of source length, capturing the chapter's spine (efficiency → information content/full disclosure → CAPM cost of capital → information asymmetry → social significance).

- [ ] **Step 3: Write `C_refleksi.md`** — `## Bagian C — Refleksi dan Analisis Akademik` with five `### ` sub-questions (understanding; importance; real-world application; links to other courses — investment/finance/audit; strengths **and** limitations). Analytical, graduate-level — name concrete limitations (e.g. CAPM common-knowledge/estimation-risk assumptions; efficiency-vs-2007–08; partial informativeness).

- [ ] **Step 4: Write `D_kesimpulan.md`** — `## Bagian D — Kesimpulan Akademik`, 150–250 words: core, benefit, practical implication, contribution to the field.

- [ ] **Step 5: Write `E_review.md`** — `## Bagian E — Review Mandiri (Active Recall)`, ≥ 5 bulleted self-test questions each with an italic `*Jawaban: …*`.

- [ ] **Step 6: Write `F_referensi.md`** — `## Bagian F — Referensi Akademik`, APA-7, hanging-indent rendered. Minimum:
```
- Scott, W. R. (2015). *Financial accounting theory* (7th ed.). Pearson Education Canada. [Bab 4 — *Efficient Securities Markets*].
- Silabus Pelaporan Keuangan Korporat (MNK202), Pascasarjana STIE YKPN Yogyakarta, Tahun Ajaran 2025/2026.
```
Include only works actually cited in the body (Fama 1970; Beaver 1973; Grossman 1976; Akerlof 1970; JLT 2011; Maffett 2012; Wurgler 2000; etc.) — APA-7 each.

- [ ] **Step 7: Build and commit**
```bash
python src/python/build_docx.py
git add content/00_identitas.md content/B_ringkasan.md content/C_refleksi.md content/D_kesimpulan.md content/E_review.md content/F_referensi.md
git commit -m "content(rmk-pert11): author identity + Bagian B–F"
```

---

## Task 9: Humanize → Simplify language pass

> Open with the `/content-research-writer` skill. Apply to ALL of `content/*.md`. Voice/clarity only — never alter facts, figures, citations, equations, or asset references.

**Files:**
- Modify: all `content/*.md`

- [ ] **Step 1: Humanize** every section — vary sentence rhythm; remove AI tells (over-hedging, mechanical "Pertama/Kedua/Kesimpulannya" scaffolding, list-like prose, prompt-restating); add genuine analytical connective tissue between ideas.

- [ ] **Step 2: Simplify** — shorten convoluted sentences; keep each technical term but ensure its first-use plain gloss is present and clear; ensure first-pass comprehension. Simple yet professional.

- [ ] **Step 3: Integrity diff-check** — confirm no `@eq`, `![...]`, citation, or number changed:
```bash
git diff --stat content/
grep -E 'table-4-1|tip-4-1|fig-4-2|@eq' content/A_cornell.md   # must still be present
```
Expected: asset/equation markers unchanged; only prose differs.

- [ ] **Step 4: Rebuild and commit**
```bash
python src/python/build_docx.py
git add content/ && git commit -m "style(rmk-pert11): humanize → simplify all sections"
```

---

## Task 10: Quality gate, page count, and final verification

**Files:**
- Read-only verification; may touch `content/*` if a gate fails.

- [ ] **Step 1: Run the full pipeline end-to-end** (reproducibility check) from the project root:
```bash
cargo run --release -p pdf_probe
python src/python/extract_text.py
python src/python/crop_exhibits.py
cargo run --release -p visual_gen
python src/python/build_docx.py
```
Expected: each stage prints success; final `Saved: …01079_Kelompok 3_RMK Pert. 11.docx`.

- [ ] **Step 2: Verify page count ≥ 8.** Convert to PDF and count (LibreOffice headless), or inspect in Word:
```bash
soffice --headless --convert-to pdf --outdir build "output/01079_Kelompok 3_RMK Pert. 11.docx"
python -c "import fitz;print('PAGES:', len(fitz.open('build/01079_Kelompok 3_RMK Pert. 11.pdf')))"
```
Expected: `PAGES: >= 8`. If short, deepen Section A/C (do NOT pad).

- [ ] **Step 3: Verify equations rendered natively.** Unzip the docx and check for OMML:
```bash
python -c "import zipfile;d=zipfile.ZipFile('output/01079_Kelompok 3_RMK Pert. 11.docx');x=d.read('word/document.xml').decode();print('oMath count:', x.count('</m:oMath>'));print('eq PNG fallbacks:', __import__('glob').glob('assets/equations/*.png'))"
```
Expected: `oMath count: >= 4` (native), OR documented PNG fallbacks listed (log any fallback in `CLAUDE.md`).

- [ ] **Step 4: Run the §9 quality-gate checklist** (from the spec) against the built doc:
  - A4 · 1.5 spacing · Calibri 12 · ≥ 8 pages · `.docx` ✓
  - Kelompok 3 identity block (6 members + NIMs) ✓
  - Cornell A–F all present ✓
  - Every §3 coverage concept present + glossed ✓
  - Fig 4.1, Table 4.1, ToP 4.1, Fig 4.2 cropped/captioned/placed; Eq 4.1–4.4 typeset with variables defined; no margin overflow ✓
  - Python exceptions justified in `CLAUDE.md` ✓
  - Summary 15–20%; conclusion 150–250 words; APA-7 complete ✓
  - Filename exact ✓

- [ ] **Step 5: Final commit + copy deliverable to repo root** (matching the prior-deliverable convention if desired)
```bash
git add -A && git commit -m "build(rmk-pert11): final RMK Pert. 11 docx — Kelompok 3, QA passed"
cp "output/01079_Kelompok 3_RMK Pert. 11.docx" "../01079_Kelompok 3_RMK Pert. 11.docx"
```

---

## Self-Review Notes (plan vs spec)

- **Spec coverage:** D1 group identity → Tasks 0/6/8; D2 clone → Task 0; D3/D4 visual identity & Cornell → inherited (build_docx unchanged styling); D5 equations → Tasks 5/6; §3 coverage map → Task 7; A–F structure → Tasks 7/8; pipeline §5 → Tasks 1–6; language pass §7 → Task 9; quality gate §9 → Task 10. All mapped.
- **Equation transcription risk:** exact Eq 4.1–4.4 forms are transcribed from the PDF during Task 7, not guessed — flagged in that step.
- **Crop coordinates** are placeholders (`0` y-values) deliberately; Task 3 Step 3 derives the real bounds before cropping.
- **Type consistency:** `latex_to_omath` / `render_eq_png` names match between Task 5 (definition) and Task 6 (use); `add_equation(doc, latex, root)` signature consistent.
