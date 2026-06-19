# Pert. 11 Canva Fill — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Insert the Pert. 11 presentation draft content into the live Canva design `DAHM_I0k_zo`, expanding template archetypes to ~20 pages, without altering the theme.

**Architecture:** The user manually duplicates + reorders template-archetype pages in Canva (the API cannot add pages). Claude then fills every new/template page's text via the Canva MCP editing transaction flow, in section-grouped batches, verifying each batch by reading the design content back. Pages 1–4 are left untouched.

**Tech Stack:** Canva MCP tools — `start-editing-transaction`, `perform-editing-operations`, `commit-editing-transaction`, `cancel-editing-transaction`, `get-design-content`, `get-design-pages`.

## Global Constraints

- Target design ID: **`DAHM_I0k_zo`** (edit link `https://www.canva.com/d/qEhNWUXUT5zGIAF`). Coordinate space **1920×1080**.
- **Never edit pages 1–4** — they are already filled and approved.
- **Theme is immutable:** no color, font-family, or layout-geometry changes. Use `replace_text` / `find_and_replace_text` / `delete_element` only; avoid `format_text` unless a slot visibly overflows.
- **Placeholder neutralization** on every filled page: `Studio Shodwe` → `Kelompok 3`; remove `www.reallygreatsite.com` / `hello@reallygreatsite.com` / `+123-456-7890`; `21 December, 2033` → `23 Juni 2026`; keep `Home / About Us / Contact Us` nav as visual chrome.
- **Zero placeholders** may remain after fill: no `Lorem ipsum`, `Studio Shodwe`, `reallygreatsite`, `2033` anywhere on filled pages.
- **Mandatory commit:** every `perform-editing-operations` run must be followed by `commit-editing-transaction` (uncommitted edits are lost). On any error, `cancel-editing-transaction`.
- Content source of truth: `docs/superpowers/specs/2026-06-19-pert11-canva-fill-design.md` §8 (copied inline into each task below).
- All on-slide copy is **Indonesian, professor-voice**; English terms kept verbatim.
- No new repo code. The only repo artifact is `progress/pert11-canva-worklog.md` (append-only log).

---

### Task 1: User duplicates + orders pages in Canva (manual checkpoint)

**Files:** none (manual Canva action by the user).

**Interfaces:**
- Produces: a deck of **19 pages** (pages 1–4 existing + 15 new), in the final order below, every new page still carrying its archetype's template placeholder text. (Optional 20th glossary page if the user wants it.)

**Duplication counts** (duplicate the named template page, then reorder):

| Archetype | Source page | Total instances | Extra duplicates |
|---|---|---|---|
| A_2check | p10 "Strategies" | 2 | +1 |
| A_3num | p8 "Challenges" | 2 | +1 |
| A_2x2 | p6 "Key Sectors" | 2 | +1 |
| A_2box | p9 "Role of Technology" | 3 | +2 |
| A_3cards | p7 "Benefits" | 2 | +1 |
| A_pills | p5 "Importance" | 1 | 0 |
| A_concl | p11 "Conclusion" | 1 | 0 |
| A_prose | p2 "Gambaran Umum" | 2 | +2 |

**Final page order** (archetype): 1 Cover · 2 Gambaran Umum · 3 Implikasi · 4 Pasar Efisien · 5 A_2check · 6 A_3num · 7 A_2x2 · 8 A_2box · 9 A_3num · 10 A_3cards · 11 A_2x2 · 12 A_2box · 13 A_pills · 14 A_concl · 15 A_3cards · 16 A_2box · 17 A_2check · 18 A_prose · 19 A_prose.

- [ ] **Step 1:** User duplicates pages per the table (8 extra duplicates) and arranges all pages into the final order. (In Canva: right-click page → Duplicate; drag in the page panel to reorder.)
- [ ] **Step 2:** Claude verifies — run `get-design-pages` for `DAHM_I0k_zo`. Expected: **19 pages** (or 20 with glossary). Record each page's `id` and `index`.
- [ ] **Step 3:** Claude spot-checks order — run `get-design-content` for pages `[5,6,7,8,9,10,11]`. Expected: page 5 shows "Strategies" placeholder text, page 6 "Challenges", page 7 "Key Sectors", page 8 "Role of Technology", page 9 "Challenges", page 10 "Benefits", page 11 "Key Sectors". If order differs, ask the user to correct before proceeding.
- [ ] **Step 4:** Append to `progress/pert11-canva-worklog.md`: "Task 1 done — N pages confirmed in order."

