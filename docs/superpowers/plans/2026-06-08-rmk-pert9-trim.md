# RMK Pert. 9 Prose Trim to ~15 Pages — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Condense the prose in `content/01…13_*.md` so the rebuilt `output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx` is ~15 pages, leaving all diagrams, tables, headings, front matter, and references unchanged.

**Architecture:** Four editing tasks (each rewrites a batch of section files to its word budget, preserving headings + embed directives verbatim), then one rebuild-and-verify task that re-runs `build_docx.py`, the test suite, and a Word-COM page count.

**Tech Stack:** Markdown content files; `src/python/build_docx.py` (python-docx); pytest; PowerShell + MS Word COM for page counting.

**Working directory:** `D:\DZAKI\S2\Sem. 1\Pelaporan Keuangan Korporat\rmk-pkk-pert9-income-statement` (repo root of the sub-project). Branch: create `feat/rmk-pert9-trim` from master before Task 1.

**Spec:** `docs/superpowers/specs/2026-06-08-rmk-pert9-trim-design.md`.

**Universal editing rules (apply to every editing task):**
- Read the current file first. Rewrite the PROSE to the target word count; do not invent content.
- Keep the `## ` heading line and any `### ` sub-heading lines exactly as they currently appear.
- Keep every embed directive line (the `@table(...)` and `![...](...)` lines) **verbatim and in the same position relative to its anchoring paragraph**. Copy it from the current file; do not retype from memory.
- Preserve every concept, every standard reference (ARB/APB/SFAS/SFAC/ASU numbers), and every named researcher already present. Cut only secondary examples, repetition, and padding.
- Keep ≥1 `(Wolk et al., 2017, PDF hlm. N)` citation per substantive paragraph; consolidate adjacent same-page citations.
- Keep each section's forward-bridge sentence, shortened.
- Bahasa Indonesia akademik; English terms in *italic*; **bold** key terms on first appearance; flowing paragraphs (no new bullet lists).
- Word count of a file = `(((Get-Content <file> -Raw) -split '\s+') | Where-Object {$_ -ne ''} | Measure-Object).Count` (this includes heading + embed-line words; targets already account for that).

---

### Task 0: Branch

- [ ] **Step 1: Create the working branch**

Run (from repo root `rmk-pkk-pert9-income-statement`, but git operates repo-wide):
```powershell
git checkout master
git checkout -b feat/rmk-pert9-trim
```
Expected: `Switched to a new branch 'feat/rmk-pert9-trim'`.

---

### Task 1: Trim §I–IV (files 01–04)

**Files:** Modify `content/01_orientasi.md`, `content/02_definisi_income_elemen.md`, `content/03_pengakuan_pendapatan.md`, `content/04_pengakuan_beban_matching.md`

Budgets (target words, ±10%): 01 → **300**; 02 → **470**; 03 → **480**; 04 → **410**.

Embed/heading lines to preserve verbatim:
- 02: heading `## II. Definisi Income dan Elemen-elemennya`; embed `@table(../assets/tables/tabel1_definisi.toml)` (after the paragraph on the revenue–expense → asset–liability evolution).
- 03: heading `## III. Pengakuan Pendapatan`; embed `![Gambar 1. Empat titik waktu alternatif pengakuan pendapatan | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 4–5](../assets/diagrams/gambar1_titik_pengakuan.png)` (after the four-timing-points paragraph).
- 04: heading `## IV. Pengakuan Beban dan Matching`; embed `![Gambar 2. Hierarki tiga tingkat pengakuan beban dan kritik alokasi Thomas | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 7–8](../assets/diagrams/gambar2_hierarki_matching.png)` (after the matching-hierarchy paragraph).
- 01: heading `## I. Orientasi: Laporan Laba Rugi dalam Teori Akuntansi`; no embeds.

