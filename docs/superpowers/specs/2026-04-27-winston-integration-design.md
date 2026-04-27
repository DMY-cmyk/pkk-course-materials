# Integrasi Patrick Winston MIT Presentation Master ke dalam Workflow Group 3 PKK

**Tanggal:** 2026-04-27
**Status:** APPROVED — disetujui pengguna pada 2026-04-27, siap diserahkan ke `writing-plans`
**Cakupan:** Brainstorm-only. Implementasi revisi v6-winston.html bukan bagian dari spec ini; itu pekerjaan `writing-plans` → `executing-plans` di tahap berikutnya.
**Bahasa:** Bahasa Indonesia (formal akademik) — sesuai konteks kelas S2 MNK202 PKK.

---

## 1. Latar Belakang & Tujuan

Folder `Patrcik Winston MIT Presentation Master/` berisi lima infografis yang merangkum kerangka "How To Speak" Patrick Winston (MIT) ke dalam lima framework:

| # | Framework | Output Chain |
|---|-----------|--------------|
| F1 | Start Any Presentation Right | Empowerment Promise → 60s Opening → Cuts → Script |
| F2 | Eliminate Slide Crimes | Crime Audit → Per-crime Fix → Final Slide Redesign → Brief |
| F3 | Make Ideas Unforgettable (STAR) | Symbol → Slogan → Surprise → Salient Idea → Story |
| F4 | Structure Any Talk That Persuades | Vision → Proof of Work → 5-min Opening → Contributions Close |
| F5 | Use Props and Stories | Confusing Concept → Prop → Story Arc → Verbal Script |

**Tujuan integrasi:** menjadikan Winston sebagai *lensa retorika* yang konsisten untuk seluruh workflow Group 3 (Phase 1–5 di CLAUDE.md), dengan dua sasaran sekaligus:

- **(B) Kodifikasi:** prinsip Winston dijadikan bagian formal dari `specs/` dan `rubrics/` sehingga setiap slide otomatis tunduk pada checklist Winston dalam tahap review.
- **(C) Audit deck v5 yang ada:** membuat *defect report* berbasis Winston atas `Pelaporan Keuangan Korporat Gr3 v5 (1).html`, lalu menyiapkan target file `v6-winston.html` (duplikat byte-identik dari v5) sebagai tempat revisi nanti.

**Prinsip duplikasi:** Deck v5 tidak disentuh. Audit menghasilkan dokumen terpisah; revisi diterapkan pada salinan v6. Hasilnya: perbandingan "sebelum vs sesudah" Winston dapat ditunjukkan secara visual.

---

## 2. Filosofi Dua-Lapisan Tata Kelola

Lima framework Winston dipetakan ke dua lapisan tata kelola yang berbeda:

### 2.1 Lapisan Deck (governs `specs/`)

Mengatur arsitektur deck secara keseluruhan. Berlaku sekali per deck.

- **F1 (Start Right)** → menentukan slide pembuka deck. Wajib menghasilkan **Empowerment Promise** spesifik dalam 60 detik pertama. Larangan: tidak boleh dibuka dengan lelucon, ucapan terima kasih, atau permintaan maaf.
- **F3 (STAR)** → menentukan *single salient idea* seluruh deck — Symbol (visual ikonik), Slogan (frasa pendek dapat diulang), Surprise (kebenaran kontra-intuitif), Salient Idea (satu, bukan dua/tiga), Story (personal namun universal).
- **F4 (Persuade Structure)** → menentukan arsitektur 32-slide: Vision Statement → Proof of Work → Contributions Close. Slide penutup wajib berisi **kontribusi konkret** — bukan "Terima Kasih" atau "Pertanyaan?".

### 2.2 Lapisan Slide (governs `rubrics/`)

Mengatur kualitas tiap slide individual. Berlaku 32 kali per deck (sekali per slide).

- **F2 (10 Slide Crimes)** → setiap rubrik slide wajib memuat checklist 10 kejahatan slide Winston (font ≥40pt, ≤25 kata, white space cukup, dst.). Hanya **design crimes** yang masuk; delivery crimes (membaca slide, jarak speaker) dipindah ke checklist presenter.
- **F5 (Props & Stories)** → wajib bagi slide kasus INDF dan slide konsep sulit. Story arc: tension → demonstration → resolution.

---

## 3. Komponen & Struktur Folder

Artefak yang akan dibuat dalam scope brainstorm ini:

