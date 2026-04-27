<!--
slide: 03
role: content
title: "Sejarah & Konteks — Mengapa Kerangka Konseptual Diperlukan?"
learning_objective: "Audiens dapat menyebutkan tiga era pre-Framework (CAP, APB, ARS) dan menjelaskan satu keterbatasan mendasar tiap era yang mendorong dibangunnya SFAC."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC kronologi SFAC 1–8"
  - doc: week-05-materials
    ref: "Week 5 Exercise — konteks sejarah FASB CF"
  - doc: wolk-dodd-rozycki
    ref: "Wolk, Dodd & Rozycki (2017) Ch. 7 pp. 163–166"
assigned_to: "TBD"
rubric: rubrics/slide-03.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 03: Sejarah & Konteks — Mengapa Kerangka Konseptual Diperlukan?

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
> **v5 audit finding:** Card "Era Pra-CF" (line 214): "CAP (1939–59) — ARBs ad hoc, tanpa fondasi teoritis / APB (1959–73) — Opinions; tekanan industri kuat; ARS 1 & 3 (1962) ditolak / Masalah fundamental: ..." = estimasi 40+ kata dalam satu card saja; total slide >100 kata — Severity HIGH, Effort L, Fix: Pisahkan timeline + tabel SFAC ke slide terpisah; pertahankan hanya timeline visual di slide ini.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Line 214–218: `.t-h5` 26px untuk bullet "Era Pra-CF"; teks detail di card "Pra-CF" dan "Pendahulu Intelektual" menggunakan inline `font-size:20px`; tabel SFAC menggunakan `.tbl compact` dengan `font-size:16px` (line 91) dan `font-size:12px` untuk th — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** SVG timeline 1760px lebar + dua panel besar bawah (grid 1fr 1fr) + tabel 8 baris = kepadatan sangat tinggi; tidak ada white space antara elemen — Severity MED, Effort L, Fix: Pisahkan ke 2 slide: (a) timeline, (b) tabel SFAC.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 03 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 03 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Slide 03 memperkenalkan konteks historis yang secara konseptual sulit: mengapa badan standar akuntansi yang terstruktur (CAP, APB) gagal, dan bagaimana kegagalan itu mendorong dibangunnya Conceptual Framework. Konsep "fondasi teoritis" vs. "aturan ad hoc" adalah perbedaan yang tidak intuitif bagi audiens yang terbiasa melihat standar akuntansi sebagai kumpulan aturan teknis.

- [ ] **Konteks/Ketegangan:** Slide menetapkan mengapa kronologi CAP–APB–SFAC
      ini penting bagi audiens — satu kalimat atau visual yang menimbulkan
      pertanyaan analitis sebelum jawaban disajikan. Contoh: "Selama 34 tahun
      (1939–1973), standar akuntansi AS ditetapkan tanpa fondasi teoritis —
      akibatnya: setiap tekanan industri dapat mengubah standar. Framework
      hadir untuk mengakhiri itu."
- [ ] **Demonstrasi:** Kronologi spesifik (CAP 1939–59, APB 1959–73, ARS 1 & 3
      1962 ditolak, FASB didirikan 1973, SFAC 1–8) disajikan dengan referensi
      ke Wolk et al. (2017) Ch. 7 pp. 163–166. Judul timeline mengandung
      pertanyaan analitis, bukan sekadar label deskriptif.
- [ ] **Resolusi:** Satu atau dua kalimat interpretasi eksplisit: era pra-CF
      menghasilkan standar tanpa landasan — Framework adalah konstitusi yang
      menutup celah itu. Menyebut secara eksplisit relevansi SFAC 8 sebagai
      versi terbaru yang menggantikan SFAC 2.
- [ ] **Per E3:** Kronologi adalah prop verbal/visual. Timeline polos tanpa
      konteks/ketegangan dan resolusi FASB = pelanggaran ganda (kekosongan
      naratif + E3).

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

Slide ini menguatkan elemen STAR mana?

- [ ] **Symbol:** Slide ini menampilkan atau secara eksplisit merujuk Symbol
      deck (bangunan tiga lantai)?
      **NOT APPLICABLE sebagai elemen utama** — slide 03 adalah konten sejarah.
      Symbol mini dapat muncul di pojok kiri atas sebagai orientasi, tetapi
      bukan elemen konten utama.
- [ ] **Slogan:** Slogan deck muncul di slide ini?
      **NOT APPLICABLE** — per spec, Slogan muncul di slides 2, 7, 19, 30.
      Slide 03 bukan lokasi Slogan wajib.
- [ ] **Surprise:** Slide ini membongkar kebenaran kontra-intuitif yang
      menentang asumsi awam tentang FASB atau pelaporan keuangan INDF?
      **APPLICABLE** — fakta bahwa SFAC secara eksplisit *bukan* GAAP (tidak
      menetapkan aturan wajib) namun berada *di atas* semua aturan adalah
      Surprise yang dapat diperkenalkan di sini sebagai hook awal. Verifikasi
      bahwa slide 03 tidak melewatkan momentum ini.
- [ ] **Salient idea:** Slide ini berkontribusi ke salient idea deck-level?
      **APPLICABLE** — sejarah mendukung Salient Idea dengan menunjukkan *mengapa*
      Framework diperlukan (sebelum Framework = chaos; Framework = konstitusi).
- [ ] **Story:** Slide ini adalah node yang teridentifikasi dalam story arc?
      **APPLICABLE** — slide 03 adalah "konteks/setup" node dalam arc:
      mengapa INDF 2024 membutuhkan Framework untuk membuat keputusan pelaporan.

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
