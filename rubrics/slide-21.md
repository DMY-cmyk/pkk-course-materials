<!--
slide: 21
role: case
title: "Profil INDF 2024 — Financial Highlights (Rp115,79T Penjualan, Rp201,71T Aset)"
learning_objective: "Audiens dapat menyebutkan empat metrik keuangan utama INDF 2024 (penjualan, total aset, goodwill, EPS) dan menjelaskan mengapa skala Rp115,79T menjadikan INDF sebagai studi kasus yang signifikan untuk menguji keandalan FASB CF."
sources:
  - doc: indf-2024-ar
    ref: "INDF AR 2024 pp. 4, 32–34 — Financial Highlights: penjualan Rp115,79T, aset Rp201,71T, goodwill Rp52,2T, EPS Rp984"
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 OB2 — primary users; RE8–9 — consolidated entity"
assigned_to: "TBD"
rubric: rubrics/slide-21.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 21: Profil INDF 2024 — Financial Highlights

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
> **v5 audit finding:** Profil INDF: org chart 4 subsidiary + 8 stat blocks (penjualan, aset, goodwill, EPS, laba bersih, ekuitas, ROE, interest coverage) + ownership donut chart + keterangan audit = estimasi >80 kata visible — Severity HIGH, Effort L, Fix: Pisahkan profil perusahaan (subsidiaries + overview) dari financial highlights (stats + ownership).

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1043–1154: stat block menggunakan `font-size:34px` (masih sub-40pt); deskripsi subsidiary menggunakan `font-size:15px`; ownership detail menggunakan `font-size:22px` dan `font-size:18px`; badge audit menggunakan `font-size:18px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Layout dua kolom: kiri org chart + 4 subsidiary cards; kanan stats (4+4 grid) + ownership chart + audit badge = hampir seluruh frame penuh — Severity MED, Effort L, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 21 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 21 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

Slide 21 adalah profil INDF — stat blocks dengan angka konkret dari AR 2024. Angka-angka ini adalah prop utama: goodwill Rp52,2T (26% total aset) adalah angka yang harus ditegaskan sebagai "mengejutkan" sebelum didemonstrasikan.

- [ ] **Konteks/Ketegangan:** "Rp201,71 triliun total aset — perusahaan
      terbesar ketiga di Indonesia. Namun 26% dari total aset itu adalah
      goodwill Rp52,2T yang tidak dapat dilihat, dipegang, atau dijual secara
      terpisah. Apakah angka itu nyata, atau sekadar konstruksi akuntansi?"
- [ ] **Demonstrasi:** Delapan stat blocks disajikan dari INDF AR 2024 pp. 4,
      32–34; org chart empat segmen; ownership structure dengan referensi halaman.
- [ ] **Resolusi:** Interpretasi: profil ini menetapkan baseline — dalam tiga
      slide berikutnya, setiap angka akan diuji dengan FASB CF untuk menilai
      apakah informasi yang tersaji benar-benar memenuhi Relevance dan
      Faithful Representation.
- [ ] **Per E3:** Stat blocks tanpa konteks/ketegangan dan resolusi FASB =
      pelanggaran ganda (kekosongan naratif + E3).

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
      Slide 21 bukan target Slogan wajib.
- [ ] **Surprise:** APPLICABLE — goodwill 26% total aset adalah angka yang
      mengejutkan dan harus diframing sebagai Surprise di awal slide ini.
- [ ] **Salient idea:** APPLICABLE — profil INDF menetapkan skala studi kasus
      yang mendukung Salient Idea: Framework bekerja nyata di perusahaan
      multinasional Rp115,79T.
- [ ] **Story:** APPLICABLE — slide 21 adalah opening node studi kasus INDF
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
