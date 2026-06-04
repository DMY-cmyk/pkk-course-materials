# RMK Spec — Wolk Ch. 13 "Statement of Cash Flows" (Kelompok 2)

Date: 2026-06-04 · Phase 1 output · Approved decisions in `design-decisions.md`.

## 1. Deliverable
- **File:** `output/RMK Chap. 13_Kelompok 2_PKK.docx` — the "_ALK" label in the original request was confirmed as a course-label error and corrected to **_PKK** (user decision, 2026-06-04).
- A single, submission-ready Word document; one member uploads for the group, so the document carries all six identities.

## 2. Format template (hard gates)
| Property | Value |
|---|---|
| Page | A4 (210×297 mm), margins 25.4 mm all round |
| Line spacing | 1.5 throughout body, headings, and tables |
| Font | **Calibri 12 pt** everywhere (headings: Calibri bold, H1 14 pt, H2 12 pt; captions Calibri 12 pt italic) |
| Length | ≥ 8 pages — achieved with substance (see §5 weighting), never padding |
| Format | OOXML `.docx`, opens cleanly in Word and LibreOffice |

## 3. Language & voice
- **Bahasa Indonesia**, professor-led S2 register: explain → interpret → connect; never list-style paraphrase.
- English technical terms retained verbatim and italicized on first use: *Statement of Cash Flows (SCF)*, *SCFP*, *free cash flow (FCF)*, *NOPLAT*, *nonarticulation*, *quality of income*, *plug number*, *direct/indirect method*, *all-inclusive/all-resources*, *fineness*, dst.
- Content source: **Wolk Ch. 13 only**. No outside material; no fabricated figures or page numbers.

## 4. Exhibit-placement policy
1. **Cropped exhibits (13.4–13.11):** rendered from the source PDF at 240 dpi, cropped to the table body (printed exhibit titles always excluded — the caption is always a Word paragraph, never the in-image title), whitespace-trimmed, embedded **centered at full text-column width 6.25 in**, aspect ratio preserved.
2. **Re-set exhibits (13.1, 13.2, 13.3):** the SAGE PDF renders these as text with broken layout (verified: 13.3 wraps "$445", floats values into margins). They are **rebuilt as native Word tables**, line-by-line faithful to the PDF content; Stage 1 review verifies every cell against the source.
3. **Equation displays (13.1, 13.2):** re-set as centered bold text lines (e.g., **FCF = NOPLAT − investasi pada *operating invested capital***), labeled "(13.1)" / "(13.2)" as in the chapter.
4. **Captions:** every exhibit gets a Word caption paragraph, italic, centered, directly beneath: "Exhibit 13.x — [original English title] (Wolk, Dodd & Rozycki, 2017, Ch. 13)".
5. **Adjacency:** each exhibit is inserted in its anchor section, immediately after the paragraph that introduces it and before the paragraph that reads it through. Never detached more than one paragraph from its explanation; never split across a page mid-image.
6. Governed by `content/figures/manifest.yaml` (id, caption, source page, crop box, width, anchor section, render type: crop|reset-table|reset-equation).

## 5. Section layout & structure
15 sections + cover, mirroring the chapter's own order (see `analysis/rmk-build-input.md` for the full concept→section table):

Cover/identitas → 0 Pendahuluan → 1 SCFP & pendahulunya (eq-13.1, Exh 13.1) → 2 Motivasi SCF → 3 Tujuan → 4 Struktur/trikotomi → 5 Metode langsung vs tidak langsung (Exh 13.2, 13.3) → 6 Nonartikulasi (Exh 13.4) → 7 Masalah klasifikasi (Exh 13.5) → 8 Kegunaan analitis → 9 Misklasifikasi → 10 SCF lebih dari CFO (Exh 13.6) → 11 Kebutuhan pengguna → 12 Free cash flow (eq-13.2, Exh 13.7–13.11) → 13 Riset → 14 Memperbaiki SCF + sintesis.

- **Layout style (chosen):** explanatory prose with exhibit read-throughs, **plus a compact synthesis table** in sections that compare alternatives — §5 (direct vs indirect trade-off), §7 (premium Methods 1–4), §12 (four performance measures). Tables are synthesis, not substitutes for prose.
- Every exhibit that contains numbers gets at least one **worked read-through** in prose (e.g., FCF 2005 = $332 from CFO $527).
- Page-weight budget: heavy §1/§5/§6/§7/§12 (≈1–1.5 pp); medium §0/§3/§9/§10/§14; light §2/§4/§8/§11/§13.

## 6. Identity policy
Cover block carries: document title, chapter identification, course "Pelaporan Keuangan Korporat (MNK202)", "Kelompok 2", and the verbatim roster table:
122501039 Satriyo Nugroho · 122501048 Mario Da Costa · 122501067 Amelda Putri Zhany Wiguna · 122501078 Ahmad Ramadhan · 122501084 Nida Nur Cahyati · 122501094 Priska Putri Parungky.

## 7. Architecture (single source of truth)
- `content/sections/*.md` (front matter: covers_concepts, embeds_exhibits, rubric) + `content/_shared/` + `content/figures/manifest.yaml` → assembled by the Rust pipeline → **python-docx bridge** (`crates/rmk-build` shells out to `tools/build_docx.py`) → `output/*.docx`.
- Never hand-edit the docx.
- Cargo workspace: `rmk-build`, `rmk-extract-figures`, `rmk-audit`, `rmk-validate`, `shared` (types: Concept, Section, Exhibit, Rubric, FormatRule).
- **Documented substitutions:** (1) docx skill unavailable on this Windows host → python-docx bridge (pattern proven in `ti4`/`ti5`); (2) tesseract unavailable → Claude native vision for the two image-OCR tasks (already executed in Phase 0). Both noted in `output/VALIDATION-REPORT.md`.

## 8. Verification
- Per-section rubric (RED) before content; `cargo test` asserts concepts present, exhibits embedded, format compliant (GREEN); S2-depth deepening (REFACTOR); commit per section.
- Two-stage review: Stage 1 completeness/exhibits/format; Stage 2 academic quality/faithfulness vs the PDF.
- Phase 5 gates: A4 ✓ 1.5 ✓ Calibri 12 ✓ ≥8 pp ✓ .docx ✓; all 62 concepts (C-01…C-62) homed; Exhibits 13.1–13.11 + both equations present, captioned, in-margin, adjacent; six identities on cover; filename exact; `cargo test` + `clippy -D warnings` + `fmt --check` clean.

## 9. Known source caveats (transparency)
- Source PDF ends at internal p. 23/31, mid-Questions — all expository content intact; no impact on the RMK body.
- Exhibit 13.3's broken source layout is the documented reason for the re-set decision.
- The lecturer's "maksimum 4 anggota" message predates the final grouping; the 6-member roster image governs identity.
