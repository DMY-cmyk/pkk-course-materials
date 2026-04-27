<!--
slide: 18
role: content
title: "Catatan & Perspektif Kritis — Keterbatasan SFAC 8 (Gaa, Archer, Wolk)"
learning_objective: "Audiens dapat menyebutkan empat keterbatasan Conceptual Framework dan merangkum pandangan tiga akademisi kritis (Gaa, Archer, Wolk) tentang keterbatasan tersebut, kemudian menilai apakah keterbatasan itu material bagi pengguna laporan INDF."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 — keterbatasan framework; catatan pada proses politik FASB"
  - doc: wolk-dodd-rozycki
    ref: "Wolk, Dodd & Rozycki (2017) Ch. 7 — Gaa, Archer, perspektif kritis"
assigned_to: "TBD"
rubric: rubrics/slide-18.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 18: Catatan & Perspektif Kritis — Keterbatasan SFAC 8

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
> **v5 audit finding:** Empat limitation boxes + tiga perspektif kritis (Gaa, Archer, Wolk) masing-masing berisi judul + body ~30 kata = estimasi >100 kata visible — Severity HIGH, Effort L, Fix: Pisahkan: (a) empat keterbatasan catatan, (b) tiga perspektif kritis.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 901–929: empat keterbatasan boxes menggunakan `font-size:22px` untuk nomor dan `font-size:20px` untuk body; tiga perspektif kritis menggunakan `font-size:19px` body dan `font-size:20px` heading; catatan kelemahan menggunakan `font-size:16px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Grid 4 kolom (limitations) + grid 3 kolom (perspectives) = frame hampir penuh; tidak ada breathing room — Severity HIGH, Effort L, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 18 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 18 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Keterbatasan Framework adalah konsep sulit karena mengharuskan audiens untuk berpikir meta: Framework yang digunakan sebagai "konstitusi" ternyata memiliki kelemahan yang diakui para akademisi. Bagaimana kita menilai Framework yang kita gunakan untuk menilai laporan keuangan?

- [ ] **Konteks/Ketegangan:** "Kita telah menggunakan SFAC 8 sebagai
      'konstitusi' laporan keuangan INDF — tetapi para akademisi seperti Gaa
      dan Archer berpendapat bahwa Framework sendiri cacat. Apakah kita
      mengevaluasi INDF dengan pisau bedah yang tidak sempurna?"
- [ ] **Demonstrasi:** Empat keterbatasan Framework disajikan dengan referensi
      spesifik; perspektif Gaa, Archer, dan Wolk disajikan dengan kutipan
      sumber Wolk et al. (2017).
- [ ] **Resolusi:** Interpretasi: keterbatasan Framework bersifat sistemik
      (karena proses politik FASB) bukan fatal — untuk kasus INDF, Framework
      masih memberikan panduan yang lebih baik daripada tidak ada panduan.
      Keterbatasan ini mendorong perlunya judgment profesional, bukan
      penggantian Framework.
- [ ] **Per E3:** Grid keterbatasan tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** APPLICABLE — keterbatasan Framework yang diakui secara
      resmi adalah informasi kontra-intuitif: "konstitusi laporan keuangan"
      ternyata tidak sempurna, dan FASB sendiri mengetahuinya.
- [ ] **Salient idea:** APPLICABLE — slide ini mengkontekstualisasikan Salient
      Idea: Framework adalah standar tunggal terbaik yang tersedia, bukan
      standar yang sempurna.
- [ ] **Story:** APPLICABLE — slide 18 adalah node "kontekstualisasi kritis"
      yang mempersiapkan transisi ke studi kasus INDF.

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
