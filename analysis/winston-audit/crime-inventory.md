# Winston Slide Crime Inventory — Deck v5 (1)

**Source file:** `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html`
**Audit date:** 2026-04-27
**Framework reference:** `.claude/winston-framework.md` F2 (10 Slide Crimes)
**Rules reference:** `specs/winston-integration-rules.md` E2 (design vs delivery), E3 (INDF case), E4 (HIGH-XL)
**Scope:** Hanya design crimes (#1, #2, #3, #7, #8, #9, #10) per E2.
Delivery crimes #4 (reading), #5 (laser), #6 (distance) di `delivery-checklist.md`.

---

## Executive Summary

**Total slides audited:** 32
**Total crime occurrences:** 98

### Severity Breakdown

| Severity | Count |
|----------|-------|
| HIGH | 55 |
| MED | 40 |
| LOW | 3 |
| **Total** | **98** |

### Effort Breakdown

| Effort | Count |
|--------|-------|
| S | 0 |
| M | 27 |
| L | 39 |
| XL | 32 |
| **Total** | **98** |

### Per-Crime Frequency

| Crime | Total Occurrences |
|-------|-------------------|
| #1 Too many slides | 3 |
| #2 Too many words | 31 |
| #3 Font <40pt | 32 |
| #7 No white space | 30 |
| #8 Background clutter / logos | 0 |
| #9 Collaborators list as final slide | 1 |
| #10 "Thank you" / "Questions?" final | 1 |
| **Total** | **98** |

> Catatan: Aggregate dihitung ulang via grep pada baris tabel; konsisten dengan jumlah aktual 98 entries. Crime #8 adalah 0 — logo hanya di slide 01 (cover), tepat sesuai standar. Grid background (`.grid-bg`) di multiple slides bersifat dekoratif dengan opasitas sangat rendah (4–5%) dan tidak termasuk "background clutter" per definisi operasional F2.

### HIGH-XL Flag (per E4)

**HIGH-XL entries (must redesign in Phase 4, not patch v6):** 32

Semua 32 slide masing-masing memiliki Crime #3 (font <40pt) dengan severity HIGH dan effort XL. Ini adalah **defect sistemik** bukan defect lokal — keseluruhan design system menggunakan tipografi body/lead/label di bawah ambang batas Winston 40pt. Global CSS (baris 28–38) menetapkan:
- `.t-h4` = 34px (sub-40pt) — dipakai sebagai heading sekunder
- `.t-h5` = 26px (sub-40pt) — dipakai sebagai heading tersier
- `.t-lead` = 26px — dipakai sebagai subtitle/lead text di SETIAP slide
- `.t-body` = 22px — dipakai sebagai body text di SETIAP slide
- `.t-body-sm` = 18px — dipakai sebagai caption/detail di SETIAP slide
- `.t-label` = 13px — dipakai sebagai label/uppercase tag di SETIAP slide
- `.t-meta` = 16px — dipakai sebagai metadata di SETIAP slide

573 dari 587 deklarasi `font-size` dalam file menggunakan ukuran sub-40px. Ini bukan masalah yang dapat di-patch di v6; harus menjadi requirement Phase 4 build dari nol dengan typography system baru.

**Ringkasan HIGH-XL per slide:** 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32

---

## Per-Slide Inventory

| Slide # | Crime # | Bukti (Quote / Lokasi) | Severity | Effort | Fix Diusulkan |
|---------|---------|------------------------|----------|--------|----------------|
| 01 | #3 | CSS global line 32: `.t-h5{font-size:26px}`, line 33: `.t-lead{font-size:26px}`, line 34: `.t-body{font-size:22px}`, line 37: `.t-label{font-size:13px}`, line 38: `.t-meta{font-size:16px}` — slide 01 menggunakan `.t-meta`, `.t-label` (lines 119–141) untuk semua nama anggota, detail institusi | HIGH | XL | Redesign global typography system: tetapkan minimum body text 40pt; gunakan 40–48pt untuk semua teks yang dapat dibaca audiens; per E4: angkat ke Phase 4 redesign requirement |
| 01 | #2 | Footer slide 01 (lines 132–143): nama 6 anggota lengkap + NIM + judul institusi + tahun akademik = estimasi 45+ kata di area bawah slide, di luar konten utama | MED | M | Pindahkan anggota ke slide dedikasi atau hapus NIM — cover cukup nama tanpa NIM dan detail institusi |
| 02 | #3 | Sama dengan #3 global: `.t-body` 22px, `.t-meta` 16px, `.t-label` 13px — digunakan di header tabel agenda (lines 157–160) dengan `font-size:13px` eksplisit | HIGH | XL | Per E4: Phase 4 redesign |
| 02 | #2 | Tabel agenda 8 baris (lines 163–170): setiap baris berisi nama bagian + slide range + durasi; body agenda melebihi 25 kata termasuk keterangan "~43 menit" dan 8 bagian bernama | MED | M | Sederhanakan ke 5–6 bagian maksimum; hapus kolom Durasi jika slide terlalu padat |
| 02 | #7 | Tabel 8 baris penuh + header "≥43 menit" + judul "Agenda Presentasi" mengisi >75% frame; sangat sedikit ruang putih di sisi kiri/kanan dan antarbaris | MED | M | Rancang ulang agenda sebagai grid visual 2×4 dengan ikon; kurangi ke 6 item maksimum |
| 03 | #3 | Line 214–218: `.t-h5` 26px untuk bullet "Era Pra-CF"; teks detail di card "Pra-CF" dan "Pendahulu Intelektual" menggunakan inline `font-size:20px`; tabel SFAC menggunakan `.tbl compact` dengan `font-size:16px` (line 91) dan `font-size:12px` untuk th | HIGH | XL | Per E4: Phase 4 redesign |
| 03 | #2 | Card "Era Pra-CF" (line 214): "CAP (1939–59) — ARBs ad hoc, tanpa fondasi teoritis / APB (1959–73) — Opinions; tekanan industri kuat; ARS 1 & 3 (1962) ditolak / Masalah fundamental: ..." = estimasi 40+ kata dalam satu card saja; total slide >100 kata | HIGH | L | Pisahkan timeline + tabel SFAC ke slide terpisah; pertahankan hanya timeline visual di slide ini |
| 03 | #7 | SVG timeline 1760px lebar + dua panel besar bawah (grid 1fr 1fr) + tabel 8 baris = kepadatan sangat tinggi; tidak ada white space antara elemen | MED | L | Pisahkan ke 2 slide: (a) timeline, (b) tabel SFAC |
| 04 | #3 | Lines 252–263: semua teks card "Primary Users" menggunakan `font-size:19px`; tabel evolusi SFAC 1 vs 8 menggunakan `.tbl compact` (`font-size:16px` td); sub-header "EVOLUSI SFAC 1 vs SFAC 8" menggunakan `.t-meta` (16px) | HIGH | XL | Per E4: Phase 4 redesign |
| 04 | #2 | Card kiri (lines 251–263): kutipan panjang OB2 + 5 item pengguna utama; card kanan: tabel 5-baris + teks OB17; estimasi total >80 kata visible | HIGH | L | Pisahkan ke 2 slide: (a) tujuan + OB2, (b) pengguna utama + evolusi |
| 04 | #7 | Dua kolom masing-masing berisi 2 card + tabel penuh = >80% area frame; tidak ada breathing room vertikal maupun horizontal yang signifikan | MED | L | Pisahkan konten; tambah margin antara elemen |
| 05 | #3 | Lines 298–327: semua teks card menggunakan `font-size:19px`; chart organisasi menggunakan `font-size:21px` untuk nama anak perusahaan dan `font-size:19px` untuk deskripsi; stats bawah menggunakan `font-size:19px` dan `font-size:20px` — semuanya sub-40px | HIGH | XL | Per E4: Phase 4 redesign |
| 05 | #2 | Kolom kiri: definisi RE1 + 3 jenis entitas + paragraf konsolidasi; kolom kanan: org chart + 4 subsidiary cards + 3 stat blocks = estimasi >90 kata visible | HIGH | L | Pisahkan definisi entitas pelapor (slide 05a) dari org chart INDF (slide 05b) |
| 05 | #7 | Dua kolom masing-masing sangat padat: kolom kiri 3 card bertumpuk, kolom kanan org chart + 4 cards + 3 stats mengisi hampir seluruh frame | MED | L | Pisahkan ke 2 slide dengan konten lebih sedikit per slide |
| 06 | #3 | Lines 344–368: hierarki QC SFAC 2 menggunakan boxes dengan `font-size:20px` dan `font-size:21px` untuk label, dan `font-size:12px` untuk subtext; bottom text (line 370) menggunakan `.t-body-sm` = 18px | HIGH | XL | Per E4: Phase 4 redesign |
| 06 | #2 | Diagram hierarki + 6 box komponen + catatan bawah line 370: "Tanpa memahami SFAC 2 — perubahan di SFAC 8 tidak akan terasa signifikan. Verifiability di sini adalah komponen FUNDAMENTAL Keandalan..." = >20 kata dalam catatan saja; total visible >50 kata | MED | M | Hapus catatan bawah; letakkan di speaker notes. Sederhanakan diagram ke nama saja tanpa deskripsi |
| 06 | #7 | Diagram hierarki vertikal + 2 kolom besar + 6 komponen boxes + catatan bawah = seluruh frame penuh; tidak ada white space | MED | L | Sederhanakan diagram; hapus sub-label di setiap box |
| 07 | #3 | Lines 386–403: teks dalam boxes menggunakan `font-size:19px`, `font-size:12px` (subtext QC numbers), `font-size:16px` (komponen boxes bawah), `font-size:20px` (enhancing QC line) | HIGH | XL | Per E4: Phase 4 redesign |
| 07 | #2 | Kolom kiri: diagram hierarki + 6 komponen boxes + enhancing QC label; kolom kanan: 5 "Transformasi Kunci" cards masing-masing berisi heading + 1 kalimat penjelasan = estimasi >100 kata visible | HIGH | L | Pisahkan diagram SFAC 8 hierarchy (slide 07a) dari tabel 5 transformasi (slide 07b) |
| 07 | #7 | Dua kolom dengan kepadatan sangat tinggi: kolom kiri diagram + 6 boxes, kolom kanan 5 cards bertumpuk; frame hampir penuh seluruhnya | HIGH | L | Pisahkan ke 2 slide |
| 08 | #3 | Lines 430–481: tiga card QC + bar chart EPS menggunakan `font-size:21px` untuk body card, `font-size:20px` untuk bar labels, `font-size:19px` untuk teks INDF application | HIGH | XL | Per E4: Phase 4 redesign |
| 08 | #2 | Tiga card QC masing-masing berisi heading + deskripsi + box aplikasi INDF + bar chart EPS 5-tahun dengan label per bar = estimasi >80 kata visible | MED | L | Pisahkan chart EPS ke slide terpisah; pertahankan 3 card QC saja |
| 08 | #7 | Tiga card penuh baris atas + bar chart penuh lebar bawah = >85% frame terisi | MED | M | Pisahkan chart EPS; tambah whitespace antara cards |
| 09 | #3 | Lines 496–531: perbandingan SFAC 2 vs SFAC 8 menggunakan `font-size:21px` untuk heading sub, `font-size:21px` untuk komponen boxes, `font-size:20px` untuk catatan konservatisme; arrow SVG di tengah membuat dua kolom sangat padat | HIGH | XL | Per E4: Phase 4 redesign |
| 09 | #2 | Dua kolom SFAC 2 vs SFAC 8 masing-masing berisi: heading + definisi + 3 komponen boxes berlabel + catatan; ditambah bar merah BC3.27 di bawah = estimasi >80 kata visible | MED | L | Pisahkan ke: (a) SFAC 2 Reliability, (b) SFAC 8 Faithful Representation + Conservatism removal |
| 09 | #7 | Dua panel besar + panel merah bawah = hampir seluruh frame penuh; arrow di tengah mengambil ruang tanpa memberikan breathing room | MED | M | Tambah padding; pindahkan BC3.27 ke catatan presenter |
| 10 | #3 | Lines 544–576: empat cards QC peningkat menggunakan `font-size:15px` untuk body text (sangat kecil), `font-size:14px` untuk INDF aplikasi box, `font-size:13px` untuk pill labels; Cost Constraint box menggunakan `font-size:15px` dan `font-size:13px` | HIGH | XL | Per E4: Phase 4 redesign |
| 10 | #2 | Empat card QC (komparabilitas, verifiabilitas, ketepatwaktuan, keterpahaman) masing-masing berisi body text ~25–30 kata + INDF aplikasi + catatan, ditambah Cost Constraint panel bawah = estimasi >100 kata visible | HIGH | L | Pisahkan 4 QC peningkat ke 2 slide (2 QC per slide); pindahkan Cost Constraint ke slide 07 atau sendiri |
| 10 | #7 | Grid 2×2 card penuh + Cost Constraint bar bawah = kepadatan sangat tinggi; font 15px di body card menandai upaya memaksakan terlalu banyak teks | HIGH | L | Redesign ke 2 slide; gunakan lebih sedikit kata per card |
| 11 | #3 | Lines 588–617: tabel 10 elemen menggunakan `.tbl` dengan `font-size:18px` untuk td (line 87: `.tbl td{font-size:18px}`) dan `font-size:14px` untuk th | HIGH | XL | Per E4: Phase 4 redesign |
| 11 | #2 | Tabel 10 elemen (seluruh slide) + heading "Sepuluh Elemen Laporan Keuangan" + lead text = tabel 10 baris × 5 kolom = estimasi >50 kata visible; tabel sangat dense | MED | M | Sederhanakan ke 4–5 elemen kunci; gunakan visual card bukan tabel penuh |
| 11 | #7 | Tabel penuh seluruh slide hampir tanpa whitespace; hanya judul dan tabel | MED | M | Hilangkan 5 elemen minor; tambah whitespace di sekitar tabel |
| 12 | #3 | Lines 628–666: dua tabel perbandingan menggunakan `.tbl compact` (font 16px td, 12px th); box aplikasi INDF goodwill menggunakan `font-size:14px` (line 634, 666) | HIGH | XL | Per E4: Phase 4 redesign |
| 12 | #2 | Dua tabel perbandingan SFAC 6 vs SFAC 8 Ch.4 (masing-masing 5–6 baris) + 2 box definisi liabilitas + tabel goodwill test 3-baris + catatan bawah = estimasi >80 kata visible | HIGH | L | Pisahkan: (a) definisi baru aset, (b) definisi baru liabilitas + INDF goodwill test |
| 12 | #7 | Tiga card/tabel bertumpuk dalam grid 1fr 1fr + tabel bawah penuh lebar = frame hampir 90% terisi | HIGH | L | Pisahkan ke 2 slide |
| 13 | #3 | Lines 682–720: card "Pendapatan vs Keuntungan" menggunakan `font-size:21px` dan `font-size:19px` untuk subcards; CI waterfall menggunakan berbagai ukuran sub-40px | HIGH | XL | Per E4: Phase 4 redesign |
| 13 | #2 | Dua card grid kiri (Revenue vs Gains, Expenses vs Losses) masing-masing berisi 2 sub-card dengan definisi + contoh INDF; ditambah CI waterfall di kanan = estimasi >70 kata visible | MED | L | Pisahkan Revenue/Gains/OCI ke slide terpisah; atau fokus hanya pada CI waterfall |
| 13 | #7 | Empat card dalam dua baris kiri + panel CI kanan = kepadatan tinggi; sub-card dalam card utama menambah kompleksitas visual | MED | M | Sederhanakan ke 2 konsep per slide |
| 14 | #3 | Lines 731–769: card SFAC 5 dan SFAC 8 Ch.5 menggunakan `font-size:21px` untuk body text per item, `font-size:20px` untuk deskripsi, `font-size:17px` untuk catatan RD3; tabel Recognition vs Disclosure menggunakan `.tbl compact` 16px/12px | HIGH | XL | Per E4: Phase 4 redesign |
| 14 | #2 | Dua card besar (SFAC 5 empat kriteria, SFAC 8 Ch.5 tiga kriteria) masing-masing berisi deskripsi + 3–4 item; ditambah tabel Recognition vs Disclosure 3-baris = estimasi >80 kata visible | HIGH | L | Pisahkan SFAC 5 vs SFAC 8 Ch.5 comparison (slide 14a) dari Recognition vs Disclosure (slide 14b) |
| 14 | #7 | Dua card besar baris atas + tabel penuh lebar bawah = >85% frame terisi | MED | M | Pisahkan ke 2 slide |
| 15 | #3 | Lines 782–800: tabel "Lima Dasar Pengukuran" menggunakan `.tbl compact` (16px td, 12px th); empat critique boxes menggunakan `font-size:21px` heading dan `font-size:20px` body | HIGH | XL | Per E4: Phase 4 redesign |
| 15 | #2 | Tabel 5 atribut (5 baris × 5 kolom) + empat critique boxes (Solomons, Sterling, SFAC 5 par. 2, Miller) masing-masing berisi kutipan dan penjelasan = estimasi >100 kata visible | HIGH | L | Pisahkan: (a) tabel lima atribut (slide 15a), (b) perspektif kritis (slide 15b) |
| 15 | #7 | Tabel penuh lebar atas + empat card bawah dalam grid 4 kolom = frame hampir penuh; teks di critique cards sangat kecil | HIGH | L | Pisahkan ke 2 slide |
| 16 | #3 | Lines 814–840: dua card Entry/Exit menggunakan `font-size:14px` untuk isi, `font-size:13px` untuk label M30–M34; tabel INDF application menggunakan `.tbl compact` (16px/12px); overall body text 14px sangat sub-40pt | HIGH | XL | Per E4: Phase 4 redesign |
| 16 | #2 | Dua panel Entry vs Exit + tabel 5-baris aplikasi INDF = estimasi >60 kata visible; tabel memiliki 4 kolom dengan teks penuh per cell | MED | L | Pisahkan: (a) Entry vs Exit concept, (b) tabel aplikasi INDF |
| 16 | #7 | Panel konsep (grid 1fr 80px 1fr) + tabel penuh lebar = >80% frame terisi | MED | M | Pisahkan ke 2 slide; sederhanakan tabel ke 3 baris kunci |
| 17 | #3 | Lines 857–884: teks hierarki laporan keuangan menggunakan `font-size:21px`, `font-size:20px`, `font-size:19px`; OCI waterfall menggunakan `font-size:20px` dan `font-size:19px`; box BC7.21 menggunakan `font-size:21px` | HIGH | XL | Per E4: Phase 4 redesign |
| 17 | #2 | Kolom kiri: hierarki FS (2 level) + box PR12 + OCI rekonsiliasi; kolom kanan: box BC7.21 + implikasi INDF = estimasi >80 kata visible | MED | L | Pisahkan BC7.21 ke slide terpisah; pertahankan hierarki FS dan OCI di slide 17 |
| 17 | #7 | Dua kolom masing-masing sangat padat; kolom kiri 3 card bertumpuk dengan OCI waterfall | MED | M | Pisahkan ke 2 slide |
| 18 | #3 | Lines 901–929: empat keterbatasan boxes menggunakan `font-size:22px` untuk nomor dan `font-size:20px` untuk body; tiga perspektif kritis menggunakan `font-size:19px` body dan `font-size:20px` heading; catatan kelemahan menggunakan `font-size:16px` | HIGH | XL | Per E4: Phase 4 redesign |
| 18 | #2 | Empat limitation boxes + tiga perspektif kritis (Gaa, Archer, Wolk) masing-masing berisi judul + body ~30 kata = estimasi >100 kata visible | HIGH | L | Pisahkan: (a) empat keterbatasan catatan, (b) tiga perspektif kritis |
| 18 | #7 | Grid 4 kolom (limitations) + grid 3 kolom (perspectives) = frame hampir penuh; tidak ada breathing room | HIGH | L | Pisahkan ke 2 slide |
| 19 | #3 | Lines 942–964: delapan chapter cards menggunakan `font-size:20px` heading dan `font-size:19px` body; timeline bar bawah menggunakan `font-size:20px` untuk milestone labels | HIGH | XL | Per E4: Phase 4 redesign |
| 19 | #2 | Grid 4×2 cards (8 chapter cards masing-masing dengan judul + 2–3 kalimat deskripsi) + timeline narasi bawah = estimasi >120 kata visible | HIGH | L | Pisahkan ke 2 slide: (a) Ch.1–4, (b) Ch.5–8 + timeline |
| 19 | #7 | Grid 4 kolom × 2 baris (8 cards) + timeline bar bawah = frame hampir penuh | HIGH | L | Pisahkan ke 2 slide |
| 20 | #3 | Lines 980–1023: teks rantai otoritas menggunakan `font-size:21px`, `font-size:20px`; tabel perbedaan menggunakan `.tbl compact` (16px/12px); convergence bullets menggunakan `font-size:20px` | HIGH | XL | Per E4: Phase 4 redesign |
| 20 | #2 | Diagram rantai FASB→IASB→PSAK→INDF + empat convergence bullets + tabel 3-baris perbedaan = estimasi >60 kata visible | MED | M | Diagram rantai sudah cukup visual; hapus tabel perbedaan atau pindahkan ke catatan |
| 20 | #7 | Diagram flowchart kiri + dua card kanan (hijau + tabel) = frame penuh; diagram flowchart itu sendiri sudah padat dengan teks | MED | M | Sederhanakan diagram; hapus tabel dalam kolom kanan |
| 21 | #3 | Lines 1043–1154: stat block menggunakan `font-size:34px` (masih sub-40pt); deskripsi subsidiary menggunakan `font-size:15px`; ownership detail menggunakan `font-size:22px` dan `font-size:18px`; badge audit menggunakan `font-size:18px` | HIGH | XL | Per E4: Phase 4 redesign |
| 21 | #2 | Profil INDF: org chart 4 subsidiary + 8 stat blocks (penjualan, aset, goodwill, EPS, laba bersih, ekuitas, ROE, interest coverage) + ownership donut chart + keterangan audit = estimasi >80 kata visible | HIGH | L | Pisahkan profil perusahaan (subsidiaries + overview) dari financial highlights (stats + ownership) |
| 21 | #7 | Layout dua kolom: kiri org chart + 4 subsidiary cards; kanan stats (4+4 grid) + ownership chart + audit badge = hampir seluruh frame penuh | MED | L | Pisahkan ke 2 slide |
| 22 | #3 | Lines 1171–1252: zona diagram menggunakan `font-size:18px`, `font-size:16px`, `font-size:15px`, `font-size:13px` untuk label; tabel kebutuhan vs tersedia menggunakan `.tbl` (`font-size:18px` td); box OB2 menggunakan `font-size:22px` | HIGH | XL | Per E4: Phase 4 redesign |
| 22 | #2 | Diagram dua zona (non-primary vs primary users) + tabel 3-baris kebutuhan + box prinsip OB2 dengan kutipan = estimasi >60 kata visible | MED | M | Sederhanakan diagram; pindahkan tabel kebutuhan ke catatan; pertahankan diagram zona + prinsip OB2 |
| 22 | #7 | Dua kolom masing-masing penuh: zona diagram bertingkat (dashed outer, solid inner) mengisi >60% tinggi slide; tabel kanan juga padat | MED | M | Sederhanakan ke diagram zona saja; hapus tabel |
| 23 | #3 | Lines 1268–1378: tiga kolom card menggunakan `font-size:18px` body dan `font-size:13px` untuk label; EPS bar chart menggunakan `font-size:13px` untuk tahun labels dan `font-size:13px` nilai | HIGH | XL | Per E4: Phase 4 redesign |
| 23 | #2 | Tiga kolom: Predictive Value (chart EPS + teks) + Confirmatory Value (margin data + analisis) + Materiality (goodwill proporsi + bar chart) = estimasi >80 kata visible | MED | L | Pisahkan menjadi (a) Predictive + Confirmatory, (b) Materiality + síntesis |
| 23 | #7 | Tiga kolom masing-masing penuh tinggi dengan teks + chart = frame hampir penuh | MED | L | Kurangi ke 2 kolom; pindahkan chart ke slide companion |
| 24 | #3 | Lines 1391–1482: tiga card Kelengkapan/Netralitas/Free from Error menggunakan `font-size:21px` untuk body bullets; limitation bar bawah menggunakan `font-size:21px` dan `font-size:19px` | HIGH | XL | Per E4: Phase 4 redesign |
| 24 | #2 | Tiga card masing-masing berisi 3 bullet points dengan teks 15–20 kata per bullet + limitation bar bawah = estimasi >80 kata visible | MED | L | Sederhanakan ke 1–2 bullet per card; pindahkan detail ke catatan presenter |
| 24 | #7 | Tiga card setinggi frame utama + limitation bar bawah = >85% frame terisi | MED | M | Kurangi bullet per card; tambah breathing room |
| 25 | #3 | Lines 1500–1582: dua tabel uji SFAC menggunakan `.tbl` (18px td) dan `card-head` labels; proportion card menggunakan `font-size:58px` (stat-num amber — ini melewati threshold tetapi untuk satu angka saja, teks lainnya sub-40pt); challenge cards menggunakan `font-size:17px` | HIGH | XL | Per E4: Phase 4 redesign |
| 25 | #2 | Dua tabel uji definisi (masing-masing 3 baris × 3 kolom) + proportion card + challenge list = estimasi >60 kata visible | MED | M | Gabungkan kedua tabel ke 1 tabel komparatif; sederhanakan challenge ke 2 poin |
| 25 | #7 | Grid 1fr 1fr 340px: dua tabel penuh + kolom kanan 2 card bertumpuk = >80% frame terisi | MED | M | Sederhanakan tabel; tambah whitespace |
| 26 | #3 | Lines 1600–1679: dua panel liabilitas + ekuitas menggunakan `font-size:20px` untuk body text, `font-size:21px` italic untuk kutipan definisi; tabel komponen liabilitas menggunakan font sub-40pt | HIGH | XL | Per E4: Phase 4 redesign |
| 26 | #2 | Panel liabilitas: definisi + tabel komponen Rp70,81T + obligasi USD; panel ekuitas: definisi + NCI Rp43,077T + retained earnings = estimasi >70 kata visible | MED | M | Sederhanakan ke angka kunci + 1 kalimat interpretasi per panel |
| 26 | #7 | Dua panel besar masing-masing berisi definisi + tabel + stats = >80% frame | MED | M | Sederhanakan; hapus tabel detail, pertahankan stats utama |
| 27 | #3 | Lines 1694–1769: tiga case cards menggunakan `font-size:24px` heading, `font-size:17px` untuk isi tabel dan bullet; RD3 banner menggunakan `font-size:19px` | HIGH | XL | Per E4: Phase 4 redesign |
| 27 | #2 | RD3 banner (line 1694–1697) + tiga case card masing-masing berisi tabel 3-baris + keterangan bawah = estimasi >80 kata visible | MED | L | Sederhanakan setiap case card ke 1 klaim utama + angka kunci; pertahankan RD3 banner |
| 27 | #7 | RD3 banner + grid 3 kolom case card setinggi frame = >85% frame terisi | MED | M | Kurangi isi per card; tambah spacing |
| 28 | #3 | Lines 1787–1874: tabel "Peta Pengukuran" menggunakan `.tbl` dengan `font-size:12px` th dan `font-size:14px` td (sangat sub-40pt); matriks 2×2 menggunakan `font-size:14px` dan `font-size:18px`; limitation box menggunakan `font-size:17px` | HIGH | XL | Per E4: Phase 4 redesign |
| 28 | #2 | Tabel 6 baris × 4 kolom (Peta Pengukuran) + matriks 2×2 Relevansi vs Verifikasi + box keterbatasan goodwill = estimasi >80 kata visible | HIGH | L | Pisahkan tabel (slide 28a) dari matriks 2×2 (slide 28b); hapus box keterbatasan atau pindahkan ke catatan |
| 28 | #7 | Kolom kiri tabel besar 6 baris + kolom kanan matriks 2×2 + box bawah = frame hampir penuh | HIGH | L | Pisahkan ke 2 slide |
| 29 | #3 | Lines 1891–1976: tiga kolom penyajian menggunakan `font-size:20px` dan berbagai ukuran sub-40pt; OCI waterfall menggunakan `font-size:20px`; tabel efek kurs menggunakan `.tbl compact` (16px/12px) | HIGH | XL | Per E4: Phase 4 redesign |
| 29 | #2 | Tiga kolom: hierarki FS (face vs notes) + OCI waterfall 5 item + efek kurs tabel 3-baris = estimasi >70 kata visible | MED | L | Fokus slide ini pada satu topik: OCI saja atau Face of FS saja |
| 29 | #7 | Grid 340px + 1fr + 1fr dengan masing-masing penuh = frame hampir penuh | MED | M | Sederhanakan ke satu fokus konten |
| 30 | #3 | Lines 1993–2083: list catatan INDF menggunakan `font-size:20px`; tabel segmen menggunakan `.tbl` (18px td); transaksi pihak berelasi menggunakan `font-size:19px`; Enhancing QC card menggunakan `font-size:19px` | HIGH | XL | Per E4: Phase 4 redesign |
| 30 | #2 | Tiga kolom: struktur catatan 5 item + tabel segmen 3-baris + transaksi pihak berelasi (stat + 3 breakdown) + Enhancing QC card = estimasi >80 kata visible | HIGH | L | Pisahkan: (a) struktur catatan + segmen, (b) related party + Enhancing QC |
| 30 | #7 | Grid 3 kolom masing-masing berisi 2 card = frame >85% terisi | MED | L | Pisahkan ke 2 slide |
| 31 | #3 | Lines 2102–2155: lima insight cards menggunakan `font-size:19px` untuk heading dan body; "Kesimpulan Overarching" menggunakan `font-size:20px` | HIGH | XL | Per E4: Phase 4 redesign |
| 31 | #2 | Grid 2 kolom: 5 insight cards masing-masing berisi heading + teks ~25–30 kata + 1 box overarching conclusion = estimasi >120 kata visible | HIGH | L | Sederhanakan ke 3 insight utama; pindahkan detail ke catatan; kesimpulan = 1 kalimat |
| 31 | #7 | Grid 2 kolom × 3 rows (5 card + 1 conclusion) = frame hampir penuh | MED | L | Kurangi ke 3 insight; tambah breathing room |
| 31 | #1 | Slide 31 berjudul "Sintesis — Lima Insight Utama" meringkas slide 08–30 dengan 5 poin, namun slide 19 ("Diagram Master SFAC 8") dan slide 20 ("PSAK vs FASB CF") sudah merupakan sintesis teori. Tiga slide sintesis (19, 20, 31) berpotensi redundan satu sama lain dalam fungsi merangkum | LOW | M | Evaluasi apakah slide 31 dapat digabung dengan elemen slide 19 atau 20; jika dipertahankan, pastikan tidak tumpang tindih dengan sintesis di slide 19 |
| 32 | #3 | Lines 2172–2213: judul "Terima Kasih" menggunakan `font-size:72px` (memenuhi), "THANK YOU" `font-size:28px`, nama anggota `font-size:18px`, NIM `font-size:16px`, Sesi Tanya Jawab `font-size:20px` — teks selain h1 utama semuanya sub-40pt | HIGH | XL | Per E4: Phase 4 redesign |
| 32 | #9 | Lines 2183–2207: daftar 6 anggota kelompok (Efri Nurmalinda, Dzaki M. Yusfian, Nuradila, Achmad Dimas W., Adinda Putri Dewi, Setiabudi Y. Pratama) lengkap dengan NIM masing-masing disajikan sebagai konten utama slide terakhir | HIGH | M | Ganti dengan Contributions Slide: daftar 3–5 kontribusi spesifik kelompok. Anggota dapat disebut dalam 1 baris kecil di chrome/footer |
| 32 | #10 | Line 2176: `<div style="font-size:72px;font-weight:800;color:#fff;...">Terima Kasih</div>` dan line 2177: `<div style="font-size:28px;...">THANK YOU</div>` — slide terakhir secara eksplisit berisi "Terima Kasih" sebagai elemen visual dominan | HIGH | M | Ganti judul slide dengan "Kontribusi Kelompok 3" atau "Temuan Utama"; pertahankan Q&A call-to-action sebagai sub-elemen kecil |
| 02 | #1 | Agenda 8 baris mencakup 8 bagian termasuk "Sintesis Teori" (slides 19–20) dan "Penutup & Kesimpulan" (31–32) sebagai bagian terpisah. Dengan 32 slide untuk presentasi ~43 menit, jumlah bagian dan slide yang ada berpotensi melebihi ambang batas optimal | LOW | L | Pertimbangkan menggabungkan "Sintesis Teori" dengan "Penutup"; hilangkan satu segmen untuk memperpadat alur |
| 19 | #1 | Slide 19 "Diagram Master SFAC 8" merangkum semua 8 chapter SFAC 8 dalam satu slide; slide ini redundan sebagian dengan slide 03 (sejarah SFAC) yang sudah memuat tabel kronologis SFAC 1–8. Sisanya adalah elaborasi yang sudah ada di slide 04–18 | LOW | M | Pertahankan jika berfungsi sebagai synthesis visual; hapus jika dianggap redundan dengan tabel slide 03. Klarifikasi tujuan berbeda: slide 03 = kronologi, slide 19 = arsitektur |

---

## Catatan Audit

### Identifikasi Slide Boundaries

Slide diidentifikasi menggunakan dua marker yang konsisten:
1. **Komentar HTML:** `<!-- ════ NN JUDUL ════ -->` (slides 01–20, lines 112–970)
2. **Atribut HTML:** `data-screen-label="NN Judul"` pada setiap elemen `<section>` (semua 32 slide)

Slide 20–32 tidak memiliki komentar `════` terpisah tetapi tetap teridentifikasi jelas via `data-screen-label`. Tidak ada ambiguitas dalam batas slide.

### Jumlah Slide Aktual vs Spesifikasi

Jumlah slide aktual = **32**, sesuai spesifikasi. Konfirmasi:
- Slide 01 (Cover) di line 113 → Slide 32 (Terima Kasih) di line 2164
- Chrome footer pada setiap slide menampilkan `NN / 32` (mis. line 174: `02 / 32`, line 2216: `32 / 32`)

### Slide yang Sulit Diaudit dari File HTML Statis

- **Crime #7 (white space):** Estimasi visual sangat bergantung pada rendering nyata. Karena slide berukuran 1920×1080px dan menggunakan layout CSS absolut, kepadatan dinilai berdasarkan kombinasi jumlah elemen, jumlah kata, dan penggunaan grid (`grid-template-columns`). Slide dengan 3+ card atau tabel + narasi dianggap high-density.
- **Slides 21–30 (INDF case slides):** Beberapa slides memiliki animasi CSS yang tidak terlihat dalam file statis (mis. `animation:pulse` di line 2211 pada slide 32). Konten statis sudah cukup untuk audit crime #2, #3, #7.

### Asumsi untuk Crime #3 (Font Size)

- **Threshold:** 40pt. Dalam konteks HTML/CSS pada layar 1920px, kami menggunakan konversi praktis: `font-size: 40px` setara dengan Winston's "40pt" threshold karena presentasi dirender secara digital pada proyektor.
- **Global CSS (lines 28–38):** `.t-h1` = 96px ✓, `.t-h2` = 68px ✓, `.t-h3` = 48px ✓, `.t-h4` = 34px ✗, `.t-h5` = 26px ✗, `.t-lead` = 26px ✗, `.t-body` = 22px ✗, `.t-body-sm` = 18px ✗, `.t-label` = 13px ✗, `.t-meta` = 16px ✗.
- `.t-h1`, `.t-h2`, `.t-h3` adalah satu-satunya kelas yang memenuhi threshold; dipakai hanya untuk judul utama slide.
- Seluruh konten informasional (body text, bullet points, tabel, card content, label, metadata) menggunakan kelas sub-40px.
- **Jumlah deklarasi:** 573 dari 587 deklarasi `font-size` dalam file menggunakan ukuran <40px.
- **Footnote exemption:** Tidak ada footnote formal dalam deck; `.t-caption` (18px) dan `.t-meta` (16px) digunakan sebagai "meta/caption" dan termasuk dalam flag crime #3 karena dipakai sebagai teks yang harus dibaca audiens (bukan sekadar attributasi kecil).

### Asumsi untuk Crime #7 (White Space)

- **Threshold operasional:** >70% area slide terisi konten dianggap "no white space".
- Estimasi berdasarkan: (a) jumlah grid columns, (b) jumlah card/tabel, (c) keberadaan elemen bawah penuh lebar.
- Slides 21–30 (INDF case slides) sering menggunakan `height:calc(100% - NNpx)` yang memaksa card mengisi tinggi penuh frame — ini dikonfirmasi sebagai high-density.
- Crime #7 ditandai sebagai MED (bukan HIGH) untuk sebagian besar slide kecuali yang menggunakan font 15px atau lebih kecil sebagai sinyal kepadatan berlebih (slides 10, 12, 15, 16, 18, 19, 28).

### Crime #8 (Background Clutter)

- **`<img>` tags:** Hanya ada di slide 01 (STIE Logo.png line 117, Logo INDF.png line 124) — tepat sesuai aturan Winston (logo hanya di slide cover).
- **`.grid-bg`:** Pattern grid geometris sangat subtle (opasitas 4–5%, lines 76–77); tidak termasuk "background clutter" karena tidak mengganggu keterbacaan.
- **SVG dekoratif:** Slide 01 berisi SVG lingkaran besar (lines 115–116) sebagai elemen visual; ini adalah desain intentional pada cover dan tidak dianggap "clutter".
- **Kesimpulan Crime #8:** 0 occurrences — deck ini sudah bersih dari logo dan clutter berlebih.

### Konsistensi Auditor

Data angka INDF dalam slide (mis. Rp52,2T goodwill, EPS Rp984, dll.) tidak diverifikasi akurasi faktualnya dalam audit ini — sesuai scope yang terbatas pada design crimes F2, bukan validasi substansi FASB. Crime #2 dinilai berdasarkan estimasi visible word count yang konservatif; beberapa slide mungkin memiliki lebih banyak kata dari perkiraan karena teks tersembunyi dalam CSS yang tidak dirender dalam file statis.
