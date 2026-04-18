# Master Cheat Sheet UAS MNK202 — Minggu 14

> Lembar ringkas ini adalah kompilasi istilah kunci, rumus, dan peta integrasi untuk seluruh materi Pasca-UTS (W8–W12) plus elemen kritis dari Pra-UTS (W1–W7). Gunakan di malam sebelum UAS sebagai refresher cepat. Format dirancang agar Anda dapat membaca satu sesi (45 menit) sebelum tidur dan kembali ke ruang ujian dengan peta konsep lengkap di kepala.

---

## §A. Istilah Kunci per Minggu

### W8 — Laporan Posisi Keuangan (Balance Sheet)
1. **Aset lancar (current asset).** Aset yang diharapkan terealisasi dalam 12 bulan atau siklus operasi normal (PSAK 1 paragraf 66).
2. **Off-balance sheet financing.** Pendanaan yang tidak ditampilkan sebagai liabilitas neraca; contoh pre-PSAK 73: sewa operasi; pasca-PSAK 73: komitmen dan kontinjensi.
3. **Goodwill.** Selisih imbalan akuisisi di atas nilai wajar aset bersih teridentifikasi (PSAK 22). Tidak diamortisasi, tetapi diuji penurunan nilai tahunan.
4. **Non-controlling interest (NCI).** Bagian ekuitas anak perusahaan yang tidak dimiliki induk; disajikan terpisah dalam ekuitas konsolidasian (PSAK 65).
5. **CKPN (Cadangan Kerugian Penurunan Nilai).** Pencadangan atas expected credit loss PSAK 71 untuk aset keuangan; sangat material bagi bank.

### W9 — Laporan Laba Rugi & Kualitas Laba
1. **Earnings persistence.** Kemampuan laba saat ini memprediksi laba masa depan; diukur dengan koefisien autoregresi laba (AR(1)).
2. **Operating leverage.** Sensitivitas EBIT terhadap perubahan penjualan; DOL = (%ΔEBIT)/(%ΔSales). Tinggi untuk perusahaan dengan biaya tetap besar.
3. **OCI (Other Comprehensive Income).** Pos pendapatan dan beban yang tidak masuk P/L; contoh: revaluasi aset tetap, translation differences, hedging instruments (PSAK 1 paragraf 7).
4. **By nature vs by function.** Klasifikasi beban: sesuai sifat (bahan baku, tenaga kerja, depresiasi) atau sesuai fungsi (HPP, pemasaran, umum-administrasi). PSAK 1 mengizinkan pilihan tetapi mensyaratkan konsistensi.
5. **Non-recurring items.** Pos-pos luar biasa atau tidak berulang; harus dipisahkan dalam analisis kualitas laba karena mengurangi persistence.

### W10 — Laporan Arus Kas & Analisis Akrual
1. **CFO (Cash Flow from Operations).** Arus kas dari aktivitas operasi (PSAK 2); indikator likuiditas fundamental.
2. **FCFF (Free Cash Flow to Firm).** Kas tersedia untuk semua penyedia modal setelah reinvestasi. Rumus: **FCFF = EBIT(1-t) + D&A - ΔWC - CapEx**.
3. **Total accruals.** Laba dikurangi kas operasi; TA = NI - CFO. Indikator konservatisme akrual.
4. **Accruals ratio.** TA dibagi total aset; batas indikatif: > 5% = red flag.
5. **Five Bold Moves.** Kerangka McKinsey untuk restrukturisasi strategis: portfolio, resource allocation, M&A, productivity, differentiation.

**Rumus wajib hafal W10:** `FCFF = EBIT × (1 - tarif pajak) + Depresiasi & Amortisasi - Perubahan Modal Kerja - CapEx`

### W11 — Hipotesis Pasar Efisien (EMH)
1. **EMH lemah.** Harga mencerminkan informasi harga historis; trading aturan dari data historis tidak menghasilkan abnormal return (Fama 1970).
2. **EMH semi-kuat.** Harga mencerminkan semua informasi publik; pengumuman publik direspons segera.
3. **EMH kuat.** Harga mencerminkan informasi publik dan privat; insider trading tidak menghasilkan abnormal return (biasanya ditolak secara empiris).
4. **Abnormal return.** Return aktual dikurangi expected return. Dasar event study.
5. **PEAD (Post-Earnings Announcement Drift).** Anomali: AR berlanjut (tidak reversal) selama beberapa minggu setelah pengumuman earnings, bertentangan dengan EMH semi-kuat (Bernard & Thomas 1989).

