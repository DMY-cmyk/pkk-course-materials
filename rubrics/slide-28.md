<!--
slide: 28
role: table
title: "Pengukuran Model Campuran INDF — Peta Pengukuran + Matriks Relevansi vs Verifikasi"
learning_objective: "Audiens dapat mengklasifikasikan minimal empat jenis aset/liabilitas INDF ke dalam atribut pengukuran yang digunakan (historical cost, fair value, present value) dan mengevaluasi posisinya dalam matriks Relevansi vs Verifikasi."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 6, M30–M34 — Entry/Exit price; SFAC 5 — lima atribut pengukuran"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — peta pengukuran: aset tetap (historical cost), aset biologis (fair value PSAK 69), goodwill (historical cost − impairment)"
assigned_to: "TBD"
rubric: rubrics/slide-28.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 28: Pengukuran Model Campuran INDF — Peta Pengukuran + Matriks

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
> **v5 audit finding:** Tabel 6 baris × 4 kolom (Peta Pengukuran) + matriks 2×2 Relevansi vs Verifikasi + box keterbatasan goodwill = estimasi >80 kata visible — Severity HIGH, Effort L, Fix: Pisahkan tabel (slide 28a) dari matriks 2×2 (slide 28b); hapus box keterbatasan atau pindahkan ke catatan.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1787–1874: tabel "Peta Pengukuran" menggunakan `.tbl` dengan `font-size:12px` th dan `font-size:14px` td (sangat sub-40pt); matriks 2×2 menggunakan `font-size:14px` dan `font-size:18px`; limitation box menggunakan `font-size:17px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Kolom kiri tabel besar 6 baris + kolom kanan matriks 2×2 + box bawah = frame hampir penuh — Severity HIGH, Effort L, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 28 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 28 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

Peta pengukuran INDF adalah prop yang memvisualkan mixed-attribute model secara konkret: mengapa satu perusahaan menggunakan empat basis pengukuran berbeda untuk jenis aset berbeda? Matriks Relevansi vs Verifikasi adalah alat analitis untuk mengevaluasi trade-off.

- [ ] **Konteks/Ketegangan:** "INDF menggunakan setidaknya tiga basis
      pengukuran berbeda dalam satu laporan keuangan: historical cost (aset
      tetap), fair value (aset biologis), dan impairment-adjusted cost
      (goodwill). Apakah ini inkonsistensi yang membingungkan investor,
      atau justru pilihan optimal per jenis aset?"
- [ ] **Demonstrasi:** Peta pengukuran 6 jenis aset/liabilitas INDF dengan
      basis pengukuran dan referensi halaman INDF AR 2024; matriks 2×2
      menunjukkan posisi trade-off Relevansi vs Verifikasi untuk masing-masing.
- [ ] **Resolusi:** Interpretasi: mixed-attribute model INDF konsisten dengan
      SFAC 5 dan SFAC 8 Ch. 6 — setiap pilihan basis pengukuran dapat
      dijustifikasi berdasarkan trade-off QC yang berbeda per jenis aset.
      Bukan inkonsistensi, melainkan judgment yang informed.
- [ ] **Per E3:** Tabel pengukuran tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — mixed-attribute model sebagai judgment
      optimal mendemonstrasikan Salient Idea secara konkret.
- [ ] **Story:** APPLICABLE — slide 28 adalah node "uji pengukuran" dalam arc.

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
