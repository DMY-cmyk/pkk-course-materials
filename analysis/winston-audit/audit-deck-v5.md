# Winston Framework Audit — Deck v5 (Narrative)

**Audit date:** 2026-04-27
**Source file:** `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html`
**Companion docs:**
- `crime-inventory.md` — tabel slide × crime (98 entries, 32 slides)
- `revision-priorities.md` — tier HIGH/MED/LOW + E4 escalation
- `delivery-checklist.md` — delivery crimes presenter (T9, akan dibangun setelah ini)

**Cakupan naratif:** Evaluasi v5 terhadap kelima framework Winston (F1–F5)
dengan bukti konkret. Mencakup area di mana v5 sudah selaras dan area
yang melanggar.

---

## F1 — Start Right Audit

### Apa yang sudah selaras

Slide 01 (lines 112–145) memiliki beberapa elemen yang memenuhi standar F1. Pertama, terdapat identifikasi topik yang jelas dan terarah: headline utama berbunyi "Kerangka Konseptual FASB: Fondasi Standar Pelaporan Keuangan" (line 128–129), disertai sub-judul yang langsung menetapkan scope studi kasus — "PT Indofood Sukses Makmur Tbk (IDX: INDF) sebagai Studi Kasus / SFAC 1 hingga SFAC 8 · Konvergensi IASB · Laporan Tahunan 2024" (line 130). Scope ini bukan deskripsi samar; ia menyebut rentang SFAC secara eksplisit, nama perusahaan, dan tahun laporan. Audiens mendapatkan informasi orientasi yang memadai dalam satu baris.

Kedua, v5 tidak membuka dengan "terima kasih" pada slide pertama. Slide 01 langsung pada judul dan identitas penyusun — elemen yang oleh Winston dikategorikan sebagai defect fatal bila diletakkan di awal ditiadakan dari posisi dominan cover.

Ketiga, terdapat penanda konteks institusional yang tepat: pill "MNK202 · Pelaporan Keuangan Korporat" (line 126) menginformasikan audiens tentang konteks mata kuliah, yang secara implisit menetapkan standar akademik yang diharapkan. Identitas dua logo (STIE YKPN dan INDF) pada slide 01 merupakan satu-satunya lokasi logo dalam seluruh deck — selaras dengan Crime #8 = 0.

### Pelanggaran ditemukan

**Tidak ada Empowerment Promise.** Winston F1 mensyaratkan satu pernyataan spesifik tentang apa yang akan diketahui audiens di akhir presentasi yang tidak mereka ketahui di awal — bukan sekadar label topik. Slide 01 tidak mengandung kalimat bertipe "Setelah presentasi ini, Anda akan mampu membaca laporan keuangan INDF 2024 dan mengidentifikasi di mana kerangka konseptual FASB bekerja secara operasional." Yang ada adalah judul deskriptif, bukan promise fungsional. Ini adalah ketidakhadiran yang bersifat struktural, bukan sekadar omisi kosmetik.

**Footer slide 01 memuat daftar 6 anggota beserta NIM** (lines 135–142): setiap anggota memiliki nomor urut, nama, dan NIM dengan font 15px (nama) dan 12px (NIM). Menurut F1, segala sesuatu yang tidak melayani empowerment promise harus dieliminasi dari pembukaan. Daftar anggota di footer cover adalah informasi administratif yang mengalihkan perhatian dari pesan pembuka; hal ini juga merupakan Crime #2 (>45 kata di area bawah, per crime-inventory.md slide 01 baris 2).

**Sub-judul di line 130 menggunakan font-size 26px** — termasuk dalam Crime #3 (font <40pt) sebagaimana dicatat dalam crime-inventory.md slide 01 baris 1. Meskipun ukuran 26px secara teknis dapat dibaca dari jarak dekat, dalam proyeksi 1920×1080px di ruang kelas, teks 26px pada jarak audiens rata-rata 5–8 meter tidak memenuhi threshold keterbacaan Winston 40pt.

