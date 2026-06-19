# Pert. 11 Slide-Presentation-Draft Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write `presentation-guidance/slide-presentation-draft-pert11.md` — a ~24-slide, Winston-compliant deck spec for Claude Design, covering Scott Ch. 4 (Efficient Securities Markets) with the 6-speaker mapping intact.

**Architecture:** A single Markdown file. A header block (Slide-Crime Audit + the Star + delivery rules), then ~24 slide blocks each carrying 5 fields (Headline · On-slide text · Visual · Speaker script · Design hint). Content is drawn verbatim-in-substance from `panduan-presentasi-kelompok3-pert11.md`; no new facts. Tasks are sliced by speaker section so each is independently reviewable.

**Tech Stack:** Markdown only. No build step. Verification is a manual checklist against the spec's acceptance criteria.

## Global Constraints

- Output path: `presentation-guidance/slide-presentation-draft-pert11.md` (verbatim).
- Language: Indonesian professor-voice; English technical terms kept verbatim.
- Headlines are full sentence-assertions, not topic labels (Winston).
- On-slide text budget: ≤4 bullets per slide, ≤6 words per bullet (forces ≥40pt).
- Section→member mapping = exactly that of `panduan-presentasi-kelompok3-pert11.md`.
- Never fabricate figures; every number traces to the panduan/chapter.
- Reference the 6 assets by relative path; never edit or regenerate them.
- Final slide = Contributions close. No "Terima kasih" / "Pertanyaan?" / collaborator-list slide.
- Slogan verbatim: *"Yang dihargai pasar adalah informasi, bukan bentuknya."*
- The 6 assets (must each appear ≥1×): `assets/exhibits/fig-4-1.png`, `assets/diagrams/efficiency-forms.png`, `assets/exhibits/table-4-1.png`, `assets/exhibits/tip-4-1.png`, `assets/diagrams/adverse-selection.png`, `assets/exhibits/fig-4-2.png`.

---

### Task 1: Document header + Vision slides (S1–S3)

**Files:**
- Create: `presentation-guidance/slide-presentation-draft-pert11.md`

**Interfaces:**
- Produces: the file, the field-schema convention, the Slide-Crime Audit table, the Star block, and slides S1–S3 that later tasks append to.

- [ ] **Step 1: Write the file front-matter + intro blocks**
  - H1 title; one-line purpose ("Spec for Claude Design — do not treat as final visual").
  - **Slide-Crime Audit** table (10 crimes + fix) copied from the spec.
  - **The Star** block (Symbol/Slogan/Surprise/Salient/Story) copied from the spec.
  - **Delivery rules** list: stand beside screen, slide text ≠ script, white space mandatory, 2 prop moments flagged.
  - A "Field schema" note explaining the 5 per-slide fields.

- [ ] **Step 2: Write S1 Cover**
  - Headline: deck title — *"Efficient Securities Markets — Mengapa Pasar Menghargai Informasi, Bukan Bentuknya"*.
  - On-slide: course (Pelaporan Keuangan Korporat / MNK202), Pertemuan 11, Kelompok 3, 6 members + NIM (from panduan identitas table).
  - Visual: group photo optional (`input/rules/Grup 3 PKK Pasca UTS.jpeg`) or clean title — note "members appear here only (crime #9)".
  - Design hint: title-dominant, generous white space, no logos.

- [ ] **Step 3: Write S2 Empowerment Promise**
  - Headline = the promise (verbatim seed from spec).
  - On-slide: 2 short outcome bullets ("Anda bisa menjelaskan…").
  - Speaker script: Winston rule — no joke, no "terima kasih sudah hadir"; first 60s earns the next 60 min.
  - Design hint: one sentence centered, huge type.

- [ ] **Step 4: Write S3 Roadmap**
  - Headline: *"Empat langkah: dari pasar efisien ke pengungkapan penuh."*
  - Visual: `assets/exhibits/fig-4-1.png` — caption "Organisasi Bab 4 (Scott)".
  - On-slide: the 6 section→speaker line-up (compact).
  - Design hint: full-width flowchart, speaker names as a thin band beneath.

- [ ] **Step 5: Verify Task 1**
  - Open the file; confirm header tables render, S1–S3 each have all 5 fields, `fig-4-1.png` referenced, no thank-you content. Fix inline.

---

### Task 2: Adinda — Definition & forms (S4–S6)

**Files:**
- Modify: `presentation-guidance/slide-presentation-draft-pert11.md` (append)