Per-file coverage that must survive the cut:
- **01**: income statement as predominant statement (predicting future cash flows, assessing management performance); *articulation* with the balance sheet (Pert. VIII) and the *revenue–expense* vs *asset–liability* framing; one clause flagging economic-income/capital-maintenance as Ch. 11 context; *decision usefulness*; a compact roadmap of sections II–XII; bridge to II.
- **02**: the four income definitions and the revenue–expense → asset–liability shift; that definition is separate from recognition/measurement; gains and the revenue-vs-gain distinction seeding CO-vs-AI; expense definitions and losses-parallel-to-gains; the table; bridge to III.
- **03**: ideal-vs-measurability tension; the four timing points with their sanctioned uses (ARB 45/SOP 81-1; ARB 43; 1934 point-of-sale norm; SFAS 66 installment); the SFAS 32 extraction program (one example is enough); accretion/discovery not permitted; the three measurable attributes; Qwest swap as earnings-management Achilles' heel; ASU 2014-09/IFRS 15; SAB 101 and FASB–SEC tension; bridge to IV.
- **04**: the three APB Statement 4 categories and the matching hierarchy; why category 3 is unproblematic; Thomas's verify/refute arbitrariness thesis and its blow to historical cost; allocation-free alternatives (name them briefly); the information-content rejoinder (Ch. 8); bridge to V.

- [ ] **Step 1: Edit the four files to budget, preserving headings/embeds/coverage above.**

- [ ] **Step 2: Verify word counts and that embeds survive**

Run:
```powershell
foreach ($f in "01_orientasi","02_definisi_income_elemen","03_pengakuan_pendapatan","04_pengakuan_beban_matching") { $p="content/$f.md"; $w=(((Get-Content $p -Raw) -split '\s+')|?{$_ -ne ''}|Measure-Object).Count; "$f = $w" }
Select-String -Path content/02_definisi_income_elemen.md -Pattern '@table' ; Select-String -Path content/03_pengakuan_pendapatan.md,content/04_pengakuan_beban_matching.md -Pattern '!\[Gambar'
```
Expected: 01≈270–330, 02≈420–520, 03≈430–530, 04≈370–450; the `@table` line present in 02; the two `![Gambar` lines present in 03 and 04.

- [ ] **Step 3: Commit**
```powershell
git add content/01_orientasi.md content/02_definisi_income_elemen.md content/03_pengakuan_pendapatan.md content/04_pengakuan_beban_matching.md
git commit -m "trim(rmk9): condense I-IV to budget"
```

---

### Task 2: Trim §V–VIII (files 05–08)

**Files:** Modify `content/05_future_events.md`, `content/06_current_operating_vs_all_inclusive.md`, `content/07_comprehensive_income.md`, `content/08_seksi_nonoperasi.md`

Budgets: 05 → **390**; 06 → **440**; 07 → **380**; 08 → **410**.

Embed/heading lines to preserve verbatim:
- 05: heading `## V. Future Events dan Pengakuan Akuntansi`; embed `![Gambar 3. Peta isu future events dalam pengakuan akuntansi | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 8–11](../assets/diagrams/gambar3_future_events.png)` (after the one-event/two-event paragraph).
- 06: heading `## VI. Current Operating versus All-Inclusive Income`; embed `![Gambar 4. Evolusi pelaporan laba: dari current operating menuju all-inclusive dan comprehensive income | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 11–13](../assets/diagrams/gambar4_evolusi_laba.png)` (at END of file).
- 07: heading `## VII. Comprehensive Income`; embed `@table(../assets/tables/tabel2_format_ci.toml)` (after the three-reporting-formats paragraph).
- 08: heading `## VIII. Seksi Nonoperasi: Extraordinary Items, Accounting Changes, dan Prior Period Adjustments`; embed `@table(../assets/tables/tabel3_accounting_changes.toml)` (after the accounting-changes paragraph).

