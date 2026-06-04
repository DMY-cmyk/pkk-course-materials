# Exhibit Map — Wolk Ch. 13 "Statement of Cash Flows"

Source: `sources/textbook-chapter/Sage_Chapter_13_Kelompok_2.pdf` (23 physical A4 pages; 595×842 pts).
Locations verified visually against 60-dpi page renders (`analysis/page-thumbs/`).
`region` = approximate [top%, bottom%] of page height, full text-column width unless noted. Final crop boxes are confirmed at 200–300 dpi in Phase 3.5.

| ID | Caption | PDF page(s) | Region (approx.) | Render type in PDF | Anchors section |
|---|---|---|---|---|---|
| eq-13-1 | Equation 13.1 — SCFP identity: *transaction credits = transaction debits* | 3 | 40–46% | image (display equation) | 01-scfp-funds-flow |
| exhibit-13-01 | Exhibit 13.1 — Standard Format of the SCFP | 3 + 4 | p3: 72–93% (Sources); p4: 7–22% (Uses) | text-rendered boxed table, **spans 2 pages** | 01-scfp-funds-flow |
| exhibit-13-02 | Exhibit 13.2 — SCF per SFAS No. 95 (Direct Method), Company M, FY2000 | 7 + 8 | p7: 84–93% (title block); p8: 7–75% (table body) | text-rendered table, **spans 2 pages** | 05-direct-vs-indirect |
| exhibit-13-03 | Exhibit 13.3 — Indirect/Reconciliation Method of Presenting Net CFO | 8 + 9 | p8: 76–93%; p9: 7–45% | text-rendered table, **spans 2 pages** (pdftotext garbles columns — crop, don't transcribe) | 05-direct-vs-indirect |
| exhibit-13-04 | Exhibit 13.4 — Comparison of Balance Sheet Changes and Working Capital Adjustments, 3M Company ($000,000) | 10 | 27–46% (incl. source note) | **image** | 06-nonarticulation |
| exhibit-13-05 | Exhibit 13.5 — Premium Allocation Between Operating and Financing Cash Flows (Methods 1–4) | 13 | 7–44% (header text sits on p12 @ ~52%; caption must be re-set with the crop) | **image** | 07-classification-problems |
| exhibit-13-06 | Exhibit 13.6 — Selected Items From WorldCom's SCF ($000,000), 12/31/98–12/31/01 | 16 | 7–24% (incl. Mergent source note; header text on p15 bottom) | **image** | 10-scf-more-than-cfo |
| eq-13-2 | Equation 13.2 — FCF = NOPLAT − investment in operating invested capital | 17 | 53–58% | image (display equation) | 12-free-cash-flow |
| exhibit-13-07 | Exhibit 13.7 — Income Statement and Balance Sheet for ABC Company (2004–2007) | 18 | 8–57% | **image** | 12-free-cash-flow |
| exhibit-13-08 | Exhibit 13.8 — Statement of Cash Flows for ABC Company | 19 | 7–50% (header text on p18 @ ~80%) | **image** | 12-free-cash-flow |
| exhibit-13-09 | Exhibit 13.9 — Statement of Free Cash Flows for ABC Company | 20 | 7–71% (header text on p19 @ ~57%) | **image** | 12-free-cash-flow |
| exhibit-13-10 | Exhibit 13.10 — Computing Free Cash Flow From the SCF for ABC Company | 20 | 72–89% (header @ ~71%) | **image** | 12-free-cash-flow |
| exhibit-13-11 | Exhibit 13.11 — A Comparison of Performance Measures for ABC Company | 21 | 9–25% (header @ ~8%) | **image** | 12-free-cash-flow |

## Pipeline implications (for Phase 3.5)
1. **Page-spanning exhibits (13.1, 13.2, 13.3):** **RESOLVED (Phase 1 decision D5): re-set as native Word tables**, cell-by-cell faithful to the PDF, verified in Stage 1 review. Rationale: the SAGE PDF's own text layout of 13.3 is broken (wrapped "$445", values floated into the margin — confirmed in the Class 2 preview crop), so a faithful crop reproduces a defect, not the exhibit.
2. **Detached headers (13.5, 13.6, 13.8, 13.9):** the caption text sits on the previous page; crop the table body only and supply the caption as a Word caption paragraph — this is required anyway by the caption rule.
3. Render at 240 dpi (A4 @ 240 dpi = 1984×2806 px) → crop → trim whitespace → embed at **6.25 in** (full text column; Phase 1 decision D4).
4. Equations 13.1 and 13.2: **RESOLVED (D7): re-set as centered bold text**, labeled (13.1)/(13.2), noted in manifest.
5. Thumbnails in `analysis/page-thumbs/` (60 dpi) are mapping aids only — never embed them.
