# Refresh the Pert. 11 HTML Slide Deck from the Updated PDF — Design

**Date:** 2026-06-20
**Status:** Approved (design)

## Goal

Regenerate `presentasi-pert11.html` so it faithfully reflects the **current**
`Presentasi PKK Pert. 11 - Kelompok 3.pdf` (18 pages, 1440×810). Every bit of
content and design must be preserved exactly as the Canva PDF export shows it —
nothing added, removed, reflowed, or restyled.

## Context

- The Canva deck was updated and the PDF re-exported (commit `2a3bbb9`,
  "build(pert11-canva): re-export PDF after user's deck updates").
- The committed `presentasi-pert11.html` is now **stale**: a deterministic
  rebuild from the current PDF yields a *different* file (10.97 MB) than the
  committed one (11.66 MB), confirming the HTML predates the latest PDF export.
- A complete, tested, committed pipeline already exists and does exactly this
  conversion — there is no new converter to write.

## Approach — reuse the proven pipeline (no new code)

Run the existing `analysis/build_pert11_html.py` with its module defaults:

- source = `Presentasi PKK Pert. 11 - Kelompok 3.pdf`
- output = `presentasi-pert11.html` (project root)
- pages = 18

The pipeline:

1. Renders each PDF page to a vector SVG with `text_as_path=True` →
   **pixel-faithful, zero font dependency**, so content and layout cannot drift.
2. Namespaces all SVG ids per page (`pNN_…`) so 18 inlined SVGs don't collide.
3. Injects the SVGs into `analysis/pert11_shell_template.html` +
   `analysis/pert11_controls.js` (keyboard/click navigation) → one
   **self-contained, fully offline** `.html` (no CDN, no network, opens by
   double-click).

It is deterministic: re-running produces byte-identical output for the same PDF.

**Why not an alternative:** writing a fresh converter would risk the exact
"broken content/design" outcome we must avoid, and would discard a tested
pipeline. The only change versus the last run is the input PDF — which is the
entire point of this task.

**On-slide text is intentionally not selectable** (`text_as_path=True`) — this
is the same accepted trade-off as the existing deck, chosen for guaranteed
visual fidelity.

## Verification (the substantive work)

1. **Build** writes `presentasi-pert11.html` without error.
2. **Sanity:** exactly 18 slides; counter shows `/ 18`; no external references
   (self-contained / offline).
3. **Page-by-page fidelity:** run `analysis/verify_pert11_fidelity.py`
   (headless Chromium/Edge renders each slide and compares it to the source PDF
   page). Result must be `PASS`. If no browser is installed, report that fidelity
   could not be auto-verified and ask the user to eyeball the deck against the
   PDF before sign-off — **do not silently skip.**
4. **No collateral changes:** `git status` shows only `presentasi-pert11.html`
   modified by the build.

## Deliverable

Updated, fidelity-verified `presentasi-pert11.html` at the project root,
committed (overwrite in place — it is the canonical single deliverable).

## Out of scope

- No edits to the source PDF.
- No changes to the build script, verifier, template, or controls (the pipeline
  is already generalized and tested).
- No content/design changes of any kind — faithful reproduction only.