Coverage that must survive:
- **05** (moderate cut): accruals depend on future events (depreciation); SFAC 6 past/future balance; one/two-event view (keep the early-retirement example briefly); SFAS 5 probability gradations + the three probability approaches (name them); management-intent rejection; Beaver on market values + conservatism; enacted-law-only rule (SFAS 109); bridge to VI.
- **06** (core, gentle cut): the controversy; current-operating argument; the four all-inclusive arguments; AAA 1936 vs AICPA/ARB 43; APB Opinion No. 9; June 2011 ASU one/two-statement choice; Gonedes + the contrary study; big-bath/Citicorp 1987; bridge to VII.
- **07** (core, gentle cut): SFAC 5 statement; proprietary-theory grounding; OCI elements (SFAS 130: FX translation, AFS unrealized, minimum pension liability); what the Board did NOT move + prior-period-adjustment rationale; no-EPS-for-CI; three formats + Board preference + dissent; the table; bridge to VIII.
- **08** (deep cut): three subdivisions + prior-period as the continuing dilemma; extraordinary items ARB 32/43 → APB 9 → APB 30 rigid uniformity (unusual AND infrequent; keep the citrus-frost example in one clause; net-of-tax display); accounting changes — three types, APB 20 vs SFAS 154 retrospective, depreciation-as-estimate rule; prior-period adjustments APB 9 → SFAS 16 (error correction + tax-loss-carryforward); recurring/transitory link to forecasting; the table; bridge to IX (EPS, NOT quality of earnings).

- [ ] **Step 1: Edit the four files to budget, preserving headings/embeds/coverage.**

- [ ] **Step 2: Verify word counts and embeds**
```powershell
foreach ($f in "05_future_events","06_current_operating_vs_all_inclusive","07_comprehensive_income","08_seksi_nonoperasi") { $p="content/$f.md"; $w=(((Get-Content $p -Raw) -split '\s+')|?{$_ -ne ''}|Measure-Object).Count; "$f = $w" }
Select-String -Path content/05_future_events.md,content/06_current_operating_vs_all_inclusive.md -Pattern '!\[Gambar'; Select-String -Path content/07_comprehensive_income.md,content/08_seksi_nonoperasi.md -Pattern '@table'
```
Expected: 05≈350–430, 06≈400–490, 07≈340–420, 08≈370–450; the two `![Gambar` lines present (05, 06); the two `@table` lines present (07, 08).

- [ ] **Step 3: Commit**
```powershell
git add content/05_future_events.md content/06_current_operating_vs_all_inclusive.md content/07_comprehensive_income.md content/08_seksi_nonoperasi.md
git commit -m "trim(rmk9): condense V-VIII to budget"
```

---

### Task 3: Trim §IX–XI (files 09–11)

**Files:** Modify `content/09_earnings_per_share.md`, `content/10_topik_khusus.md`, `content/11_earnings_management.md`

Budgets: 09 → **320**; 10 → **580**; 11 → **600**.

Embed/heading/sub-heading lines to preserve verbatim:
- 09: heading `## IX. Earnings per Share`; embed `@table(../assets/tables/tabel4_eps.toml)` (after the APB-15-vs-SFAS-128 paragraph).
- 10: heading `## X. Topik Khusus dalam Pengukuran Laba`; the FOUR `### ` sub-headings exactly: `### Development Stage Enterprises`, `### Troubled Debt Restructuring`, `### Early Extinguishment of Debt`, `### Stock Options`; embed `![Gambar 5. Lini masa standar kompensasi opsi saham | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 20–24](../assets/diagrams/gambar5_stock_options.png)` (after the stock-options chronology).
- 11: heading `## XI. Earnings Management dan Income Smoothing`; embed `![Gambar 6. Taksonomi earnings management dan tiga mekanisme income smoothing | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 24–28](../assets/diagrams/gambar6_taksonomi_em.png)` (at the taxonomy point).

