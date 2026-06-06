# Design Spec — RMK Kelompok 2: Sage Chapter 13 "Statement of Cash Flows"

**Date:** 2026-06-06
**Status:** Approved by user
**Approach:** A — Gap-analysis-driven enrichment

## Goal

Produce a comprehensive RMK (Ringkasan Materi Kuliah) in .docx for Kelompok 2, consolidating deep understanding of all files in `Kelompok 2 Pasca UTS/`:

| Source file | Role |
|---|---|
| `Sage Chapter 13.pdf` | Primary source — Wolk, Dodd & Rozycki, *Accounting Theory: Conceptual Issues in a Political and Economic Environment* (2017), Ch. 13 "Statement of Cash Flows", 31 pp (print pp. 375–409) |
| `Chapter 13 Sage Ringkasan_Summary.pdf` | Existing Indonesian ringkasan — **base structure to build on**, enriched and gap-filled from the primary source |
| `Kelompok 2 Members.jpeg` | Member identity for the cover page |

All three source files are **read-only** — never edited or overwritten.

## User decisions (from brainstorming)

1. **Existing ringkasan role:** Build on it — keep its narrative spine, enrich/deepen with the original chapter.
2. **Format:** .docx via python-docx build script.
3. **Depth:** Comprehensive deep-dive (~15–25 pages) covering every chapter section.
4. **Cover:** Full Kelompok 2 cover with all 6 members + NIMs.

## Deliverable

`Kelompok 2 Pasca UTS/output/Kelompok 2_RMK Chapter 13 Statement of Cash Flows.docx`

- **Language:** Bahasa Indonesia; English technical terms in *italics* (register matches existing ringkasan).
- **Voice:** Graduate/professor-level analysis — argumentation and "why", not undergraduate bullet summarization.
- **Cover:** Course name (Pelaporan Keuangan Korporat), book/chapter identity, member table:
  | NIM | Name |
  |---|---|
  | 122501039 | Satriyo Nugroho |
  | 122501048 | Mario Da Costa |
  | 122501067 | Amelda Putri Zhany Wiguna |
  | 122501078 | Ahmad Ramadhan |
  | 122501084 | Nida Nur Cahyati |
  | 122501094 | Priska Putri Parungky |

## RMK content structure (source order governs)

1. **Pendahuluan & Learning Objectives** — why cash matters; the 1971 (APB 19) → 1987 (SFAS 95) arc
2. **SCFP (APB Opinion No. 19)** — funds flow heritage, sources/uses logic, Exhibit 13.1, all-inclusive approach, four fund definitions
3. **Motivasi Beralih ke SCF** — working-capital weaknesses, SFAC No. 1 linkage, six benefits of cash flow data, quality of income, liquidity vs financial flexibility
4. **Persyaratan & Struktur SCF (SFAS No. 95)** — cash + cash equivalents, operating/investing/financing trichotomy, dissenting FASB views
5. **Metode Langsung vs Tidak Langsung** — Exhibit 13.2/13.3 walk-through, survey evidence, cost-vs-transparency trade-off
6. **Masalah Nonartikulasi** — worked example of why indirect-method adjustments fail to articulate with balance sheet changes
7. **Masalah Klasifikasi dalam Trikotomi FASB** — interest/dividend misclassification, noncash transactions, installment purchases
8. **Kegunaan Analitis SCF** — Largay & Stickney / W.T. Grant case, ratio analysis, user perspectives
9. **Free Cash Flow** — definitions, Buffett's owner earnings, four-measure guidance, non-GAAP caveats
10. **Riset Teoretis & Empiris** — Lawson, Lee, prediction studies, accrual/cash complementarity
11. **Rekomendasi Perbaikan SCF** — authors' (incl. Broome) recommended changes
12. **Sintesis & Simpulan** — chapter through-line for exam/discussion use

Section names above are working labels; final headings are written during content drafting from what the chapter actually contains. Every section cites the chapter (page/exhibit refs). **No fabricated content** — if the chapter doesn't say it, the RMK doesn't either.

## Workspace & pipeline

```
Kelompok 2 Pasca UTS/
├── (3 source files — read-only)
├── analysis/
│   ├── chapter-deep-read.md      # structured notes from full 31-page read
│   └── gap-analysis.md           # ringkasan vs chapter: covered / thin / missing per section
├── content/
│   └── rmk-ch13.md               # RMK source of truth (markdown)
└── output/
    ├── build_docx.py             # python-docx builder, reusing ti4/ti5 pattern
    └── Kelompok 2_RMK Chapter 13 Statement of Cash Flows.docx
```

- Docx styling follows the proven ti4/ti5 `build_docx.py` pattern: A4, Times New Roman 12, justified body, styled headings, cover page.
- Markdown is the editable source of truth; the docx is always regenerable via the build script.

## Process (execution order)

1. **Deep-read** both PDFs in full → `analysis/chapter-deep-read.md`
2. **Gap analysis** — section-by-section: what the existing ringkasan covers well / thinly / misses → `analysis/gap-analysis.md`
3. **Write RMK markdown** — keep ringkasan spine, enrich per gap analysis → `content/rmk-ch13.md`
4. **Build docx** — adapt ti4/ti5 `build_docx.py`; cover + styled content
5. **Quality gates** (below)

## Quality gates

- **Gap analysis before writing** — enrichment plan is explicit, not improvised
- **Coverage audit after writing** — every chapter learning objective, section, and exhibit checked against the RMK
- **Two-stage review** — (1) content fidelity: no fabrication, refs correct; (2) language/voice: graduate register, consistent terminology
- **verification-before-completion** — docx builds without error, opens, page count within ~15–25 target, before claiming done

## Out of scope

- No PPT/slide deck (prior Kelompok 2 deck work was removed from the repo and is not being recreated)
- No changes to Group 3 presentation work or other course deliverables
- No editing of the three source files
