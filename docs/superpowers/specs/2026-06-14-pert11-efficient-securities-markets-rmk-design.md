# Design — RMK Pertemuan 11: Efficient Securities Markets (Kelompok 3)

**Date:** 2026-06-14
**Course:** Pelaporan Keuangan Korporat (MNK202) — S2 / Pascasarjana STIE YKPN
**Topic:** Scott, *Financial Accounting Theory* (7th ed., 2015), Chapter 4 — Efficient Securities Markets (Pertemuan 11, reading code S:4)
**Deliverable:** `output/01079_Kelompok 3_RMK Pert. 11.docx`
**Status:** Approved (brainstorming) — pending spec review before writing-plans

---

## 1. Goal & Scope

Produce one graded **group** Cornell-Notes RMK (`.docx`) of Scott Ch. 4, in formal-yet-simple
academic Bahasa Indonesia with English technical terms preserved and glossed on first use.
The document captures all core chapter content at graduate depth while staying concise, fully
conforms to `Ketentuan Pembuatan RMK.png` and `Pedoman Penyusunan Resume Cornell Notes.pdf`,
embeds every required figure/table/box and Equations 4.1–4.4, and reads as human-authored
(no AI tells) after a dedicated language pass.

**In scope:** the full Cornell A–F document, the §3 coverage map, all required visuals and equations,
the reproducible pipeline, and the Humanize → Simplify pass.

**Out of scope:** any critical-review document (none present for Pertemuan 11); slides; anything
beyond the single `.docx`.

---

## 2. Key Decisions (locked in brainstorming)

| # | Decision | Choice |
|---|----------|--------|
| D1 | Document identity | **Group — Kelompok 3** (6 members + NIMs). Filename `01079_Kelompok 3_RMK Pert. 11.docx`. |
| D2 | Pipeline strategy | **Clone & adapt** the shipped `rmk-pkk-pert10` pipeline; do not rebuild from scratch. |
| D3 | `.docx` visual identity | **Reuse pert10 as-is** (A4 · Calibri 12 · 1.5 spacing · justified; navy headings; centered italic captions; figures 14.5 cm). |
| D4 | Cornell layout | **Reuse pert10** two-column table: cue 5 cm (bold, left) · notes 10 cm (justified), 11 pt, 1.5 spacing. |
| D5 | Equation typesetting | **Native Word equation objects (OMML)** for Eq 4.1–4.4, with a per-equation image fallback (see §6). |

> Note on D1: the master prompt specifies a Kelompok 3 group submission even though the
> `Ketentuan` PNG carries a handwritten "Pribadi / Individual" note and prior Pert. 9/10 RMKs
> were individual. Built as a group document per explicit instruction; if a reviewer later
> clarifies it must be individual, **only the identity block and filename change.**

---

## 3. Mandatory Content Coverage Map (Scott Ch. 4, source order)

Section A walks the chapter in source order. Every item below appears with a plain-language
gloss of its technical terms:

- **4.1 Overview** — rational investor behaviour → prices "fully reflect" collective information;
  the core accounting implication is *information content*, not *form/location* → leads to full disclosure.
- **4.2 Meaning of efficiency** — semi-strong form (Fama, 1970) vs strong form; four key points
  (relative to public info → insider trading possible; relative not omniscient → 2007–08 illustration;
  fair game / no excess risk-adjusted returns, CAPM benchmark; random walk / no serial correlation);
  informed investors and arbitrage.
- **4.2.2 How prices fully reflect information** — Beaver football-forecasting example (**Table 4.1**,
  consensus beats every individual); independence of decisions; forecasters→investors / consensus→price
  analogy; **Theory in Practice 4.1** (Malkiel, *A Random Walk Down Wall Street*; WSJ dartboard; Regulation FD).
- **4.3 Implications for financial reporting (Beaver, 1973)** — no-differential-cash-flow policy choices
  don't move price if disclosed/convertible (straight-line vs declining-balance as "paper" effects);
  efficiency ↔ full disclosure; naïve investor is price-protected; accountants compete with other sources;
  ties to decision usefulness & Conceptual Framework.
- **4.4 Informativeness of price** — Grossman (1976) logical inconsistency; resolution via noise traders
  & rational expectations → partially informative prices; voluntary disclosure, conservatism as signal, MD&A.
