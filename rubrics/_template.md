<!--
slide: NN
role: [cover|agenda|section-divider|content|case|chart|table|quote|synthesis|qanda]
title: "..."
learning_objective: "..."
sources:
  - doc: fasb-conceptual-framework
    ref: "Chapter X, QCY–QCZ"
assigned_to: "member-name"
rubric: rubrics/slide-NN.md
last_reviewed: YYYY-MM-DD
-->

# Rubric — Slide NN: [Judul]

> Template universal. Setiap rubrik slide individual (`slide-01.md` ...
> `slide-32.md`) menyalin struktur ini dan mengisi setiap section.

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
- [ ] **Crime #2 — Too many words:** Jumlah kata di body slide ≤25 kata.
      Kalimat berlebih dipindahkan ke catatan presenter, bukan dihapus.
- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

- [ ] **Apakah slide ini termasuk salah satu kategori berikut?**
  - Slide kasus INDF — mengandung angka dari INDF Annual Report 2024
    (role `case`, `chart`, atau `table` dengan data AR)
  - Slide konsep sulit — memperkenalkan konsep FASB yang sulit
    dipahami secara intuitif (mis. going concern, faithful representation,
    materiality, measurement uncertainty)

Jika TIDAK: bagian ini selesai. Lanjut ke Section 4.

Jika YA, slide WAJIB mengikuti story arc tiga-tahap F5:

- [ ] **Konteks/Ketegangan:** Slide menetapkan mengapa angka atau konsep
      ini penting — satu kalimat atau visual yang menimbulkan pertanyaan
      analitis sebelum jawaban disajikan. Contoh: "EBIT Agribusiness naik
      73% — apakah kenaikan ini mencerminkan realitas ekonomi secara
      faithful?"
- [ ] **Demonstrasi:** Angka spesifik dari INDF AR 2024 atau contoh konkret
      disajikan (tabel, grafik, atau kutipan) dengan referensi halaman.
      Judul tabel mengandung pertanyaan analitis, bukan sekadar label
      deskriptif.
- [ ] **Resolusi:** Satu atau dua kalimat interpretasi eksplisit berbasis
      konsep FASB — menyebut karakteristik kualitas mana yang terpenuhi
      atau tidak terpenuhi, bukan sekadar merangkum angka.
- [ ] **Per E3:** Untuk slide kasus, angka adalah prop. Tabel polos tanpa
      konteks/ketegangan dan resolusi FASB = pelanggaran ganda (kekosongan
      naratif + E3).

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).
> Slide tidak harus mengaktifkan semua elemen STAR. Pertanyaan ini adalah
> cek *konsistensi* dengan STAR deck-level yang sudah ditetapkan.

Slide ini menguatkan elemen STAR mana?

- [ ] **Symbol:** Slide ini menampilkan atau secara eksplisit merujuk Symbol
      deck (bangunan tiga lantai: fondasi = Conceptual Framework, tiang =
      Qualitative Characteristics, atap = Financial Statements)? Catatan:
      Symbol harus muncul di minimal 3 slide dalam seluruh deck.
- [ ] **Slogan:** Slogan deck muncul di slide ini (secara verbal atau
      visual)? Catatan: target kemunculan slogan minimal 3 kali di seluruh
      deck — verifikasi di slide 2, 7, 19, dan 30.
- [ ] **Surprise:** Slide ini membongkar kebenaran kontra-intuitif yang
      menentang asumsi awam tentang FASB atau pelaporan keuangan INDF?
- [ ] **Salient idea:** Slide ini berkontribusi ke salient idea deck-level,
      bukan menjadi tangent yang tidak berhubungan dengan inti deck?
- [ ] **Story:** Slide ini adalah node yang teridentifikasi dalam story arc
      deck (konteks INDF → analisis FASB → evaluasi → implikasi)?

---

## 5. FASB Supremacy Verifikasi (E1)

> Referensi: `specs/winston-integration-rules.md` bagian E1 — Klausul
> Supremasi FASB (TEGAS). Substansi FASB SELALU menang atas Winston.

- [ ] Substansi FASB di slide ini tidak dikorbankan demi gaya Winston.
      Definisi, komponen, dan contoh kasus FASB yang dimandatkan tampil
      utuh — tidak dipersingkat untuk memenuhi batas kata Winston.
- [ ] Bila ada konflik yang terdeteksi (mis. F2 Crime #2 ≤25 kata vs
      definisi FASB yang lebih panjang): definisi FASB tetap utuh dan
      resolusi telah diterapkan — pertimbangkan split ke dua slide (satu
      slide definisi, satu slide ilustrasi kasus INDF). Resolusi wajib
      dicatat secara eksplisit di rubrik slide ini.

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
