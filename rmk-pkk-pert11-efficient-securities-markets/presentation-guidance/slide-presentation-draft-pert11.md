# Slide Presentation Draft — Pert. 11: Efficient Securities Markets (Scott, Bab 4)

*Spec for Claude Design — not the final visual.*

---

## Slide-Crime Audit (Winston's 10 Crimes)

| # | Crime | Fix applied in this deck |
|---|---|---|
| 1 | Too many slides | Capped at ~24 for a 23-min talk (≈1 slide/min) |
| 2 | Too many words per slide | ≤4 bullets × ≤6 words; hard cap forces ≥40pt |
| 3 | Font < 40pt | On-slide text budget keeps every line large |
| 4 | Reading slides aloud | Slide text ≠ script; script carries the words |
| 5 | Laser pointer | Design hints build emphasis into the slide (callouts/highlight) |
| 6 | Speaker far from slides | Delivery note: stand beside the screen |
| 7 | No white space | Every design hint mandates breathing room |
| 8 | Background clutter / logos | No logos; one focal element per slide |
| 9 | Collaborators list as final slide | Members shown on Cover only |
| 10 | "Thank you" / "Questions?" final slide | Final slide = **Contributions close** |

---

## The Star

- **Symbol** — the two concentric circles (`assets/exhibits/fig-4-2.png`): public info vs. fundamental value.
- **Slogan** — *"Yang dihargai pasar adalah informasi, bukan bentuknya."* (repeated verbatim)
- **Surprise** — the consensus beats *every* individual forecaster (Table 4.1); darts ≈ pros.
- **Salient idea** — **asimetri informasi adalah alasan akuntansi ada.**
- **Story** — lemons market → inside information → role of reporting → fundamental value.

---

## Delivery Rules

1. Berdiri di samping layar (stand beside the screen), bukan membelakangi audiens.
2. Teks slide bukan naskah — script berada di kepala pembicara; slide hanya cue visual.
3. White space adalah wajib — setiap slide harus punya ruang napas; jangan padatkan teks.
4. Dua momen prop wajib ditandai: (a) kunci mobil bekas untuk lemons problem; (b) amplop tertutup untuk gap lingkaran dalam–luar (inside information). Speaker notes akan memflag momen ini.

---

## Field Schema

Setiap slide block memiliki lima field berikut (format baku untuk semua slide S1–S24):

| Field | Keterangan |
|---|---|
| **Headline** | Kalimat assertif penuh (bukan label topik), ≤~10 kata |
| **On-slide text** | ≤4 bullets, ≤6 kata per bullet — atau satu stat/kutipan tunggal |
| **Visual** | Path aset relatif ATAU "build: \<deskripsi\>" — diikuti caption satu baris |
| **Speaker script (id)** | Naskah 30–60 detik, professor-voice Indonesian; istilah Inggris verbatim |
| **Design hint** | Arahan layout untuk Claude Design — white space, focal point, callout |

---

## Slide S1 — Cover

**Headline:** Efficient Securities Markets — Mengapa Pasar Menghargai Informasi, Bukan Bentuknya

**On-slide text:**
- Pelaporan Keuangan Korporat / MNK202
- Pertemuan 11 · Kelompok 3

| Anggota Kelompok 3 | NIM |
|---|---|
| Odisiana Manek | 122501041 |
| Efri Nurmalinda | 122501049 |
| Prasetya Adhi Surya Gumilang | 122501068 |
| Dzaki Muhammad Yusfian | 122501079 |
| Adinda Putri Dewi | 122501086 |
| Kunthi Talibrata | 122501097 |

*(Tabel anggota = data identitas tetap, tidak dihitung terhadap kuota bullet.)*

