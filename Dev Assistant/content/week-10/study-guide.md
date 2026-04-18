# Study Guide — Minggu 10: Laporan Arus Kas & Kualitas Akrual

## Peta Konsep

| Dimensi | Metode Langsung (*direct method*) | Metode Tidak Langsung (*indirect method*) |
|---|---|---|
| Titik Awal | Penerimaan kas dari pelanggan | Laba bersih (*net income*) |
| Penyesuaian | Tidak memerlukan rekonsiliasi eksplisit | Menambah/mengurangi pos non-kas dan perubahan modal kerja |
| Yang Dihasilkan | Kas operasi langsung dari transaksi | Kas operasi via rekonsiliasi akrual-ke-kas |
| Keunggulan | Informasi langsung tentang sumber dan penggunaan kas | Menunjukkan hubungan laba-arus kas (*articulation*) |
| Kelemahan | Biaya penyusunan tinggi, data detail | Sulit dipahami pengguna non-akuntan |
| Dominasi Praktik | < 5% perusahaan global | > 95% perusahaan global (termasuk TLKM) |

| Tiga Aktivitas CFS (PSAK 2) | Contoh Masuk | Contoh Keluar |
|---|---|---|
| **Operasi** | Kas dari pelanggan, bunga diterima, restitusi pajak | Kas ke pemasok, gaji karyawan, pajak penghasilan, bunga dibayar |
| **Investasi** | Penjualan aset tetap, divestasi anak usaha, dividen dari asosiasi | Pembelian aset tetap (*capex*), akuisisi bisnis, penempatan deposito jangka panjang |
| **Pendanaan** | Penerbitan obligasi/saham, penarikan utang bank | Pembayaran dividen, pelunasan utang, *share buyback* |

| Metrik Kualitas Akrual | Formula | Interpretasi |
|---|---|---|
| *Cash Flow to Net Income Ratio* | CFO ÷ Laba Bersih | > 1 = akrual konservatif; < 1 = akrual agresif |
| *Accrual Ratio* (Sloan, 1996) | (Laba Bersih − CFO) ÷ Rata-rata Total Aset | Makin tinggi, makin rendah kualitas laba |
| *Modified Jones Model* | Sisa regresi akrual diskresioner | Estimasi manajemen laba |
| *Dechow-Dichev Model* | Sisa regresi akrual modal kerja atas CFO t-1, t, t+1 | Mengukur presisi estimasi akrual |

| FCF Variants | Formula | Peruntukan |
|---|---|---|
| **FCFF** (*Free Cash Flow to Firm*) | EBIT(1−T) + D&A − ΔWC − Capex | Valuasi seluruh perusahaan (menggunakan WACC) |
| **FCFE** (*Free Cash Flow to Equity*) | FCFF − Bunga(1−T) + Utang Baru Bersih | Valuasi ekuitas (menggunakan cost of equity) |

## Alur Pembelajaran

1. **Baca ringkasan utama (`summary.md`)** — 45–60 menit. Fokus pada sejarah PSAK 2, tiga komponen CFS, dan konsep kualitas akrual (Sloan, 1996; Dechow-Dichev, 2002).
2. **Pelajari contoh perusahaan (`company-example.md`)** — 60–90 menit. Telusuri struktur arus kas TLKM 2024, kalkulasi FCFF/FCFE, dan accrual ratio.
3. **Kerjakan latihan (`exercises.md`)** — 90 menit. Prioritaskan L3–L4 yang menuntut kalkulasi FCFF dan interpretasi rasio arus kas.
4. **Review istilah kunci (`review-sheet.md`)** — 30 menit. Gunakan sebagai bekal untuk diskusi kelas dan persiapan UTS.
5. **Baca Wolk Ch. 13** — 90 menit. Fokus pada argumen teoretis mengapa CFS menjadi laporan ketiga wajib (SFAS No. 95, 1987) dan kritik akademik terhadap metode tidak langsung.
6. **Baca Scott Ch. 5** (opsional) — 45 menit. Untuk konteks *accrual anomaly* dalam *efficient market hypothesis*.

## Pull Quote

> "The statement of cash flows attempts to rectify deficiencies of the accrual-based income statement by providing information about the cash generating ability of the firm. However, the indirect method—while retaining the articulation with net income—obscures rather than reveals the direct cash transactions with customers and suppliers, and thus only partially fulfills the mandate of SFAS No. 95." — Wolk, Dodd, & Rozycki (2017, Ch. 13)

## Lensa Dosen

Laporan Arus Kas adalah "*lie detector*" bagi laba akrual. Jika laba bersih tumbuh pesat namun arus kas operasi stagnan atau negatif, hampir selalu ada *red flag* terkait kualitas laba — entah dari pengakuan pendapatan yang agresif, manipulasi piutang, atau kapitalisasi biaya yang meragukan. Sloan (1996) membuktikan secara empiris bahwa komponen akrual laba memiliki kualitas persistensi yang lebih rendah dibanding komponen kas; artinya, investor yang fokus pada *bottom-line earnings* sistematis akan dikejutkan oleh pembalikan akrual. Mahasiswa S2 MNK202 perlu memahami bahwa FCFF dan FCFE bukan sekadar alat valuasi, melainkan alat diagnostik: selisih signifikan antara FCFF dan laba operasi mengindikasikan *capital intensity* yang tinggi (seperti TLKM dengan rasio Capex/Revenue ~17%) atau manipulasi modal kerja. Pada akhirnya, CFS adalah satu-satunya laporan keuangan yang tidak dapat "dibumbui" tanpa meninggalkan jejak audit pada rekening bank — dan itulah mengapa ia menjadi landasan analisis kualitas laba modern.
