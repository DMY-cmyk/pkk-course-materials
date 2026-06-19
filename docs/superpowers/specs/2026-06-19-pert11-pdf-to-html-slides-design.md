# Design — Pert. 11 PDF → Self-Contained HTML Slide Deck

*Date: 2026-06-19*
*Topic: Convert the exported Canva deck PDF into a browser-deliverable HTML slide presentation, preserving content and design exactly.*

## Goal

Turn `Presentasi PKK Pert. 11 - Kelompok 3.pdf` (18 pages, 1440×810, 16:9) into a single,
self-contained, offline-capable HTML slide presentation that is **deliverable as-is** and
**does not break any content or design** present in the source PDF.

## Hard Requirements

1. **Fidelity is paramount.** Every slide must render visually identical to the source PDF page.
2. **Self-contained.** One `.html` file, double-click to open, works fully offline.
3. **No fabrication / no edits to source content.** The PDF is the single source of truth.
4. The original PDF is never modified.

## Key Findings (from probing the actual PDF)

- Page geometry: 18 pages, each 1440×810 pt (16:9).
- PyMuPDF `get_svg_image(text_as_path=True)` → glyphs become vector **paths** (no font
  dependency) + embedded raster images. Renders identical everywhere.
- `text_as_path=False` → real `<text>`, but depends on fonts **Neue Montreal Bold**, **Roboto**,
  and a non-standard **Type3** font. Custom fonts aren't in browsers and the Type3 font cannot be
  extracted/embedded — selectable-text mode would risk font fallback breaking the design.
- **Decision: `text_as_path=True`** — guaranteed pixel-faithful, scalable, zero font risk.
  Trade-off accepted: on-slide text is not selectable/copyable.

## Architecture

### Component 1 — Build script (`analysis/build_pert11_html.py`)
- **What it does:** Reads the source PDF, renders each page to a vector SVG
  (`text_as_path=True`), assembles all 18 SVGs into one self-contained HTML file using a
  shell template, writes `presentasi-pert11.html` to the project root.
- **How to use it:** `python analysis/build_pert11_html.py` (deterministic; safe to re-run).
- **Depends on:** PyMuPDF (`fitz`), the source PDF, the HTML shell template (inlined in the
  script or a sibling template file).
- **Determinism:** SVG output must be byte-stable across runs (no timestamps/random ids) so
  re-builds don't produce spurious diffs. Strip/normalize any volatile metadata.

### Component 2 — HTML slide shell (the template)
- **What it does:** Hosts the 18 inline `<svg>` slides and provides all navigation/UX.
- **Structure:**
  - `<div id="deck">` containing 18 `<section class="slide">`, each wrapping one inline `<svg>`.
  - A 16:9 stage (`aspect-ratio: 16/9`) centered in the viewport with letterboxing; the SVG
    scales to fit without distortion (`width:100%`, `preserveAspectRatio` intact).
  - Only the active slide is displayed (`display` toggle / `.active` class) for performance.
- **Depends on:** nothing external — all CSS and JS inlined; no network, no fonts, no CDNs.

### Component 3 — Controls (vanilla JS, inlined)
- **Keyboard nav:** `←`/`PageUp` = prev, `→`/`Space`/`PageDown` = next, `Home` = first,
  `End` = last.
- **Fullscreen + click zones:** `F` toggles fullscreen; click on left half = prev, right half =
  next (disabled while overview is open).
- **Counter + progress:** "N / 18" readout + a thin top progress bar reflecting position.
- **Thumbnail overview:** `Esc` or `O` opens a grid of all 18 slides (reusing the same inline
  SVGs at small scale); click a thumbnail to jump; `Esc` closes. While open, click-zone nav is
  suppressed so grid clicks select rather than advance.

## Data Flow

```
Presentasi PKK Pert. 11 - Kelompok 3.pdf
        │  PyMuPDF, page-by-page, text_as_path=True
        ▼
   18 × inline <svg> (vector, faithful)
        │  assembled into shell template
        ▼
   presentasi-pert11.html  (single self-contained file)
        │  open in browser
        ▼
   Keyboard / click / fullscreen / overview navigation
```

## Error Handling

- If the source PDF is missing or page count ≠ 18, the build script aborts with a clear message
  (don't silently produce a partial deck).
- If any page yields empty/zero-length SVG, abort and report the page index.
- The shell clamps the slide index to `[0, 17]` so nav can't go out of range.

## Verification (fidelity guarantee)

After building, render both the original PDF pages and the produced HTML slides to images at the
same resolution and compare them page-by-page (visual diff / side-by-side). Done only counts when
all 18 pages match. Evidence is surfaced to the user before claiming completion.

## Output Locations

- `presentasi-pert11.html` — project root (next to the source PDF).
- `analysis/build_pert11_html.py` — reusable, deterministic build script.

## Out of Scope (YAGNI)

- No selectable/editable text (explicitly traded away for fidelity).
- No content rewriting, re-theming, or slide reordering — pure faithful conversion.
- No speaker-notes panel, no presenter view, no transitions/animations beyond plain slide swap.
