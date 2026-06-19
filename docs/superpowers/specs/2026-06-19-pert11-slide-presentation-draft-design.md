# Design — Slide-Presentation-Draft (Pert. 11 · Efficient Securities Markets)

**Date:** 2026-06-19
**Author:** Dzaki Muhammad Yusfian (assisted)
**Status:** Approved (brainstorming) → pending spec review → writing-plans

## Purpose

Produce one Markdown file that specifies a Winston-compliant slide deck for the
Kelompok 3 class presentation on **Scott (2015), Financial Accounting Theory
(7th ed.), Chapter 4 — Efficient Securities Markets**. The file is a *paste-into-Claude-Design
spec*, not the final visual: Claude Design consumes it to produce the styled deck.

It applies **Patrick Winston's MIT presentation framework** ("How to Speak") so the
talk is delivered like an experienced presenter, and it references the existing cropped
images / diagrams / tables / charts in the repository.

## Source-of-truth inputs (read-only)

| Input | Role |
|---|---|
| `presentation-guidance/panduan-presentasi-kelompok3-pert11.md` | Section→member mapping, naskah poin, glossary, durations — **governs content + order** |
| `content/B_ringkasan.md` … `content/F_referensi.md` | Professor-voice phrasing and citations |
| `assets/diagrams/efficiency-forms.png` | Three forms of efficiency (Fama 1970) — custom ID diagram |
| `assets/diagrams/adverse-selection.png` | Adverse selection → full-disclosure antidote flow — custom ID diagram |
| `assets/exhibits/fig-4-1.png` | Organization of Chapter 4 (roadmap flowchart) |
| `assets/exhibits/fig-4-2.png` | Role of Financial Reporting (concentric circles) — **the Symbol** |
| `assets/exhibits/table-4-1.png` | Forecasting Outcomes of Football Games (Beaver 1981) |
| `assets/exhibits/tip-4-1.png` | Theory in Practice 4.1 (Malkiel random walk) |
| `Patrcik Winston MIT Presentation Master/*.jpeg` | The 5-part Winston framework (transcribed below) |

**Never fabricate figures.** Every number traces to the panduan / chapter.

## Output

`presentation-guidance/slide-presentation-draft-pert11.md` — **~24 slides**, one block per slide.

### Per-slide field schema (decided: "Full")

```
## Slide NN — <Section tag · Speaker>
**Headline:** <full sentence-assertion, ≤ ~10 words>
**On-slide text:** <≤4 bullets, ≤6 words each — or a single stat/quote>
**Visual:** <asset path OR "build: <desc>"> — caption: <one line>
**Speaker script (id):** <30–60 s professor-voice Indonesian; English terms verbatim>
**Design hint:** <layout intent for Claude Design — white space, focal point, callout>
```

- **Language:** Indonesian professor-voice on slides and in script; English technical
  terms kept verbatim (efficient market, fair game, random walk, noise traders, CAPM,
  beta, adverse selection, moral hazard, lemons problem, fundamental value, …).
- **Headlines are assertions, not labels** (Winston): "Konsensus mengalahkan setiap
  peramal individual", not "Mekanisme Harga".

## Winston framework wiring (the crime fixes)

The deck opens the document with a **Slide-Crime Audit table** — Winston's 10 crimes,
each with the specific fix applied:

| # | Crime | Fix applied in this deck |
|---|---|---|
| 1 | Too many slides | Capped at ~24 for a 23-min talk (≈1 slide/min) |
| 2 | Too many words per slide | ≤4 bullets × ≤6 words; hard cap forces ≥40pt |
| 3 | Font < 40pt | On-slide text budget keeps every line large |
| 4 | Reading slides aloud | Slide text ≠ script; script carries the words |
| 5 | Laser pointer | Design hints build emphasis into the slide (callouts/highlight) |
| 6 | Speaker far from slides | Delivery note: stand beside the screen |
| 7 | No white space | Every design hint mandates breathing room |
| 8 | Background clutter / logos | No logos; one focal element per slide |
| 9 | Collaborators list as final slide | Members shown on Cover only |
| 10 | "Thank you" / "Questions?" final slide | Final slide = **Contributions close** |

