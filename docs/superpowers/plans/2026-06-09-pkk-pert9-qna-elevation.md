# Elevasi Q&A Topik Khusus (Slide 20–24) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Menghasilkan satu dokumen Q&A antisipatif berisi lima pasangan Tanya-Jawab (slide 20–24) yang ditulis dengan register profesional-visioner sesuai pola "Elevasi Q&A Topik Khusus".

**Architecture:** Satu file Markdown deliverable, `rmk-pkk-pert9-income-statement/qa-topik-khusus.md`, ditaruh di akar folder proyek RMK (BUKAN di `content/`, agar tidak terbaca pipeline `build_docx.py` yang memindai `content/NN_*.md`). Setiap Q&A menerapkan pola 4 langkah dari spec `docs/superpowers/specs/2026-06-09-pkk-pert9-qna-elevation-design.md`.

**Tech Stack:** Markdown murni; tidak ada kode/build. "Test" tiap task = verifikasi terhadap checklist pola (4 langkah) + aturan nada.

**Adaptasi format:** Karena ini deliverable konten, siklus TDD diganti **tulis → verifikasi-terhadap-pola → commit**. Teks final ditulis lengkap di tiap task (tanpa placeholder).

---

## Checklist Verifikasi Pola (dipakai di setiap task)

Sebuah jawaban LULUS bila memenuhi semuanya:
- [ ] **Langkah 1** — membuka dengan prinsip konsep (representational faithfulness / matching / decision usefulness / economic consequences), bukan nomor standar.
- [ ] **Langkah 2** — ada satu kalimat *counterfactual* (apa yang rusak jika diperlakukan sebaliknya).
- [ ] **Langkah 3** — menyambung ke tujuan kerangka konseptual (daya banding / netralitas / kegunaan-keputusan / prediktabilitas).
- [ ] **Langkah 4** — klausa penutup berorientasi ke depan; **hook dijaga umum** (tanpa nama perusahaan, kasus, angka, atau nomor regulasi).
- [ ] **Nada** — *professor-voice*, Bahasa Indonesia, istilah teknis Inggris dicetak miring, 3–5 kalimat.

---

### Task 1: Buat file deliverable + Q&A slide 20

**Files:**
- Create: `rmk-pkk-pert9-income-statement/qa-topik-khusus.md`

- [ ] **Step 1: Tulis header + Q&A slide 20 (sudah final dari spec)**

```markdown
# Tanya-Jawab Antisipatif — Topik Khusus dalam Pengukuran Laba (Slide 20–24)

> RMK Pertemuan 9 — *The Income Statement* (Wolk et al., 2017, Ch. 12).
> Register: profesional-visioner; pola "Elevasi Q&A Topik Khusus" (4 langkah).
> Sumber pola & rasional: `docs/superpowers/specs/2026-06-09-pkk-pert9-qna-elevation-design.md`.

## Slide 20 — Prior Period Adjustment

**Q — Mengapa *prior period adjustment* dibebankan langsung ke saldo awal laba ditahan, bukan ke laba bersih tahun berjalan?**

**A —** Karena koreksi itu secara konseptual *milik* periode lalu: ia membetulkan kesalahan yang sudah terkunci di dalam laba periode sebelumnya, bukan buah dari kinerja manajemen tahun ini. Bila dipaksakan masuk ke laba berjalan, angka laba tahun ini bercampur dengan untung-rugi yang tidak dihasilkan aktivitas tahun ini — melanggar *representational faithfulness* sekaligus merusak daya banding antarperiode. Dengan menyesuaikan saldo awal laba ditahan secara retrospektif, laporan laba rugi tetap menjadi ukuran kinerja periode yang bersih. Dan justru di situ letak taruhannya: kredibilitas sebuah laba bergantung pada apakah pembaca bisa mempercayai bahwa angka itu menggambarkan apa yang dicapai perusahaan tahun ini — bukan warisan kesalahan masa lalu.
```

- [ ] **Step 2: Verifikasi terhadap checklist pola** (lihat blok Checklist di atas). Konfirmasi kelima butir terpenuhi.

- [ ] **Step 3: Commit**

```bash
git add "rmk-pkk-pert9-income-statement/qa-topik-khusus.md"
git commit -m "docs(rmk9): start Q&A topik khusus deliverable (slide 20)"
```

---

### Task 2: Q&A slide 21 — Earnings Per Share

**Files:**
- Modify: `rmk-pkk-pert9-income-statement/qa-topik-khusus.md` (append)

- [ ] **Step 1: Append Q&A slide 21**

