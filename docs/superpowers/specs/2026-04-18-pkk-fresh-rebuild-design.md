# MNK202 Pelaporan Keuangan Korporat — Fresh Rebuild Design Spec

**Date:** 2026-04-18
**Course:** MNK202 Pelaporan Keuangan Korporat, Pascasarjana STIE YKPN Yogyakarta
**Decision:** Full fresh rebuild — delete git history, new Rust pipeline, Design B enriched, 14 weeks × 5 deliverables
**Status:** Approved through brainstorming — ready for implementation planning

---

## 1. Project Scope

Build a complete graduate-level course support system for MNK202 (Corporate Financial Reporting), covering:
- 14 weeks × 5 deliverables = **70 HTML output files**
- 1 Visual Companion web app
- 1 Master Print Bundle (single-file, PDF-ready)
- All content grounded in Wolk (2017) + Scott (2015) textbooks + supplementary references
- Indonesian company examples from 8 confirmed annual report PDFs on disk

---

## 2. Architecture — Approach B (Template-First, Parallel Content)

### Phase 1 — Foundation (sequential, do once)
1. Delete git history (`rm -rf .git && git init`)
2. Scaffold `Dev Assistant/` Rust crate (`devassist`)
3. Build Design B CSS system + 5 Tera HTML templates
4. Implement CLI: `week <N>`, `weeks <N-M>`, `all`, `visual-companion`, `master-bundle`
5. Verify pipeline renders a single test week correctly

### Phase 2 — Textbook Mapping (sequential, research only)
1. Read Wolk Ch. 1, 2, 3, 5, 7, 8, 9, 11, 12, 13 from PDF
2. Read Scott Ch. 4, 11 from PDF
3. Confirm week-to-section mapping (see Section 5 below)
4. Commit mapping doc before any content is written

### Phase 3 — Parallel Content Generation
1. Dispatch 14 subagents simultaneously, one per week
2. Each subagent: reads assigned textbook chapters + AR PDF → writes 5 markdown files
3. Rust pipeline renders all 70 deliverables in one pass
4. Visual Companion + Master Bundle built last
5. Final commit

---

## 3. Repository Structure

```
/
├── .gitignore
├── docs/superpowers/specs/          ← this file
├── course-materials/
│   ├── indonesia-company-sources/
│   │   └── annual-reports/          ← 8 AR PDFs (already on disk)
│   └── outputs/
│       ├── Study Guide - Aid/Week NN/index.html
│       ├── Main Summary - Ebook/Week NN/index.html
│       ├── Indonesian Company Examples/Week NN/examples.html
│       ├── Review Sheet/Week NN/index.html
│       ├── Exercises/Week NN/index.html
│       ├── Visual Companion/index.html
│       └── Master Print Bundle/course-companion.html
└── Dev Assistant/
    ├── Cargo.toml
    ├── src/main.rs
    ├── templates/
    │   ├── study-guide.html.tera
    │   ├── summary.html.tera
    │   ├── company-example.html.tera
    │   ├── review-sheet.html.tera
    │   └── exercises.html.tera
    ├── assets/
    │   ├── css/base.css
    │   ├── css/screen.css
    │   └── css/print.css
    ├── fonts/inter-v.woff2
    └── content/
        └── week-NN/
            ├── study-guide.md
            ├── summary.md
            ├── company-example.md
            ├── review-sheet.md
            └── exercises.md
```

---

## 4. Design System — Design B Enriched

### Visual Identity
- **Background:** `#f1f5f9` (slate-100) body, `#ffffff` cards
- **Accent:** `linear-gradient(90deg, #2563eb, #7c3aed, #0891b2)` — 4px top bar
- **Typography:** Inter Variable (self-hosted), system-ui fallback
- **Border radius:** 10px cards, 6px chips, 20px pills
- **Shadow:** `0 1px 3px rgba(0,0,0,.08)` on cards

### Week Hero (every deliverable)
- 4px gradient top bar (blue → purple → cyan)
- Week number watermark (right, `#e2e8f0`, 64px, font-weight 900)
- Phase pill: Pra-UTS (`#eff6ff`/`#2563eb`) or Pasca-UTS (`#f0fdf4`/`#16a34a`)
- Reference chips: Wolk (`#faf5ff`/`#7c3aed`), PSAK (`#fff7ed`/`#c2410c`), Company (`#f0fdf4`/`#15803d`)
- Tab nav: 5 deliverable tabs, active tab underline `#2563eb`

### Body Grid
- **Main column:** 1fr — section cards with icon + title headers
- **Sidebar:** 320px — deliverable switcher, anchor company panel, reference list, progress bar

