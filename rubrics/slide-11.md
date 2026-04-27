<!--
slide: 11
role: table
title: "Sepuluh Elemen Laporan Keuangan — SFAC 6"
learning_objective: "Audiens dapat menyebutkan 10 elemen laporan keuangan menurut SFAC 6 dan membedakan tiga elemen posisi keuangan (Assets, Liabilities, Equity) dari tujuh elemen kinerja (Revenues, Expenses, Gains, Losses, CI, OCI, Investment/Distribution)."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 6 — definisi 10 elemen laporan keuangan"
  - doc: week-05-materials
    ref: "Week 5 Exercise — elemen laporan keuangan SFAC 6"
assigned_to: "TBD"
rubric: rubrics/slide-11.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 11: Sepuluh Elemen Laporan Keuangan — SFAC 6

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
> **v5 audit finding:** Tabel 10 elemen (seluruh slide) + heading "Sepuluh Elemen Laporan Keuangan" + lead text = tabel 10 baris × 5 kolom = estimasi >50 kata visible; tabel sangat dense — Severity MED, Effort M, Fix: Sederhanakan ke 4–5 elemen kunci; gunakan visual card bukan tabel penuh.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 588–617: tabel 10 elemen menggunakan `.tbl` dengan `font-size:18px` untuk td (line 87: `.tbl td{font-size:18px}`) dan `font-size:14px` untuk th — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Tabel penuh seluruh slide hampir tanpa whitespace; hanya judul dan tabel — Severity MED, Effort M, Fix: Hilangkan 5 elemen minor; tambah whitespace di sekitar tabel.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 11 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 11 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Sepuluh elemen laporan keuangan adalah kerangka definitif yang menentukan apa yang boleh masuk ke laporan keuangan — bukan sekadar daftar, tetapi sistem klasifikasi dengan konsekuensi pengakuan yang besar (mis. apakah goodwill INDF Rp52,2T adalah Assets per definisi SFAC 6 atau bukan).

- [ ] **Konteks/Ketegangan:** "Mengapa kita perlu 10 kategori elemen — bukan
      cukup 5 (aset, liabilitas, ekuitas, pendapatan, beban)? Apa yang
      hilang jika CI dan OCI tidak didefinisikan secara terpisah?"
- [ ] **Demonstrasi:** Tabel 10 elemen disajikan dengan definisi singkat per
      elemen dan referensi SFAC 6; disorot elemen yang paling relevan untuk
      kasus INDF (Assets → goodwill; CI → laba komprehensif segmen).
- [ ] **Resolusi:** Interpretasi: 10 elemen memastikan bahwa setiap jenis
      perubahan posisi keuangan dikategorikan dengan tepat — CI dan OCI
      memisahkan kinerja operasional dari volatilitas akuntansi.
- [ ] **Per E3:** Tabel 10 elemen tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — definisi elemen adalah prasyarat untuk
      mengevaluasi apakah laporan INDF menghasilkan informasi yang berguna.
- [ ] **Story:** APPLICABLE — slide 11 adalah node "definisi elemen" dalam arc.

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