- **4.5 Model of cost of capital** — Sharpe–Lintner CAPM (**Eq 4.1–4.4**): return, expected return,
  beta = Cov(j,M)/Var(M), systematic risk; market model Rjt = αj + βjRMt + εjt and its three uses
  (price–expectations link; realized = expected + abnormal; estimating beta by regression); CAPM critique
  (rational expectations & estimation risk, common-knowledge assumption, zero transaction cost/liquidity,
  investor rationality — sharpened by 2007–08).
- **4.6 Information asymmetry** — adverse selection vs moral hazard; estimation risk; insurance and
  used-car/lemons markets (Akerlof, 1970), pooling; insiders as used-car-seller analogue; JLT (2011)
  blackout-period study (24% of trades inside blackout windows; general-counsel approval removes abnormal profit).
- **4.6.2 Fundamental value** — value absent inside information; **Figure 4.2** (inner/outer circles; financial
  reporting converts inside → outside information); Sarbanes-Oxley (2002); Maffett (2012) opacity study;
  "markets that work well/better"; Enron, WorldCom.
- **4.7 Social significance** — efficient capital allocation; lemons effect on under/over-investment; market
  depth vs thinness; Wurgler (2000); FHKP (2009); BHV (2009); regulation ("stick") vs incentives ("carrots").
- **4.8 Conclusions.**

**Required visuals:** Figure 4.1 (chapter organization), Table 4.1 (football forecasting),
Theory in Practice 4.1 box (Malkiel/dartboard), Figure 4.2 (role of financial reporting). Each cropped
tight (no page headers/footers), resized to ≤14.5 cm width, captioned, placed beside its explanation.

---

## 4. Document Structure (Cornell — per Pedoman)

| Bagian | Content | Notes |
|--------|---------|-------|
| Identitas | Kelompok 3 block, MNK202, Pertemuan 11, Dosen & tanggal | Dosen/tanggal read from syllabus; clearly-marked placeholder if absent |
| A — Cornell Notes | Two-column cue \| notes; the §3 coverage map in source order | substantive core; every term glossed on first use |
| B — Ringkasan | 1–2 paragraphs, own words | ≤ 15–20% of source length |
| C — Refleksi & Analisis | all 5 reflection questions; strengths **and** limitations | analytical, not descriptive — the A/B differentiator |
| D — Kesimpulan | core, benefit, practical implication, contribution | 150–250 words |
| E — Review Mandiri | ≥ 5 self-test questions with answers | active recall |
| F — Referensi | APA 7th | minimum `Scott, W. R. (2015). Financial accounting theory (7th ed.). Pearson Education Canada.` |

---

## 5. Folder Layout & Pipeline

Clone `rmk-pkk-pert10-statement-of-cash-flows/` →
`rmk-pkk-pert11-efficient-securities-markets/`:

```
rmk-pkk-pert11-efficient-securities-markets/
├── CLAUDE.md            # governing rules verbatim; Rust→Python exception log
├── README.md            # deterministic run order
├── Cargo.toml           # Rust workspace (pdf_probe, visual_gen)
├── requirements.txt     # PyMuPDF, python-docx, Pillow, (latex2mathml / mathml→omml)
├── input/{chapter,syllabus,rules}/
├── extraction/          # chapter-range.json, page-map.json, text/, verification-report.md
├── assets/{exhibits,diagrams,equations}/
├── content/             # 00_identitas.md, A_cornell.md … F_referensi.md
├── src/{rust,python}/
├── build/
└── output/01079_Kelompok 3_RMK Pert. 11.docx
```

| Stage | Tool | Output |
|-------|------|--------|
| 1 · PDF probe (page range + verification) | **Rust** `pdf_probe` | `extraction/chapter-range.json`, `verification-report.md` |
| 2 · Text extraction | **Python** PyMuPDF (documented exception) | `extraction/text/*.md`, `page-map.json` |
| 3 · Exhibit crop (Fig 4.1, Table 4.1, ToP 4.1 box, Fig 4.2) | **Python** PyMuPDF+Pillow (exception) | `assets/exhibits/*.png` |
| 4 · Diagram generation | **Rust** `visual_gen` | `assets/diagrams/*.png` |
| 5 · Equation render → OMML (Eq 4.1–4.4) | **new** (LaTeX→MathML→OMML) | `assets/equations/*.xml` (+ PNG fallback) |
| 6 · DOCX assembly | **Python** python-docx (exception) | `output/01079_Kelompok 3_RMK Pert. 11.docx` |

