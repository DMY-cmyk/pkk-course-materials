<!--
slide: 26
role: case
title: "Liabilitas dan Ekuitas INDF — Uji Definisi SFAC 8 Ch. 4 (Rp70,81T + Rp43,08T NCI)"
learning_objective: "Audiens dapat menerapkan definisi Liabilitas SFAC 8 Ch. 4 pada funded debt INDF Rp70,81T dan mengevaluasi penyajian Non-Controlling Interest Rp43,08T dalam ekuitas konsolidasi sebagai implikasi dari definisi entitas pelapor RE8–9."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 4 — definisi Liabilitas (present obligation, economic sacrifice); RE8–9 — NCI dalam konsolidasi"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 pp. 32–33 — total liabilitas, funded debt Rp70,81T; NCI Rp43,077T; retained earnings"
assigned_to: "TBD"
rubric: rubrics/slide-26.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 26: Liabilitas dan Ekuitas INDF — Uji Definisi SFAC 8 Ch. 4

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
> **v5 audit finding:** Panel liabilitas: definisi + tabel komponen Rp70,81T + obligasi USD; panel ekuitas: definisi + NCI Rp43,077T + retained earnings = estimasi >70 kata visible — Severity MED, Effort M, Fix: Sederhanakan ke angka kunci + 1 kalimat interpretasi per panel.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1600–1679: dua panel liabilitas + ekuitas menggunakan `font-size:20px` untuk body text, `font-size:21px` italic untuk kutipan definisi; tabel komponen liabilitas menggunakan font sub-40pt — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Dua panel besar masing-masing berisi definisi + tabel + stats = >80% frame — Severity MED, Effort M, Fix: Sederhanakan; hapus tabel detail, pertahankan stats utama.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 26 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 26 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

Funded debt Rp70,81T adalah liabilitas yang memerlukan uji definisi SFAC 8 Ch. 4. NCI Rp43,08T adalah elemen ekuitas yang mencerminkan kepemilikan minoritas — konsep yang tidak intuitif dalam laporan konsolidasi.

- [ ] **Konteks/Ketegangan:** "INDF memiliki utang Rp70,81T — dan Rp43,08T
      dari 'ekuitas' sebenarnya bukan milik pemegang saham INDF, melainkan
      pemilik minoritas anak perusahaan. Apakah angka-angka ini faithfully
      represent struktur keuangan INDF, atau menyesatkan investor?"
- [ ] **Demonstrasi:** Definisi Liabilitas SFAC 8 Ch. 4 diterapkan pada
      komponen funded debt (obligasi USD, pinjaman bank); NCI dijelaskan
      dengan referensi RE8–9 dan data INDF AR 2024 pp. 32–33.
- [ ] **Resolusi:** Interpretasi: funded debt INDF memenuhi definisi Liabilitas
      (present obligation untuk mentransfer economic resource); NCI dalam ekuitas
      konsolidasi adalah konsekuensi tepat dari definisi entitas pelapor RE8–9 —
      bukan penyesatan, melainkan persyaratan Completeness.
- [ ] **Per E3:** Dua panel definisi + angka tanpa konteks/ketegangan dan
      resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — uji definisi liabilitas dan ekuitas
      menguatkan Salient Idea: Framework adalah standar operasional, bukan teori.
- [ ] **Story:** APPLICABLE — slide 26 adalah node "uji definisi liabilitas
      dan ekuitas" dalam arc.

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
