# Panduan Belajar (Study Guide) — Minggu 12: Manajemen Laba (Earnings Management)

> **MNK202 Pelaporan Keuangan Korporat — Pascasarjana STIE YKPN 2025/2026**
> **Topik:** Manajemen Laba — *Earnings Management* (Scott Bab 11)
> **Anchor:** PT Garuda Indonesia (Persero) Tbk (IDX: GIAA) — Laporan Tahunan 2024
> **Bacaan Pendukung:** Healy & Wahlen (1999); Jones (1991)

---

## 1. Urutan Membaca (5 Langkah)

| Langkah | Bahan | Fokus | Output yang Diharapkan |
|---|---|---|---|
| **1** | **Scott Bab 11 §11.1–§11.2** (hal. 444–447) | Definisi EM, pola (*patterns*): *taking a bath*, *income minimization/maximization*, *income smoothing*. Konsep *accruals reversal* ("iron law"). | Mampu menjelaskan lima pola EM dan rumus: *Net income = CFO ± Akrual non-diskresioner ± Akrual diskresioner*. |
| **2** | **Scott §11.3** (hal. 448–453) — **Healy (1985)** & **Jones (1991)** | Bonus plan hypothesis (*bogey/cap*); model regresi Jones untuk memisahkan akrual diskresioner (DA) dari akrual non-diskresioner (NDA). | Memahami formula: TA_jt = α_j + β_1j ΔREV_jt + β_2j PPE_jt + ε_jt, dan alasan tanda β_1 > 0 dan β_2 < 0. |
| **3** | **Scott §11.4–§11.6** (hal. 454–472) | Motivasi lain: *debt covenants* (Sweeney 1994), ekspektasi analis, *stock offerings* (Cohen & Zarowin 2010); sisi baik (*blocked communication*, Demski & Sappington 1987) vs sisi buruk (Olympus, Groupon, Sunbeam, BMS). | Mampu membedakan *good* vs *bad earnings management*; memahami trade-off efisien vs oportunistik. |
| **4** | **Konteks GIAA** — LT 2024 hal. 18, 21–27, 50, 274 | Kondisi *financial distress*: akumulasi rugi USD 3,50 miliar (LT 2024, hal. 22), ekuitas negatif USD 1,35 miliar (LT 2024, hal. 279), *going concern note* di Catatan 49 (LT 2024, hal. 274). PKPU 2022 → restrukturisasi final. | Mengenali GIAA sebagai *case study* klasik untuk motivasi *debt covenant*, *big bath*, dan *cookie jar reserves* pasca restrukturisasi. |
| **5** | **Latihan Deteksi** — buka *exercises.md* | Terapkan diagnostik *CFO–NI divergence*, konsentrasi provisi, kualitas akrual (Dechow–Dichev). | Bisa menghitung *total accruals* dan menginterpretasi rasio CFO/NI untuk satu tahun GIAA. |

---

## 2. Grid Konsep

### Teori Utama (Biru) — Scott Bab 11
- **Definisi formal (Scott, 2015, hal. 445):** *"Earnings management is the choice by a manager of accounting policies, or real actions, affecting earnings so as to achieve some specific reported earnings objective."*
- **Dua dimensi EM:** (a) **kebijakan akuntansi** (*accounting policy choice*) — contoh: metode depresiasi, kebijakan pengakuan pendapatan, (b) **tindakan riil** (*real actions*) — contoh: memotong R&D, menjual aset, mempercepat pengiriman.
- **Iron Law (Scott, hal. 445):** "*accruals reverse*" — akrual diskresioner yang menaikkan laba periode ini **pasti** menurunkan laba periode depan.
- **Empat pola (Scott §11.2, hal. 447):**
  1. *Taking a bath* — rugi besar saat restrukturisasi
  2. *Income minimization* — reduksi pajak / biaya politis
  3. *Income maximization* — bonus / covenant
  4. *Income smoothing* — perataan laba lintas waktu

