# RMK Pert. 9 → 10 Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Condense the RMK to a hard ~10 pages: trim body prose to ~3,300 words, keep only 4 of 10 visuals, and remove the references section — while keeping every section I–XIII graduate-usable.

**Architecture:** One builder change (skip the references file in the body loop) + four content-trim batches (each also deletes the dropped embed lines) + a rebuild/iterate task that measures real pages via MS Word COM and micro-adjusts until ≤10.

**Tech Stack:** Markdown content; `src/python/build_docx.py` (python-docx); pytest; PowerShell + MS Word COM page counting.

**Working dir:** `D:\DZAKI\S2\Sem. 1\Pelaporan Keuangan Korporat\rmk-pkk-pert9-income-statement`. Branch: create `feat/rmk-pert9-10pages` from master.

**Spec:** `docs/superpowers/specs/2026-06-08-rmk-pert9-10pages-design.md`.

**Visual decisions (apply across content tasks):**
- KEEP (leave the embed line verbatim, in place): Tabel 1 in `02`, Gambar 1 in `03`, Gambar 4 at end of `06`, Gambar 6 in `11`.
- DROP (delete the entire embed line from the file): Gambar 2 in `04`, Gambar 3 in `05`, Tabel 2 in `07`, Tabel 3 in `08`, Tabel 4 in `09`, Gambar 5 in `10`. The concept the dropped visual illustrated must remain described in the bullets.