**Interfaces:**
- Consumes: file + schema from Task 1.
- Produces: S4–S6 (Section 4.1 + 4.2.1).

- [ ] **Step 1: S4 — Efficient market defined**
  - Headline: *"Pasar efisien: harga mencerminkan sepenuhnya informasi publik."*
  - On-slide: Fama 1970 · semi-strong · arbitrage · informed investors.
  - Script: semi-strong vs strong; arbitrage = the aligning engine; efficiency is a *model*, not perfection (post-2007–08).
  - Design hint: definition card + small "model, not perfection" callout.

- [ ] **Step 2: S5 — Three forms**
  - Headline: *"Tiga bentuk efisiensi: weak ⊂ semi-strong ⊂ strong."*
  - Visual: `assets/diagrams/efficiency-forms.png` — caption "Tiga bentuk (Fama 1970)".
  - Design hint: full-bleed nested diagram; semi-strong highlighted as the chapter's focus.

- [ ] **Step 3: S6 — Four properties**
  - Headline: *"Empat sifat: relatif, bukan mahatahu, fair game, random walk."*
  - On-slide: 4 bullets (relatif ke info publik / bukan kemahatahuan / fair game / random walk).
  - Script: insider-trading room; ABS pricing 2007–08; CAPM as benchmark; serial run w/o news = inefficiency.
  - Design hint: 2×2 grid, one icon each.

- [ ] **Step 4: Verify Task 2** — S4–S6 present, `efficiency-forms.png` referenced, bullets within budget, headlines are assertions. Fix inline.

---

### Task 3: Efri — Pricing mechanism & implications 1–2 (S7–S9)

**Files:** Modify the file (append).

**Interfaces:** Consumes Task 1 schema. Produces S7–S9 (4.2.2 + 4.3 i.1–2).

- [ ] **Step 1: S7 — Consensus (the Surprise)**
  - Headline: *"Konsensus mengalahkan setiap peramal individual."*
  - Visual: `assets/exhibits/table-4-1.png` — caption "Beaver (1981): 619 ramalan, 1966–68".
  - On-slide: unbiased averaging · independence required.
  - Script: car analogy; errors cancel; independence → else momentum. Flag this as a Star "Surprise" beat.
  - Design hint: table left, one-line takeaway right.

- [ ] **Step 2: S8 — Malkiel random walk**
  - Headline: *"Dart acak menyaingi manajer profesional — karena fair game."*
  - Visual: `assets/exhibits/tip-4-1.png` — caption "Theory in Practice 4.1".
  - On-slide stat: pros 10.9% · darts 4.5% · DJ 6.8% (WSJ, 100 kontes).
  - Script: Malkiel's defenses (risk, big-firm 1990s, Reg FD post-2000).
  - Design hint: three-stat bar callout beside the exhibit.

- [ ] **Step 2b (prop note):** none here; prop moments reserved for S17/S18.

- [ ] **Step 3: S9 — Implications 1–2 (Beaver 1973)**
  - Headline: *"Kebijakan tanpa efek kas tak menggerakkan harga; full disclosure menang."*
  - On-slide: (1) no cash-flow → no price move · (2) full disclosure.
  - Script: straight-line vs declining-balance = paper only; market sees through; IAS 1 policy disclosure; benefit > cost.
  - Design hint: two stacked implication cards.

- [ ] **Step 4: Verify Task 3** — S7–S9 present, `table-4-1.png` + `tip-4-1.png` referenced, stats match panduan exactly. Fix inline.

---

### Task 4: Dzaki — Implications 3–4 & informativeness (S10–S12)

**Files:** Modify the file (append).

**Interfaces:** Consumes Task 1 schema. Produces S10–S12 (4.3 i.3–4 + 4.4).

- [ ] **Step 1: S10 — Implications 3–4**
  - Headline: *"Investor naif terlindungi harga; akuntan bersaing untuk bertahan."*
  - On-slide: (3) price-protected · (4) accountants compete → decision usefulness.
  - Script: naif can hire/imitate; four implications underpin decision usefulness → Conceptual Framework.
  - Design hint: two cards + a small "→ Conceptual Framework" link.

- [ ] **Step 2: S11 — Grossman paradox**
  - Headline: *"Jika harga sepenuhnya informatif, insentif mencari informasi lenyap."*
  - On-slide: fully informative → no search → price stops reflecting → wild oscillation.
  - Script: Grossman (1976); threatens usefulness of statement analysis.
  - Design hint: a broken-loop diagram (build: arrows collapsing).

