<!--
slide: 06
role: content
title: "Karakteristik Kualitatif — Hierarki SFAC 2"
learning_objective: "Audiens dapat menggambarkan hierarki QC SFAC 2 (Relevance, Reliability, dan komponen masing-masing) dan menjelaskan posisi Neutrality sebagai komponen FUNDAMENTAL Reliability sebelum SFAC 8 merevisinya."
sources:
  - doc: fasb-conceptual-framework
    ref: "SFAC 2 — hierarki QC; Wolk (2017) Ch. 7 Exhibit 7.1"
  - doc: week-05-materials
    ref: "Week 5 Exercise — QC hierarchy SFAC 2 vs SFAC 8"
assigned_to: "TBD"
rubric: rubrics/slide-06.md
last_reviewed: 2026-04-27
-->

# Rubric — Slide 06: Karakteristik Kualitatif — Hierarki SFAC 2

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
> **v5 audit finding:** Diagram hierarki + 6 box komponen + catatan bawah line 370: "Tanpa memahami SFAC 2 — perubahan di SFAC 8 tidak akan terasa signifikan. Verifiability di sini adalah komponen FUNDAMENTAL Keandalan..." = >20 kata dalam catatan saja; total visible >50 kata — Severity MED, Effort M, Fix: Hapus catatan bawah; letakkan di speaker notes. Sederhanakan diagram ke nama saja tanpa deskripsi.

- [ ] **Crime #3 — Font ≥40pt:** Verifikasi tidak ada teks yang harus dibaca
      audiens dengan ukuran <40pt. Footnote sumber diizinkan ≥24pt tetapi
      tidak boleh memuat konten substantif.
> **v5 audit finding:** Lines 344–368: hierarki QC SFAC 2 menggunakan boxes dengan `font-size:20px` dan `font-size:21px` untuk label, dan `font-size:12px` untuk subtext; bottom text (line 370) menggunakan `.t-body-sm` = 18px — Severity HIGH, Effort XL, Fix: Per E4: Phase 4 redesign.

- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide kosong.
      White space adalah breathing room bagi otak audiens, bukan ruang sia-sia.
> **v5 audit finding:** Diagram hierarki vertikal + 2 kolom besar + 6 komponen boxes + catatan bawah = seluruh frame penuh; tidak ada white space — Severity MED, Effort L, Fix: Sederhanakan diagram; hapus sub-label di setiap box.

- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo ganda,
      atau gradient yang mengganggu fokus. Logo institusi hanya muncul di
      slide 1 (cover) dan slide 32 (contributions close).
> **v5 audit:** No violation found — confirm on rebuild.

- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini adalah slide
      penutup deck, isinya BUKAN daftar nama anggota kelompok.
> **v5 audit:** No violation found — confirm on rebuild. (Slide 06 bukan penutup.)

- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini adalah slide
      penutup deck, isinya BUKAN "Terima Kasih" atau "Pertanyaan?". Slide
      penutup wajib berisi kontribusi konkret (per F4).
> **v5 audit:** No violation found — confirm on rebuild. (Slide 06 bukan penutup.)

---

## 3. F5 Trigger — Props & Stories

> Referensi: `.claude/winston-framework.md` bagian F5; aturan E3 di
> `specs/winston-integration-rules.md`.

**Slide konsep sulit: YA — F5 wajib.**

Hierarki QC SFAC 2 adalah konsep sulit karena memperkenalkan Verifiability sebagai komponen FUNDAMENTAL Reliability — sebuah relasi yang dibalik oleh SFAC 8 (Verifiability menjadi Enhancing QC, bukan Fundamental). Perbedaan ini tidak intuitif.

- [ ] **Konteks/Ketegangan:** "Jika Verifiability adalah komponen Reliability
      di SFAC 2, mengapa SFAC 8 memindahkannya ke kategori 'enhancing' —
      bukan 'fundamental'? Apakah ini melemahkan standar verifikasi?"
- [ ] **Demonstrasi:** Diagram hierarki SFAC 2 disajikan dengan label eksplisit
      komponen (Relevance → Predictive Value + Feedback Value + Timeliness;
      Reliability → Verifiability + Representational Faithfulness + Neutrality)
      dengan referensi SFAC 2.
- [ ] **Resolusi:** Satu kalimat: pergeseran ini bukan melemahkan — SFAC 8
      mengintegrasikan Verifiability ke dalam Faithful Representation secara
      implisit, mempertegas bahwa FR harus dapat diverifikasi tanpa menjadikannya
      syarat independen.
- [ ] **Per E3:** Diagram hierarki tanpa konteks/ketegangan dan resolusi = E3.

---

## 4. STAR Alignment (deck-level F3 cek)

> Referensi: `specs/presentation-design-spec.md` bagian 2 (STAR Core Idea).

- [ ] **Symbol:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Slogan:** NOT APPLICABLE — per spec, Slogan wajib di slides 2, 7, 19, 30.
- [ ] **Surprise:** NOT APPLICABLE sebagai elemen utama slide ini.
- [ ] **Salient idea:** APPLICABLE — QC SFAC 2 adalah fondasi hierarki yang
      mendukung Salient Idea: Framework sebagai standar tunggal untuk menilai
      "berguna."
- [ ] **Story:** APPLICABLE — slide 06 adalah node teori QC dalam arc.

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
