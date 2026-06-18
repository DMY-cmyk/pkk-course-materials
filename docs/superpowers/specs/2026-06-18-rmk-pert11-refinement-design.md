# Design — RMK Pertemuan 11 (Efficient Securities Markets) Refinement

**Date:** 2026-06-18
**Author:** Dzaki Muhammad Yusfian (122501079), Kelompok 3
**Deliverable:** `rmk-pkk-pert11-efficient-securities-markets/output/01079_Kelompok 3_RMK Pert. 11.docx`
**Source of truth:** Scott, W. R. (2015), *Financial Accounting Theory* (7th ed.), Chapter 4 — print pp. 120–152, PDF pp. 1–33.

---

## 1. Purpose

Refine the existing Pertemuan 11 RMK so that it (a) is demonstrably traceable to the
exact parts of Scott Ch. 4 it explains, (b) has every genuine book exhibit cropped,
placed, and correctly sized, and (c) reads neatly and clearly. This is a **content +
structure refinement of the existing pipeline**, not a rebuild. We edit
`content/*.md` plus a small enhancement to `src/python/build_docx.py`, then regenerate
the docx deterministically with `python src/python/build_docx.py`.

The docx is **generated**; it is never hand-edited. All changes are made to the
markdown content and the builder, then the build is re-run.

## 2. Audit baseline (current state — already correct)

The PDF in the project root is byte-identical (md5 `cf7b94a9…`) to the pipeline source
`input/chapter/Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf`.

Genuine visual / structural exhibits in Ch. 4, and their current status:

| Exhibit | Print pg | Asset | Status |
|---|---|---|---|
| Figure 4.1 — Organization of Chapter 4 | 120 | `assets/exhibits/fig-4-1.png` | placed, clean crop |
| Table 4.1 — Forecasting Outcomes of Football Games | 124 | `assets/exhibits/table-4-1.png` | placed, clean crop |
| Theory in Practice 4.1 — Malkiel / WSJ darts / Reg FD | 125 | `assets/exhibits/tip-4-1.png` | placed, legible |
| Figure 4.2 — Role of Financial Reporting in an Efficient Market | 141 | `assets/exhibits/fig-4-2.png` | placed, clean crop |
| Equations 4.1, 4.2, 4.3, 4.4, β, gross return | 133–135 | inline `@eq` (native OMML) | rendered |

Two **synthesized** diagrams (not in the ebook) are also present and will be **kept**
as supplementary teaching visuals, clearly captioned "diolah dari Scott (2015)":
`assets/diagrams/efficiency-forms.png`, `assets/diagrams/adverse-selection.png`.

The PDF contains **zero embedded raster images** (verification-report.md); all exhibits
are high-DPI rasterizations of native vector figures/tables, which is correct.

Content sections A–F are faithful, graduate professor-voice Indonesian, and cover
§4.1–§4.8 completely.

## 3. Gaps this refinement closes

1. **Chapter-section traceability is absent.** The Cornell cue column uses thematic
   questions only; nothing labels which §-number of Ch. 4 each note explains.
2. **Image sizing is untuned.** Every image is forced to a uniform `width=Cm(14.5)`
   with no height cap (`build_docx.py:252`). None overflow today, but a tall raster
   (e.g. `tip-4-1`, 11.1 cm tall at 14.5 cm wide) is not guarded.
3. **No visual grouping by chapter section** — the prose is one continuous cue/notes
   stream, harder to navigate than necessary.

## 4. Design

### 4.1 Chapter-section traceability — dividers + cue tags

**Builder change (`build_docx.py`):** add a new `@section` block type. It renders a
distinct **bold, lightly shaded** divider paragraph, visually separable from both the
Bagian A/B `##` headings (13 pt bold) and the Cornell cells. Parsing: a line beginning
`@section ` emits a `("section", text)` block; `group_cornell` treats it like any other
non-cue/notes block (it flushes the pending Cornell group first — existing behavior).
Styling: ~12.5 pt bold, left-aligned, `space_before≈8pt`, single bottom border or light
shading via `w:shd` to set it apart.

**Content change (`A_cornell.md`):** insert `@section` dividers that mirror the actual
chapter spine, in order:

- `@section §4.1 — Overview (Tinjauan)`
- `@section §4.2 — Pasar Sekuritas Efisien` (covers 4.2.1 Meaning, 4.2.2 How prices
  fully reflect, 4.2.3 Summary)
