# Design Spec — Insert Pert. 11 Presentation Draft into the Canva Deck

**Date:** 2026-06-19
**Author:** Dzaki Muhammad Yusfian (Kelompok 3, MNK202 Pelaporan Keuangan Korporat)
**Status:** Awaiting user review

---

## 1. Goal

Insert the content of the Pertemuan 11 presentation draft
(`rmk-pkk-pert11-efficient-securities-markets/presentation-guidance/slide-presentation-draft-pert11.md`)
into the existing Canva design **"Salinan dari PPT PKK KELOMPOK 3"** (`DAHM_I0k_zo`),
**without changing the theme or visual design**. Only the *information* is adjusted to fit the
template's existing layouts perfectly.

## 2. Locked decisions (from brainstorming)

| Decision | Choice |
|---|---|
| Target design | `DAHM_I0k_zo` — 11 pages, 1920×1080, edit link `https://www.canva.com/d/qEhNWUXUT5zGIAF` |
| Slide structure | **Expand** — each remaining draft topic gets its own page (~20 pages total) |
| Pages 1–4 | **Keep as-is** (already filled with real Kelompok 3 content) |
| Build mechanism | **User duplicates pages in Canva per the map below; Claude fills every page via Canva MCP** |
| Placeholder chrome | **Neutralize wrong text** (Studio Shodwe → Kelompok 3 / MNK202, remove `reallygreatsite.com`, date → `23 Juni 2026`); **keep** nav-bar styling + theme colors/shapes |
| Visuals | Keep the template's existing illustrations by default (theme preservation). Equations rendered as plain text in text slots. A few slides flagged for optional custom diagrams (later enhancement). |

## 3. Constraints discovered

- **The Canva editing API cannot add or duplicate pages** — only edit existing elements
  (`replace_text`, `find_and_replace_text`, `update_fill`, `insert_fill`, `format_text`,
  `position_element`, `resize_element`, `delete_element`, `update_title`). Therefore the user
  must create the duplicate pages manually in Canva first.
- **Text elements cannot be added** via MCP (only media via `insert_fill`). So each topic must map
  to an archetype whose existing text-slot count fits the content. Bullet lists either fill one
  multi-line text element or one slot each, never new elements.
- Coordinate space for any positioning/resizing is **1920×1080** (not the 1440×810 PDF export).

## 4. Current live-design state

| Page | State | Content |
|---|---|---|
| 1 | KEEP | Cover — title, 6 members + NIMs, "Kelompok 3", 23 Juni 2026 |
| 2 | KEEP | *Gambaran Umum* — efficient-market overview |
| 3 | KEEP | *Implikasi Penting bagi Akuntansi* — 4 numbered implications |
| 4 | KEEP | *Pasar Sekuritas Efisien* — Fama definition + 4 properties |
| 5 | FILL | Template "Importance" — title + para + 4 pills + photo  (archetype **A_pills**) |
| 6 | FILL | Template "Key Sectors" — title + 2×2 headed paras + illustration  (**A_2x2**) |
| 7 | FILL | Template "Benefits" — centered title + 3 cards  (**A_3cards**) |
| 8 | FILL | Template "Challenges" — title + photo + 3 numbered 01/02/03  (**A_3num**) |
| 9 | FILL | Template "Role of Technology" — title + illustration + 2 boxes  (**A_2box**) |
| 10 | FILL | Template "Strategies" — title + para + 2 check items + photo  (**A_2check**) |
| 11 | FILL | Template "Conclusion / Thank You" — title + 2 paras + illustration  (**A_concl**) |

Archetypes also available by duplicating filled pages: **A_prose** (p2 "Gambaran Umum" style:
title + body + photo).

## 5. Remaining draft topics → archetype → final page order

Pages 1–4 already cover draft S1, S2, S9–S10, S4–S6. The remaining topics, in pedagogical order:

