# RMK Pertemuan 9 — *The Income Statement* (Wolk Ch. 12)

Reproducible pipeline that builds the graduate course-summary deliverable
**`output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx`** — an in-depth,
professor-voice Ringkasan Materi Kuliah (RMK) of Wolk, Dodd & Rozycki (2017),
*Accounting Theory*, 9th ed., **Chapter 12, "The Income Statement"**, for the
course Pelaporan Keuangan Korporat (MNK202), Pascasarjana STIE YKPN.

Author: Dzaki Muhammad Yusfian — NIM 1225 01079.

## What it produces

A ~9,000-word Word document (Times New Roman 12pt, A4, 3 cm margins, exact 18pt
line spacing, justified) in 14 sections (I. Orientasi … XIV. Referensi), with
**6 reconstructed monochrome diagrams** and **4 native Word tables** placed beside
the prose they support. Front matter is a concise centred block + rule (no cover
page). Page numbers sit bottom-right.

## Prerequisites

- **Rust** 1.94+ (`cargo`) — for the chapter locator and the SVG rasterizer.
- **Python** 3.12+ — `pip install -r requirements.txt` (python-docx 1.2.0, PyMuPDF 1.27.1).
- The two source PDFs in `input/` (already copied here, gitignored):
  - `input/textbook/Wolk_-_Accounting_Theory_9th_Ed.pdf`
  - `input/syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf`
- A system **Times New Roman** font (Windows: present by default) — the diagrams render with it.

## Run order (deterministic: `input/` → `output/`)

From this directory, run the four stages in order:

```powershell
cargo run --release -p chapter_locator   # -> extraction/chapter-range.json (pages 305-338)
python src/python/extract_text.py         # -> extraction/text/*.md, page-map.json, verification-report.md
cargo run --release -p visual_gen         # -> assets/diagrams/*.png (6 diagrams, 1712 px wide)
python src/python/build_docx.py           # -> output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx
```

Re-running from scratch regenerates every intermediate and the final document with
no manual steps. `extraction/`, `assets/diagrams/*.png`, `input/`, and `target/`
are gitignored (all regenerable); the authored `content/*.md`, `assets/diagrams/svg/*.svg`,
`assets/tables/*.toml`, source code, and the final `.docx` are tracked.

## Tests

```powershell
cargo test                                # chapter_locator (4) + visual_gen (1)
python -m pytest src/python -q            # extract_text (4) + build_docx (8)
```

## Pipeline stages & the Rust/Python split

The project spec mandates **Rust first, Python only as a documented exception**.
Two of four stages are Rust; the two Python stages are justified exceptions:

| Stage | Lang | Crate / script | Why |
|-------|------|----------------|-----|
| Locate chapter | **Rust** | `src/rust/chapter_locator` (lopdf) | Finds Ch. 12 bounds via unique running-footer markers (`Page 2 of 34` / `Page 2 of 31`) + a title-page offset → `chapter-range.json` (pages **305–338**). |
| Extract text | **Python** | `src/python/extract_text.py` (PyMuPDF) | **Documented exception.** Rust `lopdf.extract_text` returns only the page footer (~12 chars) on this PDF — its embedded fonts carry no ToUnicode CMap, so the body is unreadable via lopdf. PyMuPDF extracts the full text cleanly. The spec explicitly names PyMuPDF as the fallback for precise extraction where Rust falls short. This stage also writes a zero-exhibit **verification report**. |
| Render diagrams | **Rust** | `src/rust/visual_gen` (resvg) | Rasterizes the 6 authored SVGs in `assets/diagrams/svg/` to 300-DPI PNG (1712 px = 14.5 cm), using system fonts. |
| Assemble document | **Python** | `src/python/build_docx.py` (python-docx) | **Documented exception.** The exact typography (A4 / 3 cm / exact-18pt spacing / hanging-indent captions / native captioned tables / footer PAGE field) is proven in the project's prior python-docx builders; docx-rs would require re-proving all of it. Styling layer adapted from the Kelompok 2 RMK Ch. 13 builder. |

## Visual-fidelity policy (zero-exhibit chapter)

This SAGE-edition chapter contains **no figures, tables, or exhibits** — the only
embedded image in its 34 pages is the SAGE logo on the title page (page 305). This
is proven each run in `extraction/verification-report.md` (image-XObject count per
page). The §5 "crop every exhibit" mandate therefore yields an empty inventory, so
all 10 document visuals are honest **reconstructions** of the chapter's conceptual
structure, every one captioned "Sumber: diolah dari Wolk et al. (2017)". Nothing is
claimed to be a chapter exhibit; no data is fabricated.

## Citation convention

Inline citations read `(Wolk et al., 2017, PDF hlm. N)`, where **N is the chapter-
internal "Page N of 34" number** printed on each SAGE page (PDF page − 304). These
are verifiable against the file in hand. The Referensi section additionally lists
the print-page range (337–373).

## Layout

`content/00_front_matter.md` is the centred identity block. `content/01…14_*.md`
are the section prose; the builder reads them in filename order, resolving
`![caption](relpath)` image directives and `@table(relpath)` table directives
relative to `content/`. Diagram sources are `assets/diagrams/svg/*.svg`; table
definitions are `assets/tables/*.toml`.
