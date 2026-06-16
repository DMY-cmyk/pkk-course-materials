# Design Spec — Pert. 11 Presentation Load Rebalance (Chapter 4: Efficient Securities Markets)

**Date:** 2026-06-16
**Topic:** Re-divide Scott (2015) Ch. 4 *Efficient Securities Markets* across Kelompok 3's six speakers so every member carries a fair, weighted share — verified against the source PDF.
**Status:** Approved (design); ready for implementation plan.

## 1. Problem

The existing presentation guide (`rmk-pkk-pert11-efficient-securities-markets/presentation-guidance/panduan-presentasi-kelompok3-pert11.md`) divides the chapter into six speaker sections following chapter flow (4.1 → 4.8). The guide *claims* equal portions, but a composite load analysis (content volume × conceptual difficulty, plus opener/closer role overhead) shows the split is uneven:

- **Efri** (4.2.2 only) was under-loaded (~4.0).
- **Adinda** (4.1 + 4.2.1) and **Dzaki** (4.3 + 4.4) were over-loaded (~7.5–8.0).

The user requires that the division be (a) genuinely balanced — "no member too heavy or too light" — and (b) verified to match the actual source PDF, with every chapter part placed under the correct subsection.

## 2. Goals / Non-goals

**Goals**
- Every speaker carries a near-equal composite load (target band 6.0–7.5 on the internal load scale; mean 6.58).
- No speaker holds two heavy/technical blocks (4.5 CAPM and 4.6 asymmetry must stay solo and separated).
- Chapter narrative order 4.1 → 4.8 preserved; clean opener (Adinda) and closer + Q&A lead (Kunthi) preserved.
- Every content item is verified against the source PDF and sits under its correct subsection.

**Non-goals**
- No change to team identity, NIMs, or the six-speaker structure.
- No rewrite of the underlying chapter content (`content/`, `extraction/`) — those are read-only inputs here.
- No change to speakers 1 (Adinda), 4 (Prasetya), 5 (Odisiana) beyond minor duration/transition wording. Only Efri ↔ Dzaki change materially.

## 3. Decisions (from brainstorming)

1. **Fairness metric = Composite/balanced** (near-equal speaking time AND no member carrying two heavy/technical blocks). Speaking time has no hard floor — the class talk has no minimum duration.
2. **Boundaries = clean subsections by default; surgical split only where forced.** One split is used (§4.3) to remove the single unavoidable "light slot."
3. **Fixed roles:** Adinda opens; Kunthi closes and leads Q&A. Both carry role overhead factored into their load.
4. **All sections were freely reassignable**, but the balanced solution requires changing only the Efri/Dzaki seam.

### Key math finding
With pure clean boundaries, the 7 medium blocks force *exactly one* ~4.0 light slot — provably unavoidable (7 medium items → 3 pairs + 1 single across the 4 non-heavy speakers). The user chose **one surgical split of §4.3** (the cleanest split point: four discrete implications, no equations or figures) to eliminate that light slot and flatten the distribution.

## 4. Source verification (audit against `Efficient Securities Market - Pert. 11.pdf`, 33 pp.)

The PDF chapter skeleton (extracted):

| Subsection | Page |
|---|---|
| 4.1 Overview | 1 |
| 4.2.1 The Meaning of Efficiency | 2 |
| 4.2.2 How Do Market Prices Fully Reflect All Available Information? | 5 |
| 4.2.3 Summary | 7 |
| 4.3.1 Implications / 4.3.2 Summary | 8–9 |
| 4.4.1 A Logical Inconsistency / 4.4.2 Summary | 10–13 |
| 4.5.1 CAPM / 4.5.2 Critique / 4.5.3 Summary | 13–18 |
| 4.6.1 Information Asymmetry / 4.6.2 Fundamental Value / 4.6.3 Summary | 18–23 |
| 4.7 Social Significance | 24 |
| 4.8 Conclusions | 26 |
| Questions & Problems (excluded) | 27–33 |

**Audit verdict: every content item in the guide is placed under the correct subsection.** Verified anchors:
- Four efficiency properties → all in **4.2.1** (pp. 3–4).
- Beaver 1981 football (15–16 forecasters, 619 forecasts); ToP 4.1 Malkiel/WSJ (pros 10.9% / darts 4.5% / DJ 6.8%, Reg FD 2000) → **4.2.2** (pp. 5–7).
- Four Beaver (1973) implications + IAS 1 + decision-usefulness → **4.3.1** (pp. 8–9).
- Grossman (1976), noise traders, partial informativeness, large-firm prediction → **4.4.1** (pp. 10–13).
- Eq 4.1–4.4, Sharpe–Lintner CAPM, beta, market model, 4-assumption critique → **4.5** (pp. 13–18).
- Adverse selection/moral hazard, lemons (Akerlof 1970), JLT 2011 (260 firms; 7,856 trades; 24% in blackout; 3.6% / 10.8% excess return), Fig 4.2, SOX 2002, Maffett 2012 (42,930 funds / 42 countries), Enron/WorldCom → **4.6** (pp. 18–23).
- Wurgler 2000 / FHKP 2009 / BHV 2009, stick-vs-carrots, two social conditions → **4.7** (pp. 24–26).