### Color-coded concept boxes (4-up grid)
- Blue (`#eff6ff` / `#1d4ed8`) — primary theory
- Purple (`#faf5ff` / `#7c3aed`) — information economics
- Green (`#f0fdf4` / `#15803d`) — empirical / Indonesian context
- Amber (`#fffbeb` / `#b45309`) — measurement / valuation

### Print (`@media print`)
- White background, `#f1f5f9` card borders preserved
- Page breaks: `break-inside: avoid` on concept grid items, flow diagrams, quote blocks
- Sidebar: collapses to 2-column grid below main content
- Company Example + Main Summary: ~8–12 A4 pages each
- Review Sheet: 1–2 A4 pages

---

## 5. Syllabus-to-Chapter Mapping

| Week | Topic | Core Reading | Anchor Company | Supplementary |
|------|-------|-------------|----------------|---------------|
| W1 | Pengantar & Perspektif Historis | Syllabus + W Ch.1 §1.1–1.4 | TLKM (Telkom Indonesia) | IASB CF 2018, BAPEPAM history, TLKM AR 2024 |
| W2 | Kontrak Efisien, Asimetri Informasi | W Ch.1 + W Ch.2 | BBRI (Bank Rakyat Indonesia) | Jensen & Meckling (1976), PSAK 1 rev.2023, BBRI AR 2025 |
| W3 | Struktur Kelembagaan Akuntansi | W Ch.3 | GIAA (Garuda Indonesia) | OJK Peraturan, DSAK-IAI history, GIAA AR 2024 |
| W4 | Postulat, Prinsip, dan Konsep | W Ch.5 | ASII (Astra International) | PSAK 72, PSAK 16, ASII AR 2025 |
| W5 | Kerangka Konseptual FASB/IASB | W Ch.7 | UNVR (Unilever Indonesia) | IASB CF 2018 (full), Kerangka Konseptual IAI, UNVR AR 2024 |
| W6 | Kegunaan Informasi Akuntansi | W Ch.8 | BBCA (Bank Central Asia) | Scott Ch.3 (supp.), Ohlson (1995), PSAK 71, BBCA AR 2025 |
| W7 | Keseragaman dan Pengungkapan | W Ch.9 | ICBP (Indofood CBP) | PSAK 5, PSAK 7, ICBP AR 2024 |
| — | **UTS** — W1–W7 | — | — | — |
| W8 | Neraca / Laporan Posisi Keuangan | W Ch.11 | BBCA (Bank Central Asia) | PSAK 71 ECL, PSAK 68, BBCA AR 2025 |
| W9 | Laporan Laba Rugi & Kualitas Laba | W Ch.12 | UNVR (Unilever Indonesia) | PSAK 72, PSAK 24, UNVR AR 2024 |
| W10 | Laporan Arus Kas & Kualitas Akrual | W Ch.13 | TLKM (Telkom Indonesia) | PSAK 2, Dechow (1994), TLKM AR 2024 |
| W11 | Pasar Sekuritas Efisien (EMH) | S Ch.4 | BBRI (Bank Rakyat Indonesia) | Fama (1970, 1991), IDX price data, BBRI AR 2025 |
| W12 | Manajemen Laba | S Ch.11 | GIAA (Garuda Indonesia) | Healy & Wahlen (1999), Jones (1991), GIAA AR 2024 |
| W13 | Presentasi Term Paper (Sesi 1) | Journal papers | Student-selected | UAS prep guide, presentation rubric |
| W14 | Presentasi Term Paper (Sesi 2) | Journal papers | Student-selected | W1–W12 master review, UAS framework map |
| — | **UAS** — W8–W14 | — | — | — |

---

## 6. Weekly Deliverable Specifications

### 6.1 Study Guide (`study-guide.md`)
- Numbered reading sequence (5 steps) with time estimates per step
- 4-box concept grid (color-coded by type)
- Flow diagram (information chain or conceptual sequence)
- Pull quote from Wolk or Scott (English original + Indonesian translation)
- Lecturer's Lens: what is likely tested, with a sample UTS/UAS question

### 6.2 Main Summary (`summary.md`)
- Full academic summary of all assigned textbook sections
- Structured by section number (§X.X)
- Key definitions boxed and labeled
- Connections to PSAK standards made explicit
- ~2,000–3,500 words in Indonesian, graduate-level register