- [ ] **Step 3: S12 — Noise traders resolution**
  - Headline: *"Noise traders membuat harga hanya* partially informative *— analisis pulih."*
  - On-slide: noise traders · rational expectations · partially informative.
  - Script: can't tell superior info from noise; incentive restored via analysis, conservatism signal, voluntary disclosure, MD&A; big firms' prices more informative.
  - Design hint: contrast panel "fully vs partially informative".

- [ ] **Step 4: Verify Task 4** — S10–S12 present, Grossman→noise-trader logic intact, "partially informative" used. Fix inline.

---

### Task 5: Prasetya — CAPM (S13–S15)

**Files:** Modify the file (append).

**Interfaces:** Consumes Task 1 schema. Produces S13–S15 (4.5).

- [ ] **Step 1: S13 — CAPM equation**
  - Headline: *"CAPM menautkan harga efisien, risiko, dan return."*
  - On-slide (large, one line): E(Rjt) = Rf(1 − βj) + βj · E(RMt).
  - Script: ex post vs ex ante return; assumptions (rational risk-averse, Rf exists, efficient, zero transaction cost). Deliver equation slowly, point at each symbol (Winston: not a laser — built-in highlight).
  - Design hint: equation centered, each symbol annotated; no clutter.

- [ ] **Step 2: S14 — Beta / systematic risk**
  - Headline: *"Hanya risiko sistematis (beta) yang dikompensasi."*
  - On-slide: βj = Cov(j,M)/Var(M) · high: airlines/aircraft · low: fast-food/utilities.
  - Script: firm-specific risk diversifies away; E(Rjt) = cost of equity capital.
  - Design hint: beta scale visual, two example chips.

- [ ] **Step 3: S15 — Market model + critique**
  - Headline: *"Market model memisah return harapan dari abnormal — lalu empat asumsinya digugat."*
  - On-slide: Rjt = αj + βj·RMt + εjt · E(εjt)=0 · 4 critiques.
  - Script: three uses; four-assumption critique post-2007–08 (estimation risk, common knowledge/hedge funds, zero-cost/liquidity, rationality); CAPM understates cost of capital but remains a useful starting point.
  - Design hint: equation top, 4-item critique list below.

- [ ] **Step 4: Verify Task 5** — equations exact, no fabricated betas, S13–S15 present. Fix inline.

---

### Task 6: Odisiana — Information asymmetry (S16–S19)

**Files:** Modify the file (append).

**Interfaces:** Consumes Task 1 schema. Produces S16–S19 (4.6). Contains the Symbol (S18).

- [ ] **Step 1: S16 — Two asymmetries**
  - Headline: *"Asimetri informasi: adverse selection vs moral hazard."*
  - On-slide: adverse selection = hidden info (pre) · moral hazard = hidden action (post).
  - Script: unknown parameter each; raises cost of capital; can cause market incompleteness.
  - Design hint: side-by-side compare card.

- [ ] **Step 2: S17 — Lemons story (prop moment)**
  - Headline: *"Pembeli tak bisa bedakan mobil bagus dari* lemon *— harga semua tertekan."*
  - Visual: `assets/diagrams/adverse-selection.png` — caption "Adverse selection → antidot full disclosure".
  - Script: Akerlof (1970) pooling; certificates/warranty/reputation; seller = insider. **PROP:** hold up a used-car key — "informasi yang Anda tak punya."
  - Design hint: flow diagram full width; prop cue in notes only.

- [ ] **Step 3: S18 — Fundamental value (THE SYMBOL)**
  - Headline: *"Selisih dua lingkaran itu = informasi orang dalam."*
  - Visual: `assets/exhibits/fig-4-2.png` — caption "Figure 4.2: peran pelaporan keuangan".
  - On-slide: outer = fundamental value · inner = public info · gap = inside info.
  - Script: reporting turns inside info into outside info — grows the inner circle, never quite touches the outer. **PROP:** sealed envelope = inside information. Repeat the **Slogan** verbatim here.
  - Design hint: the concentric circles as the hero image; minimal text.

- [ ] **Step 4: S19 — Evidence**
  - Headline: *"Bukti: pengungkapan superior menyusutkan laba orang dalam."*
  - On-slide: JLT (2011): 24% trades in blackout; 3.6%/180d, ~0 w/ general counsel · Maffett (2012): 42,930 funds, 42 negara · SOX (2002).
  - Script: general counsel > blackout period; SOX shifts price toward fundamental value; Enron/WorldCom inner circle collapse.
  - Design hint: 3 evidence chips, one stat each.