**Rust-first rationale & Python exceptions** (logged verbatim in `CLAUDE.md`, mirroring pert10):
PyMuPDF for text/crop because lopdf returns only footers on these SAGE/Pearson exports (no usable
ToUnicode CMap); python-docx for assembly because the proven K2/pert9/pert10 typography (exact
spacing, hanging indents, captioned tables, footer fields) is already encoded there.

---

## 6. Equations (D5 — native Word, with fallback)

Eq 4.1 (single-security return), 4.2 (expected return / CAPM), 4.3 (market model
`Rjt = αj + βjRMt + εjt`), 4.4 (beta `= Cov(Rj,RM)/Var(RM)`) are authored as LaTeX, converted to
MathML and then to **OMML** (Office Math) via the standard `OMML2MML.XSL`-inverse / `latex2mathml`
route, and injected into the python-docx document as native, editable Word equations. Each equation
is followed immediately by plain-Bahasa-Indonesia definitions of every variable.

**Safeguard:** during QA each equation's OMML is opened/validated; if any single equation fails to
validate or render, that one equation falls back to a high-DPI rendered PNG (route B) so a single
tricky equation cannot block the build. Fallbacks, if any, are logged in `CLAUDE.md`.

---

## 7. Language Pass — Humanize → Simplify

After the draft content exists, run `/content-research-writer` across all six sections:
- **Humanize:** vary sentence rhythm; remove AI tells (over-hedging, list-like prose, mechanical
  "Firstly/Secondly", prompt-restating); add genuine analytical connective tissue. Voice, never content.
- **Simplify:** shorten convoluted sentences; keep each technical term but pair with a brief plain gloss
  on first appearance; ensure first-pass comprehension. Simple yet professional, never dumbed-down.

Target register = the shipped pert10 voice. Every fact, figure, citation, and term is preserved.

---

## 8. Source-of-Truth Hierarchy

1. `Ketentuan Pembuatan RMK.png` + `Pedoman Penyusunan Resume Cornell Notes.pdf` (format & structure)
2. `Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf` (content — sole substantive source)
3. `Silabus_Pelaporan Keuangan Korporat_25-26.pdf` (scope & identity)
4. Master prompt / this spec (workflow & tech)

Never fabricate data, figures, citations, or equations not in the chapter PDF. If the rules PNG is
unreadable or a required detail is missing, stop and ask rather than guess.

---

## 9. Quality Gate (before emit)

- A4 · 1.5 spacing · Calibri 12 · ≥ 8 pages · `.docx`.
- Kelompok 3 identity block correct (6 members + NIMs).
- Cornell A–F present and rubric-aligned (Cornell 20% · summary 20% · analysis 25% · conclusion 15% ·
  active recall 10% · language & format 10%).
- Bagian C delivers real graduate analysis (strengths **and** limitations).
- Every §3 coverage-map concept present with a plain-language gloss.
- Figure 4.1, Table 4.1, ToP 4.1 box, Figure 4.2 cropped, resized, captioned, placed beside their
  explanation; Eq 4.1–4.4 typeset natively with variables defined; no margin overflow.
- Pipeline Rust-first; every Python exception justified in `CLAUDE.md`.
- Humanize → Simplify applied to all sections; reads human, deep, clear.
- Summary within 15–20%; conclusion 150–250 words; APA-7 references complete.
- Output filename exact: `01079_Kelompok 3_RMK Pert. 11.docx`.

---

## 10. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Chapter PDF text extraction garbled (CMap) | PyMuPDF exception (proven on pert9/10); verification-report cross-check |
| OMML equation fails to render in Word | Per-equation PNG fallback (§6); QA validation step |
| Document under 8 pages | Coverage map is broad; pert10 reached length comfortably; check at QA |
| Dosen/tanggal absent from syllabus | Clearly-marked placeholder per master-prompt instruction |
| Group-vs-individual ambiguity resurfaces | Only identity block + filename change; content unaffected |
