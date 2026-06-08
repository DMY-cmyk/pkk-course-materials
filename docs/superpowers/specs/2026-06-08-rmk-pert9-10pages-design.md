# Design Spec — RMK Pert. 9 condensed to 10 pages

**Date:** 2026-06-08
**Target:** `rmk-pkk-pert9-income-statement/output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx`
**Builds on:** the bulletized 16-page version (merged commit `3d60aac`).

## Goal

Condense the RMK to **exactly ~10 pages** (hard target) while keeping the main
substance of every retained section at graduate level. Format stays bulleted +
heading-rich + simple language, single 12pt spacing.

## Hard constraints

1. **10 pages.** Iterate (text + visual size) until Word COM reports ≤10 pages
   (10 or just under). If the first pass overshoots, micro-trim and/or shrink the
   4 kept visuals, then rebuild and re-measure.
2. **No references / Daftar Pustaka page.** Remove §XIV entirely from the
   document. The builder must NOT emit `content/14_referensi.md`. Inline citations
   `(Wolk et al., 2017, PDF hlm. N)` remain throughout for attribution; the full
   Wolk citation already sits in the front-matter block.
3. **Keep all remaining sections I–XIII** with their core substance: definitions,
   key standards (ARB/APB/SFAS/SFAC/ASU), the central debate/tension of each
   section, and at least one citation per section.

## Visual curation — keep 4, drop 6

**Keep (still embedded):**
- **Tabel 1** — evolusi definisi income/revenue/expense (§II)
- **Gambar 1** — empat titik pengakuan pendapatan (§III)
- **Gambar 4** — evolusi laba: current operating → all-inclusive → comprehensive income (placed at the §VI/§VII seam)
- **Gambar 6** — taksonomi earnings management (§XI)

**Drop the embed lines for (concepts stay in text; assets remain on disk, just not embedded):**
- Gambar 2 (matching hierarchy, §IV)
- Gambar 3 (future events map, §V)
- Gambar 5 (stock-options timeline, §X)
- Tabel 2 (CI reporting formats, §VII)
- Tabel 3 (accounting changes, §VIII)
- Tabel 4 (EPS, §IX)

## Text budget

Body (sections I–XIII) from ~5,533 → **~3,300 words** (~40% cut). Deeper cuts on
the longest enumerative sections (§X, §XI, §III, §XII ≈ −45%); gentler on the
conceptual core (§II, §VI, §VII, §XIII ≈ −25%). Every section keeps: its `##`
heading, its sub-headings, its key concepts/standards/researchers-of-record, ≥1
citation, and a one-line bridge.

## Builder change

In `src/python/build_docx.py`, the body loop currently skips files starting with
`00_`. Extend it to also skip `14_` so the references section is excluded. No
other builder change unless page-count tuning requires shrinking image width
(currently `Cm(14.5)`; may reduce the 4 kept diagrams toward ~12 cm if needed).

## Execution

1. Edit `content/01…13_*.md`: trim prose to budget; **remove the 6 dropped embed
   lines**; keep the 4 retained embed lines verbatim and in place.
2. Edit `build_docx.py` to skip `14_`.
3. Rebuild; measure pages via Word COM; if > 10, micro-trim longest sections
   and/or shrink the 4 diagrams; rebuild; repeat until ≤10.
4. Re-run tests. Note: `test_build_docx.py::test_six_images_and_four_tables`
   asserts 6 images + 4 tables — UPDATE that test to the new counts (4 of the
   kept set: 1 table embed [Tabel 1] + 3 image embeds [Gambar 1, 4, 6] → 3 inline
   images + 1 table). Re-verify section count is 13 (I–XIII), no XIV.

## Quality bar

Still readable by a graduate student with deep command of the chapter: no concept
silently dropped, only compressed; professorial-but-simple tone; standards and key
researchers preserved; the 4 visuals carry the chapter's spine.

## Out of scope

Diagram/table internal content; pipeline stages other than build_docx; the
front-matter block.