| Final pg | Draft | Topic | Archetype |
|---|---|---|---|
| 1–4 | S1,S2,S9–10,S4–6 | (existing — keep) | — |
| 5 | S7 | Konsensus / Beaver | A_2check |
| 6 | S8 | Random walk / Malkiel (3 stats) | A_3num |
| 7 | S11 | Paradoks Grossman (4-node loop) | A_2x2 |
| 8 | S12 | Noise traders (2-col contrast) | A_2box |
| 9 | S13 | CAPM equation (3 symbol callouts) | A_3num |
| 10 | S14 | Beta / systematic risk (3 cards) | A_3cards |
| 11 | S15 | Market model + 4 critiques | A_2x2 |
| 12 | S16 | Dua asimetri (adverse/moral) | A_2box |
| 13 | S17 | Lemons problem (4 bullets) | A_pills |
| 14 | S18 | Fundamental value (Fig 4.2) | A_concl |
| 15 | S19 | Bukti empiris (3 studies) | A_3cards |
| 16 | S20 | Signifikansi sosial (2-branch) | A_2box |
| 17 | S21 | Stick vs carrots (+ evidence) | A_2check |
| 18 | S22 | Sintesis / slogan | A_prose |
| 19 | S23 | Penutup / contributions close | A_prose |
| 20 | S24 | Glosarium (appendix) — **OPTIONAL** | A_concl |

## 6. Duplication instructions (what the user does in Canva)

Final deck = pages 1–4 (untouched) + 15 new content pages (+ optional glossary). Each new page is a
**duplicate of the matching template archetype page**, which Claude then overwrites. Instance counts:

| Archetype | Source template page | Instances needed | Duplicates to create |
|---|---|---|---|
| A_2check | p10 "Strategies" | 2 (pg 5, 17) | +1 |
| A_3num | p8 "Challenges" | 2 (pg 6, 9) | +1 |
| A_2x2 | p6 "Key Sectors" | 2 (pg 7, 11) | +1 |
| A_2box | p9 "Role of Technology" | 3 (pg 8, 12, 16) | +2 |
| A_3cards | p7 "Benefits" | 2 (pg 10, 15) | +1 |
| A_pills | p5 "Importance" | 1 (pg 13) | 0 |
| A_concl | p11 "Conclusion" | 1 (pg 14) [+1 if glossary] | 0 (+1 optional) |
| A_prose | p2 "Gambaran Umum" | 2 (pg 18, 19) | +2 |

After duplicating, arrange all pages into the **final order** in §5. Claude then fills each by page
index. (Claude will re-read pages before filling, so exact ordering can be confirmed live.)

## 7. Placeholder neutralization (apply to every FILLED page)

- `Studio Shodwe` → `Kelompok 3` (or `Kelompok 3 · MNK202`)
- `www.reallygreatsite.com`, `hello@reallygreatsite.com`, `+123-456-7890` → remove (clear text)
- `21 December, 2033` → `23 Juni 2026`
- `Home / About Us / Contact Us` nav labels → **keep as visual chrome** (do not remove)
- All `Lorem ipsum…` → replaced by the per-page content in §8

## 8. Per-page fill content (Indonesian, professor-voice)

Title format follows the template's two-line pattern (small top line / big phrase). Each item shows
**slot label → text**. English terms kept verbatim per draft.

### Pg 5 — Konsensus (S7) · A_2check
- **Title:** "Pembentukan Harga: / Kekuatan Konsensus"
- **Intro para:** "Harga pasar mencerminkan rata-rata taksiran investor. Selama penilaian tidak bias dan independen, kesalahan individual saling menghapus — konsensus mengalahkan setiap peramal tunggal (Beaver, 1981: 619 ramalan, 1966–1968)."
- **Check 1:** "Rata-rata tak bias" → "Kesalahan ke atas dan ke bawah saling meniadakan."
- **Check 2:** "Independensi mutlak" → "Tanpa independensi muncul share price momentum, bukan harga rasional."

### Pg 6 — Random Walk / Malkiel (S8) · A_3num
- **Title:** "Random Walk: / Dart vs Profesional"
- **01 Profesional 10,9%** → "Rata-rata return manajer profesional (100 kontes pertama WSJ)."
- **02 Dart acak 4,5%** → "Lemparan dart nyaris menyaingi — pasar adalah fair game."
- **03 Dow Jones 6,8%** → "Tolok ukur indeks; sulit mengungguli pasar yang sudah efisien."

