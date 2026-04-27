# Winston Integration — Process & Resolution Rules

**Source:** Spec `docs/superpowers/specs/2026-04-27-winston-integration-design.md` Bagian 5.
**Tujuan:** Aturan tetap untuk menyelesaikan konflik antara Winston dan
substansi/konteks akademik PKK. Dokumen ini mengatur *cara kerja*
integrasi lintas fase — bukan konten deck itu sendiri (itu tugas
`specs/presentation-design-spec.md`).

---

## E1 — Klausul Supremasi FASB (TEGAS)

**Aturan:** Substansi FASB Conceptual Framework dan Week 5 SELALU menang
atas Winston. Winston adalah *lensa retorika*, bukan editor konten
akademik. Bila ada konflik antara tuntutan retorika Winston dan kewajiban
substansi FASB/Week 5, framework Winston WAJIB diadaptasi — TIDAK BOLEH
substansi FASB yang dipotong, dipersingkat, atau dihilangkan.

**Operasionalisasi:**

- Bila satu framework Winston memaksa pemotongan konten yang dimandatkan
  FASB atau Week 5, framework itu diadaptasi ke struktur dua slide, visual
  pendukung, atau catatan presenter — bukan dengan menghapus substansinya.
- **Contoh konkret — F3 "satu salient idea" vs FASB "dua karakteristik
  fundamental":** Winston F3 mensyaratkan satu salient idea untuk seluruh
  deck. FASB mensyaratkan dua karakteristik kualitatif fundamental —
  Relevance dan Faithful Representation — disajikan utuh dan dibedakan
  secara eksplisit. Resolusi: salient idea hidup di level *deck*
  ("Conceptual Framework adalah konstitusi pelaporan keuangan") sebagai
  ringkasan meta; Relevance dan Faithful Representation tetap muncul
  sebagai dua konsep terpisah di slide masing-masing (slides 10–13) tanpa
  kompromi definisi, komponen, atau contoh kasus.
