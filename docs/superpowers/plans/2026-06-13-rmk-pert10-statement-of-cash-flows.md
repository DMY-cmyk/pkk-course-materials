# RMK Pertemuan 10 — Statement of Cash Flows Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the individual graded deliverable `output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx` — a graduate, professor-voice Cornell-Notes RMK of Wolk Ch.13 "Statement of Cash Flows" — via a reproducible Rust-first pipeline with documented Python exceptions.

**Architecture:** Five-stage `input/ → output/` pipeline in a new sibling project `rmk-pkk-pert10-statement-of-cash-flows/`, mirroring the proven `rmk-pkk-pert9-income-statement/` layout. Stage 1 (Rust `pdf_probe`, lopdf) confirms the page range and inventories per-page image XObjects. Stage 2 (Python `extract_text.py`, PyMuPDF) extracts/segments the chapter text. Stage 3 (Python `crop_exhibits.py`, PyMuPDF+PIL) crops exhibits — K2's verified rectangles reused against the identical SAGE export. Stage 4 (Rust `visual_gen`, resvg) rasterizes authored SVG diagrams. Stage 5 (Python `build_docx.py`, python-docx) assembles the docx: Calibri 12 / 1.5 spacing / A4, Cornell two-column Bagian A with full-width exhibit breakouts, Bagian B–F. Content markdown in `content/` is the editable source of truth, re-authored fresh in Dzaki's voice from the citation-identical K2 Ch.13 analysis.

**Tech Stack:** Rust (lopdf, resvg, anyhow, clap, serde) · Python 3.12 (python-docx 1.2.0, PyMuPDF 1.27.x, Pillow) · pytest · cargo.

**Spec:** `docs/superpowers/specs/2026-06-13-rmk-pert10-statement-of-cash-flows-design.md`

**Reuse sources (read for exact code/coords; copy then edit):**
- `rmk-pkk-pert9-income-statement/` — `src/python/{extract_text,build_docx}.py`, `src/python/test_*.py`, `src/rust/{chapter_locator,visual_gen}/`, `Cargo.toml`, `requirements.txt`, `.gitignore`, `README.md`
- `Kelompok 2 Pasca UTS/` — `assets/crop_exhibits.py`, `assets/make_diagrams.py`, the 6 cropped `exhibit-13-*.png`, the 5 `diagram-*.png`, `analysis/{chapter-deep-read,gap-analysis,coverage-audit}.md`, `content/rmk-ch13.md`
- Source PDF: `PKK Pert. 10 - Statement of Cashflow.pdf` (repo root) — Wolk Ch.13, print pp. 375–409.
- Syllabus: `rmk-pkk-pert9-income-statement/input/syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf`

**Path note:** All paths below are relative to the new project root `rmk-pkk-pert10-statement-of-cash-flows/` unless prefixed `REPO/` (= the course folder root). The project root is referred to as `PROJ/`.

---

## File Structure

| File | Responsibility |
|---|---|
| `PROJ/CLAUDE.md` | Standing instructions + Rust→Python fallback justification log |
| `PROJ/README.md` | Run order, prerequisites, Rust/Python split table |
| `PROJ/.gitignore` | Ignore `input/`, `extraction/`, `assets/**/*.png` (regenerable), `target/`, `__pycache__/`, `.pytest_cache/` |
| `PROJ/Cargo.toml` | Rust workspace: members `src/rust/pdf_probe`, `src/rust/visual_gen` |
| `PROJ/requirements.txt` | `python-docx==1.2.0`, `PyMuPDF`, `Pillow` |
| `PROJ/input/chapter/PKK Pert. 10 - Statement of Cashflow.pdf` | Source chapter (copied; gitignored) |
| `PROJ/input/syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf` | Syllabus (copied; gitignored) |
| `PROJ/src/rust/pdf_probe/{Cargo.toml,src/main.rs}` | Stage 1: page-range + image-XObject inventory → `extraction/chapter-range.json`, `extraction/verification-report.md` |
| `PROJ/src/rust/visual_gen/{Cargo.toml,src/main.rs}` | Stage 4: SVG→PNG rasterizer (reused from pert9) |
| `PROJ/src/python/extract_text.py` | Stage 2: PyMuPDF text extraction + section segmentation |
| `PROJ/src/python/crop_exhibits.py` | Stage 3: PyMuPDF/PIL exhibit cropping |
| `PROJ/src/python/build_docx.py` | Stage 5: python-docx assembly (Calibri/1.5/A4, Cornell two-column, A–F) |
| `PROJ/src/python/test_extract_text.py` | Tests for `segment()` |
| `PROJ/src/python/test_build_docx.py` | Tests for `parse_blocks()`, Cornell grouping, inline runs |
| `PROJ/assets/diagrams/svg/*.svg` | Authored diagram sources |
| `PROJ/assets/diagrams/*.png` | Rasterized diagrams (gitignored) |
| `PROJ/assets/exhibits/*.png` | Cropped exhibits (gitignored) |
| `PROJ/content/00_identitas.md` | Identitas Resume header block |
| `PROJ/content/A_cornell.md` | Bagian A — Cornell Notes (cue/notes rows + exhibit/image directives) |
| `PROJ/content/B_ringkasan.md` | Bagian B — Ringkasan |
| `PROJ/content/C_refleksi.md` | Bagian C — Refleksi & Analisis (5 questions) |
| `PROJ/content/D_kesimpulan.md` | Bagian D — Kesimpulan (150–250 words) |
| `PROJ/content/E_review.md` | Bagian E — Review Mandiri (≥5 Q) |
| `PROJ/content/F_referensi.md` | Bagian F — Referensi (APA-7) |
| `PROJ/output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx` | Final deliverable |

