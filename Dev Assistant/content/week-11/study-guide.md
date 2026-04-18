# Panduan Belajar (Study Guide) — Minggu 11: Pasar Sekuritas Efisien (Efficient Market Hypothesis/EMH)

> Mata Kuliah: MNK202 Pelaporan Keuangan Korporat (Pascasarjana STIE YKPN Yogyakarta)
> Bacaan Inti: Scott, W.R. (2015), *Financial Accounting Theory*, 7th ed., Pearson — Bab 4 "Efficient Securities Markets" (hal. 120–152)
> Bacaan Pendukung: Fama, E.F. (1970) "Efficient Capital Markets: A Review of Theory and Empirical Work"; Fama, E.F. (1991) "Efficient Capital Markets: II"; Beaver, W.H. (1973) "What Should Be the FASB's Objectives?"
> Perusahaan Jangkar: PT Bank Rakyat Indonesia (Persero) Tbk (ticker: BBRI) — Laporan Tahunan 2025

---

## 1. Urutan Membaca yang Direkomendasikan (5 Langkah)

Pembelajaran topik *efficient market hypothesis* membutuhkan pergerakan dari teori dasar, ke formulasi matematis, ke bukti empiris, lalu ke kasus pasar Indonesia. Urutan berikut meminimalkan beban kognitif dan memastikan mahasiswa tidak "tersesat" dalam notasi matematis sebelum intuisi ekonominya terbentuk.

**Langkah 1 — Scott Bab 4 §4.1–§4.2 (hal. 120–126): Makna Efisiensi Pasar.**
Mulailah dengan definisi Fama (1970) yang dikutip Scott: "*An efficient securities market is one where the prices of securities traded on that market at all times fully reflect all information that is publicly known about those securities*" (hal. 122). Fokus pada empat poin Scott: (1) efisiensi didefinisikan relatif terhadap *stock of information*; (2) pasar merespons cepat (quickly adjust) terhadap informasi baru atau yang direvisi; (3) investasi merupakan *fair game*; (4) harga berfluktuasi acak (*random walk*) ketika tidak ada informasi baru. Waktu membaca: 45 menit.

**Langkah 2 — Fama (1970) abstract dan klasifikasi tiga bentuk EMH.**
Baca paper Fama sendiri untuk memahami klasifikasi bentuk lemah (hanya harga historis), setengah kuat (semua informasi publik), dan kuat (termasuk informasi privat/orang dalam). Catat bahwa Scott di Bab 4 memilih menggunakan **bentuk setengah kuat** sebagai fokus utama karena relevansinya dengan laporan keuangan yang merupakan informasi publik. Fama (1991) menambahkan pembaruan nomenklatur: (1) *tests for return predictability*, (2) *event studies*, (3) *tests for private information*. Waktu membaca: 30 menit.

**Langkah 3 — Scott Bab 4 §4.3–§4.5 (hal. 127–137): Implikasi bagi Pelaporan dan CAPM.**
Ini adalah inti ujian (UAS). Pahami enam implikasi Beaver (1973) yang dikutip Scott: (a) kebijakan akuntansi yang tidak memiliki efek arus kas tidak memengaruhi harga; (b) pengungkapan penuh (*full disclosure*) menyertai efisiensi pasar; (c) perusahaan tidak perlu khawatir akan investor naif karena mereka *price-protected*; (d) akuntansi bersaing dengan sumber informasi lain. Kuasai formula **market model**: Rjt = αj + βjRMt + εjt (persamaan 4.4, hal. 135), di mana εjt adalah *abnormal return* yang menjadi sinyal bahwa informasi baru telah menggerakkan harga. Waktu membaca: 60 menit.

**Langkah 4 — BBRI Laporan Tahunan 2025 §Ikhtisar Saham (hal. 35–36) dan §Dividen (hal. 487–489).**
Aplikasikan teori ke data nyata. Perhatikan bahwa harga saham BBRI turun dari penutupan Q1 2024 sebesar Rp6.050 menjadi Rp3.660 pada akhir 2025 — penurunan sebesar ~40% meski laba 2024 tercatat Rp60,3 triliun (AR 2025, hal. 28). Dividen per saham tahun buku 2024 sebesar Rp343,4 (AR 2025, hal. 487) dengan DPR 86%. Pertanyakan: apakah penurunan harga ini mencerminkan informasi baru yang legitimate ataukah *noise trading*/liquidity pricing? Waktu membaca: 30 menit.

**Langkah 5 — Aplikasi Konsep Event Study pada Pengumuman Laba BBRI.**
Rancang kerangka event study sederhana: identifikasi tanggal pengumuman RUPST BBRI (25 Maret 2025 untuk dividen tahun buku 2024; AR 2025, hal. 487), estimasi market model BBRI terhadap IHSG menggunakan data 120 hari sebelum *event window*, hitung *cumulative abnormal return* (CAR) pada jendela [-1, +1] hari seputar tanggal pengumuman. Bandingkan dengan pengumuman laba interim (16 Desember 2024; AR 2025, hal. 488). Waktu: 45 menit sebagai latihan.

