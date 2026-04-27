# Winston Revision Priorities — Deck v5 → v6

**Source:** `crime-inventory.md` (commit `f58531d`)
**Output target:** `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html`
**E4 escalation rule:** HIGH-XL diangkat ke Phase 4 redesign, bukan patch v6.

> **Catatan Rekonsiliasi:** Executive summary di `crime-inventory.md` menyatakan total 109 entri
> (HIGH=40, MED=56, LOW=13). Namun hitungan baris aktual pada tabel Per-Slide Inventory
> menghasilkan **98 baris** (HIGH=55, MED=40, LOW=3). Selisih 11 entri kemungkinan disebabkan
> oleh inkonsistensi internal antara summary dan tabel pada sumber T6. Dokumen ini mem-bucket
> 98 baris yang secara eksplisit tercantum dalam tabel — tidak ada entri yang diinventarisasi
> ulang maupun dihilangkan. Eksekutor Phase 4 harus merujuk ke tabel aktual `crime-inventory.md`
> sebagai otoritas data, bukan ringkasan eksekutif.

---

## Tier 1 — HIGH (Must-Fix Sebelum Demo)

> Defect yang merusak kredibilitas atau pemahaman audiens. Wajib dibereskan
> sebelum file dapat dipresentasikan. Catatan: entries HIGH-XL dipindahkan
> ke "E4 Escalation" sub-section di bawah — tidak di-patch di v6, melainkan
> menjadi requirement redesign Phase 4.

---

### Tier 1a — HIGH (non-XL, fix di v6)