**Universal trim rules:** keep the `##` heading and `###` sub-headings; keep bulleted style + simple language; preserve every concept, standard reference (ARB/APB/SFAS/SFAC/ASU), and the section's central tension; keep ≥1 `(Wolk et al., 2017, PDF hlm. N)` citation per section (consolidate freely); keep a one-line bridge. Cut secondary examples, minor researchers, and repetition. Word count of a file (rendered, excludes image-alt lines): `((Get-Content <f> | ?{ $_ -notmatch '^!\[' }) -join ' ' -split '\s+' | ?{$_ -ne ''} | Measure-Object).Count`.

---

### Task 0: Branch

- [ ] **Step 1**
```powershell
git checkout master
git checkout -b feat/rmk-pert9-10pages
```
Expected: `Switched to a new branch 'feat/rmk-pert9-10pages'`.

---

### Task 1: Builder skips references; update tests

**Files:** Modify `src/python/build_docx.py`, `src/python/test_build_docx.py`

- [ ] **Step 1: Exclude the references file from the body loop.** In `build_docx.py`, find:
```python
        if os.path.basename(path).startswith("00_"):
            continue
```
Replace with:
```python
        if os.path.basename(path).startswith(("00_", "14_")):
            continue  # 00 = front matter (handled above); 14 = references (omitted per spec)
```

- [ ] **Step 2: Update the structural test** in `test_build_docx.py`. Replace the `test_six_images_and_four_tables` test with:
```python
def test_four_kept_visuals(built):
    # After 10-page curation: keep Tabel 1 (1 table) + Gambar 1/4/6 (3 images).
    assert len(built.inline_shapes) == 3
    assert len(built.tables) == 1


def test_no_references_section(built):
    text = "\n".join(p.text for p in built.paragraphs)
    assert "XIV." not in text and "Referensi" not in text
    # Body ends at XIII. Sintesis
    romans = [p.text for p in built.paragraphs
              if p.text.strip()[:5].rstrip(". ") in
              ("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV")]
```
(The `romans` line is illustrative; the two asserts are what matter. If the existing test file imports differ, keep imports intact — only swap this one test function.)

- [ ] **Step 3: Run the parser-only tests to confirm no import breakage**
```powershell
python -m pytest src/python/test_build_docx.py -q -k "inline or blocks or caption"
```
Expected: 3 passed. (Document-fixture tests will be re-run after content trimming in Task 6 — they need the trimmed content + curated embeds to pass.)

- [ ] **Step 4: Commit**
```powershell
git add src/python/build_docx.py src/python/test_build_docx.py
git commit -m "feat(rmk9): builder omits references section; tests expect 4 kept visuals"
```

---

### Task 2: Trim §I–IV + drop Gambar 2 (files 01–04)

**Files:** Modify `content/01_orientasi.md` (→~200 w), `content/02_definisi_income_elemen.md` (→~320 w, KEEP `@table(../assets/tables/tabel1_definisi.toml)`), `content/03_pengakuan_pendapatan.md` (→~300 w, KEEP `![Gambar 1 ...](../assets/diagrams/gambar1_titik_pengakuan.png)`), `content/04_pengakuan_beban_matching.md` (→~230 w, DELETE the `![Gambar 2 ...]` embed line).

- [ ] **Step 1: Edit the four files.** Trim to budgets; in `04` remove the Gambar 2 embed line entirely (keep the matching-hierarchy explanation in bullets). Keep all concepts: §I (statement role, articulation w/ Pert. VIII, decision usefulness, roadmap); §II (4 definitions, revenue–expense vs asset–liability, gains/expenses/losses, table); §III (4 timing points + standards, point-of-sale norm, SFAS 32, 3 measurable attributes, Qwest, ASU 2014-09/IFRS 15, SAB 101, gambar 1); §IV (3 APB St.4 categories, matching hierarchy, Thomas arbitrariness, allocation-free, information-content rejoinder).

- [ ] **Step 2: Verify**
```powershell
foreach ($f in "01_orientasi","02_definisi_income_elemen","03_pengakuan_pendapatan","04_pengakuan_beban_matching"){ $p="content/$f.md"; "$f=" + ((Get-Content $p | ?{ $_ -notmatch '^!\[' }) -join ' ' -split '\s+'|?{$_ -ne ''}|Measure-Object).Count }
Select-String content/02_definisi_income_elemen.md -Pattern '@table'      # expect 1
Select-String content/03_pengakuan_pendapatan.md -Pattern 'gambar1'        # expect 1
Select-String content/04_pengakuan_beban_matching.md -Pattern 'gambar2'    # expect 0 (dropped)
```
Expected totals ≈ 01:170–230, 02:280–360, 03:260–340, 04:200–260; tabel1 & gambar1 present; gambar2 absent.

- [ ] **Step 3: Commit**
```powershell
git add content/01_orientasi.md content/02_definisi_income_elemen.md content/03_pengakuan_pendapatan.md content/04_pengakuan_beban_matching.md
git commit -m "condense(rmk9): I-IV to budget, drop Gambar 2 embed"
```

---

### Task 3: Trim §V–VIII + drop Gambar 3, Tabel 2, Tabel 3 (files 05–08)

**Files:** `content/05_future_events.md` (→~220 w, DELETE `![Gambar 3 ...]`), `content/06_current_operating_vs_all_inclusive.md` (→~300 w, KEEP `![Gambar 4 ...](../assets/diagrams/gambar4_evolusi_laba.png)` at end), `content/07_comprehensive_income.md` (→~260 w, DELETE `@table(...tabel2_format_ci.toml)`), `content/08_seksi_nonoperasi.md` (→~250 w, DELETE `@table(...tabel3_accounting_changes.toml)`).

- [ ] **Step 1: Edit the four files.** Remove the three dropped embed lines; keep their concepts in bullets. Preserve: §V (future-events dependence, one/two-event view, SFAS 5 probabilities + 3 approaches, management-intent rejection, Beaver, SFAS 109); §VI (CO vs AI, four all-inclusive arguments, AAA/AICPA/APB 9, ASU 2011, Gonedes, big bath/Citicorp, gambar 4); §VII (SFAC 5, proprietary theory, OCI elements SFAS 130, three formats + Board preference + dissent, no-EPS-for-CI); §VIII (extraordinary ARB 32/43→APB 9→APB 30 rigid uniformity, accounting changes APB 20 vs SFAS 154, prior-period APB 9→SFAS 16, recurring/transitory).

- [ ] **Step 2: Verify**
```powershell
foreach ($f in "05_future_events","06_current_operating_vs_all_inclusive","07_comprehensive_income","08_seksi_nonoperasi"){ $p="content/$f.md"; "$f=" + ((Get-Content $p | ?{ $_ -notmatch '^!\[' }) -join ' ' -split '\s+'|?{$_ -ne ''}|Measure-Object).Count }
Select-String content/06_current_operating_vs_all_inclusive.md -Pattern 'gambar4'   # expect 1
Select-String content/05_future_events.md -Pattern 'gambar3'                         # expect 0
Select-String content/07_comprehensive_income.md -Pattern 'tabel2'                   # expect 0
Select-String content/08_seksi_nonoperasi.md -Pattern 'tabel3'                       # expect 0
```
Expected totals ≈ 05:190–250, 06:270–340, 07:230–300, 08:220–290; gambar4 present; gambar3/tabel2/tabel3 absent.

- [ ] **Step 3: Commit**
```powershell
git add content/05_future_events.md content/06_current_operating_vs_all_inclusive.md content/07_comprehensive_income.md content/08_seksi_nonoperasi.md
git commit -m "condense(rmk9): V-VIII to budget, drop Gambar 3 + Tabel 2 + Tabel 3 embeds"
```

---

### Task 4: Trim §IX–XI + drop Tabel 4, Gambar 5 (files 09–11)

**Files:** `content/09_earnings_per_share.md` (→~200 w, DELETE `@table(...tabel4_eps.toml)`), `content/10_topik_khusus.md` (→~340 w, DELETE `![Gambar 5 ...]`; KEEP its four `###` sub-headings), `content/11_earnings_management.md` (→~340 w, KEEP `![Gambar 6 ...](../assets/diagrams/gambar6_taksonomi_em.png)`).

- [ ] **Step 1: Edit the three files.** Remove the two dropped embeds; keep concepts in bullets. Preserve: §IX (summary indicator, APB 15 complexity, SFAS 21, SFAS 128 three rationales, PEPS elimination, 3% rule, basic/diluted + reconciliation); §X under its 4 sub-heads (SFAS 7; SFAS 15/114 + dissents + asymmetry; APB 26/30 + SFAS 4; stock options APB 25→SFAS 123→123R + IFRS 2 + backdating + entity/proprietary reformat); §XI (Schipper, agency triad, classification shifting McVay/Borden, acquisition/buyout, Kasznik, auditor study, ceiling/floor Healy, discretionary vs real accruals, smoothing mechanisms + Chaney&Jeter/DeFond&Park + random-walk, gambar 6).

- [ ] **Step 2: Verify**
```powershell
foreach ($f in "09_earnings_per_share","10_topik_khusus","11_earnings_management"){ $p="content/$f.md"; "$f=" + ((Get-Content $p | ?{ $_ -notmatch '^!\[' }) -join ' ' -split '\s+'|?{$_ -ne ''}|Measure-Object).Count }
(Select-String content/10_topik_khusus.md -Pattern '^### ').Count   # expect 4
Select-String content/11_earnings_management.md -Pattern 'gambar6'   # expect 1
Select-String content/09_earnings_per_share.md -Pattern 'tabel4'     # expect 0
Select-String content/10_topik_khusus.md -Pattern 'gambar5'          # expect 0
```
Expected totals ≈ 09:170–230, 10:300–380, 11:300–380; file 10 sub-heads = 4; gambar6 present; tabel4/gambar5 absent.

- [ ] **Step 3: Commit**
```powershell
git add content/09_earnings_per_share.md content/10_topik_khusus.md content/11_earnings_management.md
git commit -m "condense(rmk9): IX-XI to budget, drop Tabel 4 + Gambar 5 embeds"
```

---

### Task 5: Trim §XII–XIII (files 12–13)

**Files:** `content/12_perkembangan.md` (→~240 w, KEEP its four `###` sub-headings, no embeds), `content/13_sintesis.md` (→~230 w, no embeds).

- [ ] **Step 1: Edit the two files.** Preserve: §XII under its 4 sub-heads (Cash Earnings Howell + rebuttal; Pro Forma + Reg G 2002; G4+1 + matrix Barker/Glover; Lundholm + QoE + restatements 1,420/SOX 404/SAB 99); §XIII (summary arc historical-cost→rigid uniformity→CI vs pro-forma dialectic; asset–liability shift + articulation to Pert. VIII; course themes decision usefulness / information asymmetry-agency / efficient markets / historical cost vs fair value; closing relevance-vs-reliability).

- [ ] **Step 2: Verify**
```powershell
foreach ($f in "12_perkembangan","13_sintesis"){ $p="content/$f.md"; "$f=" + ((Get-Content $p | ?{ $_ -notmatch '^!\[' }) -join ' ' -split '\s+'|?{$_ -ne ''}|Measure-Object).Count }
(Select-String content/12_perkembangan.md -Pattern '^### ').Count   # expect 4
```
Expected: 12:210–280, 13:200–270; file 12 sub-heads = 4.

- [ ] **Step 3: Commit**
```powershell
git add content/12_perkembangan.md content/13_sintesis.md
git commit -m "condense(rmk9): XII-XIII to budget"
```

---

### Task 6: Rebuild, iterate to 10 pages, verify, finish

- [ ] **Step 1: Confirm body total**
```powershell
$t=0; Get-ChildItem content\*.md | ?{ $_.Name -notmatch '^00_|^14_' } | %{ $t += ((Get-Content $_.FullName | ?{ $_ -notmatch '^!\[' }) -join ' ' -split '\s+'|?{$_ -ne ''}|Measure-Object).Count }; "BODY TOTAL = $t"
```
Expected ~3,100–3,500.

- [ ] **Step 2: Rebuild and count pages**
```powershell
python src/python/build_docx.py | Select-String "Size"
$path=(Resolve-Path "output\01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx").Path
$w=New-Object -ComObject Word.Application; $w.Visible=$false; $d=$w.Documents.Open($path); $d.Repaginate(); "PAGES = "+$d.ComputeStatistics(2)+" ; WORDS = "+$d.ComputeStatistics(0); $d.Close($false); $w.Quit()
```
Expected: `PAGES = ` 10 or 11.

- [ ] **Step 3: If PAGES > 10, iterate.** Apply in this order until ≤10, rebuilding + recounting after each:
  1. Shrink the 4 kept diagrams: in `build_docx.py` `add_image_with_caption`, change `width=Cm(14.5)` to `width=Cm(12)` (commit message: `style(rmk9): shrink kept diagrams to 12cm`).
  2. If still >10, trim ~150–250 words from the longest files (10, 11, 03) and rebuild.
  3. If still >10, reduce `BODY_LINE_PT` from 12 to 11.5.
  Stop as soon as PAGES ≤ 10.

- [ ] **Step 4: Run the test suite**
```powershell
cargo test -q 2>&1 | Select-String "test result"
python -m pytest src/python -q 2>&1 | Select-Object -Last 2
```
Expected: cargo 4+1 passed; pytest all passed (incl. updated `test_four_kept_visuals` = 3 images + 1 table, and `test_no_references_section`).

- [ ] **Step 5: Structural confirmation**
```powershell
python -c "from docx import Document; import re; d=Document(r'output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx'); rs=[p.text for p in d.paragraphs if re.match(r'^(I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII)\. ',p.text.strip())]; print('sections:',len(rs),'| images:',len(d.inline_shapes),'| tables:',len(d.tables),'| has_XIV:', any('XIV' in p.text for p in d.paragraphs))"
```
Expected: sections: 13 | images: 3 | tables: 1 | has_XIV: False.

- [ ] **Step 6: Commit the rebuilt document**
```powershell
git add content/ src/python/build_docx.py "output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx"
git commit -m "condense(rmk9): rebuild final 10-page document (4 visuals, no references)"
```

---

## Self-review (planning-time)

1. **Spec coverage:** 10-page hard target (Task 6 Steps 2–3 iterate via Word COM); no references (Task 1 builder skip + `test_no_references_section`); keep sections I–XIII (content tasks preserve every heading + concept list); 4 kept / 6 dropped visuals (explicit per-file KEEP/DELETE in Tasks 2–5 + verify greps); ~3,300-word budget (per-file targets sum ≈ 3,430; Task 6 Step 1 checks total); test update to 3 images + 1 table (Task 1 Step 2). All covered.
2. **Placeholders:** none — exact files, budgets, embed-line keep/delete instructions, greps with expected counts, and the iterate ladder are all concrete.
3. **Consistency:** embed filenames (tabel1_definisi, gambar1_titik_pengakuan, gambar4_evolusi_laba, gambar6_taksonomi_em kept; gambar2/gambar3/gambar5/tabel2/tabel3/tabel4 dropped) match the repo; the test names (`test_four_kept_visuals`, `test_no_references_section`) are introduced in Task 1 and referenced in Task 6 Step 4; "3 images + 1 table" is consistent everywhere (Tabel 1 = table; Gambar 1/4/6 = images).
