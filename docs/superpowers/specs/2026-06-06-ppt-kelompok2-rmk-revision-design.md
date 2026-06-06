# Design: PPT Kelompok 2 PKK — RMK-Aligned Deck Revision

**Date:** 2026-06-06
**Status:** Approved (Approach A — "one beat per RMK section")
**Deck:** `PPT Kelompok 2 PKK/Statement of Cash Flows.html` (19 slides → 23 slides)
**Authoritative content source:** `pkk-rmk-cash-flows-kelompok2/content/` markdown sections (the single source of truth behind `output/RMK Chap. 13_Kelompok 2_PKK.docx`, validated 62/62 concepts). The docx itself is never parsed; the markdown sections are its build input.

## Goal

Revise the 19-slide Statement of Cash Flows deck so that:
1. Every factual claim and number matches the RMK (which is faithful to Wolk, Dodd & Rozycki, *Accounting Theory* 9th ed., Ch. 13).
2. Slide order strictly follows the RMK's 15-section sequence (user decision — Winston dramaturgy framing dropped where it conflicts).
3. RMK content currently missing from the deck gets a home (notably Section 14 "Riset").
4. The visual system is untouched: `deck.css` and `deck-stage.js` are NOT modified. New slides are composed exclusively from existing components (`.sidepanel`, `.gcards`, `.statgrid`, `.exhibit`, `.ghost`, `.pill`, `.bul`, `.bigstat`, blobs).

## User decisions (clarified 2026-06-06)

| Question | Decision |
|---|---|
| Scope | Align + fill gaps (~23 slides), fix all factual errors |
| Narrative order | Strict RMK section order; drop Winston spine where it conflicts |
| Simplified exhibits (13.5 cards, 13.7 diagram) | Keep presentation-friendly forms, make their content exactly faithful |

## Confirmed factual errors to fix

1. **Slide 7 / new slide 8 (Exhibit 13.2, Direct Method):**
   - `Proceeds from sale of facility $6,001` → **$600** (CFI total $(1,175) = 600 + 150 − 1,000 − 925).
   - `Net increase in cash & equivalents $1,665` → **$1,065** (= 1,365 − 1,175 + 875), plus a closing line "Cash & equivalents, end of year $1,665" so the familiar $1,665 stays visible and correctly labeled.
2. **Slide 11 / new slide 12 (Exhibit 13.5, premium methods):** replace card texts for Methods 2–4 with the RMK's actual methods (Vent, Cowling & Sevalstad):
   - Method 1: premi $1.000 seluruhnya arus masuk **pendanaan** tahun 2000; arus operasi 2001–2004 = $(800)/tahun ≠ beban akrual $550. Pilihan penulis; hampir pasti dipakai bersama metode langsung.
   - Method 2: premi dipindahkan ke **operasi pada tahun pelunasan (2004)**.
   - Method 3: premi dipindahkan ke **operasi pada tahun penerbitan (2000)**.
   - Method 4: premi dialokasikan sepanjang umur obligasi sebagai arus keluar **pendanaan**; arus tahunan $800 terpecah: operasi $(550) + pendanaan $(250). Paling tidak masuk akal (penilaian penulis).
   - Working example header: obligasi kupon 8%, 4 tahun, nominal $10.000, terjual $11.000 (31 Des 2000); amortisasi garis lurus $250/tahun; beban bunga akrual $550 (= kupon $800 − amortisasi $250).

## Target structure — 23 slides, strict RMK order

Notation: **[KEEP]** = content verified, light edits only; **[EDIT]** = same slide, content corrected/enriched; **[SPLIT]** = derived from an existing slide; **[NEW]** = new slide; **[REPLACE]** = same position-role, new content.