---

### Task 2: Pre-flight element map

**Files:** none (read-only Canva).

**Interfaces:**
- Consumes: 19-page ordered deck from Task 1.
- Produces: a confirmed mapping of each fill-page's editable text elements (captured live from the transaction), used by Tasks 3–7.

- [ ] **Step 1:** `start-editing-transaction` on `DAHM_I0k_zo`. Capture `transaction_id` and the `pages` array (element IDs + current text).
- [ ] **Step 2:** For pages 5–19, note for each: the title element(s), body/para element(s), per-item label + description elements, and the chrome elements (`Studio Shodwe`, date, website, nav). Match elements by their current placeholder text.
- [ ] **Step 3:** Confirm no page 1–4 element is in scope. If the transaction must stay open across tasks is not guaranteed, `cancel-editing-transaction` now and re-open per batch in Tasks 3–7 (transactions are cheap; element IDs are stable across a session unless pages change).
- [ ] **Step 4:** Append to worklog: "Task 2 done — element map captured."

---

### Task 3: Fill Section 2 — Efri (pages 5–6)

**Files:** none (Canva pages 5, 6).

**Interfaces:**
- Consumes: element map (Task 2).
- Produces: pages 5–6 filled; placeholders cleared.

**Page 5 — Konsensus (A_2check):**
- Title → `Pembentukan Harga:` / `Kekuatan Konsensus`
- Intro para → `Harga pasar mencerminkan rata-rata taksiran investor. Selama penilaian tidak bias dan independen, kesalahan individual saling menghapus — konsensus mengalahkan setiap peramal tunggal (Beaver, 1981: 619 ramalan, 1966–1968).`
- Check 1 label → `Rata-rata tak bias`; desc → `Kesalahan ke atas dan ke bawah saling meniadakan.`
- Check 2 label → `Independensi mutlak`; desc → `Tanpa independensi muncul share price momentum, bukan harga rasional.`

**Page 6 — Random Walk / Malkiel (A_3num):**
- Title → `Random Walk:` / `Dart vs Profesional`
- 01 label → `Profesional 10,9%`; desc → `Rata-rata return manajer profesional (100 kontes pertama WSJ).`
- 02 label → `Dart acak 4,5%`; desc → `Lemparan dart nyaris menyaingi — pasar adalah fair game.`
- 03 label → `Dow Jones 6,8%`; desc → `Tolok ukur indeks; sulit mengungguli pasar yang sudah efisien.`

- [ ] **Step 1:** `start-editing-transaction` → `transaction_id` + `pages`.
- [ ] **Step 2:** `perform-editing-operations` (page_index 5) with `replace_text`/`find_and_replace_text` ops for every Page-5 and Page-6 element above, plus chrome neutralization (`Studio Shodwe`→`Kelompok 3`; `21 December, 2033`→`23 Juni 2026`; clear website). Pass the `pages` array from Step 1.
- [ ] **Step 3:** `commit-editing-transaction`.
- [ ] **Step 4 (verify):** `get-design-content` pages `[5,6]`. Expected: contains `Kekuatan Konsensus`, `Dart vs Profesional`, `Beaver`, `10,9%`; does **not** contain `Lorem`, `Studio Shodwe`, `2033`, `reallygreatsite`. If any placeholder remains, re-open transaction and fix before continuing.
- [ ] **Step 5:** Append to worklog: "Task 3 done — pages 5–6 filled & verified."

---

### Task 4: Fill Section 3 — Dzaki (pages 7–8)

**Files:** none (Canva pages 7, 8).

**Interfaces:**
- Consumes: element map (Task 2).
- Produces: pages 7–8 filled; placeholders cleared.

**Page 7 — Paradoks Grossman (A_2x2):**
- Title → `Paradoks Informativeness` / `(Grossman, 1976)`
- Q1 label → `Harga fully informative`; desc → `Harga mencerminkan seluruh informasi relevan.`
- Q2 label → `Insentif lenyap`; desc → `Tak ada alasan menanggung biaya mencari informasi.`
- Q3 label → `Investor berhenti`; desc → `Pencarian informasi terhenti.`
- Q4 label → `Harga tak informatif`; desc → `Kontradiksi — ekuilibrium stabil tak terbentuk.`