| Slide # | Crime # | Bukti | Effort | Fix |
|---------|---------|-------|--------|-----|
| 03 | #2 | Card "Era Pra-CF": CAP/APB/ARS narasi panjang; total slide >100 kata visible | L | Pisahkan timeline + tabel SFAC ke slide terpisah; pertahankan hanya timeline visual di slide ini |
| 04 | #2 | Card kiri OB2 + 5 item pengguna utama; card kanan tabel 5-baris + OB17; >80 kata visible | L | Pisahkan ke 2 slide: (a) tujuan + OB2, (b) pengguna utama + evolusi |
| 05 | #2 | Kolom kiri definisi RE1 + entitas + konsolidasi; kolom kanan org chart + 4 subsidiary + 3 stats; >90 kata | L | Pisahkan definisi entitas pelapor (slide 05a) dari org chart INDF (slide 05b) |
| 07 | #2 | Kolom kiri diagram SFAC 8 + 6 boxes; kolom kanan 5 "Transformasi Kunci" cards; >100 kata visible | L | Pisahkan diagram SFAC 8 hierarchy (slide 07a) dari tabel 5 transformasi (slide 07b) |
| 07 | #7 | Dua kolom kepadatan sangat tinggi: kolom kiri diagram + 6 boxes, kolom kanan 5 cards bertumpuk; frame hampir penuh | L | Pisahkan ke 2 slide |
| 10 | #2 | 4 card QC masing-masing 25–30 kata body + INDF aplikasi + catatan; Cost Constraint panel bawah; >100 kata | L | Pisahkan 4 QC peningkat ke 2 slide (2 QC per slide); pindahkan Cost Constraint ke slide 07 atau sendiri |
| 10 | #7 | Grid 2×2 card penuh + Cost Constraint bar bawah; font 15px menandai kepadatan berlebih | L | Redesign ke 2 slide; gunakan lebih sedikit kata per card |
| 12 | #2 | 2 tabel perbandingan SFAC 6 vs SFAC 8 Ch.4 + 2 box definisi liabilitas + tabel goodwill 3-baris; >80 kata | L | Pisahkan: (a) definisi baru aset, (b) definisi baru liabilitas + INDF goodwill test |
| 12 | #7 | 3 card/tabel bertumpuk dalam grid 1fr 1fr + tabel bawah penuh lebar; frame ~90% terisi | L | Pisahkan ke 2 slide |
| 14 | #2 | 2 card besar SFAC 5 (4 kriteria) + SFAC 8 Ch.5 (3 kriteria); tabel Recognition vs Disclosure; >80 kata | L | Pisahkan SFAC 5 vs SFAC 8 Ch.5 (slide 14a) dari Recognition vs Disclosure (slide 14b) |
| 15 | #2 | Tabel 5 atribut (5×5 kolom) + 4 critique boxes (Solomons, Sterling, SFAC 5 par. 2, Miller); >100 kata | L | Pisahkan: (a) tabel lima atribut (slide 15a), (b) perspektif kritis (slide 15b) |
| 15 | #7 | Tabel penuh lebar atas + 4 card bawah grid 4 kolom; teks critique cards sangat kecil; frame hampir penuh | L | Pisahkan ke 2 slide |
| 18 | #2 | 4 limitation boxes + 3 perspektif kritis (Gaa, Archer, Wolk) masing-masing ~30 kata; >100 kata visible | L | Pisahkan: (a) empat keterbatasan (slide 18a), (b) tiga perspektif kritis (slide 18b) |
| 18 | #7 | Grid 4 kolom (limitations) + grid 3 kolom (perspectives); tidak ada breathing room; frame hampir penuh | L | Pisahkan ke 2 slide |
| 19 | #2 | Grid 4×2 (8 chapter cards, tiap card 2–3 kalimat deskripsi) + timeline narasi bawah; >120 kata visible | L | Pisahkan ke 2 slide: (a) Ch.1–4, (b) Ch.5–8 + timeline |
| 19 | #7 | Grid 4×2 rows (8 cards) + timeline bar bawah; frame hampir penuh | L | Pisahkan ke 2 slide |
| 21 | #2 | Org chart 4 subsidiary + 8 stat blocks + ownership donut chart + keterangan audit; >80 kata visible | L | Pisahkan profil perusahaan (subsidiaries + overview) dari financial highlights (stats + ownership) |
| 28 | #2 | Tabel 6 baris × 4 kolom (Peta Pengukuran) + matriks 2×2 Relevansi vs Verifikasi + box keterbatasan; >80 kata | L | Pisahkan tabel (slide 28a) dari matriks 2×2 (slide 28b); pindahkan box keterbatasan ke catatan |
| 28 | #7 | Kolom kiri tabel besar 6 baris + kolom kanan matriks 2×2 + box bawah; frame hampir penuh | L | Pisahkan ke 2 slide |
| 30 | #2 | 3 kolom: catatan 5 item + tabel segmen 3-baris + related party (stat + 3 breakdown) + Enhancing QC card; >80 kata | L | Pisahkan: (a) struktur catatan + segmen, (b) related party + Enhancing QC |
| 31 | #2 | Grid 2 kolom: 5 insight cards masing-masing ~25–30 kata + 1 box overarching conclusion; >120 kata visible | L | Sederhanakan ke 3 insight utama; pindahkan detail ke catatan; kesimpulan = 1 kalimat |
| 32 | #9 | Daftar 6 anggota kelompok lengkap dengan NIM disajikan sebagai konten utama slide terakhir | M | Ganti dengan Contributions Slide (3–5 kontribusi spesifik); sebutkan anggota hanya di chrome/footer |
| 32 | #10 | "Terima Kasih" (72px) + "THANK YOU" (28px) sebagai judul dominan slide terakhir | M | Ganti judul slide dengan "Kontribusi Kelompok 3" atau "Temuan Utama"; pertahankan Q&A sebagai sub-elemen kecil |

**Subtotal HIGH non-XL:** 23 entries.

---

### Tier 1b — HIGH-XL (E4 Escalation — redesign, not patch)