Total waktu rekomendasi: ~3.5 jam untuk penguasaan dasar sebelum kelas.

---

## 2. Grid Konsep (4 Kuadran)

Grid ini memetakan konsep utama Minggu 11 ke empat kategori warna sesuai sistem pedagogis mata kuliah.

### Kuadran Biru — Teori Utama (*Core Theory*)

| Konsep | Definisi Scott/Fama | Halaman Scott |
|---|---|---|
| **Hipotesis Pasar Efisien (efficient market hypothesis/EMH)** | Pasar di mana harga sekuritas setiap saat "fully reflect" semua informasi yang tersedia | hal. 122 |
| **Bentuk lemah (weak form)** | Harga hanya mencerminkan data harga historis; pengujian dengan serial correlation | Fama (1970) |
| **Bentuk setengah kuat (semi-strong form)** | Harga mencerminkan semua informasi publik (laporan keuangan, pengumuman, berita media) | hal. 122 |
| **Bentuk kuat (strong form)** | Harga mencerminkan semua informasi termasuk informasi privat/orang dalam | hal. 122 |
| **Fair game** | Investor tidak dapat secara konsisten memperoleh excess return di atas expected return yang disesuaikan risiko | hal. 123 |
| **Random walk** | Deret waktu perubahan harga yang tidak berkorelasi serial — konsekuensi logis dari efisiensi pasar | hal. 123 |

### Kuadran Ungu — Ekonomi Informasi (*Information Economics*)

| Konsep | Peran dalam Kerangka EMH |
|---|---|
| **Asimetri informasi (information asymmetry)** | Alasan fundamental mengapa akuntansi eksis; memunculkan adverse selection dan moral hazard (Scott, hal. 121) |
| **Full disclosure** | Implikasi langsung EMH: pasar "mendengar" kandungan informasi apapun bentuknya — catatan kaki sama dengan laporan utama (Scott, hal. 120) |
| **Price-protection** | Investor naif "dilindungi" oleh harga efisien tanpa perlu analisis sendiri (Scott, hal. 128) |
| **Noise traders** | Pedagang yang bertransaksi bukan atas dasar informasi; mengurangi informativeness harga tetapi memungkinkan insentif untuk mengumpulkan informasi (Scott, hal. 130) |
| **Fundamental value** | Nilai teoretis jika tidak ada informasi dalam; efficient price selalu di bawah fundamental value jika ada informasi orang dalam (Scott, hal. 140) |
| **Partially informative prices** | Akomodasi teoretis atas inkonsistensi logis Grossman (1976): harga mencerminkan sebagian informasi, sisanya mendorong investor mengumpulkan info tambahan (Scott, hal. 131) |

### Kuadran Hijau — Konteks Indonesia (*Indonesian Context*)

| Aspek | Realitas IDX / BBRI |
|---|---|
| **Likuiditas BBRI** | Volume perdagangan 2025 berkisar 10,69–17,82 miliar lembar per kuartal (AR 2025, hal. 36); kapitalisasi pasar Rp554,71–613,81 triliun (AR 2025, hal. 35) — salah satu saham paling likuid di IDX |
| **Indeks LQ45 dan blue chip** | BBRI adalah anggota LQ45 sejak IPO November 2003 (AR 2025, hal. 13) |
| **OJK insider trading regulation** | POJK Nomor 17/2023 dan sistem *Pencegahan Transaksi Orang Dalam (Insider Trading)* yang diimplementasikan BBRI (AR 2025, hal. 904) |
| **Semi-annual/quarterly earnings disclosure** | BBRI merilis laporan keuangan triwulanan sesuai POJK, memberikan banyak titik *event* untuk studi |
| **Kepemilikan pemerintah** | Negara RI (via BP BUMN dan Danantara) memiliki 53,19% saham BBRI (AR 2025, hal. 11); dapat menciptakan asimetri informasi sistemik terkait kebijakan BUMN |
| **Literatur empirik IDX** | Studi semi-strong efficiency IDX menunjukkan bukti campuran: efisiensi lebih tinggi pada saham blue-chip seperti BBRI, lebih rendah pada small-cap |

### Kuadran Amber — Pengukuran dan Valuasi (*Measurement & Valuation*)

