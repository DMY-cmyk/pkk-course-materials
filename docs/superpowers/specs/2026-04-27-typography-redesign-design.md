# Typography Redesign untuk `v6-winston.html` — Design Spec

**Tanggal:** 2026-04-27
**Status:** APPROVED — disetujui pengguna pada 2026-04-27 setelah lima ronde brainstorming.
**Cakupan:** Brainstorm-only. Implementasi (Fase 1 token substitution + Fase 2 per-slide reflow) bukan bagian dari spec ini; itu pekerjaan `writing-plans` → execution di tahap berikutnya.
**Bahasa:** Bahasa Indonesia formal akademik.
**Konteks:** Lanjutan dari spec Winston Integration (`2026-04-27-winston-integration-design.md`) yang men-flag 32 entries Crime #3 (font <40pt sistemik) sebagai HIGH-XL → redesign Phase 4 per E4. Spec ini adalah operasionalisasi redesain itu.

---

## 1. Latar Belakang & Tujuan

Audit Winston Phase 1 (`analysis/winston-audit/crime-inventory.md`) menemukan bahwa 97.6% deklarasi `font-size` di v5 deck (`Pelaporan Keuangan Korporat Gr3 v5 (1).html` lines 28-38) berada di bawah ambang batas Winston 40pt (≈53px CSS pada canvas 1920×1080). Ini bukan defect lokal melainkan **systemic typography choice** yang per E4 wajib di-redesign, bukan di-patch.

Tujuan: tingkatkan tipografi v6 ke **Strict-Content level** (body/lead/heading ≥53px; caption/label/meta diizinkan 28-36px) dengan implementasi root-level token replacement plus per-slide reflow yang mendapat persetujuan eksplisit pengguna untuk setiap slide.

---

## 2. Filosofi: Operasi Dua-Fase

Redesain ini dipecah menjadi dua fase berurutan dengan karakter berbeda:

### Fase 1 — Token Substitution (otomatis, sekali)

Edit blok CSS di lines 28-38 `v6-winston.html`. Ganti 12 definisi token (`.t-h1` … `.t-caption`) ke skala Balanced (lihat Bagian 3). Satu commit. Setelah Fase 1, sebagian besar slide overflow karena density lama dirancang untuk 22px body — file secara teknis "broken" sampai Fase 2 selesai. Ini **expected behavior**, bukan bug (per E6 di Bagian 5).

### Fase 2 — Per-Slide Reflow (manual, 32 iterasi dengan gate persetujuan)

Untuk setiap slide N (01-32), siklus enam langkah:

1. Baca slide N dari v6 (post-Fase-1, overflow state).
2. Identifikasi crime audit T6 untuk slide N (Crime #2 too-many-words, #3 font, #7 white-space).
3. Tentukan strategi sesuai Hybrid policy: split-first (slide 4-29 teori+kasus) atau cut-first (slide 1-3, 30-32 opening+close).
4. Bangun mockup HTML BEFORE/AFTER, push ke Visual Companion server.
5. Pengguna review di browser, klik **Approve** atau beri revisi (kembali ke step 4 dengan v2/v3).
6. Setelah approve: apply edit aktual ke v6.html, append entry ke `reflow-log.md`, commit individual.

**Karakteristik:**
- **Sinkron, bukan paralel.** Tidak kerjakan slide N+1 sebelum N approved.
- **Audit-trail mandatori.** Setiap approve tercatat dengan timestamp + commit SHA.
- **Reversibility per slide.** Setiap slide = 1 commit, bisa direvert individual.
- **Estimasi:** 5-10 menit per slide × 32 = 3-6 jam interaksi.

---

## 3. Skala Tipografi — Balanced

Token system v6 setelah Fase 1:

| Token | v5 (px) | v6 (px) | Kelas | Compliance |
|-------|---------|---------|-------|------------|
| `.t-h1` | 96 | **110** | DECK heading | ≥40pt ✓ |
| `.t-h2` | 68 | **84** | DECK heading | ≥40pt ✓ |
| `.t-h3` | 48 | **68** | DECK heading | ≥40pt ✓ |
| `.t-h4` | 34 ✗ | **60** | DECK heading | ≥40pt ✓ |
| `.t-h5` | 26 ✗ | **53** | DECK heading | ≥40pt ✓ |
| `.t-lead` | 26 ✗ | **60** | Subtitle/lead | ≥40pt ✓ |
| `.t-body` | 22 ✗ | **53** | Body | ≥40pt ✓ |
| `.t-body-dark` | 22 ✗ | **53** | Body (dark on light) | ≥40pt ✓ |
| `.t-body-sm` | 18 ✗ | **36** | Body small (cap) | <40pt — caption tier |
| `.t-meta` | 16 ✗ | **28** | Metadata (cap) | <40pt — metadata tier |
| `.t-label` | 13 ✗ | **28** | Uppercase label (cap) | <40pt — label tier |
| `.t-caption` | 18 ✗ | **36** | Caption (cap) | <40pt — caption tier |

**Hierarchy spread (Balanced):** h1 = 2.07× body, h2 = 1.58× body, h3 = 1.28× body, h4 = 1.13× body, h5 = body. Audiens dapat membedakan struktur tanpa squinting.

**Property non-tipografi (color, font-weight, letter-spacing) TIDAK diubah.** Hanya `font-size` dan optional `line-height` (line-height baru: 1.05 untuk h1-h2, 1.1-1.15 untuk h3-h5, 1.25-1.3 untuk body/lead).

---

## 4. Komponen yang Dibuat/Dimodifikasi

| Path | Aksi | Tanggung jawab |
|------|------|----------------|
| `specs/typography-tokens.md` | BARU | Definisi resmi 12 token Balanced + line-height + spacing rules. Single source of truth Fase 1. |
| `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html` | DIMODIFIKASI | Lines 28-38 (Fase 1) + lines 40-2223 (Fase 2 per-slide reflow). v5 tidak disentuh. |
| `analysis/winston-audit/reflow-log.md` | BARU | Audit trail per-slide: BEFORE state, AFTER decision, exception flags, approval timestamp, commit SHA. |
| `.superpowers/brainstorm/<session>/content/slide-NN-review-vK.html` | BARU per slide | Mockup BEFORE/AFTER untuk review browser. Tidak di-commit (gitignored via `.superpowers/`). |

**Yang TIDAK dibuat di scope ini:**
- Modifikasi konten substansi FASB/INDF (out-of-scope; itu option b yang ditunda).
- Slide rubrik baru (sudah ada di master).
- Brand color / spacing / illustration changes.
- Update `presentation-design-spec.md` slide block structure (V4 di Bagian 6 mengangkatnya sebagai out-of-scope; akan di-flag di reflow-log akhir).

---

## 5. Aturan Resolusi Kasus Tepi

### E1 — Slide tidak muat bahkan setelah split
Pecah lebih lanjut. Tidak ada batas atas split. Lebih baik 4 slide bersih daripada 2 slide overflow. Reviewer Phase 4 boleh menolak slide overflow apa pun jumlahnya.

**Eksepsi:** Tabel agregat (mis. Financial Highlights INDF 5-tahun × 8-row) yang secara substantif tidak dapat dipecah tanpa kehilangan makna komparatif → diizinkan menggunakan body-sm (36px) dengan flag eksplisit di reflow-log: `EXCEPTION: tabel-agregat`. Bukan default; harus dibenarkan.

### E2 — Konten v5 tidak ditemukan / dirombak total
**STOP. Jangan perbaiki data.** Itu out-of-scope (option b yang ditunda). Catat di reflow-log: `CONTENT-DRIFT: line X claim Y, perlu verifikasi terpisah`. Slide tetap di-reflow dengan content existing, tapi flag dihormati.

### E3 — Symbol/Slogan/STAR conflict dengan reflow
Slide 02/07/19/30 wajib menampilkan Slogan deck (per `presentation-design-spec.md`). Slogan adalah heading atau lead text — wajib ≥60px (lead) atau ≥84px (h2). Jika reflow membuat slot tidak cukup untuk slogan + content, content yang dipangkas (atau split lagi). Slogan tidak boleh shrink ke caption-tier.

### E4 — Brand color / spacing tidak sengaja terganggu
Edit hanya `font-size` dan `line-height` per token. Property lain (`color`, `font-weight`, `letter-spacing`) tetap. Verify dengan `git diff` per slide → tidak boleh ada perubahan di property non-tipografi kecuali secara eksplisit di-approve.

### E5 — Pengguna mengubah pikiran di tengah loop
**OK, dukung.** Catat perubahan di reflow-log section "MID-COURSE CORRECTION", apply revised approach untuk slide selanjutnya. Slide yang sudah ter-reflow tetap; jika pengguna mau retrofit, itu loop kedua (estimasi 2-4 jam tambahan).

### E6 — Token Substitution (Fase 1) merusak slide rendering secara fundamental
Itu **expected behavior**, bukan bug. Fase 1 secara intentional meninggalkan v6 dalam state "broken" sampai Fase 2 selesai. Jangan rollback Fase 1. v5 tetap utuh sebagai control sample — tetapi v5 **tidak boleh dibuka di browser sebagai standar visual** selama Fase 2 berjalan; perbandingan visual hanya via mockup yang di-approve.

---

## 6. Verifikasi & Kriteria Selesai

### V1 — Fase 1 (Token Substitution)

Selesai jika:
- Lines 28-38 v6.html berisi 12 token sesuai Bagian 3 (`.t-h1`=110, `.t-h2`=84, `.t-h3`=68, `.t-h4`=60, `.t-h5`=53, `.t-lead`=60, `.t-body`=53, `.t-body-dark`=53, `.t-body-sm`=36, `.t-meta`=28, `.t-label`=28, `.t-caption`=36).
- `git diff` menunjukkan HANYA `font-size` dan optional `line-height` berubah (tidak ada color/weight/padding tersentuh).
- Commit: `feat(deck): apply Winston typography token substitution (Phase 1)`.

### V2 — Fase 2 per slide (32 iterasi)

Selesai PER SLIDE jika:
- Mockup BEFORE/AFTER di-push, pengguna approve.
- Edit aktual ke v6.html sesuai approved mockup.
- `reflow-log.md` berisi entry: `| NN | strategi (split-K / cut) | exception | timestamp | commit SHA |`.
- Commit individual: `feat(deck): slide NN winston reflow (split→K slides | cut)`.

Selesai SECARA KESELURUHAN (32 slide) jika:
- 32 entry di reflow-log.
- 32 commit individual.
- `grep -c '\.t-body[^-]' v6.html` ≥ count v5 baseline.

### V3 — Audit Crime #3 v6 final

Selesai jika:
- Tidak ada `font-size` < 36px di body deck (footer/citation diizinkan jika di-approve).
- Tidak ada `font-size` < 53px untuk text dengan class `.t-body`, `.t-lead`, `.t-h1`…`.t-h5`.
- Grep verification: `grep -E 'font-size:\s*(1[0-9]|2[0-9]|3[0-5])px' v6.html` → output hanya inline footer/citation/badge yang sudah ter-approve sebagai exception.

### V4 — Total Slide Deck v6

Selesai jika:
- Total slide v6 dihitung (32 → ~38-45 expected).
- **OUT-OF-SCOPE:** Update `presentation-design-spec.md` block structure NOT dilakukan di sesi ini. Akan di-flag di reflow-log akhir bahwa update ini diperlukan di sesi terpisah.

### V5 — Audit Trail

`reflow-log.md` selesai jika:
- Header dengan timestamp Fase 1 commit + Fase 2 start.
- Tabel 32 entry per slide.
- Section "Exceptions" merangkum slide dengan exception flag.
- Section "Mid-course corrections" jika ada.
- Section "Out-of-scope flags" mencatat presentation-design-spec.md update yang diperlukan.

### V6 — Brainstorm Keseluruhan

Sesi ini siap diserahkan ke `writing-plans` jika:
- Spec ini ditulis lengkap, lulus self-review, di-approve pengguna.
- Tidak ada placeholder/kontradiksi/ambiguitas.

---

## 7. Apa yang BUKAN Bagian dari Spec Ini

- ❌ Implementasi Fase 1 dan Fase 2 — itu pekerjaan `writing-plans` → execution.
- ❌ Modifikasi konten substansi FASB/INDF (option b yang ditunda).
- ❌ Update `presentation-design-spec.md` block structure setelah deck membengkak.
- ❌ Brand color / spacing / illustration changes — murni typography.
- ❌ Modifikasi v5 (1).html — selamanya control sample.
- ❌ Test harness / runtime testing — deck adalah HTML statis; verifikasi murni visual + grep + persetujuan pengguna.

---

## 8. Langkah Berikutnya

Setelah spec ini disetujui:

1. **`writing-plans`** — menyusun rencana eksekusi terperinci. Plan akan memuat:
   - Task A: Tulis `specs/typography-tokens.md` (single source of truth).
   - Task B: Fase 1 — root-level token substitution di v6.html.
   - Task C–AH (32 task): Fase 2 per-slide reflow, masing-masing dengan loop mockup → approve → edit → commit.
   - Task AI: Finalisasi reflow-log.md.
   - Task AJ: Final V3 grep verification.

2. **Eksekusi** — manual loop dengan Visual Companion. Tidak otomatis dapat di-dispatch ke subagent karena membutuhkan persetujuan pengguna per slide.

3. **Verifikasi V1-V6** — sebelum menyatakan typography redesign selesai.

Setelah typography stabil, sesi terpisah brainstorm option (b) — content revision — dapat dimulai dengan v6 typography yang sudah Winston-compliant sebagai fondasi.