Coverage that must survive:
- **09** (moderate): summary-indicator concept; APB 15 rigid complexity; SFAS 21 nonpublic suspension; SFAS 128's three rationales; PEPS elimination + "less is more"; 3% rule elimination; basic vs diluted display + reconciliation; the table; bridge to X.
- **10** (deep cut but keep all four sub-topics): Development stage (SFAS 7, cost-nature-not-entity, rigid uniformity); Troubled debt (SFAS 15 economic-consequences triumph; SFAS 114 original-rate discounting + two dissents + debtor–creditor asymmetry); Early extinguishment (APB 26 → APB 30 nine-month flip → SFAS 4 extraordinary-like, constituency concession); Stock options (alignment vs WorldCom; APB 25 bargain mechanics in brief; 1993 ED Black-Scholes + 1994 withdrawal; SFAS 123 disclosure; SFAS 123R required expensing + IFRS 2; backdating + Efendi; entity-vs-proprietary and the reformat proposal); the diagram; bridge to XI. Trim the dense mechanics to their essentials.
- **11** (core, gentle cut): Schipper definition; agency motive triad; meet/beat asymmetry; classification shifting (McVay + Borden in brief); acquisition-inflation vs buyout-deflation (Erickson&Wang; Wu vs DeAngelo); Kasznik; detection difficulty + SEC seriousness; auditor study (Nelson et al.) in brief; compensation ceiling/floor (Healy et al.); discretionary vs real-cost accruals; income smoothing — valuation motive + Ronen&Sadan; three mechanisms; smoother profiles (Chaney&Jeter; DeFond&Park); three research problems; random-walk counterevidence; the diagram; bridge to XII.

- [ ] **Step 1: Edit the three files to budget, preserving headings/sub-headings/embeds/coverage.**

- [ ] **Step 2: Verify word counts, the four sub-headings, and embeds**
```powershell
foreach ($f in "09_earnings_per_share","10_topik_khusus","11_earnings_management") { $p="content/$f.md"; $w=(((Get-Content $p -Raw) -split '\s+')|?{$_ -ne ''}|Measure-Object).Count; "$f = $w" }
(Select-String -Path content/10_topik_khusus.md -Pattern '^### ').Count
Select-String -Path content/09_earnings_per_share.md -Pattern '@table'; Select-String -Path content/10_topik_khusus.md,content/11_earnings_management.md -Pattern '!\[Gambar'
```
Expected: 09≈290–360, 10≈520–640, 11≈540–660; sub-heading count in file 10 = **4**; the `@table` line in 09; the `![Gambar` lines in 10 and 11.

- [ ] **Step 3: Commit**
```powershell
git add content/09_earnings_per_share.md content/10_topik_khusus.md content/11_earnings_management.md
git commit -m "trim(rmk9): condense IX-XI to budget"
```

---

### Task 4: Trim §XII–XIII (files 12–13)

**Files:** Modify `content/12_perkembangan.md`, `content/13_sintesis.md`

Budgets: 12 → **410**; 13 → **320**.

Heading/sub-heading lines to preserve verbatim:
- 12: heading `## XII. Perkembangan dalam Income Statement`; the four `### ` sub-headings exactly: `### Cash Earnings`, `### Pro Forma Earnings`, `### Laporan G4+1 dan Pendekatan Matrix`, `### Retrospective Reports, Quality of Earnings, dan Restatements`. No embeds.
- 13: heading `## XIII. Sintesis`. No embeds.

Coverage that must survive:
- **12** (deep cut, keep four sub-topics): Cash Earnings (Howell + accrual rejoinder); Pro Forma (predictive rationale, bad-news misuse, Reg G 2002 equal-prominence + reconciliation); G4+1 + matrix (three components; Barker vs Glover; recurring/nonrecurring most promising); Retrospective/QoE/Restatements (Lundholm ex-post; two QoE definitions; restatements 1,420 in 2006, SOX 404, leases, SAB 99); bridge to XIII.
- **13** (core, gentle cut): the chapter's summary arc (historical-cost base; rigid-uniformity drift; comprehensive income vs pro-forma/G4+1 unresolved dialectic); the asset–liability/balance-sheet-cleanup shift (articulation back to Pert. VIII); explicit ties to course themes (decision usefulness, information asymmetry/agency, efficient markets, historical cost vs fair value); closing paragraph on *relevance* vs *reliability* and preparer discretion vs user needs.

- [ ] **Step 1: Edit the two files to budget, preserving headings/sub-headings/coverage.**