| Metode | Formula / Aplikasi |
|---|---|
| **Return periode t** | Rjt = (Pjt + Djt − Pj,t−1) / Pj,t−1 (Scott Persamaan 4.1, hal. 133) |
| **Expected return CAPM** | E(Rjt) = Rf(1 − βj) + βjE(RMt) (Scott Persamaan 4.3, hal. 133) |
| **Market model (ex post)** | Rjt = αj + βjRMt + εjt (Scott Persamaan 4.4, hal. 135) |
| **Abnormal return** | AR_jt = Rjt − E(Rjt); komponen εjt menangkap dampak informasi tak-terduga |
| **Cumulative Abnormal Return (CAR)** | CAR = Σ εjt sepanjang event window [t1, t2] |
| **Beta** | βj = Cov(j,M) / Var(M); mengukur systematic risk BBRI terhadap IHSG |
| **EPS BBRI 2025** | Rp376 per lembar (dasar dan dilusian) (AR 2025, hal. 29) |
| **BVPS BBRI 2025** | Total ekuitas induk Rp324,03 triliun ÷ 151.559.001.604 lembar = Rp2.138 per lembar |

---

## 3. Diagram Alur (*Flowchart*) Proses Informasi dalam Pasar Efisien

```
                  [Informasi Baru Muncul]
                  (earnings release, dividend
                   announcement, corporate action)
                           │
                           ▼
          [Investor Informed Menerima Sinyal]
          (analyst, fund manager, proprietary trader)
                           │
                           ▼
             [Revisi Ekspektasi E(Pjt+1, Djt+1)]
                           │
                           ▼
          [Buy/Sell Orders Mengalir ke Pasar]
                           │
                           ▼
              [Harga Bergerak: Arbitrage]
                           │
                           ▼
     [Harga Baru "Fully Reflect" Informasi Publik]
                           │
                           ▼
             [Abnormal Return εjt ≠ 0 pada t=0]
             [εjt = 0 pada t>0 (random walk resumes)]
                           │
                           ▼
        [Ekuilibrium Baru; Menunggu Informasi Baru]
                           │
                           ▼
   ┌────────────────────────────────────────────┐
   │  IMPLIKASI BAGI PELAPORAN KEUANGAN:        │
   │  • Bentuk pengungkapan tidak krusial        │
   │    — isi informasi yang dihargai           │
   │  • Full disclosure optimal                  │
   │  • Kebijakan akuntansi tanpa dampak         │
   │    arus kas tidak menggerakkan harga       │
   │  • Auditor, MD&A, catatan kaki semuanya    │
   │    "dihitung" oleh pasar                    │
   └────────────────────────────────────────────┘
```

Diagram menunjukkan bahwa EMH bukan klaim "harga selalu benar" melainkan klaim bahwa proses penyesuaian berlangsung cepat dan tidak bias secara sistematis. Catatan penting: Scott (hal. 131) menekankan bahwa dalam praktiknya harga hanya **partially informative** — ada ruang bagi analis yang sungguh-sungguh menganalisis laporan tahunan untuk mengidentifikasi mispricing temporer, inilah yang mempertahankan insentif produksi informasi.

---

## 4. Kutipan Kunci (*Key Quotes*)

### Kutipan 1 — Definisi EMH (Fama via Scott, hal. 122)

> **Bahasa asli (English):** "An efficient securities market is one where the prices of securities traded on that market at all times fully reflect all information that is publicly known about those securities."

> **Terjemahan Indonesia:** "Pasar sekuritas yang efisien adalah pasar di mana harga sekuritas yang diperdagangkan pada pasar tersebut setiap saat sepenuhnya mencerminkan semua informasi yang diketahui publik mengenai sekuritas tersebut."

**Mengapa penting:** Definisi ini menjadi pengujian teori utama bagi praktisi akuntansi. Jika benar, maka keputusan manajemen tentang "sampul" laporan keuangan (misalnya apakah menggunakan metode penyusutan garis lurus atau saldo menurun) tidak memengaruhi harga saham sepanjang kebijakan itu diungkapkan — karena pasar dapat mengkonversikan antar kebijakan. Implikasi ini secara kualitatif mengubah cara pandang akuntan profesional terhadap "permainan angka" yang hanya memengaruhi laba akuntansi tanpa memengaruhi arus kas.

### Kutipan 2 — Implikasi bagi Kebijakan Akuntansi (Beaver via Scott, hal. 127)

> **Bahasa asli:** "The efficient market argument is that as long as firms disclose their selected policy and any additional information needed to convert from one method to another, the market can see through to the ultimate cash flow and dividend implications regardless of which accounting policy is actually used for reporting. In effect, the efficient market is not 'fooled' by differing accounting policies when comparing different firms' securities."

> **Terjemahan:** "Argumen pasar efisien adalah bahwa selama perusahaan mengungkapkan kebijakan akuntansi yang dipilih dan informasi tambahan yang diperlukan untuk mengkonversi antar metode, pasar dapat melihat langsung ke implikasi arus kas dan dividen akhir terlepas dari kebijakan akuntansi apa yang sebenarnya digunakan untuk pelaporan. Pada praktiknya, pasar yang efisien tidak 'tertipu' oleh perbedaan kebijakan akuntansi ketika membandingkan sekuritas perusahaan-perusahaan yang berbeda."