| # | data-label | RMK source | Layout | Spec |
|---|---|---|---|---|
| 1 | Judul | 00-cover | title (current s1) | [KEEP] Members/NIMs verified vs cover. |
| 2 | Pendahuluan | 00-pendahuluan | hero + gcards (replaces s2) | [REPLACE] *Music Man* hook ("Cash for the merchandise…"); tesis: tagihan dibayar kas, bukan laba; arc 1971 APB Op. 19 (SCFP) → 1987 SFAS 95 (SCF); roadmap kalimat penutup RMK pendahuluan (konstruksi SCFP → tujuan → struktur → dua masalah besar → kegunaan → FCF → riset → perbaikan). |
| 3 | SCFP Sources & Uses | 01-scfp-funds-flow | split layout + exhibit (current s4) | [EDIT] Keep Exhibit 13.1 table. Add: eq. (13.1) *transaction credits = transaction debits*; APB 19's three reporting objectives (complete disclosure / summarize financing & investing / report funds flow from operations); derivative-statement nature. Bullet on "all-inclusive" stays. |
| 4 | Definisi Dana & Garis Waktu | 01-scfp-funds-flow | sidepanel + statgrid | [NEW] Four permitted fund definitions (kas; kas + near cash; quick assets; modal kerja) + cost rationale (working capital minimizes nonfund items → majority choice); timeline 1963 APB Op. 3 (anjuran) → 1971 SEC wajib statutory filings → 1971 APB Op. 19 (wajib semua pelaporan). |
| 5 | Motivasi ke Kas | 02-motivation-scf | sidepanel + statgrid (split from s5) | [SPLIT] Three NWC weaknesses verbatim-faithful: (1) deferred charges/credits tanpa konsekuensi kas; (2) konversi aset lancar bisa >1 tahun (siklus operasi panjang); (3) persediaan berbasis biaya, bukan potensi kas nyata. Closer: "cash is cash is cash". |
| 6 | Tujuan SCF | 03-objectives | content + gcards (split from s5) | [SPLIT] SFAC No. 1 (decision-usefulness → menilai arus kas masa depan); SFAC No. 5 (3 domain + 4 kegunaan: likuiditas, fleksibilitas, profitabilitas, risiko); discussion memorandum's SIX benefits (umpan balik kas aktual; hubungan laba–kas; quality of income; komparabilitas; fleksibilitas & likuiditas; prediksi); quality of income = korelasi laba–CFO; likuiditas ≠ fleksibilitas; neraca = "crude ranking of liquidity"; expanded disclosure philosophy. (Densest slide — prioritize 6 benefits as gcards/statgrid, the rest as bullets.) |
| 7 | Tiga Aktivitas | 04-structure-trichotomy | sidepanel + statgrid (current s6) | [EDIT] Keep trichotomy stats. Add: kas = kas + cash equivalents (definisi); noncash investing/financing wajib diungkap suplemen (semangat all-inclusive); teaser dissent 3/7 anggota FASB (detail di slide 11). |
| 8 | Direct Method | 05-direct-vs-indirect | split + exhibit 13.2 (current s7) | [EDIT] **Fix $600 and $1,065** + add "Cash & equivalents, end of year $1,665" closing row. Bullets keep: literal per klasifikasi laba rugi; disukai FASB; wajib rekonsiliasi. |
| 9 | Indirect Method | 05-direct-vs-indirect | split + exhibit 13.3 (current s8) | [EDIT] Keep table (verified). Enrich bullets: identical bottom line $1,365 (konsekuensi matematis); *plug number* dalam praktik; McEnroe **282 responden**, 56% vs 44%; trade-off mudah-disusun vs sulit-dibaca. |
| 10 | Nonartikulasi 3M | 06-nonarticulation | hero + exhibit 13.4 (current s9) | [EDIT] Keep table (verified). Fix the three causes to match RMK: (1) akuisisi tengah tahun; (2) transaksi modal kerja nonkas (write-up/down persediaan saat akuisisi purchase, alokasi depresiasi ke persediaan manufaktur, reklasifikasi lancar↔tak lancar); (3) satu akun AP untuk pembelian operasi & investasi (paling umum). Add: FASB–IASB 2008 discussion paper — klasifikasi "business" gabungan berpotensi menekan classification shifting. |
| 11 | Bunga & Dividen | 04 (dissent) + 07-classification-problems | sidepanel + statgrid (current s10) | [EDIT] Keep 4 stats, enrich: Nurnberg's irony (ketiga elemen masuk kategori yang paling tidak mencerminkan hakikat ekonominya); proprietary vs entity theory; tekanan industri perbankan (hindari CFO negatif); IAS 7 fleksibel asal konsisten → keseragaman intra-industri, tidak lintas-industri. |
| 12 | Premium Obligasi | 07-classification-problems | 4 gcards (current s11) | [EDIT] **Fix Methods 2/3/4 per error list above.** Keep working-example intro. Footer line: masalah alokasi (arbitrariness); kasus serupa — bunga dikapitalisasi SFAS 34 (hakikat vs tujuan), lease (operating = operasi; capital = bunga operasi + pokok pendanaan), SFAS 104 hedging (fineness vs komparabilitas). |
| 13 | Ingram & Lee | 08-analytical-usefulness | split + gcards (split from s12) | [SPLIT] Growth firms: laba ↑ tapi CFO ↓ (piutang & persediaan membengkak); contraction firms simetris: laba ↓ CFO ↑ (kas terbebaskan), investasi berkurang, distribusi naik; ±1.000 firma 1974–1992; temuan leverage: firma ekspansi menanggung leverage lebih besar. Pola SCF = sidik jari siklus hidup → insentif merekayasa. |
| 14 | Misklasifikasi | 09-misclassification | split + gcards (split from s12) | [SPLIT] Mekanisme: geser arus keluar operasi→investasi / arus masuk investasi→operasi, posisi kas total tak berubah. Tyco (kontrak dealer = "akuisisi"); Ford/GM/Harley notes receivable ke dealer = investasi; GM: CFO $7,6 M vs $3,5 M; Navistar reklasifikasi ke operasi + kutipan Oberle ("we define ourselves as a manufacturing company…"). Simpulan: aturan tak dilanggar formal, komparabilitas tetap lemah. |
| 15 | WorldCom Terlihat Sehat | 10-scf-more-than-cfo | hero + exhibit 13.6 (current s13) | [KEEP] Table verified. Minor: tambahkan kutipan "investors who ignore one or more parts do so at their peril." |
| 16 | Minus 12,3 Miliar | 10-scf-more-than-cfo | bigstat (current s14) | [KEEP] Verified. Bullet tambahan: pertanyaan analitis — berapa lama pola ini bisa berlanjut? |
| 17 | Buffett & Nilai Intrinsik | 11-user-needs | content + gcards (split from s15) | [SPLIT] Buffett 1988: 3 pertanyaan (nilai? kewajiban? kinerja manajer?) → 3 fungsi (valuation, kredit, stewardship); keputusan investasi = capital budgeting, terima jika NPV positif; nilai intrinsik = nilai diskonto kas yang dapat diambil selama sisa umur bisnis — estimasi, bukan presisi; jembatan: arus kas apa? → FCF. |
| 18 | Free Cash Flow | 12-free-cash-flow | split + FCF anatomy diagram (split from s15) | [SPLIT] Eq. (13.2) FCF = NOPLAT − investasi pada operating invested capital. "Free" = *absence of a superior claim* (Mulford & Comiskey). Diagram keeps NOPLAT − investment = FCF; notes: beban bunga TIDAK termasuk (beban pendanaan); kas operasi bagian dari net operating working capital; entity theory → cash flow to the firm; FCF tidak tersedia langsung dari SCF. |
| 19 | ABC: SCF ke FCF | 12-free-cash-flow | split + exhibit 13.8/13.9 (current s16) | [EDIT] Numbers verified (CFO 527/466/434; FCF 332/99/80; NI 320/312/331; CFI (277)/(309)/(360)). Add interpretive bullet: penurunan FCF = investasi makin agresif, bukan operasi memburuk. |
| 20 | Empat Ukuran | 12-free-cash-flow | dual exhibit 13.10/13.11 (current s17) | [EDIT] Tables verified. Add when-to-use guidance row (waktu/sumber daya/tujuan): NI = cepat; CFO = kualitas laba; CFO−CFI = anti-kapitalisasi-beban; FCF = paling murni, dasar DCF dengan WACC; "the real world is never simple." |
| 21 | Riset Arus Kas | 13-research | content + gcards | [NEW] Lawson & Lee; kutipan Lee: *"Cash flow and not profit is the end result of entity activity. Profit is an abstraction; cash is a physical resource."*; riset pasar modal: akrual informatif di atas arus kas → komplementer, bukan substitusi; survei FAF: kepentingan data arus dana naik, akrual turun. |
| 22 | Memperbaiki SCF | 14-improving-scf | sidepanel (current s18) | [EDIT] Broome's 3 recommendations explicit: (1) wajibkan direct method DAN rekonsiliasi; (2) panduan klasifikasi lebih banyak; (3) balik arah rekonsiliasi (dari CFO ke laba); penulis: skedul transaksi nonkas modal kerja, skedul akuisisi tengah tahun, jelaskan sumber nonartikulasi. |
| 23 | Sintesis | 14-improving-scf (¶ sintesis) | statgrid close (reworks s19) | [REPLACE] Sintesis penutup RMK: SCF = kasus khusus SCFP (dana = kas); laporan derivatif namun informasi baru via dekomposisi kas/akrual + reklasifikasi trikotomi; pilihan proprietary → isu klasifikasi; dua masalah menetap (nonartikulasi, misklasifikasi); penilaian akhir afirmatif — konsistensi, daya prediksi, komparabilitas naik; SCF kian penting karena bebas arbitrariness laba. Sumber: Wolk, Dodd & Rozycki (2017) Bab 13. |

