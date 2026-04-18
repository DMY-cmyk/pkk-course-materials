# Review Sheet — Minggu 06: Kegunaan Informasi Akuntansi

> **Topik:** Usefulness of Accounting Information to Investors and Creditors
> **Bacaan Inti:** Wolk Ch. 8; Scott Ch. 3 & 6.10; Ohlson (1995)
> **Perusahaan Jangkar:** PT Bank Central Asia Tbk (BBCA) — Laporan Tahunan 2025

---

## Kamus Istilah

| Istilah | Definisi Ringkas |
|:--------|:-----------------|
| **Decision Usefulness** | Tujuan utama pelaporan keuangan: menyediakan informasi yang berguna bagi investor, kreditur, dan pemakai lain dalam pengambilan keputusan alokasi sumber daya (IASB CF §1.2). |
| **Relevance (Relevansi)** | Karakteristik fundamental pertama: informasi yang mampu membuat perbedaan dalam keputusan pemakai. Terdiri dari *predictive value*, *confirmatory value*, dan *materiality*. |
| **Faithful Representation** | Karakteristik fundamental kedua: informasi yang secara jujur merepresentasikan substansi ekonomi — lengkap (*complete*), netral (*neutral*), dan bebas dari kesalahan material (*free from error*). |
| **Predictive Value** | Kemampuan informasi historis untuk membantu pemakai memperkirakan hasil masa depan. Contoh: tren laba BBCA 5 tahun membantu proyeksi EPS 2026. |
| **Confirmatory Value** | Kemampuan informasi untuk mengkonfirmasi atau merevisi ekspektasi sebelumnya. Contoh: realisasi ROE BBCA 23,3% vs target 21%-23% mengkonfirmasi ekspektasi positif. |
| **Materiality (Materialitas)** | Ambang signifikansi: informasi material jika penghilangan atau kesalahannya dapat mempengaruhi keputusan pemakai. Bersifat *entity-specific* dan bergantung pada konteks. |
| **Comparability** | Karakteristik *enhancing*: informasi dapat dibandingkan antar periode (*time-series*) dan antar entitas (*cross-section*). BBCA menyajikan data 5 tahun untuk memfasilitasi ini. |
| **Verifiability** | Karakteristik *enhancing*: dua pengamat independen dapat mencapai kesimpulan serupa. Audit oleh PwC meningkatkan *verifiability* estimasi manajemen BBCA. |
| **Timeliness** | Karakteristik *enhancing*: informasi tersedia sebelum kehilangan kapasitasnya untuk mempengaruhi keputusan. Laporan kuartalan lebih *timely* dibandingkan laporan tahunan. |
| **Understandability** | Karakteristik *enhancing*: disajikan dengan cara yang dapat dipahami pemakai yang memiliki pengetahuan bisnis dan keuangan memadai. |
| **Information Asymmetry** | Kondisi di mana manajemen memiliki informasi yang lebih banyak atau lebih baik dibandingkan pemakai eksternal. Laporan keuangan adalah mekanisme utama untuk menguranginya. |
| **Value Relevance** | Sejauh mana angka akuntansi berkorelasi secara statistik dengan harga saham atau *return* (Ball & Brown 1968). |
| **Earnings Response Coefficient (ERC)** | Sensitivitas harga saham terhadap kejutan laba (*unexpected earnings*). Tinggi untuk perusahaan dengan laba persisten, leverage rendah, dan beta rendah. |
| **Residual Income / Abnormal Earnings** | Laba dikurangi biaya modal: x^a_t = earnings_t − r × BV_{t−1}. Jika ROE > r, perusahaan menciptakan nilai ekonomi bagi pemegang saham. |
| **Clean Surplus** | Kondisi di mana semua perubahan ekuitas (selain transaksi dengan pemilik) melewati laporan laba rugi. Syarat model Ohlson agar BV_t = BV_{t−1} + earnings_t − dividends_t. |
| **Ohlson Model (1995)** | V_t = BV_t + Σ E[x^a_{t+τ}]/(1+r)^τ. Nilai intrinsik = nilai buku + PV laba abnormal masa depan. Menyatukan pendekatan *balance sheet* dan *income statement*. |
| **Earnings Persistence (ω)** | Parameter dalam model Ohlson: x^a_{t+1} = ω·x^a_t + ε. Nilai ω mendekati 1 = laba abnormal persisten. BBCA memiliki ω tinggi karena *economic moat* CASA. |
| **Expected Credit Loss (ECL)** | Model penurunan nilai dalam PSAK 71 (IFRS 9). Tiga stage: Stage 1 (ECL 12-bulan), Stage 2 (Lifetime ECL, SICR), Stage 3 (Lifetime ECL, credit-impaired). |
| **Fair Value Hierarchy** | Level 1 (harga pasar aktif), Level 2 (input observasi tidak langsung), Level 3 (input tidak observasi / model internal). Hampir seluruh efek BBCA berada di Level 1-2. |

---

## Cheat Sheet: Hierarki Karakteristik Kualitatif IASB