### 6.3 Company Example (`company-example.md`)
- 13 sections (established template):
  1. Profil Perusahaan & Konteks IDX
  2. Relevansi Topik Minggu Ini
  3. Struktur Kepemilikan & Governance
  4. Auditor & Independensi
  5. Analisis Laporan Posisi Keuangan (selected)
  6. Analisis Laporan Laba Rugi (selected)
  7. Analisis Arus Kas (selected)
  8. Kebijakan Akuntansi Kritis
  9. Catatan atas Laporan Keuangan (key notes)
  10. Penerapan Topik Minggu Ini (direct application)
  11. Perbandingan dengan Standar Internasional
  12. Implikasi bagi Investor & Kreditur
  13. Pertanyaan Analitis untuk Diskusi
- All figures sourced from actual AR PDF — no indicative data
- ~4,000–5,000 words

### 6.4 Review Sheet (`review-sheet.md`)
- Key terms table (Indonesian term | English term | Definition | PSAK ref)
- Framework cheat-sheet (one visual per major model)
- Formula/model summary where applicable
- 5 quick-check questions with answers
- Target: prints to 1–2 A4 pages

### 6.5 Exercises (`exercises.md`)
- 5–8 problems, UTS/UAS style
- Difficulty range: definitional (L1) → analytical (L3) → synthesis (L4)
- One fully worked example included
- Indonesian company data used in at least 2 problems per week

---

## 7. Language Policy

| Element | Language |
|---------|----------|
| Headers, labels, navigation | Bilingual — Indonesian primary, English in parentheses |
| Body text | Indonesian — graduate-level register |
| Key technical terms (first use) | Indonesian with English parenthetical: *kegunaan keputusan (decision usefulness)* |
| Textbook quotes | English original, Indonesian translation below |
| PSAK references | Official Indonesian terminology per DSAK-IAI publication |
| Formulas, models | As published (English notation retained) |

---

## 8. Supplementary Reference Layer

### Layer 1 — Seminal Academic Papers
| Paper | Week |
|-------|------|
| Jensen & Meckling (1976) — Theory of the Firm | W2 |
| Ohlson (1995) — Earnings, Book Values, Dividends in Equity Valuation | W6 |
| Dechow (1994) — Accounting Earnings and Cash Flows | W10 |
| Fama (1970) — Efficient Capital Markets: A Review | W11 |
| Fama (1991) — Efficient Capital Markets: II | W11 |
| Healy & Wahlen (1999) — A Review of the Earnings Management Literature | W12 |
| Jones (1991) — Earnings Management During Import Relief Investigations | W12 |

### Layer 2 — Indonesian Regulatory Standards
PSAK 1, 2, 5, 7, 16, 24, 68, 71, 72 + IASB Conceptual Framework 2018 + Kerangka Konseptual IAI

### Layer 3 — Annual Reports (all confirmed on disk)
TLKM-2024, BBRI-2025, GIAA-2024, ASII-2025, UNVR-2024, BBCA-2025, ICBP-2024, INDF-2024

---

## 9. Git History Deletion Plan

```bash
cd "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat"
rm -rf .git
git init
git add .gitignore
git commit -m "chore: fresh start — MNK202 new build 2026-04-18"
```

**What is preserved:** All PDF files (textbooks, AR PDFs, syllabus), docs/ folder including this spec.
**What is erased:** All prior commit history (all prior phases A–E, 310 previously tracked files).
**This is irreversible.** Explicitly approved by user during brainstorming session 2026-04-18.

---

## 10. Rust Pipeline Specifications

- **Crate name:** `devassist`
- **Dependencies:** `pulldown-cmark` (markdown parsing), `tera` (HTML templating), `clap` (CLI), `walkdir` (directory traversal), `serde + toml` (config)
- **CLI commands:**
  - `cargo run -- week 6` — build Week 6 (5 deliverables)
  - `cargo run -- weeks 1-7` — build Weeks 1–7
  - `cargo run -- all` — build all 14 weeks
  - `cargo run -- visual-companion` — build Visual Companion
  - `cargo run -- master-bundle` — build Master Print Bundle
- **Output:** HTML files per deliverable with CSS files copied alongside in the same output directory (not inlined — keeps file size manageable and print CSS separate)
- **Config:** `Dev Assistant/configs/mapping.toml` — week metadata, company name, ticker, AR source, chapter refs

---

## 11. Success Criteria

- [ ] All 70 deliverable HTML files render correctly in browser
- [ ] Print-to-PDF from Chrome preserves layout with no broken elements
- [ ] Every Company Example cites specific AR page numbers or note numbers
- [ ] Every Main Summary explicitly references Wolk/Scott section numbers
- [ ] Visual Companion shows all 14 weeks with tab navigation
- [ ] Master Bundle is a single self-contained HTML file (~800KB target)
- [ ] No indicative or unverified data in any Company Example
- [ ] Graduate-level academic register maintained throughout (no simplification)
