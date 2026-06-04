# CLAUDE.md — RMK Chapter 13: Statement of Cash Flows (Kelompok 2)

## Project Purpose
From-scratch, exhibit-rich **RMK (Ringkasan Materi Kuliah)** of Wolk, Dodd & Rozycki,
*Accounting Theory*, 9th ed., **Chapter 13 "Statement of Cash Flows"** (SAGE, print pp. 375–409)
for the graduate course **Pelaporan Keuangan Korporat (MNK202)** — **Kelompok 2**.

This is NOT a revision of an existing draft (there is none) and NOT a text-only summary.
Every figure/table/exhibit from the chapter must be cropped from the PDF and embedded
inline beside the explanation it illustrates.

## Final Deliverable
`output/RMK Chap. 13_Kelompok 2_PKK.docx`
(Phase 1 decision D1: the originally requested "_ALK" label was confirmed as a course-label error and corrected to "_PKK".)

## THE FIVE FORMAT GATES (lecturer's rules — HARD validation gates)
1. Paper size **A4**
2. Line spacing **1.5**
3. Font **12 pt, Calibri or Aptos**
4. **Minimum 8 pages** (depth instruction — substance, never padding)
5. **Microsoft Word .docx** (one member uploads for the group → document carries all identities)

## EXHIBIT-EMBEDDING REQUIREMENT (first-class, non-negotiable)
All of **Exhibit 13.1 – 13.11** plus equation displays (13.1 SCFP identity, 13.2 FCF definition)
must be embedded, captioned, sized to the A4 text column (6.25″ — D4), and placed adjacent to
the text that explains them. Missing/detached/mis-sized = failure. Treatment (D5/D7):
**13.4–13.11 cropped** from the PDF at 240 dpi (pdftoppm + image crate); **13.1–13.3 re-set as
native Word tables** (their source text layout is broken in the SAGE PDF — verified in Phase 1);
**equations re-set** as centered bold text labeled (13.1)/(13.2).

| Exhibit | Content |
|---|---|
| 13.1 | Standard Format of the SCFP (sources/uses) |
| 13.2 | SCF Direct Method, Company M FY2000 |
| 13.3 | Indirect / Reconciliation Method |
| 13.4 | 3M balance-sheet-change vs working-capital adjustment (2005/2004) |
| 13.5 | Premium Allocation Operating vs Financing (Methods 1–4) |
| 13.6 | Selected Items From WorldCom's SCF (1998–2001) |
| 13.7 | ABC Company income statement & balance sheet |
| 13.8 | SCF for ABC Company |
| 13.9 | Statement of Free Cash Flows for ABC Company |
| 13.10 | Computing FCF From the SCF for ABC Company |
| 13.11 | Comparison of Performance Measures for ABC Company |

## Kelompok 2 Identities (verbatim on cover/identity block)
| NIM | Name |
|---|---|
| 122501039 | Satriyo Nugroho |
| 122501048 | Mario Da Costa |
| 122501067 | Amelda Putri Zhany Wiguna |
| 122501078 | Ahmad Ramadhan |
| 122501084 | Nida Nur Cahyati |
| 122501094 | Priska Putri Parungky |

## Sources (read-only — NEVER edit)
| File | Purpose |
|---|---|
| `sources/textbook-chapter/Sage_Chapter_13_Kelompok_2.pdf` | ONLY content source for the RMK body |
| `sources/assignment/Tugas_RMK_Kelompok.png` | Lecturer's format rules (re-confirm by vision OCR) |
| `sources/group/Kelompok_2_Member_NIMs.jpeg` | Roster — names + NIMs |
| `sources/syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf` | Depth calibration; W-13 session mapping |

## Toolchain (verified 2026-06-04)
- cargo 1.94.0 ✓ · pdftotext/pdftoppm/pdfimages (MiKTeX poppler) ✓ · Python 3.12 ✓
- **tesseract NOT installed** → substitution: Claude native vision (Read tool) for image OCR
- **docx skill (/mnt/skills) not present on this Windows machine** → substitution: python-docx
  `build_docx.py` bridge (proven pattern in repo: `ti4/output/build_docx.py`, `ti5/output/build_docx.py`)
- Both substitutions must be noted in `output/VALIDATION-REPORT.md`

## Workflow Phases (do not skip; explicit user approval between phases)
- Phase 0: Ingestion Audit (3 tiers: chapter+exhibit map → assignment rules → identity+syllabus → synthesis)
- Phase 1: `brainstorming` + Document Visual Companion (3 preview classes: font, exhibit placement, section layout) — flag "_ALK" discrepancy; confirm language (default Indonesian)
- Phase 2: `using-git-worktrees` — worktree `feat/rmk-cash-flows-kelompok2`, Cargo workspace scaffold
- Phase 3: `writing-plans` — section-by-section plan mirroring chapter order
- Phase 3.5: extract & crop all exhibits → `content/figures/` + `manifest.yaml`
- Phase 4: `subagent-driven-development` + TDD-adapted rubrics (RED/GREEN/REFACTOR/COMMIT per section) + two-stage review (Stage 1: completeness/exhibits/format · Stage 2: academic quality/faithfulness)
- Phase 5: `finishing-a-development-branch` — build, validate all gates, VALIDATION-REPORT.md

## Hard Rules
1. **From-scratch completeness** — every Phase 0 concept must have a home.
2. **Every exhibit embedded** — 13.1–13.11 + equations, captioned, in-margin, adjacent.
3. **Five format gates** — A4 · 1.5 · 12 pt Calibri/Aptos · ≥8 pages · .docx.
4. **Faithfulness to Wolk Ch. 13 only** — no fabrication, no outside content sources.
5. **S2 depth, professor-led voice** — explain & interpret, never list/paraphrase.
6. **Single source of truth** — markdown sections + figure manifest → docx; never hand-edit docx.
7. **Never edit `sources/`**; never touch the parent repo's Gr. 3 project files.
8. `cargo test`, `clippy -- -D warnings`, `fmt --check` pass at every commit.
9. **Never proceed past a phase without explicit user approval.**

## Current Status
- [x] Sources confirmed and copied into `sources/` (canonical names)
- [x] Toolchain verified (with the two documented substitutions)
- [x] `.claude/CLAUDE.md` created
- [x] Phase 0: Ingestion Audit — COMPLETE (62 concepts inventoried; 11 exhibits + 2 equations mapped to exact pages/regions; 5 format rules re-confirmed by vision OCR; roster + W-13 syllabus mapping confirmed; synthesis in `analysis/rmk-build-input.md`)
- [x] Phase 1: Brainstorming + Visual Companion — COMPLETE (D1–D8 in `specs/design-decisions.md`; spec approved: `specs/rmk-spec.md`. Calibri 12, Indonesian, full-column 6.25″, `_PKK` filename, prose + synthesis tables)
- [x] Phase 2: Workspace scaffold — COMPLETE (worktree `feat/rmk-cash-flows-kelompok2`; Cargo workspace: shared types + 4 CLI crates; python-docx bridge `tools/build_docx.py` with green `--smoke`; cargo test/clippy/fmt all green)
- [ ] Phase 3: Content plan
- [ ] Phase 3.5: Exhibit extraction & crop
- [ ] Phase 4: Author sections
- [ ] Phase 5: Validate & deliver
