<!--
slide: 20
role: content
title: "PSAK vs FASB CF — Rantai Otoritas FASB → IASB → PSAK → INDF"
learning_objective: "Audiens dapat menelusuri rantai otoritas dari FASB Conceptual Framework ke IASB Conceptual Framework 2018 ke PSAK ke praktik pelaporan INDF, dan menjelaskan mengapa INDF 'bukan di jalur FASB langsung' namun tetap relevan untuk dianalisis dengan lensa FASB."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 — Framework sebagai sumber otoritas; konvergensi FASB-IASB"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — pernyataan kepatuhan PSAK; basis penyusunan laporan keuangan"
assigned_to: "TBD"
rubric: rubrics/slide-20.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 20: PSAK vs FASB CF — Rantai Otoritas FASB → IASB → PSAK → INDF

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
> **v5 audit finding:** Diagram rantai FASB→IASB→PSAK→INDF + empat convergence bullets + tabel 3-baris perbedaan = estimasi >60 kata visible — Severity MED, Effort M, Fix: Diagram rantai sudah cukup visual; hapus tabel perbedaan atau pindahkan ke catatan.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 980–1023: teks rantai otoritas menggunakan `font-size:21px`, `font-size:20px`; tabel perbedaan menggunakan `.tbl compact` (16px/12px); convergence bullets menggunakan `font-size:20px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Diagram flowchart kiri + dua card kanan (hijau + tabel) = frame penuh; diagram flowchart itu sendiri sudah padat dengan teks — Severity MED, Effort M, Fix: Sederhanakan diagram; hapus tabel dalam kolom kanan.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 20 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 20 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Klaim di slide 20 (line 999 v5.html): "INDF bukan di jalur FASB langsung — INDF → PSAK → IASB CF 2018." Ini adalah Surprise terkuat dalam deck yang dikubur di slide 20 — perlu konteks/ketegangan yang kuat sebelum klaim ini disajikan.

- [ ] **Konteks/Ketegangan:** "Presentasi ini menganalisis INDF dengan FASB
      Conceptual Framework — tetapi INDF menyusun laporan keuangan berdasarkan
      PSAK, bukan US GAAP. Apakah analisis kita valid? Atau kita sedang
      menggunakan pisau bedah yang salah?"
- [ ] **Demonstrasi:** Diagram rantai otoritas FASB → IASB CF 2018 (Joint
      Conceptual Framework Project) → PSAK → INDF disajikan dengan titik
      konvergensi yang eksplisit; perbedaan FASB vs IASB CF 2018 yang material
      disajikan dengan referensi spesifik.
- [ ] **Resolusi:** Interpretasi: analisis FASB-lensa valid karena IASB CF
      2018 adalah produk konvergensi dengan FASB; perbedaan yang ada (mis.
      Prudence dalam IASB CF 2018 vs penghapusan Conservatism di SFAC 8)
      disebutkan secara eksplisit sebagai caveat analisis.
- [ ] **Per E3:** Diagram rantai tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
      Slide 20 bukan target Slogan wajib.
- [ ] **Surprise:** **APPLICABLE dan KUAT** — "INDF bukan di jalur FASB
      langsung" (audit-deck-v5.md, F3 Surprise section, line 999 v5.html)
      adalah Surprise utama deck yang harus dieksploitasi secara penuh di
      slide ini. Verifikasi bahwa framing Surprise hadir secara eksplisit.
- [ ] **Salient idea:** APPLICABLE — slide 20 mengkontekstualisasikan Salient
      Idea: Framework bekerja nyata meski melalui jalur konvergensi tidak langsung.
- [ ] **Story:** APPLICABLE — slide 20 adalah node "jembatan teori ke kasus"
      dalam arc; ia menjustifikasi mengapa analisis FASB-lensa valid untuk INDF.

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
