# Winston Typography Redesign — Implementation Plan

> **For agentic workers:** PARTIAL automation only. Tasks A, B, AI, AJ are mechanical and can be subagent-dispatched. Tasks C-001 … C-032 (per-slide reflow) require **user approval gate via Visual Companion** for each slide and are CONTROLLER-driven (cannot be batched to a subagent without losing the spec's per-slide gate). Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Operationalize Winston typography redesign per spec `2026-04-27-typography-redesign-design.md`: (Phase 1) replace 12 CSS type tokens at v6.html lines 28-38 with the Balanced 40pt-floor scale; (Phase 2) for each of 32 slides, push BEFORE/AFTER mockup → user approves → apply edit → commit, with audit trail in `reflow-log.md`.

**Architecture:** Two-phase with hybrid overflow policy. Phase 1 = single root-level token substitution commit. Phase 2 = 32 controller-led iterations, each with a mockup→gate→edit→commit cycle. v5 (1).html stays untouched as control sample. v6-winston.html progresses from "broken post-Phase-1" through 32 reflowed-slide commits to "final Winston-compliant deck".

**Tech Stack:** Markdown (specs, log, plan), HTML/CSS edit (v6.html), Visual Companion server (`.superpowers/brainstorm/<session>/content/`), Bash (grep verification, git), Edit/MultiEdit tools.

**Critical rules from spec (do NOT violate):**
- E1 split-first for theory+case slides 4-29; cut-first for opening+close slides 1-3, 30-32; no upper bound on splits
- E2 do NOT modify FASB/INDF substance content (out of scope, deferred option b)
- E3 Slogan slides 02/07/19/30 must use lead (60px) or h2 (84px); never shrink to caption tier
- E4 only `font-size` and optional `line-height` properties may change; color/weight/letter-spacing untouched
- E5 mid-loop strategy changes are OK; flag in reflow-log
- E6 v6 is intentionally broken between Task B commit and last per-slide commit; do not rollback
- v5 (1).html never modified

---

## File Structure

| Path | Created/Modified | Owner Task |
|------|------------------|------------|
| `specs/typography-tokens.md` | Create | Task A |
| `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html` | Modify lines 28-38 (Task B), then per-slide content sections (Tasks C-001…C-032) | Tasks B, C-001..C-032 |
| `analysis/winston-audit/reflow-log.md` | Create (Task A); append per slide (Tasks C-001…C-032); finalize (Task AI) | All Tasks |
| `.superpowers/brainstorm/<session>/content/slide-NN-review-vK.html` | Create per-slide mockup (gitignored) | Tasks C-001..C-032 |

---

## Pre-flight Checklist

- [ ] **Step 0a: Set up worktree**

```bash
cd "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat"
git worktree add .worktrees/typography-redesign -b feature/typography-redesign
cd .worktrees/typography-redesign
```

- [ ] **Step 0b: Start Visual Companion server**

```bash
"C:/Users/HP/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.7/skills/brainstorming/scripts/start-server.sh" \
  --project-dir "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat"
```
Note URL and screen_dir from `$STATE_DIR/server-info`.

- [ ] **Step 0c: Verify v6 in worktree matches v5 (md5)**

```bash
md5sum "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html" \
       "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html"
```
Expected: identical hashes (`fb0816fe…`). If not, abort.

---

## Task A: Create `specs/typography-tokens.md` and seed `reflow-log.md`

**Files:**
- Create: `specs/typography-tokens.md`
- Create: `analysis/winston-audit/reflow-log.md`

- [ ] **Step 1: Write `specs/typography-tokens.md` with the Balanced scale**

```markdown
# Winston Typography Tokens — Balanced Scale (Single Source of Truth)

**Source:** `docs/superpowers/specs/2026-04-27-typography-redesign-design.md` Bagian 3.
**Compliance:** Strict-Content level — body/lead/heading ≥53px (Winston 40pt floor on 1920×1080 canvas); body-sm/meta/label/caption are caps-tier.
**Canvas:** 1920×1080 fixed (per v5 line 2 `<deck-stage>` definition).

## Token Definitions

| Token | Size (px) | Line-height | Weight | Tier | Notes |
|-------|-----------|-------------|--------|------|-------|
| `.t-h1` | 110 | 1.05 | 800 | DECK heading | Cover, section dividers |
| `.t-h2` | 84 | 1.05 | 800 | DECK heading | Slide titles |
| `.t-h3` | 68 | 1.10 | 700 | DECK heading | Subsection headings |
| `.t-h4` | 60 | 1.15 | 700 | DECK heading | Card titles |
| `.t-h5` | 53 | 1.20 | 700 | DECK heading | Smallest hierarchy heading |
| `.t-lead` | 60 | 1.25 | 400 | Subtitle/lead | Slide subtitles, key sentences |
| `.t-body` | 53 | 1.30 | 400 | Body | Main reading text |
| `.t-body-dark` | 53 | 1.30 | 400 | Body (dark on light) | Same as body, navy color |
| `.t-body-sm` | 36 | 1.30 | 400 | Caption tier | Card descriptions, secondary text |
| `.t-caption` | 36 | 1.30 | 400 | Caption tier | Image captions, table footnotes |
| `.t-meta` | 28 | 1.20 | 600 | Metadata tier | Slide-number, breadcrumbs |
| `.t-label` | 28 | 1.20 | 700 | Label tier | Uppercase labels, badges |

## Properties NOT changed by this redesign

- `color` — preserve all existing color tokens (`var(--navy-900)`, `var(--slate-500)`, etc.)
- `letter-spacing` — preserve all existing tracking values
- `font-weight` — preserve weights as listed above; existing weights are correct
- `font-family` — Inter remains the deck typeface

## Migration Verification

- After Phase 1 (`v6-winston.html` lines 28-38), `git diff` shows ONLY `font-size` and `line-height` changes
- After Phase 2 (32 per-slide commits), no inline `font-size` declaration is below 36px except where flagged in `reflow-log.md` Exceptions section
```

- [ ] **Step 2: Write `analysis/winston-audit/reflow-log.md` skeleton**

```markdown
# Typography Reflow Log — v6-winston.html

**Spec:** `docs/superpowers/specs/2026-04-27-typography-redesign-design.md`
**Tokens:** `specs/typography-tokens.md`
**v5 baseline (control sample):** md5 `fb0816fe4c4987e235fd06a31b5cd94a`

## Phase 1 — Token Substitution

- **Commit SHA:** [filled by Task B]
- **Timestamp:** [filled by Task B]
- **Tokens replaced:** 12 (per `specs/typography-tokens.md`)

## Phase 2 — Per-Slide Reflow

| Slide | Strategy | Splits | Exception | Approved | Commit |
|-------|----------|--------|-----------|----------|--------|
| 01 | (pending) | — | — | — | — |
| 02 | (pending) | — | — | — | — |
| ... | (pending) | — | — | — | — |
| 32 | (pending) | — | — | — | — |

## Exceptions

(pending — populated as exceptions are flagged during Phase 2)

## Mid-Course Corrections

(pending — populated if strategy changes mid-loop per spec E5)

## Out-of-Scope Flags

(pending — populated when CONTENT-DRIFT or block-structure-update items emerge)
```

- [ ] **Step 3: Commit**

```bash
git add specs/typography-tokens.md analysis/winston-audit/reflow-log.md
git commit -m "docs(spec): add typography tokens + reflow-log skeleton

Defines the 12 Winston-compliant Balanced-scale tokens (single source
of truth for Phase 1) plus the audit-trail skeleton populated during
Phase 2. Tokens: h1=110, h2=84, h3=68, h4=60, h5=53, lead=60, body=53,
body-dark=53, body-sm=36, caption=36, meta=28, label=28.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task B: Phase 1 — Root-Level Token Substitution

**Files:**
- Modify: `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html` lines 28-38

- [ ] **Step 1: Read current v6 lines 28-38 to confirm exact baseline**

```bash
sed -n '28,38p' "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html"
```
Expected output (must match v5 exactly since v6 is byte-identical pre-Phase-1):
```
  .t-h1{font-weight:800;font-size:96px;line-height:1;letter-spacing:-0.04em}
  .t-h2{font-weight:800;font-size:68px;line-height:1.03;letter-spacing:-0.035em}
  .t-h3{font-weight:700;font-size:48px;line-height:1.08;letter-spacing:-0.03em}
  .t-h4{font-weight:700;font-size:34px;line-height:1.15;letter-spacing:-0.025em}
  .t-h5{font-weight:700;font-size:26px;line-height:1.2;letter-spacing:-0.02em}
  .t-lead{font-weight:400;font-size:26px;line-height:1.38;color:var(--slate-500);letter-spacing:-0.015em}
  .t-body{font-weight:400;font-size:22px;line-height:1.45;color:var(--slate-500)}
  .t-body-dark{font-weight:400;font-size:22px;line-height:1.45;color:var(--navy-900)}
  .t-body-sm{font-weight:400;font-size:18px;line-height:1.45;color:var(--slate-500)}
  .t-label{font-weight:700;font-size:13px;line-height:1.2;color:var(--slate-500);letter-spacing:0.1em;text-transform:uppercase}
  .t-meta{font-weight:600;font-size:16px;line-height:1.2;color:var(--slate-500);letter-spacing:0.02em}
```

If output differs (lines drift, additional rules), STOP and report — plan assumes the v5 baseline.

- [ ] **Step 2: Apply token substitution via Edit tool**

For each of the 12 token lines, replace the `font-size` and `line-height` values. Keep all other properties (`font-weight`, `color`, `letter-spacing`, `text-transform`) verbatim.

Target lines (one Edit per token, or one MultiEdit batch):

```css
.t-h1{font-weight:800;font-size:110px;line-height:1.05;letter-spacing:-0.04em}
.t-h2{font-weight:800;font-size:84px;line-height:1.05;letter-spacing:-0.035em}
.t-h3{font-weight:700;font-size:68px;line-height:1.10;letter-spacing:-0.03em}
.t-h4{font-weight:700;font-size:60px;line-height:1.15;letter-spacing:-0.025em}
.t-h5{font-weight:700;font-size:53px;line-height:1.20;letter-spacing:-0.02em}
.t-lead{font-weight:400;font-size:60px;line-height:1.25;color:var(--slate-500);letter-spacing:-0.015em}
.t-body{font-weight:400;font-size:53px;line-height:1.30;color:var(--slate-500)}
.t-body-dark{font-weight:400;font-size:53px;line-height:1.30;color:var(--navy-900)}
.t-body-sm{font-weight:400;font-size:36px;line-height:1.30;color:var(--slate-500)}
.t-label{font-weight:700;font-size:28px;line-height:1.20;color:var(--slate-500);letter-spacing:0.1em;text-transform:uppercase}
.t-meta{font-weight:600;font-size:28px;line-height:1.20;color:var(--slate-500);letter-spacing:0.02em}
```

Note: v5 has `.t-h1`–`.t-meta` (11 tokens at lines 28-38) plus `.t-caption` defined separately later in CSS. Find `.t-caption` and update its `font-size:18px` to `font-size:36px` and add `line-height:1.30` if absent (verify by grep first).

- [ ] **Step 3: Verify diff is font-size/line-height ONLY**

```bash
git diff "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html" | grep -E '^[-+]' | grep -vE '^[-+]{3}|font-size|line-height'
```
Expected: empty output (no other property changed). If output appears, revert and retry.

- [ ] **Step 4: Update reflow-log Phase 1 entry with commit SHA placeholder**

Edit `reflow-log.md` Phase 1 section: replace `[filled by Task B]` placeholders with timestamp `2026-04-27T<HH:MM>` and a note that the SHA is the next commit. After the commit in Step 5, return to amend with the actual SHA.

- [ ] **Step 5: Commit**

```bash
git add "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html" \
        analysis/winston-audit/reflow-log.md
git commit -m "feat(deck): apply Winston typography token substitution (Phase 1)

Replaces the 12 type tokens in v6-winston.html lines 28-38 (and
.t-caption) with the Balanced 40pt-floor scale per
specs/typography-tokens.md. v6 is now intentionally in 'broken
overflow' state until Phase 2 per-slide reflow completes (per spec
E6). v5 (1).html unchanged as control sample.

