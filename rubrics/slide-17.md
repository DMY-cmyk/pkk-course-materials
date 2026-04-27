<!--
slide: 17
role: content
title: "Penyajian — SFAC 8 Ch. 7 (PR12) + OCI Rekonsiliasi + BC7.21"
learning_objective: "Audiens dapat menjelaskan prinsip penyajian SFAC 8 Ch. 7 PR12 dan menginterpretasikan implikasi BC7.21 terhadap cara INDF menyajikan Comprehensive Income dengan rekonsiliasi OCI."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 7, PR12 — presentation principles; BC7.21 — Basis for Conclusions penyajian CI"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — penyajian Comprehensive Income dan rekonsiliasi OCI"
assigned_to: "TBD"
rubric: rubrics/slide-17.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 17: Penyajian — SFAC 8 Ch. 7 (PR12) + OCI Rekonsiliasi + BC7.21

---

## 1. Front-Matter Compliance

- [ ] Front-matter HTML comment lengkap sesuai CLAUDE.md `# File Conventions`
- [ ] `role` dipilih dari enum yang valid: `cover`, `agenda`, `section-divider`,
      `content`, `case`, `chart`, `table`, `quote`, `synthesis`, atau `qanda`
- [ ] `learning_objective` satu kalimat, dapat diuji (bukan sekadar "memahami X")
- [ ] `sources` mengutip FASB CF / INDF AR / Week 5 / Wolk / Scott — tidak fabrikasi

---

## 2. F2 Design Crimes Checklist (per E2 — delivery crimes excluded)

> Referensi: `.claude/winston-framework.md` bagian F2 — The 10 Slide Crimes.
> Hanya 7 design crimes yang tercantum di sini (Crimes #1, #2, #3, #7, #8, #9, #10).
> Crimes #4 (reading aloud), #5 (laser pointer), #6 (speaker distance)
> dipindah ke `analysis/winston-audit/delivery-checklist.md` per E2.

- [ ] **Crime #1 — Too many slides:** Slide ini perlu secara mandiri? Jika
      substansi sudah ada di slide tetangga, gabung. Setiap slide harus
      memiliki satu ide tunggal yang tidak dapat disatukan dengan slide lain
      tanpa kehilangan kejelasan.
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #2 — Too many words:** Jumlah kata di body slide ≤25 kata.
      Kalimat berlebih dipindahkan ke catatan presenter, bukan dihapus.
> **v5 audit finding:** Kolom kiri: hierarki FS (2 level) + box PR12 + OCI rekonsiliasi; kolom kanan: box BC7.21 + implikasi INDF = estimasi >80 kata visible — Severity MED, Effort L, Fix: Pisahkan BC7.21 ke slide terpisah; pertahankan hierarki FS dan OCI di slide 17.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 857–884: teks hierarki laporan keuangan menggunakan `font-size:21px`, `font-size:20px`, `font-size:19px`; OCI waterfall menggunakan `font-size:20px` dan `font-size:19px`; box BC7.21 menggunakan `font-size:21px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Dua kolom masing-masing sangat padat; kolom kiri 3 card bertumpuk dengan OCI waterfall — Severity MED, Effort M, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 17 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 17 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Prinsip penyajian SFAC 8 Ch. 7 dan BC7.21 adalah konsep sulit: mengapa FASB memisahkan penyajian (presentation) dari pengakuan (recognition) sebagai chapter terpisah, dan bagaimana PR12 menentukan di mana dalam laporan keuangan sebuah item harus ditampilkan.

- [ ] **Konteks/Ketegangan:** "Goodwill INDF sudah 'diakui' sebagai Aset —
      tetapi di baris mana di neraca ia harus disajikan? Dan mengapa OCI
      disajikan dalam laporan terpisah dari Net Income? Penyajian yang berbeda
      menghasilkan persepsi kinerja yang berbeda bagi investor."
- [ ] **Demonstrasi:** Hierarki laporan keuangan INDF (face vs notes) disajikan
      dengan referensi PR12; OCI rekonsiliasi ditampilkan dengan komponen
      spesifik dari INDF AR 2024; BC7.21 dikutip dengan referensi paragraph.
- [ ] **Resolusi:** Interpretasi: pemisahan CI menjadi Net Income + OCI dalam
      penyajian meningkatkan Disaggregasi — audiens dapat menilai kinerja
      operasional inti (Net Income) terpisah dari perubahan nilai unrealized (OCI).
- [ ] **Per E3:** Hierarki FS tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — penyajian yang tepat adalah elemen akhir
      dari rantai informasi berguna bagi pengambil keputusan.
- [ ] **Story:** APPLICABLE — slide 17 adalah node "prinsip penyajian" dalam arc.

---

## 5. FASB Supremacy Verifikasi (E1)

> Referensi: `specs/winston-integration-rules.md` bagian E1 — Klausul
> Supremasi FASB (TEGAS). Substansi FASB SELALU menang atas Winston.

- [ ] Substansi FASB di slide ini tidak dikorbankan demi gaya Winston.
      Definisi, komponen, dan contoh kasus FASB yang dimandatkan tampil
      utuh — tidak dipersingkat untuk memenuhi batas kata Winston.
- [ ] Bila ada konflik yang terdeteksi (mis. F2 Crime #2 ≤25 kata vs
      definisi FASB yang lebih panjang): definisi FASB tetap utuh dan
      resolusi telah diterapkan. Resolusi wajib dicatat secara eksplisit
      di rubrik slide ini.

---

## 6. Sumber & Traceability

- [ ] Setiap klaim numerik (angka dari INDF AR 2024) mengutip nomor
      halaman atau lokasi spesifik di Annual Report.
- [ ] Setiap klaim konseptual (dari FASB CF, Wolk, Scott, atau Week 5)
      mengutip chapter, halaman, atau nomor paragraf.
- [ ] Tidak ada angka fabrikasi (per CLAUDE.md aturan #3: "Never fabricate
      data. If INDF AR does not contain a figure, say so.").

---

## 7. Tanda Tangan Reviewer

- Reviewer 1 (peer): __________ tanggal __________
- Reviewer 2 (final): __________ tanggal __________