- `@section §4.3 — Implikasi bagi Pelaporan Keuangan`
- `@section §4.4 — Keinformatifan Harga (Informativeness of Price)`
- `@section §4.5 — Model Biaya Modal: CAPM & Market Model`
- `@section §4.6 — Asimetri Informasi`
- `@section §4.7 — Signifikansi Sosial Pasar yang Bekerja Baik`
- `@section §4.8 — Kesimpulan atas Pasar Sekuritas Efisien`

**Cue tags:** each existing Cornell cue cell gets its precise sub-section tag prepended
as a **bold `§`-number run** above the question text (e.g. `§4.2.1` over the
"meaning of efficiency" cue; `§4.5.1`/`§4.5.2` over the CAPM/critique cues; `§4.6.1`
over adverse-selection/JLT; `§4.6.2` over fundamental value). Implementation: a small
convention in the cue payload — the builder splits a leading `§…` token onto its own
bold line within the cue cell. Mapping of every existing cue to its §-number is fixed in
the implementation plan.

This keeps the document **Cornell-compliant** (cue | notes two-column structure intact)
while making each note traceable to an exact chapter location.

### 4.2 Exhibits — verified present; sizing tuned

- Keep all 4 book exhibits + 2 olahan diagrams + 5 equations.
- Replace the blanket `width=Cm(14.5)` in `add_image_with_caption` with **aspect-ratio-
  aware sizing that caps both width and height**: target width 14.5 cm, but if the
  resulting height would exceed a cap (~12 cm), scale by height instead so no single
  exhibit dominates a page. Uses Pillow to read pixel dimensions (already a dependency
  via the crop stage). Width stays ≤ usable text width (15 cm), height ≤ cap.
- Captions: preserve the "Sumber: Scott (2015)" vs "diolah dari Scott (2015)"
  distinction. Ensure each book-exhibit caption names its figure/table number so the
  reader ties it to the chapter (already the case for Fig 4.1 / Table 4.1 / TiP 4.1 /
  Fig 4.2; verify after rewrite).

### 4.3 Readability pass — /content-research-writer, facts-preserved

Run `content-research-writer` section-by-section over A–F to:

- split overly dense paragraphs, tighten sentences, smooth transitions;
- neaten the Active Recall (E) and Reference (F) lists;
- keep the narrative aligned to the new `@section` structure.

**Hard constraints (no drift):** preserve every fact, numeric figure, citation, and
italic-term gloss (e.g. *fully reflect*, *semi-strong*, *random walk*, *adverse
selection*); preserve professor-voice graduate Indonesian; keep all `@cue/@notes/@eq/
@section` and image markers intact. After the pass, **re-verify each claim against the
chapter PDF** before rebuilding.

### 4.4 Verify & rebuild

- Regenerate: `python src/python/build_docx.py`.
- Verify: build succeeds and prints the saved path/size; **page count ≥ 8** (governing
  rule); all 6 images embed; all 5 equations render (native OMML, no PNG fallback noise);
  Calibri 12 / 1.5 spacing / A4 / 3 cm margins preserved; identity header intact.
- Commit on a feature branch; do not overwrite `input/`.

## 5. Order of work

1. Add `@section` block type + cue-tag handling + sizing change to `build_docx.py`.
2. Insert `@section` dividers and cue `§`-tags into `A_cornell.md` (and any minor
   section labels in B–D where helpful).
3. Run content-research-writer readability pass over A–F; re-verify against PDF.
4. Rebuild docx; verify all acceptance criteria.
5. Commit; finish branch.

## 6. Acceptance criteria

- [ ] Every Cornell note is traceable to a Ch. 4 §-number via a divider + cue tag.
- [ ] All 4 genuine book exhibits + 2 olahan diagrams + 5 equations present, correctly
      captioned, none overflowing a page.
- [ ] Prose reads cleanly; no fact, figure, citation, or gloss lost vs. the pre-rewrite
      content; professor-voice preserved.
- [ ] `build_docx.py` runs clean; docx ≥ 8 pages; Calibri 12 / 1.5 / A4 / 3 cm margins.
- [ ] No edits to `input/`; docx never hand-edited (pipeline-regenerated only).

## 7. Out of scope

- Re-cropping exhibits (current crops are clean) — only re-crop if a sizing defect is
  found during verification.
- Changing the Rust pipeline stages, group identity, or the governing Cornell ruleset.
- Adding case studies or data not present in Scott Ch. 4 (no fabrication).
