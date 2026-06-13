# CLAUDE.md — RMK Pertemuan 10: Statement of Cash Flows

## Project Purpose

Individual deliverable for the S2 (Graduate) course **Pelaporan Keuangan Korporat** (MNK202),
Pertemuan 10. Format: **Cornell Notes** in MS Word. Topic: **Wolk, Dodd & Tearney Ch. 13 —
Statement of Cash Flows**.

The pipeline produces a single Word document:
`output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx`

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
2. **Chapter PDF** (`input/chapter/PKK Pert. 10 - Statement of Cashflow.pdf`) — primary content
3. **Syllabus** (`input/syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf`) — scope alignment
4. **Master prompt / task instructions** — pipeline orchestration

When any conflict arises, resolve it by applying the highest-authority source. Never fabricate data or
figures not present in the chapter PDF.

---

## Rust → Python Fallback Log

Three pipeline stages deviate from the default Rust implementation. Each deviation is justified:

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

---

## Pipeline Stage Map

| Stage | Tool | Module |
|-------|------|--------|
| 1. PDF probe + range detection | Rust | `src/rust/pdf_probe` |
| 2. Text extraction | Python (exception 1) | `src/python/extract_text.py` |
| 3. Exhibit cropping | Python (exception 2) | `src/python/crop_exhibits.py` |
| 4. Diagram generation | Rust | `src/rust/visual_gen` |
| 5. DOCX assembly | Python (exception 3) | `src/python/build_docx.py` |

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
