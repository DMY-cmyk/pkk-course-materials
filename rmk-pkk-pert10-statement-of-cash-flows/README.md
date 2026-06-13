# RMK Pertemuan 10 — Statement of Cash Flows

**Course:** Pelaporan Keuangan Korporat (MNK202) — S2  
**Author:** Dzaki Muhammad Yusfian (NIM 1225 01079)  
**Source:** Wolk, Dodd & Rozycki, Ch. 13 — Statement of Cash Flows  
**Output:** `output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx`

---

## Prerequisites

| Dependency | Version / Notes |
|-----------|----------------|
| Rust | 1.94 or later (`rustup update stable`) |
| Python | 3.12 |
| Python packages | `pip install -r requirements.txt` |
| Calibri font | Must be installed as a system font (included with Microsoft Office / Windows) |

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

---

## Deterministic Run Order

Run each stage in sequence from the project root:

```powershell
# Stage 1 — PDF probe: detect chapter page range, emit verification report
cargo run --release -p pdf_probe
# Outputs: extraction/chapter-range.json, extraction/verification-report.md

# Stage 2 — Text extraction (Python exception: PyMuPDF, see CLAUDE.md)
python src/python/extract_text.py
# Outputs: extraction/text/*.md, extraction/page-map.json

# Stage 3 — Exhibit cropping (Python exception: PyMuPDF + PIL, see CLAUDE.md)
python src/python/crop_exhibits.py
# Outputs: assets/exhibits/*.png

# Stage 4 — Diagram generation
cargo run --release -p visual_gen
# Outputs: assets/diagrams/*.png

# Stage 5 — DOCX assembly (Python exception: python-docx, see CLAUDE.md)
python src/python/build_docx.py
# Outputs: output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx
```

---

## Rust / Python Split

| Module | Language | Reason |
|--------|----------|--------|
| `src/rust/pdf_probe` | Rust | Fast, zero-dependency page-range detection and verification |
| `src/python/extract_text.py` | Python (exception) | lopdf returns only footers on this SAGE PDF (no ToUnicode CMap); PyMuPDF resolves glyphs correctly |
| `src/python/crop_exhibits.py` | Python (exception) | Page rasterization + tight PIL clipping; battle-tested from Pert. 9 pipeline |
| `src/rust/visual_gen` | Rust | SVG/PNG diagram generation; deterministic, no runtime dependencies |
| `src/python/build_docx.py` | Python (exception) | Calibri/1.5-spacing/A4/Cornell table/footer-PAGE proven in python-docx from Pert. 9; re-proving in docx-rs adds risk |

Full justification for each exception: see `CLAUDE.md § Rust → Python Fallback Log`.

---

## Tests

```powershell
# Rust unit tests (all crates)
cargo test

# Python unit tests
python -m pytest src/python -q
```

---

## Output Specification

The generated DOCX must satisfy all Ketentuan Pembuatan RMK rules:

- Paper: A4
- Line spacing: 1.5
- Font: Calibri 12 pt
- Minimum page count: 8
- Format: MS Word (.docx)

Cornell structure enforced: Identitas + Bagian A (Cue/Note columns) + Bagian B (Summary) +
Bagian C (Analisis Kritis) + Bagian D (Kesimpulan) + Bagian E (Active Recall) + Bagian F (Daftar Pustaka).

---

## Directory Layout

```
rmk-pkk-pert10-statement-of-cash-flows/
├── input/                  # READ-ONLY — gitignored
│   ├── chapter/            # PKK Pert. 10 - Statement of Cashflow.pdf
│   └── syllabus/           # Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf
├── extraction/             # Generated — gitignored
│   ├── text/               # Per-page markdown from extract_text.py
│   ├── page-map.json
│   ├── chapter-range.json
│   └── verification-report.md
├── assets/
│   ├── diagrams/
│   │   └── svg/            # Source SVG files (tracked)
│   └── exhibits/           # Cropped PNG exhibits — gitignored
├── content/                # Authored Cornell A–F markdown
├── src/
│   ├── rust/
│   │   ├── pdf_probe/
│   │   └── visual_gen/
│   └── python/
│       ├── extract_text.py
│       ├── crop_exhibits.py
│       └── build_docx.py
├── output/                 # Final DOCX
├── Cargo.toml
├── requirements.txt
├── CLAUDE.md
└── README.md
```