Diff scope: font-size and line-height only. color, font-weight,
letter-spacing, text-transform untouched per spec E4.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

- [ ] **Step 6: Amend reflow-log with actual SHA**

```bash
SHA=$(git log -1 --format=%H)
# Edit reflow-log Phase 1 SHA placeholder to actual SHA via Edit tool, then:
git add analysis/winston-audit/reflow-log.md
git commit --amend --no-edit
```

---

## Task C-NN Template (32 instances: C-001, C-002, …, C-032)

**This task pattern repeats 32 times. Each instance is one slide. Slide N maps to instance C-NN.** Controller (you) drives the loop; user approves each mockup before edit ships.

**Files (per slide N):**
- Read: `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html` (find slide N section)
- Read: `analysis/winston-audit/crime-inventory.md` (find slide N row(s))
- Read: `rubrics/slide-NN.md` (already exists from previous session — context for STAR/F5/role)
- Create: `.superpowers/brainstorm/<session>/content/slide-NN-review-v1.html` (mockup; not committed)
- Modify: `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html` (slide N section)
- Append: `analysis/winston-audit/reflow-log.md` (Phase 2 table row for slide N)

**Strategy lookup:**
- Slides 1, 2, 3, 30, 31, 32 → **cut-first** (preserve slide count)
- Slides 4-29 → **split-first** (preserve substance, deck grows)