### Pg 7 — Paradoks Grossman (S11) · A_2x2
- **Title:** "Paradoks Informativeness / (Grossman, 1976)"
- **Q1 Harga fully informative** → "Harga mencerminkan seluruh informasi relevan."
- **Q2 Insentif lenyap** → "Tak ada alasan menanggung biaya mencari informasi."
- **Q3 Investor berhenti** → "Pencarian informasi terhenti."
- **Q4 Harga tak informatif** → "Kontradiksi — ekuilibrium stabil tak terbentuk."

### Pg 8 — Noise Traders (S12) · A_2box
- **Title:** "Penyelesaian: / Noise Traders"
- **Box 1 Fully informative → insentif nol** → "Jika harga merangkum segalanya, analisis tak bernilai."
- **Box 2 Partially informative → analisis pulih** → "Noise traders membuat investor tak bisa membedakan informasi dari noise; insentif analisis kembali."

### Pg 9 — CAPM (S13) · A_3num
- **Title:** "CAPM: Risiko, Return, / Harga Efisien"
- **Equation (prominent text):** `E(Rjt) = Rf(1 − βj) + βj · E(RMt)`
- **01 Rf** → "Return aset bebas risiko."
- **02 βj** → "Kepekaan saham terhadap pergerakan pasar."
- **03 E(RMt)** → "Return pasar yang diharapkan."

### Pg 10 — Beta (S14) · A_3cards
- **Title:** "Beta: Hanya Risiko / Sistematis Dikompensasi"
- **Card 1 Beta tinggi** → "Maskapai, produsen pesawat — peka siklus ekonomi; return harapan lebih besar."
- **Card 2 Beta rendah** → "Makanan cepat saji, utilitas — stabil; return harapan lebih kecil."
- **Card 3 Risiko spesifik** → "Terdiversifikasi habis. βj = Cov(j,M)/Var(M)."

### Pg 11 — Market Model + Kritik (S15) · A_2x2
- **Title:** "Market Model & / Empat Gugatan"
- **Equation (text):** `Rjt = αj + βj·RMt + εjt;  E(εjt)=0`
- **Q1 Estimation risk** → "Beta tak pernah diketahui pasti."
- **Q2 Common knowledge** → "Mengabaikan hedge fund di luar info publik."
- **Q3 Biaya & likuiditas** → "Fee, bid–ask spread, liquidity risk nyata."
- **Q4 Rasionalitas** → "Bias kognitif sistematis pasca-krisis 2007–08."

### Pg 12 — Dua Asimetri (S16) · A_2box
- **Title:** "Asimetri Informasi: / Dua Bentuk"
- **Box 1 Adverse selection** → "Hidden information sebelum transaksi; orang dalam tahu kualitas aset."
- **Box 2 Moral hazard** → "Hidden action setelah transaksi; upaya manajer tak teramati."

### Pg 13 — Lemons (S17) · A_pills
- **Title:** "Lemons Problem / (Akerlof, 1970)"
- **Para:** "Pembeli tak bisa membedakan mobil bagus dari lemon, sehingga menekan harga semua ke kualitas rata-rata (pooling). Mobil bagus tersingkir — pasar dapat runtuh. Analogi saham: penjual = insider, pembeli = investor luar, catatan servis = laporan keuangan."
- **Pill 1** → "Pembeli tak tahu kualitas"
- **Pill 2** → "Pooling: harga rata-rata"
- **Pill 3** → "Mobil bagus tersingkir"
- **Pill 4** → "Antidot: sertifikat, garansi, reputasi"

### Pg 14 — Fundamental Value (S18) · A_concl
- **Title:** "Nilai Fundamental & / Peran Pelaporan"
- **Para 1:** "Figure 4.2 — dua lingkaran konsentris. Lingkaran luar = fundamental value (harga ideal tanpa informasi orang dalam). Lingkaran dalam = harga efisien semi-strong yang mencerminkan informasi publik."
- **Para 2:** "Selisih kedua lingkaran = informasi orang dalam. Peran pelaporan keuangan: memperbesar lingkaran dalam mendekati nilai fundamental. 'Yang dihargai pasar adalah informasi, bukan bentuknya.'"
- *Optional custom visual: concentric-circles diagram (`fig-4-2.png`).*