```
.claude/
└── winston-framework.md              [BARU] Sumber tunggal kebenaran (single source
                                              of truth) — transkripsi 5 framework

specs/                                [BARU folder]
├── presentation-design-spec.md       [BARU] Deck-level: Empowerment Promise,
│                                            STAR core idea, Vision Statement,
│                                            Contributions Close, struktur 32 slide
└── winston-integration-rules.md      [BARU] Aturan tetap proses kerja antar fase,
                                              termasuk Klausul Supremasi FASB

rubrics/                              [BARU folder]
└── _template.md                      [BARU] Template rubrik universal — 10 design
                                              crimes + slot STAR-alignment + trigger F5

analysis/winston-audit/               [BARU subfolder]
├── audit-deck-v5.md                  [BARU] Naratif per framework atas v5
├── crime-inventory.md                [BARU] Tabel slide × crime × bukti × severity
├── revision-priorities.md            [BARU] HIGH/MEDIUM/LOW + effort S/M/L/XL
└── delivery-checklist.md             [BARU] Crimes yang hanya bisa dinilai saat
                                              presentasi langsung (bukan dari file)

Pelaporan Keuangan Korporat Gr. 3/
└── Pelaporan Keuangan Korporat Gr3 v6-winston.html  [BARU] Duplikat byte-identik
                                              dari v5; placeholder untuk revisi nanti
```

**Yang TIDAK dibuat sekarang:**
- `rubrics/slide-01.md … slide-32.md` — itu pekerjaan Phase 3 (writing-plans).
- Modifikasi konten apa pun pada `v6-winston.html` — itu pekerjaan tahap eksekusi.
- `design-system/`, `slides/`, `assets/`, `reviews/`, `progress/`, `team/` — di luar scope Winston, akan dibuat saat Phase 2 penuh dijalankan.

---

## 4. Aliran Data (Data Flow)

Tiga aliran paralel yang bertemu di Phase 3:

### 4.1 Aliran A — Kodifikasi

```
5 jpeg Winston
      │  (transkripsi + sintesis)
      ▼
.claude/winston-framework.md          ← single source of truth
      │
      ├──► specs/presentation-design-spec.md   (F1, F3, F4 — deck-level)
      ├──► specs/winston-integration-rules.md  (proses kerja antar fase)
      └──► rubrics/_template.md                (F2, F5 — slide-level)
```

Aliran satu arah, top-down. Revisi Winston hanya boleh dilakukan dengan mengubah `winston-framework.md` lalu mempropagasi turun.

### 4.2 Aliran B — Audit

```
Pelaporan Keuangan Korporat Gr. 3/v5 (1).html   (control sample, tidak disentuh)
                  │
                  ▼
       [Audit Pass berbasis F1–F5]
                  │
                  ├──► analysis/winston-audit/audit-deck-v5.md
                  ├──► analysis/winston-audit/crime-inventory.md
                  ├──► analysis/winston-audit/revision-priorities.md
                  └──► analysis/winston-audit/delivery-checklist.md
```

Audit wajib menyertakan **bukti kutipan/lokasi konkret** di v5. Tidak boleh ada penilaian subjektif tanpa dasar.

### 4.3 Aliran C — Duplikasi

```
v5 (1).html ──── (cp) ────► v6-winston.html  (placeholder)
```

Verifikasi via `md5sum` setelah penyalinan untuk memastikan byte-identik.

### 4.4 Sinkronisasi di Phase 3

Tiga aliran di atas menghasilkan tiga input untuk Phase 3 (`writing-plans`):

1. **Spec Winston** (`specs/*`) → standar yang harus dipenuhi
2. **Audit v5** (`analysis/winston-audit/*`) → defect mana yang harus diperbaiki
3. **Target file** (`v6-winston.html`) → di mana revisi diterapkan

Phase 3 menyatukan ketiganya menjadi rencana eksekusi slide-by-slide.

---

## 5. Penanganan Kasus Tepi (Edge Cases)

### E1 — Konflik Winston vs FASB/Week 5 (Klausul Supremasi FASB)

**Aturan:** Substansi FASB menang. Winston adalah lensa retorika, bukan editor konten akademik. Bila satu framework Winston memaksa pemotongan substansi yang dimandatkan FASB/Week 5, framework itu **diadaptasi** — bukan substansi FASB yang dipotong.

**Contoh:** Winston "satu salient idea" vs FASB "Relevance + Faithful Representation (dua karakteristik fundamental)". Resolusi: satu salient idea untuk *deck* ("Conceptual Framework adalah konstitusi pelaporan keuangan"), tetapi Relevance dan Faithful Representation tetap muncul utuh di slide masing-masing.

### E2 — Pemisahan Design Crimes vs Delivery Crimes

Crime #4 (reading aloud), #6 (speaker distance) tidak dapat diaudit dari file HTML. Dipisahkan ke `delivery-checklist.md` sebagai catatan presenter. Hanya design crimes yang masuk `crime-inventory.md`.

### E3 — Slide Kasus INDF: Angka sebagai Prop

Untuk slide kasus, **angka adalah prop**. Penyajian wajib mengikuti story arc: konteks/ketegangan → demonstrasi (tabel/grafik) → resolusi (interpretasi via FASB). Tabel polos tanpa story arc = crime tambahan khusus slide kasus.

### E4 — Defect HIGH-XL: Diangkat ke Spec, Bukan Patch v6

