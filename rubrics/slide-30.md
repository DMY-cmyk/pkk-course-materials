<!--
slide: 30
role: synthesis
title: "Disclosure — Catatan INDF, Segmen, Related Party + Enhancing QC"
learning_objective: "Audiens dapat mengevaluasi apakah struktur catatan (notes) INDF 2024 memenuhi prinsip Disclosure SFAC 8 dan menjelaskan bagaimana catatan tentang segmen dan transaksi pihak berelasi meningkatkan Enhancing QC (Comparability, Verifiability, Understandability)."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 8 — Notes and Disclosure; QC19–QC32 — Enhancing QC (Comparability, Verifiability, Timeliness, Understandability)"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — catatan laporan keuangan; segmen disclosure; transaksi pihak berelasi Rp10,11T"
assigned_to: "TBD"
rubric: rubrics/slide-30.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 30: Disclosure — Catatan INDF, Segmen, Related Party + Enhancing QC

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
> **v5 audit finding:** Tiga kolom: struktur catatan 5 item + tabel segmen 3-baris + transaksi pihak berelasi (stat + 3 breakdown) + Enhancing QC card = estimasi >80 kata visible — Severity HIGH, Effort L, Fix: Pisahkan: (a) struktur catatan + segmen, (b) related party + Enhancing QC.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1993–2083: list catatan INDF menggunakan `font-size:20px`; tabel segmen menggunakan `.tbl` (18px td); transaksi pihak berelasi menggunakan `font-size:19px`; Enhancing QC card menggunakan `font-size:19px` — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Grid 3 kolom masing-masing berisi 2 card = frame >85% terisi — Severity MED, Effort L, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 30 bukan penutup terakhir — slide 32 adalah penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 30 bukan penutup terakhir.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

Catatan laporan keuangan INDF adalah prop: mereka adalah enabler Enhancing QC. Tanpa catatan yang memadai tentang segmen, related party, dan risiko, angka di badan laporan keuangan tidak dapat diverifikasi atau dipahami secara penuh.

- [ ] **Konteks/Ketegangan:** "Angka Rp201,71T total aset dan Rp115,79T
      penjualan ada di badan laporan keuangan — tetapi *mengapa* dan *bagaimana*
      angka itu dihasilkan ada di catatan. Jika catatan tidak memadai,
      audiens memiliki angka tanpa konteks. Apakah catatan INDF 2024 memadai?"
- [ ] **Demonstrasi:** Struktur catatan INDF (5 kategori utama) disajikan
      dengan referensi halaman INDF AR 2024; tabel segmen menunjukkan
      disaggregasi yang memungkinkan Comparability; transaksi pihak berelasi
      Rp10,11T disajikan sebagai contoh Verifiability requirement.
- [ ] **Resolusi:** Interpretasi: catatan INDF 2024 memenuhi Enhancing QC —
      segmen disclosure memungkinkan Comparability antar divisi; catatan
      related party memungkinkan Verifiability; struktur catatan keseluruhan
      meningkatkan Understandability bagi primary users.
- [ ] **Per E3:** Daftar catatan tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini — namun Symbol
      bangunan dapat muncul sebagai mini-icon penanda transisi ke blok Close.
- [ ] **Slogan:** **APPLICABLE dan WAJIB** — per `specs/presentation-design-spec.md`
      bagian 2, slide 30 adalah lokasi kemunculan Slogan keempat (terakhir):
      "Conceptual Framework: konstitusi laporan keuangan." Verifikasi bahwa
      Slogan hadir di slide ini sebagai pembuka blok Contributions Close.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — catatan sebagai Enhancing QC enabler
      adalah demonstrasi terakhir bahwa Framework bekerja nyata.
- [ ] **Story:** APPLICABLE — slide 30 adalah node transisi "dari kasus ke
      sintesis/kontribusi" dalam arc.

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