### Pg 15 — Bukti Empiris (S19) · A_3cards
- **Title:** "Bukti: Pengungkapan / Menyusutkan Laba Insider"
- **Card 1 JLT (2011)** → "24% transaksi di dalam blackout; 3,6%/180 hari, ≈0 dengan persetujuan general counsel."
- **Card 2 Maffett (2012)** → "42.930 reksa dana, 42 negara: kualitas pelaporan ↓ return abnormal."
- **Card 3 SOX (2002)** → "Menggeser harga menuju nilai fundamental; Enron & WorldCom sebagai antitesis."

### Pg 16 — Signifikansi Sosial (S20) · A_2box
- **Title:** "Signifikansi Sosial: / Alokasi Modal Langka"
- **Box 1 Harga ≈ fundamental → alokasi efisien** → "Perusahaan berinvestasi hingga profitabilitas marjinal = biaya marjinal."
- **Box 2 Lemons / inside info → underinvestment** → "Investor mundur, pasar kehilangan depth; proyek bermutu tersingkir."

### Pg 17 — Stick vs Carrots (S21) · A_2check
- **Title:** "Mendorong Pengungkapan: / Stick & Carrots"
- **Intro para:** "Dua mekanisme berdampingan. Bukti lintas-negara: Wurgler (2000), FHKP (2009), BHV (2009)."
- **Check 1 Stick — regulasi** → "Standar minimum, kontrol insider trading, penalti."
- **Check 2 Carrots — insentif pasar** → "Reputasi, harga saham naik, biaya modal turun → pengungkapan sukarela."

### Pg 18 — Sintesis / Slogan (S22) · A_prose
- **Title:** "Simpulan Bab 4"
- **Body:** "'Yang dihargai pasar adalah informasi, bukan bentuknya.' Rasionalitas berlaku rata-rata, bukan seragam. Noise traders menyelamatkan insentif analisis. Selalu ada residual informasi orang dalam — di sanalah peran akuntansi: memperkecil gap lewat pengungkapan yang berguna dan hemat biaya. Asimetri informasi adalah alasan akuntansi ada."

### Pg 19 — Penutup (S23) · A_prose
- **Title:** "Yang Kini Anda Kuasai"
- **Body (4 poin):**
  - Pasar menghargai informasi, bukan bentuk.
  - Asimetri informasi: alasan akuntansi ada.
  - Full disclosure → alokasi modal efisien.
  - Pelaporan berkualitas = kepentingan sosial.

### Pg 20 — Glosarium (S24) · A_concl — OPTIONAL
- **Title:** "Glosarium — Rujukan Tanya-Jawab"
- **Body (definisi ringkas):** Efficient market · Fair game · Random walk · Noise traders / partially informative · CAPM / beta / market model · Adverse selection / moral hazard · Lemons problem · Fundamental value · Estimation risk.

## 9. Fill mechanics (per page, via Canva MCP)

1. `start-editing-transaction` on `DAHM_I0k_zo` → get `transaction_id` + `pages` array (element IDs).
2. Per page: `replace_text` / `find_and_replace_text` on each text element; `delete_element` for unused
   slots (e.g., A_3cards used with only 2 cards); apply placeholder neutralization (§7).
3. Optional `format_text` only where the template's own sizing breaks (avoid restyling — preserve theme).
4. `commit-editing-transaction` (mandatory — uncommitted edits are lost).
5. Re-read via `get-design-pages` thumbnail / `get-design-content` to verify before moving on.

## 10. Visuals policy

- Default: **keep** the template's existing illustrations/photos on every page (theme preservation).
- Equations: render as **plain text** in an existing text slot (no asset upload).
- Optional later enhancement (requires uploading assets to Canva): swap in custom diagrams for
  Pg 7 (Grossman loop), Pg 13 (lemons), Pg 14 (concentric Fig 4.2). Out of scope for the first pass.

## 11. Out of scope / non-goals

- No theme, color, font-family, or layout-geometry changes.
- No new pages created by Claude (user duplicates).
- No fabricated data — every figure traces to the draft / Scott Ch. 4.

## 12. Acceptance criteria

- Pages 1–4 unchanged.
- Every duplicated page filled with its §8 content; zero `Lorem ipsum`, `Studio Shodwe`,
  `reallygreatsite`, or `2033` remaining anywhere.
- Final deck reads as one coherent Kelompok 3 Pert. 11 presentation in the original Canva theme.
- User can export to PDF/PPTX cleanly.