```
TUJUAN PELAPORAN KEUANGAN
"Decision Usefulness" (IASB CF §1.2)
         │
         ▼
┌─────────────────────────────────────────────────────┐
│         KARAKTERISTIK FUNDAMENTAL                   │
│   (Keduanya harus dipenuhi agar informasi berguna)  │
│                                                     │
│  ┌──────────────────┐   ┌───────────────────────┐  │
│  │   RELEVANCE      │   │  FAITHFUL             │  │
│  │   (Relevansi)    │   │  REPRESENTATION       │  │
│  │                  │   │  (Penyajian Jujur)    │  │
│  │ • Predictive     │   │                       │  │
│  │   Value          │   │ • Complete (Lengkap)  │  │
│  │ • Confirmatory   │   │ • Neutral (Netral)    │  │
│  │   Value          │   │ • Free from Error     │  │
│  │ • Materiality    │   │   (Bebas Kesalahan)   │  │
│  └──────────────────┘   └───────────────────────┘  │
└─────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────┐
│       KARAKTERISTIK ENHANCING                       │
│  (Meningkatkan kegunaan, tetapi tidak cukup sendiri)│
│                                                     │
│  COMPARABILITY  |  VERIFIABILITY  |  TIMELINESS    │
│  (Dapat        |  (Dapat         |  (Tepat Waktu)  │
│   Dibandingkan) |   Diverifikasi) |                │
│                                                     │
│               UNDERSTANDABILITY                     │
│               (Dapat Dipahami)                      │
└─────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────┐
│          BATASAN BIAYA (Cost Constraint)            │
│   Manfaat informasi harus melebihi biaya            │
│   penyediaan dan penggunaannya.                     │
└─────────────────────────────────────────────────────┘
```

**Catatan penting:** *Relevance* dan *faithful representation* adalah karakteristik **fundamental** — keduanya harus dipenuhi. Jika informasi relevan tapi tidak jujur (misal: laba yang dimanipulasi), atau jujur tapi tidak relevan (misal: informasi historis yang sudah basi), maka informasi tersebut **tidak berguna**. Empat karakteristik *enhancing* hanya menambah nilai di atas fondasi fundamental.

---

## Mapping BBCA ke Hierarki Karakteristik Kualitatif

| Karakteristik | Manifestasi di BBCA (2025) | Kualitas |
|:-------------|:--------------------------|:---------|
| Predictive Value | Tren laba 5 tahun + guidance ROE 21,5%-23,5% (2026) | Tinggi |
| Confirmatory Value | ROA 3,9% vs target 3,6%-3,8%; ROE 23,3% vs target 21%-23% | Tinggi |
| Materiality | Obligasi Rp 65M diungkapkan meski kecil secara kuantitatif | Tepat |
| Complete | Data 5 tahun, 16+ rasio prudensial, CALK rinci | Tinggi |
| Neutral | Audit PwC; ASEAN CG Score 108,2 | Tinggi |
| Free from Error | Opini WTP auditor (inferensi dari data AR) | Tinggi |
| Comparability | Data 5 tahun disajikan berjajar; rasio standar OJK | Tinggi |
| Verifiability | Audit Big-4; rasio prudensial terpublikasi BI | Tinggi |
| Timeliness | Laporan kuartalan + *earnings call* + situs IR | Tinggi |
| Understandability | Ikhtisar 3 halaman cukup untuk investor ritel | Moderat |

---

## Lima Pertanyaan Esensial

**Q1. Apa perbedaan mendasar antara investor ekuitas dan kreditur dalam menggunakan informasi akuntansi?**

Investor ekuitas adalah *residual claimant* yang berfokus pada *upside* (pertumbuhan laba, ROE, dividen) karena mereka mendapatkan seluruh nilai setelah kewajiban terbayar. Kreditur adalah *fixed claimant* yang berfokus pada *downside protection* (kemampuan membayar bunga dan pokok, kualitas agunan, *covenant compliance*) karena mereka tidak menikmati upside di atas kupon. Kebijakan akuntansi yang meningkatkan kegunaan bagi investor (mis. *fair value* — lebih relevan) bisa merugikan kreditur (volatilitas laba bisa memicu pelanggaran *debt covenant*). Dalam kasus BBCA: investor menggunakan ROE 23,3% dan P/BV 3,8x; kreditur menggunakan LCR 310,8% dan CAR 29,8%.

**Q2. Mengapa Ball & Brown (1968) penting bagi teori *decision usefulness*?**

Ball & Brown adalah *event study* pertama yang secara empiris membuktikan bahwa laporan keuangan memiliki *information content*. Mereka menunjukkan bahwa perusahaan dengan "berita baik" laba (realisasi di atas ekspektasi) menghasilkan *abnormal return* positif kumulatif, sementara "berita buruk" menghasilkan *abnormal return* negatif — dan sebagian besar informasi sudah diantisipasi pasar sebelum pengumuman resmi. Ini membuktikan bahwa pasar *menggunakan* informasi akuntansi, mengkonfirmasi premis normative bahwa laporan keuangan seharusnya dirancang untuk berguna (*decision useful*). Tanpa bukti empiris Ball & Brown, teori *decision usefulness* akan tetap menjadi klaim normatif tanpa dukungan data.

