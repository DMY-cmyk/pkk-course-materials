# Design Spec — RMK Pertemuan 10: "Statement of Cash Flows" (Individual / Dzaki)

**Date:** 2026-06-13
**Status:** Approved by user
**Course:** Pelaporan Keuangan Korporat (MNK202), Pascasarjana STIE YKPN, TA 2025/2026
**Author of deliverable:** Dzaki Muhammad Yusfian — NIM 1225 01079

## Goal

Produce one graded individual academic deliverable — a Microsoft Word `.docx`
**RMK (Ringkasan Materi Kuliah)** of Wolk, Dodd & Rozycki (2017), *Accounting
Theory*, 9th ed., **Ch. 13 "Statement of Cash Flows"** — written at graduate
(professor) depth, in formal academic Bahasa Indonesia with glossed English
technical terms, fully conforming to the **Cornell Notes pedoman** and the
**Ketentuan Pembuatan RMK**.

## Source-of-truth hierarchy

1. `Ketentuan Pembuatan RMK.png` + `Pedoman Penyusunan Resume Cornell Notes.pdf` — format & structure
2. `PKK Pert. 10 - Statement of Cashflow.pdf` — content (the chapter)
3. `Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf` — scope & identity
4. The master prompt — workflow & technology

### Source files (read-only — never edited)

| File | Role |
|---|---|
| `PKK Pert. 10 - Statement of Cashflow.pdf` | Primary source. **Confirmed identical SAGE Knowledge export** of Wolk Ch.13 "Statement of Cash Flows", print pp. 375–409, DOI …n13 — i.e. the same chapter the Kelompok 2 deliverable was built from. |
| `Ketentuan Pembuatan RMK.png` | Mechanical format rules (read by OCR/vision). |
| `Pedoman Penyusunan Resume Cornell Notes.pdf` | Cornell structure (Identitas + Bagian A–F) and grading rubric. |
| `rmk-pkk-pert9-income-statement/input/syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf` | Syllabus (scope, identity, dosen/tanggal). |

## Governing rules (verbatim)

**Ketentuan Pembuatan RMK** (marked *Pribadi/Individual*):
1. Ukuran kertas **A4**.
2. Jarak antar baris **1,5 spasi**.
3. Font size **12, Calibri atau Aptos**.
4. **Minimal 8 halaman**.
5. Dibikin dalam format **MS Word**.

→ **Font decision: Calibri** (not Aptos). Aptos ships only with Office 2023+ and
is not guaranteed in python-docx or on the grader's machine; Calibri is universal.
The ketentuan permits either.

**Cornell pedoman** — structure: *Identitas Resume* + *Bagian A–F*. Rubric:
Kelengkapan Cornell Notes 20% · Ketepatan Ringkasan 20% · Kedalaman Analisis 25% ·
Kualitas Kesimpulan 15% · Active Recall 10% · Bahasa Akademik & Format 10%.

## Deliverable

`rmk-pkk-pert10-statement-of-cash-flows/output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx`

- **Language:** formal academic Bahasa Indonesia; English technical terms in *italics*, glossed on first use.
- **Voice:** graduate/professor-level analysis ("what / why / how / how-it-connects"), never undergraduate bullet summarization.
- **Typography:** A4, Calibri 12, 1.5 line spacing, justified body, page numbers bottom-right, **≥ 8 pages**.

## Document structure (Cornell A–F)

- **Identitas Resume** — Mata Kuliah, Topik (Statement of Cash Flows), Pertemuan 10,
  Dosen Pengampu & Tanggal (read from syllabus; clearly-marked placeholder if absent),
  Nama (Dzaki Muhammad Yusfian), NIM (1225 01079), Program Studi (Pascasarjana — Magister Akuntansi/Manajemen).
- **Bagian A — Cornell Notes** — rendered as **Layout B** (user-selected):
  a two-column *Kata Kunci/Pertanyaan (Cue)* | *Catatan Materi (Notes)* table for the
  prose; **each exhibit breaks out to full page width** immediately after the row that
  discusses it, with a caption. Left column carries active study cues (key terms,
  conceptual questions, relationships); right column carries definitions, theory,
  models, worked examples.
- **Bagian B — Ringkasan** — 1–2 paragraphs, own words, ≤ 15–20% of source length.
- **Bagian C — Refleksi & Analisis Akademik** — answers all five reflection questions
  (pemahaman, pentingnya, penerapan dunia nyata, hubungan antar-mata-kuliah,
  kelebihan & keterbatasan teori). Analytical, not descriptive — the A/B differentiator.
- **Bagian D — Kesimpulan Akademik** — 150–250 words (inti, manfaat, implikasi praktis, kontribusi).
- **Bagian E — Review Mandiri (Active Recall)** — ≥ 5 self-test questions.
- **Bagian F — Referensi Akademik** — APA 7th. Minimum:
  `Wolk, H. I., Dodd, J. L., & Rozycki, J. J. (2017). Accounting theory: Conceptual issues in a political and economic environment (9th ed.). SAGE Publications.`
  plus the syllabus.

## Mandatory coverage map (Bagian A/B/C as relevant)