**Visual:** `input/rules/Grup 3 PKK Pasca UTS.jpeg` (opsional) atau clean title tanpa gambar — caption: Kelompok 3 · MNK202 · Pert. 11. *(Members appear here only — crime #9.)*

**Speaker script (id):** *(Tidak dibacakan; slide ditampilkan saat audiens masuk. Adinda memulai dengan S2 tanpa membaca ulang nama-nama.)*

**Design hint:** Title-dominant. Judul utama di tengah atas dengan ukuran besar (≥60pt). Tabel anggota di bawah, compact, font kecil tapi terbaca. Generous white space di sekeliling tabel. Tidak ada logo institusi. Satu warna latar bersih.

---

## Slide S2 — Vision · Adinda Putri Dewi

**Headline:** Pasar menghargai informasi — dan akuntansi ada karena asimetrinya.

**On-slide text:**
- Pasar menghargai informasi, bukan bentuknya.
- Asimetri informasi: alasan akuntansi ada.

**Visual:** build: satu kalimat besar terpusat di layar putih — "Yang dihargai pasar adalah informasi, bukan bentuknya." — caption: Empowerment promise · S2

**Speaker script (id):** Bab empat Scott bukan sekadar tentang pasar modal — ini tentang *mengapa* akuntansi ada. Dalam 23 menit ke depan, Anda akan bisa menjelaskan dua hal yang saling terhubung: pertama, mengapa pasar menghargai *informasi* — bukan format, bukan letak, bukan medium pengungkapan — melainkan kandungan informasinya itu sendiri; dan kedua, mengapa tanpa *asimetri informasi*, profesi akuntansi tidak punya alasan fundamental untuk ada. Itulah janji sesi ini: di akhir ±23 menit, Anda memegang dua kunci konseptual itu. Kita mulai dengan peta perjalanannya.

**Design hint:** Satu kalimat empowerment promise dicetak besar, terpusat, dengan tipe ≥48pt. Dua bullet outcome di bawahnya lebih kecil tapi masih besar (≥40pt). Latar putih, satu focal point. Tidak ada dekorasi tambahan.

---

## Slide S3 — Vision · Adinda Putri Dewi

**Headline:** Empat langkah: dari pasar efisien ke pengungkapan penuh.

**On-slide text:**
- Adinda · 4.1–4.2.1: definisi efisiensi
- Efri & Dzaki · 4.3–4.4: implikasi
- Prasetya · 4.5: CAPM
- Odisiana & Kunthi · 4.6–4.8: asimetri

**Visual:** `assets/exhibits/fig-4-1.png` — caption: Organisasi Bab 4 (Scott)

**Speaker script (id):** Bab empat bergerak dalam empat blok besar. Adinda membuka dengan definisi *efficient securities market* versi Fama dan empat properti efisiensi. Efri dan Dzaki menelusuri implikasi langsung bagi pelaporan, termasuk paradoks informativeness yang dipecahkan *noise traders*. Prasetya memformalkan hubungan risiko dan return lewat CAPM. Terakhir, Odisiana dan Kunthi menyambungkan seluruh bab ke *information asymmetry*, *fundamental value*, dan signifikansi sosial pelaporan berkualitas.

**Design hint:** Flowchart `fig-4-1.png` ditampilkan full-width sebagai focal point utama. Empat bullet line-up pembicara disusun sebagai band tipis di bawah flowchart — font kecil, satu baris per blok. Tidak ada teks lain yang bersaing dengan diagram.

---

## Slide S4 — 4.1 · Adinda Putri Dewi — Efficient market defined

**Headline:** Pasar efisien: harga mencerminkan sepenuhnya informasi publik.

**On-slide text:**
- Fama 1970 · semi-strong form
- Arbitrage: mesin penyelaras harga
- Informed investors bergerak cepat
- Efisiensi: model, bukan kesempurnaan

**Visual:** build: kartu definisi tunggal terpusat — kutipan singkat "harga mencerminkan sepenuhnya informasi publik" — dengan callout kecil di pojok bawah bertuliskan "model, bukan kesempurnaan" — caption: Fama (1970) via Scott (2015), hlm. Bab 4

**Speaker script (id):** Fama (1970) mendefinisikan *efficient securities market* dalam bentuk *semi-strong*: harga sekuritas pada setiap saat mencerminkan sepenuhnya semua informasi yang diketahui publik. Ini bukan *strong form* — yang mengklaim harga mencerminkan pula informasi orang dalam — karena menghapus seluruh informasi orang dalam dari pasar terlampau mahal; dalam praktiknya, hampir mustahil. Mesin yang menyelaraskan harga dengan informasi adalah *arbitrage*: begitu informasi baru muncul, *informed investors* — yang rela menanggung biaya untuk memperoleh dan mengolah informasi — bergerak cepat, membeli atau menjual hingga harga kembali mencerminkan informasi tersebut. Yang perlu ditekankan: efisiensi adalah sebuah *model*, bukan klaim kesempurnaan. Pertanyaan yang tepat bukan "efisien atau tidak", melainkan seberapa dekat pasar nyata mendekati ideal — pertanyaan yang makin relevan setelah *meltdown* 2007–2008.

**Design hint:** Satu kartu definisi (definition card) mendominasi slide — teks definisi dicetak ≥40pt, terpusat. Callout kecil "model, bukan kesempurnaan" ditempatkan di sudut bawah kanan dengan bingkai tipis atau warna kontras ringan, ukuran ≥28pt. Empat bullet on-slide disusun di sisi atau bawah kartu — singkat, ≥40pt. Latar bersih, satu focal point.

---

## Slide S5 — 4.2.1 · Adinda Putri Dewi — Three forms

**Headline:** Tiga bentuk efisiensi: weak ⊂ semi-strong ⊂ strong.

**On-slide text:** *(slide ini berbasis visual — tidak ada bullet teks tambahan; caption diagram menjadi satu-satunya teks pendukung)*

**Visual:** `assets/diagrams/efficiency-forms.png` — caption: Tiga bentuk efisiensi (Fama 1970); semi-strong = fokus Bab 4

**Speaker script (id):** Fama (1970) membedakan tiga tingkatan efisiensi dalam hubungan subset bersarang. *Weak form*: harga mencerminkan semua informasi harga historis — analisis teknikal tidak menghasilkan laba abnormal. *Semi-strong form*: harga mencerminkan semua informasi yang diketahui publik, termasuk laporan keuangan, berita, dan pengumuman dividen — inilah bentuk yang menjadi landasan Bab 4 Scott. *Strong form*: harga mencerminkan pula informasi orang dalam — teoretis sempurna, tetapi nyaris mustahil secara praktis karena biayanya terlalu tinggi. Semakin dalam lingkaran, semakin banyak informasi yang sudah "tertanam" dalam harga; implikasi bagi akuntansi berangkat dari lapisan *semi-strong* — itulah batas di mana pelaporan keuangan beroperasi.

**Design hint:** Diagram `assets/diagrams/efficiency-forms.png` ditampilkan *full-bleed* sebagai satu-satunya focal point — tidak ada elemen bersaing. Lingkaran *semi-strong* diberi highlight (warna berbeda atau garis tebal) untuk menandainya sebagai fokus bab. Caption satu baris di bawah diagram, ≥28pt. Tidak ada bullet teks selain caption; white space di sekeliling diagram wajib dijaga lebar.

---

## Slide S6 — 4.2.1 · Adinda Putri Dewi — Four properties

**Headline:** Empat sifat: relatif, bukan mahatahu, fair game, random walk.

**On-slide text:**
- Relatif terhadap informasi publik
- Bukan kemahatahuan pasar
- Fair game: tak ada return abnormal
- Random walk: perubahan tak berkorelasi

**Visual:** build: grid 2×2, satu ikon per sel — (1) lingkaran info publik; (2) tanda seru "≠ mahatahu"; (3) timbangan (fair game); (4) jejak acak (random walk) — caption: Empat properti efisiensi (Scott, 2015, Bab 4)

**Speaker script (id):** Definisi Fama membawa empat sifat yang perlu dipahami bersama. Pertama, efisiensi bersifat *relatif* terhadap informasi publik — bukan terhadap semua informasi; ini menyisakan ruang bagi *insider trading*, yang itulah sebabnya regulasi sekuritas melarangnya. Kedua, efisiensi bukan kemahatahuan: harga bisa meleset bila informasi publik tidak lengkap atau keliru — contoh nyata, harga aset beragun aset (*asset-backed securities*) melambung tepat sebelum meltdown 2007–2008, padahal risikonya sudah ada; pasar belum mendapatkan informasi yang cukup. Ketiga, berinvestasi adalah *fair game*: tidak ada peluang laba di atas return normal yang telah disesuaikan risiko; CAPM menjadi tolok ukur return normal itu. Keempat, harga ber-*random walk* — perubahan tidak berkorelasi dari satu periode ke periode berikutnya; bila harga terus naik tanpa berita yang mendasarinya, itu justru tanda inefisiensi, bukan konfirmasi tren.

**Design hint:** Tata letak grid 2×2; satu ikon vektor sederhana di tengah tiap sel, label properti ≥40pt di bawah ikon. Tidak ada paragraf teks dalam sel — narasi sepenuhnya ada di speaker script. Garis pembatas tipis antar-sel; white space di dalam tiap sel wajib lapang. Sel "bukan kemahatahuan" boleh diberi sub-label kecil "(ABS · 2007–08)" sebagai anchor visual ≥28pt.

---

## Slide S7 — 4.2.2 · Efri Nurmalinda — Konsensus

**Headline:** Konsensus mengalahkan setiap peramal individual.

**On-slide text:**
- Rata-rata taksiran tak bias
- Kesalahan individual saling menghapus
- Independensi: syarat mutlak
- Tanpa independensi → momentum harga

**Visual:** `assets/exhibits/table-4-1.png` — caption: Beaver (1981): 619 ramalan, 1966–1968

**Speaker script (id):** *(Ini adalah "Surprise" beat dari The Star — sampaikan dengan jeda sebelum membuka tabel.)* Teka-teki sentralnya begini: dua investor yang sama-sama rasional bisa bereaksi berbeda atas informasi yang sama. Analogi mobil: model keputusan menyediakan *kendaraan* untuk mengolah informasi, tetapi tidak menyeragamkan cara mengemudinya. Jadi bagaimana harga bisa mencerminkan seluruh informasi? Jawabannya bukan keseragaman — melainkan *perata-rataan*. Yang dibutuhkan hanya bahwa taksiran investor secara rata-rata tidak bias; kesalahan ke atas dan ke bawah saling meniadakan. Beaver (1981) membuktikan ini dengan 15–16 peramal sepak bola yang membuat 619 ramalan selama 1966–1968 — tak ada satu peramal pun yang konsisten unggul, tetapi *konsensus* selalu menang. Analoginya ke pasar: peramal adalah investor, ramalan adalah keputusan beli atau jual, dan konsensus adalah harga pasar. Satu syarat krusial: *independensi*. Argumen ini runtuh begitu investor berunding — atau terserang bias kolektif — karena kekeliruan tak lagi menghapus satu sama lain; sebaliknya muncul *share price momentum*, harga terdorong naik oleh kenaikan itu sendiri, bukan oleh penilaian rasional.

**Design hint:** Tabel `table-4-1.png` ditempatkan di sisi kiri slide sebagai focal point utama — tampilkan full-height, tidak diperkecil. Di sisi kanan, satu baris takeaway tunggal dicetak ≥44pt: "Konsensus selalu menang — karena kesalahan saling menghapus." Empat bullet on-slide disusun di bawah tabel atau sebagai band tipis, ≥40pt. Jaga generous white space; tidak ada elemen dekoratif bersaing dengan tabel.

---

## Slide S8 — 4.2.2 · Efri Nurmalinda — Random Walk Malkiel

**Headline:** Dart acak menyaingi manajer profesional — karena fair game.

**On-slide text:**
- Profesional: 10,9% rata-rata
- Dart acak: 4,5% rata-rata
- Dow Jones: 6,8% rata-rata
- WSJ · 100 kontes pertama

**Visual:** `assets/exhibits/tip-4-1.png` — caption: Theory in Practice 4.1 (Malkiel)

**Speaker script (id):** Malkiel (1973), dalam *A Random Walk Down Wall Street*, berargumen bahwa melempar dart acak ke daftar saham NYSE menghasilkan *return* setinggi manajer profesional — sebab bila pasar adalah *fair game*, tidak ada saham yang "murah". WSJ menguji klaim ini selama 100 kontes pertama di tahun 1990-an: profesional rata-rata 10,9%, dart rata-rata 4,5%, dan indeks Dow Jones 6,8%. Pembelaan Malkiel ada tiga. Pertama, manajer profesional mungkin memilih saham yang lebih berisiko, sehingga *return* lebih tinggi mencerminkan kompensasi risiko, bukan keunggulan analisis. Kedua, pasar 1990-an didominasi firma-firma besar yang lebih banyak diikuti analis, sehingga peluang salah-harga hampir tidak ada. Ketiga — dan ini catatan regulasi penting — profesional mungkin punya akses informasi orang dalam, karena *Regulation FD* baru berlaku efektif tahun 2000. Ketiga pembelaan ini konsisten dengan efisiensi: dart tidak membuktikan inefisiensi; ia justru menegaskan betapa sulitnya mengungguli pasar yang sudah *fair game*.

**Design hint:** Tiga callout statistik ditempatkan berdampingan di sisi kanan exhibit `tip-4-1.png`: kotak "Profesional 10,9%" · "Dart 4,5%" · "Dow Jones 6,8%" — masing-masing dengan label sumber kecil di bawahnya (WSJ · 100 kontes). Angka dicetak ≥48pt; label sumber ≥28pt. Exhibit di sisi kiri, tiga callout di sisi kanan. White space wajib lapang di sekeliling keduanya. Tidak ada teks lain bersaing dengan tiga angka tersebut.

---

## Slide S9 — 4.3 implikasi 1–2 · Efri Nurmalinda (Beaver 1973)

**Headline:** Kebijakan tanpa efek kas tak menggerakkan harga.

**On-slide text:**
- Tanpa efek kas → harga tetap
- Pasar tembus ke implikasi kas
- Full disclosure: ungkap, manfaat > biaya
- IAS 1: kebijakan wajib diungkap

**Visual:** build: dua kartu implikasi bertumpuk secara vertikal — kartu atas berlabel "Implikasi 1 · Beaver (1973)" dengan ikon timbangan kecil; kartu bawah berlabel "Implikasi 2 · Beaver (1973)" dengan ikon megafon kecil — caption: Dua implikasi pertama efisiensi bagi pelaporan (Beaver, 1973)

**Speaker script (id):** Beaver (1973) menulis khusus untuk menjelaskan implikasi teori pasar efisien kepada akuntan praktik. Dua implikasi pertamanya langsung menyentuh pilihan kebijakan yang kita buat sehari-hari. Implikasi pertama: kebijakan akuntansi yang tidak menghasilkan *cash-flow effect* tidak menggerakkan harga. Contoh konkret — pilih amortisasi garis lurus atau saldo menurun: laba berubah di kertas, tetapi arus kas dan pajak tidak. Pasar "menembus" sampai ke implikasi kas yang sesungguhnya, asalkan kebijakan diungkapkan dan dapat dikonversi. Pengungkapan kebijakan ini bukan pilihan — *IAS 1* mewajibkannya sebagai bagian laporan keuangan lengkap. Implikasi kedua: *full disclosure*. Pasar efisien berjalan berdampingan dengan pengungkapan penuh; ungkapkan setiap informasi relevan yang murah secara tepat waktu, selama manfaatnya melampaui biayanya. Alasannya ganda: investor pasti memakai setiap informasi yang tersedia sehingga tak ada yang terbuang; dan makin terbuka, makin tumbuh kepercayaan pasar karena makin sedikit informasi orang dalam yang dikhawatirkan.

**Design hint:** Dua kartu implikasi disusun vertikal di tengah slide, masing-masing dengan latar warna berbeda (kartu atas lebih gelap, kartu bawah lebih terang) untuk membedakan secara visual. Label "Implikasi 1" dan "Implikasi 2" dicetak ≥40pt di pojok kiri atas tiap kartu; isi kartu (satu frasa ringkas per kartu) ≥40pt. Ikon kecil di pojok kanan atas tiap kartu sebagai focal point visual — tidak perlu besar, cukup sebagai penanda. White space wajib lapang di sekeliling kedua kartu; tidak ada elemen lain bersaing.

---

## Slide S10 — 4.3 implikasi 3–4 · Dzaki Muhammad Yusfian

**Headline:** Investor naif terlindungi harga; akuntan bersaing untuk bertahan.

**On-slide text:**
- (3) Naif: terlindungi harga efisien
- (4) Akuntan bersaing, tanpa jaminan
- Empat implikasi → decision usefulness
- Decision usefulness → Conceptual Framework

**Visual:** build: dua kartu berdampingan horizontal — kartu kiri berlabel "Implikasi 3 · Price-Protected" dengan ikon perisai kecil; kartu kanan berlabel "Implikasi 4 · Akuntan Bersaing" dengan ikon tanda seru — diikuti tanda panah kecil "→ Conceptual Framework" di bawah kedua kartu — caption: Dua implikasi terakhir efisiensi bagi pelaporan (Beaver, 1973)

**Speaker script (id):** Efri telah menyampaikan dua implikasi pertama Beaver — netralitas kebijakan tanpa efek kas dan *full disclosure*. Saya melanjutkan dengan dua yang tersisa. Implikasi ketiga: investor naif *price-protected*. Selama cukup banyak investor terinformasi memahami pengungkapan, harga terbentuk seolah semua investor memahaminya — investor naif terlindungi karena mereka dapat menyewa ahli atau sekadar meniru keputusan investor terinformasi. Ini berarti standar tidak perlu dirancang untuk melindungi yang paling awam sekalipun; harga pasar sudah melakukannya. Implikasi keempat: akuntan *bersaing* dengan sumber informasi lain — analis, media, bahkan harga pasar itu sendiri — dan tidak ada jaminan kelangsungan. Laporan keuangan harus terus-menerus membuktikan kegunaannya. Keempat implikasi ini bersama-sama menopang konsep *decision usefulness* — informasi berguna bagi pengambilan keputusan investor — yang menjadi fondasi *Conceptual Framework* standar akuntansi modern.

**Design hint:** Dua kartu berdampingan horizontal, lebar setara, tinggi cukup lapang untuk satu frasa ringkas per kartu (≥40pt). Label "Implikasi 3" dan "Implikasi 4" di pojok kiri atas tiap kartu, ≥40pt. Ikon perisai (kiri) dan tanda seru (kanan) di pojok kanan atas, ukuran minimal — hanya sebagai penanda visual. Tanda panah kecil "→ Conceptual Framework" ditempatkan di bawah kedua kartu, terpusat, font ≥40pt dengan warna aksen berbeda. White space wajib lapang di sekeliling kartu; tidak ada teks lain bersaing.

---

## Slide S11 — 4.4 · Dzaki Muhammad Yusfian — Grossman paradox

**Headline:** Jika harga sepenuhnya informatif, insentif mencari informasi lenyap.

**On-slide text:**
- Fully informative → insentif pencarian lenyap
- Investor berhenti → harga tak informatif
- Ekuilibrium stabil tak terbentuk
- Analisis laporan keuangan terancam

**Visual:** build: diagram loop yang terputus — empat simpul dalam lingkaran: "Harga fully informative" → "Insentif lenyap" → "Investor berhenti mencari" → "Harga tak lagi informatif" → (panah kembali ke simpul pertama putus dengan tanda silang merah di titik putusnya, disertai label "osilasi liar") — caption: Paradoks Grossman (1976)

**Speaker script (id):** Setelah empat implikasi itu, muncul inkonsistensi logis yang diidentifikasi Grossman pada 1976. Bayangkan skenario ekstrem: harga saham mencerminkan *seluruh* informasi yang relevan — *fully informative*. Jika demikian, mengapa seorang investor masih mau mengeluarkan biaya mahal untuk mencari dan mengolah informasi? Tidak ada insentifnya. Bila insentif itu lenyap, investor berhenti mencari. Namun bila investor berhenti mencari, harga tidak lagi mencerminkan seluruh informasi — kontradiksi langsung dengan asumsi awal. Tidak ada ekuilibrium stabil yang terbentuk; harga berosilasi liar antara dua keadaan yang saling mengancam. Implikasinya bagi kita: jika paradoks ini dibiarkan tanpa penyelesaian, seluruh kegunaan analisis laporan keuangan menjadi tanda tanya — mengapa menganalisis jika harga sudah meringkasnya, dan mengapa mempercayai harga jika tidak ada yang menganalisis?

**Design hint:** Diagram loop yang terputus menjadi satu-satunya focal point, ditampilkan besar di tengah slide. Empat simpul digambarkan dengan lingkaran atau kotak bernomor urut; panah antar-simpul tebal dan jelas. Titik putus (antara simpul keempat dan pertama) ditandai dengan silang merah tebal dan label "osilasi liar" ≥28pt dengan aksen merah. Caption "Paradoks Grossman (1976)" di bawah diagram ≥28pt. Empat bullet on-slide disusun sebagai band tipis di bawah diagram — font ≥40pt. White space lapang di atas diagram; tidak ada elemen dekoratif tambahan.

---

## Slide S12 — 4.4 · Dzaki Muhammad Yusfian — Noise-traders resolution

**Headline:** Noise traders membuat harga hanya partially informative — analisis pulih.

**On-slide text:**
- Noise traders bertransaksi karena alasan acak
- Investor rasional tak bisa bedakan noise
- Harga menjadi partially informative
- Insentif analisis laporan keuangan pulih

**Visual:** build: panel kontras dua kolom — kolom kiri berlabel "Fully Informative" (latar abu-abu redup, ikon loop tertutup sempurna, label "insentif = nol"); kolom kanan berlabel "Partially Informative" (latar terang, ikon loop dengan noise kecil di sisinya, label "analisis bernilai") — caption: Penyelesaian noise traders (Grossman, 1976 via Scott, 2015)

**Speaker script (id):** Paradoks Grossman diselesaikan melalui konsep *noise traders* dan *rational expectations*. *Noise traders* adalah pelaku pasar yang membeli atau menjual bukan karena analisis informasi, melainkan karena alasan acak — sentimen, rumor, atau sekadar kebutuhan likuiditas. Keberadaan mereka menciptakan ketidakpastian bagi investor rasional: ketika harga saham bergerak naik, apakah itu karena ada investor lain yang memegang informasi superior, atau sekadar karena noise? Investor rasional tidak bisa memastikannya. Akibatnya harga hanya menjadi *partially informative* — mencerminkan sebagian, bukan seluruh informasi. Inilah titik pemulihan: karena harga tidak merangkum segalanya, insentif untuk mencari informasi kembali bernilai. Analisis laporan keuangan, kebijakan konservatif sebagai sinyal kualitas, *voluntary disclosure*, dan *MD&A* semuanya mendapat peran kembali. Satu prediksi empiris penting: firma besar cenderung harganya lebih informatif karena lebih banyak dianalisis, sehingga laporan keuangan mereka *lebih sedikit* menggerakkan harga dibanding firma kecil — efek yang telah dikonfirmasi secara empiris.

**Design hint:** Panel kontras dua kolom ditampilkan berdampingan, lebar setara. Label kolom "Fully Informative" dan "Partially Informative" dicetak ≥44pt di atas masing-masing kolom. Kolom kiri diberi latar abu-abu redup atau warna dingin; kolom kanan latar putih bersih atau warna hangat — kontras visual yang tegas. Ikon loop di tiap kolom berukuran sedang, terpusat dalam kolom. Label singkat "insentif = nol" (kiri) dan "analisis bernilai" (kanan) ≥28pt di bawah ikon. Empat bullet on-slide disusun sebagai band tipis di bawah panel ≥40pt. White space wajib lapang di sekeliling panel; tidak ada elemen bersaing.

---

## Slide S13 — 4.5 · Prasetya A. S. Gumilang — CAPM equation

**Headline:** CAPM menautkan harga efisien, risiko, dan return.

**On-slide text:**

*(Equation line — exempt from 6-word cap):*
E(Rjt) = Rf(1 − βj) + βj · E(RMt)

- Rf: return aset bebas risiko
- βj: kepekaan terhadap pasar
- E(RMt): return pasar harapan

**Visual:** build: persamaan tunggal dicetak besar terpusat (≥40pt, bold), dengan tiga callout bernomor yang masing-masing menunjuk simbol Rf, βj, dan E(RMt) — setiap callout berisi satu baris label deskriptif singkat; latar putih bersih tanpa dekorasi — caption: Sharpe–Lintner CAPM (via Scott, 2015, Bab 4)

**Speaker script (id):** CAPM memformalkan hubungan yang selama ini hanya diisyaratkan — bahwa harga efisien, risiko, dan return terhubung dalam satu persamaan. Sebelum masuk ke persamaannya, kita perlu bedakan dua jenis return. Return realisasi — *ex post* — adalah Rjt sama dengan Pjt ditambah Djt dikurangi Pj,t−1, dibagi Pj,t−1: berapa sebenarnya yang investor dapatkan setelah fakta terjadi. Return harapan — *ex ante* — adalah E(Rjt) sama dengan ekspektasi atas Pjt ditambah Djt dibagi Pj,t−1, dikurangi satu: berapa yang diharapkan sebelum fakta terjadi. Rumus *ex ante* sudah mengandung efisiensi karena harga harapan mencerminkan seluruh informasi publik yang ada pada t−1. Kini, Sharpe dan Lintner menyatakan bahwa return harapan tersebut ditentukan oleh: E(Rjt) sama dengan Rf kali satu dikurangi βj, ditambah βj kali E(RMt). Persamaan ini bertumpu pada empat asumsi: banyak investor yang rasional dan menghindari risiko; tersedia satu aset bebas risiko Rf; pasar efisien; dan biaya transaksi nol. Sampaikan persamaan ini perlahan — tunjuk Rf, lalu βj, lalu E(RMt) — bukan dengan laser, tetapi dengan callout yang sudah tercetak di slide.

**Design hint:** Persamaan E(Rjt) = Rf(1 − βj) + βj · E(RMt) ditempatkan di tengah slide, dicetak ≥40pt bold, menjadi satu-satunya focal point utama. Tiga callout bernomor menunjuk masing-masing simbol Rf, βj, dan E(RMt) dengan garis tipis dan label satu baris (≥28pt). Tidak ada bullet teks lain yang bersaing dengan persamaan; empat bullet on-slide disusun sebagai band tipis di bawah callout ≥40pt. Latar putih bersih; generous white space di sekeliling persamaan; tidak ada dekorasi tambahan.

---

## Slide S14 — 4.5 · Prasetya A. S. Gumilang — Beta / systematic risk

**Headline:** Hanya risiko sistematis (beta) yang dikompensasi.

**On-slide text:**

*(Equation line — exempt from 6-word cap):*
βj = Cov(j,M) / Var(M)

- Beta tinggi: maskapai, pesawat
- Beta rendah: makanan cepat saji, utilitas
- Risiko spesifik: terdiversifikasi habis

**Visual:** build: skala beta horizontal (angka rendah di kiri, angka tinggi di kanan) dengan dua "chip" contoh — chip kiri berlabel "Makanan Cepat Saji · Utilitas" (beta rendah, warna hijau/biru tenang); chip kanan berlabel "Maskapai · Pesawat" (beta tinggi, warna merah/oranye) — persamaan βj = Cov(j,M)/Var(M) tercetak di atas skala — caption: Beta sebagai ukuran risiko sistematis (Scott, 2015, Bab 4)

**Speaker script (id):** Apa yang menentukan seberapa besar return harapan suatu saham? Jawabannya bukan risiko total, melainkan hanya risiko yang tidak bisa dihilangkan lewat diversifikasi — yaitu *systematic risk*, yang diukur oleh beta. Beta didefinisikan sebagai Cov(j,M) dibagi Var(M): kovarians antara return saham j dan return pasar M, dibagi dengan variansi pasar. Beta mengukur kepekaan return saham terhadap pergerakan pasar secara keseluruhan — faktor ekonomi luas yang dialami semua perusahaan sekaligus dan tak bisa dihindari walau portofolio sudah didiversifikasi penuh. Risiko yang bersifat spesifik-perusahaan — risiko bencana pabrik, pergantian CEO, atau gugatan hukum tunggal — justru *terdiversifikasi habis* dalam portofolio yang cukup lebar. Oleh karena itu, hanya beta yang layak dikompensasi oleh return. Contoh praktis: maskapai penerbangan dan produsen pesawat sangat peka terhadap siklus ekonomi — beta tinggi, return harapan lebih besar. Waralaba makanan cepat saji dan perusahaan utilitas listrik bergerak relatif stabil terlepas dari kondisi pasar — beta rendah, return harapan lebih kecil. Konsekuensi penting: E(Rjt) dalam CAPM dapat dibaca sebagai *biaya modal ekuitas* perusahaan — return minimum yang disyaratkan investor atas risikonya.

**Design hint:** Skala beta horizontal menjadi focal point visual utama, ditempatkan di tengah bawah slide. Dua chip contoh digantungkan di atas skala pada posisi kiri (beta rendah) dan kanan (beta tinggi), masing-masing dengan warna pembeda yang tegas. Persamaan βj = Cov(j,M)/Var(M) dicetak ≥40pt di atas skala, terpusat. Tiga bullet on-slide disusun sebagai band tipis di bawah visual ≥40pt. White space wajib lapang di sekeliling skala; tidak ada elemen dekoratif bersaing.

---

## Slide S15 — 4.5 · Prasetya A. S. Gumilang — Market model + critique

**Headline:** Market model memisah return harapan dari abnormal — lalu digugat.

**On-slide text:**

*(Equation line — exempt from 6-word cap):*
Rjt = αj + βj · RMt + εjt

- E(εjt) = 0 di pasar efisien
- Estimation risk: beta tak pasti
- Common knowledge: abaikan hedge fund
- Biaya transaksi, likuiditas, rasionalitas

**Visual:** build: layout dua zona vertikal — zona atas berisi persamaan Rjt = αj + βj·RMt + εjt (≥40pt, bold) dengan tiga callout: αj → "return harapan"; βj·RMt → "komponen pasar"; εjt → "abnormal return"; zona bawah berisi daftar empat kritik bernomor dalam dua kolom 2×2 — caption: Market model & kritik empat asumsi CAPM (Scott, 2015, Bab 4)

**Speaker script (id):** *Market model* adalah bentuk regresi *ex post* dari CAPM: Rjt sama dengan αj ditambah βj kali RMt ditambah εjt. Konstanta αj sama dengan Rf kali satu dikurangi βj — komponen return harapan yang bersumber dari aset bebas risiko. Term εjt adalah *abnormal return*: bagian return realisasi yang tidak terduga sejak awal periode. Di pasar efisien, E(εjt) sama dengan nol karena informasi baru datang secara acak dan sudah langsung terserap ke harga. Model ini punya tiga kegunaan. Pertama, ia menegaskan bahwa harga sekarang bergantung pada ekspektasi atas harga dan dividen masa depan — beta menentukan seberapa jauh harga bergerak mengikuti pasar. Kedua, ia memisah return realisasi menjadi komponen harapan dan komponen abnormal — dan inilah yang menjadi dasar metodologi *event studies* dalam riset akuntansi. Ketiga, ia menyediakan cara praktis mengestimasi beta lewat regresi kuadrat terkecil atas data historis, dengan cek silang αj ≈ Rf(1 − βj). Namun pasca-*meltdown* 2007–2008, empat asumsi CAPM digugat serius. Pertama, *rational expectations*: beta tidak pernah diketahui pasti — memunculkan *estimation risk* yang diabaikan model. Kedua, *common knowledge*: asumsi ini mengabaikan investor canggih seperti hedge fund yang beroperasi di luar basis informasi publik. Ketiga, biaya transaksi nol dan pasar sempurna likuid: kenyataannya ada *fee*, bid–ask spread, dan *liquidity risk* yang signifikan. Keempat, rasionalitas investor: bukti perilaku pasca-krisis menunjukkan bias kognitif yang sistematis. Catatan penutup: karena CAPM mengabaikan informasi orang dalam, ia cenderung *menaksir terlalu rendah* biaya modal. Meski demikian, CAPM tetap titik awal yang berguna dan masih dipakai hingga hari ini.

**Design hint:** Layout dua zona vertikal: zona atas (±40% tinggi slide) berisi persamaan Rjt = αj + βj·RMt + εjt dicetak ≥40pt bold dengan tiga callout tipis menunjuk αj, βj·RMt, dan εjt; zona bawah (±60%) berisi empat kritik dalam grid 2×2, masing-masing dengan nomor bernomor (1)–(4) dan label ≥36pt. Pemisah tipis atau warna latar berbeda antar zona untuk mempertegas struktur. White space wajib lapang di sekeliling persamaan dan di dalam setiap sel kritik. Tidak ada teks narasi; seluruh substansi ada di speaker script.

---

## Slide S16 — 4.6 · Odisiana Manek — Dua asimetri informasi

**Headline:** Asimetri informasi: adverse selection vs moral hazard.

**On-slide text:**
- Adverse selection: hidden info pra-transaksi
- Moral hazard: hidden action pasca-transaksi
- Asimetri → harga ditekan investor luar
- Ekstrem: market incompleteness

**Visual:** build: kartu perbandingan dua kolom berdampingan — kolom kiri berlabel "Adverse Selection" (ikon tanda tanya sebelum tanda panah transaksi); kolom kanan berlabel "Moral Hazard" (ikon mata tertutup setelah tanda panah transaksi); teks satu baris per kolom — caption: Dua jenis asimetri informasi (Scott, 2015, Bab 4)

**Speaker script (id):** Seluruh seksi 4.6 bertumpu pada dua jenis asimetri informasi yang berbeda mekanismenya. *Adverse selection* terjadi sebelum transaksi: satu pihak — biasanya orang dalam — tahu lebih banyak tentang kualitas aset yang diperdagangkan; parameter yang tak diketahui investor luar adalah seberapa jujur orang dalam tersebut. *Moral hazard* terjadi setelah transaksi: upaya nyata manajer dalam menjalankan perusahaan tidak teramati oleh pemegang saham; parameter yang tak diketahui adalah seberapa jauh manajer bermalas-malasan. Dalam kedua kasus, investor luar menghadapi ketidakpastian ekstra — bukan risiko pasar yang bisa didiversifikasi, melainkan *estimation risk* atas parameter yang tersembunyi. Mekanisme harganya langsung: investor luar menawar turun harga sekuritas sebesar perkiraan kerugian dari asimetri itu, sehingga biaya modal perusahaan naik. Dalam kasus ekstrem — misalnya asuransi atas kegagalan memperoleh gelar — ketidakpastian begitu besar hingga pasar sama sekali tidak terbentuk: *market incompleteness*. Inilah alasan terdalam mengapa pelaporan keuangan berkualitas ada.

**Design hint:** Side-by-side compare card: dua kolom setara lebar, pemisah vertikal tipis di tengah. Label kolom "Adverse Selection" dan "Moral Hazard" dicetak ≥44pt di atas masing-masing kolom, warna kontras berbeda. Satu baris deskripsi kunci per kolom ≥40pt. Ikon sederhana (tanda tanya kiri, mata tertutup kanan) sebagai penanda visual minimal. White space lapang di dalam dan di sekeliling kartu; tidak ada teks lain bersaing.

---

## Slide S17 — 4.6 · Odisiana Manek — Lemons problem (PROP MOMENT)

**Headline:** Pembeli tak bisa bedakan mobil bagus dari lemon — harga semua tertekan.

**On-slide text:**
- Pembeli tak tahu kualitas sebenarnya
- Pooling: harga = kualitas rata-rata
- Mobil bagus tersingkir dari pasar
- Antidot: sertifikat, garansi, reputasi

**Visual:** `assets/diagrams/adverse-selection.png` — caption: Adverse selection → antidot full disclosure

**Speaker script (id):** Akerlof (1970) membuktikan mekanisme adverse selection lewat pasar mobil bekas. Bayangkan ada dua jenis mobil: bagus dan "lemon" — mobil rusak. Pembeli tidak bisa membedakannya sebelum membeli. Akibatnya, pembeli menekan harga untuk semua mobil ke titik kualitas rata-rata — inilah yang Scott sebut *pooling*. Harga rata-rata ini terlalu rendah untuk pemilik mobil bagus, sehingga mereka enggan menjual dan menarik mobilnya dari pasar. Kini rata-rata kualitas turun lebih jauh, harga ikut turun, pemilik mobil bagus berikutnya keluar — siklus ini dapat berlanjut hingga pasar runtuh total. Peredam asimetri yang dikenal: sertifikat inspeksi pihak ketiga, garansi dari penjual, dan reputasi dealer yang dipertaruhkan. Analogi ke pasar saham langsung: penjual mobil bekas adalah orang dalam (*insider*), pembeli adalah investor luar, dan catatan servis yang diungkapkan secara penuh adalah laporan keuangan berkualitas. *(PROP: di sini tunjukkan kunci mobil bekas kepada audiens — "Ini adalah informasi yang Anda tak punya.")*

**Design hint:** Diagram `assets/diagrams/adverse-selection.png` ditampilkan full-width sebagai focal point tunggal — tidak ada elemen bersaing di area diagram. Empat bullet on-slide disusun sebagai band tipis di bawah diagram, ≥40pt. Caption satu baris di bawah diagram ≥28pt. White space lapang di atas diagram; prop cue hanya ada di speaker notes, tidak di slide. Tidak ada teks narasi tambahan pada area visual.

---

## Slide S18 — 4.6 · Odisiana Manek — Fundamental value (SIMBOL + SLOGAN + PROP)

**Headline:** Selisih dua lingkaran itu = informasi orang dalam.

**On-slide text:**
- Lingkaran luar: fundamental value
- Lingkaran dalam: info publik
- Selisih: informasi orang dalam

**Visual:** `assets/exhibits/fig-4-2.png` — caption: Figure 4.2: peran pelaporan keuangan

**Speaker script (id):** Figure 4.2 adalah simbol sentral bab ini — dua lingkaran konsentris. Lingkaran luar adalah *fundamental value*: harga yang akan dicapai saham di pasar efisien seandainya tidak ada informasi orang dalam sama sekali — ideal teoretis yang tak pernah benar-benar tercapai. Lingkaran dalam adalah harga pasar efisien semi-strong: harga yang mencerminkan seluruh informasi publik. Selisih antara lingkaran luar dan lingkaran dalam adalah informasi orang dalam yang belum terungkap ke publik. Peran pelaporan keuangan adalah mengubah informasi dalam menjadi informasi luar — memperbesar lingkaran dalam — sehingga harga mendekati fundamental value. Lingkaran dalam bertumbuh setiap kali pengungkapan berkualitas dibuat, tetapi tidak pernah benar-benar menyentuh lingkaran luar: selalu ada informasi orang dalam yang tersisa. "Yang dihargai pasar adalah informasi, bukan bentuknya." *(PROP: tunjukkan amplop tertutup kepada audiens — amplop ini adalah informasi orang dalam: gap antara dua lingkaran itu.)*

**Design hint:** Gambar konsentris `assets/exhibits/fig-4-2.png` menjadi hero image tunggal, ditampilkan besar di tengah slide — minimal teks yang bersaing. Tiga bullet on-slide disusun sebagai band tipis di sisi atau bawah gambar ≥40pt. Caption satu baris di bawah gambar ≥28pt. Prop cue hanya di speaker notes, tidak di slide. White space sangat lapang di sekeliling gambar; tidak ada dekorasi tambahan.

---

## Slide S19 — 4.6 · Odisiana Manek — Bukti empiris

**Headline:** Bukti: pengungkapan superior menyusutkan laba orang dalam.

**On-slide text:**
- JLT (2011): 24% di dalam blackout
- 3,6%/180 hari; ~0 dengan general counsel
- Maffett (2012): 42.930 reksa dana, 42 negara
- SOX (2002): harga → fundamental value

**Visual:** build: tiga "evidence chip" berdampingan horizontal — chip kiri berlabel "JLT (2011)" dengan satu statistik kunci; chip tengah berlabel "Maffett (2012)" dengan satu statistik kunci; chip kanan berlabel "SOX (2002)" dengan satu frasa kunci — caption: Tiga bukti pengungkapan mengurangi laba insider (Scott, 2015, Bab 4)

**Speaker script (id):** Tiga studi mengonfirmasi bahwa pengungkapan superior secara nyata menyusutkan laba informasi orang dalam. Studi pertama: Jagolinzer, Larcker, dan Taylor (2011) mengamati 260 firma AS yang memiliki kebijakan *blackout period*, dengan 7.856 transaksi orang dalam selama 2003–2005. Temuan mengejutkan: 24% transaksi itu terjadi justru di dalam periode blackout. Tanpa persetujuan *general counsel*, orang dalam meraih *excess return* rata-rata 3,6% per 180 hari — dan 10,8% untuk transaksi yang dilakukan di dalam blackout itu sendiri. Namun ketika persetujuan general counsel diwajibkan, laba abnormal itu nyaris lenyap. Kesimpulan: general counsel lebih efektif daripada blackout period semata. Studi kedua: Maffett (2012) menelaah 42.930 reksa dana di 42 negara selama 1999–2009 dan menemukan hubungan negatif yang konsisten antara kemampuan reksa dana meraih return abnormal dan kualitas pelaporan di negara asal perusahaan target. Sarbanes-Oxley (2002) hadir untuk menggeser harga saham menuju nilai fundamental — dan kasus Enron serta WorldCom adalah contoh nyata lingkaran dalam yang runtuh, menyeret harga saham bersama kejatuhan integritasnya.

**Design hint:** Tiga evidence chip disusun berdampingan horizontal, lebar setara, tinggi cukup lapang. Label studi di atas tiap chip ≥40pt; satu statistik kunci di bawah label ≥40pt bold; label sumber kecil ≥28pt. Warna chip berbeda untuk ketiga studi. Empat bullet on-slide disusun sebagai band tipis di bawah tiga chip ≥40pt. White space lapang di sekeliling chip; tidak ada teks narasi bersaing.

---

## Slide S20 — 4.7 · Kunthi Talibrata — Social significance

**Headline:** Pasar yang bekerja baik mengalokasikan modal yang langka.

**On-slide text:**
- Harga ≈ nilai fundamental → alokasi efisien
- Lemons → underinvestment
- Investor mundur → hilang depth
- Proyek bermutu tersingkir pasar

**Visual:** build: diagram alir modal sederhana — anak panah dari "Modal Langka" menuju dua cabang: cabang atas berlabel "Harga ≈ Fundamental Value → Alokasi Efisien" (warna hijau/biru); cabang bawah berlabel "Lemons / Inside Info → Underinvestment + Kehilangan Depth" (warna merah/oranye) — caption: Signifikansi sosial pasar efisien (Scott, 2015, Bab 4)

**Speaker script (id):** Pasar modal bukan sekadar arena transaksi — ia adalah kendaraan utama yang menghimpun dan menyalurkan modal yang langka kepada proyek-proyek produktif. Secara sosial diinginkan agar harga sekuritas mendekati *fundamental value*, sebab hanya dengan begitu perusahaan akan berinvestasi sampai titik profitabilitas marjinal setara biaya marjinal — inilah definisi alokasi modal yang efisien. Begitu informasi orang dalam masuk ke gambar, investor luar mundur atau menurunkan harga yang bersedia mereka bayar. Akibatnya, firma dengan proyek bermutu tinggi tidak mendapat penilaian yang pantas dan akhirnya *underinvestment* — investasi yang secara sosial menguntungkan gagal terlaksana. Bila terlalu banyak investor mundur, pasar kehilangan *depth* — kedalaman likuiditas yang memungkinkan transaksi besar tanpa menggoyang harga — dan tekanan terhadap investasi makin parah.

**Design hint:** Diagram alir modal dua-cabang menjadi focal point utama, ditampilkan besar di tengah slide. Cabang atas (alokasi efisien) diberi warna hangat positif ≥40pt; cabang bawah (underinvestment + depth) diberi warna merah/oranye dengan label ≥40pt. Empat bullet on-slide disusun sebagai band tipis di bawah diagram ≥40pt. White space lapang di sekeliling diagram; tidak ada elemen dekoratif bersaing.

---

## Slide S21 — 4.7 · Kunthi Talibrata — Stick vs carrots + evidence

**Headline:** Regulasi (stick) dan insentif pasar (carrots) berdampingan.

**On-slide text:**
- Stick: regulasi, penalti, insider trading
- Carrots: reputasi, harga naik, modal turun
- Dua syarat sosial pelaporan berguna
- Bukti: Wurgler · FHKP · BHV

**Visual:** build: timbangan dengan dua piringan — piringan kiri berlabel "Stick" (ikon palu regulasi); piringan kanan berlabel "Carrots" (ikon wortel); di bawah timbangan, satu band tipis berisi tiga label bukti: "Wurgler (2000) · FHKP (2009) · BHV (2009)" — caption: Dua mekanisme dan tiga bukti lintas-negara (Scott, 2015, Bab 4)

**Speaker script (id):** Dua mekanisme bekerja berdampingan untuk mendorong pelaporan berkualitas. "Stick" adalah regulasi: komisi sekuritas menetapkan standar minimum, mengendalikan *insider trading*, dan mendesak pengungkapan tepat waktu — tanpa penalti, standar kehilangan gigi. "Carrots" adalah insentif pasar: perusahaan yang berdisiplin mengungkap melampaui minimum memperoleh reputasi yang lebih baik, harga saham yang lebih tinggi, dan biaya modal yang lebih rendah — insentif nyata yang mendorong pengungkapan sukarela. Tiga studi lintas-negara mengonfirmasi signifikansi sosial ini. Wurgler (2000) meneliti 65 negara selama 1963–1995 dan menemukan bahwa makin banyak informasi spesifik-perusahaan yang tertanam dalam harga, makin efisien alokasi modal di negara tersebut. Francis, Huang, Khurana, dan Pereira — FHKP (2009) — menunjukkan bahwa negara dengan kualitas pelaporan lebih tinggi memberikan akses pembiayaan lebih lapang, sehingga laju pertumbuhan industri antarnegara berkualitas tinggi cenderung serupa. Biddle, Hilary, dan Verdi — BHV (2009) — membuktikan bahwa pelaporan berkualitas tinggi menekan baik *underinvestment* maupun *overinvestment* secara bersamaan. Dua syarat sosial yang menutup seksi ini: pertama, seluruh informasi berguna tersedia bagi publik sejauh penalti dan insentif sanggup memotivasinya; kedua, harga pasar efisien relatif terhadap informasi publik tersebut.

**Design hint:** Timbangan dua piringan menjadi focal point visual utama, ditempatkan di tengah-atas slide. Label "Stick" (kiri) dan "Carrots" (kanan) ≥44pt. Band bukti tipis di bawah timbangan memuat tiga label "Wurgler (2000)" · "FHKP (2009)" · "BHV (2009)" — font ≥28pt, warna aksen berbeda dari piringan timbangan. Empat bullet on-slide disusun sebagai band paling bawah ≥40pt. White space lapang di sekeliling timbangan; tidak ada elemen dekoratif bersaing dengan visual timbangan.

---

## Slide S22 — 4.8 · Kunthi Talibrata — Chapter synthesis

**Headline:** Asimetri informasi adalah alasan akuntansi ada.

**On-slide text:**

*(Hero line — exempt from 6-word cap):*
"Yang dihargai pasar adalah informasi, bukan bentuknya."

- Rasionalitas berlaku rata-rata, bukan seragam
- Noise traders menyelamatkan insentif analisis
- Residual inside info selalu tersisa

**Visual:** build: satu kalimat slogan dicetak besar terpusat sebagai hero line — "Yang dihargai pasar adalah informasi, bukan bentuknya." — dalam kotak atau panel tipis berwarna aksen; tiga bullet takeaway di bawahnya lebih kecil namun masih ≥40pt — caption: Salient idea · Slogan (Scott, 2015, Bab 4)

**Speaker script (id):** Bab empat Scott berpijak pada sebuah landasan epistemis yang penting: rasionalitas investor berlaku *rata-rata*, bukan seragam — tidak semua investor harus bereaksi identik atas informasi yang sama; yang dibutuhkan hanyalah bahwa taksiran mereka secara rata-rata tidak bias. Kontradiksi Grossman — bahwa harga *fully informative* justru menghapus insentif mencari informasi — diselesaikan oleh keberadaan *noise traders*: selama ada pedagang acak, investor rasional tidak pernah bisa memastikan apakah pergerakan harga disebabkan informasi superior pihak lain atau sekadar noise, sehingga harga tetap hanya *partially informative* dan insentif analisis pulih. Namun selalu ada residual informasi orang dalam yang tersisa — gap antara lingkaran dalam dan lingkaran luar Figure 4.2 tidak pernah menutup sepenuhnya. Di sinilah peran akuntansi: memperkecil gap itu lewat standar pengungkapan yang berguna dan hemat biaya. Model seperti CAPM memang digugat karena gagal meramalkan *meltdown* 2007–2008, namun banyak bukti empiris yang dikembangkan dari kerangka efisiensi tetap konsisten dengan teori ini — efisiensi tetap model yang paling produktif untuk memaknai pasar modal. Itulah mengapa kalimat ini adalah inti bab: "Yang dihargai pasar adalah informasi, bukan bentuknya."

**Design hint:** Slogan hero line "Yang dihargai pasar adalah informasi, bukan bentuknya." dicetak ≥48pt, terpusat, dalam panel berwarna aksen (misal latar biru tua atau hijau tua dengan teks putih) sebagai focal point tunggal bagian atas slide. Tiga bullet takeaway disusun di bawah panel ≥40pt, latar putih bersih. White space wajib lapang antara panel slogan dan bullet; tidak ada elemen dekoratif bersaing dengan hero line.

---

## Slide S23 — Close · Kunthi Talibrata — Contributions close

**Headline:** Yang kini Anda kuasai.

**On-slide text:**
- Pasar menghargai informasi, bukan bentuk
- Asimetri informasi: alasan akuntansi ada
- Full disclosure → alokasi modal efisien
- Pelaporan berkualitas = kepentingan sosial

**Visual:** build: panel "promise kept" yang mencerminkan tata letak S2 — satu kalimat empowerment dicetak besar terpusat: "Janji di awal sudah ditepati." — empat bullet kontribusi di bawahnya dalam font ≥40pt; latar putih bersih, satu focal point — caption: Contributions close · S23 (mirrors S2)

**Speaker script (id):** Di awal sesi ini, Adinda menjanjikan dua hal: bahwa Anda akan bisa menjelaskan mengapa pasar menghargai *informasi* — bukan format, bukan medium, bukan letak pengungkapan — melainkan kandungan informasinya; dan mengapa tanpa *asimetri informasi*, profesi akuntansi tidak punya alasan fundamental untuk ada. Dua puluh tiga menit kemudian, janji itu sudah ditepati. Anda kini memegang empat kunci: pertama, pasar menghargai informasi, bukan bentuk pengungkapannya; kedua, asimetri informasi adalah alasan terdalam akuntansi ada; ketiga, *full disclosure* mendekatkan harga ke *fundamental value* sehingga alokasi modal menjadi lebih efisien; dan keempat, pelaporan berkualitas bukan sekadar urusan perusahaan — ia adalah kepentingan sosial yang ditopang bukti lintas-negara. Saya buka sesi tanya-jawab — silakan ajukan pertanyaan kepada siapa pun di antara kami.

**Design hint:** Tata letak cermin S2: satu kalimat "promise kept" dicetak ≥48pt terpusat di bagian atas, diikuti empat bullet kontribusi ≥40pt di bawahnya. Latar putih bersih; satu focal point; tidak ada logo, foto anggota, atau teks "Terima kasih"/"Pertanyaan?" dalam bentuk apa pun. Slide ini TETAP DITAMPILKAN selama sesi tanya-jawab berlangsung (Winston crime #10 fix). Generous white space di sekeliling seluruh elemen.

---

## Slide S24 — Appendix · Glosarium

**Headline:** Glosarium — rujukan cepat untuk tanya-jawab.

**On-slide text:**

*(Dua kolom — reference slide; exempt from 6-word bullet cap)*

| Istilah | Definisi Ringkas |
|---|---|
| Efficient market | Harga mencerminkan sepenuhnya informasi publik |
| Fair game | Tak ada return abnormal di atas risiko |
| Random walk | Perubahan harga tak berkorelasi antarwaktu |
| Noise traders / partially informative | Pedagang acak → harga hanya sebagian informatif |
| CAPM / beta / market model | Model biaya modal; beta = risiko sistematis |
| Adverse selection / moral hazard | Hidden info pra-transaksi vs hidden action pasca |
| Lemons problem | Pembeli menekan harga semua barang karena tak bisa membedakan mutu |
| Fundamental value | Harga ideal tanpa informasi orang dalam |
| Estimation risk | Risiko parameter tak diketahui pasti |

**Visual:** build: tabel dua kolom low-emphasis — kolom kiri "Istilah" (bold); kolom kanan "Definisi Ringkas" (reguler); latar abu-abu sangat muda; header kolom warna aksen ringan — caption: Glosarium Bersama · back-up untuk sesi tanya-jawab

**Speaker script (id):** *(Slide ini tidak dipresentasikan — ditampilkan hanya jika diperlukan sebagai rujukan selama tanya-jawab. Seluruh anggota wajib hafal istilah-istilah ini.)*

**Design hint:** Reference slide — low-emphasis by design. Tabel dua kolom selebar slide dengan padding sel yang lapang; font lebih kecil dari slide konten (≥28pt cukup untuk reference slide, karena audiens tidak perlu membacanya dari jauh secara real-time). Header "Istilah" dan "Definisi Ringkas" ≥32pt bold. Latar abu-abu sangat muda atau putih gading; tidak ada focal point visual yang bersaing; tidak ada dekorasi. Label "back-up untuk sesi tanya-jawab" di pojok bawah ≥24pt italic.

---

