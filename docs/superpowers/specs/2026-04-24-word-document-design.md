# Design Spec: Dokumen Word — Ringkasan Akademik Presentasi Kelompok 3

**Date:** 2026-04-24
**Topic:** FASB Conceptual Framework × Indofood (INDF) 2024 Case Study
**Course:** MNK202 Pelaporan Keuangan Korporat — Program Magister Akuntansi, STIE YKPN Yogyakarta
**Output file:** `01079_Dzaki Muhammad Yusfian_Tugas Kelompok PKK.docx` (or equivalent group filename)

---

## 1. Tujuan dan Konteks

Dokumen Word ini adalah **ringkasan akademik tertulis** dari seluruh isi presentasi 32-slide Kelompok 3. Fungsinya sebagai:
- Dokumen pendamping presentasi oral yang dapat dikumpulkan ke dosen
- Referensi tertulis lengkap dengan sitasi yang substantif
- Demonstrasi penguasaan materi teori FASB CF dan aplikasi empiris di INDF 2024

---

## 2. Pendekatan Dokumen

**Tipe:** Academic Report — Formal & Dense (Opsi A)
- Setiap bagian = narasi substantif + visual inline
- ~40–60 halaman
- Bahasa: Bahasa Indonesia utama; istilah teknis akuntansi dalam Bahasa Inggris ditulis dalam tanda kurung, contoh: *Faithful Representation* (representasi tepat)
- Tidak ada bullet point berdiri sendiri — semua informasi dalam paragraf naratif atau tabel

---

## 3. Tipografi

| Elemen | Font | Ukuran | Style |
|--------|------|--------|-------|
| Judul Dokumen (cover) | Times New Roman | 16pt | Bold |
| Section Heading (I, II, …) | Times New Roman | 14pt | Bold + bottom border |
| Sub-Heading (1.1, 1.2, …) | Times New Roman | 12pt | Bold |
| Body Text | Times New Roman | 12pt | Regular |
| Tabel Header | Times New Roman | 11pt | Bold |
| Caption / Catatan Kaki | Times New Roman | 10pt | Italic |

