# Review Sheet — Minggu 10: Laporan Arus Kas & Kualitas Akrual

**Mata Kuliah:** MNK202 Pelaporan Keuangan Korporat
**Topik:** The Statement of Cash Flows and Accrual Quality
**Bacaan:** Wolk, Dodd & Rozycki (2017), Ch. 13; PSAK 2; Sloan (1996); Damodaran (2012)
**Anchor Company:** PT Telkom Indonesia Tbk (TLKM) — Annual Report 2024

---

## Kamus Istilah

| Istilah | Definisi | Sumber |
|---|---|---|
| **Laporan Arus Kas (LAK)** / *Statement of Cash Flows* (CFS) | Laporan keuangan yang mengklasifikasikan perubahan kas dan setara kas ke dalam tiga aktivitas: operasi, investasi, dan pendanaan | PSAK 2 (IAS 7) |
| **Setara Kas** (*Cash Equivalents*) | Investasi jangka pendek, sangat likuid, mudah dikonversi ke kas, dan tidak terekspos risiko perubahan nilai material; umumnya jatuh tempo ≤ 3 bulan | PSAK 2, par. 6 |
| **Arus Kas Operasi (CFO)** | Arus kas dari transaksi yang menghasilkan pendapatan utama entitas; komponen terpenting karena mencerminkan kemampuan inti bisnis menghasilkan kas | PSAK 2; Wolk Ch. 13 |
| **Arus Kas Investasi (CFI)** | Arus kas dari perolehan dan pelepasan aset jangka panjang serta investasi lain; biasanya negatif pada perusahaan tumbuh (CapEx tinggi) | PSAK 2; Wolk Ch. 13 |
| **Arus Kas Pendanaan (CFF)** | Arus kas dari transaksi dengan pemilik (dividen, buyback) dan kreditor (penerbitan/pelunasan utang, obligasi) | PSAK 2; Wolk Ch. 13 |
| **Metode Langsung** (*Direct Method*) | Metode penyajian CFO yang menampilkan penerimaan dan pengeluaran kas operasi secara bruto; didorong FASB/IASB tapi jarang digunakan | PSAK 2, par. 18 |
| **Metode Tidak Langsung** (*Indirect Method*) | Metode penyajian CFO mulai dari laba bersih, disesuaikan dengan pos non-kas dan perubahan modal kerja; dominan di praktik global (>95% perusahaan) | PSAK 2, par. 18 |
| **Kualitas Akrual** (*Accrual Quality*) | Presisi dengan mana akrual merefleksikan arus kas yang mendasarinya; akrual berkualitas tinggi bertransformasi menjadi kas dengan cepat | Richardson et al. (2005) |
| **Akrual Total** (*Total Accruals*) | NI − CFO; selisih antara laba akuntansi dan kas yang dihasilkan; semakin besar, semakin tinggi risiko manipulasi | Sloan (1996) |
| ***Accrual Anomaly*** | Fenomena bahwa komponen akrual laba lebih rendah persistensinya dibanding komponen kas, namun pasar tidak sepenuhnya merefleksikan ini dalam harga | Sloan (1996) TAR |
| **Akrual Diskresioner** (*Discretionary Accruals*) | Komponen akrual yang mencerminkan pilihan manajemen — estimasi piutang tak tertagih, timing pengakuan, provisi; proksi untuk *earnings management* | Jones (1991); Dechow et al. (1995) |
| **Akrual Non-Diskresioner** | Komponen akrual yang terkait dengan pertumbuhan operasi normal (perubahan modal kerja operasional, depresiasi sesuai manfaat ekonomi) | Jones (1991) |
| ***Free Cash Flow to Firm* (FCFF)** | CFO + Beban Bunga×(1-t) − CapEx; arus kas untuk seluruh penyedia modal (pemegang utang + saham) setelah kebutuhan investasi terpenuhi | Damodaran (2012) |
| ***Free Cash Flow to Equity* (FCFE)** | CFO − CapEx + Utang Baru Bersih; arus kas yang tersedia bagi pemegang saham setelah memenuhi kebutuhan investasi dan kewajiban hutang | Damodaran (2012) |
| ***Dividend Payout Ratio* (DPR)** | Dividen / Laba Bersih; mengukur proporsi laba yang dibagikan sebagai dividen; interpretasi berbeda jika dihitung berbasis FCFE | Damodaran (2012) |
| **Capital Expenditure (CapEx)** | Pengeluaran untuk perolehan atau peningkatan aset tetap dan aset tidak berwujud berjangka panjang; biasanya muncul di aktivitas investasi CFS | PSAK 2 |
| ***Depresiasi & Amortisasi* (D&A)** | Pos non-kas terbesar yang ditambahkan kembali ke laba bersih dalam rekonsiliasi metode tidak langsung; bukan sumber kas meskipun sering disalahartikan demikian | PSAK 16; PSAK 19 |
| **PSAK 2** | Standar Akuntansi Indonesia tentang Laporan Arus Kas; adopsi IAS 7; berlaku efektif 1 Januari 2015; mewajibkan 3-aktivitas klasifikasi dan rekonsiliasi kas | DSAK IAI |
| **Rasio CFO/NI** | *Cash conversion ratio* — mengukur proporsi laba yang dikonversi menjadi arus kas operasi; > 1 menandakan laba berkualitas baik | Wolk Ch. 13 |

