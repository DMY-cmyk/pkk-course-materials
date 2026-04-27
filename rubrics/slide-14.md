<!--
slide: 14
role: content
title: "Pengakuan — SFAC 5 vs SFAC 8 Ch. 5 (Recognition vs Disclosure)"
learning_objective: "Audiens dapat menyebutkan empat kriteria pengakuan SFAC 5 dan tiga kriteria SFAC 8 Ch. 5, serta menjelaskan kapan pengakuan lebih tepat dari disclosure dengan contoh konkret dari praktik INDF."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 5 — empat kriteria pengakuan; SFAC 8 Ch. 5, RD3 — kriteria revised"
  - doc: week-05-materials
    ref: "Week 5 Exercise — recognition criteria dan recognition vs disclosure"
assigned_to: "TBD"
rubric: rubrics/slide-14.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 14: Pengakuan — SFAC 5 vs SFAC 8 Ch. 5 (Recognition vs Disclosure)

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
> **v5 audit finding:** Dua card besar (SFAC 5 empat kriteria, SFAC 8 Ch.5 tiga kriteria) masing-masing berisi deskripsi + 3–4 item; ditambah tabel Recognition vs Disclosure 3-baris = estimasi >80 kata visible — Severity HIGH, Effort L, Fix: Pisahkan SFAC 5 vs SFAC 8 Ch.5 comparison (slide 14a) dari Recognition vs Disclosure (slide 14b).

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 731–769: card SFAC 5 dan SFAC 8 Ch.5 menggunakan `font-size:21px` untuk body text per item, `font-size:20px` untuk deskripsi, `font-size:17px` untuk catatan RD3; tabel Recognition vs Disclosure menggunakan `.tbl compact` 16px/12px — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Dua card besar baris atas + tabel penuh lebar bawah = >85% frame terisi — Severity MED, Effort M, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 14 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 14 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Perbedaan Recognition vs Disclosure adalah salah satu konsep paling sulit dalam Framework: kapan sesuatu cukup "diungkapkan dalam catatan" vs harus "diakui di badan laporan keuangan"? Ini memiliki implikasi besar pada angka-angka laporan INDF.

- [ ] **Konteks/Ketegangan:** "Sebuah kontrak sewa dengan nilai present value
      Rp10 miliar — apakah cukup dicatat di notes (disclosure) atau harus
      masuk ke neraca sebagai liabilitas (recognition)? Perbedaan ini
      mengubah rasio utang INDF secara dramatis."
- [ ] **Demonstrasi:** Empat kriteria SFAC 5 dan tiga kriteria SFAC 8 Ch. 5
      disajikan komparatif; tabel Recognition vs Disclosure menunjukkan
      perbedaan konsekuensi informasional; RD3 dikutip dengan referensi
      paragraf.
- [ ] **Resolusi:** Interpretasi: SFAC 8 menyederhanakan dari 4 ke 3 kriteria
      karena "probable future economic benefits" sudah tercakup dalam definisi
      elemen — pengakuan terjadi ketika informasi menghasilkan manfaat yang
      melebihi biaya dan memenuhi definisi elemen.
- [ ] **Per E3:** Tabel perbandingan tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — recognition criteria menentukan kapan
      informasi "berguna bagi pengambil keputusan" masuk ke laporan formal.
- [ ] **Story:** APPLICABLE — slide 14 adalah node "kriteria pengakuan" dalam arc.

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