### Ekonomi Informasi (Ungu) — Asimetri & Kontrak Efisien
- **Blocked communication (Demski–Sappington 1987):** manajer memiliki informasi superior; EM *bisa* menjadi kendaraan komunikasi kredibel jika dipakai untuk menurunkan laba *transitory* (Scott §11.5.1, hal. 459).
- **Efisien vs oportunistik:** manajer memilih kebijakan akuntansi untuk (a) memitigasi rigidity kontrak (EM baik) atau (b) memperkaya diri (EM buruk).
- **Peran akrual:** akrual adalah "*smoothing device*" alami (matching principle), namun memberi manajer ruang diskresi yang dieksploitasi (Healy, 1985).
- **Hubungan dengan EMH (Scott §11.6.2, hal. 469):** banyak taktik EM hanya masuk akal jika manajer **tidak sepenuhnya** menerima efisiensi pasar.

### Konteks Indonesia (Hijau) — GIAA & Regulasi OJK
- **GIAA: kasus klasik *distressed EM*** — restrukturisasi PKPU 2022 menghasilkan *gain on debt restructuring* USD 2,854 juta di 2022 (LT 2024, hal. 23, 308), kemudian rugi bersih USD 69,78 juta di 2024 meski CFO positif USD 585,74 juta (LT 2024, hal. 25) — divergensi klasik sinyal akrual masif.
- **Preseden GIAA-2018** (bukan bagian LT 2024, tapi konteks): pengakuan pendapatan "hak kompensasi" dari Mahata/Sriwijaya USD 239 juta yang ditolak OJK dan menghasilkan *restatement* — contoh nyata *aggressive revenue recognition* versi Groupon (Scott, Theory in Practice 11.1).
- **Regulator Indonesia:** OJK (POJK No. 14/2012 tentang Laporan Tahunan), Bursa Efek Indonesia (Peraturan I-E), Ikatan Akuntan Indonesia (PSAK 1, 8, 37, 72, 73). Sanksi historis OJK mencakup denda, restatement, dan pencabutan izin KAP.

### Pengukuran & Valuasi (Amber) — Model Jones & Modifikasi
- **Model Jones (1991)** — Scott §11.3, hal. 453:
  $$\frac{TA_{it}}{A_{i,t-1}} = \alpha_i \left(\frac{1}{A_{i,t-1}}\right) + \beta_{1i} \left(\frac{\Delta REV_{it}}{A_{i,t-1}}\right) + \beta_{2i} \left(\frac{PPE_{it}}{A_{i,t-1}}\right) + \varepsilon_{it}$$
  - **TA_it** = total akrual (NI – CFO) perusahaan i tahun t
  - **ΔREV_it** = perubahan pendapatan
  - **PPE_it** = *gross property, plant & equipment*
  - **A_{i,t-1}** = total aset awal periode (*deflator* skala)
  - **ε_it** = residu, proksi akrual diskresioner

- **Modified Jones (Dechow, Sloan, Sweeney 1995):** mengganti ΔREV dengan (ΔREV – ΔREC) untuk mengontrol manipulasi kredit:
  $$NDA_{it} = \alpha_i \left(\frac{1}{A_{i,t-1}}\right) + \beta_{1i} \left(\frac{\Delta REV_{it} - \Delta REC_{it}}{A_{i,t-1}}\right) + \beta_{2i} \left(\frac{PPE_{it}}{A_{i,t-1}}\right)$$
  di mana ΔREC = perubahan piutang usaha — menutup celah pengakuan pendapatan belum tertagih.

- **Tanda koefisien yang diharapkan:** β_1 > 0 (makin banyak pendapatan → makin banyak *working capital accruals* tak diskresioner); β_2 < 0 (PPE makin besar → beban depresiasi makin besar → akrual makin negatif).

---

## 3. Diagram Alur — dari Motivasi ke Deteksi

