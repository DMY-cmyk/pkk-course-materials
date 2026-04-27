<!--
slide: 04
role: content
title: "Tujuan Pelaporan Keuangan — SFAC 8 (OB1–OB21)"
learning_objective: "Audiens dapat membedakan tujuan pelaporan keuangan SFAC 1 (OB2) dari SFAC 8 (OB17) dan menjelaskan mengapa pergeseran dari 'investor + kreditor' ke 'primary users' secara substantif mengubah scope laporan keuangan."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 1, OB2, OB17; SFAC 1 — evolusi definisi tujuan"
  - doc: week-05-materials
    ref: "Week 5 Exercise — tujuan pelaporan keuangan"
assigned_to: "TBD"
rubric: rubrics/slide-04.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 04: Tujuan Pelaporan Keuangan — SFAC 8 (OB1–OB21)

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
> **v5 audit finding:** Card kiri (lines 251–263): kutipan panjang OB2 + 5 item pengguna utama; card kanan: tabel 5-baris + teks OB17; estimasi total >80 kata visible — Severity HIGH, Effort L, Fix: Pisahkan ke 2 slide: (a) tujuan + OB2, (b) pengguna utama + evolusi.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 252–263: semua teks card "Primary Users" menggunakan `font-size:19px`; tabel evolusi SFAC 1 vs SFAC 8 menggunakan `.tbl compact` (`font-size:16px` td); sub-header "EVOLUSI SFAC 1 vs SFAC 8" menggunakan `.t-meta` (16px) — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Dua kolom masing-masing berisi 2 card + tabel penuh = >80% area frame; tidak ada breathing room vertikal maupun horizontal yang signifikan — Severity MED, Effort L, Fix: Pisahkan konten; tambah margin antara elemen.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 04 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 04 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Konsep "decision usefulness" dan pergeseran dari SFAC 1 ke SFAC 8 dalam definisi pengguna primer laporan keuangan adalah konsep yang tidak intuitif: mengapa mendefinisikan ulang "siapa pengguna" mengubah seluruh arsitektur informasi keuangan?

- [ ] **Konteks/Ketegangan:** Slide menetapkan ketegangan sebelum definisi
      disajikan — contoh: "Jika tujuan laporan keuangan hanyalah 'memberikan
      informasi', mengapa FASB perlu merevisi SFAC 1 dengan SFAC 8 setelah
      30 tahun? Apa yang berubah secara substantif?"
- [ ] **Demonstrasi:** OB2 (SFAC 8) dan OB17 disajikan secara eksplisit dengan
      paragraf referensi; evolusi SFAC 1 vs SFAC 8 ditampilkan sebagai perbandingan
      yang mengungkapkan perubahan substantif (bukan kosmetik).
- [ ] **Resolusi:** Satu kalimat interpretasi: pergeseran ke "primary users"
      (SFAC 8 OB2) mempersempit scope tetapi meningkatkan relevansi — implikasinya
      bagi laporan INDF 2024 adalah bahwa informasi segmen diprioritaskan untuk
      investor dan kreditor, bukan semua pemangku kepentingan.
- [ ] **Per E3:** Definisi adalah prop konseptual. Definisi polos tanpa
      konteks/ketegangan dan resolusi = pelanggaran E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama — verifikasi Symbol mini
      di pojok kiri atas jika desain memungkinkan.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
      Slide 04 bukan lokasi Slogan wajib.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — tujuan pelaporan keuangan adalah fondasi
      Salient Idea deck: informasi yang berguna bagi pengambil keputusan.
- [ ] **Story:** APPLICABLE — slide 04 adalah node "setup teori" dalam arc.

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
