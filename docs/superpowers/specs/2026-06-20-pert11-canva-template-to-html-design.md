# Design — Pert. 11 Canva Template PDF → Self-Contained HTML Slide Deck

*Date: 2026-06-20*
*Topic: Convert `Presentation Template Pert. 11 Canva.pdf` (10 pages) into a browser-deliverable, self-contained HTML slide show, preserving content and design exactly.*

## Goal

Turn `Presentation Template Pert. 11 Canva.pdf` (10 pages, 1440×810, 16:9) into a single,
self-contained, offline-capable HTML slide presentation that is **deliverable as-is** and
**does not break any content or design** present in the source PDF.

This reuses the proven, fidelity-tested pipeline already built for the 18-page deck
(`Presentasi PKK Pert. 11 - Kelompok 3.pdf` → `presentasi-pert11.html`). See the prior design:
`docs/superpowers/specs/2026-06-19-pert11-pdf-to-html-slides-design.md`.

## Hard Requirements

1. **Fidelity is paramount.** Every slide must render visually identical to the source PDF page.
2. **Self-contained.** One `.html` file, double-click to open, works fully offline (no fonts, CDNs, network).
3. **No fabrication / no edits to source content.** The PDF is the single source of truth.
4. The original PDF is **never modified**.
5. **The existing `presentasi-pert11.html` (18-page deck) is never overwritten or regressed.**

## Key Findings (already established + re-confirmed for this PDF)

- `Presentation Template Pert. 11 Canva.pdf`: **10 pages, each 1440×810 pt (16:9)** — confirmed via PyMuPDF probe.
- Render mode `text_as_path=True` → glyphs become vector **paths** (no font dependency) +
  embedded raster images → renders pixel-identical in every browser. Trade-off (accepted, same as
  prior deck): on-slide text is not selectable/copyable.
- The existing template (`analysis/pert11_shell_template.html`) and controls
  (`analysis/pert11_controls.js`) are deck-size-agnostic — slide count is injected at build time.

## Architecture

### Change 1 — Generalize the build script (`analysis/build_pert11_html.py`)
Replace the three hardcoded module constants (`SOURCE_PDF`, `OUTPUT`, `EXPECTED_PAGES`) with
**CLI parameters** so one tested codebase serves both decks:

- `--source` (path to source PDF, relative to project root)
- `--output` (output HTML filename, relative to project root)
- `--pages` (expected page count; build aborts if the PDF page count differs)

Backward compatibility: when invoked with no arguments, default to the existing 18-page deck
values so the prior build path is unchanged. All current logic (SVG rendering, id namespacing,
template assembly, determinism) is preserved verbatim — only the inputs become parameters.

### Reused unchanged
- **`analysis/pert11_shell_template.html`** — 16:9 stage, letterboxing, active-slide toggle.
- **`analysis/pert11_controls.js`** — keyboard nav, click-zones, fullscreen, counter, progress
  bar, thumbnail overview. Slide count injected via `{{SLIDE_COUNT}}`.
- **`namespace_svg_ids`** — prefixes per-page SVG ids (`p{NN}_`) to avoid collisions when many
  SVGs are inlined into one document.

## Data Flow

```
Presentation Template Pert. 11 Canva.pdf  (10 pages)
        │  PyMuPDF, page-by-page, text_as_path=True
        ▼
   10 × inline <svg> (vector, faithful)  →  namespaced ids
        │  assembled into shell template (slide count = 10)
        ▼
   presentation-template-pert11.html  (single self-contained file)
        │  open in browser
        ▼
   Keyboard / click / fullscreen / overview navigation
```

## Invocation

```
python analysis/build_pert11_html.py \
  --source "Presentation Template Pert. 11 Canva.pdf" \
  --output "presentation-template-pert11.html" \
  --pages 10
```

Deterministic and safe to re-run (byte-stable output; no timestamps/random ids).

## Error Handling

- Source PDF missing or page count ≠ `--pages` → abort with a clear message (no partial deck).
- Any page yields empty/too-small SVG (< 1000 chars) → abort, report the page index.
- Shell clamps slide index to `[0, N-1]` so nav can't go out of range.

## Verification (fidelity guarantee)

After building, render both the original PDF pages and the produced HTML slides to images at the
same resolution (real browser render via the existing fidelity harness) and compare page-by-page.
**Done only counts when all 10 pages match.** Evidence is surfaced to the user before claiming
completion. Also re-confirm the existing `presentasi-pert11.html` still builds byte-identically
(no regression from the parameterization).

## Output Locations

- `presentation-template-pert11.html` — project root (next to the source PDF).
- `analysis/build_pert11_html.py` — generalized, reusable, deterministic build script.

## Out of Scope (YAGNI)

- No selectable/editable text (explicitly traded away for fidelity).
- No content rewriting, re-theming, or slide reordering — pure faithful conversion.
- No speaker-notes panel, presenter view, or transitions beyond the existing plain slide swap.
- No changes to the existing 18-page deck's content or output.