| Slide # | Crime # | Bukti | Effort | Reason for E4 escalation | Spec Reference |
|---------|---------|-------|--------|---------------------------|-----------------|
| 01 | #3 | `.t-meta`/`.t-label` (13–16px) di semua nama anggota; `.t-body` 22px; `.t-lead` 26px | XL | Defek sistemik CSS root: 573/587 deklarasi font-size di bawah 40px. Tidak feasible patch per slide. | `specs/winston-integration-rules.md` E4 |
| 02 | #3 | `.t-body` 22px, `.t-meta` 16px, `.t-label` 13px di header tabel agenda | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 03 | #3 | `.t-h5` 26px; inline `font-size:20px`; tabel SFAC `.tbl compact` 16px/12px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 04 | #3 | Semua teks card "Primary Users" 19px; tabel evolusi `.tbl compact` 16px; `.t-meta` 16px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 05 | #3 | Semua teks card 19px; org chart 21px/19px; stats bawah 19–20px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 06 | #3 | Boxes hierarki QC 20–21px label; subtext 12px; bottom text `.t-body-sm` 18px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 07 | #3 | Boxes 19px/12px/16px/20px; semua sub-40px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 08 | #3 | Card body 21px; bar labels 20px; INDF application text 19px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 09 | #3 | Heading sub 21px; komponen boxes 21px; catatan konservatisme 20px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 10 | #3 | Body text 15px (sangat kecil); INDF aplikasi 14px; pill labels 13px; Cost Constraint 15px/13px | XL | Sama — font 15px mengkonfirmasi konten berlebih yang dipaksakan masuk | `specs/winston-integration-rules.md` E4 |
| 11 | #3 | `.tbl td` 18px; `.tbl th` 14px; seluruh tabel elemen | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 12 | #3 | `.tbl compact` 16px/12px; box goodwill 14px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 13 | #3 | Card 21px/19px; CI waterfall berbagai ukuran sub-40px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 14 | #3 | Card body 21px/20px; catatan RD3 17px; `.tbl compact` 16px/12px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 15 | #3 | `.tbl compact` 16px/12px; critique boxes heading 21px; body 20px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 16 | #3 | Body text Entry/Exit 14px; label M30–M34 13px; `.tbl compact` 16px/12px | XL | Font 14–13px mengkonfirmasi konten dipaksakan; root cause ada di design system | `specs/winston-integration-rules.md` E4 |
| 17 | #3 | Hierarki FS 21px/20px/19px; OCI waterfall 20px/19px; BC7.21 box 21px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 18 | #3 | Limitation boxes 22px/20px; perspektif kritis 19px/20px; catatan kelemahan 16px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 19 | #3 | Chapter cards heading 20px; body 19px; timeline labels 20px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 20 | #3 | Rantai otoritas 21px/20px; `.tbl compact` 16px/12px; convergence bullets 20px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 21 | #3 | Stat block 34px (masih sub-40pt); subsidiary 15px; ownership 22px/18px; audit badge 18px | XL | Sama — global typography system; 34px stat masih di bawah ambang batas 40px | `specs/winston-integration-rules.md` E4 |
| 22 | #3 | Zona diagram 18px/16px/15px/13px; tabel kebutuhan 18px td; OB2 box 22px | XL | Font 13px di zona diagram = extreme sub-threshold; root cause global | `specs/winston-integration-rules.md` E4 |
| 23 | #3 | Card body 18px; label 13px; EPS bar chart tahun 13px; nilai 13px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 24 | #3 | Card body bullets 21px; limitation bar 21px/19px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 25 | #3 | Tabel uji 18px td; challenge cards 17px; (stat angka utama 58px memenuhi, teks lain tidak) | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 26 | #3 | Body text panel 20px; kutipan definisi italic 21px; tabel komponen sub-40pt | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 27 | #3 | Case cards heading 24px; isi tabel/bullet 17px; RD3 banner 19px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 28 | #3 | Tabel Peta Pengukuran 12px th / 14px td (sangat sub-threshold); matriks 2×2 14px/18px; limitation 17px | XL | Font 12–14px di tabel = paling ekstrem; tidak mungkin patch per cell | `specs/winston-integration-rules.md` E4 |
| 29 | #3 | 3 kolom penyajian 20px; OCI waterfall 20px; tabel efek kurs `.tbl compact` 16px/12px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 30 | #3 | Catatan INDF 20px; tabel segmen 18px; related party 19px; Enhancing QC 19px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 31 | #3 | Insight cards heading + body 19px; "Kesimpulan Overarching" 20px | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |
| 32 | #3 | "THANK YOU" 28px; nama anggota 18px; NIM 16px; Sesi Tanya Jawab 20px (h1 utama 72px saja yang memenuhi) | XL | Sama — global typography system | `specs/winston-integration-rules.md` E4 |