- [ ] **Step 1: Read current state of slide N in v6**

Use Grep to locate slide N's section (typical pattern in v5/v6: `data-screen-label="..."` or `<section>` with nth-child=N). Capture the exact line range.

- [ ] **Step 2: Read crime-inventory entries for slide N**

```bash
grep -E '^\| 0?N |' analysis/winston-audit/crime-inventory.md
# Replace N with the slide number (zero-padded for 01-09)
```
Note all crime entries for this slide (typically 3-4 rows: Crime #2, #3, #7, sometimes #9/#10 for slide 32).

- [ ] **Step 3: Read rubric for STAR/F5/role context**

```bash
sed -n '1,15p' rubrics/slide-NN.md  # front-matter
grep -A 3 'STAR Alignment' rubrics/slide-NN.md  # STAR applicability
grep -A 3 'F5 Trigger' rubrics/slide-NN.md  # F5 trigger flag
```

- [ ] **Step 4: Determine reflow plan for slide N**

Decision tree:
- If slide is in {1, 2, 3, 30, 31, 32}: **cut-first**. Identify words/sentences that can be removed without violating E1 (FASB Supremacy) or E3 (Slogan preservation). Output: 1 final slide with reduced content.
- If slide is in {4..29}: **split-first**. Identify natural content boundaries (paragraph breaks, list-item groupings). Output: K slides where K = ceil(content / fits-per-slide). Typical K = 2; some heavy slides (multi-table) may go K=3-4.
- Special: if slide content references unsplittable agg-table that fits with body-sm (36px), apply E1 exception. Flag in reflow-log.

- [ ] **Step 5: Build BEFORE/AFTER mockup HTML**

Write `.superpowers/brainstorm/<session>/content/slide-NN-review-v1.html`. Template:

```html
<h2>Slide NN Reflow Review</h2>
<p class="subtitle">Strategy: <strong>[cut-first | split-first → K slides]</strong> · v5 audit findings: [list crimes from inventory] · STAR alignment: [list applicable elements]</p>

<div class="section">
  <span class="label">BEFORE — Phase 1 raw (overflow)</span>
  <div class="mockup">
    <div class="mockup-header">v6 slide NN, post-Phase-1 token substitution</div>
    <div class="mockup-body" style="padding:24px;background:#fff;color:#0b1220;height:540px;overflow:hidden">
      <!-- Reproduce slide NN content with Phase-1 token sizes — likely overflow -->
      <h2 style="font-size:84px;font-weight:800;line-height:1.05;margin:0 0 14px">[Slide title]</h2>
      <p style="font-size:53px;line-height:1.30;color:#5a6478;margin:0 0 18px">[Body text first paragraph from v5]</p>
      <p style="font-size:53px;line-height:1.30;color:#5a6478;margin:0">[Body text remaining paragraphs — overflow expected]</p>
    </div>
  </div>
</div>

<div class="section">
  <span class="label">AFTER — proposed reflow</span>
  [Show K slides side-by-side using class="split", or show single cut-down slide.
   Each shows fitted content per Balanced tokens.]
</div>

<div class="section">
  <span class="label">Reflow plan</span>
  <ul>
    <li><strong>Strategy:</strong> [cut-first | split-first to K=N slides]</li>
    <li><strong>Splits at:</strong> [describe content boundaries — e.g., "after Faithful Representation paragraph", "before Free from Error subsection"]</li>
    <li><strong>Cuts:</strong> [describe words/sentences removed if cut-first]</li>
    <li><strong>STAR preservation:</strong> [if Slogan slide: confirm Slogan stays at lead/h2 size]</li>
    <li><strong>Exceptions:</strong> [E1-table-aggregate flag if applicable, else "none"]</li>
  </ul>
</div>

<div class="options">
  <div class="option" data-choice="approve" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content"><h3>Approve — apply this reflow</h3></div>
  </div>
  <div class="option" data-choice="revise" onclick="toggleSelect(this)">
    <div class="letter">B</div>
    <div class="content"><h3>Revise — see comments in terminal</h3></div>
  </div>
  <div class="option" data-choice="skip" onclick="toggleSelect(this)">
    <div class="letter">C</div>
    <div class="content"><h3>Skip this slide for now (return later)</h3></div>
  </div>
</div>
```

- [ ] **Step 6: Push mockup, prompt user, wait**

Tell user: "Slide NN mockup pushed. Open http://localhost:<port>. Approve / Revise / Skip?"

End turn. Wait for user response.

- [ ] **Step 7: On user response**

- **Approve:** continue to Step 8.
- **Revise:** read user feedback, update mockup to v2 (filename `slide-NN-review-v2.html`), repeat Step 6.
- **Skip:** mark reflow-log row as "DEFERRED", do not commit, move to next slide. Return to skipped slides at end before Task AI.

- [ ] **Step 8: Apply edit to v6.html**

Use Edit/MultiEdit tool to apply the approved reflow to the slide N section in v6.html. For split-first, this means:
- Insert (K-1) new `<section>` elements after the original
- Distribute content per the approved boundaries
- Adjust slide-number metadata if any per-slide numbering exists

For cut-first, this means: shorten body/lead text per approved cuts.

Verify with `git diff` that only the slide N section changed.

- [ ] **Step 9: Append reflow-log entry**

Edit `reflow-log.md` Phase 2 table, replace the `(pending)` row for slide NN with:

```
| NN | [cut-first | split-first] | [K if split] | [exception flag or —] | 2026-04-27T<HH:MM> | <commit SHA placeholder> |
```

If exception was used (E1 table-aggregate), also append a row to the Exceptions section describing what and why.

- [ ] **Step 10: Commit**

```bash
git add "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html" \
        analysis/winston-audit/reflow-log.md
git commit -m "feat(deck): slide NN winston reflow ([cut-first | split-first → K slides])

[1-2 line description: which content boundaries chosen for split, or which
words removed for cut. Note any exception flags.]

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

- [ ] **Step 11: Backfill commit SHA in reflow-log**

```bash
SHA=$(git log -1 --format=%H)
# Edit reflow-log slide NN row to replace SHA placeholder with actual SHA
git add analysis/winston-audit/reflow-log.md
git commit --amend --no-edit
```

- [ ] **Step 12: Move to slide NN+1, repeat from Step 1**

End-of-loop check: when N = 32 done, proceed to Task AI.

---

## Task AI: Finalize `reflow-log.md`

**Files:**
- Modify: `analysis/winston-audit/reflow-log.md`

- [ ] **Step 1: Verify all 32 rows in Phase 2 table populated**

```bash
grep -cE '^\| (0[1-9]|[12][0-9]|3[0-2]) \| (cut-first|split-first|DEFERRED)' analysis/winston-audit/reflow-log.md
```
Expected: 32. If less, revisit deferred slides.

- [ ] **Step 2: Resolve any DEFERRED slides**

For each slide with strategy `DEFERRED`: re-run Task C-NN (Steps 1-11) for that slide.

- [ ] **Step 3: Populate "Out-of-Scope Flags" section**

Required flag: `presentation-design-spec.md block structure update needed — original 32-slide block (Opening 1-3, Proof 4-29, Close 30-32) no longer reflects post-reflow deck count of [computed-N]. Renumbering and block-boundary update is out-of-scope per typography-redesign-design.md V4; defer to a separate brainstorming session.`

Add any CONTENT-DRIFT flags accumulated during Phase 2.

- [ ] **Step 4: Compute final slide count**

```bash
grep -cE '<section[^>]*data-screen-label' "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html"
```
(or whichever marker delimits slides in v5/v6 — verify in Step 1 of any C-NN task). Record this number in the "Phase 2" header section of reflow-log.

- [ ] **Step 5: Commit**

```bash
git add analysis/winston-audit/reflow-log.md
git commit -m "audit(reflow): finalize reflow-log with exceptions, drift flags, slide count

All 32 source slides processed. Final v6 deck has [computed-N] slides.
Out-of-scope flag added: presentation-design-spec.md block structure
update required in separate session.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task AJ: Final V3 Grep Verification (Crime #3 Compliance Check)

**Files:**
- Read: `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html`

- [ ] **Step 1: Grep for any `font-size` below 36px in v6**

```bash
cd "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat/.worktrees/typography-redesign"
grep -nE 'font-size:\s*(1[0-9]|2[0-9]|3[0-5])px' \
  "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html"
```

Expected: empty, OR every match is in an approved exception location (verify against reflow-log.md Exceptions section).

If unexpected matches appear: investigate which slide they belong to, decide whether to fix (return to Task C-NN for that slide) or document as new exception.

- [ ] **Step 2: Grep for body/lead/h-class with sizes <53px**

```bash
grep -nE '\.t-(h[1-5]|body|body-dark|lead).*font-size:\s*([1-4][0-9]|5[0-2])px' \
  "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html"
```

Expected: empty. If any match: Phase 1 token replacement was incomplete. Fix and re-verify.

- [ ] **Step 3: Verify v5 unchanged**

```bash
md5sum "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html"
```
Expected: `fb0816fe4c4987e235fd06a31b5cd94a` (control sample untouched).

- [ ] **Step 4: Verify token-only diff vs master**

```bash
git diff master -- "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html"
```
Expected: empty (v5 is control sample, must not appear in branch diff).

- [ ] **Step 5: Compose V7 final summary in reflow-log**

Append a "Final Verification" section to reflow-log.md:

```markdown
## Final Verification (V3 / Task AJ)

- [x] V3 grep `font-size <36px`: [empty | all matches in approved exceptions]
- [x] V3 grep `.t-(h1..h5|body|body-dark|lead)` <53px: empty
- [x] V5 md5 unchanged: fb0816fe4c4987e235fd06a31b5cd94a
- [x] V5 not in branch diff: confirmed
- [x] All 32 slides reflowed: confirmed (Phase 2 table 32/32)
- [x] Final deck slide count: [N]
```

- [ ] **Step 6: Commit**

```bash
git add analysis/winston-audit/reflow-log.md
git commit -m "audit(reflow): final V3 verification — Winston typography compliant

All grep checks pass. v6 deck Winston-compliant: no body/lead/heading
font-size below 53px; all <36px appearances are documented exceptions
(table-aggregates per E1). v5 (1).html control sample unchanged.

Branch ready for merge to master.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Self-Review Checklist (Run after writing this plan)

**Spec coverage (V1-V6 from spec):**
- V1 Phase 1 token substitution → Task B ✓
- V2 Phase 2 per-slide → Tasks C-001 … C-032 ✓
- V3 Audit Crime #3 → Task AJ ✓
- V4 Total slide deck count → Task AI Step 4 ✓ (with out-of-scope flag for block-structure update)
- V5 Audit trail → Task A (skeleton), Tasks C-NN (rows), Task AI (finalize) ✓
- V6 Brainstorm itself → spec already approved before this plan ✓

**E-rule coverage:**
- E1 split unbounded → Task C-NN Step 4 ✓
- E2 no content modification → Task C-NN Step 4 (CONTENT-DRIFT flag) ✓
- E3 Slogan preservation → Task C-NN Step 5 mockup template ✓
- E4 only font-size/line-height → Task B Step 3 grep verification ✓
- E5 mid-loop changes → reflow-log Mid-Course Corrections section (Task A skeleton) ✓
- E6 broken-state intentional → header note + Task B Step 5 commit message ✓

**Placeholder scan:** No "TBD" / "TODO" / generic "implement later". The `[N]`, `[K]`, `[Slide title]`, `[port]` placeholders are PER-INSTANCE values filled by controller during execution — they're parametric, not unfilled.

**Type/path consistency:**
- `.superpowers/brainstorm/<session>/content/` path used consistently
- `reflow-log.md` location consistent
- `v6-winston.html` filename consistent everywhere

---

## Execution Notes

- **Tasks A, B, AI, AJ:** subagent-dispatchable (mechanical, no user gate).
- **Tasks C-001 … C-032:** controller + user only. Each task ends with "End turn. Wait for user response." This cannot be subagent-driven without losing the spec's core gate.
- **Estimated time:** Task A 10 min, Task B 15 min, Each C-NN 5-10 min, Task AI 15 min, Task AJ 10 min. Total: ≈ 3-6 hours user-interactive time.
- **Worktree cleanup:** after Task AJ approves, merge to master and remove worktree per `superpowers:finishing-a-development-branch`.
