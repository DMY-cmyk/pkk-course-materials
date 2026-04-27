<!--
slide: 29
role: case
title: "Penyajian OCI INDF — Hierarki FS, OCI Waterfall, Efek Kurs"
learning_objective: "Audiens dapat mengidentifikasi komponen OCI INDF 2024 dalam waterfall dan menjelaskan mengapa efek translasi mata uang asing disajikan dalam OCI (bukan Net Income) sebagai implementasi prinsip Disaggregasi per SFAC 8 Ch. 7."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 7, PR12 — presentation disaggregation; BC7.21 — rationale OCI presentation"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — Comprehensive Income statement; OCI components (forex translation, biological asset revaluation); efek kurs"
assigned_to: "TBD"
rubric: rubrics/slide-29.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 29: Penyajian OCI INDF — Hierarki FS, OCI Waterfall, Efek Kurs

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
> **v5 audit finding:** Tiga kolom: hierarki FS (face vs notes) + OCI waterfall 5 item + efek kurs tabel 3-baris = estimasi >70 kata visible — Severity MED, Effort L, Fix: Fokus slide ini pada satu topik: OCI saja atau Face of FS saja.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1891–1976: tiga kolom penyajian menggunakan `font-size:20px` dan berbagai ukuran sub-40pt; OCI waterfall menggunakan `font-size:20px`; tabel efek kurs menggunakan `.tbl compact` (16px/12px) — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Grid 340px + 1fr + 1fr dengan masing-masing penuh = frame hampir penuh — Severity MED, Effort M, Fix: Sederhanakan ke satu fokus konten.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 29 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 29 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

OCI waterfall INDF adalah prop visual kunci: ia memisahkan laba operasional dari efek kurs dan revaluasi aset biologis — komponen yang volatil dan "tidak berulang" (non-recurring). Tanpa pemahaman prinsip Disaggregasi, audiens tidak dapat menginterpretasikan mengapa pemisahan ini penting.

- [ ] **Konteks/Ketegangan:** "INDF memiliki operasi di 24 negara dengan
      pendapatan dan biaya dalam berbagai mata uang. Jika efek kurs
      dimasukkan ke Net Income, laba INDF 2024 akan terlihat sangat berbeda
      dari kinerja operasional inti. OCI memisahkan itu — tetapi apakah
      pemisahan ini fair bagi investor?"
- [ ] **Demonstrasi:** OCI waterfall INDF disajikan dengan komponen spesifik
      (translasi mata uang, revaluasi aset biologis, dll.) dari INDF AR 2024;
      tabel efek kurs menunjukkan dampak kuantitatif; referensi PR12 dan BC7.21.
- [ ] **Resolusi:** Interpretasi: pemisahan OCI meningkatkan Disaggregasi dan
      Predictive Value — investor dapat menilai kinerja operasional inti
      terpisah dari volatilitas kurs, konsisten dengan SFAC 8 Ch. 7 BC7.21.
- [ ] **Per E3:** Waterfall chart tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — penyajian OCI yang tepat adalah contoh
      konkret terakhir dari Salient Idea sebelum sintesis.
- [ ] **Story:** APPLICABLE — slide 29 adalah node "uji penyajian" dan penutup
      blok kasus INDF dalam arc.

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