**Subtotal HIGH-XL:** 32 entries.

---

## Tier 2 — MEDIUM (Fix di v6, Tidak Mendesak)

| Slide # | Crime # | Bukti | Effort | Fix |
|---------|---------|-------|--------|-----|
| 01 | #2 | Footer 45+ kata: 6 nama anggota + NIM + judul institusi + tahun akademik | M | Pindahkan anggota ke slide dedikasi atau hapus NIM; cover cukup nama tanpa NIM dan detail institusi |
| 02 | #2 | Tabel agenda 8 baris dengan nama bagian + slide range + durasi; >25 kata termasuk "~43 menit" | M | Sederhanakan ke 5–6 bagian maksimum; hapus kolom Durasi |
| 02 | #7 | Tabel 8 baris + header "≥43 menit" + judul mengisi >75% frame; sedikit ruang putih | M | Rancang ulang agenda sebagai grid visual 2×4 dengan ikon; kurangi ke 6 item |
| 03 | #7 | SVG timeline 1760px + 2 panel besar bawah (grid 1fr 1fr) + tabel 8 baris; kepadatan sangat tinggi | L | Pisahkan ke 2 slide: (a) timeline, (b) tabel SFAC |
| 04 | #7 | 2 kolom masing-masing 2 card + tabel penuh; >80% area frame; tidak ada breathing room | L | Pisahkan konten; tambah margin antara elemen |
| 05 | #7 | 2 kolom sangat padat: kiri 3 card bertumpuk; kanan org chart + 4 cards + 3 stats | L | Pisahkan ke 2 slide dengan konten lebih sedikit per slide |
| 06 | #2 | Catatan bawah >20 kata: "Tanpa memahami SFAC 2..."; total visible >50 kata | M | Hapus catatan bawah; letakkan di speaker notes; sederhanakan diagram ke nama saja |
| 06 | #7 | Diagram hierarki vertikal + 2 kolom besar + 6 komponen boxes + catatan bawah; frame penuh | L | Sederhanakan diagram; hapus sub-label di setiap box |
| 08 | #2 | 3 card QC masing-masing heading + deskripsi + INDF box + bar chart EPS 5-tahun; >80 kata visible | L | Pisahkan chart EPS ke slide terpisah; pertahankan 3 card QC saja |
| 08 | #7 | 3 card penuh baris atas + bar chart penuh lebar bawah; >85% frame terisi | M | Pisahkan chart EPS; tambah whitespace antara cards |
| 09 | #2 | 2 kolom SFAC 2 vs SFAC 8 (heading + definisi + 3 komponen + catatan) + bar merah BC3.27; >80 kata | L | Pisahkan ke: (a) SFAC 2 Reliability, (b) SFAC 8 Faithful Representation + Conservatism removal |
| 09 | #7 | 2 panel besar + panel merah bawah; arrow di tengah tidak memberi breathing room; hampir penuh | M | Tambah padding; pindahkan BC3.27 ke catatan presenter |
| 11 | #2 | Tabel 10 elemen (10 baris × 5 kolom) + heading + lead text; >50 kata visible; dense | M | Sederhanakan ke 4–5 elemen kunci; gunakan visual card bukan tabel penuh |
| 11 | #7 | Tabel penuh seluruh slide hampir tanpa whitespace; hanya judul dan tabel | M | Hilangkan 5 elemen minor; tambah whitespace di sekitar tabel |
| 13 | #2 | 2 card grid kiri (Revenue/Gains + Expenses/Losses) dengan 2 sub-card + definisi + contoh INDF; CI waterfall kanan; >70 kata | L | Pisahkan Revenue/Gains/OCI ke slide terpisah; atau fokus hanya pada CI waterfall |
| 13 | #7 | 4 card dalam 2 baris kiri + panel CI kanan; sub-card dalam card utama menambah kompleksitas | M | Sederhanakan ke 2 konsep per slide |
| 14 | #7 | 2 card besar baris atas + tabel penuh lebar bawah; >85% frame terisi | M | Pisahkan ke 2 slide |
| 16 | #2 | 2 panel Entry vs Exit + tabel 5-baris aplikasi INDF (4 kolom teks penuh per cell); >60 kata | L | Pisahkan: (a) Entry vs Exit concept, (b) tabel aplikasi INDF |
| 16 | #7 | Panel konsep (grid 1fr 80px 1fr) + tabel penuh lebar; >80% frame terisi | M | Pisahkan ke 2 slide; sederhanakan tabel ke 3 baris kunci |
| 17 | #2 | Kolom kiri hierarki FS + PR12 + OCI rekonsiliasi; kolom kanan BC7.21 + INDF implikasi; >80 kata | L | Pisahkan BC7.21 ke slide terpisah; pertahankan hierarki FS dan OCI di slide 17 |
| 17 | #7 | 2 kolom masing-masing sangat padat; kolom kiri 3 card bertumpuk + OCI waterfall | M | Pisahkan ke 2 slide |
| 20 | #2 | Diagram rantai FASB→IASB→PSAK→INDF + 4 convergence bullets + tabel 3-baris perbedaan; >60 kata | M | Hapus tabel perbedaan atau pindahkan ke catatan; diagram rantai sudah cukup visual |
| 20 | #7 | Diagram flowchart kiri + 2 card kanan (hijau + tabel); flowchart sendiri sudah padat dengan teks | M | Sederhanakan diagram; hapus tabel dalam kolom kanan |
| 21 | #7 | 2 kolom: kiri org chart + 4 subsidiary cards; kanan stats (4+4 grid) + ownership chart + audit badge | L | Pisahkan ke 2 slide |
| 22 | #2 | Diagram 2 zona + tabel 3-baris kebutuhan + box prinsip OB2 dengan kutipan; >60 kata | M | Sederhanakan diagram; pindahkan tabel kebutuhan ke catatan; pertahankan zona + OB2 |
| 22 | #7 | 2 kolom masing-masing penuh: zona diagram bertingkat mengisi >60% tinggi; tabel kanan padat | M | Sederhanakan ke diagram zona saja; hapus tabel |
| 23 | #2 | 3 kolom: Predictive (chart EPS + teks) + Confirmatory (margin data) + Materiality (goodwill + bar chart); >80 kata | L | Pisahkan menjadi (a) Predictive + Confirmatory, (b) Materiality + síntesis |
| 23 | #7 | 3 kolom masing-masing penuh tinggi dengan teks + chart; frame hampir penuh | L | Kurangi ke 2 kolom; pindahkan chart ke slide companion |
| 24 | #2 | 3 card masing-masing 3 bullets (15–20 kata/bullet) + limitation bar bawah; >80 kata | L | Sederhanakan ke 1–2 bullet per card; pindahkan detail ke catatan presenter |
| 24 | #7 | 3 card setinggi frame utama + limitation bar bawah; >85% frame terisi | M | Kurangi bullet per card; tambah breathing room |
| 25 | #2 | 2 tabel uji definisi (masing-masing 3×3 kolom) + proportion card + challenge list; >60 kata | M | Gabungkan kedua tabel ke 1 tabel komparatif; sederhanakan challenge ke 2 poin |
| 25 | #7 | Grid 1fr 1fr 340px: 2 tabel penuh + kolom kanan 2 card bertumpuk; >80% frame terisi | M | Sederhanakan tabel; tambah whitespace |
| 26 | #2 | Panel liabilitas (definisi + tabel Rp70,81T + obligasi USD) + panel ekuitas (NCI + retained earnings); >70 kata | M | Sederhanakan ke angka kunci + 1 kalimat interpretasi per panel |
| 26 | #7 | 2 panel besar masing-masing berisi definisi + tabel + stats; >80% frame | M | Sederhanakan; hapus tabel detail, pertahankan stats utama |
| 27 | #2 | RD3 banner + 3 case card masing-masing tabel 3-baris + keterangan bawah; >80 kata | L | Sederhanakan setiap case card ke 1 klaim utama + angka kunci; pertahankan RD3 banner |
| 27 | #7 | RD3 banner + grid 3 kolom case card setinggi frame; >85% frame terisi | M | Kurangi isi per card; tambah spacing |
| 29 | #2 | 3 kolom: hierarki FS (face vs notes) + OCI waterfall 5 item + efek kurs tabel 3-baris; >70 kata | L | Fokus slide ini pada satu topik: OCI saja atau Face of FS saja |
| 29 | #7 | Grid 340px + 1fr + 1fr dengan masing-masing penuh; frame hampir penuh | M | Sederhanakan ke satu fokus konten |
| 30 | #7 | Grid 3 kolom masing-masing berisi 2 card; frame >85% terisi | L | Pisahkan ke 2 slide |
| 31 | #7 | Grid 2 kolom × 3 rows (5 card + 1 conclusion); frame hampir penuh | L | Kurangi ke 3 insight; tambah breathing room |

