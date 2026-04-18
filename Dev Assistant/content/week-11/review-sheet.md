# Review Sheet — Minggu 11: Pasar Sekuritas Efisien (Efficient Securities Markets)

**Mata Kuliah:** MNK202 Pelaporan Keuangan Korporat
**Topik:** Efficient Securities Markets — Implikasi bagi Pelaporan Keuangan
**Bacaan:** Scott, W.R. (2015), Financial Accounting Theory, 7th ed., Ch. 4; Fama (1970, 1991); Beaver (1973)
**Anchor Company:** PT Bank Rakyat Indonesia Tbk (BBRI) — Annual Report 2024

---

## Kamus Istilah

| Istilah | Definisi | Sumber |
|---|---|---|
| **Hipotesis Pasar Efisien (EMH)** | Hipotesis bahwa pasar sekuritas yang efisien merupakan pasar di mana harga sekuritas setiap saat sepenuhnya mencerminkan semua informasi yang diketahui publik | Fama (1970); Scott, hal. 122 |
| **EMH Bentuk Lemah** (*Weak Form*) | Harga mencerminkan semua informasi harga historis; pengujian dengan auto-correlation, runs test, filter rules; tidak ada keuntungan dari analisis teknikal | Fama (1970) |
| **EMH Bentuk Setengah Kuat** (*Semi-Strong Form*) | Harga mencerminkan semua informasi yang dapat diakses publik — termasuk laporan keuangan, pengumuman laba, akuisisi; pengujian dengan *event studies* | Fama (1970, 1991) |
| **EMH Bentuk Kuat** (*Strong Form*) | Harga mencerminkan SEMUA informasi termasuk informasi privat *insider*; pengujian dengan studi keuntungan insider trading dan kinerja reksa dana | Fama (1970) |
| ***Event Study*** | Metode empiris untuk menguji EMH: mengukur *abnormal return* di sekitar pengumuman suatu peristiwa (laba, dividen, akuisisi) untuk melihat apakah harga bereaksi cepat dan akurat | MacKinlay (1997) |
| ***Abnormal Return* (AR)** | Return aktual dikurangi *expected return* (biasanya dari CAPM); AR ≠ 0 setelah pengumuman publik mengindikasikan pasar tidak sepenuhnya efisien bentuk setengah kuat | Fama (1970) |
| ***Cumulative Abnormal Return* (CAR)** | Jumlah abnormal return selama window pengamatan di sekitar event; digunakan untuk mengukur total reaksi pasar terhadap informasi | MacKinlay (1997) |
| **Capital Asset Pricing Model (CAPM)** | Model yang mendefinisikan expected return sebagai: E(R_i) = R_f + β_i(E(R_m) − R_f); β mengukur sensitivitas terhadap risiko pasar sistematis | Sharpe (1964); Lintner (1965) |
| **Beta (β)** | Koefisien risiko sistematis CAPM; β > 1 berarti saham lebih volatil dari pasar; β < 1 berarti lebih defensif; β = 1 bergerak bersama pasar | CAPM; Scott, hal. 131 |
| ***Earnings Response Coefficient* (ERC)** | Koefisien regresi yang mengukur perubahan harga saham per unit *unexpected earnings* (earnings surprise); lebih tinggi untuk laba persisten | Collins & Kothari (1989) |
| ***Unexpected Earnings* (UE)** | Perbedaan antara laba aktual dan laba yang diharapkan (*earnings surprise*) — dasar pengujian reaksi pasar terhadap pengumuman laba | Ball & Brown (1968) |
| **Paradoks Grossman-Stiglitz** | Inkonsistensi logis EMH: jika harga benar-benar informatif sempurna, tidak ada insentif mengumpulkan informasi → informasi tidak dikumpulkan → harga tidak informatif | Grossman & Stiglitz (1980) |
| ***Noise Traders*** | Investor yang berdagang berdasarkan "noise" (bukan informasi fundamental) — keberadaan mereka menciptakan risiko arbitrase dan memungkinkan informed traders mendapat keuntungan | Black (1986); De Long et al. (1990) |
| **Full Disclosure** | Prinsip pengungkapan penuh: berdasarkan EMH, kandungan informasi lebih penting dari lokasi/format pengungkapan karena pasar efisien akan memprosesnya | Beaver (1973); Scott, hal. 127 |
| ***Information Asymmetry*** | Kondisi di mana manajemen (*insider*) memiliki informasi lebih dari investor (*outsider*) — merupakan alasan fundamental eksistensi akuntansi menurut EMH | Akerlof (1970); Scott, hal. 121 |
| ***Price Protected* (Investor Naif)** | Argumen Beaver: investor naif terlindungi oleh harga pasar efisien yang sudah mencerminkan pemahaman investor informatif — tidak perlu laporan keuangan "sederhana" | Beaver (1973); Scott, hal. 128 |
| ***Accrual Anomaly*** | Bukti bertentangan dengan EMH: pasar tidak sepenuhnya mencerminkan informasi akrual — saham dengan akrual tinggi mengalami return lebih rendah di masa depan | Sloan (1996) |
| ***Post-Earnings Announcement Drift* (PEAD)** | Fenomena harga saham terus bergerak ke arah kejutan laba selama beberapa minggu/bulan pasca pengumuman — bukti bertentangan dengan EMH bentuk setengah kuat | Ball & Brown (1968); Bernard & Thomas (1989) |
| **Danantara** | Badan Pengelola Investasi Daya Anagata Nusantara, holding BUMN terbaru di Indonesia; per 2024 menguasai ~53,19% saham BBRI melalui konsolidasi kepemilikan negara | BBRI AR 2024 |

