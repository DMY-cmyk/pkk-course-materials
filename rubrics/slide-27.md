<!--
slide: 27
role: case
title: "Pengakuan INDF — Tiga Kasus Kompleks (Goodwill Rp12,8T, PSAK 72, Related Party Rp10,11T)"
learning_objective: "Audiens dapat menerapkan kriteria pengakuan RD3 (SFAC 8 Ch. 5) pada tiga kasus konkret INDF (pengakuan goodwill akuisisi Rp12,8T, pengakuan pendapatan PSAK 72 lima langkah, pengakuan transaksi pihak berelasi Rp10,11T) dan menentukan apakah masing-masing memenuhi kriteria."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 5, RD3 — recognition criteria; BC4.7 — recognition vs disclosure"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — goodwill akuisisi Rp12,8T; PSAK 72 revenue recognition; related party transactions Rp10,11T"
assigned_to: "TBD"
rubric: rubrics/slide-27.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 27: Pengakuan INDF — Tiga Kasus Kompleks

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
> **v5 audit finding:** RD3 banner (line 1694–1697) + tiga case card masing-masing berisi tabel 3-baris + keterangan bawah = estimasi >80 kata visible — Severity MED, Effort L, Fix: Sederhanakan setiap case card ke 1 klaim utama + angka kunci; pertahankan RD3 banner.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1694–1769: tiga case cards menggunakan `font-size:24px` heading, `font-size:17px` untuk isi tabel dan bullet; RD3 banner menggunakan `font-size:19px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** RD3 banner + grid 3 kolom case card setinggi frame = >85% frame terisi — Severity MED, Effort M, Fix: Kurangi isi per card; tambah spacing.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 27 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 27 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

Per audit-deck-v5.md F5: "Slide 27 (Recognition Cases) menggunakan struktur tiga kolom dengan tiga 'kasus' — goodwill Rp12,8T, PSAK 72 lima-langkah, dan related party Rp10,11T. Setiap kolom berisi judul + tabel angka + keterangan. Ini mendekati struktur F5... tetapi ketegangan (tension) tidak diartikulasikan: mengapa kasus ini sulit?"

- [ ] **Konteks/Ketegangan:** "Tiga transaksi yang tampak sederhana — tetapi
      masing-masing memunculkan pertanyaan pengakuan yang kompleks: kapan
      goodwill diakui? kapan pendapatan INDF dari kontrak jangka panjang
      diakui? apakah transaksi dengan pihak berelasi diakui pada nilai pasar
      atau harga internal?"
- [ ] **Demonstrasi:** Tiga kasus disajikan dengan angka konkret dari INDF
      AR 2024; RD3 dikutip dengan referensi paragraf; setiap kasus diuji
      terhadap kriteria recognition.
- [ ] **Resolusi:** Interpretasi: ketiga kasus memenuhi RD3 dengan penjelasan
      berbeda per kasus; implikasi Comparability disinggung (apakah metode
      pengakuan INDF konsisten lintas tahun dan dengan peers?).
- [ ] **Per E3:** Tiga kolom kasus tanpa konteks/ketegangan = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — tiga kasus recognition langsung
      mendemonstrasikan Salient Idea: Framework sebagai alat operasional nyata.
- [ ] **Story:** APPLICABLE — slide 27 adalah node "uji pengakuan" dalam arc.

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