**Subtotal MEDIUM:** 40 entries.

---

## Tier 3 — LOW (Kosmetik)

| Slide # | Crime # | Bukti | Effort | Fix |
|---------|---------|-------|--------|-----|
| 02 | #1 | Agenda 8 bagian termasuk "Sintesis Teori" + "Penutup & Kesimpulan" sebagai segmen terpisah; ~43 menit berpotensi melebihi ambang optimal | L | Pertimbangkan menggabungkan "Sintesis Teori" dengan "Penutup"; hilangkan satu segmen untuk memperpadat alur |
| 19 | #1 | Slide 19 "Diagram Master SFAC 8" merangkum 8 chapter; redundan sebagian dengan slide 03 yang sudah memuat tabel kronologis SFAC 1–8 | M | Klarifikasi tujuan berbeda (slide 03 = kronologi, slide 19 = arsitektur); hapus jika dianggap redundan |
| 31 | #1 | Slide 31 "Sintesis — Lima Insight Utama" berpotensi tumpang tindih dengan slide 19 dan 20 dalam fungsi merangkum; tiga slide sintesis berpotensi redundan | M | Evaluasi apakah slide 31 dapat digabung dengan elemen slide 19 atau 20 |

**Subtotal LOW:** 3 entries.

---

## Ringkasan Agregat

