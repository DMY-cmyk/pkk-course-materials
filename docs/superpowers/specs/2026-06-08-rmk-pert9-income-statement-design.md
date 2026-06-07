# Design Spec — RMK Pertemuan 9: "The Income Statement" (Wolk Ch. 12)

**Date:** 2026-06-08
**Deliverable:** `output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx`
**Course:** Pelaporan Keuangan Korporat (MNK202), Pascasarjana STIE YKPN, TA 2025/2026
**Sources (read in full before this spec):**
- Syllabus `03-Course-Admin/Silabus_Pelaporan Keuangan Korporat_25-26.pdf` — confirms Pertemuan IX = "The Income Statement", reading W: 12, summary TT + Group, HW7; homework weight 10%.
- Wolk, Dodd & Rozycki (2017), *Accounting Theory*, 9th ed., Sage — Chapter 12, SAGE Knowledge edition, PDF pages 305–338 (1-based), print pages 337–373.

## Key findings that shaped this design

1. **Chapter structure differs from the master prompt's anticipated scaffold.** Ch. 12 has no "economic concept of income" or "capital maintenance" sections (Ch. 11 territory) and no five-step ASC 606 detail; it DOES have large sections the scaffold did not anticipate: Future Events and Accounting Recognition; Specialized Subjects (development stage enterprises, troubled debt restructuring, early extinguishment of debt, stock options); Income Statement Developments (cash earnings, pro forma/Reg G, G4+1, matrix approaches, retrospective reports, quality of earnings, restatements).
2. **Zero-exhibit chapter (verified programmatically).** The 34 SAGE pages contain 0 figures, 0 tables, 0 exhibits; the only embedded image is the SAGE logo on the title page. The §5 "crop every exhibit" mandate yields an EMPTY inventory. Consequence: no PDF rasterization/crop stage; visuals are honest *reconstructions* labeled "Sumber: diolah dari Wolk et al. (2017)".

## Confirmed decisions (Visual Companion previews shown for each)

| # | Decision | Choice |
|---|----------|--------|
| 1 | Language | Bahasa Indonesia akademik; istilah teknis Inggris dipertahankan italic (K2 Ch. 13 convention) |
| 2 | Section structure | **Option C — Hybrid:** body (II–XII) faithful to the chapter's actual order; framed by Orientasi (I) and Sintesis (XIII) connecting to course themes. Economic income touched only in Orientasi, labeled as Ch. 11 context, never claimed as Ch. 12 content |
| 3 | Visual strategy | **Option D — Hybrid:** 6 reconstructed monochrome diagrams (PNG 300 DPI, max width 14.5 cm) + 4 native Word tables; placed adjacent to the discussing section; captions "Gambar/Tabel N. … \| Sumber: diolah dari Wolk et al. (2017), hlm. X" |
| 4 | Layout/typography | **Option B — concise front matter:** Times New Roman 12pt, A4, 3 cm margins, exact 18pt line spacing, justified; NO separate cover page — compact identity block + rule at top of page 1; headings Roman-numeral bold; sub-headings bold-italic; page numbers bottom-right; figure captions 11pt italic centered below figure, table captions above table |
| 5 | Depth/length | 7,000–9,000 words (~15–18 content pages), K2-grade professorial depth |
| 6 | Rust/Python split | **Option B — Rust core + Python docx assembly** (documented exception per §6) |

## Document structure (14 sections → content/ files)