**Q3. Bagaimana model Ohlson (1995) menghubungkan nilai buku dan laba dengan nilai intrinsik perusahaan?**

Model Ohlson: **V_t = BV_t + Σ E_t[x^a_{t+τ}] / (1+r)^τ**, di mana x^a_t = laba_t − r × BV_{t−1} adalah *abnormal earnings* (laba abnormal). Intuisinya: jika perusahaan hanya mampu menghasilkan ROE = biaya ekuitas (r), tidak ada *abnormal earnings*, dan nilai pasar = nilai buku. Jika ROE > r secara persisten, ada *goodwill* yang bernilai PV laba abnormal masa depan. BBCA dengan ROE 23,3% vs biaya ekuitas ~12%: laba abnormal per saham ≈ Rp 258/tahun. P/BV 3,8x berarti pasar menilai goodwill BBCA sebesar 2,8 × BV = sekitar Rp 713 triliun — *belief* bahwa laba abnormal ini akan persisten sangat lama.

**Q4. Apa yang dimaksud dengan *information asymmetry* dan bagaimana laporan keuangan mengatasinya?**

*Information asymmetry* terjadi ketika manajemen memiliki informasi tentang perusahaan yang lebih baik daripada investor eksternal. Ini menciptakan dua masalah: *adverse selection* (investor tidak tahu kualitas sebenarnya perusahaan, seperti di pasar "lemons" Akerlof) dan *moral hazard* (manajemen bisa bertindak demi kepentingan sendiri tanpa sepengetahuan investor). Laporan keuangan mengurangi asimetri dengan mengharuskan perusahaan mengungkapkan informasi material secara transparan dan terverifikasi (audit). Di BBCA: 16+ rasio prudensial, distribusi ECL per stage, dan Laporan Direksi yang substantif semuanya berfungsi mengurangi asimetri — meskipun asimetri residual (seperti model internal ECL) tetap ada.

**Q5. Mengapa BBCA memiliki P/BV 3,8x meskipun laporan keuangan berbasis *historical cost* yang cenderung *understate* nilai?**

P/BV 3,8x mencerminkan bahwa pasar memproyeksikan *abnormal earnings* yang persisten — yaitu ROE jauh di atas biaya ekuitas selama bertahun-tahun ke depan. Tiga faktor mendorong ini: (1) *Moat* CASA 83,7% yang memberikan biaya pendanaan sangat rendah dan defensif terhadap persaingan; (2) jaringan 1.270 cabang + 43,5 juta rekening yang menciptakan *switching cost* tinggi bagi nasabah; (3) *brand equity* "BCA" yang menjadi sinonim perbankan transaksional di Indonesia. Aset-aset tidak berwujud ini tidak tercatat di neraca (PSAK 19 melarang *internally generated goodwill*), sehingga nilai buku hanya Rp 2.288/saham sementara pasar menghargai Rp 8.075/saham — selisihnya adalah *goodwill* implisit yang dipercayai pasar akan menghasilkan *abnormal earnings* di masa depan.

---

## Ringkasan Perbandingan: Investor vs Kreditur BBCA

| Dimensi | Investor Ekuitas | Kreditur |
|:--------|:-----------------|:---------|
| **Klaim** | Residual (setelah semua) | Fixed (bunga + pokok) |
| **Fokus Risiko** | Upside potential | Downside protection |
| **Rasio Utama** | ROE, EPS, P/E, P/BV, NIM | LCR, NSFR, CAR, NPL |
| **Nilai BBCA 2025** | ROE 23,3%; EPS Rp 467; P/E 17,3x | LCR 310,8%; CAR 29,8%; NPL 1,7% |
| **Model Analisis** | Ohlson, DCF, DDM | Altman Z-score, Stress Test |
| **Karakteristik Kualitatif** | Predictive value, timeliness | Verifiability, completeness |

---

## Formula Kunci

**Laba Abnormal (Residual Income):**
```
x^a_t = earnings_t − r × BV_{t−1}
       = (ROE − r) × BV_{t−1}
```

**Model Ohlson:**
```
V_t = BV_t + Σ E_t[x^a_{t+τ}] / (1+r)^τ
```

**Earnings Response Coefficient (ERC):**
```
CAR_j = α + β × UE_j + ε_j
         └─────────────────── β = ERC
```

**ERC tinggi jika:** laba persisten, leverage rendah, beta rendah, pertumbuhan tinggi.

**Clean Surplus:**
```
BV_t = BV_{t−1} + earnings_t − dividends_t
```
Dilanggar jika ada OCI yang melewati neraca langsung (FVOCI di BBCA).

---

*Disusun untuk MNK202 — Pelaporan Keuangan Korporat, Pascasarjana STIE YKPN Yogyakarta. Minggu 06.*