Bila audit menemukan defect HIGH severity dengan effort XL (mis. font 24pt di seluruh deck), perbaikan tidak terjadi sebagai patch di v6 melainkan menjadi *requirement* untuk Phase 4 build dari nol. Menghindari `v6-winston.html` menjadi tambal-sulam yang tetap inferior.

### E5 — Bahasa: Indonesia (Deck) vs Inggris (Winston)

Sintesis STAR ditulis dwibahasa di `presentation-design-spec.md`. Slogan diuji dalam Bahasa Indonesia (yang akan diucapkan di kelas), dengan terjemahan Inggris di catatan kaki untuk traceability ke Winston asli.

---

## 6. Kriteria Selesai (Acceptance Criteria)

Brainstorm dianggap selesai dan siap diserahkan ke `writing-plans` jika:

### V1 — `.claude/winston-framework.md`
- Kelima framework lengkap: Role, Task, Steps, Rules, Output chain (sesuai persis 5 jpeg).
- Setiap framework berlabel **DECK-LEVEL** atau **SLIDE-LEVEL**.
- Memuat tabel referensi silang framework × fase CLAUDE.md.
- Bebas placeholder.

### V2 — `specs/presentation-design-spec.md`
- Berisi Empowerment Promise deck dalam Bahasa Indonesia, satu kalimat.
- Berisi STAR core idea lengkap (S–T–A–R) dwibahasa per E5.
- Berisi Vision Statement dan rancangan Contributions Close.
- Mendefinisikan pembagian 32 slide ke blok opening (1–3) / proof of work (4–29) / contributions close (30–32).

### V3 — `specs/winston-integration-rules.md`
- Memuat Klausul Supremasi FASB (E1) tegas dan eksplisit.
- Memuat aturan resolusi E2–E5.
- Memetakan setiap framework ke fase CLAUDE.md di mana ia wajib diberlakukan dan ke artefak mana ia wajib muncul.

### V4 — `rubrics/_template.md`
- Memuat front-matter slide standar sesuai `# File Conventions` di CLAUDE.md.
- Memuat checklist 10 design crimes (delivery crimes dipindah).
- Memuat trigger F5 (slide kasus INDF + slide konsep sulit).
- Memuat slot evaluasi STAR-alignment.

### V5 — Audit Deck v5
- `audit-deck-v5.md`: setiap framework dievaluasi terhadap v5 dengan bukti kutipan/lokasi konkret. Mencakup area di mana v5 sudah selaras (bukan hanya defect).
- `crime-inventory.md`: tabel **Slide # | Crime # | Bukti | Severity (HIGH/MED/LOW) | Effort (S/M/L/XL) | Fix yang Diusulkan** untuk seluruh 32 slide. Agregat per kategori untuk eksekutif summary.
- `revision-priorities.md`: tier HIGH/MEDIUM/LOW + flag "needs full redesign, not patch" untuk HIGH-XL.
- `delivery-checklist.md`: seluruh delivery crimes sebagai catatan presenter.

### V6 — `Pelaporan Keuangan Korporat Gr3 v6-winston.html`
- Bytewise identik dengan v5 (verifikasi `md5sum`).
- File pendamping (CSS/JS/asset) tetap dapat diakses dari v6 — tidak ada broken reference.
- Belum ada modifikasi konten Winston.

### V7 — Brainstorm Keseluruhan
- V1–V6 tercentang.
- Spec ini lulus self-review dan disetujui pengguna.
- Semua artefak ter-commit ke git dengan commit message deskriptif.

---

## 7. Apa yang BUKAN Bagian dari Spec Ini

Untuk menghindari scope creep:

- ❌ Implementasi revisi `v6-winston.html` — itu pekerjaan tahap `executing-plans`.
- ❌ Pembuatan `rubrics/slide-01.md … slide-32.md` — itu pekerjaan Phase 3 (`writing-plans`).
- ❌ Phase 1 brainstorming Group 3 deck secara penuh (Visual Companion, dst.) — Winston *memberi bahan* untuk Phase 1, tetapi Phase 1 sendiri adalah brainstorm terpisah.
- ❌ Pembuatan slide HTML baru di `slides/` — itu Phase 4 (`subagent-driven-development`).
- ❌ Modifikasi `sources/group-work-original/` — selamanya read-only per CLAUDE.md.

---

## 8. Langkah Berikutnya

Setelah spec ini disetujui:

1. **`writing-plans`** — menyusun rencana eksekusi terperinci untuk membuat semua artefak yang tercantum di Bagian 3, dalam urutan yang benar (dengan dependensi: misal `winston-framework.md` harus selesai sebelum `_template.md` karena yang kedua merujuk yang pertama).
2. **`executing-plans`** atau **`subagent-driven-development`** — eksekusi rencana, menghasilkan artefak satu per satu dengan checkpoint review.
3. **Verifikasi V1–V7** — sebelum menyatakan integrasi Winston selesai.

Setelah Winston terintegrasi, Phase 1 brainstorming Group 3 deck (per CLAUDE.md) dapat dimulai dengan Winston sebagai lensa default.