| File | Section | Chapter coverage |
|------|---------|------------------|
| `00_front_matter.md` | Identity block | Title RMK Pert. 9, MNK202, Dzaki Muhammad Yusfian — NIM 1225 01079, full Wolk Ch. 12 citation |
| `01_orientasi.md` | I. Orientasi | Income statement's place in accounting theory; articulation with balance sheet (Pert. 8); decision usefulness; chapter learning objectives; brief economic-income context flagged as Ch. 11 material |
| `02_definisi_income_elemen.md` | II. Definisi Income dan Elemen-elemennya | Income/net income/comprehensive income definitions; revenues & gains; expenses & losses; ATB 2 → APB St. 4 → SFAC 6 evolution (revenue–expense vs asset–liability approach) |
| `03_pengakuan_pendapatan.md` | III. Pengakuan Pendapatan | Theoretical ideal vs measurability; 4 timing points; point-of-sale norm (ARB 43); industry exceptions; SFAS 32 program; accretion/discovery bases; measurement attributes; Qwest swap example; ASU 2014-09/IFRS 15; SAB 101 & FASB–SEC tension |
| `04_pengakuan_beban_matching.md` | IV. Pengakuan Beban dan Matching | Expense/loss definitions; 3 APB St. 4 categories; matching hierarchy; Thomas on arbitrary allocations; allocation-free accounting; information content despite allocations |
| `05_future_events.md` | V. Future Events dan Pengakuan | One-event vs two-event view; probabilistic nature (SFAS 5); management intent rejection; market values (Beaver); conservatism; future economic conditions; future legal requirements |
| `06_current_operating_vs_all_inclusive.md` | VI. Current Operating vs All-Inclusive | Both camps' arguments; AAA 1936 vs AICPA; APB Op. 9; empirical research (Gonedes; nonoperating items & security prices); big bath theory (Citicorp 1987) |
| `07_comprehensive_income.md` | VII. Comprehensive Income | SFAC 5 proposal; proprietary theory grounding; OCI elements (SFAS 130); three reporting formats & Board preference; dissent & flexibility critique; no EPS on CI |
| `08_seksi_nonoperasi.md` | VIII. Seksi Nonoperasi | Extraordinary items (ARB 43 → APB 9 → APB 30 rigid uniformity, unusual + infrequent, citrus-frost example); accounting changes (3 types; APB 20 → SFAS 154 retrospective); prior period adjustments (APB 9 → SFAS 16) |
| `09_earnings_per_share.md` | IX. Earnings per Share | Summary indicator concept; APB Op. 15 rigid rules; SFAS 128: PEPS elimination, 3% rule elimination, basic vs diluted, reconciliation requirement |
| `10_topik_khusus.md` | X. Topik Khusus Pengukuran Laba | Development stage enterprises (SFAS 7); troubled debt restructuring (SFAS 15/114 debtor–creditor asymmetry); early extinguishment of debt (APB 26/30, SFAS 4); stock options (APB 25, SFAS 123/123R, Black-Scholes, backdating, entity vs proprietary reformat proposal) |
| `11_earnings_management.md` | XI. Earnings Management dan Income Smoothing | Schipper definition; agency motives; meet-or-beat analyst forecasts; classification shifting (McVay, Borden); M&A/buyout evidence; auditor study (Nelson et al.); management compensation ceiling/floor (Healy); discretionary accruals; income smoothing: 3 mechanisms, research problems, random-walk findings |
| `12_perkembangan.md` | XII. Perkembangan Income Statement | Cash earnings (Howell); pro forma & Reg G; G4+1 three-component report & earnings sustainability; matrix approaches (Barker; Glover et al. fact-vs-forecast); retrospective reports (Lundholm); quality of earnings; restatements growth & SAB 99 |
| `13_sintesis.md` | XIII. Sintesis | Relevance vs reliability; economic ideal vs practical measurement; user needs vs preparer discretion; ties to course themes: information asymmetry, contracting/agency, efficient markets, historical cost vs fair value; FASB trajectory (rigid uniformity, asset–liability shift) |
| `14_referensi.md` | XIV. Referensi | Wolk et al. (2017) full citation + any secondary sources actually used |

## Visual inventory (all reconstructions, never claimed as chapter exhibits)

**Diagrams (6) — monochrome, Georgia/TNR-consistent style, PNG 300 DPI, ≤14.5 cm:**
1. Timeline: 4 revenue recognition timing points, point-of-sale emphasized (§III)
2. Matching hierarchy: 3-tier fallback flow (§IV)
3. Future-events issue map: one/two-event, probability, intent, market values, conservatism (§V)
4. Evolution timeline: current operating → all-inclusive → comprehensive income, AAA 1936 → APB 9 1966 → SFAS 130 → ASU 2011 (§VI–VII)
5. Stock-option standards timeline: APB 25 → SFAS 123 (1995 retreat) → SFAS 123R (2004) + IFRS 2 convergence (§X)
6. Earnings-management taxonomy: compensation-driven / classification shifting / income smoothing (3 mechanisms) (§XI)

**Native Word tables (4):**
1. Definition evolution: income, revenue, expense across ATB/APB St. 4/SFAC 6 with orientation column (§II)
2. SFAS 130 three comprehensive-income reporting formats + Board preference + dissent (§VII)
3. Three accounting-change types: treatment under APB 20 vs SFAS 154 (§VIII)
4. EPS: APB 15 vs SFAS 128 (PEPS, 3% rule, basic/diluted, reconciliation) (§IX)