---

## Cheat Sheet 1: Tiga Bentuk EMH

```
┌────────────────────────────────────────────────────────────────┐
│                    TIGA BENTUK EMH (Fama, 1970)                │
├─────────────┬──────────────────────┬───────────────────────────┤
│ BENTUK      │ INFORMASI YANG        │ PENGUJIAN EMPIRIS         │
│             │ TERCERMIN DALAM HARGA │                           │
├─────────────┼──────────────────────┼───────────────────────────┤
│ LEMAH       │ Harga historis saja  │ Autocorrelation           │
│ (Weak)      │                      │ Runs test                 │
│             │                      │ Filter rules              │
│             │ → Analisis teknikal  │ [Sebagian besar mendukung │
│             │ TIDAK efektif        │  bentuk lemah]            │
├─────────────┼──────────────────────┼───────────────────────────┤
│ SETENGAH    │ Semua informasi      │ Event studies             │
│ KUAT        │ PUBLIK (laporan      │ [Secara umum mendukung;   │
│ (Semi-      │ keuangan, laba,      │ tapi ada PEAD dan         │
│ Strong)     │ akuisisi, dll.)      │ accrual anomaly]          │
│             │                      │                           │
│             │ → Analisis fundament │                           │
│             │ TIDAK memberi excess │                           │
│             │ return konsisten     │                           │
├─────────────┼──────────────────────┼───────────────────────────┤
│ KUAT        │ SEMUA informasi      │ Studi insider trading     │
│ (Strong)    │ termasuk privat      │ Kinerja reksa dana        │
│             │                      │ [TIDAK mendukung —        │
│             │ → Insider trading    │ insider memang memperoleh │
│             │ tidak memberikan     │ abnormal return]          │
│             │ excess return        │                           │
└─────────────┴──────────────────────┴───────────────────────────┘
```

---

## Cheat Sheet 2: Empat Implikasi Beaver (1973) untuk Akuntansi

```
IMPLIKASI 1 — Akuntansi tanpa cash-flow impact tidak memengaruhi harga
  Contoh: Pilihan FIFO vs. LIFO (dengan pengungkapan cukup) = paper effect
  
IMPLIKASI 2 — Full disclosure searah dengan efisiensi pasar
  Pengungkapan biaya rendah → wajib diungkap; mengurangi asimetri informasi
  
IMPLIKASI 3 — Perusahaan tidak perlu khawatir investor naif
  Investor naif "price protected" — harga mencerminkan pemahaman investor canggih
  (CATATAN: argumen ini dikritik karena distribusi informasi tidak merata)
  
IMPLIKASI 4 — Akuntansi bersaing dengan sumber informasi lain
  Laporan keuangan bertahan hanya jika cost-effective dan berguna relatif
  terhadap analis, media, dan harga pasar itu sendiri
```

