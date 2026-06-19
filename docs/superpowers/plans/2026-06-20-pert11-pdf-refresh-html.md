# Pert. 11 HTML Deck Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Regenerate `presentasi-pert11.html` so it faithfully reflects the current (re-exported) `Presentasi PKK Pert. 11 - Kelompok 3.pdf` (18 pages), then verify nothing in the content or design broke.

**Architecture:** Re-run the existing, tested, committed pipeline `analysis/build_pert11_html.py` with its module defaults. The pipeline renders each PDF page to a vector SVG (`text_as_path=True` — pixel-faithful, zero font dependency), namespaces ids per page, and injects them into the shell template + controls JS to produce one self-contained, offline HTML deck. No code is written or changed; the only difference from the last run is the updated input PDF. Verify the result page-by-page against the source PDF.

**Tech Stack:** Python 3.12, PyMuPDF (`fitz`), Pillow + numpy (fidelity check only), headless Chromium/Edge, pytest. Vanilla HTML/CSS/JS deck (no build tooling, no network).

## Global Constraints

- **Fidelity is paramount** — every slide must render visually identical to the source PDF page; no content added, removed, reflowed, or restyled.
- **Self-contained** — one `.html` file, opens by double-click, works fully offline (no fonts, CDNs, network).
- **The source PDF is never modified.**
- **No edits to the build script, verifier, template, or controls** — the pipeline is already generalized and tested; this task only runs it.
- **Determinism** — re-running the build produces byte-identical output for the same PDF.
- Render mode is `text_as_path=True`; on-slide text is intentionally not selectable (accepted trade-off, same as the existing deck).
- Output (overwrite in place): `presentasi-pert11.html` (project root). Source: `Presentasi PKK Pert. 11 - Kelompok 3.pdf` (18 pages, 1440×810).

---

### Task 1: Rebuild and verify the refreshed deck

**Files:**
- Modify (regenerate): `presentasi-pert11.html` (project root — the deliverable)
- Run (no changes): `analysis/build_pert11_html.py`, `analysis/verify_pert11_fidelity.py`, `tests/test_build_pert11_html.py`

**Interfaces:**
- Consumes: `build_pert11_html.main()` defaults (`SOURCE_PDF = "Presentasi PKK Pert. 11 - Kelompok 3.pdf"`, `EXPECTED_PAGES = 18`, `OUTPUT = presentasi-pert11.html`); `verify_pert11_fidelity.main(argv)` with `--source`/`--pages`.
- Produces: regenerated `presentasi-pert11.html` + page-by-page fidelity evidence surfaced to the user.

- [ ] **Step 1: Confirm the pipeline is green before rebuilding**

Run: `python -m pytest tests/test_build_pert11_html.py -v`
Expected: PASS (all existing tests). This proves the converter is intact before we use it. If any test fails, STOP and switch to systematic-debugging — do not build on a broken pipeline.

- [ ] **Step 2: Confirm the input PDF is the current 18-page export**

Run:
```bash
python -c "import fitz; d=fitz.open('Presentasi PKK Pert. 11 - Kelompok 3.pdf'); print('pages=',d.page_count,'size=',tuple(round(x) for x in d[0].rect))"
git status --porcelain "Presentasi PKK Pert. 11 - Kelompok 3.pdf"
```
Expected: `pages= 18 size= (0, 0, 1440, 810)` and an empty `git status` line (PDF is the committed, current export). If pages ≠ 18, STOP and report — the deck size assumption changed and the plan must be revisited.

- [ ] **Step 3: Rebuild the deck (overwrite in place)**

Run: `python analysis/build_pert11_html.py`
Expected: prints `wrote .../presentasi-pert11.html (<N> bytes)` with no error. (No `--source/--output/--pages` needed — the module defaults already target this PDF and output.)

- [ ] **Step 4: Sanity-check the deliverable (count + self-contained)**

Run:
```bash
python -c "import re; h=open('presentasi-pert11.html',encoding='utf-8').read(); print('slides=',h.count('class=\"slide\"')); print('counter_total=','/ 18' in h); ns=re.sub(r'\sxmlns(?::\w+)?=\"[^\"]*\"','',h); print('no_external=', not any(x in ns for x in ('http://','https://','<link','@import','src=\"//')))"
```
Expected: `slides= 18`, `counter_total= True`, `no_external= True`. If any is wrong, STOP — the build did not produce a complete self-contained 18-slide deck.

- [ ] **Step 5: Run the page-by-page fidelity verification**

Run: `python -m analysis.verify_pert11_fidelity --source "Presentasi PKK Pert. 11 - Kelompok 3.pdf" --pages 18`
Expected: eighteen `page NN: mean_abs_diff=… pct>20=… OK` lines and a final `RESULT: PASS` (exit 0).
- If `RESULT: REVIEW NEEDED`: inspect the flagged page's `analysis/_pert11_fidelity/pdf_NN.png` vs. `chrome_NN.png`, diagnose with systematic-debugging, and do NOT claim completion.
- If the verifier exits 2 (`NO BROWSER FOUND`): report that fidelity could not be auto-verified and ask the user to open `presentasi-pert11.html` and eyeball all 18 slides against the PDF before sign-off — do not silently skip.

- [ ] **Step 6: Confirm only the deliverable changed (no collateral changes)**

Run: `git status --porcelain`
Expected: `presentasi-pert11.html` shows as modified; no source PDF, build script, verifier, template, or controls changes. (Untracked `analysis/_pert11_fidelity/` render artifacts are expected and ignorable.)

- [ ] **Step 7: Commit the refreshed deck**

```bash
git add "presentasi-pert11.html"
git commit -m "build(pert11-html): refresh deck from updated Kelompok 3 PDF export"
```

---

## Self-Review

**Spec coverage:**
- Faithful conversion of the current 18-page PDF → Task 1 Steps 2–3 + `text_as_path=True` (pipeline unchanged). ✓
- Self-contained / offline → Step 4 check. ✓
- Source PDF never modified → no step writes to it; Step 6 confirms. ✓
- No edits to build script/verifier/template/controls → only run, never modified; Step 6 confirms. ✓
- Page-by-page fidelity verification, no silent skip → Step 5. ✓
- Determinism → existing build logic unchanged (covered by `test_build_html_deterministic` run in Step 1). ✓
- Overwrite `presentasi-pert11.html` in place → Step 3 (module default) + Step 7. ✓

**Placeholder scan:** No TBD/TODO; every step shows the exact command and expected output. ✓

**Type consistency:** `main()` (argless build) and `verify_pert11_fidelity.main(argv)` with `--source`/`--pages` match the committed signatures used in Steps 3 and 5. ✓