---

## Task 1: Worktree + workspace scaffold

**Files:**
- Create: `PROJ/.gitignore`, `PROJ/Cargo.toml`, `PROJ/requirements.txt`, `PROJ/CLAUDE.md`, `PROJ/README.md`
- Create dirs: `PROJ/{input/chapter,input/syllabus,extraction,assets/diagrams/svg,assets/exhibits,content,src/rust,src/python,output}`

- [ ] **Step 1: Create the worktree** (per superpowers:using-git-worktrees)

Run from `REPO/`:
```bash
git worktree add -b feat/rmk-pert10 ../pkk-rmk-pert10 HEAD
```
All subsequent work happens inside that worktree's `rmk-pkk-pert10-statement-of-cash-flows/` directory. If the user prefers working in-place on a branch instead, create the branch `feat/rmk-pert10` and skip the worktree.

- [ ] **Step 2: Create directory tree and copy inputs**

```bash
cd <worktree-root>
mkdir -p rmk-pkk-pert10-statement-of-cash-flows/{input/chapter,input/syllabus,extraction,assets/diagrams/svg,assets/exhibits,content,src/rust,src/python,output}
cp "PKK Pert. 10 - Statement of Cashflow.pdf" "rmk-pkk-pert10-statement-of-cash-flows/input/chapter/"
cp "rmk-pkk-pert9-income-statement/input/syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf" "rmk-pkk-pert10-statement-of-cash-flows/input/syllabus/"
```

- [ ] **Step 3: Write `PROJ/.gitignore`**

```gitignore
/input/
/extraction/
/assets/diagrams/*.png
/assets/exhibits/*.png
/target/
**/__pycache__/
.pytest_cache/
```

- [ ] **Step 4: Write `PROJ/requirements.txt`**

```
python-docx==1.2.0
PyMuPDF
Pillow
```

- [ ] **Step 5: Write `PROJ/Cargo.toml`** (workspace)

```toml
[workspace]
resolver = "2"
members = ["src/rust/pdf_probe", "src/rust/visual_gen"]
```

- [ ] **Step 6: Write `PROJ/CLAUDE.md`**

Include: project purpose (RMK Pert.10 individual, Cornell), the governing rules verbatim (A4, Calibri 12, 1.5 spacing, ≥8 pages, MS Word; Cornell A–F + rubric), the source-of-truth hierarchy, and a **Rust→Python fallback log** with three justified exceptions: (1) `extract_text.py` PyMuPDF — lopdf returns only footers (no ToUnicode CMap); (2) `crop_exhibits.py` PyMuPDF/PIL — page rasterization + tight clipping; (3) `build_docx.py` python-docx — exact Calibri/1.5/A4/Cornell-table/footer typography proven in prior builders.

- [ ] **Step 7: Write `PROJ/README.md`**

Document prerequisites and the deterministic run order:
```powershell
cargo run --release -p pdf_probe        # -> extraction/chapter-range.json + verification-report.md
python src/python/extract_text.py        # -> extraction/text/*.md, page-map.json
python src/python/crop_exhibits.py       # -> assets/exhibits/*.png
cargo run --release -p visual_gen        # -> assets/diagrams/*.png
python src/python/build_docx.py          # -> output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx
```
Plus the Rust/Python split table and the tests section (`cargo test`; `python -m pytest src/python -q`).

- [ ] **Step 8: Commit**

```bash
git add rmk-pkk-pert10-statement-of-cash-flows/{.gitignore,Cargo.toml,requirements.txt,CLAUDE.md,README.md}
git commit -m "feat(rmk10): scaffold workspace, inputs, and docs"
```

---

## Task 2: Rust `pdf_probe` — page range + image inventory

The assigned PDF is a single-chapter file, so the "chapter range" is the whole document. This crate confirms the page count, records the print-page range, and inventories image XObjects per page (which pages carry exhibits) using lopdf — the verification report this produces is genuinely useful since this chapter (unlike Ch.12) has exhibits.

**Files:**
- Create: `PROJ/src/rust/pdf_probe/Cargo.toml`
- Create: `PROJ/src/rust/pdf_probe/src/main.rs`

- [ ] **Step 1: Write `PROJ/src/rust/pdf_probe/Cargo.toml`**

```toml
[package]
name = "pdf_probe"
version = "0.1.0"
edition = "2021"

[dependencies]
anyhow = "1"
clap = { version = "4", features = ["derive"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
lopdf = "0.34"
```

- [ ] **Step 2: Write the failing test** in `PROJ/src/rust/pdf_probe/src/main.rs`