---

## Cheat Sheet 3: CAPM dan ERC

```
CAPM: E(R_i) = R_f + β_i × (E(R_m) - R_f)

β BBRI = 1,10 (lebih volatil dari pasar)
R_f = 6,5% (SBN 10 tahun Indonesia, 2024)
Market Risk Premium = 6,0% (asumsi)
E(R_BBRI) = 6,5% + 1,10 × 6,0% = 13,1% per tahun

EARNINGS RESPONSE COEFFICIENT (ERC):
ERC lebih tinggi jika:
• Laba lebih persisten (recurring components)
• Leverage lebih rendah (risiko default lebih kecil)
• Kualitas audit lebih baik
• Perusahaan lebih besar (lebih diikuti analis)
• Pertumbuhan laba lebih tinggi

ERC lebih rendah jika:
• Laba transitoris (one-time items)
• Leverage tinggi (risiko kebangkrutan menyerap sinyal laba)
• Ketidakpastian tinggi
```

---

## Lima Pertanyaan Esensial

**Q1:** Jelaskan definisi formal EMH menurut Fama (1970) yang diadopsi Scott (2015), dan sebutkan empat poin Scott yang mempertegas definisi ini.

**A1:** Fama (1970): "*An efficient securities market is one where the prices of securities traded on that market at all times fully reflect all information that is publicly known about those securities.*" (Scott, hal. 122). Ini adalah bentuk setengah kuat. Empat poin Scott: (1) **Efisiensi relatif terhadap stok informasi** — harga mencerminkan informasi yang telah menjadi publik, bukan selalu nilai fundamental; (2) **Harga bereaksi cepat** — begitu informasi baru publik, harga langsung menyesuaikan; (3) **Investasi adalah *fair game*** — tidak ada investor yang bisa secara konsisten mendapat *excess return* di atas yang disesuaikan risiko; (4) **Random walk** — karena semua info yang dapat diprediksi sudah tercermin, perubahan harga berikutnya hanya didorong informasi tak terduga yang muncul secara acak (Scott, hal. 122-123).

---

**Q2:** Apa yang dimaksud dengan Paradoks Grossman-Stiglitz, dan bagaimana resolusinya melalui konsep *noise traders*?

**A2:** Paradoks: jika harga benar-benar mencerminkan semua informasi (fully informative), investor tidak memiliki insentif mengumpulkan informasi mahal — karena mereka tidak bisa mendapat keuntungan darinya. Jika tidak ada yang mengumpulkan informasi, harga tidak lagi mencerminkan informasi → EMH runtuh (Grossman & Stiglitz, 1980). Resolusi melalui *noise traders* (Black, 1986; De Long et al., 1990): di pasar nyata, selalu ada investor yang berdagang berdasarkan "noise" — bukan informasi fundamental. Keberadaan *noise traders* menciptakan risiko arbitrase: investor berbasis informasi tidak bisa mendapatkan keuntungan pasti karena harga mungkin bergerak semakin salah arah sebelum koreksi terjadi. Ini memberikan kompensasi return bagi informed traders dan mempertahankan insentif pengumpulan informasi — sehingga ekuilibrium stabil dapat tercapai (Scott, hal. 129-130). Implikasi bagi akuntansi: laporan keuangan berkualitas tinggi mengurangi risiko arbitrase dengan menyediakan informasi yang dapat diandalkan.

---

**Q3:** Jelaskan implikasi Beaver (1973) tentang "investor naif terlindungi oleh harga." Apa kritik yang dapat diajukan terhadap argumen ini dari perspektif pasar Indonesia?

