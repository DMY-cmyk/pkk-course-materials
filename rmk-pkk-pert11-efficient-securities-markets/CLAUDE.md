# CLAUDE.md — RMK Pertemuan 11: Efficient Securities Markets

## Project Purpose

GROUP deliverable for the S2 (Graduate) course **Pelaporan Keuangan Korporat** (MNK202),
Pertemuan 11. Format: **Cornell Notes** in MS Word. Topic: **Efficient Securities Markets**.
Source: **Scott, W. R. (2015). Financial Accounting Theory (7th ed.). Pearson Education Canada —
Chapter 4**.

The pipeline produces a single Word document:
`output/01079_Kelompok 3_RMK Pert. 11.docx`

---

## Group Identity — Kelompok 3 (use verbatim in the RMK header)

| Anggota Kelompok 3 | NIM |
|---|---|
| Odisiana Manek | 122501041 |
| Efri Nurmalinda | 122501049 |
| Prasetya Adhi Surya Gumilang | 122501068 |
| Dzaki Muhammad Yusfian | 122501079 |
| Adinda Putri Dewi | 122501086 |
| Kunthi Talibrata | 122501097 |

---

## Governing Rules (VERBATIM — do not paraphrase, do not deviate)

### Ketentuan Pembuatan RMK

- Kertas A4
- Spasi 1,5
- Font Calibri ukuran 12
- Minimal 8 halaman
- Format MS Word

### Pedoman Cornell Notes — Struktur & Rubrik

**Struktur wajib:**

| Bagian | Keterangan |
|--------|-----------|
| Identitas | Nama, NIM, Mata Kuliah, Pertemuan, Tanggal |
| Bagian A | Kolom Cornell: Cue Column (kiri) + Note Column (kanan) |
| Bagian B | Summary section |
| Bagian C | Analisis kritis |
| Bagian D | Kesimpulan |
| Bagian E | Active Recall (pertanyaan mandiri + jawaban) |
| Bagian F | Daftar Pustaka |

**Rubrik penilaian:**

| Kriteria | Bobot |
|----------|-------|
| Kelengkapan Cornell Notes | 20% |
| Ketepatan Ringkasan | 20% |
| Kedalaman Analisis | 25% |
| Kualitas Kesimpulan | 15% |
| Active Recall | 10% |
| Bahasa Akademik & Format | 10% |

---

## Source-of-Truth Hierarchy

1. **Ketentuan Pembuatan RMK + Pedoman Cornell Notes** (governing rules above) — highest authority
2. **Chapter PDF** (`input/chapter/Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf`) — primary content
3. **Syllabus** (`input/syllabus/Silabus_Pelaporan Keuangan Korporat_25-26.pdf`) — scope alignment
4. **Master prompt / task instructions** — pipeline orchestration

When any conflict arises, resolve it by applying the highest-authority source. Never fabricate data or
figures not present in the chapter PDF.

---

## Rust → Python Fallback Log

Four pipeline stages deviate from the default Rust implementation. Each deviation is justified:

### Exception 1: `src/python/extract_text.py` — uses PyMuPDF

**Justification:** Rust `lopdf`'s `extract_text` returns only page footers on this SAGE-edition PDF.
The embedded fonts lack a ToUnicode CMap, so lopdf cannot map glyph IDs to Unicode code points.
PyMuPDF (MuPDF C engine) resolves glyphs via its own built-in CMap tables and produces full,
well-structured text output. This exception is pre-confirmed by the `reference_wolk_pdf_lopdf_no_text`
memory note recorded during Pertemuan 9.

### Exception 2: `src/python/crop_exhibits.py` — uses PyMuPDF + PIL

**Justification:** Exhibit cropping requires page rasterization at high DPI followed by tight
bounding-box clipping. PyMuPDF exposes `page.get_pixmap(matrix=fitz.Matrix(dpi, dpi))` and PIL
provides `Image.crop()` with sub-pixel precision. Implementing equivalent rasterization in Rust
(via `pdfium-render` or similar) would require vendoring a large C/C++ dependency and re-proving
output fidelity. The Python path is battle-tested from the Pertemuan 9 pipeline.

### Exception 3: `src/python/build_docx.py` — uses python-docx

**Justification:** The exact typographic requirements (Calibri font, 1.5 line spacing, A4 page size,
Cornell two-column table layout, footer PAGE field) are proven to work correctly with `python-docx`
from the prior Pertemuan 9 builder (`rmk-pkk-pert9-income-statement/src/python/build_docx.py`).
Re-implementing this in `docx-rs` (Rust) would require re-proving all typographic output with no
correctness advantage, adding risk at a deadline-sensitive stage.

### Exception 4: `src/python/latex_to_omml.py` + equation step in `build_docx.py` — uses latex2mathml + lxml (+ matplotlib fallback)

**Justification:** Word equations are OMML (Office Math Markup). There is no Rust crate that
produces Word-native OMML; the reproducible route is LaTeX → MathML (`latex2mathml`) → OMML via
Microsoft's shipped `MML2OMML.XSL` stylesheet (applied with `lxml`). If the stylesheet is absent or
a transform fails, that single equation falls back to a 300-DPI `matplotlib` mathtext PNG. Both are
Python-only; no Rust equivalent exists.

---

## Pipeline Stage Map

| Stage | Tool | Module |
|-------|------|--------|
| 1. PDF probe + range detection | Rust | `src/rust/pdf_probe` |
| 2. Text extraction | Python (exception 1) | `src/python/extract_text.py` |
| 3. Exhibit cropping | Python (exception 2) | `src/python/crop_exhibits.py` |
| 4. Diagram generation | Rust | `src/rust/visual_gen` |
| 5. Equation rendering (helper module, invoked during stage 6) | Python (exception 4) | `src/python/latex_to_omml.py` |
| 6. DOCX assembly (renders @eq equations inline via stage-5 module) | Python (exception 3) | `src/python/build_docx.py` |

---

## Critical Rules

1. **Never edit files in `input/`.** They are read-only source artifacts.
2. **Never fabricate figures.** Every numeric claim must trace to the chapter PDF.
3. **Never skip the rubric.** All six Cornell sections (Identitas + A–F) must be present.
4. **Professor-voice only.** Graduate-level academic Indonesian throughout. No undergraduate
   summarization.
5. **Minimum 8 pages.** The build step must verify page count before reporting success.
6. **Gitignored artifacts are regenerable.** `input/`, `extraction/`, and PNG assets are excluded
   from version control; they are reproduced deterministically by running the pipeline.