Add a pure helper `print_page_range(start_print: u32, n_pages: u32) -> String` that maps the chapter's first print page and the page count to an inclusive print range string, then a test:

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn print_range_inclusive() {
        // 35 content pages starting at print page 375 -> "375-409"
        assert_eq!(print_page_range(375, 35), "375-409");
    }

    #[test]
    fn single_page_range() {
        assert_eq!(print_page_range(375, 1), "375");
    }
}
```

- [ ] **Step 3: Run test to verify it fails**

Run: `cargo test -p pdf_probe`
Expected: FAIL — `print_page_range` not found / does not compile.

- [ ] **Step 4: Write minimal implementation** in `PROJ/src/rust/pdf_probe/src/main.rs`

```rust
//! Probes the standalone single-chapter SAGE PDF (Wolk Ch.13 "Statement of
//! Cash Flows"). Emits extraction/chapter-range.json (range = whole file) and
//! extraction/verification-report.md (per-page image-XObject inventory).

use anyhow::{Context, Result};
use clap::Parser;
use serde::Serialize;

/// Inclusive print-page range string from a starting print page and page count.
fn print_page_range(start_print: u32, n_pages: u32) -> String {
    if n_pages <= 1 {
        return start_print.to_string();
    }
    format!("{}-{}", start_print, start_print + n_pages - 1)
}

#[derive(Parser)]
struct Args {
    #[arg(long, default_value = "input/chapter/PKK Pert. 10 - Statement of Cashflow.pdf")]
    pdf: String,
    #[arg(long, default_value = "extraction/chapter-range.json")]
    out: String,
    #[arg(long, default_value = "extraction/verification-report.md")]
    report: String,
    /// First print page of the chapter (SAGE title page) — for the range string.
    #[arg(long, default_value = "375")]
    start_print: u32,
}

#[derive(Serialize)]
struct RangeOut {
    start_page: u32,
    end_page: u32,
    print_pages: String,
}

fn main() -> Result<()> {
    let args = Args::parse();
    let doc = lopdf::Document::load(&args.pdf)
        .with_context(|| format!("loading PDF {}", args.pdf))?;
    let page_ids: Vec<(u32, _)> = doc.get_pages().into_iter().collect();
    let n_pages = page_ids.len() as u32;
    anyhow::ensure!(n_pages > 0, "PDF has no pages");

    // Per-page image-XObject count.
    let mut report = vec![
        "# Verification report — exhibit (image XObject) inventory".to_string(),
        format!("PDF: {} — {} pages, print pages {}",
                args.pdf, n_pages, print_page_range(args.start_print, n_pages)),
        "".into(), "| PDF page | image count |".into(), "|---|---|".into(),
    ];
    let mut total = 0usize;
    for (i, (page_no, _)) in page_ids.iter().enumerate() {
        let n_imgs = count_page_images(&doc, *page_no);
        total += n_imgs;
        report.push(format!("| {} | {} |", i + 1, n_imgs));
    }
    report.push(format!("\n**Total image XObjects: {total}.** Pages with images are exhibit-bearing; cross-check against crop_exhibits.py rectangles."));

    if let Some(parent) = std::path::Path::new(&args.out).parent() {
        std::fs::create_dir_all(parent)?;
    }
    let range = RangeOut { start_page: 1, end_page: n_pages, print_pages: print_page_range(args.start_print, n_pages) };
    std::fs::write(&args.out, serde_json::to_string_pretty(&range)?)?;
    std::fs::write(&args.report, report.join("\n"))?;
    println!("range: 1-{n_pages} ({}) ; total images {total}", range.print_pages);
    Ok(())
}

/// Count image XObjects referenced by a page's resources (best-effort; lopdf).
fn count_page_images(doc: &lopdf::Document, page_no: u32) -> usize {
    use lopdf::Object;
    let Ok(page_dict) = doc.get_dictionary(*doc.get_pages().get(&page_no).unwrap()) else { return 0 };
    let Ok(res) = page_dict.get(b"Resources").and_then(|o| doc.dereference(o)).map(|(_, o)| o) else { return 0 };
    let Ok(res_dict) = res.as_dict() else { return 0 };
    let Ok(xobj) = res_dict.get(b"XObject").and_then(|o| doc.dereference(o)).map(|(_, o)| o) else { return 0 };
    let Ok(xobj_dict) = xobj.as_dict() else { return 0 };
    let mut n = 0;
    for (_, v) in xobj_dict.iter() {
        if let Ok((_, Object::Stream(s))) = doc.dereference(v) {
            if let Ok(sub) = s.dict.get(b"Subtype").and_then(|o| o.as_name()) {
                if sub == b"Image" { n += 1; }
            }
        }
    }
    n
}
```

Note: `count_page_images` is best-effort. If the lopdf resource-walk API differs in the pinned version, simplify to counting `XObject` entries whose subtype is `Image`; the exact count is advisory (the authoritative exhibit list comes from `crop_exhibits.py`). Keep the two unit tests green regardless.

- [ ] **Step 5: Run tests to verify they pass**

Run: `cargo test -p pdf_probe`
Expected: PASS (2 tests).

- [ ] **Step 6: Run the probe against the real PDF**

Run from `PROJ/`: `cargo run --release -p pdf_probe`
Expected: prints `range: 1-N (375-...) ; total images M`; writes `extraction/chapter-range.json` and `extraction/verification-report.md`. Record N (page count) — it feeds Task 4 (text extraction reads pages 1..N).

- [ ] **Step 7: Commit**

```bash
git add src/rust/pdf_probe Cargo.toml
git commit -m "feat(rmk10): rust pdf_probe — range + image inventory"
```

---

## Task 3: Python `extract_text.py` — text + section segmentation

Documented Python exception (PyMuPDF): lopdf cannot read this SAGE PDF's body. Reuse pert9's `extract_text.py` structure and its `segment()`/`page_numbers()` helpers verbatim; change the section heading list to Ch.13's, and read from the standalone chapter PDF over pages `1..end_page` from `chapter-range.json`.

**Files:**
- Create: `PROJ/src/python/extract_text.py`
- Test: `PROJ/src/python/test_extract_text.py`

- [ ] **Step 1: Write the failing test** `PROJ/src/python/test_extract_text.py`

Copy pert9's `test_extract_text.py` tests for `segment()` (they are content-agnostic). Add one Ch.13-specific test:

```python
from extract_text import segment, page_numbers

