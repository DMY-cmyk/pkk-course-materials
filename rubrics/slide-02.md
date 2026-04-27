<!--
slide: 02
role: agenda
title: "Agenda Presentasi"
learning_objective: "Audiens dapat menyebut delapan bagian agenda dan menghubungkan setiap bagian ke Empowerment Promise deck setelah melihat slide ini selama 30 detik."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 1–8 — kerangka urutan agenda"
  - doc: week-05-materials
    ref: "Week 5 Exercise — urutan topik yang ditekankan"
assigned_to: "TBD"
rubric: rubrics/slide-02.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 02: Agenda Presentasi

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
> **v5 audit finding:** Agenda 8 baris mencakup 8 bagian termasuk "Sintesis Teori" (slides 19–20) dan "Penutup & Kesimpulan" (31–32) sebagai bagian terpisah. Dengan 32 slide untuk presentasi ~43 menit, jumlah bagian dan slide yang ada berpotensi melebihi ambang batas optimal — Severity LOW, Effort L, Fix: Pertimbangkan menggabungkan "Sintesis Teori" dengan "Penutup"; hilangkan satu segmen untuk memperpadat alur.

- [ ] **Crime #2 — Too many words:** Jumlah kata di body slide ≤25 kata.
      Kalimat berlebih dipindahkan ke catatan presenter, bukan dihapus.
> **v5 audit finding:** Tabel agenda 8 baris (lines 163–170): setiap baris berisi nama bagian + slide range + durasi; body agenda melebihi 25 kata termasuk keterangan "~43 menit" dan 8 bagian bernama — Severity MED, Effort M, Fix: Sederhanakan ke 5–6 bagian maksimum; hapus kolom Durasi jika slide terlalu padat.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Sama dengan #3 global: `.t-body` 22px, `.t-meta` 16px, `.t-label` 13px — digunakan di header tabel agenda (lines 157–160) dengan `font-size:13px` eksplisit — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Tabel 8 baris penuh + header "≥43 menit" + judul "Agenda Presentasi" mengisi >75% frame; sangat sedikit ruang putih di sisi kiri/kanan dan antarbaris — Severity MED, Effort M, Fix: Rancang ulang agenda sebagai grid visual 2×4 dengan ikon; kurangi ke 6 item maksimum.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 02 adalah agenda, bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 02 adalah agenda, bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: TIDAK | Slide konsep sulit: TIDAK — F5 trigger inactive.**

Slide 02 adalah agenda presentasi. Tidak mengandung angka INDF AR maupun konsep FASB yang sulit. Bagian ini selesai.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

Slide ini menguatkan elemen STAR mana?

- [ ] **Symbol:** Slide ini menampilkan atau secara eksplisit merujuk Symbol
      deck (bangunan tiga lantai: fondasi = Conceptual Framework, tiang =
      Qualitative Characteristics, atap = Financial Statements)?
      **NOT APPLICABLE sebagai elemen utama** — Symbol tidak wajib di agenda,
      tetapi dapat muncul sebagai mini-icon di pojok slide divider. Verifikasi
      pada rebuild.
- [ ] **Slogan:** Slogan deck muncul di slide ini (secara verbal atau visual)?
      **APPLICABLE dan WAJIB** — per `specs/presentation-design-spec.md`
      bagian 2 (Slogan), slide 2 adalah lokasi kemunculan Slogan pertama:
      "Conceptual Framework: konstitusi laporan keuangan." Verifikasi bahwa
      Slogan hadir secara visual atau verbal di slide ini.
- [ ] **Surprise:** Slide ini membongkar kebenaran kontra-intuitif yang
      menentang asumsi awam tentang FASB atau pelaporan keuangan INDF?
      **NOT APPLICABLE** — agenda adalah peta perjalanan, bukan lokasi Surprise.
- [ ] **Salient idea:** Slide ini berkontribusi ke salient idea deck-level,
      bukan menjadi tangent yang tidak berhubungan dengan inti deck?
      **APPLICABLE** — agenda menstrukturkan perjalanan dari teori ke bukti
      INDF, konsisten dengan Salient Idea: CF sebagai alat analisis operasional.
- [ ] **Story:** Slide ini adalah node yang teridentifikasi dalam story arc
      deck (konteks INDF → analisis FASB → evaluasi → implikasi)?
      **APPLICABLE** — slide agenda adalah "peta arc" yang membantu audiens
      menempatkan setiap node berikutnya dalam alur naratif.

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
