<!--
slide: 10
role: content
title: "Enhancing Qualitative Characteristics + Cost Constraint (QC19–QC39)"
learning_objective: "Audiens dapat menyebutkan empat Enhancing QC (Comparability, Verifiability, Timeliness, Understandability), menjelaskan perbedaannya dari Fundamental QC, dan menerapkan Cost Constraint sebagai pertimbangan praktis dalam pelaporan INDF."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 QC19–QC39 — Enhancing QC; QC35–QC39 — Cost Constraint"
  - doc: indf-2024-ar
    ref: "Aplikasi Enhancing QC dalam disclosure INDF AR 2024"
assigned_to: "TBD"
rubric: rubrics/slide-10.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 10: Enhancing Qualitative Characteristics + Cost Constraint

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
> **v5 audit finding:** Empat card QC (komparabilitas, verifiabilitas, ketepatwaktuan, keterpahaman) masing-masing berisi body text ~25–30 kata + INDF aplikasi + catatan, ditambah Cost Constraint panel bawah = estimasi >100 kata visible — Severity HIGH, Effort L, Fix: Pisahkan 4 QC peningkat ke 2 slide (2 QC per slide); pindahkan Cost Constraint ke slide 07 atau sendiri.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 544–576: empat cards QC peningkat menggunakan `font-size:15px` untuk body text (sangat kecil), `font-size:14px` untuk INDF aplikasi box, `font-size:13px` untuk pill labels; Cost Constraint box menggunakan `font-size:15px` dan `font-size:13px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Grid 2×2 card penuh + Cost Constraint bar bawah = kepadatan sangat tinggi; font 15px di body card menandai upaya memaksakan terlalu banyak teks — Severity HIGH, Effort L, Fix: Redesign ke 2 slide; gunakan lebih sedikit kata per card.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 10 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 10 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Perbedaan Enhancing QC dari Fundamental QC adalah konsep sulit: Enhancing QC bukan opsional — mereka meningkatkan kegunaan informasi yang sudah memenuhi Fundamental QC, tetapi mereka tidak dapat "menyelamatkan" informasi yang tidak relevan atau tidak faithfully represented.

- [ ] **Konteks/Ketegangan:** "Jika informasi sudah Relevan dan Faithfully
      Represented, apakah Comparability masih perlu dipikirkan? Atau cukup
      satu laporan keuangan yang akurat tanpa perlu dibandingkan?"
- [ ] **Demonstrasi:** Empat Enhancing QC disajikan dengan definisi singkat
      dan satu contoh konkret INDF per QC (mis. Comparability: restatement
      PSAK 24 untuk komparabilitas 2020–2024); Cost Constraint disajikan
      dengan referensi QC35–QC39.
- [ ] **Resolusi:** Interpretasi: Enhancing QC melipatgandakan nilai informasi
      — laporan yang sudah akurat menjadi jauh lebih berguna ketika dapat
      dibandingkan lintas waktu dan perusahaan; Cost Constraint menetapkan
      bahwa peningkatan kualitas ini harus cost-justified.
- [ ] **Per E3:** Grid 4 QC card tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — Enhancing QC melengkapi Fundamental QC
      dalam mendefinisikan "berguna bagi pengambil keputusan."
- [ ] **Story:** APPLICABLE — slide 10 adalah node "teori QC peningkat" dalam arc.

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