def test_segment_splits_on_ch13_headings():
    lines = ["[[page:1]]", "preamble text",
             "Statement of Changes in Financial Position", "scfp body",
             "Free Cash Flow", "fcf body"]
    sections = [("Statement of Changes in Financial Position", "02_scfp"),
                ("Free Cash Flow", "10_fcf")]
    out = dict(segment(lines, sections))
    assert "00_preamble" in out
    assert "scfp body" in out["02_scfp"]
    assert "fcf body" in out["10_fcf"]

def test_page_numbers_parses_markers():
    assert page_numbers("a [[page:3]] b [[page:5]] c") == [3, 5]
```

- [ ] **Step 2: Run test to verify it fails**

Run from `PROJ/src/python`: `python -m pytest test_extract_text.py -q`
Expected: FAIL — `extract_text` module not found.

- [ ] **Step 3: Write `PROJ/src/python/extract_text.py`**

Copy pert9 `src/python/extract_text.py` and make exactly these edits:
1. Replace the `SECTIONS` list with Ch.13 headings (verify the exact strings against `extraction/text` after a first raw run; start from these, taken from the K2 deep-read):

```python
SECTIONS = [
    ("Learning Objectives", "01_learning_objectives"),
    ("Statement of Changes in Financial Position", "02_scfp"),
    ("Funds Flow and Solvency", "03_funds_solvency"),
    ("Cash Flow and Working Capital", "04_cash_vs_wc"),
    ("The Motivation for a Statement of Cash Flows", "05_motivation"),
    ("Cash Flow Statement Requirements", "06_requirements"),
    ("The Nonarticulation Problem", "07_nonarticulation"),
    ("Classification Problems of SFAS No. 95", "08_classification"),
    ("The Analytical Usefulness of the Cash Flow Statement", "09_analytical"),
    ("Free Cash Flow", "10_free_cash_flow"),
    ("Cash Flow Research", "11_research"),
    ("Improving the Statement of Cash Flows", "12_improving"),
    ("Summary", "13_summary"),
    ("Questions", "14_questions"),
]
```
2. Change the PDF path to `input/chapter/PKK Pert. 10 - Statement of Cashflow.pdf`.
3. Read pages `start..end` from `chapter-range.json` (already 1..N).
4. Rewrite the verification block header to "Wolk Ch. 13 (SAGE edition)" and report image counts (this chapter HAS exhibits — do not assert zero).
5. Relax the heading-match guard: `if matched < 4: sys.exit(...)` (segment count is advisory; exact headings are tuned after the first run).

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest test_extract_text.py -q`
Expected: PASS.

- [ ] **Step 5: Run extraction against the real PDF, then tune headings**

Run from `PROJ/`: `python src/python/extract_text.py`
Expected: writes `extraction/text/*.md` + `page-map.json`. Open `extraction/text/00_preamble.md` and the segment files; if a heading did not split (section text landed in the wrong file), correct the exact heading string in `SECTIONS` to match the PDF and re-run. This is the source-of-truth text used for authoring.

- [ ] **Step 6: Commit**

```bash
git add src/python/extract_text.py src/python/test_extract_text.py
git commit -m "feat(rmk10): PyMuPDF text extraction + Ch.13 segmentation"
```

---

## Task 4: Python `crop_exhibits.py` — exhibit crops

Documented Python exception (PyMuPDF/PIL). The assigned PDF is the identical SAGE export K2 cropped, so K2's rectangles transfer directly. Reuse them, verify visually, and add any missing coverage-map exhibits (13.1 SCFP format, the ABC Company / FCF tables) after a page survey.

**Files:**
- Create: `PROJ/src/python/crop_exhibits.py`
- Output: `PROJ/assets/exhibits/*.png`

- [ ] **Step 1: Write `PROJ/src/python/crop_exhibits.py`**

Copy `REPO/Kelompok 2 Pasca UTS/assets/crop_exhibits.py` and edit:
1. `PDF = os.path.join(HERE, "..", "..", "input", "chapter", "PKK Pert. 10 - Statement of Cashflow.pdf")`
2. Output dir → `os.path.join(HERE, "..", "..", "assets", "exhibits")`; `os.makedirs(out_dir, exist_ok=True)`.
3. Keep the existing `EXHIBITS` dict (13-2, 13-3, 13-4, 13-5, 13-6, 13-9) verbatim.