---

## Cheat Sheet 1: Rekonsiliasi Metode Tidak Langsung (Indirect Method)

```
LABA BERSIH
+ Penyusutan & Amortisasi (D&A)                [pos non-kas terbesar]
+ Kerugian Penurunan Nilai (Impairment)         [non-kas]
+ Beban Penyisihan (Piutang, Persediaan)        [non-kas]
+/- Perubahan Modal Kerja:
    - Kenaikan Piutang                          [− kas]
    + Penurunan Piutang                         [+ kas]
    - Kenaikan Persediaan                       [− kas]
    + Kenaikan Utang Usaha                      [+ kas]
    + Kenaikan Liabilitas Akrual                [+ kas]
- Keuntungan dari Penjualan Aset Tetap          [dipindah ke CFI]
+/- Pos lain                                   [beban non-kas, dll.]
────────────────────────────────────────────────
= ARUS KAS DARI AKTIVITAS OPERASI (CFO)

TLKM 2024:
Laba Bersih       Rp30.743T
+ D&A             Rp32.643T
+ Penyesuaian lain (neto)       ≈ Rp(1.786T)
─────────────────
CFO               Rp61.600T   → CFO/NI = 2,00x (kualitas sangat baik)
```

---

## Cheat Sheet 2: 14 Metrik Kunci Analisis Arus Kas

```
METRIK                  RUMUS                           INTERPRETASI
────────────────────────────────────────────────────────────────────
CFO/NI                  CFO / Laba Bersih               >1 baik; <1 warning
Accrual Ratio (Sloan)   (NI−CFO) / Avg Total Aset       Negatif = kualitas baik
CapEx/D&A               CapEx / D&A                     >1 = investasi aktif
FCFF                    CFO + Int(1−t) − CapEx          Arus kas seluruh modal
FCFE                    CFO − CapEx + Net Debt           Arus kas pemegang saham
DPR (NI basis)          Dividen / NI                    Historis; mudah dihitung
DPR (FCFE basis)        Dividen / FCFE                  Lebih konservatif & realistis
CFO/Revenue             CFO / Penjualan Bersih          Profitabilitas kas
Debt/EBITDA             Total Utang Berbunga / EBITDA   Leverage; <3x aman
EBITDA margin           EBITDA / Revenue                Proxy arus kas operasi kasar
CFO/Total Liabilities   CFO / Total Liabilitas          Kemampuan bayar utang
Free Cash Yield         FCFF / Market Cap               Valuasi relatif
Maintenance CapEx       CapEx − (D&A × faktor growth)   CapEx minimum agar aset stabil
Cash Conversion Cycle   DIO + DSO − DPO                 Efisiensi modal kerja (hari)
```

