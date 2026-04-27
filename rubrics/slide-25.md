<!--
slide: 25
role: case
title: "Goodwill Uji Definisi Aset — SFAC 8 Ch. 4 (Rp52,2T = 26% Total Aset)"
learning_objective: "Audiens dapat menerapkan uji definisi Aset SFAC 8 Ch. 4 pada goodwill INDF Rp52,2T menggunakan dua tabel uji (economic resource, controlled by entity, result of past event) dan menarik kesimpulan yang didukung bukti apakah goodwill memenuhi definisi Aset."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 4 — definisi Aset; tiga kriteria economic resource, control, past event"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — goodwill Rp52,2T (26% dari Rp201,71T total aset); catatan goodwill"
assigned_to: "TBD"
rubric: rubrics/slide-25.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 25: Goodwill Uji Definisi Aset — SFAC 8 Ch. 4

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
> Crimes #4 (reading aloud), #5 (laser pointer), #6 (speaker disease)
> dipindah ke `analysis/winston-audit/delivery-checklist.md` per E2.

- [ ] **Crime #1 — Too many slides:** Slide ini perlu secara mandiri? Jika
      substansi sudah ada di slide tetangga, gabung. Setiap slide harus
      memiliki satu ide tunggal yang tidak dapat disatukan dengan slide lain
      tanpa kehilangan kejelasan.
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #2 — Too many words:** Jumlah kata di body slide ≤25 kata.
      Kalimat berlebih dipindahkan ke catatan presenter, bukan dihapus.
> **v5 audit finding:** Dua tabel uji definisi (masing-masing 3 baris × 3 kolom) + proportion card + challenge list = estimasi >60 kata visible — Severity MED, Effort M, Fix: Gabungkan kedua tabel ke 1 tabel komparatif; sederhanakan challenge ke 2 poin.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1500–1582: dua tabel uji SFAC menggunakan `.tbl` (18px td) dan `card-head` labels; proportion card menggunakan `font-size:58px` (stat-num amber — ini melewati threshold tetapi untuk satu angka saja, teks lainnya sub-40pt); challenge cards menggunakan `font-size:17px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Grid 1fr 1fr 340px: dua tabel penuh + kolom kanan 2 card bertumpuk = >80% frame terisi — Severity MED, Effort M, Fix: Sederhanakan tabel; tambah whitespace.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 25 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 25 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

Per audit-deck-v5.md F5 section: "Slide 25 (yang berkaitan dengan goodwill test) lebih mendekati story arc: ia memiliki konteks (proporsi goodwill Rp52,2T terhadap total aset), lalu demonstrasi (dua tabel uji definisi SFAC), lalu partial resolusi."

- [ ] **Konteks/Ketegangan:** "Rp52,2T goodwill — 26% dari seluruh aset
      INDF — adalah angka yang bergantung sepenuhnya pada satu pertanyaan:
      apakah goodwill benar-benar memenuhi definisi Aset per SFAC 8? Jika
      tidak, Rp52,2T harus dihapus dari neraca."
- [ ] **Demonstrasi:** Dua tabel uji (SFAC 6 vs SFAC 8 Ch. 4 criteria)
      diterapkan pada goodwill INDF; proportion card menunjukkan 26% dari
      total aset dengan referensi INDF AR 2024; challenge list menyajikan
      dua keterbatasan utama (impairment risk, amortization policy).
- [ ] **Resolusi:** Interpretasi via FASB: goodwill INDF memenuhi tiga
      kriteria SFAC 8 Ch. 4 (economic resource dari sinergi; dikontrol INDF;
      berasal dari akuisisi masa lalu). Namun risiko impairment harus
      diungkapkan secara Faithful — jika sinergi tidak terealisasi, goodwill
      harus diimpair sesuai PSAK 48/IAS 36.
- [ ] **Per E3:** Tabel uji definisi tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** APPLICABLE — goodwill 26% total aset yang lolos uji
      definisi Aset SFAC 8 adalah konfirmasi mengejutkan bahwa "angka
      intangible" memiliki legitimasi FASB yang kokoh.
- [ ] **Salient idea:** APPLICABLE — uji definisi goodwill langsung
      mendemonstrasikan Salient Idea: Framework sebagai alat analisis operasional.
- [ ] **Story:** APPLICABLE — slide 25 adalah node "uji definisi elemen"
      dalam arc studi kasus.

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