**Konteks BBRI:** BBRI menggunakan PSAK 71 untuk instrumen keuangan dengan ECL (expected credit loss). Kebijakan ini menghasilkan CKPN Rp83,06 triliun pada 2025 (AR 2025, hal. 26). Jika BBRI mengubah metodologi ECL internalnya (misalnya mengubah skenario makro), laba akuntansi dapat bergerak signifikan. Namun, sepanjang kebijakan diungkapkan penuh, pasar efisien secara teoretis dapat "melihat tembus" perubahan teknis itu dan hanya bereaksi pada bagian yang benar-benar menyiratkan arus kas masa depan berbeda.

---

## 5. Kacamata Dosen (*Instructor's Lens*) — Fokus UAS

### Tiga Area Ujian Tinggi Prioritas

**A. Ketiga Bentuk EMH dan Pengujian Empiriknya**
Mahasiswa harus dapat: (1) membedakan weak/semi-strong/strong form; (2) menjelaskan mengapa Scott memilih semi-strong sebagai fokus teori akuntansi; (3) memberikan contoh studi yang menguji masing-masing bentuk (misalnya serial correlation tests untuk weak form, event studies untuk semi-strong, insider trading studies untuk strong form).

**B. Event Study dan Perhitungan Abnormal Return**
Langkah-langkah yang harus dikuasai: (1) estimasi market model βj dengan regresi OLS terhadap 120–250 hari pre-event data; (2) hitung expected return pada event window; (3) kalkulasi AR = Rjt − (αj + βjRMt); (4) agregasi CAR dan uji signifikansi dengan t-test. Kritis: pemahaman bahwa CAR positif pada hari 0 plus CAR ≈ 0 pada hari berikutnya adalah bukti semi-strong efficiency — pasar telah mencerna informasi dengan cepat.

**C. Implikasi bagi Standard-Setting (IASB/DSAK-IAI)**
Scott (hal. 127–128) menegaskan bahwa DSAK-IAI seharusnya mendorong full disclosure dan tidak khawatir tentang "mengurangi manipulasi" melalui restriksi pilihan kebijakan — karena pasar efisien dapat mengadjust. Namun, untuk kebijakan yang berdampak arus kas (misalnya aturan pajak penghasilan yang terkait dengan penyusutan di laporan laba rugi fiskal), disclosure saja tidak cukup karena pilihan kebijakan berdampak riil.

### Contoh Pertanyaan UAS (*Sample Question*)

> **Pertanyaan:** PT Bank Rakyat Indonesia Tbk (BBRI) mengumumkan laba bersih 2025 sebesar Rp57,13 triliun, turun 5,3% dari Rp60,30 triliun pada 2024 (AR 2025, hal. 28). Pada hari pengumuman (akhir Februari 2026), harga saham BBRI turun 2,5% sementara IHSG turun 0,3%. Beta BBRI diestimasi = 1,05.
>
> (a) Hitung abnormal return BBRI pada hari pengumuman. (5 poin)
> (b) Interpretasikan hasil (a) dalam konteks EMH bentuk setengah kuat. (5 poin)
> (c) Jika analis konsensus memperkirakan laba 2025 sebesar Rp55 triliun (yaitu mereka mengantisipasi penurunan lebih dalam), apakah penurunan harga 2,5% itu konsisten dengan EMH? Jelaskan. (10 poin)
>
> **Jawaban ringkas:**
> (a) Expected return = 1,05 × (−0,3%) = −0,315%. Abnormal return = −2,5% − (−0,315%) = −2,185%.
> (b) AR negatif signifikan menunjukkan pasar merespons informasi baru secara cepat. Konsisten dengan semi-strong efficiency karena harga bergerak segera setelah informasi publik dirilis.
> (c) Jika konsensus Rp55 triliun, maka laba aktual Rp57,13 triliun adalah *good news* relatif terhadap ekspektasi (meskipun turun dari tahun sebelumnya). Dalam EMH, pasar seharusnya **naik** sebagai respons atas earnings surprise positif. Harga yang tetap turun −2,185% AR mungkin menyiratkan: (i) pasar juga memproses informasi lain negatif (misalnya panduan forward rendah), atau (ii) kualitas laba dipersepsikan rendah (misalnya didorong oleh pembalikan CKPN, bukan ekspansi inti), atau (iii) inefisiensi/overreaction sementara.

---

*Selamat belajar. Minggu 11 membangun jembatan antara teori akuntansi normatif dan realitas pasar modal — kunci keberhasilan UAS adalah kemampuan menghitung, menginterpretasi, dan mengritisi simultan.*