| Tier | Sub-tier | Count |
|------|----------|-------|
| Tier 1 — HIGH | 1a (non-XL, fix v6) | 23 |
| Tier 1 — HIGH | 1b (XL, E4 escalation) | 32 |
| Tier 2 — MEDIUM | fix v6, tidak mendesak | 40 |
| Tier 3 — LOW | kosmetik | 3 |
| **Total** | | **98** |

> **Rekonsiliasi vs T6 Executive Summary:** T6 menyatakan total 109 (HIGH=40, MED=56, LOW=13).
> Hitung aktual dari baris tabel Per-Slide Inventory: 98 baris (HIGH=55, MED=40, LOW=3).
> Selisih 11 entri tidak dapat diselesaikan tanpa re-audit, yang di luar scope dokumen ini.
> Eksekutor Phase 4 harus menggunakan 98 baris yang terdokumentasi sebagai basis kerja.

---

## E4 Escalation Summary

> Daftar entri HIGH-XL yang TIDAK akan di-patch di v6, melainkan diangkat
> ke spec untuk Phase 4 redesign per `specs/winston-integration-rules.md` E4.

Seluruh 32 entri Crime #3 HIGH-XL berakar pada satu akar masalah yang sama: **design system global v5 menggunakan tipografi di bawah ambang batas Winston 40pt untuk hampir seluruh konten informasional.** CSS root (baris 28–38 pada file HTML) menetapkan kelas-kelas seperti `.t-h4` (34px), `.t-h5` (26px), `.t-lead` (26px), `.t-body` (22px), `.t-body-sm` (18px), `.t-label` (13px), dan `.t-meta` (16px) — semuanya sub-40px, dan semuanya dipakai di setiap slide sebagai teks yang harus dibaca audiens. Audit mengkonfirmasi 573 dari 587 deklarasi `font-size` dalam file menggunakan ukuran di bawah 40px (97,6%). Skala ini tidak meninggalkan ruang untuk intervensi lokal: memperbaiki satu slide saja akan merusak konsistensi visual deck dan tidak menyelesaikan masalah untuk 31 slide lainnya.

