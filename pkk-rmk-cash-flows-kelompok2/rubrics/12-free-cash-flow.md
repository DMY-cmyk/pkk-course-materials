---
id: 12-free-cash-flow
required_concepts: ["C-51", "C-52", "C-53", "C-54", "C-55"]
required_exhibits: ["eq-13-2", "exhibit-13-07", "exhibit-13-08", "exhibit-13-09", "exhibit-13-10", "exhibit-13-11"]
wolk_refs: ["Ch.13 FCF, PDF pp.17-21"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["NOPLAT", "free cash flow", "WACC", "ABC Company", "Mulford", "entity theory", "332", "Exhibit 13.7", "Exhibit 13.8", "Exhibit 13.9", "Exhibit 13.10", "Exhibit 13.11"]
depth_check:
  - "Makna 'free' (tiadanya klaim senior) dan basis entity theory dijelaskan"
  - "Persamaan (13.2) dijelaskan komponen demi komponen (NOPLAT; investasi modal kerja operasi neto + aset tak lancar; bunga dikecualikan; kas operasi = invested capital)"
  - "Kelima exhibit ABC dibaca berurutan sebagai satu alur konstruksi; Exhibit 13.10 dibaca dengan angka 2005: CFO $527 -> FCF $332"
  - "Exhibit 13.11 ditafsirkan: empat ukuran, empat sudut pandang; pilihan bergantung waktu/sumber daya/tujuan; CFO 'terkontaminasi' bunga"
  - "Tabel sintesis empat ukuran kinerja hadir"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik FCF: definisi, persamaan 13.2, alur ABC Company 13.7-13.11, WACC.
