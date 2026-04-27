<!--
slide: 24
role: case
title: "Representasi Tepat INDF — Kelengkapan, Netralitas, Free from Error (Aset Biologis)"
learning_objective: "Audiens dapat mengevaluasi tiga komponen Faithful Representation (Completeness, Neutrality, Free from Error) terhadap pengukuran aset biologis perkebunan INDF dan menyimpulkan apakah laporan INDF 2024 faithfully represents realitas ekonomi aset biologis."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 QC12–QC16 — Faithful Representation: Completeness, Neutrality, Free from Error"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — Agribusiness Group aset biologis; EBIT +73%; PSAK 69 pengukuran"
assigned_to: "TBD"
rubric: rubrics/slide-24.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 24: Representasi Tepat INDF — Kelengkapan, Netralitas, Free from Error

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
> **v5 audit finding:** Tiga card masing-masing berisi 3 bullet points dengan teks 15–20 kata per bullet + limitation bar bawah = estimasi >80 kata visible — Severity MED, Effort L, Fix: Sederhanakan ke 1–2 bullet per card; pindahkan detail ke catatan presenter.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1391–1482: tiga card Kelengkapan/Netralitas/Free from Error menggunakan `font-size:21px` untuk body bullets; limitation bar bawah menggunakan `font-size:21px` dan `font-size:19px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Tiga card setinggi frame utama + limitation bar bawah = >85% frame terisi — Severity MED, Effort M, Fix: Kurangi bullet per card; tambah breathing room.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 24 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 24 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

EBIT Agribusiness INDF +73% di 2024 adalah prop kunci: angka ini mengejutkan dan memerlukan interpretasi FR — apakah kenaikan 73% mencerminkan realitas ekonomi (CPO price premium) atau bias pengukuran (fair value volatility)?

- [ ] **Konteks/Ketegangan:** "EBIT Agribusiness naik 73% di 2024 — apakah
      kenaikan ini mencerminkan realitas ekonomi secara Faithful? Atau apakah
      fair value aset biologis CPO telah 'memperbesar' angka laba yang
      sebenarnya lebih moderat?"
- [ ] **Demonstrasi:** Tiga komponen FR (Completeness, Neutrality, Free from
      Error) dievaluasi terhadap pengukuran aset biologis INDF: Completeness
      (disclosure metode PSAK 69); Neutrality (tidak ada bukti manajemen
      memilih asumsi yang menguntungkan); Free from Error (auditor memberikan
      opini WTP).
- [ ] **Resolusi:** Interpretasi: laporan INDF 2024 secara substansial faithfully
      represents aset biologis — Completeness terpenuhi via catatan PSAK 69;
      Neutrality terpenuhi (EBIT +73% didukung data harga CPO eksternal);
      Free from Error terpenuhi (WTP opinion).
- [ ] **Per E3:** Tiga card FR tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** APPLICABLE — EBIT +73% sebagai angka yang tampak mencurigakan
      tetapi ternyata faithfully represents realitas ekonomi CPO adalah
      mini-Surprise yang harus dieksploitasi.
- [ ] **Salient idea:** APPLICABLE — uji Faithful Representation adalah inti
      dari Salient Idea: informasi yang benar-benar berguna harus faithfully
      represent realitas ekonomi.
- [ ] **Story:** APPLICABLE — slide 24 adalah node "uji Faithful Representation"
      dalam arc.

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
