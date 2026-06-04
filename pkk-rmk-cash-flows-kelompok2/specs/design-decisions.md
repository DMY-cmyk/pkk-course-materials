# Design Decisions Log — RMK Ch. 13 Kelompok 2

| # | Date | Decision | Options considered | Chosen | Preview evidence |
|---|---|---|---|---|---|
| D1 | 2026-06-04 | Output filename ("_ALK" discrepancy flagged per master prompt) | keep `_ALK` verbatim / correct to `_PKK` / drop suffix | **`RMK Chap. 13_Kelompok 2_PKK.docx`** | — (text decision) |
| D2 | 2026-06-04 | RMK body language | Indonesian / English / bilingual headings | **Indonesian**, English technical terms retained | — (text decision) |
| D3 | 2026-06-04 | Class 1 — font template | Calibri 12 pt / Aptos 12 pt | **Calibri 12 pt** (Aptos not installed on build machine → substitution risk) | `previews/font-template/option-{a,b}-*.docx` |
| D4 | 2026-06-04 | Class 2 — exhibit width | full column 6.25″ / inset 4.6″ | **Full column 6.25″** | `previews/exhibit-placement/option-{a,b}-*.docx` (real Exhibit 13.3 crop embedded) |
| D5 | 2026-06-04 | Treatment of text-rendered Exhibits 13.1–13.3 (source layout of 13.3 is broken in the SAGE PDF) | composite-crop faithfully / re-set as native Word tables | **Re-set as Word tables**, cell-by-cell faithful, verified in Stage 1 review; 13.4–13.11 cropped at 240 dpi | broken layout visible in Class 2 previews; clean crop standard shown by Exhibit 13.10 |
| D6 | 2026-06-04 | Class 3 — section layout depth | prose only / prose + compact synthesis tables | **Prose + synthesis tables** in comparison-bearing sections (§5, §7, §12) | `previews/section-layout/option-{a,b}-*.docx` |
| D7 | 2026-06-04 | Equations 13.1, 13.2 | crop as images / re-set as styled text | **Re-set as centered bold text**, labeled (13.1)/(13.2) | consistent with D5 |
| D8 | 2026-06-04 | Tooling substitutions acknowledged | — | tesseract → Claude vision OCR; docx skill → python-docx bridge; poppler via MiKTeX | logged in `analysis/identity-and-context.md` |