**Precision notes (record, not defects):**
1. The five `x.x.3 Summary` subsections (4.2.3, 4.3.2, 4.4.2, 4.5.3, 4.6.3) are recaps; each folds into its parent-section speaker — no orphaned content.
2. *"CAPM understates cost of capital"* physically appears in **4.6.1 (p. 21)** but is thematically owned by Prasetya's CAPM section. Mark it as a Prasetya↔Odisiana bridge so neither double-covers it.

## 5. Final division

| # | Speaker (NIM) | Section | Load |
|---|---|---|---|
| 1 | Adinda Putri Dewi (086) | 4.1 + 4.2.1 — open/agenda · Fama definition · four properties | 7.5 (opener) |
| 2 | Efri Nurmalinda (049) | 4.2.2 + **4.3 implications 1–2** | 6.0 |
| 3 | Dzaki Muhammad Yusfian (079) | **4.3 implications 3–4** + 4.4 | 6.0 |
| 4 | Prasetya A. S. Gumilang (068) | 4.5 (CAPM + market model + critique) | 6.0 |
| 5 | Odisiana Manek (041) | 4.6 (asymmetry · lemons · JLT · fundamental value · Fig 4.2 · SOX · Maffett) | 6.5 |
| 6 | Kunthi Talibrata (097) | 4.7 + 4.8 (social significance · conclusions · lead Q&A) | 7.5 (closer) |

**Spread 6.0–7.5** (mean 6.58). The two 7.5 loads land on the opener and closer (framing + recap overhead is real work); the four pure-content speakers sit flat at 6.0–6.5.

### §4.3 split detail (the only structural change)
- **Efri** delivers the §4.3 intro ("Beaver 1973 outlined four implications…") and **implications 1–2**: (1) accounting policy with no cash-flow effect does not move price (straight-line vs declining balance; IAS 1); (2) full disclosure (benefits exceed costs).
- **Dzaki** opens with "The third implication…" and delivers **implications 3–4**: (3) naïve investor price-protected (Fama 1970); (4) accountants compete / decision-usefulness — then continues into **4.4** (Grossman paradox, noise traders, etc.).
- **Handoff line (Efri → Dzaki):** "…that's policy-neutrality and full disclosure. Dzaki takes the remaining two implications and the paradox they expose."

## 6. Implementation surface

Edit only `panduan-presentasi-kelompok3-pert11.md`:
1. **Peta Pembagian Seksi** table — update Efri's and Dzaki's `Seksi`, `Fokus`, and `Durasi` rows; adjust durations to reflect the rebalanced flow (Efri up, Dzaki down).
2. **Bagian 2 (Efri)** — append §4.3 implications 1–2 to her Naskah Poin, add the relevant Istilah Kunci (cash-flow effect, full disclosure), update her Kalimat Transisi to the new handoff line, refresh Antisipasi Tanya-Jawab.
3. **Bagian 3 (Dzaki)** — rewrite the opening so it starts at implication 3 (not implication 1); keep implications 3–4 + all of 4.4; adjust Istilah Kunci so cash-flow/full-disclosure terms move to Efri and Dzaki retains price-protected, decision-usefulness, noise-traders, etc.
4. **Aturan Main / intro paragraph** — keep wording about equal portions; the claim is now actually true.
5. **Bagian 1, 4, 5, 6** — no content change; only revisit Adinda's closing transition into Efri if it references section numbering, and verify durations sum consistently.

Then rebuild output:
- Run `build_guidance_docx.py` to regenerate `output/Panduan Presentasi Kelompok 3 - Pert. 11.docx`.

## 7. Testing / verification

- **Coverage check:** confirm all of 4.1–4.8 (incl. every summary recap) still appears in exactly one speaker section after the edit — no gaps, no double-coverage (special attention to the §4.3 seam and the CAPM-cost-of-capital bridge).
- **Citation integrity:** every figure/study still cited under the subsection the PDF audit confirmed.
- **Load check:** re-tally the load table; confirm all six speakers land in 6.0–7.5.
- **Build check:** `build_guidance_docx.py` runs clean and the `.docx` regenerates without error; spot-check that Efri's and Dzaki's sections render with the new content and transition.