---

## Cheat Sheet 3: FCFF vs. FCFE

```
                        FCFF                    FCFE
────────────────────────────────────────────────────────────
Penyedia modal          Semua (debt + equity)   Pemegang saham saja
Rumus                   CFO + Int(1-t) - CapEx  CFO - CapEx + Net Borrowing
Discount rate           WACC                    Cost of equity (CAPM)
Cocok untuk             Perusahaan leverage      Perusahaan stable leverage
                        berubah                  atau bank
Manfaat                 Tidak dipengaruhi        Langsung relevan untuk
                        struktur modal           ekuitas
Kelemahan               Butuh tax rate dan       Sensitif terhadap asumsi
                        struktur modal           net borrowing masa depan
```

---

## Lima Pertanyaan Esensial

**Q1:** Mengapa Laporan Arus Kas diperlukan meskipun laporan laba rugi sudah menyajikan kinerja entitas? Apa yang "dilihat" CFS yang tidak terlihat dari laporan laba rugi?

**A1:** Laporan laba rugi berbasis akrual menyajikan laba yang mencerminkan ekonomi periode berjalan — bukan kas yang diterima/dikeluarkan saat itu. Akrual adalah estimasi manajemen (penyisihan piutang, depresiasi, provisi) yang dapat disalahgunakan. CFS menyajikan realitas kas yang tidak bisa dimanipulasi semudah akrual: kas yang masuk/keluar adalah fakta, bukan estimasi. CFS mengungkap tiga hal penting yang tidak terlihat di laba rugi: (1) apakah bisnis inti benar-benar menghasilkan kas (CFO); (2) seberapa banyak kas yang diinvestasikan untuk pertumbuhan (CFI); (3) bagaimana entitas mendanai operasinya — dari kas sendiri atau utang/saham baru (CFF). Dalam contoh TLKM 2024: laba bersih Rp30,743T "diperkuat" CFO Rp61,600T (2× lebih tinggi) karena D&A Rp32,643T bersifat non-kas — informasi ini hanya terlihat di CFS (Wolk Ch. 13; PSAK 2).

---

**Q2:** Jelaskan perbedaan metode langsung dan tidak langsung dalam penyajian aktivitas operasi CFS. Mengapa metode langsung dianggap lebih informatif tetapi jarang digunakan?

**A2:** Metode langsung menyajikan penerimaan dan pengeluaran kas operasi secara bruto: "Penerimaan dari pelanggan Rp151T", "Pembayaran kepada pemasok Rp89T" — pengguna dapat langsung melihat sumber kas. Metode tidak langsung mulai dari laba bersih dan menambahkan/mengurangkan penyesuaian: D&A ditambahkan (karena sudah mengurangi laba tapi bukan pengeluaran kas), perubahan piutang mengurangi CFO (pendapatan diakui tapi kas belum diterima), dst. Metode langsung lebih informatif karena pengguna tidak perlu melakukan "de-akrual" mental — setiap baris adalah arus kas nyata. Namun jarang digunakan karena: (1) biaya implementasi tinggi — memerlukan sistem paralel yang melacak setiap transaksi secara kas; (2) perusahaan harus mengungkap rekonsiliasi laba-ke-CFO pula (PSAK 2 par. 19) — sehingga manfaat incremental tidak sepadan; (3) tidak ada insentif kompetitif untuk mengadopsi jika kompetitor tidak melakukannya (Wolk Ch. 13).

---

**Q3:** Jelaskan model Sloan (1996) tentang *accrual anomaly*. Apa prediksi model ini dan apa bukti empirisnya?

