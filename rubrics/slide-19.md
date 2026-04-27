<!--
slide: 19
role: content
title: "Diagram Master SFAC 8 — Arsitektur Lengkap 8 Chapter"
learning_objective: "Audiens dapat menggambarkan arsitektur SFAC 8 sebagai sistem terintegrasi delapan chapter dan menjelaskan mengapa urutan chapter (Objectives → QC → Elements → Recognition → Measurement → Presentation → Notes) mencerminkan hierarki keputusan pelaporan keuangan."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 1–8 — arsitektur kerangka konseptual lengkap"
  - doc: week-05-materials
    ref: "Week 5 Exercise — SFAC 8 overview"
assigned_to: "TBD"
rubric: rubrics/slide-19.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 19: Diagram Master SFAC 8 — Arsitektur Lengkap 8 Chapter

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
> **v5 audit finding:** Slide 19 "Diagram Master SFAC 8" merangkum semua 8 chapter SFAC 8 dalam satu slide; slide ini redundan sebagian dengan slide 03 (sejarah SFAC) yang sudah memuat tabel kronologis SFAC 1–8. Sisanya adalah elaborasi yang sudah ada di slide 04–18 — Severity LOW, Effort M, Fix: Pertahankan jika berfungsi sebagai synthesis visual; hapus jika dianggap redundan dengan tabel slide 03. Klarifikasi tujuan berbeda: slide 03 = kronologi, slide 19 = arsitektur.

- [ ] **Crime #2 — Too many words:** Jumlah kata di body slide ≤25 kata.
      Kalimat berlebih dipindahkan ke catatan presenter, bukan dihapus.
> **v5 audit finding:** Grid 4×2 cards (8 chapter cards masing-masing dengan judul + 2–3 kalimat deskripsi) + timeline narasi bawah = estimasi >120 kata visible — Severity HIGH, Effort L, Fix: Pisahkan ke 2 slide: (a) Ch.1–4, (b) Ch.5–8 + timeline.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 942–964: delapan chapter cards menggunakan `font-size:20px` heading dan `font-size:19px` body; timeline bar bawah menggunakan `font-size:20px` untuk milestone labels — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Grid 4 kolom × 2 baris (8 cards) + timeline bar bawah = frame hampir penuh — Severity HIGH, Effort L, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 19 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 19 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Slide 19 adalah slide sintesis teori — merangkum arsitektur 8 chapter SFAC 8 sebagai satu sistem. Memahami SFAC 8 sebagai "sistem terintegrasi" (bukan 8 dokumen terpisah) adalah konsep sulit yang memerlukan story arc.

- [ ] **Konteks/Ketegangan:** "Kita telah mengkaji 8 chapter SFAC 8 secara
      individual — tetapi apakah mereka benar-benar terintegrasi? Atau hanya
      8 dokumen yang dikompilasi? Arsitektur ini menentukan apakah Framework
      benar-benar berfungsi sebagai 'konstitusi'."
- [ ] **Demonstrasi:** Delapan chapter disajikan sebagai sistem bertingkat
      dengan arah aliran (Objectives → QC → Elements → Recognition →
      Measurement → Presentation → Notes → Disclosure) dengan referensi SFAC 8.
- [ ] **Resolusi:** Interpretasi: SFAC 8 adalah sistem hierarkis — setiap
      keputusan pelaporan INDF dimulai dari tujuan (OB), difilter oleh QC,
      dikategorikan dalam elemen, dan akhirnya disajikan. Tidak ada keputusan
      yang melewati langkah dalam hierarki ini.
- [ ] **Per E3:** Grid 8 chapter tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** APPLICABLE — slide 19 adalah lokasi yang tepat untuk
      memperkuat Symbol bangunan tiga lantai sebagai visual representasi
      arsitektur SFAC 8 (fondasi = Objectives; tiang = QC; atap = FS).
- [ ] **Slogan:** **APPLICABLE dan WAJIB** — per `specs/presentation-design-spec.md`
      bagian 2, slide 19 adalah lokasi kemunculan Slogan ketiga:
      "Conceptual Framework: konstitusi laporan keuangan." Verifikasi bahwa
      Slogan hadir di slide ini sebagai transisi ke studi kasus INDF.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — arsitektur SFAC 8 sebagai sistem adalah
      inti dari Salient Idea: Framework bukan kumpulan aturan, melainkan
      konstitusi hierarkis.
- [ ] **Story:** APPLICABLE — slide 19 adalah node transisi "dari teori ke
      kasus" dalam arc.

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