**The Star (one per deck spine):**
- **Symbol** — the two concentric circles (`fig-4-2.png`): public info vs. fundamental value.
- **Slogan** — *"Yang dihargai pasar adalah informasi, bukan bentuknya."* (repeated verbatim)
- **Surprise** — the consensus beats *every* individual forecaster (Table 4.1); darts ≈ pros.
- **Salient idea** — **asimetri informasi adalah alasan akuntansi ada.**
- **Story** — lemons market → inside information → role of reporting → fundamental value.

**Persuasion structure (job-talk):** Vision (S1–S3) → Proof of work (the 6 sections) →
**Contributions close** (S23) that mirrors the S2 empowerment promise. Vision lands inside
the first ~3 slides.

**Empowerment Promise (S2, verbatim seed):** *"Di akhir 23 menit, Anda bisa menjelaskan
mengapa pasar menghargai* informasi *— bukan bentuk pengungkapan — dan mengapa asimetri
informasi adalah alasan akuntansi ada."*

**Props & Stories:** speaker notes flag ≥2 physical-prop moments — e.g. a used-car key for
the lemons problem; a sealed envelope for "inside information" / the gap between the circles.

## Slide map (~24, 6-speaker mapping preserved)

| Slide | Section · Speaker | Core |
|---|---|---|
| S1 | Cover | Title, Kelompok 3 members + NIM, course, Pert. 11 |
| S2 | Vision · (opener, Adinda) | Empowerment promise |
| S3 | Vision · Adinda | Roadmap — `fig-4-1.png` |
| S4 | 4.1 · Adinda | Efficient market defined (Fama semi-strong) |
| S5 | 4.2.1 · Adinda | Three forms — `efficiency-forms.png` |
| S6 | 4.2.1 · Adinda | Four properties of efficiency |
| S7 | 4.2.2 · Efri | Averaging/consensus — `table-4-1.png` (Surprise) |
| S8 | 4.2.2 · Efri | Malkiel random walk — `tip-4-1.png` |
| S9 | 4.3 i.1–2 · Efri | Implications 1–2 (no-cash-flow neutrality, full disclosure) |
| S10 | 4.3 i.3–4 · Dzaki | Implications 3–4 (price-protected, accountants compete) |
| S11 | 4.4 · Dzaki | Grossman paradox |
| S12 | 4.4 · Dzaki | Noise traders → partially informative (resolution) |
| S13 | 4.5 · Prasetya | CAPM equation |
| S14 | 4.5 · Prasetya | Beta / systematic risk |
| S15 | 4.5 · Prasetya | Market model + four-assumption critique |
| S16 | 4.6 · Odisiana | Asymmetry: adverse selection vs moral hazard |
| S17 | 4.6 · Odisiana | Lemons story — `adverse-selection.png` (prop moment) |
| S18 | 4.6 · Odisiana | Fundamental value — `fig-4-2.png` (**the Symbol**) |
| S19 | 4.6 · Odisiana | Evidence: JLT (2011), Maffett (2012), SOX |
| S20 | 4.7 · Kunthi | Social significance — capital allocation |
| S21 | 4.7 · Kunthi | Stick vs carrots + two social conditions |
| S22 | 4.8 · Kunthi | Chapter synthesis (slogan + salient idea) |
| S23 | Close · Kunthi | **Contributions close** (mirrors S2 promise) |
| S24 | Appendix | Glossary / back-up for Q&A |

Compression lever: S19 and S21 may merge into adjacent slides to reach ~22 if desired.

## Constraints / non-goals

- Do **not** regenerate or edit the image assets; reference them by relative path.
- Do **not** restructure away the 6-speaker section assignment (graded group work).
- Do **not** produce the final styled deck here — that is Claude Design's job.
- Keep professor-voice; undergraduate summarization is a defect (CLAUDE.md rule).

## Acceptance criteria

1. File exists at `presentation-guidance/slide-presentation-draft-pert11.md`.
2. Slide-Crime Audit table present; all 10 crimes addressed.
3. ~22–24 slide blocks, each with all 5 fields populated.
4. Every visual asset (6) referenced at least once at its correct slide.
5. S2 carries the empowerment promise; S23 is a contributions close (no thank-you/Q&A slide).
6. The Star's slogan appears verbatim on ≥2 slides (intro + synthesis).
7. Every numeric claim traces to the panduan/chapter; no fabrication.
8. Section→member mapping matches `panduan-presentasi-kelompok3-pert11.md` exactly.