**A3:** Sloan (1996) dalam "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?" (*TAR*) mendefinisikan Total Accruals = NI − CFO. Premis model: komponen kas laba lebih persisten dibanding komponen akrual — laba yang tinggi karena banyak akrual (bukan karena kas) lebih mungkin untuk *mean-revert* di masa depan. Jika pasar sepenuhnya efisien, harga sudah mengantisipasi perbedaan persistensi ini. Bukti Sloan: pasar **TIDAK** sepenuhnya mengantisipasi rendahnya persistensi akrual. Perusahaan dengan akrual tinggi (laba > kas) mengalami *negative returns* di masa depan; perusahaan dengan akrual rendah (kas > laba) mengalami *positive returns*. Strategi long-short berdasarkan akrual menghasilkan abnormal return ~10% per tahun — anomali ini (accrual anomaly) menantang hipotesis pasar efisien bentuk setengah kuat. Namun banyak studi selanjutnya menunjukkan anomali ini melemah setelah dipublikasikan (investor mengeksploitasinya) (Sloan, 1996; Richardson et al., 2005).

---

**Q4:** Apa perbedaan antara FCFF dan FCFE, dan kapan masing-masing lebih tepat digunakan sebagai dasar valuasi?

**A4:** FCFF (Free Cash Flow to Firm) = CFO + Biaya Bunga×(1−t) − CapEx: arus kas untuk seluruh penyedia modal sebelum pembayaran bunga, didiskonto dengan WACC. FCFE (Free Cash Flow to Equity) = CFO − CapEx + Net Borrowing Baru: arus kas residual untuk pemegang saham setelah utang dilayani, didiskonto dengan Cost of Equity. FCFF lebih tepat ketika: (a) struktur modal perusahaan berubah signifikan (leverage ratio berfluktuasi) — FCFF tidak dipengaruhi oleh jumlah utang; (b) analisis perbandingan lintas-industri dengan leverage berbeda. FCFE lebih tepat ketika: (a) perusahaan memiliki leverage stabil; (b) analis langsung menilai nilai ekuitas (bukan enterprise value); (c) perusahaan keuangan (bank) di mana utang adalah "bahan baku" bukan financing — FCFF tidak bermakna untuk bank. Untuk TLKM (telekomunikasi): FCFF lebih tepat karena leverage berubah (ekspansi infrastruktur dengan utang), sementara FCFE digunakan untuk menilai apakah dividen berkelanjutan (Damodaran, 2012).

---

**Q5:** Apa kelemahan utama *Dividend Payout Ratio* (DPR) berbasis laba bersih, dan mengapa DPR berbasis FCFE memberikan gambaran yang lebih akurat tentang keberlanjutan dividen?

**A5:** DPR berbasis NI = Dividen / Laba Bersih. Kelemahannya: laba bersih mencakup beban non-kas (depresiasi Rp32,6T di TLKM) yang mengurangi laba tapi tidak mengonsumsi kas. Sebaliknya, CapEx (investasi aset tetap baru) mengonsumsi kas tapi tidak masuk laba rugi secara langsung. Jadi DPR-NI membandingkan dividen dengan angka yang tidak merepresentasikan kas yang benar-benar tersedia. DPR-FCFE menggunakan FCFE = CFO − CapEx + Net Borrowing sebagai denominator — ini adalah kas yang benar-benar "tersisa" setelah perusahaan mempertahankan dan mengembangkan aset produktifnya dan melunasi kewajiban hutang. Jika DPR-FCFE > 100%, perusahaan membayar dividen melebihi arus kas bebas untuk ekuitas — berarti mendanai dividen dari kas cadangan atau utang baru, yang tidak sustainable jangka panjang. Untuk TLKM: DPR-NI ≈74,8% tampak moderat, tetapi DPR-FCFE ≈44,2% menunjukkan bahwa setelah CapEx yang besar, TLKM masih memiliki ruang untuk dividen — sinyal keberlanjutan lebih baik dari UNVR (DPR-FCFE UNVR > 100%) (Damodaran, 2012).

---

*Referensi: Wolk, Dodd & Rozycki (2017) Ch. 13; PSAK 2 (IAS 7); Sloan (1996) TAR; Richardson et al. (2005) JAE; Dechow & Dichev (2002) TAR; Jones (1991); Damodaran (2012) *Investment Valuation*; TLKM Annual Report 2024.*