Konsekuensinya, semua 32 entri Crime #3 diangkat ke Phase 4 sebagai **satu requirement tunggal: redesign typography system dari nol** dengan minimum body text 40pt, sebelum slide-level content writing dimulai. Ini berarti v6 tidak mencoba memperbaiki Crime #3 per slide — v6 hanya menyelesaikan Tier 1a (content density + Crime #9/#10) dan Tier 2–3, sementara typography adalah pre-condition Phase 4. Slide 32 mendapat perhatian tambahan karena menggabungkan Crime #3 + #9 + #10 secara bersamaan: redesign slide terakhir harus terjadi setelah typography system selesai.

| Slide # | Crime # | Alasan E4 | Spec Reference |
|---------|---------|------------|-----------------|
| 01 | #3 | CSS root: `.t-label` 13px dipakai untuk nama anggota; root-level defect | `specs/winston-integration-rules.md` E4 |
| 02 | #3 | CSS root: `.t-label` 13px di header tabel agenda | `specs/winston-integration-rules.md` E4 |
| 03 | #3 | `.t-h5` 26px + `.tbl compact` 16px/12px; bukan outlier, bagian sistem | `specs/winston-integration-rules.md` E4 |
| 04 | #3 | Card body 19px; `.tbl compact` 16px; semuanya dari kelas global | `specs/winston-integration-rules.md` E4 |
| 05 | #3 | Card body 19px; org chart 21px/19px; stats 19–20px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 06 | #3 | Box labels 20–21px + subtext 12px; `.t-body-sm` 18px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 07 | #3 | Boxes 12–20px; tidak ada satu ukuran pun yang mencapai 40px | `specs/winston-integration-rules.md` E4 |
| 08 | #3 | Card body 21px; bar labels 20px; INDF text 19px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 09 | #3 | Heading sub 21px; komponen boxes 21px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 10 | #3 | Body text 15px — font terkecil di deck; membuktikan konten berlebih dipaksakan masuk | `specs/winston-integration-rules.md` E4 |
| 11 | #3 | `.tbl td` 18px; `.tbl th` 14px; kelas global `.tbl` menjadi akar masalah | `specs/winston-integration-rules.md` E4 |
| 12 | #3 | `.tbl compact` 16px/12px; box goodwill 14px; global `.tbl compact` bermasalah | `specs/winston-integration-rules.md` E4 |
| 13 | #3 | Card 21px/19px; waterfall sub-40px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 14 | #3 | Card body 21px/20px; RD3 17px; `.tbl compact` 16px/12px; dari sistem | `specs/winston-integration-rules.md` E4 |
| 15 | #3 | `.tbl compact` 16px/12px; critique boxes 20–21px; dari sistem | `specs/winston-integration-rules.md` E4 |
| 16 | #3 | Body text 14px; label 13px — sangat sub-threshold; `.tbl compact` 16px/12px | `specs/winston-integration-rules.md` E4 |
| 17 | #3 | Hierarki FS 19–21px; OCI waterfall 19–20px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 18 | #3 | Limitation boxes 20–22px; perspektif kritis 19–20px; catatan 16px | `specs/winston-integration-rules.md` E4 |
| 19 | #3 | Chapter cards 19–20px; timeline labels 20px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 20 | #3 | Rantai otoritas 20–21px; `.tbl compact` 16px/12px; convergence bullets 20px | `specs/winston-integration-rules.md` E4 |
| 21 | #3 | Stat block 34px masih sub-40pt; subsidiary 15px; ownership 18–22px | `specs/winston-integration-rules.md` E4 |
| 22 | #3 | Zona diagram 13–18px; OB2 box 22px; tabel 18px; 13px di zona diagram sangat ekstrem | `specs/winston-integration-rules.md` E4 |
| 23 | #3 | Card body 18px; label 13px; EPS chart 13px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 24 | #3 | Card bullets 21px; limitation bar 19–21px; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 25 | #3 | Tabel 18px td; challenge cards 17px; (58px stat angka saja yang ≥40pt) | `specs/winston-integration-rules.md` E4 |
| 26 | #3 | Body panel 20px; definisi italic 21px; tabel sub-40pt; semua dari sistem | `specs/winston-integration-rules.md` E4 |
| 27 | #3 | Case cards heading 24px; isi 17px; RD3 banner 19px; semua sub-40pt | `specs/winston-integration-rules.md` E4 |
| 28 | #3 | Tabel Peta Pengukuran 12px th / 14px td — paling ekstrem di seluruh deck | `specs/winston-integration-rules.md` E4 |
| 29 | #3 | Kolom penyajian 20px; OCI waterfall 20px; tabel efek kurs 12–16px | `specs/winston-integration-rules.md` E4 |
| 30 | #3 | Catatan INDF 20px; tabel segmen 18px; related party 19px; Enhancing QC 19px | `specs/winston-integration-rules.md` E4 |
| 31 | #3 | Insight cards heading + body 19px; "Kesimpulan Overarching" 20px | `specs/winston-integration-rules.md` E4 |
| 32 | #3 | "THANK YOU" 28px; nama 18px; NIM 16px; Sesi Tanya Jawab 20px (h1 72px saja yang memenuhi) | `specs/winston-integration-rules.md` E4 |