**Page 8 — Noise Traders (A_2box):**
- Title → `Penyelesaian:` / `Noise Traders`
- Box 1 label → `Fully informative → insentif nol`; desc → `Jika harga merangkum segalanya, analisis tak bernilai.`
- Box 2 label → `Partially informative → analisis pulih`; desc → `Noise traders membuat investor tak bisa membedakan informasi dari noise; insentif analisis kembali.`

- [ ] **Step 1:** `start-editing-transaction`.
- [ ] **Step 2:** `perform-editing-operations` (page_index 7) for all Page-7/Page-8 elements above + chrome neutralization on both pages.
- [ ] **Step 3:** `commit-editing-transaction`.
- [ ] **Step 4 (verify):** `get-design-content` pages `[7,8]`. Expected: contains `Paradoks Informativeness`, `Grossman`, `Noise Traders`; no `Lorem`/`Studio Shodwe`/`2033`/`reallygreatsite`.
- [ ] **Step 5:** Append to worklog: "Task 4 done — pages 7–8 filled & verified."

---

### Task 5: Fill Section 4 — Prasetya (pages 9–11)

**Files:** none (Canva pages 9, 10, 11).

**Interfaces:**
- Consumes: element map (Task 2).
- Produces: pages 9–11 filled; placeholders cleared.

**Page 9 — CAPM (A_3num):**
- Title → `CAPM: Risiko, Return,` / `Harga Efisien`
- Equation (use the page's photo-area caption or a prominent text slot; if only numbered slots exist, prepend to the title's big line) → `E(Rjt) = Rf(1 − βj) + βj · E(RMt)`
- 01 label → `Rf`; desc → `Return aset bebas risiko.`
- 02 label → `βj`; desc → `Kepekaan saham terhadap pergerakan pasar.`
- 03 label → `E(RMt)`; desc → `Return pasar yang diharapkan.`

**Page 10 — Beta (A_3cards):**
- Title → `Beta: Hanya Risiko` / `Sistematis Dikompensasi`
- Card 1 label → `Beta tinggi`; desc → `Maskapai, produsen pesawat — peka siklus ekonomi; return harapan lebih besar.`
- Card 2 label → `Beta rendah`; desc → `Makanan cepat saji, utilitas — stabil; return harapan lebih kecil.`
- Card 3 label → `Risiko spesifik`; desc → `Terdiversifikasi habis. βj = Cov(j,M)/Var(M).`

**Page 11 — Market Model + Kritik (A_2x2):**
- Title → `Market Model &` / `Empat Gugatan`
- Equation (prepend to body or place in a free text slot) → `Rjt = αj + βj·RMt + εjt; E(εjt)=0`
- Q1 label → `Estimation risk`; desc → `Beta tak pernah diketahui pasti.`
- Q2 label → `Common knowledge`; desc → `Mengabaikan hedge fund di luar info publik.`
- Q3 label → `Biaya & likuiditas`; desc → `Fee, bid–ask spread, liquidity risk nyata.`
- Q4 label → `Rasionalitas`; desc → `Bias kognitif sistematis pasca-krisis 2007–08.`

- [ ] **Step 1:** `start-editing-transaction`.
- [ ] **Step 2:** `perform-editing-operations` (page_index 9) for all Page-9/10/11 elements + chrome neutralization on all three.
- [ ] **Step 3:** `commit-editing-transaction`.
- [ ] **Step 4 (verify):** `get-design-content` pages `[9,10,11]`. Expected: contains `CAPM`, `Beta`, `Market Model`, `Estimation risk`, `E(Rjt)`; no `Lorem`/`Studio Shodwe`/`2033`/`reallygreatsite`.
- [ ] **Step 5:** Append to worklog: "Task 5 done — pages 9–11 filled & verified."

---

### Task 6: Fill Section 5 — Odisiana (pages 12–15)

**Files:** none (Canva pages 12, 13, 14, 15).

**Interfaces:**
- Consumes: element map (Task 2).
- Produces: pages 12–15 filled; placeholders cleared.

