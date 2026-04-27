<!--
slide: 12
role: content
title: "Definisi Baru Aset & Liabilitas — SFAC 8 Ch. 4 (Goodwill INDF Rp52,2T)"
learning_objective: "Audiens dapat membandingkan definisi Aset SFAC 6 dengan definisi baru SFAC 8 Ch. 4, menjelaskan perubahan substantif (economic resource + present obligation), dan menerapkan uji definisi pada goodwill INDF Rp52,2T."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 Ch. 4 — definisi baru aset dan liabilitas; SFAC 6 — definisi lama"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 — goodwill Rp52,2T (26% total aset)"
assigned_to: "TBD"
rubric: rubrics/slide-12.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 12: Definisi Baru Aset & Liabilitas — SFAC 8 Ch. 4

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
> **v5 audit finding:** Dua tabel perbandingan SFAC 6 vs SFAC 8 Ch.4 (masing-masing 5–6 baris) + 2 box definisi liabilitas + tabel goodwill test 3-baris + catatan bawah = estimasi >80 kata visible — Severity HIGH, Effort L, Fix: Pisahkan: (a) definisi baru aset, (b) definisi baru liabilitas + INDF goodwill test.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 628–666: dua tabel perbandingan menggunakan `.tbl compact` (font 16px td, 12px th); box aplikasi INDF goodwill menggunakan `font-size:14px` (line 634, 666) — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Tiga card/tabel bertumpuk dalam grid 1fr 1fr + tabel bawah penuh lebar = frame hampir 90% terisi — Severity HIGH, Effort L, Fix: Pisahkan ke 2 slide.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 12 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 12 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA (goodwill test) + Slide konsep sulit: YA (definisi baru) — F5 wajib.**

Goodwill Rp52,2T adalah 26% total aset INDF — angka ini berfungsi sebagai prop untuk menguji definisi Aset SFAC 8. Apakah goodwill memenuhi definisi "economic resource controlled by the entity" per SFAC 8 Ch. 4?

- [ ] **Konteks/Ketegangan:** "Goodwill senilai Rp52,2T — setara 26% total
      aset INDF — adalah angka yang hanya ada di laporan keuangan, bukan
      di gudang atau pabrik. Apakah goodwill adalah 'aset' menurut SFAC 8,
      atau sekadar residual dari harga akuisisi?"
- [ ] **Demonstrasi:** Definisi Aset SFAC 6 vs SFAC 8 Ch. 4 disajikan secara
      komparatif; uji tiga kriteria (economic resource, controlled by entity,
      result of past event) diterapkan pada goodwill INDF dengan referensi
      INDF AR 2024.
- [ ] **Resolusi:** Interpretasi: goodwill INDF memenuhi definisi Aset SFAC 8
      karena merupakan economic resource (kemampuan menghasilkan arus kas dari
      sinergi akuisisi) yang dikontrol INDF dan berasal dari transaksi masa lalu
      (akuisisi CBP, Bogasari).
- [ ] **Per E3:** Tabel perbandingan definisi tanpa konteks/ketegangan dan
      resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** APPLICABLE — goodwill 26% total aset adalah angka yang
      mengejutkan; definisi baru SFAC 8 yang mengkonfirmasi goodwill sebagai
      Aset (bukan sekadar "catatan harga") adalah mini-Surprise.
- [ ] **Salient idea:** APPLICABLE — definisi elemen yang tepat adalah prasyarat
      untuk informasi yang berguna bagi pengambil keputusan.
- [ ] **Story:** APPLICABLE — slide 12 adalah node "uji definisi elemen dengan
      kasus INDF" dalam arc.

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