```
  MOTIVASI                FLEKSIBILITAS      AKRUAL              POLA EM
  (Why)                   GAAP               DISKRESIONER        (What)
  ─────────               ───────────        ─────────────       ────────
  • Bonus plan      ───▶  • Estimasi       ───▶ • Provisi      ───▶ • Big bath
  • Debt covenant         • Metode             • Write-off         • Smoothing
  • IPO / SEO             • Timing             • Allowance         • Maximization
  • Analyst fcst.         • Reklasifikasi      • Accrual timing    • Minimization
  • Political cost                                                  (Cookie jar)
                                    │
                                    ▼
                          DETEKSI (Peneliti/Auditor/Regulator)
                          ──────────────────────────────────
                          • Jones / Modified Jones model
                          • CFO vs NI divergence
                          • Akrual kualitas (Dechow–Dichev)
                          • Small-loss avoidance ratio (LNW 2003)
                                    │
                                    ▼
                          RESPONS REGULASI
                          ────────────────
                          • SFAS 146 (ASC 420) — restrukturisasi hanya saat terjadi
                          • IAS 37 (PSAK 57) — provisi wajib estimasi andal
                          • SOX (2002) / POJK / Bapepam-Kep-134 — pengungkapan
```

**Panah balik penting:** "iron law of accruals reversal" (Scott hal. 445) — akrual diskresioner positif sekarang = akrual negatif di masa depan; karena itu EM bersifat *self-limiting* kecuali perusahaan terus menambahkan lapisan baru.

---

## 4. Kutipan Kunci (Scott Bab 11)

### Definisi Formal EM
> **"Earnings management is the choice by a manager of accounting policies, or real actions, affecting earnings so as to achieve some specific reported earnings objective."**
> — *Scott (2015), Financial Accounting Theory, 7th ed., hal. 445*

**Terjemahan:** *Manajemen laba adalah pilihan manajer atas kebijakan akuntansi, atau tindakan riil, yang memengaruhi laba sedemikian rupa sehingga tujuan laba yang dilaporkan dapat tercapai.*

### Definisi Alternatif (Healy & Wahlen 1999) — dikutip Scott secara tersirat via §11.4.3
> **"Earnings management occurs when managers use judgment in financial reporting and in structuring transactions to alter financial reports to either mislead some stakeholders about the underlying economic performance of the company or to influence contractual outcomes that depend on reported accounting numbers."**
> — *Healy & Wahlen (1999), "A Review of the Earnings Management Literature and Its Implications for Standard Setting," Accounting Horizons, 13(4), hal. 368*

**Terjemahan:** *Manajemen laba terjadi ketika manajer menggunakan pertimbangan dalam pelaporan keuangan dan dalam merancang transaksi untuk mengubah laporan keuangan, baik untuk menyesatkan sebagian pemangku kepentingan mengenai kinerja ekonomi perusahaan, maupun untuk memengaruhi hasil kontrak yang bergantung pada angka akuntansi yang dilaporkan.*

### Iron Law of Accruals Reversal
> **"The reversal of these accruals in subsequent periods will force future earnings downward just as surely as current earnings were raised."**
> — *Scott (2015), hal. 445*

**Terjemahan:** *Pembalikan akrual tersebut pada periode berikutnya akan menekan laba masa depan dengan kepastian yang sama seperti ketika laba saat ini dinaikkan.*

### Jones Model — Rasionalitas Ekonomi
> **"ΔREV_jt controls for the non-discretionary accruals of current assets and liabilities on the grounds that these depend on changes in business activity as measured by revenues... PPE_jt controls for the non-discretionary component of amortization expense, on the grounds that this depends on the firm's investment in capital assets."**
> — *Scott (2015), hal. 453*

**Terjemahan:** *Perubahan pendapatan (ΔREV) mengontrol akrual non-diskresioner pada aset dan liabilitas lancar, karena komponen ini bergantung pada perubahan aktivitas bisnis yang diukur oleh pendapatan. Sementara itu, PPE mengontrol komponen non-diskresioner dari beban amortisasi/depresiasi, karena bergantung pada investasi perusahaan dalam aset tetap.*

---

## 5. Kacamata Dosen (Lensa UAS)