**Page 12 — Dua Asimetri (A_2box):**
- Title → `Asimetri Informasi:` / `Dua Bentuk`
- Box 1 label → `Adverse selection`; desc → `Hidden information sebelum transaksi; orang dalam tahu kualitas aset.`
- Box 2 label → `Moral hazard`; desc → `Hidden action setelah transaksi; upaya manajer tak teramati.`

**Page 13 — Lemons (A_pills):**
- Title → `Lemons Problem` / `(Akerlof, 1970)`
- Para → `Pembeli tak bisa membedakan mobil bagus dari lemon, sehingga menekan harga semua ke kualitas rata-rata (pooling). Mobil bagus tersingkir — pasar dapat runtuh. Analogi saham: penjual = insider, pembeli = investor luar, catatan servis = laporan keuangan.`
- Pill 1 → `Pembeli tak tahu kualitas`
- Pill 2 → `Pooling: harga rata-rata`
- Pill 3 → `Mobil bagus tersingkir`
- Pill 4 → `Antidot: sertifikat, garansi, reputasi`

**Page 14 — Fundamental Value (A_concl):**
- Title → `Nilai Fundamental &` / `Peran Pelaporan`
- Para 1 → `Figure 4.2 — dua lingkaran konsentris. Lingkaran luar = fundamental value (harga ideal tanpa informasi orang dalam). Lingkaran dalam = harga efisien semi-strong yang mencerminkan informasi publik.`
- Para 2 → `Selisih kedua lingkaran = informasi orang dalam. Peran pelaporan keuangan: memperbesar lingkaran dalam mendekati nilai fundamental. "Yang dihargai pasar adalah informasi, bukan bentuknya."`

**Page 15 — Bukti Empiris (A_3cards):**
- Title → `Bukti: Pengungkapan` / `Menyusutkan Laba Insider`
- Card 1 label → `JLT (2011)`; desc → `24% transaksi di dalam blackout; 3,6%/180 hari, ≈0 dengan persetujuan general counsel.`
- Card 2 label → `Maffett (2012)`; desc → `42.930 reksa dana, 42 negara: kualitas pelaporan ↓ return abnormal.`
- Card 3 label → `SOX (2002)`; desc → `Menggeser harga menuju nilai fundamental; Enron & WorldCom sebagai antitesis.`

- [ ] **Step 1:** `start-editing-transaction`.
- [ ] **Step 2:** `perform-editing-operations` (page_index 12) for all Page-12/13/14/15 elements + chrome neutralization on all four.
- [ ] **Step 3:** `commit-editing-transaction`.
- [ ] **Step 4 (verify):** `get-design-content` pages `[12,13,14,15]`. Expected: contains `Adverse selection`, `Lemons Problem`, `Nilai Fundamental`, `JLT (2011)`, `Maffett`; no `Lorem`/`Studio Shodwe`/`2033`/`reallygreatsite`.
- [ ] **Step 5:** Append to worklog: "Task 6 done — pages 12–15 filled & verified."

---

### Task 7: Fill Section 6 — Kunthi (pages 16–19)

**Files:** none (Canva pages 16, 17, 18, 19).

**Interfaces:**
- Consumes: element map (Task 2).
- Produces: pages 16–19 filled; placeholders cleared. Deck content-complete.

**Page 16 — Signifikansi Sosial (A_2box):**
- Title → `Signifikansi Sosial:` / `Alokasi Modal Langka`
- Box 1 label → `Harga ≈ fundamental → alokasi efisien`; desc → `Perusahaan berinvestasi hingga profitabilitas marjinal = biaya marjinal.`
- Box 2 label → `Lemons / inside info → underinvestment`; desc → `Investor mundur, pasar kehilangan depth; proyek bermutu tersingkir.`

**Page 17 — Stick vs Carrots (A_2check):**
- Title → `Mendorong Pengungkapan:` / `Stick & Carrots`
- Intro para → `Dua mekanisme berdampingan. Bukti lintas-negara: Wurgler (2000), FHKP (2009), BHV (2009).`
- Check 1 label → `Stick — regulasi`; desc → `Standar minimum, kontrol insider trading, penalti.`
- Check 2 label → `Carrots — insentif pasar`; desc → `Reputasi, harga saham naik, biaya modal turun → pengungkapan sukarela.`