- [ ] **Step 2: Survey pages to confirm coordinates transfer**

Run from `PROJ/`: `python src/python/crop_exhibits.py --pages`
Then run the default crop: `python src/python/crop_exhibits.py`
Open each `assets/exhibits/exhibit-13-*.png`. Expected: each shows the exhibit table tightly cropped, no page header/footer, no caption of the *next* exhibit. If the export's page geometry differs, adjust the `fitz.Rect` y-bounds and re-run.

- [ ] **Step 3: Add missing coverage-map exhibits**

Using the survey PNGs, locate **Exhibit 13.1 (SCFP format)** and the **ABC Company / Free Cash Flow** tables (per the coverage map and `extraction/verification-report.md` image pages). Add entries to `EXHIBITS`, e.g.:

```python
    # Exhibit 13.1 — SCFP (sources/uses) format. Page/rect set from --pages survey.
    "exhibit-13-1": [(P, fitz.Rect(X0, Y0, X1, Y1))],
    # ABC Company FCF table(s) — set from survey.
    "exhibit-13-8-abc": [(P, fitz.Rect(X0, Y0, X1, Y1))],
```
Re-run the crop; verify the new PNGs. If a target turns out to be vector text rather than an embedded image (no XObject on that page per the report), it is still croppable as a rectangle clip — that is fine.

- [ ] **Step 4: Commit** (PNGs are gitignored; commit the script)

```bash
git add src/python/crop_exhibits.py
git commit -m "feat(rmk10): exhibit cropping (K2 rects reused + 13.1/ABC added)"
```

---

## Task 5: Rust `visual_gen` + authored diagram SVGs

Reuse pert9's `visual_gen` crate verbatim (it rasterizes every `assets/diagrams/svg/*.svg` to PNG via resvg). Author the SVG diagrams for the reconstructed visuals (OIF trichotomy, nonarticulation, FCF waterfall, four cash-flow measures, the APB19→SFAS95 timeline) — re-create them from K2's `make_diagrams.py`/`diagram-*.png` as honest reconstructions captioned "diolah dari Wolk et al. (2017)".

**Files:**
- Create: `PROJ/src/rust/visual_gen/{Cargo.toml,src/main.rs}` (copied from pert9)
- Create: `PROJ/assets/diagrams/svg/{trichotomy,nonarticulation,fcf_waterfall,four_measures,timeline}.svg`
- Output: `PROJ/assets/diagrams/*.png`

- [ ] **Step 1: Copy the `visual_gen` crate**

Copy `rmk-pkk-pert9-income-statement/src/rust/visual_gen/` → `PROJ/src/rust/visual_gen/` unchanged (it globs `assets/diagrams/svg/*.svg` → `assets/diagrams/*.png` at 300 DPI / ~1712px). Confirm `Cargo.toml` package name `visual_gen` matches the workspace member path.

- [ ] **Step 2: Author the 5 SVG diagrams**

Write five monochrome SVGs to `assets/diagrams/svg/`. Use K2's `assets/make_diagrams.py` and `assets/diagram-*.png` as the visual reference for content/layout (re-draw, do not copy raster). Each diagram is 1712px-wide-equivalent viewBox, Calibri/sans labels, black-on-white. Subjects:
- `trichotomy.svg` — Operating / Investing / Financing three-box classification.
- `nonarticulation.svg` — why indirect-method adjustments ≠ balance-sheet changes (3M illustration schematic).
- `fcf_waterfall.svg` — NOPLAT − investment in operating invested capital → FCF.
- `four_measures.svg` — the four cash-flow performance measures.
- `timeline.svg` — APB Opinion No. 19 (1971) → SFAS No. 95 (1987) → later refinements.

- [ ] **Step 3: Run the rasterizer and the crate test**

Run from `PROJ/`: `cargo test -p visual_gen` then `cargo run --release -p visual_gen`
Expected: tests pass; five `assets/diagrams/*.png` written. Open each to confirm labels render (system Calibri present).

- [ ] **Step 4: Commit** (SVGs tracked; PNGs gitignored)

```bash
git add src/rust/visual_gen assets/diagrams/svg
git commit -m "feat(rmk10): visual_gen crate + 5 reconstructed diagram SVGs"
```

---

## Task 6: Python `build_docx.py` — Calibri/1.5/A4 + Cornell two-column + A–F

Adapt pert9's `build_docx.py` (most evolved: footer PAGE field, `@table` TOML, subheadings, rule). Three substantive changes: (1) `FONT="Calibri"` and 1.5 line spacing; (2) a **new Cornell two-column renderer** with full-width image breakout (Layout B); (3) build flow reads `00_identitas.md` as a header block then `A_*`…`F_*` in order, with no references-omission (references ARE included as Bagian F).

**Files:**
- Create: `PROJ/src/python/build_docx.py`
- Test: `PROJ/src/python/test_build_docx.py`

- [ ] **Step 1: Write the failing tests** `PROJ/src/python/test_build_docx.py`

