# RMK Build Input — Phase 0 Synthesis

Inputs: `chapter13-concept-inventory.md` (62 concepts C-01…C-62) · `exhibit-map.md` (11 exhibits + 2 equations) · `assignment-rules.md` (5 hard gates + identity rule) · `identity-and-context.md`.

## Section plan seed (mirrors the chapter's own order — 15 sections + cover)

| § | id | Working title (ID) | Concepts owned | Exhibits anchored |
|---|---|---|---|---|
| — | 00-cover | Halaman identitas (course, chapter, all 6 members + NIMs) | — | — |
| 0 | 00-pendahuluan | Pendahuluan: Kas, Bukan Laba, yang Membayar Tagihan | C-01, C-02, C-03 | — |
| 1 | 01-scfp-funds-flow | Statement of Changes in Financial Position (SCFP) dan Pendahulunya | C-04…C-10 | eq-13-1, exhibit-13-01 |
| 2 | 02-motivation-scf | Motivasi Menuju Laporan Arus Kas | C-11, C-12 | — |
| 3 | 03-objectives | Tujuan Pelaporan Keuangan dan Tujuan SCF | C-13…C-20 | — |
| 4 | 04-structure-trichotomy | Struktur SCF: Trikotomi Operasi–Investasi–Pendanaan | C-21…C-24 | — |
| 5 | 05-direct-vs-indirect | Metode Langsung vs Metode Tidak Langsung | C-25…C-28 | exhibit-13-02, exhibit-13-03 |
| 6 | 06-nonarticulation | Masalah Nonartikulasi | C-29…C-34 | exhibit-13-04 |
| 7 | 07-classification-problems | Masalah Klasifikasi SFAS No. 95 | C-35…C-41 | exhibit-13-05 |
| 8 | 08-analytical-usefulness | Kegunaan Analitis SCF (Ingram & Lee) | C-42 | — |
| 9 | 09-misclassification | Misklasifikasi dan Manipulasi Klasifikasi | C-43…C-46 | — |
| 10 | 10-scf-more-than-cfo | SCF Lebih dari Sekadar CFO: Kasus WorldCom | C-47, C-48 | exhibit-13-06 |
| 11 | 11-user-needs | Kebutuhan Arus Kas Berbagai Pengguna | C-49, C-50 | — |
| 12 | 12-free-cash-flow | Free Cash Flow dan Contoh ABC Company | C-51…C-55 | eq-13-2, exhibit-13-07…13-11 |
| 13 | 13-research | Riset Arus Kas dan Arus Dana | C-56…C-58 | — |
| 14 | 14-improving-scf | Memperbaiki SCF + Sintesis Penutup | C-59…C-62 | — |

Coverage check: C-01…C-62 all assigned, exactly once each (C-62 Summary folded into §14 synthesis). Exhibits 13.1–13.11 + both equations all anchored. ✔

## Weighting toward the ≥8-page gate (depth, not padding)
- Heaviest sections (≈1–1.5 pp each): §1 (SCFP), §5 (direct/indirect), §6 (nonarticulation), §7 (classification), §12 (FCF — five exhibits, the chapter's analytical climax).
- Medium (≈0.5–0.75 pp): §0, §3, §9, §10, §14.
- Light (≈0.3–0.5 pp): §2, §4, §8, §11, §13.
- Eleven embedded exhibits at ~5.8-in width contribute substantial vertical space; prose must still independently carry S2 depth.

## DRY shared fragments (`content/_shared/`)
- `activity-classification.md` — the operating/investing/financing definitions (used by §4, §5, §7, §9).
- `indirect-method-logic.md` — the accrual→cash adjustment logic (used by §5, §6, §14).

## Open decisions carried into Phase 1 (brainstorming + Visual Companion)
1. **"_ALK" filename discrepancy** — confirm `RMK Chap. 13_Kelompok 2_ALK.docx` verbatim vs corrected label (course is PKK/MNK202).
2. **Language** — Indonesian by default (course language), English technical terms retained (SCF, FCF, NOPLAT, nonarticulation…).
3. **Class 1** — Calibri 12 pt vs Aptos 12 pt template.
4. **Class 2** — exhibit width: full text column vs inset+caption; also resolves the page-spanning exhibit treatment (composite crop vs native re-set for 13.1–13.3).
5. **Class 3** — section layout: prose+exhibit read-through vs prose+compact summary table.
6. Acknowledge Rust-default tooling + two documented substitutions (vision OCR; python-docx bridge).