SCFP (APB Opinion No. 19; sources/uses; fund-balance definitions; all-inclusive
approach) → motivation for SCF (funds = cash; net-working-capital weakness; SFAS
No. 95, 1987) → objectives (SFAC No. 1 & No. 5; six benefits; quality of income;
financial flexibility & liquidity) → structure (operating/investing/financing
**trichotomy**; cash & cash equivalents; **direct vs indirect**; noncash
disclosure) → **nonarticulation** (Bahnson, Miller & Budge; 3M) → classification
problems (Nurnberg; interest/dividends; proprietary vs entity theory; IAS 7) →
premium/discount on bonds (**four allocation methods**, Vent/Cowling/Sevalstad;
SFAS No. 34; leases; SFAS No. 104) → analytical usefulness (**Ingram & Lee**) →
classification manipulation (**Tyco**; Ford/GM/Harley-Davidson; **Navistar**;
**WorldCom** CFO–CFI) → user cash-flow needs (Buffett; NPV) → **Free Cash Flow**
(`FCF = NOPLAT − investment in operating invested capital`; ABC Company) →
improving the SCF (Broome's three recommendations; authors' position).

Every technical term glossed in plain language on first use. No fabrication — if
the chapter does not say it, the RMK does not either.

## Content sourcing

Reuse the **citation-identical** Kelompok 2 Ch.13 analysis as the base:
`Kelompok 2 Pasca UTS/analysis/{chapter-deep-read,gap-analysis,coverage-audit}.md`
and `content/rmk-ch13.md`. **All prose is re-authored fresh** in Dzaki's individual
professor-voice and **restructured into Cornell A–F** (the K2 doc is a flowing
group RMK, not Cornell). Every figure and citation re-verified against the assigned
PDF.

## Visual inventory (exhibits beside their explanation)

- **Reuse** K2's already-cropped exhibits: `exhibit-13-2, 13-3, 13-4, 13-5, 13-6, 13-9`
  and its 5 reconstructed diagrams (trichotomy, nonarticulation, fcf-waterfall,
  four-measures, timeline).
- **Extract** any additional chapter exhibits the coverage map needs that K2 did not
  crop (candidates: **13.1 SCFP format**, the **ABC Company / FCF** tables, the
  **premium-allocation** illustration). Final inventory is locked during execution by
  auditing the PDF page-by-page.
- Each asset cropped tightly (no page headers/footers), resized to page width without
  distortion, captioned (e.g. *"Exhibit 13.8 — Statement of Cash Flows for ABC Company.
  Sumber: Wolk et al. (2017), hlm. N"*). Never paste an uncropped page; never overflow margins.

## Pipeline (Rust-first; documented Python exceptions — same split as Pert. 9)

| Stage | Lang | Tool | Why |
|---|---|---|---|
| Locate chapter | **Rust** | `chapter_locator` (lopdf) | Confirm chapter page range via running-footer markers. |
| Extract text | **Python** | `extract_text.py` (PyMuPDF) | **Documented exception** — this SAGE PDF's embedded fonts carry no ToUnicode CMap, so lopdf returns only footers; PyMuPDF extracts full text. |
| Crop exhibits | **Python** | `crop_exhibits.py` (PyMuPDF) | **Documented exception** — reuse K2 raster/crop script; PyMuPDF rasterizes pages for tight cropping. |
| Render diagrams | **Rust** | `visual_gen` (resvg) | Rasterize authored SVG diagrams to 300-DPI PNG with system fonts. |
| Assemble docx | **Python** | `build_docx.py` (python-docx) | **Documented exception** — exact A4 / Calibri 12 / 1.5-spacing / Cornell two-column tables / full-width captioned exhibits / page-field footer proven in prior builders. |

Reproducible: re-running `input/` → `output/` regenerates the identical `.docx`.
Every Python use is logged as a justified exception in the project `CLAUDE.md`/`README.md`.

## Workspace

New folder `rmk-pkk-pert10-statement-of-cash-flows/` mirroring the Pert. 9 layout:

```
rmk-pkk-pert10-statement-of-cash-flows/
├── CLAUDE.md            # standing instructions + Rust→Python fallback log
├── README.md            # run order
├── Cargo.toml           # Rust workspace (chapter_locator, visual_gen)
├── requirements.txt     # python-docx, PyMuPDF
├── input/               # source PDF + syllabus (gitignored)
├── extraction/          # text/*.md, page-map.json, verification-report.md (gitignored)
├── assets/              # cropped exhibits + reconstructed diagrams (+ svg/)
├── content/             # 00_identitas.md, A–F section markdown (source of truth)
├── src/rust/{chapter_locator,visual_gen}/
├── src/python/{extract_text,crop_exhibits,build_docx}.py (+ tests)
└── output/01079_Dzaki Muhammad Yusfian_RMK Pert. 10.docx
```

Built on a git worktree per the Superpowers workflow (Phase 2).

## Process (execution order)

1. Scaffold workspace + worktree.
2. Rust `chapter_locator` → confirm page range; PyMuPDF `extract_text` → text + verification report.
3. Audit exhibit inventory against the PDF; reuse K2 crops, extract missing.
4. Author Cornell A–F content markdown (fresh prose, professor-voice, glossed terms).
5. Render diagrams (Rust `visual_gen`); finalize cropped exhibits.
6. Build docx (python-docx) — Calibri 12 / 1.5 / A4 / Cornell two-column / full-width exhibits.
7. Quality gates.

## Quality gates

- **Coverage audit** — every coverage-map concept, each learning objective, and each
  embedded exhibit checked against the RMK.
- **Two-stage review** — (1) content fidelity: no fabrication, refs/exhibit numbers
  correct; (2) language/voice/format: graduate register, consistent terminology,
  Cornell A–F complete, rubric-aligned.
- **verification-before-completion** — docx builds without error, opens, **≥ 8 pages**,
  Calibri / 1.5-spacing / A4 confirmed, Bagian B ≤ 15–20% length, Kesimpulan 150–250
  words, APA-7 references complete, filename exact — all confirmed before claiming done.

## Out of scope

- No PPT/slide deck.
- No edits to the source PDF, the Kelompok 2 deliverable, or any other course work.
- No fabricated content, statistics, citations, or exhibits.
