<!--
slide: 15
role: table
title: "Lima Atribut Pengukuran — SFAC 5 + Perspektif Kritis (Solomons, Sterling, Miller)"
learning_objective: "Audiens dapat menyebutkan lima atribut pengukuran SFAC 5, membandingkan pandangan dua tokoh kritis (mis. Sterling: current exit price; Solomons: current cost) dengan pilihan SFAC 5, dan menjelaskan mengapa SFAC 5 memilih mixed-attribute model."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 5 — lima atribut pengukuran (historical cost, current cost, current market value, net realizable value, present value of future cash flows)"
  - doc: wolk-dodd-rozycki
    ref: "Wolk, Dodd & Rozycki (2017) Ch. 7 — perspektif kritis Solomons, Sterling, Miller, SFAC 5 par. 2"
assigned_to: "TBD"
rubric: rubrics/slide-15.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 15: Lima Atribut Pengukuran — SFAC 5 + Perspektif Kritis

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
> **v5 audit finding:** Tabel 5 atribut (5 baris × 5 kolom) + empat critique boxes (Solomons, Sterling, SFAC 5 par. 2, Miller) masing-masing berisi kutipan dan penjelasan = estimasi >100 kata visible — Severity HIGH, Effort L, Fix: Pisahkan: (a) tabel lima atribut (slide 15a), (b) perspektif kritis (slide 15b).

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 782–800: tabel "Lima Dasar Pengukuran" menggunakan `.tbl compact` (16px td, 12px th); empat critique boxes menggunakan `font-size:21px` heading dan `font-size:20px` body — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Tabel penuh lebar atas + empat card bawah dalam grid 4 kolom = frame hampir penuh; teks di critique cards sangat kecil — Severity HIGH, Effort L, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 15 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 15 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Mixed-attribute model adalah konsep sulit: mengapa aset biologis INDF dapat diukur dengan fair value (PSAK 69/IAS 41) sementara aset tetap lain diukur dengan historical cost? Pilihan ini bukan arbitrary — ia mencerminkan trade-off SFAC 5 antara relevansi dan verifiabilitas.

- [ ] **Konteks/Ketegangan:** "Mengapa INDF menggunakan fair value untuk
      perkebunan kelapa sawit tetapi historical cost untuk pabrik? Apakah
      ini inkonsistensi, atau justru pilihan yang optimal per Framework?"
- [ ] **Demonstrasi:** Lima atribut SFAC 5 disajikan dalam tabel dengan
      kolom relevansi vs verifiabilitas; perspektif kritis Solomons dan
      Sterling disajikan sebagai pandangan alternatif dengan kutipan sumber
      Wolk et al. (2017).
- [ ] **Resolusi:** Interpretasi: SFAC 5 memilih mixed-attribute model bukan
      karena kompromi politik tetapi karena setiap atribut memiliki trade-off
      relevansi–verifiabilitas yang berbeda per jenis aset — pilihan yang
      paling informatif per jenis aset.
- [ ] **Per E3:** Tabel atribut tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** APPLICABLE — mixed-attribute model sebagai pilihan optimal
      (bukan kompromi) adalah insight kontra-intuitif yang dapat dieksploitasi.
- [ ] **Salient idea:** APPLICABLE — measurement attributes menentukan apakah
      angka yang dilaporkan benar-benar berguna bagi pengambil keputusan.
- [ ] **Story:** APPLICABLE — slide 15 adalah node "teori pengukuran" dalam arc.

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
