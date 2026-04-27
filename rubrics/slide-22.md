<!--
slide: 22
role: case
title: "Primary Users INDF — Uji OB2: Siapa yang Dilayani Laporan INDF?"
learning_objective: "Audiens dapat mengidentifikasi primary users laporan keuangan INDF per SFAC 8 OB2 dan mengevaluasi apakah struktur disclosure INDF (segmented EBIT, goodwill breakdown) mencerminkan prioritas kebutuhan primary users tersebut."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 OB2 — primary users: existing and potential investors, lenders, other creditors"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — struktur disclosure kepada investor dan kreditor; basis penyusunan"
assigned_to: "TBD"
rubric: rubrics/slide-22.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 22: Primary Users INDF — Uji OB2

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
> **v5 audit finding:** Diagram dua zona (non-primary vs primary users) + tabel 3-baris kebutuhan + box prinsip OB2 dengan kutipan = estimasi >60 kata visible — Severity MED, Effort M, Fix: Sederhanakan diagram; pindahkan tabel kebutuhan ke catatan; pertahankan diagram zona + prinsip OB2.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1171–1252: zona diagram menggunakan `font-size:18px`, `font-size:16px`, `font-size:15px`, `font-size:13px` untuk label; tabel kebutuhan vs tersedia menggunakan `.tbl` (`font-size:18px` td); box OB2 menggunakan `font-size:22px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Dua kolom masing-masing penuh: zona diagram bertingkat (dashed outer, solid inner) mengisi >60% tinggi slide; tabel kanan juga padat — Severity MED, Effort M, Fix: Sederhanakan ke diagram zona saja; hapus tabel.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 22 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 22 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

Slide 22 menguji OB2 (primary users) terhadap struktur disclosure INDF. Angka dan struktur disclosure INDF adalah prop untuk menilai apakah laporan INDF benar-benar melayani investor dan kreditor sebagai primary users.

- [ ] **Konteks/Ketegangan:** "INDF menerbitkan Annual Report setebal ratusan
      halaman. Tetapi untuk siapa? Jika OB2 mensyaratkan primary users adalah
      investor dan kreditor — apakah breakdown segmen INDF cukup informatif
      bagi investor yang ingin menilai prospek masing-masing divisi?"
- [ ] **Demonstrasi:** Diagram zona primary vs non-primary users dengan referensi
      OB2; tabel kebutuhan informasi primary users (predictive, accountability)
      vs informasi yang tersedia di INDF AR 2024.
- [ ] **Resolusi:** Interpretasi: INDF menyediakan segmented EBIT disclosure
      (CBP, Bogasari, Agribusiness, Distribution) yang memenuhi kebutuhan
      predictive value bagi investor — selaras dengan OB2. Namun informasi
      tentang keputusan alokasi modal antar segmen masih terbatas.
- [ ] **Per E3:** Diagram zona tanpa konteks/ketegangan dan resolusi FASB =
      pelanggaran E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — uji OB2 menjawab apakah informasi INDF
      benar-benar berguna bagi pengambil keputusan yang tepat.
- [ ] **Story:** APPLICABLE — slide 22 adalah node "uji tujuan pelaporan"
      dalam arc studi kasus INDF.

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
