<!--
slide: 07
role: content
title: "Karakteristik Kualitatif — Hierarki SFAC 8 (QC1–QC39)"
learning_objective: "Audiens dapat membedakan dua Fundamental QC (Relevance, Faithful Representation) dari empat Enhancing QC (Comparability, Verifiability, Timeliness, Understandability) dan menyebutkan lima transformasi kunci SFAC 8 dari SFAC 2."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 3, QC1–QC39 — fundamental dan enhancing QC"
  - doc: week-05-materials
    ref: "Week 5 Exercise — QC hierarchy SFAC 8"
assigned_to: "TBD"
rubric: rubrics/slide-07.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 07: Karakteristik Kualitatif — Hierarki SFAC 8 (QC1–QC39)

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
> **v5 audit finding:** Kolom kiri: diagram hierarki + 6 komponen boxes + enhancing QC label; kolom kanan: 5 "Transformasi Kunci" cards masing-masing berisi heading + 1 kalimat penjelasan = estimasi >100 kata visible — Severity HIGH, Effort L, Fix: Pisahkan diagram SFAC 8 hierarchy (slide 07a) dari tabel 5 transformasi (slide 07b).

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 386–403: teks dalam boxes menggunakan `font-size:19px`, `font-size:12px` (subtext QC numbers), `font-size:16px` (komponen boxes bawah), `font-size:20px` (enhancing QC line) — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Dua kolom dengan kepadatan sangat tinggi: kolom kiri diagram + 6 boxes, kolom kanan 5 cards bertumpuk; frame hampir penuh seluruhnya — Severity HIGH, Effort L, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 07 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 07 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Hierarki SFAC 8 mengubah arsitektur QC secara fundamental: Reliability diganti Faithful Representation; Conservatism dihapus dari QC; Verifiability turun dari Fundamental ke Enhancing. Ini adalah perubahan konseptual sulit yang tidak dapat dipahami hanya dari diagram.

- [ ] **Konteks/Ketegangan:** "Mengapa FASB menghapus Conservatism dari QC
      di SFAC 8 — padahal konservatisme adalah prinsip yang telah ada selama
      puluhan tahun? Apakah ini sinyal bahwa FASB lebih memilih relevansi
      daripada kehati-hatian?"
- [ ] **Demonstrasi:** Diagram hierarki SFAC 8 disajikan dengan label eksplisit
      (Relevance → Predictive Value + Confirmatory Value + Materiality;
      Faithful Representation → Completeness + Neutrality + Free from Error)
      dengan referensi QC1–QC39; lima transformasi kunci disajikan dengan
      referensi paragraf.
- [ ] **Resolusi:** Interpretasi: penghapusan Conservatism bukan melemahkan
      kehati-hatian — ia menegaskan bahwa Neutrality (sub-komponen Faithful
      Representation) sudah mencakup kebutuhan konservatisme tanpa bias ke
      arah sebaliknya.
- [ ] **Per E3:** Diagram hierarki tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama — Symbol bangunan dapat
      muncul sebagai mini-icon penghubung ke fondasi CF.
- [ ] **Slogan:** **APPLICABLE dan WAJIB** — per `specs/presentation-design-spec.md`
      bagian 2, slide 7 adalah lokasi kemunculan Slogan kedua:
      "Conceptual Framework: konstitusi laporan keuangan." Verifikasi bahwa
      Slogan hadir secara visual atau verbal di slide ini.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — QC SFAC 8 adalah operasionalisasi Salient
      Idea: Framework sebagai standar tunggal untuk menilai "berguna."
- [ ] **Story:** APPLICABLE — slide 07 adalah node utama "teori QC SFAC 8"
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