### Fokus Ujian (berdasarkan Silabus 2025/2026 & pola UTS pra-UAS)
1. **Definisi & motivasi** — mampu memberi definisi EM (versi Scott + Healy–Wahlen), menyebutkan minimal 4 motivasi, dan menghubungkan masing-masing ke teori agensi (Bab 9).
2. **Identifikasi pola dari data** — diberi laporan keuangan ringkas, mahasiswa harus mengenali pola (*big bath*, *cookie jar*, *income smoothing*, dll.).
3. **Model Jones (intuisi, bukan regresi OLS penuh)** — mampu menulis persamaan, menjelaskan tanda koefisien yang diharapkan, dan menafsirkan residu sebagai DA.
4. **Penerapan ke kasus Indonesia** — khususnya GIAA: apakah *big loss* 2024 (–USD 69,78 juta) setelah rugi besar 2021 (–USD 4,17 miliar) konsisten dengan *iron law*? Bagaimana CFO positif USD 585,74 juta bisa menyertai rugi bersih?
5. **Implikasi etis & regulasi** — apakah EM *selalu* tidak etis? Kapan EM "baik" (Demski–Sappington / *blocked communication*)?

### Contoh Pertanyaan UAS (prediksi)
> **"PT Garuda Indonesia (Persero) Tbk pada tahun 2024 melaporkan rugi bersih USD 69,78 juta (LT 2024, hal. 25), namun arus kas operasi positif USD 585,74 juta (LT 2024, hal. 25). Pada 2022, perusahaan mencatat laba USD 3,74 miliar (LT 2024, hal. 24) yang didominasi *gain on debt restructuring* USD 2,85 miliar dari proses PKPU.**
>
> **Berdasarkan Scott Bab 11:**
> **(a) Identifikasi dua pola manajemen laba yang konsisten dengan data tersebut dan jelaskan alasannya (bobot 30%).**
> **(b) Gunakan intuisi model Jones (1991) untuk menjelaskan mengapa pemisahan akrual diskresioner dari non-diskresioner penting dalam kasus GIAA (bobot 30%).**
> **(c) Catatan 49 Laporan Keuangan GIAA menyebutkan *going concern issue*, namun opini audit KAP Rintis, Jumadi, Rianto & Rekan (PwC) tidak dimodifikasi (LT 2024, hal. 274). Diskusikan implikasinya bagi reliability laporan keuangan menggunakan kerangka Healy & Wahlen (1999) (bobot 40%)."**

### Jebakan yang Harus Dihindari
- Menganggap *semua* akrual adalah EM. Scott (hal. 445) menegaskan: akrual **non-diskresioner** (depresiasi sesuai umur, piutang mengikuti penjualan) **bukan** EM.
- Menganggap *real EM* (memotong R&D, menunda maintenance) bukan EM karena "bukan rekayasa pembukuan" — Scott hal. 446 eksplisit memasukkannya (Roychowdhury 2006).
- Menyimpulkan EM = *fraud*. EM dalam koridor PSAK/IFRS bukan fraud; fraud hanya ketika melanggar standar (mis. Olympus 2011 — Scott Theory in Practice 11.3, hal. 467).

---

## 6. Ringkasan Satu Menit

Manajemen laba adalah pemanfaatan diskresi GAAP atau tindakan riil untuk mencapai target laba tertentu. Motivasinya mencakup bonus, kovenan utang, ekspektasi analis, IPO/SEO, dan biaya politis. Alat utamanya adalah **akrual diskresioner** yang dipisahkan dari akrual non-diskresioner melalui **model Jones** (1991) atau modifikasinya. Pola empiris meliputi *big bath*, *income smoothing*, *income maximization/minimization*, dan *cookie jar reserves*. Sisi baiknya — EM dapat mengkomunikasikan informasi inside (Demski–Sappington). Sisi buruknya — EM menjadi kendaraan fraud (Olympus, Sunbeam, Enron). Kasus Garuda Indonesia 2024 — dengan akumulasi rugi USD 3,50 miliar, ekuitas negatif USD 1,35 miliar, dan catatan *going concern* — menjadi laboratorium ideal untuk membaca sinyal EM dalam konteks *distress*. Ujian keberhasilan: mampu **mengenali pola**, **menghitung sinyal**, dan **membenarkan interpretasi** dengan teori.