Copy pert9's `test_build_docx.py` tests for `parse_inline_runs`, `split_caption`, and `parse_blocks` that still apply. Add tests for the new Cornell parsing/grouping:

```python
from build_docx import parse_blocks, group_cornell, parse_inline_runs

def test_parse_blocks_emits_cue_and_notes():
    md = "@cue Apa itu SCF?\n@notes *Statement of cash flows* menyajikan arus kas.\n"
    blocks = parse_blocks(md)
    assert ("cue", "Apa itu SCF?") in blocks
    assert blocks[1][0] == "notes"

def test_group_cornell_pairs_consecutive_rows():
    blocks = [("cue", "Q1"), ("notes", "A1"),
              ("cue", "Q2"), ("notes", "A2"),
              ("image", ("Exhibit 13.2 | Sumber: x", "p.png")),
              ("cue", "Q3"), ("notes", "A3")]
    grouped = group_cornell(blocks)
    # two cornell tables, split by the image
    assert grouped[0] == ("cornell", [("Q1", "A1"), ("Q2", "A2")])
    assert grouped[1][0] == "image"
    assert grouped[2] == ("cornell", [("Q3", "A3")])

def test_inline_runs_bold_italic():
    runs = parse_inline_runs("a **b** *c*")
    assert ("b", True, False) in runs
    assert ("c", False, True) in runs
```

- [ ] **Step 2: Run tests to verify they fail**

Run from `PROJ/src/python`: `python -m pytest test_build_docx.py -q`
Expected: FAIL — `build_docx` / `group_cornell` not defined.

- [ ] **Step 3: Write `PROJ/src/python/build_docx.py`**

Start from pert9 `src/python/build_docx.py`. Apply these exact changes:

1. **Constants:**
```python
FONT = "Calibri"
STUDENT = "Dzaki Muhammad Yusfian"
NIM = "1225 01079"
OUT_NAME = "01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx"
```
2. **Line spacing → 1.5.** In `_add_para`, replace the EXACTLY/`BODY_LINE_PT` lines with:
```python
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
```
(remove the `pf.line_spacing = Pt(BODY_LINE_PT)` line and the `BODY_LINE_PT` constant). Do the same wherever cell paragraphs set spacing — use `WD_LINE_SPACING.ONE_POINT_FIVE`.
3. **Extend `parse_blocks`** to recognize Cornell directives — add these branches before the generic `else`:
```python
        elif stripped.startswith("@cue "):
            flush()
            blocks.append(("cue", stripped[5:].strip()))
        elif stripped.startswith("@notes "):
            flush()
            blocks.append(("notes", stripped[7:].strip()))
```
4. **Add `group_cornell(blocks)`** — pairs consecutive `cue`+`notes` into `("cornell", [(cue, notes), ...])`, flushing on any other block:
```python
def group_cornell(blocks):
    out, pending, last_cue = [], [], None
    def flush_rows():
        nonlocal pending
        if pending:
            out.append(("cornell", pending)); pending = []
    for kind, payload in blocks:
        if kind == "cue":
            last_cue = payload
        elif kind == "notes":
            pending.append((last_cue or "", payload)); last_cue = None
        else:
            flush_rows(); out.append((kind, payload))
    flush_rows()
    return out
```
5. **Add the Cornell table renderer:**
```python
def add_cornell_table(doc, rows):
    table = doc.add_table(rows=len(rows), cols=2)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (cue, notes) in enumerate(rows):
        for j, txt in enumerate((cue, notes)):
            cell = table.rows[i].cells[j]
            cell.text = ""
            para = cell.paragraphs[0]
            para.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            para.alignment = (WD_ALIGN_PARAGRAPH.LEFT if j == 0
                              else WD_ALIGN_PARAGRAPH.JUSTIFY)
            for t, b, it in parse_inline_runs(txt):
                _style_run(para.add_run(t), font_size=11,
                           bold=(b or j == 0), italic=it)
    for row in table.rows:           # Cue 5 cm | Notes 10 cm (text width 15 cm)
        row.cells[0].width = Cm(5)
        row.cells[1].width = Cm(10)
```
6. **Rewrite `build()` flow:**
   - Page setup A4, 3 cm margins, footer PAGE field (unchanged). Set `style.font.name = FONT`.
   - **Identitas:** read `content/00_identitas.md`; first non-`#` line bold 14 pt centered, remaining lines 12 pt centered; then `add_rule(doc)`. (Reuse pert9 front-matter loop.)
   - **Body:** for each of `["A_cornell.md","B_ringkasan.md","C_refleksi.md","D_kesimpulan.md","E_review.md","F_referensi.md"]` (explicit order), read the file, `blocks = parse_blocks(md)`, then `for kind, payload in group_cornell(blocks):` dispatch:
     - `"cornell"` → `add_cornell_table(doc, payload)`
     - `"image"` → `add_image_with_caption(doc, resolved_path, caption)`
     - `"table"` → `add_table_from_toml(...)` (kept for any data tables)
     - `"heading"` → bold 13 pt left (Bagian headings)
     - `"subheading"` → bold-italic 12 pt left
     - `"bullet"` → `• ` + runs, indent 0.75 cm
     - `"ref"` → hanging indent (references)
     - else → justified paragraph
   - Image paths in `A_cornell.md` are written relative to `content/` (e.g. `../assets/exhibits/exhibit-13-2.png`); resolve with `os.path.normpath(os.path.join(content_dir, rel))`.
   - In `add_image_with_caption`, set width to `Cm(14.5)` (full text-width breakout).
   - Save to `output/OUT_NAME`; print path + size.
   - Remove the pert9 "skip 14_ references" logic — Bagian F references are included.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest test_build_docx.py -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/python/build_docx.py src/python/test_build_docx.py