**Rumus wajib hafal W11:** `AR_it = R_it - E(R_it)`, di mana `E(R_it) = α_i + β_i × R_mt` (market model). Cumulative: `CAR_i[T1,T2] = Σ AR_it dari T1 ke T2`.

### W12 — Manajemen Laba (Earnings Management)
1. **Discretionary accruals (DA).** Akrual yang berada di bawah kontrol manajer; proksi manajemen laba.
2. **Model Jones (1991).** Memisahkan NDA (non-discretionary accruals) dari DA menggunakan perubahan penjualan dan PPE sebagai kontrol. Residual regresi = DA.
3. **Real earnings management.** Manipulasi aktivitas operasional nyata (over-produksi, potongan harga akhir kuartal, pemotongan R&D) untuk mempengaruhi laba (Roychowdhury 2006).
4. **Bonus plan hypothesis.** Manajer dengan bonus berbasis laba akan memilih akrual yang meningkatkan laba (Watts & Zimmerman 1986).
5. **Debt covenant hypothesis.** Perusahaan yang mendekati pelanggaran kovenan akan memilih akrual yang meningkatkan laba untuk mengurangi risiko default teknis.

**Rumus wajib hafal W12:** Model Jones: `TA_it / A_{i,t-1} = α_i × (1/A_{i,t-1}) + β_1 × (ΔREV_it/A_{i,t-1}) + β_2 × (PPE_it/A_{i,t-1}) + ε_it`. Residual ε_it = **DA** (proksi manajemen laba). Jones Modifikasi mengganti ΔREV dengan (ΔREV - ΔAR).

---

## §B. Tabel Integrasi Lintas-Minggu

| Konsep Pasangan | Hubungan | Contoh Soal UAS |
|-----------------|----------|-----------------|
| W9 × W10 | Kualitas laba bergantung pada kualitas akrual | "Bandingkan earnings quality UNVR dan GIAA melalui indikator akrual." |
| W10 × W12 | Akrual tinggi = potensi manajemen laba | "Perusahaan X melaporkan NI naik 40% tetapi CFO turun 20%. Evaluasi." |
| W11 × W12 | Manajemen laba menguji efisiensi pasar | "Jika pasar efisien semi-kuat, mengapa manajer masih melakukan earnings management?" |
| W5 × W8 | Definisi aset/liabilitas dari Kerangka menentukan klasifikasi neraca | "Apakah pos Y memenuhi definisi aset PSAK?" |
| W6 × W11 | Disclosure yang kuat memperkuat efisiensi pasar | "Diskusikan peran mandatory disclosure dalam mencegah insider trading." |
| W1 × W12 | Kelembagaan lemah = insentif manajemen laba lebih besar | "Mengapa BUMN lebih rentan terhadap political cost-motivated earnings management?" |

---

## §C. 10 Quick Q&A UAS

**Q1. Apa perbedaan persistence dan predictability dalam kualitas laba?**
A. Persistence: kemampuan laba bertahan tinggi melintasi waktu (AR(1) tinggi). Predictability: kemampuan laba saat ini memprediksi laba masa depan dengan tingkat error rendah. Keduanya berkorelasi tetapi tidak identik.

**Q2. Mengapa CFO bisa negatif sementara NI positif?**
A. Karena akrual positif besar. Contoh: piutang bertambah, persediaan menumpuk, pendapatan diakui tetapi belum diterima kas, atau akrual pendapatan dari revisi estimasi.

**Q3. Apa bedanya model Jones dan Jones Modifikasi?**
A. Jones asli menggunakan ΔREV sebagai regresor; Jones Modifikasi menggunakan (ΔREV - ΔAR) untuk mengontrol manipulasi pendapatan via piutang (Dechow et al. 1995).

**Q4. Apakah AR positif selalu berarti manajemen berkinerja baik?**
A. Tidak. AR positif bisa berarti: (a) kinerja sesungguhnya baik (sahih), (b) pasar bereaksi pada laba surface tanpa melihat kualitas (functional fixation), (c) informasi asimetris di mana pasar belum memiliki data kualitas akrual.

**Q5. Apa arti CAR = 0?**
A. Tidak ada abnormal return terakumulasi. Dapat berarti: (a) informasi sudah sepenuhnya diantisipasi (konsisten EMH semi-kuat kuat), (b) peristiwa tidak informatif, (c) reaksi positif dan negatif saling menetralkan.