- [ ] **Step 5: Verify Task 6** — `adverse-selection.png` + `fig-4-2.png` referenced, Slogan appears at S18, both prop moments flagged, JLT stats exact. Fix inline.

---

### Task 7: Kunthi — Social significance, synthesis, Contributions close (S20–S24)

**Files:** Modify the file (append).

**Interfaces:** Consumes Task 1 schema + the S2 promise (to mirror at S23). Produces S20–S24 (4.7 + 4.8 + close + appendix).

- [ ] **Step 1: S20 — Social significance**
  - Headline: *"Pasar yang bekerja baik mengalokasikan modal yang langka."*
  - On-slide: price ≈ fundamental value → efficient capital allocation; lemons → underinvestment + lost depth.
  - Script: invest until marginal profitability = marginal cost.
  - Design hint: simple capital-flow visual.

- [ ] **Step 2: S21 — Stick vs carrots + evidence**
  - Headline: *"Regulasi (stick) dan insentif pasar (carrots) berdampingan."*
  - On-slide: stick = penalties/regulation · carrots = reputation, higher price, lower cost of capital · 2 social conditions.
  - Script: cross-country evidence — Wurgler (2000, 65 negara), FHKP (2009), BHV (2009).
  - Design hint: balance-scale visual; evidence as a thin footer band.

- [ ] **Step 3: S22 — Chapter synthesis**
  - Headline: the **Salient idea** — *"Asimetri informasi adalah alasan akuntansi ada."*
  - On-slide: the **Slogan** verbatim (2nd verbatim occurrence) + 3 takeaways.
  - Script: rationality on average not uniform; Grossman saved by noise traders; CAPM critiqued yet evidence still consistent with efficiency.
  - Design hint: slogan as hero line.

- [ ] **Step 4: S23 — Contributions close (mirrors S2)**
  - Headline: *"Yang kini Anda kuasai."* (NOT thank-you / questions)
  - On-slide: 3–4 contribution bullets that mirror the S2 promise (information not form · asymmetry = why accounting exists · full disclosure → fundamental value → better capital allocation).
  - Script: restate promise kept; then open discussion verbally (no Q&A slide).
  - Design hint: stays on screen during Q&A; mirrors S2 layout.

- [ ] **Step 5: S24 — Appendix / glossary**
  - On-slide: compact glossary from panduan (efficient market, fair game, random walk, noise traders, CAPM/beta, adverse selection/moral hazard, lemons, fundamental value, estimation risk).
  - Design hint: two-column reference, low-emphasis; "back-up for Q&A".

- [ ] **Step 6: Verify Task 7** — S20–S24 present; S23 mirrors S2 and has no thank-you/Q&A; Slogan now appears ≥2× total; cross-country evidence exact. Fix inline.

---

### Task 8: Final acceptance pass

**Files:** Modify the file (fixes only).

**Interfaces:** Consumes the whole file.

- [ ] **Step 1: Run the spec acceptance checklist**
  - Using superpowers:verification-before-completion, check all 8 acceptance criteria from the spec:
    1. File at correct path.
    2. Slide-Crime Audit table present; 10 crimes addressed.
    3. ~22–24 blocks, each with all 5 fields.
    4. All 6 assets referenced ≥1×.
    5. S2 promise present; S23 contributions close; no thank-you/Q&A.
    6. Slogan verbatim ≥2×.
    7. Every numeric claim traces to panduan; spot-check 5 numbers.
    8. Section→member mapping matches panduan exactly.

- [ ] **Step 2: Fix any failures inline; re-check only the failed items.**

- [ ] **Step 3 (optional, on user request): commit**
  - Per repo convention, commit only if the user asks. If asked: branch off `master`, stage the spec + plan + draft, commit with a `content(pert11-slides)` message.

---

## Self-Review (plan vs spec)

- **Spec coverage:** field schema → Task 1 Step 1; Slide-Crime Audit → T1; the Star → T1 + slogan at S18/S22; empowerment promise → S2; persuasion structure → S1–3 vision + S23 close; 24-slide map → T1–T7 cover S1–S24; all 6 assets → fig-4-1 (S3), efficiency-forms (S5), table-4-1 (S7), tip-4-1 (S8), adverse-selection (S17), fig-4-2 (S18); acceptance criteria → Task 8. No gaps.
- **Placeholder scan:** every slide step names its headline, visual, and script substance; no TBD/TODO. Clean.
- **Type consistency:** asset paths identical to Global Constraints; slogan string identical everywhere; slide numbering S1–S24 contiguous and non-overlapping across tasks. Consistent.
