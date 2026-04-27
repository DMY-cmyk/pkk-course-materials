<!--
slide: 31
role: synthesis
title: "Sintesis — Lima Insight Utama (Kontribusi Kelompok 2)"
learning_objective: "Audiens dapat merangkum lima insight utama kelompok tentang penerapan FASB CF di INDF 2024 dan mengevaluasi argumen bahwa INDF lebih memprioritaskan Faithful Representation daripada maksimisasi Relevance."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 QC6–QC16 — Relevance dan Faithful Representation; trade-off antara keduanya"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — restatement PSAK 24; goodwill Rp12,8T akuisisi; PSAK 72; related party Rp10,11T"
  - doc: wolk-dodd-rozycki
    ref: "Wolk, Dodd & Rozycki (2017) — ketegangan Relevance vs Reliability/FR dalam FMCG"
assigned_to: "TBD"
rubric: rubrics/slide-31.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 31: Sintesis — Lima Insight Utama (Kontribusi Kelompok 2)

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
> **v5 audit finding:** Slide 31 berjudul "Sintesis — Lima Insight Utama" meringkas slide 08–30 dengan 5 poin, namun slide 19 ("Diagram Master SFAC 8") dan slide 20 ("PSAK vs FASB CF") sudah merupakan sintesis teori. Tiga slide sintesis (19, 20, 31) berpotensi redundan satu sama lain dalam fungsi merangkum — Severity LOW, Effort M, Fix: Evaluasi apakah slide 31 dapat digabung dengan elemen slide 19 atau 20; jika dipertahankan, pastikan tidak tumpang tindih dengan sintesis di slide 19.

- [ ] **Crime #2 — Too many words:** Jumlah kata di body slide ≤25 kata.
      Kalimat berlebih dipindahkan ke catatan presenter, bukan dihapus.
> **v5 audit finding:** Grid 2 kolom: 5 insight cards masing-masing berisi heading + teks ~25–30 kata + 1 box overarching conclusion = estimasi >120 kata visible — Severity HIGH, Effort L, Fix: Sederhanakan ke 3 insight utama; pindahkan detail ke catatan; kesimpulan = 1 kalimat.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 2102–2155: lima insight cards menggunakan `font-size:19px` untuk heading dan body; "Kesimpulan Overarching" menggunakan `font-size:20px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Grid 2 kolom × 3 rows (5 card + 1 conclusion) = frame hampir penuh — Severity MED, Effort L, Fix: Kurangi ke 3 insight; tambah breathing room.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 31 bukan slide terakhir; slide 32 adalah penutup. Slide 31 berisi insight, bukan nama anggota.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found untuk slide 31 — slide 31 berisi insight, bukan "Terima Kasih". Namun per spec, slide 31 adalah Contributions 2 (sintesis argumen Relevance vs FR). Verifikasi konten sesuai spec bagian 3.

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA (sintesis angka INDF) — F5 wajib.**

Per audit-deck-v5.md F5: "Slide 31 (sintesis) mengintegrasikan angka konkret ke dalam pernyataan insight: 'Goodwill Rp12,8T, PSAK 72 lima-langkah, dan related party Rp10,11T — semua memenuhi kriteria RD3' — ini adalah contoh 'angka sebagai prop dengan interpretasi'."

- [ ] **Konteks/Ketegangan:** "Setelah mengkaji 29 slide — tujuan, QC,
      elemen, pengakuan, pengukuran, dan penyajian INDF — kesimpulan apa
      yang dapat kita tarik? Apakah INDF 2024 lebih faithfully represents
      atau lebih relevan? Dan apakah trade-off itu konsekuensi intentional?"
- [ ] **Demonstrasi:** Lima insight (atau tiga insight yang dikonsolidasikan)
      disajikan dengan angka konkret per insight: EPS, goodwill, restatement
      PSAK 24, EBIT +73%, related party Rp10,11T — semua dengan referensi
      halaman INDF AR 2024. Kalimat Kesimpulan Overarching dari slide 31
      v5.html (line 2153) dipertahankan sebagai kandidat Salient Idea.
- [ ] **Resolusi:** Argumen eksplisit: INDF 2024 secara keseluruhan lebih
      memprioritaskan Faithful Representation (restatement PSAK 24 sukarela,
      konservatisme goodwill impairment) dibanding maksimisasi Relevance —
      implikasinya bagi investor yang menggunakan laporan ini untuk alokasi modal.
- [ ] **Per E3:** Insight cards tanpa referensi angka dan resolusi FASB = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** APPLICABLE — slide 31 (Contributions 2) adalah lokasi yang
      tepat untuk memperkuat Symbol bangunan tiga lantai sebagai penutup
      visual sebelum slide terakhir.
- [ ] **Slogan:** NOT APPLICABLE sebagai lokasi Slogan wajib — per spec,
      Slogan wajib di slides 2, 7, 19, 30. Slide 31 bukan target Slogan
      wajib, meskipun Slogan dapat muncul sebagai kutipan penutup.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE dan KRITIS — slide 31 adalah lokasi di
      mana Salient Idea deck harus diartikulasikan secara eksplisit sebagai
      kesimpulan: "FASB CF bukan teori abstrak — ia bekerja nyata di INDF 2024."
      Kalimat Kesimpulan Overarching dari line 2153 v5.html adalah kandidat
      terkuat untuk Salient Idea final.
- [ ] **Story:** APPLICABLE — slide 31 adalah node "resolusi" dalam arc story
      (promise kept, dari promise yang dibuat di slide 2).

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