**Q6. Apa yang dimaksud dengan "clean surplus"?**
A. Kondisi di mana seluruh perubahan ekuitas (kecuali transaksi dengan pemegang saham) melalui P/L. Jika OCI diakui, maka prinsip clean surplus dimodifikasi menjadi "dirty surplus". Kerangka Konseptual 2018 mempertahankan dirty surplus via OCI.

**Q7. Apa kaitan PSAK 73 dengan analisis leverage?**
A. PSAK 73 memindahkan sewa operasi dari off-balance sheet ke on-balance sheet sebagai hak-guna-aset dan liabilitas sewa. Dampaknya: aset dan liabilitas naik (leverage ratio naik), EBIT naik (depresiasi dan bunga menggantikan beban sewa), tetapi laba bersih jangka panjang relatif stabil.

**Q8. Apa tiga motif utama manajemen laba?**
A. (1) Bonus plan — manajer dengan bonus berbasis laba; (2) Debt covenant — menghindari pelanggaran kovenan; (3) Capital market — meningkatkan harga saham pra-IPO/SEO; (4) political-tax — mengurangi biaya politik atau pajak.

**Q9. Apa perbedaan real earnings management vs accruals-based?**
A. Accruals-based: memilih kebijakan akuntansi atau estimasi yang mempengaruhi akrual tanpa mengubah keputusan operasional nyata. Real: mengubah keputusan operasional nyata (produksi berlebihan, potongan harga akhir kuartal, pemangkasan R&D) dengan konsekuensi ekonomi riil jangka panjang.

**Q10. Bagaimana Kerangka Konseptual 2018 memperlakukan stewardship?**
A. Kerangka 2018 mengembalikan stewardship sebagai objective eksplisit (paragraf 1.2, 1.22–1.23) — manajemen bertanggung jawab atas pengelolaan sumber daya yang dipercayakan. Pra-2010, stewardship dihapus; revisi 2018 memasukkannya kembali karena umpan balik publik yang kuat.

---

## §D. 5 Top UAS Pitfalls to Avoid

**Pitfall 1 — Deskripsi tanpa evaluasi.** Menulis "NTT menerapkan PSAK 72" bukan jawaban; "NTT menerapkan PSAK 72, tetapi pengungkapan alokasi transaksi loyalty points masih minim, sehingga kualitas pengakuan pendapatan sulit diverifikasi" adalah jawaban evaluatif.

**Pitfall 2 — Mengaku hafal tetapi salah aplikasi.** Sering terjadi pada Model Jones — mahasiswa menulis rumus benar tetapi salah mengidentifikasi mana yang diskresioner (residual) vs non-diskresioner (fitted value). Latih aplikasi numerik, bukan hanya rumus.

**Pitfall 3 — Mengabaikan konteks industri.** Rasio current ratio 1,5 adalah sehat untuk FMCG, tetapi rendah untuk retail (yang biasanya > 2,0) dan tinggi untuk bank (yang biasanya < 1,0 karena struktur neraca berbeda). Selalu sebut konteks industri.

**Pitfall 4 — Terjebak satu perspektif.** Soal UAS sintesis selalu meminta multi-perspektif. Jawaban yang hanya menggunakan satu kerangka (misalnya hanya EMH) akan kehilangan nilai karena tidak menampilkan kemampuan integrasi.

**Pitfall 5 — Tidak menjawab pertanyaan yang ditanyakan.** Dosen menulis "evaluasilah" — Anda mendeskripsikan. Dosen menulis "bandingkan" — Anda mendeskripsikan secara terpisah. Dosen menulis "rekomendasikan" — Anda menganalisis tanpa memberi rekomendasi. Baca kata kerja pertanyaan tiga kali sebelum menjawab.

---

## §E. Catatan Akhir

Hafalkan tiga hal saja jika waktu Anda sangat terbatas:
1. **Rumus FCFF** (W10) dan **Model Jones** (W12).
2. **Tiga bentuk EMH** (W11) dan implikasinya.
3. **Enam lensa analitis** (institusional, konseptual, disclosure, balance sheet, income, market) dari company-example.md.

Dengan ketiga itu, Anda dapat merangkai jawaban untuk 80% soal UAS. Sisanya 20% diselesaikan dengan logika dan pengalaman membaca laporan keuangan.

Selamat menempuh UAS. Pastikan tidur cukup dan sarapan sebelum ujian.

---

*Lembar ini berpasangan dengan study-guide.md, summary.md, company-example.md, dan exercises.md pada folder week-14.*