- [ ] **Step 2: Verify word counts and sub-headings**
```powershell
foreach ($f in "12_perkembangan","13_sintesis") { $p="content/$f.md"; $w=(((Get-Content $p -Raw) -split '\s+')|?{$_ -ne ''}|Measure-Object).Count; "$f = $w" }
(Select-String -Path content/12_perkembangan.md -Pattern '^### ').Count
```
Expected: 12≈370–450, 13≈290–360; sub-heading count in file 12 = **4**.

- [ ] **Step 3: Commit**
```powershell
git add content/12_perkembangan.md content/13_sintesis.md
git commit -m "trim(rmk9): condense XII-XIII to budget"
```

---

### Task 5: Rebuild, verify, page-count, commit

- [ ] **Step 1: Confirm total body word count is on target**
```powershell
$sum=0; Get-ChildItem content\0*.md,content\1*.md | ?{ $_.Name -notmatch '^00_|^14_' } | %{ $sum += (((Get-Content $_.FullName -Raw) -split '\s+')|?{$_ -ne ''}|Measure-Object).Count }; "BODY TOTAL = $sum"
```
Expected: ~5,300–5,800. If well above 5,800, do a micro-trim pass on files 10, 11, 03 before continuing.

- [ ] **Step 2: Rebuild the document (only the assembly stage changed)**
```powershell
python src/python/build_docx.py
```
Expected: `Saved: ...01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx` with a new (smaller) byte size.

- [ ] **Step 3: Run the test suite**
```powershell
cargo test -q 2>&1 | Select-String "test result"
python -m pytest src/python -q 2>&1 | Select-Object -Last 2
```
Expected: cargo 4+1 passed; pytest 12 passed. (The `build_docx` document-fixture tests still assert 14 headings, 6 images, 4 tables, A4/3cm — all unchanged by trimming.)

- [ ] **Step 4: Count actual pages via MS Word COM (Windows)**
```powershell
$path = (Resolve-Path "output\01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx").Path
try {
  $word = New-Object -ComObject Word.Application
  $word.Visible = $false
  $doc = $word.Documents.Open($path, $false, $true)
  $doc.Repaginate()
  $pages = $doc.ComputeStatistics(2)   # 2 = wdStatisticPages
  $words = $doc.ComputeStatistics(0)   # 0 = wdStatisticWords
  "PAGES = $pages ; WORDS = $words"
  $doc.Close($false); $word.Quit()
} catch { "Word COM unavailable: $($_.Exception.Message). Fall back to word-count proxy and ask user to confirm in Word." }
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) 2>$null | Out-Null
```
Expected: `PAGES = ` ~14–16. If PAGES > 16, return to the longest sections (10, 11, 03, 08) for a micro-trim of ~150–250 words total, rebuild, and re-count. If Word COM is unavailable, report the body word total (~5,500) as the proxy and note the user should confirm page count in Word.

- [ ] **Step 5: Commit the rebuilt document**
```powershell
git add content/ "output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx"
git commit -m "trim(rmk9): rebuild ~15-page RMK Pert. 9 document"
```

---

## Self-review (planning-time)

1. **Spec coverage:** visuals/tables/headings/front-matter/refs untouched (editing tasks modify only 01–13 prose and explicitly preserve embed lines + headings — Tasks 1–4); per-section budgets (Tasks 1–4 match the spec table); editing rules (universal block + per-file coverage lists); rebuild only assembly stage (Task 5 Step 2); test re-run (Task 5 Step 3); actual page count via Word COM with fallback (Task 5 Step 4); micro-trim contingency if > 16 pages (Task 5 Steps 1 & 4). All spec requirements mapped.
2. **Placeholder scan:** none — every task has concrete files, budgets, preserved-line text, coverage checklists, exact commands, and expected outputs.
3. **Consistency:** embed directive strings quoted here match those authored in the original build; file names match the repo; the four `### ` sub-headings for files 10 and 12 are enumerated explicitly; budgets sum to ~5,510 (within the spec's ~5,500 binding total).