- **Contoh konkret — F2 "≤25 kata per slide" vs definisi FASB lengkap:**
  Definisi formal FASB (mis. "Faithful Representation requires completeness,
  neutrality, and freedom from error" beserta penjelasan masing-masing)
  tidak boleh dipotong ke 25 kata. Resolusi: split ke dua slide — satu
  slide definisi (komponen tetap utuh), satu slide ilustrasi kasus INDF
  (≤25 kata body, narasi di catatan presenter).
- Reviewer Phase 4 WAJIB menolak setiap fix Winston yang melanggar klausul
  ini. Gate review slides 7–18 (blok teori FASB; slide kasus INDF di 19–29
  mengikuti gate E3) menggunakan `rubrics/_template.md` Bagian 5 ("FASB
  Supremacy Verifikasi") sebagai checklist wajib.
- Flag supremasi ini berlaku per slide: bila rubrik `rubrics/slide-NN.md`
  mendeteksi konflik, dokumen tersebut wajib mencatat resolusi eksplisit
  — bukan membiarkan konflik tak terdokumentasi.

---

## E2 — Pemisahan Design Crimes vs Delivery Crimes

**Aturan:** Dari sepuluh slide crimes Winston (F2), tiga adalah *delivery
crimes* — hanya dapat dinilai saat presentasi langsung, bukan dari file
HTML. Crimes ini TIDAK BOLEH masuk ke `crime-inventory.md`.

**Crimes yang termasuk delivery crimes (per F2 Winston):**

- Crime #4 — Membaca slide (reading aloud): hanya teramati saat presenter
  berbicara.
- Crime #5 — Penggunaan laser pointer: hanya teramati saat presentasi.
- Crime #6 — Presenter berdiri jauh dari slide: hanya teramati di venue.

**Operasionalisasi:**

- `analysis/winston-audit/crime-inventory.md` memuat HANYA tujuh design
  crimes (#1, #2, #3, #7, #8, #9, #10) — crimes yang dapat dinilai dari
  inspeksi file HTML.
- Delivery crimes (#4, #5, #6) dipindah ke
  `analysis/winston-audit/delivery-checklist.md` sebagai catatan dan
  checklist pre-demo untuk presenter Group 3.
- Rubrik slide (`rubrics/_template.md`) mencantumkan catatan eksplisit
  bahwa Crimes #4, #5, #6 dikecualikan dari checklist design — disertai
  pointer ke `delivery-checklist.md` agar auditor tidak bingung.
- Bila reviewer Phase 4 menemukan catatan presenter yang "membaca slide",
  ini dilaporkan ke `delivery-checklist.md` sebagai catatan latihan —
  bukan dicatat sebagai defect file di `crime-inventory.md`.

---

## E3 — Slide Kasus INDF: Angka sebagai Prop

**Aturan:** Untuk setiap slide yang mengandung angka dari INDF Annual
Report 2024, **angka adalah prop** dalam pengertian F5 Winston. Penyajian
wajib mengikuti story arc tiga-tahap F5: (1) konteks/ketegangan, (2)
demonstrasi via tabel/grafik, (3) resolusi melalui interpretasi FASB.
Angka yang disajikan tanpa story arc ini melanggar F5 dan WAJIB diperbaiki.

**Operasionalisasi:**

- Tabel atau grafik INDF yang berdiri sendiri tanpa narasi konteks dan
  resolusi FASB = pelanggaran ganda: kekosongan konteks naratif yang melanggar
  semangat F5 DAN pelanggaran E3 khusus. Keduanya dicatat terpisah di
  `crime-inventory.md`.
- Story arc wajib diimplementasikan sebagai berikut dalam satu slide atau
  sequence dua slide berurutan:
  - **Konteks/Ketegangan:** Satu kalimat atau visual yang menetapkan
    mengapa angka ini penting dan apa yang menjadi pertanyaan atau
    ketegangan analitisnya (mis. "EBIT Agribusiness naik 73% — apakah
    kenaikan ini mencerminkan realitas ekonomi secara faithful?").
  - **Demonstrasi:** Tabel atau grafik dengan angka spesifik dari AR INDF
    2024 disertai lokasi halaman. Tabel wajib diberi judul yang
    mengandung pertanyaan analitis, bukan sekadar label deskriptif.
  - **Resolusi:** Satu atau dua kalimat interpretasi eksplisit berbasis
    konsep FASB — menyebut karakteristik kualitas mana yang terpenuhi
    atau tidak terpenuhi, bukan sekadar ringkasan angka.
- Rubrik `rubrics/_template.md` Bagian 3 ("F5 Trigger") secara otomatis
  memicu checklist story arc ini untuk semua slide dengan role `case`,
  `chart`, atau `table` yang mengandung angka AR INDF.
- Tidak boleh ada fabrikasi angka: setiap angka wajib mengutip halaman
  INDF AR 2024. Pelanggaran ini sekaligus melanggar CLAUDE.md aturan #3
  ("Never fabricate data").

---

## E4 — Defect HIGH-XL: Diangkat ke Spec, Bukan Patch v6

**Aturan:** Bila audit menemukan defect dengan severity HIGH dan effort XL
(lebih dari 4 jam untuk diperbaiki — mis. font 24pt di seluruh 32 slide,
atau struktur visual yang mengabaikan white space secara sistemik di
seluruh deck), perbaikan TIDAK BOLEH dilakukan sebagai patch tambal-sulam
di `v6-winston.html`. Defect ini diangkat menjadi *requirement* untuk
Phase 4 build dari nol.

**Operasionalisasi:**

- `analysis/winston-audit/revision-priorities.md` wajib menandai setiap
  entri HIGH-XL dengan flag eksplisit: "needs full redesign, not patch"
  di kolom "E4 Flag".
- Entri HIGH-XL tersebut juga dikumpulkan di bagian terpisah "E4 Escalation
  Summary" dalam `revision-priorities.md`, mencantumkan: nomor slide,
  crime, alasan klasifikasi XL, dan referensi ke spec Phase 4 yang
  mengangkut requirement tersebut.
- Eksekutor Phase 4 WAJIB membaca `revision-priorities.md` bagian E4
  Escalation Summary sebelum memulai build. Requirement dari escalation
  ini dimasukkan ke `specs/presentation-design-spec.md` sebagai tambahan
  desain sistem (mis. "typography baseline: minimum 40pt untuk semua body
  text, tanpa pengecualian").
- `v6-winston.html` tetap sebagai duplikat byte-identik v5 untuk semua
  entri HIGH-XL — patch parsial yang meninggalkan defect sistemik lebih
  berbahaya daripada tidak ada patch, karena menciptakan ilusi perbaikan
  tanpa substansi.
- Klasifikasi "XL" ditentukan berdasarkan kriteria: perubahan yang
  membutuhkan lebih dari 4 jam edit, atau perubahan yang memengaruhi lebih
  dari 50% slide secara bersamaan, atau perubahan yang membutuhkan
  redesain arsitektur visual (bukan hanya edit teks).

---

## E5 — Dwibahasa: Indonesia Primer, Inggris Catatan Kaki

**Aturan:** Seluruh sintesis STAR ditulis dwibahasa di
`specs/presentation-design-spec.md`. Bahasa Indonesia adalah bahasa
primer — yang akan diucapkan dan ditampilkan di kelas S2 PKK. Bahasa
Inggris hadir sebagai catatan kaki untuk menjaga traceability ke sumber
Winston asli (berbahasa Inggris) dan ke literatur akademik (Wolk, Scott).

**Operasionalisasi:**

- Format dwibahasa yang wajib diterapkan di setiap elemen STAR dalam
  `specs/presentation-design-spec.md`:
  - Konten substantif ditulis dalam Bahasa Indonesia (primer).
  - Setelah konten Indonesia, blok **"English (catatan kaki untuk
    traceability):"** dalam blockquote `> ...` berisi terjemahan atau
    padanan Inggris yang memungkinkan pembaca menelusuri asal istilah ke
    sumber Winston.
- Slogan deck secara khusus wajib diuji keberterimaan dalam Bahasa
  Indonesia: dapat diucapkan dalam satu napas, dapat diulang tanpa
  penjelasan, dan tidak mengandung calque kaku dari Inggris. Terjemahan
  Inggris hanya di catatan kaki.
- Artefak lain (rubrik, audit, checklist) ditulis dalam Bahasa Indonesia
  formal akademik. Istilah teknis FASB dan Winston boleh dipertahankan
  dalam Bahasa Inggris bila tidak ada padanan Indonesia yang tepat (mis.
  "Faithful Representation", "salient idea", "props") — tetapi harus
  konsisten di seluruh dokumen.
- Transkripsi langsung dari jpeg Winston di `.claude/winston-framework.md`
  dipertahankan dalam Bahasa Inggris aslinya karena bersifat kutipan
  literal, bukan sintesis.
- Filename, label kode, perintah shell, dan referensi path file tetap
  dalam Bahasa Inggris tanpa pengecualian.

---

## Pemetaan Framework × Fase CLAUDE.md

| Framework | Phase 1 | Phase 3 | Phase 4 build | Phase 4 review |
|-----------|---------|---------|---------------|----------------|
| F1 Start Right | Input brainstorm: bentuk Empowerment Promise | Output wajib di `presentation-design-spec.md` | Diaplikasikan ke slide 1–3 | Reviewer cek slide 1 berisi promise |
| F2 Slide Crimes | (n/a) | Item rubrik tiap slide | Diaplikasikan per slide saat build | Reviewer cek 7 design crimes |
| F3 STAR | Input brainstorm: cari Symbol/Slogan | Output wajib di `presentation-design-spec.md` | Symbol muncul di ≥3 slide; Slogan ≥3× | Reviewer cek STAR alignment |
| F4 Persuade | Input brainstorm: tetapkan blok 3-segment | Output wajib (struktur 32 slide) | Boundaries slide 3/4 dan 29/30 | Reviewer cek slide 32 = contributions |
| F5 Props & Stories | Input brainstorm: tandai slide kasus | Output rubrik trigger | Aplikasi pada slide kasus + konsep sulit | Reviewer cek story arc |

**Catatan kolom:**

- **Phase 1 (brainstorm):** Framework digunakan sebagai *lensa input* —
  pertanyaan Winston membentuk arah brainstorm tanpa mengunci output.
  Hasil brainstorm dituangkan ke `specs/presentation-design-spec.md`.
- **Phase 3 (plan):** Framework menghasilkan *artefak wajib* — Empowerment
  Promise (F1), STAR lengkap (F3), dan struktur 32 slide (F4) harus ada
  di `presentation-design-spec.md` sebelum Phase 3 dapat ditandai selesai.
  F2 menghasilkan item rubrik di `rubrics/_template.md`; F5 menghasilkan
  trigger condition di rubrik yang sama.
- **Phase 4 build:** Framework menjadi *constraint implementasi* —
  eksekutor wajib memeriksa checklist F2 saat membangun setiap slide,
  menggunakan STAR dari `presentation-design-spec.md` sebagai referensi
  konstan, dan menerapkan story arc F5 di setiap slide kasus INDF.
- **Phase 4 review:** Framework menjadi *gate* — reviewer tidak boleh
  menandai slide APPROVED sebelum setiap item checklist di
  `rubrics/slide-NN.md` tercentang. Konflik Winston × FASB diselesaikan
  per E1 (FASB menang); resolusi dicatat di rubrik slide bersangkutan.

---

## Verifikasi (V3)

- [x] Klausul Supremasi FASB tegas dan eksplisit — E1 menggunakan imperatif
  "SELALU menang", "WAJIB diadaptasi", "TIDAK BOLEH", disertai dua contoh
  konkret dengan resolusi spesifik ✓
- [x] Aturan E2–E5 lengkap — setiap aturan memiliki bagian terpisah dengan
  sub-blok Aturan dan Operasionalisasi; tidak ada placeholder ✓
- [x] Pemetaan framework × fase CLAUDE.md lengkap — tabel F1–F5 × Phase 1,
  3, 4 build, 4 review terisi; catatan kolom menjelaskan semantik tiap
  fase ✓

---

*Dokumen ini adalah artefak PROSES. Konten deck-level ada di
`specs/presentation-design-spec.md`. Rubrik slide-level ada di
`rubrics/_template.md`. Single source of truth framework Winston ada di
`.claude/winston-framework.md`.*
