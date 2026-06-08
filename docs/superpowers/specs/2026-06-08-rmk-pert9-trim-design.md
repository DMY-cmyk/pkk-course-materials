# Design Spec — RMK Pert. 9 Prose Trim to ~15 Pages

**Date:** 2026-06-08
**Target document:** `rmk-pkk-pert9-income-statement/output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx`
**Builds on:** `docs/superpowers/specs/2026-06-08-rmk-pert9-income-statement-design.md` (original build, merged to master)

## Goal

Reduce the assembled RMK from ~20–22 pages to **~15 pages total** by condensing
ONLY the prose. All diagrams, tables, headings, front matter, references, and
pipeline code remain unchanged.

## Constraints (hard)

1. **Visuals untouched.** The 6 rendered diagram PNGs and their SVG sources, and
   the 4 native-table TOML definitions, are NOT modified. Their embed directive
   lines in the content markdown stay verbatim and in their current positions.
2. **Structure preserved.** All 14 sections (I–XIV) remain. Every `## ` heading
   and every `### ` sub-heading is kept unchanged. `00_front_matter.md` and
   `14_referensi.md` are not edited.
3. **Only text changes.** Edits touch sentences and paragraphs in
   `content/01…13_*.md` only.
4. **No fabrication, no concept loss.** Every concept, standard reference
   (ARB/APB/SFAS/SFAC/ASU numbers), and named researcher currently present must
   survive. Cuts come from secondary examples, repetition, and over-elaboration —
   not from core reasoning.

## Length target

Body prose 8,967 → **~5,500 words** (~39% reduction). With the fixed ~4 pages of
visuals + front matter + references + heading/spacing overhead, this lands at
~15 pages (aiming ≤ 16).

## Per-section word budgets

Strategy: "protect core, cut dense." Conceptual core sections take a gentler cut;
the longest enumerative sections take a deeper cut.

| File | Section | Now | Target | Tier |
|------|---------|-----|--------|------|
| 01_orientasi.md | I. Orientasi | 476 | 300 | moderate |
| 02_definisi_income_elemen.md | II. Definisi & Elemen | 676 | 470 | **core** |
| 03_pengakuan_pendapatan.md | III. Pengakuan Pendapatan | 802 | 480 | deep |
| 04_pengakuan_beban_matching.md | IV. Matching | 669 | 410 | moderate |
| 05_future_events.md | V. Future Events | 646 | 390 | moderate |
| 06_current_operating_vs_all_inclusive.md | VI. CO vs All-Inclusive | 637 | 440 | **core** |
| 07_comprehensive_income.md | VII. Comprehensive Income | 534 | 380 | **core** |
| 08_seksi_nonoperasi.md | VIII. Nonoperasi | 735 | 410 | deep |
| 09_earnings_per_share.md | IX. EPS | 459 | 320 | moderate |
| 10_topik_khusus.md | X. Topik Khusus | 1175 | 580 | deep |
| 11_earnings_management.md | XI. Earnings Management | 930 | 600 | **core** |
| 12_perkembangan.md | XII. Perkembangan | 798 | 410 | deep |
| 13_sintesis.md | XIII. Sintesis | 430 | 320 | **core** |
| | **TOTAL body** | **8967** | **~5510** | |

Front matter (53) and references (56) unchanged. Budgets are guidance ±10%; the
overall total (~5,500) is the binding figure.

## Editing rules (per file)

- Keep the section heading line and any `### ` sub-heading lines verbatim.
- Keep every embed directive line (`@table(...)` and `![...](...)`) verbatim and
  in the same relative position (after the same anchoring paragraph).
- Preserve every concept name, standard citation, and researcher name already
  present; remove only secondary examples, redundant restatement, and padding.
- Keep at least one `(Wolk et al., 2017, PDF hlm. N)` citation per substantive
  paragraph; adjacent citations of the same page may be consolidated.
- Keep each section's forward-bridge sentence but tighten it.
- Maintain professorial Bahasa Indonesia register; English technical terms stay in
  *italic*; key terms keep **bold** on first appearance.
- Flowing paragraphs (no new bullet lists).

## Execution

1. Edit `content/01…13_*.md` in batches (sub-agent-driven, grouped sensibly), each
   batch honoring the budgets and rules above.
2. Re-run ONLY the assembly stage — `python src/python/build_docx.py` (chapter
   locator, text extraction, and diagram rendering are unchanged and their outputs
   already exist on disk).
3. Re-run the test suite (`cargo test`; `python -m pytest src/python -q`).

## Verification

- Word-count proxy: confirm body prose total is ~5,300–5,800.
- Structural: rebuilt docx still has 14 section headings, 6 inline images, 4 tables,
  citations throughout, correct page setup.
- **Actual page count:** attempt MS Word COM conversion to PDF (Windows) to count
  pages. If Word is unavailable, report the word-budget-based estimate and ask the
  user to confirm in Word.
- If the rendered document exceeds 16 pages, run one more micro-trim pass on the
  longest remaining sections (X, XI, III) and rebuild.

## Out of scope

Diagram/table content or styling; pipeline code; section structure; front matter;
references; the original build's design decisions.