```markdown

## Slide 21 — Earnings Per Share (EPS)

**Q — Mengapa EPS perlu distandardisasi seketat itu, padahal ia "hanya" satu angka ringkas?**

**A —** Justru karena EPS adalah *summary indicator* yang paling sering dikutip pasar — satu angka yang memadatkan seluruh kinerja menjadi nilai per lembar saham — maka kerapian definisinya menentukan segalanya. *Decision usefulness*-nya tinggi karena ringkas, tetapi keringkasan itu pula yang membuatnya rapuh: bila tiap perusahaan bebas menentukan sendiri penyebut dan cara memperlakukan efek dilutif, dua angka EPS yang tampak setara sebenarnya tidak dapat dibandingkan. Standardisasi yang ketat menutup celah itu agar daya banding antarperusahaan — bahkan antarnegara — tetap terjaga. Pelajarannya: makin sebuah angka diandalkan banyak pihak, makin tinggi taruhan pada keseragaman aturan yang melahirkannya.
```

- [ ] **Step 2: Verifikasi terhadap checklist pola.** Langkah 1 = *decision usefulness* (ringkas); Langkah 2 = "bila tiap perusahaan bebas… tidak dapat dibandingkan"; Langkah 3 = daya banding antarperusahaan/antarnegara; Langkah 4 = hook umum tentang keandalan angka, tanpa nomor regulasi.

- [ ] **Step 3: Commit**

```bash
git add "rmk-pkk-pert9-income-statement/qa-topik-khusus.md"
git commit -m "docs(rmk9): add Q&A slide 21 (EPS)"
```

---

### Task 3: Q&A slide 22 — Development Stage Enterprises

**Files:**
- Modify: `rmk-pkk-pert9-income-statement/qa-topik-khusus.md` (append)

- [ ] **Step 1: Append Q&A slide 22**

```markdown

## Slide 22 — Development Stage Enterprises

**Q — Mengapa perlakuan biaya ditentukan oleh sifat biayanya, bukan oleh jenis (status) perusahaannya?**

**A —** Karena yang menentukan ekonomi sebuah biaya adalah sifat biaya itu sendiri, bukan label perusahaan yang menanggungnya. Jika aturan dibedakan menurut jenis entitas — perusahaan tahap-rintis diistimewakan dibanding perusahaan mapan — maka dua biaya yang ekonominya identik akan dicatat berbeda hanya karena status pelakunya, dan daya banding antarentitas runtuh. *Rigid uniformity* di sini justru melindungi *representational faithfulness*: substansi transaksi yang sama dipetakan ke perlakuan yang sama. Pelajaran jangka panjangnya sederhana namun mendasar — begitu akuntansi mulai bertanya "siapa yang mencatat" alih-alih "apa yang terjadi", laporan kehilangan netralitasnya.
```

- [ ] **Step 2: Verifikasi terhadap checklist pola.** Langkah 1 = sifat biaya / *rigid uniformity*; Langkah 2 = "jika dibedakan menurut jenis entitas… daya banding runtuh"; Langkah 3 = daya banding + netralitas; Langkah 4 = hook umum "siapa vs apa", tanpa kasus.

- [ ] **Step 3: Commit**

```bash
git add "rmk-pkk-pert9-income-statement/qa-topik-khusus.md"
git commit -m "docs(rmk9): add Q&A slide 22 (development stage enterprises)"
```

---

### Task 4: Q&A slide 23 — Troubled Debt Restructuring

**Files:**
- Modify: `rmk-pkk-pert9-income-statement/qa-topik-khusus.md` (append)

- [ ] **Step 1: Append Q&A slide 23**

```markdown

## Slide 23 — Troubled Debt Restructuring

**Q — Mengapa mengukur restrukturisasi utang tanpa mendiskontokan arus kas masa depan disebut "kemenangan konsekuensi ekonomi atas kesetiaan representasional"?**

**A —** Karena mendiskontokan arus kas adalah cara mengakui bahwa uang yang diterima lebih lambat dan lebih sedikit bernilai lebih rendah hari ini — itu realitas ekonomi. Aturan awal mengabaikannya: selama jumlah nominal arus kas masa depan masih menutup nilai tercatat, untung-rugi dianggap nihil, sehingga kreditor yang sebenarnya menanggung kerugian bisa melaporkan seolah tak terjadi apa-apa. Hasilnya enak dipandang — beban kerugian tertunda — tetapi tidak setia pada substansi; di situlah "konsekuensi ekonomi" menang atas *representational faithfulness*. Pesan visionernya: standar yang dirancang agar angka terlihat nyaman justru paling perlu diwaspadai, sebab laporan yang menyenangkan secara politis belum tentu jujur secara ekonomi.
```

