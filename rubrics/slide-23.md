<!--
slide: 23
role: case
title: "Relevansi INDF — Predictive Value, Confirmatory Value, Materiality (Goodwill 26%)"
learning_objective: "Audiens dapat mengevaluasi tiga komponen Relevance (Predictive Value, Confirmatory Value, Materiality) terhadap disclosure segmented EBIT INDF dan goodwill Rp52,2T, serta menyimpulkan apakah disclosure INDF memenuhi standar Relevance per SFAC 8."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 8 QC6–QC10 — Relevance; QC11 — Materiality"
  - doc: indf-2024-ar
    ref: "INDF AR 2024 pp. 26–28 — EBIT segmen; goodwill Rp52,2T (26% total aset); EPS data"
assigned_to: "TBD"
rubric: rubrics/slide-23.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 23: Relevansi INDF — Predictive Value, Confirmatory Value, Materiality

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
> **v5 audit finding:** Tiga kolom: Predictive Value (chart EPS + teks) + Confirmatory Value (margin data + analisis) + Materiality (goodwill proporsi + bar chart) = estimasi >80 kata visible — Severity MED, Effort L, Fix: Pisahkan menjadi (a) Predictive + Confirmatory, (b) Materiality + síntesis.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 1268–1378: tiga kolom card menggunakan `font-size:18px` body dan `font-size:13px` untuk label; EPS bar chart menggunakan `font-size:13px` untuk tahun labels dan `font-size:13px` nilai — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Tiga kolom masing-masing penuh tinggi dengan teks + chart = frame hampir penuh — Severity MED, Effort L, Fix: Kurangi ke 2 kolom; pindahkan chart ke slide companion.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 23 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 23 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide kasus INDF: YA — F5 wajib.**

Per audit-deck-v5.md F5 section: "Slide 23 (Materiality) adalah pengecualian parsial: ia menyajikan angka goodwill Rp52,2T sebagai 26% total aset — ini adalah angka yang berfungsi sebagai prop karena skalanya mengejutkan. Namun arc-nya tetap tidak lengkap: tidak ada kalimat yang menetapkan ketegangan."

- [ ] **Konteks/Ketegangan:** "Goodwill Rp52,2T — satu seperempat seluruh aset
      INDF senilai Rp201T. Jika angka ini tidak material, tidak ada yang material.
      Namun goodwill tidak menghasilkan arus kas langsung — apakah ia tetap
      Relevan bagi investor yang menilai prospek INDF?"
- [ ] **Demonstrasi:** Tiga komponen Relevance disajikan dengan data INDF:
      Predictive Value (EPS deret waktu); Confirmatory Value (margin EBIT segmen);
      Materiality (goodwill 26% total aset). Semua dengan referensi halaman
      INDF AR 2024.
- [ ] **Resolusi:** Interpretasi: disclosure segmented EBIT memenuhi Predictive
      dan Confirmatory Value; goodwill Rp52,2T material secara kuantitatif
      (>5% total aset) — INDF telah menerapkan Relevance secara substansial
      meskipun impairment test goodwill memerlukan verifikasi lebih lanjut.
- [ ] **Per E3:** Tiga kolom data tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** APPLICABLE — goodwill 26% total aset adalah angka yang
      harus diframing sebagai Surprise Materiality.
- [ ] **Salient idea:** APPLICABLE — slide 23 langsung menguji Salient Idea:
      apakah informasi INDF benar-benar berguna bagi pengambil keputusan?
- [ ] **Story:** APPLICABLE — slide 23 adalah node "uji Relevance" dalam arc.

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