**Page 18 — Sintesis / Slogan (A_prose):**
- Title → `Simpulan Bab 4`
- Body → `"Yang dihargai pasar adalah informasi, bukan bentuknya." Rasionalitas berlaku rata-rata, bukan seragam. Noise traders menyelamatkan insentif analisis. Selalu ada residual informasi orang dalam — di sanalah peran akuntansi: memperkecil gap lewat pengungkapan yang berguna dan hemat biaya. Asimetri informasi adalah alasan akuntansi ada.`

**Page 19 — Penutup (A_prose):**
- Title → `Yang Kini Anda Kuasai`
- Body (4 poin, as list lines in the body text element) →
  `Pasar menghargai informasi, bukan bentuk.`
  `Asimetri informasi: alasan akuntansi ada.`
  `Full disclosure → alokasi modal efisien.`
  `Pelaporan berkualitas = kepentingan sosial.`

- [ ] **Step 1:** `start-editing-transaction`.
- [ ] **Step 2:** `perform-editing-operations` (page_index 16) for all Page-16/17/18/19 elements + chrome neutralization on all four.
- [ ] **Step 3:** `commit-editing-transaction`.
- [ ] **Step 4 (verify):** `get-design-content` pages `[16,17,18,19]`. Expected: contains `Signifikansi Sosial`, `Stick & Carrots`, `Simpulan Bab 4`, `Yang Kini Anda Kuasai`; no `Lorem`/`Studio Shodwe`/`2033`/`reallygreatsite`.
- [ ] **Step 5:** Append to worklog: "Task 7 done — pages 16–19 filled & verified."

---

### Task 8: Optional glossary + full-deck QA

**Files:** none (Canva), `progress/pert11-canva-worklog.md`.

**Interfaces:**
- Consumes: filled deck (Tasks 3–7).
- Produces: final verified deck ready for export.

**Page 20 — Glosarium (A_concl) — only if user added the page:**
- Title → `Glosarium — Rujukan Tanya-Jawab`
- Body → `Efficient market · Fair game · Random walk · Noise traders / partially informative · CAPM / beta / market model · Adverse selection / moral hazard · Lemons problem · Fundamental value · Estimation risk.`

- [ ] **Step 1 (if glossary page exists):** Fill page 20 via a transaction + commit, then verify with `get-design-content` page `[20]`.
- [ ] **Step 2 (full QA):** `get-design-content` for **all** pages. Assert across the whole deck: zero occurrences of `Lorem`, `Studio Shodwe`, `reallygreatsite`, `2033`, `Creative Economy`. List any hit and fix in a follow-up transaction.
- [ ] **Step 3 (visual QA):** `get-design-pages` and review thumbnails for overflow/clipping on the densest pages (9 CAPM, 11 market model, 13 lemons). If text overflows a slot, shorten the copy (do not resize/restyle) and re-commit.
- [ ] **Step 4:** Confirm pages 1–4 still match their original content (regression check) via `get-design-content` `[1,2,3,4]`.
- [ ] **Step 5:** Append to worklog: "Task 8 done — full-deck QA passed; ready for export." Tell the user the deck is ready and they can export to PDF/PPTX from Canva.

---

## Self-Review

**Spec coverage:** Spec §5 page map (S7–S23) → Tasks 3–7 cover pages 5–19 one-to-one; §8 content copied inline per page; optional glossary (§5 pg 20) → Task 8; §7 neutralization → Global Constraints + every fill task Step 2; §9 mechanics → transaction/commit/verify steps; §6 duplication → Task 1; pages 1–4 keep (§2) → Global Constraints + Task 8 Step 4 regression. No gaps.

**Placeholder scan:** No `TBD`/`TODO`; every page's exact replacement strings are inline. Equation-slot placement on pages 9/11 is given a concrete fallback ("prepend to title big line / body") rather than left open.

**Type/name consistency:** Archetype names (A_2check, A_3num, A_2x2, A_2box, A_3cards, A_pills, A_concl, A_prose) used identically in spec and plan. Page numbers consistent between Task 1 final order and Tasks 3–7. Design ID `DAHM_I0k_zo` consistent throughout.
