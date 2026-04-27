<!--
slide: 01
role: cover
title: "Cover — Kerangka Konseptual FASB: Fondasi Standar Pelaporan Keuangan"
learning_objective: "Audiens dapat mengidentifikasi topik, scope (SFAC 1–8, konvergensi IASB, INDF AR 2024), dan Empowerment Promise setelah 10 detik melihat slide ini."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 1–8 — scope presentasi"
  - doc: indf-2024-ar
    ref: "PT Indofood Sukses Makmur Tbk (IDX: INDF) — identitas studi kasus"
assigned_to: "TBD"
rubric: rubrics/slide-01.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 01: Cover — Kerangka Konseptual FASB: Fondasi Standar Pelaporan Keuangan

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
> **v5 audit finding:** Footer slide 01 (lines 132–143): nama 6 anggota lengkap + NIM + judul institusi + tahun akademik = estimasi 45+ kata di area bawah slide, di luar konten utama — Severity MED, Effort M, Fix: Pindahkan anggota ke slide dedikasi atau hapus NIM — cover cukup nama tanpa NIM dan detail institusi.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** CSS global line 32: `.t-h5{font-size:26px}`, line 33: `.t-lead{font-size:26px}`, line 34: `.t-body{font-size:22px}`, line 37: `.t-label{font-size:13px}`, line 38: `.t-meta{font-size:16px}` — slide 01 menggunakan `.t-meta`, `.t-label` (lines 119–141) untuk semua nama anggota, detail institusi — Severity HIGH, Effort XL, Fix: Redesign global typography system: tetapkan minimum body text 40pt; per E4: angkat ke Phase 4 redesign requirement.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild. (Logo STIE dan INDF di slide cover adalah posisi yang tepat per Crime #8 = 0.)

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 01 adalah cover, bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 01 adalah cover, bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claire/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: TIDAK | Slide konsep sulit: TIDAK — F5 trigger inactive.**

Slide 01 adalah cover deck. Tidak mengandung angka INDF AR maupun konsep FASB yang sulit. Bagian ini selesai.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

Slide ini menguatkan elemen STAR mana?

- [ ] **Symbol:** Slide ini menampilkan atau secara eksplisit merujuk Symbol
      deck (bangunan tiga lantai: fondasi = Conceptual Framework, tiang =
      Qualitative Characteristics, atap = Financial Statements)?
      **APPLICABLE** — per spec, Symbol bangunan tiga lantai diperkenalkan di
      slide cover (ukuran penuh). Verifikasi pada rebuild bahwa visual Symbol
      hadir di slide 01.
- [ ] **Slogan:** Slogan deck muncul di slide ini (secara verbal atau visual)?
      **NOT APPLICABLE pada slide 01** — per spec, Slogan pertama muncul di
      slide 2 (Agenda/Empowerment Promise). Slide 01 adalah cover; Slogan
      tidak wajib di sini, tetapi tidak dilarang jika desain memungkinkan.
- [ ] **Surprise:** Slide ini membongkar kebenaran kontra-intuitif yang
      menentang asumsi awam tentang FASB atau pelaporan keuangan INDF?
      **NOT APPLICABLE pada slide 01** — Surprise ditempatkan di slides awal
      (opening hook), tetapi slide cover bukan lokasi Surprise utama.
- [ ] **Salient idea:** Slide ini berkontribusi ke salient idea deck-level,
      bukan menjadi tangent yang tidak berhubungan dengan inti deck?
      **APPLICABLE** — cover menetapkan identitas topik yang konsisten dengan
      Salient Idea: FASB CF sebagai konstitusi laporan keuangan.
- [ ] **Story:** Slide ini adalah node yang teridentifikasi dalam story arc
      deck (konteks INDF → analisis FASB → evaluasi → implikasi)?
      **APPLICABLE** — slide 01 adalah titik awal arc (opening node).

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