**Slide 03 (lines 177–xx) berfungsi sebagai konteks sejarah**, bukan sebagai slide yang membangun promise. Dalam arsitektur F1, 60 detik pertama harus berisi promise + konteks + mengapa ini penting sekarang. v5 langsung masuk ke kronologi CAP–APB–FASB tanpa menegaskan secara eksplisit mengapa kronologi itu relevan bagi audiens dalam mata kuliah ini.

### Rekomendasi

Revisi slide 01 ke v6 wajib menambahkan satu elemen Empowerment Promise yang berdiri sendiri — setidaknya satu kalimat outcome-driven di bawah headline, sebelum sub-judul teknis. Contoh kandidat (akan difinalisasi oleh tim): "Setelah presentasi ini, Anda akan memahami mengapa INDF 2024 — konglomerat Rp115,79T — melaporkan goodwill Rp52,2T sebagai aset bukan beban, dan bagaimana FASB Conceptual Framework menentukan batas itu." Daftar anggota dipindahkan ke slide dedikasi atau hanya disebut di chrome footer. Detail revisi: revision-priorities.md Tier 1a slides 01 (Crime #2), Tier 1b slide 01 (Crime #3 → E4 Phase 4).

---

## F2 — Slide Crimes Audit (Ringkasan Naratif)

> Detail per-slide ada di `crime-inventory.md`. Bagian ini hanya naratif
> agregat.

### Apa yang sudah selaras

**Crime #8 = 0 occurrences** — ini adalah satu-satunya crime yang tidak ditemukan di seluruh deck. Logo (STIE YKPN dan INDF) hanya muncul di slide 01 (cover), tepat sesuai aturan Winston: logo tidak boleh menghiasi setiap slide karena menjadi background clutter yang menurunkan fokus audiens. Elemen dekoratif lain yang berpotensi masuk kategori ini — pattern grid geometris (`.grid-bg`, lines 76–77) dengan opasitas 4–5% — dievaluasi dan dikecualikan karena tidak mengganggu keterbacaan teks (opasitas terlalu rendah untuk menjadi "clutter"). Kesimpulan dari crime-inventory.md (catatan audit, Crime #8): "deck ini sudah bersih dari logo dan clutter berlebih."

Selain itu, slide-slide INDF case (slides 21–30) menampilkan angka dalam card yang terstruktur dengan warna yang berbeda per divisi (CBP: biru, Bogasari: amber, Agri: hijau, Distribusi: ungu), yang merupakan sistem penanda visual yang konsisten — meskipun sistem ini belum mencapai level "Symbol" F3, ia menunjukkan kesadaran desain yang baik.

### Crime paling sering muncul

**Crime #3 (Font <40pt) = 32 occurrences** — hadir di setiap satu dari 32 slide tanpa pengecualian. Ini adalah crime tunggal paling sering dalam deck.

Urutan crime berdasarkan frekuensi (dari crime-inventory.md Per-Crime Frequency):

| Crime | Occurrences |
|-------|-------------|
| #3 Font <40pt | 32 |
| #2 Too many words | 31 |
| #7 No white space | 30 |
| #1 Too many slides | 3 |
| #9 Collaborators as final slide | 1 |
| #10 "Thank you" as final slide | 1 |
| #8 Background clutter / logos | **0** |

### Slide paling bermasalah

Tiga slide dengan jumlah crime terbanyak (berdasarkan crime-inventory.md):

1. **Slide 07** — 3 crimes: #3 (HIGH-XL), #2 (HIGH-L), #7 (HIGH-L). Slide ini memiliki dua kolom dengan kepadatan sangat tinggi: kolom kiri diagram hierarki SFAC 8 + 6 komponen boxes, kolom kanan 5 "Transformasi Kunci" cards bertumpuk — estimasi >100 kata visible, frame hampir penuh.

2. **Slide 10** — 3 crimes: #3 (HIGH-XL), #2 (HIGH-L), #7 (HIGH-L). Grid 2×2 dengan 4 QC peningkat masing-masing berisi body text 15px — ukuran font terkecil dalam seluruh deck, yang secara langsung membuktikan bahwa konten dipaksakan masuk. Cost Constraint panel di bawah menambah kepadatan.

3. **Slide 19** — 3 crimes: #3 (HIGH-XL), #2 (HIGH-L), #7 (HIGH-L), ditambah #1 (LOW-M). Slide ini menampilkan grid 4×2 delapan chapter cards masing-masing dengan 2–3 kalimat deskripsi, ditambah timeline narasi di bagian bawah — estimasi >120 kata visible, frame hampir penuh. Ini adalah slide dengan word count tertinggi dalam deck.

Slide lain yang sama-sama memiliki 3 crimes berat: 03, 12, 15, 18, 28, 30, 31.

### Pola sistemik

**Crime #3 muncul di 32/32 slide — ini bukan defect lokal melainkan defect sistemik pada design system global.** CSS root (lines 28–38 v5.html) menetapkan seluruh hierarki tipografi konten informasional di bawah threshold Winston 40pt:

```css
/* Global CSS lines 28–38 — SEMUA sub-40px kecuali .t-h1/.t-h2/.t-h3 */
.t-h4  { font-size: 34px }  /* heading sekunder — sub-40pt */
.t-h5  { font-size: 26px }  /* heading tersier — sub-40pt */
.t-lead{ font-size: 26px }  /* subtitle/lead text SETIAP slide — sub-40pt */
.t-body{ font-size: 22px }  /* body text SETIAP slide — sub-40pt */
.t-body-sm{ font-size: 18px } /* caption/detail SETIAP slide — sub-40pt */
.t-label  { font-size: 13px } /* label/tag SETIAP slide — sub-40pt */
.t-meta   { font-size: 16px } /* metadata SETIAP slide — sub-40pt */
```

Hanya `.t-h1` (96px), `.t-h2` (68px), dan `.t-h3` (48px) yang memenuhi threshold — dan ketiga kelas ini hanya dipakai untuk judul utama slide. Seluruh konten informasional (body text, bullet points, tabel, card content, label, metadata) menggunakan kelas-kelas sub-40px. Crime-inventory.md mengkonfirmasi: 573 dari 587 deklarasi `font-size` dalam file menggunakan ukuran di bawah 40px (97,6%).

Ini berarti Crime #3 bukan dapat diselesaikan dengan patch per-slide di v6 — ia memerlukan redesign typography system dari nol sebagai prerequisite Phase 4 (per revision-priorities.md E4 Escalation Summary).

**Crime #2 (Too many words) muncul di 31/32 slide** — hanya 1 slide yang tidak memiliki crime ini. Pola kepadatan kata bukan pilihan editorial per slide, melainkan konsekuensi dari pendekatan desain yang mencoba memuat keseluruhan materi SFAC ke dalam 32 slide tanpa split. Ini adalah pola sistemik kedua.

**Crime #7 (No white space) muncul di 30/32 slide** — konsekuensi langsung dari Crime #2: ketika terlalu banyak konten masuk satu slide, breathing room tereliminasi.

### Rekomendasi

Detail lengkap di revision-priorities.md. Ringkasan: 23 HIGH non-XL (patch v6), 32 HIGH-XL (Phase 4 redesign), 40 MED (patch v6), 3 LOW (opsional). Prioritas utama: (1) redesign global typography system sebagai prerequisite semua yang lain; (2) slide 32 (Crime #9 + #10 — most visible impact); (3) slides 03, 04, 05, 07, 10, 12, 14, 15, 18, 19, 21, 28, 30, 31 (HIGH non-XL, content split diperlukan).

---

## F3 — STAR Audit

### Symbol

**Tidak ada Symbol yang dapat dikenali.** Winston mendefinisikan Symbol sebagai visual atau objek yang merepresentasikan ide secara instan dan dapat dikenali lintas slide. Dalam v5, tidak ada elemen visual tunggal yang berulang di semua slide sebagai penanda identitas deck. Logo INDF dan STIE hanya muncul di slide 01 (sesuai aturan Crime #8). Sistem warna per divisi (biru/CBP, amber/Bogasari, hijau/Agri, ungu/Distribusi) digunakan di slides 21–30 tetapi tidak merupakan Symbol karena: (a) hanya muncul di bagian Studi Kasus, tidak di keseluruhan deck; (b) tidak merepresentasikan ide inti kerangka konseptual FASB, melainkan hanya identitas bisnis anak perusahaan.

Yang ada adalah konsistensi gaya visual (palette navy-400 + blue-500, card system, chrome footer), tetapi konsistensi gaya belum setara dengan Symbol. Symbol harus menjadi satu elemen visual yang, ketika dilihat, langsung memicu asosiasi dengan ide inti. v5 tidak memiliki ini.

**Implikasi untuk v6/Phase 4:** Symbol perlu dirancang. Kandidat: diagram kerangka SFAC 8 tereduksi (8 chapter sebagai 8 node) yang diulang sebagai mini-map di setiap slide divider, atau ikon "jembatan" yang merepresentasikan hubungan teori–praktik (FASB ↔ INDF).

### Slogan

**Tidak ada Slogan yang dapat diidentifikasi.** Pencarian dalam v5.html tidak menemukan satu frasa pendek yang diulang di multiple slides sebagai "handle" audiens. Chrome footer di setiap slide berbunyi "Kelompok 3 · [Nama Bagian]" (contoh: line 174 "Kelompok 3 · FASB CF x INDF 2024", line 967 "Kelompok 3 · Sintesis Teori · SFAC 8 Arsitektur Lengkap") — ini adalah metadata navigasi, bukan Slogan. Sebuah Slogan harus dapat diulang oleh audiens dalam meeting tanpa penjelasan tambahan.

Slide 31 (line 2153) memuat kalimat: "INDF 2024 membuktikan bahwa FASB Conceptual Framework bukan dokumen normatif yang abstrak, melainkan peta jalan operasional yang bekerja nyata di perusahaan multinasional skala Rp115,79T." Ini adalah kandidat Salient Idea yang kuat (lihat sub-seksi di bawah), tetapi terlalu panjang untuk menjadi Slogan. Winston mensyaratkan frasa yang dapat diulang "in a meeting without explanation" — kalimat 40+ kata tidak memenuhi ini.

**Implikasi untuk v6/Phase 4:** Slogan perlu dibuat. Kandidat dwibahasa per spec E5: "Kerangka bekerja — bukan teori" / "The Framework Works — Not Just Theory." Harus muncul minimal di slide 01, slide divider tiap bagian, dan slide 31.

### Surprise

**Ada satu elemen Surprise yang dapat diidentifikasi, meskipun tidak dieksploitasi secara maksimal.** Slide 20 (lines 970–1001) menampilkan diagram rantai otoritas FASB → IASB → PSAK → INDF, dan secara eksplisit menyatakan (line 999): "INDF bukan di jalur FASB langsung — INDF → PSAK → IASB CF 2018." Ini adalah klaim kontra-intuitif: audiens yang memahami bahwa presentasi ini tentang "FASB × INDF" mungkin berasumsi INDF mengikuti FASB secara langsung. Kenyataan bahwa INDF berada di jalur IASB (bukan FASB) adalah informasi yang genuine mengejutkan.

Namun, klaim ini muncul di slide 20 dari 32, bukan di pembukaan. Winston mensyaratkan Surprise ditempatkan di early slides untuk "stop the audience and make them think." Di v5, Surprise yang paling kuat dikubur di tengah deck.

Elemen Surprise sekunder: Slide 25 (line ~1500) memuat statistik bahwa goodwill Rp52,2T setara 26% total aset INDF — ini adalah angka yang mengejutkan (satu pos intangible senilai seperempat seluruh aset perusahaan Rp201T) tetapi lagi-lagi muncul di tengah deck dalam slide yang padat.

### Salient Idea

**Salient Idea ada, tetapi tersebar ke lima ide berbeda.** Slide 31 "Lima Insight Utama" (lines 2102–2155) secara eksplisit mengidentifikasi lima insight: (1) Karakteristik Kualitatif Terpenuhi, (2) Pengakuan: Tiga Kasus Kompleks, (3) Pengukuran: Mixed-Attribute Model, (4) OCI & Disaggregasi Penyajian, (5) Catatan sebagai Enabler QC.

Winston mensyaratkan satu Salient Idea — "the one idea that sticks out above everything else." Dengan lima insight setara, audiens menghadapi pilihan tentang mana yang paling penting. Kalimat Kesimpulan Overarching di slide 31 (line 2153) menawarkan kandidat Salient Idea yang lebih kuat: "FASB Conceptual Framework bukan dokumen normatif yang abstrak, melainkan peta jalan operasional yang bekerja nyata di perusahaan multinasional skala Rp115,79T." Namun, kalimat ini muncul hanya di akhir slide 31, tidak diulang dan tidak menjadi benang merah yang dipertegas di pembukaan.

**Implikasi untuk v6/Phase 4:** Salient Idea perlu dipilih satu dan dijadikan benang merah: dari slide 01 (sebagai promise) → muncul di setiap section divider (sebagai pengingat) → dikonfirmasi di slide 31 (sebagai bukti). Kandidat terkuat dari konten v5 sendiri: "Kerangka konseptual FASB bekerja nyata — bukan teori" yang dibuktikan oleh kasus INDF 2024.

### Story

**Ada arc narasi yang dapat diidentifikasi, meskipun tidak dikemas secara eksplisit sebagai Story.** Agenda slide 02 (lines 155–172) menunjukkan struktur berikut: Konteks & Evolusi → Karakteristik Kualitatif → Elemen → Pengakuan & Pengukuran → Catatan & Perspektif Kritis → Sintesis Teori → Studi Kasus INDF → Penutup & Kesimpulan. Ini adalah struktur yang logis: teori dulu (slides 03–20), kemudian bukti empiris (slides 21–30), kemudian sintesis (slides 31–32).

Arc ini memiliki pola tension-resolution yang implisit: "Ada kerangka konseptual yang telah berkembang selama 71 tahun (slides 03–20) — apakah ia benar-benar bekerja di dunia nyata? INDF 2024 membuktikannya (slides 21–30) — dan hasilnya adalah [lima insight] (slide 31)." Tension tidak diartikulasikan secara verbal di slide pembuka; resolusinya (slide 31) tidak secara eksplisit merujuk kembali ke promise awal.

Kelemahan struktural: Slides 19 dan 20 ("Sintesis Teori") muncul sebelum Studi Kasus INDF (slides 21–30), bukan setelahnya. Ini menempatkan "sintesis" di tengah arc, bukan di akhir. Hasilnya adalah arc yang terfragmentasi: ...teori → sintesis → bukti → sintesis lagi (slide 31). Winston mensyaratkan story arc yang linear: setup → tension → demonstration → resolution. v5 memiliki dua momen sintesis yang berpotensi membingungkan struktur.

---

## F4 — Persuade Structure Audit

### Vision Statement

**Tidak ada Vision Statement yang eksplisit.** Winston mendefinisikan Vision sebagai pernyataan problem yang diperhatikan orang + pendekatan baru yang ditawarkan, disampaikan dalam 5 menit pertama. Slide 01 menyampaikan judul dan scope; slide 02 menyampaikan agenda; slide 03 membuka dengan "Mengapa Kerangka Konseptual Diperlukan?" (line 180) — ini adalah langkah yang tepat menuju Vision.

Namun, slide 03 langsung membahas kronologi CAP (1939) tanpa terlebih dahulu menegaskan problem yang relevan bagi audiens saat ini. Vision harus berbentuk: "Problem: X (yang Anda hadapi sebagai pengguna laporan keuangan). Pendekatan baru: Y (yang akan kita tunjukkan melalui kasus INDF)." Pertanyaan retoris "Mengapa Kerangka Konseptual Diperlukan?" (slide 03 header) mendekati Vision tetapi tidak dijawab dengan promise spesifik; ia dijawab dengan kronologi sejarah.

**Apa yang sudah selaras:** Slide 03 memiliki struktur "problem before solution" yang tepat — ia membuka dengan era pra-kerangka (CAP, APB, ARS) sebelum menunjukkan solusi (SFAC 8). Ini adalah sinyal bahwa tim memahami pola Vision, meskipun eksekusinya tidak memenuhi standar F4 sepenuhnya.

### Proof of Work

**Proof of Work hadir dan substantif, terutama di bagian Studi Kasus INDF (slides 21–30).** Winston mendefinisikan Proof of Work sebagai langkah-langkah spesifik yang membuktikan sesuatu yang nyata telah dilakukan. Dalam konteks ini, "proof of work" adalah evidence bahwa teori FASB dapat diterapkan pada kasus empiris nyata.

Slide 08 (lines 430–481) menyajikan bar chart EPS INDF 5 tahun dengan data aktual; card-head mengutip "INDF AR 2024 pp.32–34." Slide 21 (lines 1043–1098) menampilkan delapan stat blocks dengan angka AR: penjualan Rp115,79T, aset Rp201,71T, goodwill Rp52,2T (26% total aset), EPS Rp984 — semua dengan sumber "INDF AR 2024 pp.4, 32–34." Slide 27 (lines 1694–1769) menyajikan tiga "recognition cases" (goodwill, PSAK 72, related party) dengan tabel angka spesifik per kasus.

Citation ke INDF AR dan ke paragraf SFAC (mis. OB2, OB17, RE8–9, QC1–39, RD3, BC4.7, BC7.21, M30–34) muncul di slide-slide teori, memberikan kesan bahwa konten berbasis dokumen primer bukan ringkasan sekunder. Ini adalah alignment dengan F4 yang signifikan.

**Kelemahan Proof of Work:** Slide 03 (kronologi) mengutip "Wolk Ch. 7 pp. 163–166" tetapi tidak menggunakan angka atau kutipan langsung dari sumber. Slides teori lainnya (04–18) menggunakan citation SFAC paragraph tetapi seringkali tanpa kutipan verbatim — hanya parafrase. Winston mensyaratkan "specific steps — not vague accomplishments." Kutipan tanpa angka atau teks langsung dari sumber adalah proof yang lemah.

### Opening-Close Mirror

**Opening-Close Mirror tidak terpenuhi.** Winston mensyaratkan bahwa slide terakhir mencerminkan promise slide pertama — "promise made, promise kept." Slide 01 (line 128–130) berisi headline dan scope; tidak ada promise spesifik tentang apa yang akan diketahui audiens. Oleh karena itu, bahkan jika slide 32 berisi Contributions Close, ia tidak dapat mencerminkan sebuah promise yang tidak pernah dibuat.

Lebih jauh, slide 32 adalah "Terima Kasih" — ia tidak mencerminkan apapun dari slide 01. Slide 31 (Lima Insight Utama) mendekati fungsi close yang baik: ia merangkum lima temuan dengan angka konkret. Namun, slide 31 bukan slide terakhir (slide 32 adalah yang terakhir dan mendominasi kesan akhir audiens).

**Apa yang sudah selaras:** Slide 31 (lines 2092–2162) mengandung struktur yang mendekati "promise kept" — ia menggunakan kalimat Kesimpulan Overarching (line 2153) yang berfungsi sebagai pernyataan final. Jika slide 31 dijadikan slide terakhir dan diperkuat dengan echo dari promise slide 01, opening-close mirror dapat dipenuhi tanpa perubahan drastis pada konten.

### Contributions Close

**Slide 32 secara jelas melanggar F4 — Contributions Close.** Evidens dari v5.html:

- Line 2176: `<div style="font-size:72px;font-weight:800;color:#fff;...">`**Terima Kasih**`</div>` — judul dominan slide terakhir.
- Line 2177: `<div style="font-size:28px;font-weight:300;color:rgba(255,255,255,0.5);...">`**THANK YOU**`</div>` — penguat bilingual.
- Lines 2183–2207: Grid 3 kolom × 2 baris, menampilkan 6 anggota kelompok dengan NIM masing-masing — Crime #9 dari crime-inventory.md.
- Line 2212: "Sesi Tanya Jawab — Kami siap menjawab pertanyaan Anda" — Crime #10 dari crime-inventory.md.

Winston secara eksplisit melarang "Thank you" atau "Questions?" sebagai slide terakhir karena keduanya melemahkan pesan akhir dan menggantikan posisi yang seharusnya diisi oleh Contributions Slide. Daftar anggota sebagai konten utama slide terakhir juga melanggar aturan F4: "Contributions slide stays up during questions — never replaced with 'thank you'." Slide 32 menggabungkan tiga violations dalam satu slide: Crime #3 (font), Crime #9 (anggota list), Crime #10 ("Terima Kasih").

### Rekomendasi

Slide 01 perlu ditambahkan Empowerment Promise. Slide 32 perlu diubah menjadi Contributions Slide: "3–5 kontribusi spesifik kelompok" (sesuai revision-priorities.md Tier 1a slide 32 Crime #9 dan #10). Anggota dicantumkan hanya di chrome footer. Judul diubah menjadi "Kontribusi Kelompok 3" atau "Temuan Utama." Q&A tetap sebagai sub-elemen kecil, bukan elemen dominan.

---

## F5 — Props & Stories Audit

### Slide kasus INDF

**Angka-angka INDF dihadirkan, tetapi story arc (konteks → demonstrasi → resolusi) tidak sepenuhnya terpenuhi.** Per spec E3, angka adalah "prop" dalam slide kasus INDF, dan story arc yang diperlukan adalah: konteks/ketegangan → demonstrasi (tabel/grafik) → resolusi (interpretasi via FASB).

Slide 21 (lines 1043–1098, data-screen-label "21 Profil INDF") menampilkan delapan stat blocks dengan angka konkret: Rp115,79T penjualan, Rp201,71T aset, Rp52,2T goodwill (26% total aset), EPS Rp984. Angka-angka ini hadir sebagai prop. Namun, tidak ada kalimat "konteks" yang menetapkan mengapa angka ini mengejutkan atau bermasalah sebelum angka ditampilkan, dan tidak ada kalimat "resolusi" yang menginterpretasikan angka melalui lensa FASB secara eksplisit di slide yang sama.

Slide 25 (yang berkaitan dengan goodwill test) lebih mendekati story arc: ia memiliki konteks (proporsi goodwill Rp52,2T terhadap total aset), lalu demonstrasi (dua tabel uji definisi SFAC), lalu partial resolusi. Namun, berdasarkan crime-inventory.md slide 25, slide ini mengandung >60 kata visible dan font 17–18px — konten terlalu padat untuk story arc yang efektif.

Slide 27 (Recognition Cases) menggunakan struktur tiga kolom dengan tiga "kasus" — goodwill Rp12,8T, PSAK 72 lima-langkah, dan related party Rp10,11T. Setiap kolom berisi judul + tabel angka + keterangan. Ini mendekati struktur F5 (satu prop per kasus), tetapi ketegangan (tension) tidak diartikulasikan: mengapa kasus ini sulit? Apa yang tidak jelas sebelum FASB memberikan kerangka? Story arc memerlukan tension sebelum resolusi — slide 27 melewati tension dan langsung ke demonstrasi.

**Apa yang sudah selaras:** Slide 31 (sintesis) mengintegrasikan angka konkret ke dalam pernyataan insight: "Goodwill Rp12,8T, PSAK 72 lima-langkah, dan related party Rp10,11T — semua memenuhi kriteria RD3" (line 2118). Ini adalah contoh "angka sebagai prop dengan interpretasi," meskipun dalam konteks ringkasan bukan narasi tensional.

### Slide konsep sulit

**Slide-slide konsep sulit mengandalkan definisi tekstual, bukan prop.** Konsep-konsep paling sulit dalam deck: faithful representation (slide 09), going concern (implisit di slides 11–12), materiality (slide 23), recognition criteria (slide 14).

Slide 09 (SFAC 2 vs SFAC 8: Faithful Representation) menyajikan perbandingan dua kolom dengan definisi + komponen boxes. Tidak ada prop fisik atau analogi yang membuat perbedaan antara "Reliability" dan "Faithful Representation" terasa konkret. Audiens diberikan definisi formal, bukan objek atau analogi yang membuat konsep "terpegang di tangan."

Slide 14 (Recognition Criteria) menyajikan empat kriteria SFAC 5 dan tiga kriteria SFAC 8 dalam dua card besar plus tabel Recognition vs Disclosure — semuanya teks dan tabel. Tidak ada contoh konkret tentang kapan recognition terjadi vs kapan disclosure cukup; tidak ada prop yang membuat perbedaan ini terasa fisik.

Slide 23 (Materiality) adalah pengecualian parsial: ia menyajikan angka goodwill Rp52,2T sebagai 26% total aset — ini adalah angka yang berfungsi sebagai prop karena skalanya mengejutkan. Namun, arc-nya tetap tidak lengkap: tidak ada kalimat yang menetapkan ketegangan ("Apakah Rp52,2T itu material atau tidak?") sebelum demonstrasi angka.

**Catatan positif:** Slide 08 (QC Relevansi — EPS 5 tahun) menggunakan bar chart EPS 2020–2024 sebagai prop visual. Ini adalah satu-satunya slide yang paling mendekati F5 secara formal: angka EPS deret waktu memungkinkan audiens melihat pola (Predictive Value) dan mengkonfirmasi tren (Confirmatory Value). Story arc-nya parsial — ada demonstrasi (bar chart), ada resolusi (interpretasi QC), tetapi tension (mengapa EPS INDF berfluktuasi? apa risikonya?) tidak diartikulasikan.

### Rekomendasi

Untuk setiap slide kasus INDF (21–30), tambahkan satu kalimat "tension setter" sebelum tabel/grafik — satu pertanyaan atau klaim yang membuat audiens ingin tahu jawaban sebelum angka ditampilkan. Untuk slide konsep sulit (09, 14, 23), rancang analogi atau objek verbal (Winston: "if no physical prop exists, design the closest verbal equivalent") yang membuat konsep terasa fisik. Detail per-slide akan masuk ke rubrics/ per slide saat Phase 4 build.

---

## Kesimpulan Naratif

Deck v5 berada pada posisi yang dapat digambarkan sebagai "matang secara substantif, tetapi belum siap secara komunikatif." Dari sisi konten, v5 mengandung korpus materi yang kaya: citation ke paragraf SFAC spesifik (OB2, OB17, RE8–9, QC1–39, RD3, BC4.7, BC7.21, M30–34), angka-angka INDF AR 2024 yang terverifikasi sumbernya, dan struktur logis yang mengikuti urutan SFAC 8. Tim jelas telah membaca sumber primer. Kekuatan yang perlu dipertahankan: Crime #8 = 0 (logo discipline tepat), citation sistem yang konsisten, dan konten substantif yang mencerminkan kerja akademik yang serius.

Namun, tiga defect fundamental membatasi efektivitas komunikasi deck ini. Pertama, defect tipografi sistemik: 573 dari 587 deklarasi font-size (97,6%) menggunakan ukuran di bawah threshold Winston 40pt, karena seluruh design system dibangun dengan kelas `.t-body` (22px), `.t-lead` (26px), `.t-label` (13px) sebagai standar — bukan pengecualian. Ini bukan 32 bug terpisah yang dapat di-patch; ini adalah satu keputusan arsitektur CSS (lines 28–38) yang harus diulang dari nol. Kedua, tidak ada empowerment promise di slide 01 dan tidak ada Contributions Close di slide 32 — kedua ekstrem deck ini melanggar F1 dan F4 sekaligus. Slide terakhir yang audiens lihat adalah "Terima Kasih" dengan daftar anggota dan NIM, bukan pernyataan kontribusi yang bertahan di memori. Ketiga, tidak ada Symbol, tidak ada Slogan, dan Salient Idea tersebar menjadi lima — F3 (STAR) sepenuhnya absen dari deck.

Arah revisi split dua jalur: 23 HIGH non-XL (konten density, slide splits, Crime #9/#10) dan 40 MED dapat diselesaikan sebagai patch v6 karena merupakan intervensi konten dan struktur yang tidak bergantung pada typography. Sebaliknya, 32 HIGH-XL Crime #3 tidak dapat di-patch v6 — ia adalah prerequisite Phase 4 yang harus diselesaikan pertama sebelum satu slide pun dibangun ulang, karena memperbaiki typography di satu slide tanpa memperbaiki design system global akan menghasilkan inkonsistensi yang lebih buruk dari kondisi saat ini. Phase 4 harus dimulai dengan satu deliverable tunggal: typography system baru dengan minimum body text 40pt, baru kemudian slide-level content ditulis ulang.