git commit -m "feat(rmk10): docx builder — Calibri/1.5/A4 + Cornell two-column (Layout B)"
```

---

## Task 7: Author content (Identitas + Bagian A–F)

Re-author all prose fresh in Dzaki's individual professor-voice, restructured into Cornell A–F, from the citation-identical K2 Ch.13 analysis (`REPO/Kelompok 2 Pasca UTS/analysis/*.md`, `content/rmk-ch13.md`) and the freshly-extracted `extraction/text/*.md`. Formal academic Bahasa Indonesia; English technical terms in *italics*, glossed on first use. No fabrication — every figure/claim traceable to the chapter; inline citations `(Wolk et al., 2017, hlm. N)` using the **print page** (375–409).

**Files:** Create `PROJ/content/{00_identitas,A_cornell,B_ringkasan,C_refleksi,D_kesimpulan,E_review,F_referensi}.md`

- [ ] **Step 1: Write `content/00_identitas.md`**

```markdown
RINGKASAN MATERI KULIAH (RMK) — PERTEMUAN 10
Mata Kuliah: Pelaporan Keuangan Korporat (MNK202)
Topik: Statement of Cash Flows
Dosen Pengampu: <isi dari silabus; jika tidak tercantum, beri tanda [—]>
Nama Mahasiswa: Dzaki Muhammad Yusfian — NIM 1225 01079
Program Studi: Pascasarjana — Magister Akuntansi / Magister Manajemen, STIE YKPN
Tanggal: <isi dari silabus / [—]>
```
First read the syllabus PDF (`input/syllabus/...`) to fill Dosen/Tanggal; if absent, leave the bracketed placeholder (per spec). Source: `Wolk, Dodd & Rozycki (2017), Accounting Theory (9th ed.), Ch.13`.

- [ ] **Step 2: Write `content/A_cornell.md` — Bagian A (Cornell Notes, Layout B)**

Begin with `## Bagian A — Cornell Notes`. Then author cue/notes rows covering the full mandatory coverage map **in chapter order**, breaking exhibits/diagrams out full-width right after the row they support. Each `@cue` is a key term or conceptual question; each `@notes` is one dense professor-voice paragraph (definitions, theory, why, links), glossing English terms. Use this directive grammar (consumed by `build_docx.py`):
```markdown
@cue Mengapa "funds" akhirnya didefinisikan sebagai kas? (APB 19 → SFAS 95)
@notes *Statement of Changes in Financial Position* (SCFP, APB Opinion No. 19, 1971) memakai konsep *funds* = modal kerja bersih... SFAS No. 95 (1987) menggantinya karena kas lebih relevan untuk menilai *liquidity* (likuiditas) dan *financial flexibility* (fleksibilitas keuangan) (Wolk et al., 2017, hlm. 377).

![Exhibit 13.2 — Statement of Cash Flows: Direct vs Indirect Method | Sumber: Wolk et al. (2017), hlm. 384](../assets/exhibits/exhibit-13-2.png)

@cue Apa perbedaan metode langsung dan tidak langsung?
@notes ...
```
Coverage to embed across the rows (each glossed): SCFP/APB 19 & all-inclusive approach; motivation & six benefits & SFAС 1/5; OIF *trichotomy* + cash equivalents; direct vs indirect; **nonarticulation** (Bahnson/Miller/Budge, 3M); classification problems (Nurnberg, interest/dividends, *proprietary vs entity theory*, IAS 7); premium/discount four allocation methods + SFAS 34 + SFAS 104; Ingram & Lee; manipulation (Tyco, Ford/GM/Harley, Navistar, WorldCom CFO–CFI); user needs (Buffett, NPV); **FCF = NOPLAT − investment in operating invested capital** (ABC Company); Broome's three recommendations. Place exhibits 13-2/3/4/5/6/9 + 13-1/ABC and the five diagrams beside their relevant rows.

- [ ] **Step 3: Write `content/B_ringkasan.md` — Bagian B**

`## Bagian B — Ringkasan` + 1–2 own-words paragraphs capturing the chapter's core, **≤ 15–20% of source length** (the chapter is ~35 pages of prose; keep this to roughly 250–400 words). No citations needed; synthesis voice.

- [ ] **Step 4: Write `content/C_refleksi.md` — Bagian C**

`## Bagian C — Refleksi dan Analisis Akademik`. Answer the five reflection questions as `### ` subheadings, each with an analytical (not descriptive) paragraph: (1) pemahaman; (2) mengapa penting; (3) penerapan dunia nyata (e.g. analisis solvabilitas, kasus WorldCom/W.T. Grant); (4) hubungan dengan mata kuliah lain (analisis laporan keuangan, manajemen keuangan, audit); (5) **kelebihan dan keterbatasan** teori (nonartikulasi, ruang klasifikasi SFAS 95, FCF non-GAAP). This section carries the most rubric weight (Analisis 25%) — make it argumentative.

- [ ] **Step 5: Write `content/D_kesimpulan.md` — Bagian D**

`## Bagian D — Kesimpulan Akademik` + one cohesive paragraph, **150–250 words**, answering: inti materi, manfaat, implikasi praktis, kontribusi terhadap ilmu. Open with "Berdasarkan pembahasan yang telah dilakukan, dapat disimpulkan bahwa ...".

- [ ] **Step 6: Write `content/E_review.md` — Bagian E**

`## Bagian E — Review Mandiri (Active Recall)` + **≥ 5** numbered self-test questions as bullets covering SCFP→SFAS 95, trichotomy, direct/indirect, nonarticulation, FCF, and a manipulation case.

- [ ] **Step 7: Write `content/F_referensi.md` — Bagian F**

`## Bagian F — Referensi Akademik` (APA-7) as `- ` bullets (hanging indent):
```markdown
- Wolk, H. I., Dodd, J. L., & Rozycki, J. J. (2017). *Accounting theory: Conceptual issues in a political and economic environment* (9th ed.). SAGE Publications.
- Silabus Pelaporan Keuangan Korporat (MNK202), Pascasarjana STIE YKPN Yogyakarta, Tahun Ajaran 2025/2026.
```

- [ ] **Step 8: Commit**

```bash
git add content/
git commit -m "docs(rmk10): author Cornell A–F content (professor-voice, glossed)"
```

---

## Task 8: Build, verify, and quality-gate

**Files:** Output `PROJ/output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx`

- [ ] **Step 1: Run the full pipeline end-to-end**

Run from `PROJ/`:
```powershell
cargo run --release -p pdf_probe
python src/python/extract_text.py
python src/python/crop_exhibits.py
cargo run --release -p visual_gen
python src/python/build_docx.py
```
Expected: each stage prints success; `output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx` written.

- [ ] **Step 2: Run all tests**

```bash
cargo test
python -m pytest src/python -q
```
Expected: all green.

- [ ] **Step 3: Verify the docx against the rules (verification-before-completion)**

Open the docx and confirm, recording evidence for each:
- Font Calibri 12; line spacing 1.5; A4; page numbers bottom-right.
- **Page count ≥ 8.** If short, deepen Bagian A/C prose (not padding) and rebuild.
- Identitas + Bagian A–F all present and ordered; Bagian A renders as a two-column Cornell table with full-width exhibits beside their explanations.
- Every cropped exhibit displays correctly (no overflow, no header/footer, correct caption + "Sumber").
- Bagian B ≤ ~20% length; Bagian D 150–250 words; Bagian E ≥ 5 questions; Bagian F APA-7.
- Filename exact: `01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx`.

Programmatic page-count check (optional):
```python
# quick check via python-docx is unreliable for page count; open in Word/LibreOffice to confirm, or:
import subprocess  # use a headless LibreOffice to PDF then count if available
```
Page count must be confirmed by opening the document, not asserted blindly.

- [ ] **Step 4: Two-stage review** (per superpowers:requesting-code-review)
- Stage 1 — content fidelity: no fabrication; every exhibit number, page citation, and figure traceable to the chapter; coverage-map complete.
- Stage 2 — language/voice/format: graduate register, consistent *italic* term treatment, Cornell completeness, rubric alignment (Cornell 20 / Ringkasan 20 / Analisis 25 / Kesimpulan 15 / Recall 10 / Bahasa-Format 10).

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "feat(rmk10): build final RMK Pert. 10 docx; verified rules + coverage"
```

- [ ] **Step 6: Finish the branch** (per superpowers:finishing-a-development-branch)

Present merge/PR options to the user.

---

## Self-Review (completed by plan author)

**Spec coverage:** A4/Calibri/1.5/≥8pp → Tasks 6, 8. Cornell A–F (Layout B) → Tasks 6, 7. Coverage map → Task 7 Step 2. Reuse K2 analysis/exhibits → Tasks 3, 4, 7. Rust-first + documented Python exceptions → Tasks 1 (CLAUDE.md log), 2, 5 (Rust) and 3, 4, 6 (justified Python). Visual inventory (reuse + extract 13.1/ABC) → Task 4. Pipeline reproducibility → Tasks 1, 7 (README run order), 8. Quality gates → Task 8. No gaps found.

**Placeholder scan:** Content prose is intentionally authored in Task 7 (the deliverable is prose; the plan specifies exact sections, coverage, constraints, and a worked directive example rather than pre-writing 8 pages). Exhibit rectangles for 13.1/ABC are marked to be set from the `--pages` survey — an inherent runtime measurement, not a skipped detail. No code-step placeholders.

**Type/name consistency:** `parse_blocks` emits `("cue"|"notes", str)`; `group_cornell` consumes them and emits `("cornell", [(cue,notes)])`; `add_cornell_table(doc, rows)` consumes `rows` as `[(cue,notes)]`. `print_page_range(start_print, n_pages)` used consistently in Task 2. Directive grammar `@cue`/`@notes`/`![cap | Sumber](path)` consistent between Tasks 6 and 7.