**A3:** Argumen Beaver: dalam pasar efisien, investor naif (*unsophisticated*) tidak perlu khawatir karena harga sudah mencerminkan pemahaman investor yang informatif dan canggih. Beli di harga pasar = beli di harga "adil" yang sudah memproses semua informasi publik. Dengan demikian, pembuat standar tidak perlu membuat laporan keuangan "sederhana untuk semua orang" — cukup informatif bagi investor canggih, dan harga akan melindungi yang lain (Scott, hal. 128). Kritik untuk pasar Indonesia: (1) BEI didominasi investor ritel — proporsi investor institusional lebih rendah dibanding NYSE/LSE; harga mungkin kurang efisien karena lebih sedikit investor "canggih" yang memproses informasi; (2) banyak saham BUMN dan konglomerasi memiliki *free float* rendah, mengurangi kekuatan price discovery; (3) kasus TLKM dan BBRI dengan kepemilikan negara/Danantara 53% — pemegang saham mayoritas bukanlah "investor rasional di pasar kompetitif" tetapi entitas kebijakan; (4) *insider trading* masih terjadi (kasus-kasus OJK) — menandakan bentuk kuat EMH tidak berlaku.

---

**Q4:** Apa itu ERC (*Earnings Response Coefficient*) dan faktor-faktor apa yang meningkatkan atau menurunkan ERC suatu perusahaan?

**A4:** ERC adalah koefisien regresi yang mengukur seberapa besar harga saham berubah per unit *earnings surprise* (*unexpected earnings*). Secara formal: ΔP_i = α + ERC × UE_i + ε, di mana UE = Laba aktual − Laba yang diekspektasikan. ERC lebih tinggi jika: (1) **Laba lebih persisten** — laba yang diharapkan berulang di masa depan lebih bernilai bagi investor (setiap Rp1 laba persisten "membeli" lebih banyak nilai); (2) **Leverage lebih rendah** — perusahaan leverage tinggi, kejutan laba positif sebagian masuk ke kreditor, bukan pemegang saham; (3) **Pertumbuhan lebih tinggi** — perusahaan tumbuh memberikan leverage positif atas kejutan laba (Kothari, 2001); (4) **Kualitas audit lebih baik** — laporan lebih credible; (5) **Perusahaan lebih besar dan diikuti lebih banyak analis**. ERC lebih rendah jika: laba transitoris (*one-time items*), leverage tinggi, ketidakpastian tinggi, atau berada dalam industri yang diregulasi berat (bank Indonesia — regulator mungkin dianggap memiliki informasi lebih dari pasar).

---

**Q5:** Identifikasi dan jelaskan dua anomali pasar yang secara empiris paling menantang EMH bentuk setengah kuat. Apa implikasinya bagi analis keuangan yang menggunakan laporan keuangan?

**A5:** (1) **Post-Earnings Announcement Drift (PEAD)**: Ball & Brown (1968) dan Bernard & Thomas (1989) menemukan bahwa harga saham terus bergerak ke arah kejutan laba selama 30-90 hari setelah pengumuman — mengindikasikan pasar tidak langsung fully reflect informasi laba publik. Ini bertentangan dengan EMH bentuk setengah kuat yang mensyaratkan reaksi instan. Kemungkinan penjelasan: biaya pemrosesan informasi, investor ritel lambat bereaksi, *bounded rationality*. (2) **Accrual Anomaly** (Sloan, 1996): strategi long-short berdasarkan komponen akrual menghasilkan abnormal return ~10%/tahun — pasar tidak sepenuhnya mengantisipasi rendahnya persistensi akrual tinggi. Implikasi bagi analis: (a) PEAD → strategi *earnings momentum* (beli saham kejutan positif, jual kejutan negatif) mungkin menghasilkan return; (b) Accrual anomaly → analisis kualitas laba (AQ Sloan) memberikan keunggulan informasional; (c) keberadaan anomali ini mengindikasikan bahwa analisis fundamental berbasis laporan keuangan masih memberikan nilai tambah di pasar yang tidak sepenuhnya efisien seperti BEI.

---

*Referensi: Scott, W.R. (2015) Ch. 4; Fama (1970) JF; Fama (1991) JF; Beaver (1973) AR; Ball & Brown (1968) JAR; Sloan (1996) TAR; Grossman & Stiglitz (1980) AER; MacKinlay (1997) JEL; BBRI Annual Report 2024.*
