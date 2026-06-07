# Design Spec — Visuals for Kelompok 2 RMK (Sage Ch. 13)

**Date:** 2026-06-07
**Status:** Approved by user
**Approach:** A — extend the markdown→docx pipeline
**Parent spec:** `2026-06-06-rmk-sage-ch13-design.md` (RMK delivered at commit `16d1047`)

## Goal

Insert 11 explanatory visuals into the RMK docx — 6 authentic exhibits cropped from the chapter PDF + 5 generated monochrome diagrams — sized and placed to support the prose, while preserving the regenerable single-source-of-truth pipeline (`content/rmk-ch13.md` → `output/build_docx.py` → docx).

## User decisions (from brainstorming)

1. **Source:** Both — cropped exhibits AND generated diagrams.
2. **Set:** All 11 candidates (6 exhibits: 13.2, 13.3, 13.4, 13.5, 13.6, 13.9; 5 diagrams: timeline, trichotomy, nonarticulation flow, FCF waterfall, four-measures chart).
3. **Diagram style:** Akademik Monokrom — grayscale only, print-safe (style sample approved in visual companion session `2049-1780809044`).
4. **Pipeline:** Approach A (markdown image directive + parser/renderer extension), over docx post-processing (B) or manual insertion (C).

## Assets — `Kelompok 2 Pasca UTS/assets/`

### Cropped exhibits (6) — `crop_exhibits.py`
- PyMuPDF (`pymupdf` package) renders `Sage Chapter 13.pdf` pages at 300 DPI and crops hardcoded `(page_index, fitz.Rect)` regions.
- Crop rectangles are determined during implementation by rendering candidate pages to images, locating each exhibit visually, and refining coordinates until the crop is clean (whole exhibit incl. its header line; no surrounding body text; no cut rows/columns).
- Outputs: `exhibit-13-2.png`, `exhibit-13-3.png`, `exhibit-13-4.png`, `exhibit-13-5.png`, `exhibit-13-6.png`, `exhibit-13-9.png`.
- Exhibit page locations (from `analysis/chapter-deep-read.md`): 13.2 → PDF pp. 7–8 (may need a two-part crop stitched vertically or the larger single-page portion; implementer decides after viewing), 13.3 → p. 8 (within 8–9), 13.4 → p. 10, 13.5 → p. 13, 13.6 → p. 16, 13.9 → p. 20.
- The source PDF remains READ-ONLY.

### Generated diagrams (5) — `make_diagrams.py`
- matplotlib, grayscale palette only (#111 … #ccc), serif font family, 300 DPI, sized to render legibly at 14.5 cm width.
- Content (all figures/dates from `analysis/chapter-deep-read.md` — no invented data):
  1. `diagram-timeline.png` — 1963 APB Op. 3 (recommended) → 1971 SEC mandatory + APB 19 (SCFP) → 1987 SFAS 95 (SCF) → 2008 FASB/IASB discussion paper.
  2. `diagram-trichotomy.png` — three activity boxes (Operasi / Investasi / Pendanaan) with example flows, plus markers on the disputed items (bunga & dividen diterima → operasi per SFAS 95 though dissenters say investasi; bunga dibayar → operasi though dissenters say pendanaan).
  3. `diagram-nonarticulation.png` — flow: three causes (akuisisi tengah tahun; transaksi nonkas; akun utang gabungan) → balance-sheet Δ ≠ SCF adjustment → consequence for users.
  4. `diagram-fcf-waterfall.png` — CFO $527 → + bunga setelah pajak → − kenaikan kas operasi → + CFI $(277) → FCF $332 (ABC 2005, from Exhibit 13.10 bridge).
  5. `diagram-four-measures.png` — grouped bar chart, ABC 2005–2007: NI $320/312/331; CFO $527/466/434; CFO−CFI $250/157/74; FCF $332/99/80.
- Both scripts are committed and re-runnable; regenerating produces identical assets.

## Markdown grammar extension (one construct)

Image line, full-line form, placed immediately after the paragraph it supports:

```
![Gambar N. <judul Indonesia> | Sumber: <attribution>](../assets/<file>.png)
```

- Parser: a line matching `!\[(.+?)\]\((.+?)\)` becomes an `("image", caption_text, path)` block; `caption_text` splits on `" | "` into title and source line (source optional).
- Path is relative to `content/`.
- Grammar otherwise unchanged (no tables, no `###`, no nesting, no inline images).

## Rendering (build_docx.py)

- Picture: centered, width 14.5 cm (content width is 15 cm on A4 with 3 cm margins), aspect preserved (python-docx scales height automatically). Tall exhibits flow to the next page naturally — acceptable.
- Caption below the picture, centered, 11 pt, Times New Roman:
  - Line 1: bold "Gambar N." prefix + regular title text.
  - Line 2 (when source present): italic source attribution.
- Spacing: 6 pt after picture paragraph, 12 pt after caption (breathing room before next body paragraph).
- TDD: new unit tests for (a) image-line parsing into the `image` block with path and caption, (b) caption split with and without the `| Sumber:` part; existing 5 tests keep passing.

## Placement map (document order defines Gambar numbering)

| # | Asset | Insert after the paragraph about… | RMK section |
|---|---|---|---|
| 1 | diagram-timeline.png | staged history APB 3 → SEC → APB 19 (→ SFAS 95) | II |
| 2 | diagram-trichotomy.png | the three-activity trichotomy + dissent | IV |
| 3 | exhibit-13-2.png | direct-method walkthrough (Company M) | V |
| 4 | exhibit-13-3.png | indirect reconciliation ($445/$605) | V |
| 5 | exhibit-13-4.png | 3M nonarticulation case | VI |
| 6 | diagram-nonarticulation.png | the three causes of nonarticulation | VI |
| 7 | exhibit-13-5.png | the four bond-premium methods | VII |
| 8 | exhibit-13-6.png | the WorldCom story | VIII |
| 9 | exhibit-13-9.png | the FCF build-up (NOPLAT → FCF) | IX |
| 10 | diagram-fcf-waterfall.png | the CFO→FCF bridge (Exhibit 13.10 narration) | IX |
| 11 | diagram-four-measures.png | the four-measures comparison | IX |

Caption sources: exhibits → "Sumber: Wolk, Dodd & Rozycki (2017), Exhibit 13.x, PDF hlm. N." Generated diagrams → "Sumber: diolah dari Wolk, Dodd & Rozycki (2017), PDF hlm. N."

## Quality gates

1. **Crop inspection** — every cropped PNG viewed (Read tool) and accepted before wiring into the markdown: whole exhibit, clean edges, legible at target width.
2. **Diagram fidelity** — every number/date in generated diagrams cross-checked against `chapter-deep-read.md`.
3. **Tests green** — old 5 + new image-parsing tests.
4. **Docx integrity** — rebuilt docx reopened programmatically: exactly 11 inline images; 11 "Gambar N." caption lines numbered 1–11 in order; no literal `![` text leaking into paragraphs.
5. **verification-before-completion** — build runs clean; user does the final visual check in Word (page count will grow beyond the original 15–25 estimate; that is expected and accepted).

## Out of scope

- No changes to the RMK prose beyond inserting image lines.
- No re-cropping of the ringkasan PDF's tables (the chapter PDF is the authentic source).
- No color styles (monochrome approved).
- No new analysis documents.