### Slide-number furniture
Ghost numbers / sidepanel `pnum` values must be renumbered to match new positions (02–23). Keep the established alternation rhythm (ghost br / ghost tr blue / sidepanel) roughly as inherited from neighboring slides so the visual cadence survives the reorder.

## Components & constraints

- **No changes** to `deck.css`, `deck-stage.js`, fonts, or assets. If a new slide needs a variation, use inline styles exactly as existing slides do.
- All slides in Bahasa Indonesia, professor-voice (S2 register) — match RMK phrasing where it appears on-slide; compress, never dumb down.
- `data-label` attributes updated to the table above (the thumbnail rail and screen labels derive from them).
- Slide text budget: respect existing type scale; if RMK content exceeds a slide's layout capacity, cut detail (the RMK remains the deep reference) — never shrink type below existing sizes.

## Error handling / fidelity protocol

- Every number that appears on a slide must tie to the RMK section text or its exhibit tables (`content/figures/tables/*.md`, `manifest.yaml` captions).
- No content from outside Wolk Ch. 13 / the RMK may be introduced (consistent with RMK hard rule 4).
- Quotes reproduced verbatim (Lee, Oberle, "investors who ignore…", "the real world is never simple").

## Verification (definition of done)

1. **Number audit:** scripted/agent pass — extract every figure on every slide, tie each to its RMK source line. Zero unmatched numbers.
2. **Coverage audit:** every RMK section 00–14 maps to ≥1 slide; the 23-slide table above is the checklist.
3. **Order audit:** slide sequence matches RMK section sequence monotonically.
4. **Render check:** deck opens in browser; no console errors; spot-check new/edited slides for overflow (ghost numbers vs tables, statgrid density) at 1920×1080.
5. **Two-stage review** per repo convention: Stage 1 completeness/numbers/layout; Stage 2 academic faithfulness & register.

## Out of scope

- Speaker notes, PPTX/PDF export (possible follow-ups).
- Any change to the RMK pipeline or docx.
- Visual redesign of the design system.