---

## Recommended Execution Order untuk Phase 4

1. **[Redesign typography system secara global]**
   Alasan: 32 slide di-flag Crime #3 HIGH-XL. CSS root (baris 28–38) menjadi akar tunggal masalah. Patch per slide tidak feasible karena berarti 32 × intervensi yang akan saling bertentangan dan tidak menyelesaikan konsistensi. Tetapkan terlebih dahulu: minimum body text 40pt (`≥40px`), gunakan 48–56pt untuk body text utama, 64–72pt untuk heading sekunder. Semua kelas `.t-h4`, `.t-h5`, `.t-lead`, `.t-body`, `.t-body-sm`, `.t-label`, `.t-meta` harus direvisi di CSS global sebelum satu slide pun disentuh kontennya.

2. **[Tier 1a — fix HIGH non-XL di v6]**
   Prioritas urutan dalam Tier 1a (berdasarkan dampak audiens):
   - Slide 32: Crime #9 + #10 — ganti "Terima Kasih" dengan Contributions Slide (M effort, dampak langsung pada kesan akhir audiens)
   - Slide 19: Crime #2 + #7 — pisahkan 8 chapter cards ke 2 slide (L effort, slide paling padat dalam deck)
   - Slide 18: Crime #2 + #7 — pisahkan limitations dan perspectives (L effort)
   - Slide 15: Crime #2 + #7 — pisahkan tabel atribut dan critique boxes (L effort)
   - Slide 10: Crime #2 + #7 — pisahkan 4 QC peningkat + Cost Constraint (L effort)
   - Sisa Tier 1a sesuai slide order (slides 03, 04, 05, 07, 12, 14, 21, 28, 30, 31)

3. **[Slide 32 redesign — gabungan Crime #9 + #10]**
   Slide terakhir memerlukan redesign konseptual: ganti dari "Terima Kasih / daftar anggota" menjadi slide Kontribusi Kelompok 3 yang menampilkan 3–5 finding spesifik. Ini bukan sekadar edit teks — butuh struktur slide baru. Lakukan setelah typography system selesai.

4. **[Tier 2 entries — fix MEDIUM di v6]**
   Urutan rekomendasi dalam Tier 2:
   - Slide 02: Crime #2 + #7 (agenda padat — langsung terlihat audiens di awal presentasi)
   - Slides 06, 08, 09, 11, 13, 14, 16, 17, 20 (konten teori)
   - Slides 21–30 (INDF case slides: 22, 23, 24, 25, 26, 27, 29, 30)
   - Slide 31: Crime #7 (sintesis — konten terakhir sebelum slide penutup)

5. **[Tier 3 entries — jika waktu cukup]**
   Crime #1 (slides 02, 19, 31) bersifat struktural — keputusan apakah slide redundan atau tidak harus dilakukan oleh tim presentasi, bukan eksekutor teknis. Tandai sebagai "keputusan editorial tim" dan anggit sebagai opsional.
