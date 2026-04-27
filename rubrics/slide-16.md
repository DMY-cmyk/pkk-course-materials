<!--
slide: 16
role: content
title: "Entry vs Exit Price — SFAC 8 Ch. 6 (M30–M34) — Aplikasi INDF"
learning_objective: "Audiens dapat mendefinisikan Entry Price vs Exit Price per SFAC 8 Ch. 6 M30–M34 dan menjelaskan kapan INDF menggunakan masing-masing atribut dalam laporan keuangan 2024 beserta alasannya."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 6, M30–M34 — Entry Price, Exit Price, dan atribut pengukuran"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — aplikasi Entry/Exit price dalam pengukuran aset dan liabilitas"
assigned_to: "TBD"
rubric: rubrics/slide-16.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 16: Entry vs Exit Price — SFAC 8 Ch. 6 (M30–M34)

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
> **v5 audit finding:** Dua panel Entry vs Exit + tabel 5-baris aplikasi INDF = estimasi >60 kata visible; tabel memiliki 4 kolom dengan teks penuh per cell — Severity MED, Effort L, Fix: Pisahkan: (a) Entry vs Exit concept, (b) tabel aplikasi INDF.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 814–840: dua card Entry/Exit menggunakan `font-size:14px` untuk isi, `font-size:13px` untuk label M30–M34; tabel INDF application menggunakan `.tbl compact` (16px/12px); overall body text 14px sangat sub-40pt — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Panel konsep (grid 1fr 80px 1fr) + tabel penuh lebar = >80% frame terisi — Severity MED, Effort M, Fix: Pisahkan ke 2 slide; sederhanakan tabel ke 3 baris kunci.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 16 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 16 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Perbedaan Entry Price vs Exit Price adalah konsep teknis yang memiliki konsekuensi besar: fair value (Exit Price) menghasilkan angka yang berbeda dari historical cost (Entry Price), dan pilihan antara keduanya menentukan apakah laporan keuangan INDF mencerminkan nilai pasar atau nilai historis perolehan.

- [ ] **Konteks/Ketegangan:** "Aset biologis perkebunan INDF dicatat dengan
      nilai berapa — harga perolehan ketika ditanam (Entry Price) atau nilai
      pasar CPO saat pelaporan (Exit Price)? Perbedaannya bisa ratusan
      miliar rupiah — dan Framework menentukan mana yang lebih 'benar'."
- [ ] **Demonstrasi:** Dua panel Entry vs Exit dengan definisi per M30–M34;
      tabel aplikasi INDF menunjukkan jenis aset vs atribut yang digunakan
      dengan referensi INDF AR 2024.
- [ ] **Resolusi:** Interpretasi: INDF menggunakan campuran Entry (historical
      cost untuk aset tetap) dan Exit (fair value untuk aset biologis per
      PSAK 69) — campuran ini adalah implementasi mixed-attribute model yang
      konsisten dengan SFAC 5 dan SFAC 8 Ch. 6.
- [ ] **Per E3:** Panel konsep tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — pilihan pengukuran secara langsung
      mempengaruhi kegunaan informasi bagi pengambil keputusan.
- [ ] **Story:** APPLICABLE — slide 16 adalah node "pengukuran Entry vs Exit"
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