- [ ] **Step 2: Verifikasi terhadap checklist pola.** Langkah 1 = nilai waktu uang / realitas ekonomi; Langkah 2 = "selama nominal menutup nilai tercatat… seolah tak terjadi apa-apa"; Langkah 3 = *representational faithfulness* dikorbankan; Langkah 4 = hook umum tentang standar yang "tampak nyaman", tanpa nomor regulasi.

- [ ] **Step 3: Commit**

```bash
git add "rmk-pkk-pert9-income-statement/qa-topik-khusus.md"
git commit -m "docs(rmk9): add Q&A slide 23 (troubled debt restructuring)"
```

---

### Task 5: Q&A slide 24 — Early Extinguishment of Debt

**Files:**
- Modify: `rmk-pkk-pert9-income-statement/qa-topik-khusus.md` (append)

- [ ] **Step 1: Append Q&A slide 24**

```markdown

## Slide 24 — Early Extinguishment of Debt

**Q — Apa pelajaran dari satu item — pelunasan dini utang — yang berpindah klasifikasi tiga kali (luar biasa → operasi biasa → seperti luar biasa) dalam waktu singkat?**

**A —** Pelajarannya bukan soal mana klasifikasi yang "benar", melainkan soal harga dari ketidakstabilan itu sendiri. Bagaimana sebuah pos dikelompokkan — luar biasa atau operasi biasa — mengubah cara pembaca menilai apakah laba itu berkelanjutan; maka ketika satu item berpindah kelas tiga kali dalam waktu singkat, laba "inti" perusahaan bisa tampak naik-turun tanpa ada satu pun perubahan ekonomi yang nyata. Yang tergerus adalah daya banding antarperiode dan kemampuan pembaca memprediksi. Inilah pesan jangka panjangnya: konsistensi dan kejelasan alasan sebuah aturan sering lebih bernilai daripada penyempurnaan teknisnya, sebab standar yang labil membuat pengguna kesulitan memisahkan perubahan ekonomi dari sekadar perubahan aturan.
```

- [ ] **Step 2: Verifikasi terhadap checklist pola.** Langkah 1 = makna klasifikasi pos bagi keberlanjutan laba; Langkah 2 = "laba inti tampak naik-turun tanpa perubahan ekonomi"; Langkah 3 = daya banding antarperiode + prediktabilitas; Langkah 4 = hook umum "konsistensi > penyempurnaan teknis", tanpa kasus.

- [ ] **Step 3: Commit**

```bash
git add "rmk-pkk-pert9-income-statement/qa-topik-khusus.md"
git commit -m "docs(rmk9): add Q&A slide 24 (early extinguishment of debt)"
```

---

### Task 6: Review konsistensi lintas-lima Q&A

**Files:**
- Modify (jika perlu): `rmk-pkk-pert9-income-statement/qa-topik-khusus.md`

- [ ] **Step 1: Baca kelima Q&A berurutan.** Periksa:
  - Tidak ada pengulangan klausa penutup yang identik antar-jawaban (hook harus bervariasi).
  - Format judul `## Slide NN — Topik` seragam; bold `**Q —**` / `**A —**` konsisten.
  - Tiap jawaban 3–5 kalimat; istilah Inggris dicetak miring secara konsisten.
  - Tidak ada nama perusahaan/kasus/angka/nomor regulasi di klausa penutup (hook) mana pun.

- [ ] **Step 2: Perbaiki inline bila ada temuan.** Edit langsung; tidak perlu review ulang.

- [ ] **Step 3: Commit (hanya jika ada perubahan)**

```bash
git add "rmk-pkk-pert9-income-statement/qa-topik-khusus.md"
git commit -m "docs(rmk9): tighten Q&A consistency across slide 20-24"
```

---

## Self-Review (penulis plan)

**1. Spec coverage:**
- Spec §A (Q&A slide 20) → Task 1. ✓
- Spec §B (pola 4 langkah) → diterapkan & diverifikasi di Task 2–5; checklist pola eksplisit. ✓
- Spec §B tabel slide 21–24 (kerangka) → menjadi teks final di Task 2–5. ✓
- Spec "Kriteria keberhasilan" (4 langkah + nada + tanpa specifics) → checklist verifikasi tiap task + Task 6. ✓

**2. Placeholder scan:** Tidak ada "TBD/TODO"; semua teks Q&A final tertulis utuh. ✓

**3. Type consistency:** Konvensi penamaan seragam — heading `## Slide NN — Topik`, penanda `**Q —**` / `**A —**`, nama file `qa-topik-khusus.md` identik di semua task. ✓