- **Warna teks:** Hitam (#000000) satu warna untuk semua elemen
- **Spasi baris body:** 1.5
- **Alignment body:** Justify
- **Margin halaman:** 2.5 cm semua sisi (standar A4 akademik)

---

## 4. Halaman Cover

**Desain:** Formal Akademik Klasik (Opsi A)

Layout dari atas ke bawah:
1. Garis batas biru tua (lebar penuh) di bagian atas
2. Header institusi: "PROGRAM MAGISTER AKUNTANSI — STIE YKPN YOGYAKARTA" (centered, 11pt Bold, biru tua)
3. Logo STIE YKPN (centered, ~4 cm tinggi) — dari file `STIE Logo.png`
4. Judul dokumen (centered, 16pt Bold, hitam):
   ```
   KERANGKA KONSEPTUAL FASB:
   FONDASI STANDAR PELAPORAN KEUANGAN
   ```
5. Sub-judul (centered, 12pt Italic, hitam):
   ```
   PT Indofood Sukses Makmur Tbk (INDF) sebagai Studi Kasus
   ```
6. Spasi
7. Nama mata kuliah: "MNK202 Pelaporan Keuangan Korporat" (11pt)
8. "Kelompok 3 | Tahun Akademik 2025/2026" (11pt)
9. Daftar anggota (12pt, centered):
   ```
   1. Efri Nurmalinda                NIM: 1225 01049
   2. Dzaki Muhammad Yusfian         NIM: 1225 01079
   3. Nuradila                       NIM: 1225 01080
   4. Achmad Dimas Wibawa            NIM: 1225 01083
   5. Adinda Putri Dewi              NIM: 1225 01086
   6. Setiabudi Yudha Pratama        NIM: 1225 01098
   ```
10. Garis batas biru tua (lebar penuh) di bagian bawah

---

## 5. Halaman Depan (Front Matter)

### 5.1 Daftar Isi
- Di-generate otomatis dari heading styles dalam python-docx
- Format: Section heading ↔ nomor halaman (right-aligned)

### 5.2 Kata Pengantar
- ~150–200 kata, 1 paragraf singkat
- Menerangkan tujuan dokumen dan konteks tugas kelompok

---

## 6. Struktur Isi Utama (8 Bagian)

### Bagian I — Konteks dan Evolusi Kerangka Konseptual FASB
**Slide acuan:** 3–5 | **Target:** ~4–6 halaman

Sub-bagian:
- I.1 Sejarah Perkembangan: SFAC 1 (1978) sampai SFAC 8 (September 2024)
- I.2 SFAC 1: Tujuan Pelaporan Keuangan — *Primary Users* dan kebutuhan informasi
- I.3 Norwalk Agreement (2002) dan konvergensi FASB–IASB
- I.4 Relevansi bagi Indonesia: Jalur IASB CF 2018 → PSAK

Visuals:
- **Bagan 1.1** — Timeline evolusi (SFAC 1 → SFAC 8, 1978–2024)
- **Tabel 1.1** — 8 SFAC: nomor, tahun, topik, status
- **Tabel 1.2** — SFAC 1 (1978) vs. SFAC 8 Ch.1 (2010): perbandingan tujuan
- **Bagan 1.2** — Primary Users dan zona informasi

---

### Bagian II — Karakteristik Kualitatif Informasi Keuangan
**Slide acuan:** 6–10 | **Target:** ~5–7 halaman

Sub-bagian:
- II.1 SFAC 2 (1980): Hierarki Reliability — Wolk et al. Exhibit 7.1
- II.2 SFAC 8 (2010): Perubahan ke Faithful Representation — Exhibit 7.5
- II.3 Analisis komparatif: mengapa Verifiability diturunkan, mengapa Konservatisme dihapus (BC3.27–29)
- II.4 Relevansi: predictive value, confirmatory value, materiality threshold
- II.5 Enhancing QCs: Comparability, Verifiability, Timeliness, Understandability

Visuals:
- **Bagan 2.1** — Hierarki QC SFAC 2: pohon Reliability
- **Bagan 2.2** — Hierarki QC SFAC 8: Fundamental (Relevance + FR) + Enhancing
- **Tabel 2.1** — Perbandingan SFAC 2 vs SFAC 8 (5 dimensi)
- **Grafik 2.1** — Tren EPS INDF 2020–2024 (bar chart, nilai aktual dari AR)

---

### Bagian III — Elemen-Elemen Laporan Keuangan
**Slide acuan:** 11–13 | **Target:** ~4–5 halaman

Sub-bagian:
- III.1 SFAC 6: 10 elemen laporan keuangan
- III.2 SFAC 8 Ch.4 (July 2024): Definisi aset baru — "present right to an economic benefit"
  - Penghapusan "probable" dan "control" sebagai kriteria
  - BC4.7: primasi konseptual
- III.3 Comprehensive Income (CI): definisi, komponen, hubungan dengan OCI
- III.4 Aplikasi di INDF: Goodwill Rp52.2T sebagai contoh aset intangible

Visuals:
- **Tabel 3.1** — 10 elemen SFAC 6: nama, definisi singkat
- **Tabel 3.2** — Definisi Aset: SFAC 6 vs. SFAC 8 Ch.4 — perbandingan kalimat per kalimat
- **Bagan 3.1** — Waterfall Comprehensive Income INDF 2024

---

### Bagian IV — Pengakuan dan Pengukuran
**Slide acuan:** 14–17 | **Target:** ~5–7 halaman

Sub-bagian:
- IV.1 SFAC 5: "Achilles' heel" — kritik Solomons; empat kriteria pengakuan
- IV.2 SFAC 8 Ch.5 (July 2024): 3 kriteria pengakuan; RD3: "recognition = words + numbers"
  - Disclosure ≠ Recognition
- IV.3 SFAC 8 Ch.6 (July 2024): Dua sistem pengukuran
  - Entry Price: Historical Cost, Replacement Cost, Net Realizable Value (entry)
  - Exit Price: Fair Value, Net Realizable Value (exit), Value in Use
  - M30–34: harga unik → Entry, harga tidak unik → Exit
- IV.4 SFAC 8 Ch.7 (July 2024): Penyajian dan Notes
  - PR12: notes tidak dapat menggantikan recognition
  - BC7.21: tidak ada basis konseptual untuk OCI

Visuals:
- **Tabel 4.1** — Perbandingan 4 kriteria SFAC 5 vs. 3 kriteria SFAC 8 Ch.5
- **Tabel 4.2** — 5 atribut pengukuran SFAC 5 + peta ke SFAC 8 Ch.6
- **Bagan 4.1** — Entry Price vs. Exit Price: pohon keputusan M30–34
- **Bagan 4.2** — Hirarki laporan keuangan (SFAC 8 Ch.7): FS → Notes → MD&A

---

### Bagian V — Catatan Kritis dan Perspektif Akademis
**Slide acuan:** 18 | **Target:** ~3–4 halaman

Sub-bagian:
- V.1 SFAC 5 sebagai "Achilles' heel" — kutipan langsung Solomons (via Wolk et al.)
- V.2 Kritik terhadap Fair Value: pro-cyclicality; relevansi vs. reliabilitas
- V.3 Ketegangan konservatisme: mengapa SFAC 8 menghapusnya (BC3.27–29)
- V.4 Implikasi bagi standar setter: IASB CF 2018 dan PSAK

---

### Bagian VI — Sintesis Teori: SFAC 8 Keseluruhan
**Slide acuan:** 19–20 | **Target:** ~3–4 halaman

Sub-bagian:
- VI.1 Peta 8 Chapters SFAC 8 (September 2024): hubungan antar chapter
- VI.2 Jalur pengaruh: FASB CF → IASB CF 2018 → PSAK → Laporan Keuangan Indonesia

Visuals:
- **Tabel 5.1** — 8 Chapters SFAC 8: nomor, judul, tanggal, isi pokok
- **Bagan 5.1** — Alur FASB → IASB → PSAK → INDF

---

### Bagian VII — Studi Kasus: PT Indofood Sukses Makmur Tbk (INDF) 2024
**Slide acuan:** 21–30 | **Target:** ~12–16 halaman

Sub-bagian:
- VII.1 Profil Perusahaan: struktur konglomerat, First Pacific 50.07%, EY sebagai auditor
- VII.2 Primary Users INDF: identifikasi investor (First Pacific, investor minoritas, NCI Rp43.077T)
- VII.3 Relevansi: Net Sales Rp115.79T; EPS trend 735→873→724→928→984; predictive vs. confirmatory value
- VII.4 Faithful Representation: kompleksitas konsolidasi 4 divisi; NCI disclosure
- VII.5 Aset dan Goodwill: Goodwill Rp52.2T (26% total aset) — impairment test analysis
- VII.6 Liabilitas dan Ekuitas: komposisi liabilitas; NCI vs. CSHE classification
- VII.7 Pengakuan di INDF: 3 kriteria SFAC 8 Ch.5 vs. praktik aktual
- VII.8 Pengukuran di INDF: Entry vs. Exit Price mapping per item LK
- VII.9 Penyajian (Presentation): SFAC 8 Ch.7 di laporan INDF; catatan footnote analysis
- VII.10 Catatan (Notes): SFAC 8 Ch.8 di INDF; 4 limitasi notes; D32 adverse consequences

Visuals:
- **Bagan 6.1** — Org chart konglomerat + angka kunci 2024
- **Bagan 6.2** — Pie chart kepemilikan (First Pacific 50.07%, publik, treasury)
- **Tabel 6.1** — Goodwill impairment test: nilai tercatat vs. recoverable amount
- **Tabel 6.2** — Peta pengukuran INDF: item LK → metode → SFAC 8 Ch.6 referensi
- **Bagan 6.3** — Matrix 2×2: Relevance vs. Faithful Representation per item
- **Tabel 6.3** — Ringkasan disclosure INDF vs. standar SFAC 8 Ch.8 + verdict

---

### Bagian VIII — Kesimpulan
**Slide acuan:** 31 | **Target:** ~2–3 halaman

Sub-bagian:
- VIII.1 Sintesis: CF sebagai fondasi hierarki standar → praktik → LK
- VIII.2 INDF 2024 sebagai cerminan teori: di mana selaras, di mana masih ada gap
- VIII.3 Implikasi untuk standard-setter Indonesia (OJK, DSAK-IAI)

---

## 7. Daftar Pustaka

- Halaman terpisah setelah Kesimpulan
- Format: APA 7th edition
- Sumber: dari file `Daftar Pustaka — Presentasi Kelompok 3.txt` (164 baris, 7 kategori)
- Tidak duplikasi dengan slide (slide tidak memuat Daftar Pustaka)

---

## 8. Visual Summary — 23 Visuals

| No | Kode | Jenis | Bagian | Keterangan |
|----|------|-------|--------|------------|
| 1 | Bagan 1.1 | Timeline / flow | I | Evolusi SFAC 1–8, 1978–2024 |
| 2 | Tabel 1.1 | Table | I | 8 SFAC: nomor, tahun, topik |
| 3 | Tabel 1.2 | Table | I | SFAC 1 vs SFAC 8 Ch.1 |
| 4 | Bagan 1.2 | Zone diagram | I | Primary Users zones |
| 5 | Bagan 2.1 | Tree diagram | II | QC hierarchy SFAC 2 |
| 6 | Bagan 2.2 | Tree diagram | II | QC hierarchy SFAC 8 |
| 7 | Tabel 2.1 | Table | II | SFAC 2 vs SFAC 8 QC comparison |
| 8 | Grafik 2.1 | Bar chart | II | EPS INDF 2020–2024 |
| 9 | Tabel 3.1 | Table | III | 10 elemen SFAC 6 |
| 10 | Tabel 3.2 | Table | III | Definisi aset SFAC 6 vs Ch.4 |
| 11 | Bagan 3.1 | Waterfall | III | Comprehensive Income INDF 2024 |
| 12 | Tabel 4.1 | Table | IV | Kriteria pengakuan SFAC 5 vs Ch.5 |
| 13 | Tabel 4.2 | Table | IV | 5 atribut pengukuran SFAC 5 + SFAC 8 |
| 14 | Bagan 4.1 | Decision tree | IV | Entry vs Exit M30–34 |
| 15 | Bagan 4.2 | Hierarchy | IV | FS hierarchy SFAC 8 Ch.7 |
| 16 | Tabel 5.1 | Table | VI | 8 Chapters SFAC 8 summary |
| 17 | Bagan 5.1 | Flow | VI | FASB→IASB→PSAK→INDF |
| 18 | Bagan 6.1 | Org chart | VII | Konglomerat INDF + key figures |
| 19 | Bagan 6.2 | Pie chart | VII | Kepemilikan INDF |
| 20 | Tabel 6.1 | Table | VII | Goodwill impairment test |
| 21 | Tabel 6.2 | Table | VII | Measurement map INDF |
| 22 | Bagan 6.3 | 2×2 matrix | VII | Relevance × Faithful Representation |
| 23 | Tabel 6.3 | Table | VII | Disclosure verdict INDF |

---

## 9. Implementasi Teknis

**Tool:** `python-docx` (Python library)
**Script output:** Single `.docx` file, A4 page size
**Logo handling:** Load `STIE Logo.png` from working directory via `docx.shared.Inches`

### python-docx implementation notes:
- All text uses `Times New Roman` font explicitly set per run
- Section Headings: `style='Heading 1'` custom styled; bottom border added via `paragraph.paragraph_format`
- Tables: `Table` objects with `WORD_CONTENT_COLOR` set per header row; zebra striping via row index
- Charts: matplotlib-generated PNG images (embedded as `InlineImage`); NOT Word native charts
- Flow/tree diagrams: matplotlib or PIL-generated PNG images
- Page numbers: footer with `add_footer` → `add_paragraph` → field code XML injection

### Script location:
`scripts/generate_word_doc.py`

### Dependencies:
```
python-docx>=1.1.0
matplotlib>=3.8.0
Pillow>=10.0.0
```

---

## 10. Constraints dan Batasan

1. **No fabricated data** — semua angka INDF harus dari `sources/indf-2024-ar.pdf`
2. **No bullet-only sections** — setiap bagian harus ada narasi paragraf
3. **English terms in parentheses** — bukan substitusi, bukan terjemahan paksa
4. **Logo file must exist** — jika `STIE Logo.png` tidak ditemukan, cover dibuat tanpa logo (with warning)
5. **Daftar Pustaka from .txt file** — jangan generate dari ingatan
6. **Font consistency** — semua teks Times New Roman; tidak boleh ada fallback ke Calibri atau Arial

---

## 11. Kriteria Sukses

- [ ] Cover: STIE logo terpasang, 6 anggota lengkap, borders atas-bawah
- [ ] Daftar Isi: semua 8 section + sub-section tercantum dengan nomor halaman
- [ ] Semua 23 visual terpasang di posisi yang benar
- [ ] Tidak ada data INDF yang tidak bersumber dari AR 2024
- [ ] Font konsisten Times New Roman di seluruh dokumen
- [ ] Dokumen dapat dibuka di Microsoft Word 2016+
- [ ] ~40–60 halaman setelah final render
