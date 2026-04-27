<!--
slide: 32
role: qanda
title: "Kontribusi Kelompok 3 — Q&A Staging (Menggantikan 'Terima Kasih')"
learning_objective: "Audiens dapat menjawab pertanyaan terbuka yang diajukan kelompok — 'Jika INDF menerapkan full fair value untuk aset biologis, apakah laporan 2024 lebih relevan atau kurang faithfully represented?' — dengan menggunakan FASB CF sebagai kerangka analisis."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 QC6–QC16 — Relevance vs Faithful Representation; SFAC 5 — fair value vs historical cost trade-off"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — aset biologis perkebunan (PSAK 69/IAS 41); goodwill; EBIT Agribusiness +73%"
assigned_to: "TBD"
rubric: rubrics/slide-32.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 32: Kontribusi Kelompok 3 — Q&A Staging

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
> **v5 audit:** No violation found — confirm on rebuild. (Slide 32 sebagai Contributions Close / Q&A staging adalah slide yang diperlukan secara mandiri.)

- [ ] **Crime #2 — Too many words:** Jumlah kata di body slide ≤25 kata.
      Kalimat berlebih dipindahkan ke catatan presenter, bukan dihapus.
> **v5 audit:** No violation found untuk konten substantif — namun catatan: v5 menggunakan "Terima Kasih" + daftar anggota yang harus DIGANTI dengan Contributions Close. Setelah rebuild, verifikasi body slide ≤25 kata.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 2172–2213: judul "Terima Kasih" menggunakan `font-size:72px` (memenuhi), "THANK YOU" `font-size:28px`, nama anggota `font-size:18px`, NIM `font-size:16px`, Sesi Tanya Jawab `font-size:20px` — teks selain h1 utama semuanya sub-40pt — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign. Catatan: konten slide harus diubah total menjadi Contributions Close sebelum redesign tipografi.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit:** No violation found untuk slide ini setelah rebuild — Contributions Close dengan 1 pertanyaan terbuka + 3 kontribusi singkat akan memiliki ruang putih yang lebih dari cukup.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild. (Perlu verifikasi: per spec, logo boleh muncul di slide 32 sebagai penutup visual — pastikan tidak melebihi satu logo institusi.)

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit finding:** Lines 2183–2207: daftar 6 anggota kelompok (Efri Nurmalinda, Dzaki M. Yusfian, Nuradila, Achmad Dimas W., Adinda Putri Dewi, Setiabudi Y. Pratama) lengkap dengan NIM masing-masing disajikan sebagai konten utama slide terakhir — Severity HIGH, Effort M, Fix: Ganti dengan Contributions Slide: daftar 3–5 kontribusi spesifik kelompok. Anggota dapat disebut dalam 1 baris kecil di chrome/footer.

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit finding:** Line 2176: `<div style="font-size:72px;font-weight:800;color:#fff;...">Terima Kasih</div>` dan line 2177: `<div style="font-size:28px;...">THANK YOU</div>` — slide terakhir secara eksplisit berisi "Terima Kasih" sebagai elemen visual dominan — Severity HIGH, Effort M, Fix: Ganti judul slide dengan "Kontribusi Kelompok 3" atau "Temuan Utama"; pertahankan Q&A call-to-action sebagai sub-elemen kecil.

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA (Q&A dengan angka INDF) + Slide konsep sulit: YA (trade-off Relevance vs FR) — F5 wajib.**

Pertanyaan terbuka yang diajukan di slide 32 (per presentation-design-spec.md bagian 3, Slide 32 spec): "Jika INDF menerapkan full fair value measurement untuk aset biologis perkebunannya (sesuai PSAK 69/IAS 41), apakah laporan keuangan 2024 akan lebih relevan atau justru kurang faithfully represented — dan Framework mana yang memutuskan?" Ini adalah pertanyaan F5 sempurna: mengandung ketegangan, menggunakan angka INDF sebagai prop, dan memerlukan resolusi berbasis FASB CF.

- [ ] **Konteks/Ketegangan:** Pertanyaan terbuka itu sendiri adalah ketegangan —
      ia menempatkan audiens dalam posisi analis yang harus memilih antara
      dua nilai yang keduanya valid per FASB CF. Verifikasi bahwa pertanyaan
      diframing sebagai dilema nyata, bukan pertanyaan retoris dengan jawaban
      jelas.
- [ ] **Demonstrasi:** Slide menampilkan satu pertanyaan terbuka yang jelas
      + tiga kontribusi konkret kelompok (per spec bagian 3: tabel evaluasi
      3×3, argumen FR vs Relevance, Q&A staging) sebagai referensi bagi
      audiens untuk menjawab selama diskusi.
- [ ] **Resolusi:** Tidak ada resolusi pre-determined di slide — resolusi
      muncul dari diskusi Q&A. Slide tetap di layar selama Q&A; slide tidak
      digantikan slide kosong atau "Terima Kasih" (per F4 Contributions Close
      rules).
- [ ] **Per E3:** Slide Q&A tanpa pertanyaan yang dirumuskan dengan ketegangan
      = pelanggaran prinsip F5 dan F4.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** **APPLICABLE dan WAJIB** — per `specs/presentation-design-spec.md`
      bagian 2, Symbol bangunan tiga lantai harus muncul di slide Contributions
      Close (ukuran sedang, sebagai penutup visual). Verifikasi bahwa Symbol
      hadir di slide 32.
- [ ] **Slogan:** NOT APPLICABLE sebagai lokasi Slogan wajib — per spec,
      Slogan wajib di slides 2, 7, 19, 30. Slide 32 bukan target Slogan wajib.
      Namun Slogan dapat muncul sebagai kutipan penutup visual.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini — Surprise
      sudah dihadirkan di slides sebelumnya.
- [ ] **Salient idea:** APPLICABLE dan KRITIS — slide 32 adalah "promise
      kept" moment: Salient Idea harus terkonfirmasi secara visual di slide
      ini. Pertanyaan terbuka yang diajukan harus mencerminkan Salient Idea
      deck: Framework sebagai standar operasional untuk menilai "berguna."
- [ ] **Story:** APPLICABLE — slide 32 adalah node terakhir dalam arc (resolusi
      terbuka yang diundang untuk diskusi), memenuhi Opening-Close Mirror per F4.

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