## Repository layout

```
rmk-pkk-pert9-income-statement/
├── README.md                      # run order, exact commands, Rust/Python split rationale
├── Cargo.toml                     # workspace: chapter_locator, text_extract, visual_gen
├── requirements.txt               # python-docx (pinned), pillow if needed
├── input/
│   ├── syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf   # copies, read-only
│   └── textbook/Wolk_-_Accounting_Theory_9th_Ed.pdf
├── src/rust/chapter_locator/      # lopdf+clap+anyhow → extraction/chapter-range.json
├── src/rust/text_extract/         # pdf-extract → extraction/text/*.md + page map + zero-exhibit verification report
├── src/rust/visual_gen/           # svg+resvg → assets/diagrams/*.png (documented matplotlib fallback if TNR font rendering fails on Windows)
├── src/python/build_docx.py       # python-docx assembly (documented exception per §6)
├── src/python/test_build_docx.py  # K2-pattern unit tests
├── extraction/                    # generated, reproducible
├── assets/diagrams/  assets/tables/   # PNGs + table definitions (TOML/JSON)
├── content/                       # 15 authored .md files per table above
├── design/previews/               # archived brainstorm previews
└── output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx
```

Note: master prompt's `pdf_extract` + `asset_crop` crates and `locate_chapter.py`/`crop_assets.py`/`extract_tables.py`/`docx_patch.py` fallbacks are dropped — the zero-exhibit finding removes rasterization/cropping entirely. `content/` file list reconciled to the chapter's actual structure (15 files vs the prompt's anticipated 13).

## Pipeline stages & contracts

1. **chapter_locator** (Rust): scans textbook PDF for chapter title boundaries ("The Income Statement" → "Statement of Cash Flows"); emits `extraction/chapter-range.json` `{start_page, end_page, print_pages}`. Manual ground truth: PDF 305–338 (1-based). Fails loudly if boundaries not found exactly once.
2. **text_extract** (Rust): extracts per-page text for the range; segments by the chapter's headings; emits `extraction/text/NN_<slug>.md` + `extraction/page-map.json` + `extraction/verification-report.md` (image-XObject count per page proving the zero-exhibit claim).
3. **visual_gen** (Rust): 6 diagrams authored as deterministic SVG, rasterized via resvg with system Times New Roman; emits `assets/diagrams/*.png` at 300 DPI. Fallback (documented in README + code comments): matplotlib per K2 `make_diagrams.py` if resvg font shaping proves unreliable.
4. **build_docx.py** (Python): reads `content/*.md` (supports the K2 markdown conventions: bold/italic runs, image directives, citation text) + `assets/`; applies Layout B typography; builds the 4 tables natively from `assets/tables/*.toml`; writes the exactly-named output file.

Determinism: every artifact regenerable `input/ → output/` with no manual steps; no network access; Python deps pinned.

## Error handling

- Rust crates: `anyhow` contexts at every I/O boundary; `thiserror` for domain errors (ChapterNotFound, AmbiguousBoundary, EmptySegment).
- Each stage validates its upstream artifact exists and is well-formed before work; exits non-zero with a precise message otherwise.
- build_docx.py: validates all 15 content files present, all 6 PNGs present and ≥ expected pixel width, output filename matches spec exactly.

## Testing

- `chapter_locator`: unit test on boundary detection logic (synthetic fixture + assertion against ground-truth 305–338 when the real PDF is present).
- `text_extract`: heading segmentation tests on fixture text; verification-report assertions.
- `visual_gen`: PNG count/dimensions/DPI assertions.
- `test_build_docx.py` (K2 pattern): document opens; section count; A4 + 3 cm margins; TNR 12; exact 18pt spacing; 6 inline images; 4 tables; caption presence; exact filename.
- Final §9 self-review checklist before declaring done: graduate depth, completeness vs the chapter-coverage table above, professorial credibility, visual fidelity (all 10 assets placed correctly, legible, within margins), reproducibility, exact filename, attribution.

## Authoring quality bar (content/)

Professorial Bahasa Indonesia prose per the K2 Ch. 13 precedent: every concept gets what-why-significance-connections-tensions treatment; inline citations `(Wolk et al., 2017, hlm. X)` using print pages 337–373; sections end with a forward link to the next section; no undergraduate listing; no fabricated data; course themes (decision usefulness, information asymmetry, efficient markets, historical cost vs fair value, contracting/agency, earnings management) woven through Orientasi, body asides, and Sintesis.
