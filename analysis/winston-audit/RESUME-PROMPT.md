# Resume Autoprompt — Winston Typography Redesign

Copy-paste blok di bawah ke chat baru (working dir: `D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat`, model Opus 4.7 1M):

---

```
Resume Winston typography redesign untuk v6-winston.html. 11/32 slide v5 selesai.
Lanjut dari slide 12 v5.

# Workspace
- Worktree: .worktrees/typography-redesign (branch feature/typography-redesign)
- Latest commit: ed84a1a; deck v6 = 48 slides
- v5 control sample md5: fb0816fe4c4987e235fd06a31b5cd94a (jangan disentuh)

# Wajib Baca Dulu (urutan)
1. docs/superpowers/specs/2026-04-27-typography-redesign-design.md (Bagian 5 = E1-E6)
2. docs/superpowers/plans/2026-04-27-typography-redesign.md (Task C-NN template)
3. .worktrees/typography-redesign/analysis/winston-audit/reflow-log.md (state lengkap)

# Setup Visual Companion
"C:/Users/HP/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.7/skills/brainstorming/scripts/start-server.sh" --project-dir "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat"
URL + screen_dir di .superpowers/brainstorm/<newest>/state/server-info

# Token Balanced (Phase 1 sudah applied)
h1=110 h2=84 h3=68 h4=60 h5=53 lead=60 body=53 body-sm=36 caption=36 meta=28 label=28

# Aturan Sizing (per slide WAJIB ≤904px slack ≥30px)
- Frame avail: 904px (1080 - 80 top - 96 chrome)
- Header pill+h2+lead = 257-281
- 2-col/3-col cards: body 36 caption-tier (E1 exception)
- Multi-row table: body 36 caption-tier (E1 exception)
- Hanya font-size + line-height yang berubah; color/weight/letter-spacing tetap (E4)

# Pattern per Slide
A. grep posisi slide v5 di v6 sekarang (line range bergeser tiap split)
B. Baca crime-inventory entries: grep -E '^\| NN ' analysis/winston-audit/crime-inventory.md
C. Strategi: cut-first (1-3, 30-32), split-first (4-29), F5 wajib (kasus 19-29)
D. Build HD preview di screen_dir (full HTML, deck CSS, scale 0.5×)
E. User approve A/B/C
F. Apply Edit, update reflow-log row, commit "feat(deck): slide NN ..."

# Slogan Deployment
#1 ✓ slide 02 (italic 60 lead, border-left blue) | #2 ✓ slide 13
#3 pending ~v5-19 | #4 pending ~v5-30

# Out-of-Scope Flags (sudah di reflow-log)
- Chrome /32 cascade (opportunistic atau Task AI bulk)
- presentation-design-spec block structure update
- OB17 deferred ke Pengakuan & Pengukuran section

# Tasks Queue
21 slide tersisa (v5 12-32) → Task AI (finalize log) → Task AJ (V3 grep) → finishing-a-development-branch

# Lanjut
Slide 12 v5 = "SFAC 8 Bab 4 (Juli 2024): Definisi Baru".
grep -nE 'data-screen-label="12 SFAC' "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html"
Build HD preview, push, await user choice.
```

---

## Slide-by-slide Status

| v5 | Status | Strategy | v6 |
|----|--------|----------|----|
| 01 | ✓ 7c19bcf | cut-first | 01 |
| 02 | ✓ e2b2c4e | cut-first + Slogan #1 | 02 |
| 03 | ✓ 215ddd7 | split → 3 | 03/04/05 |
| 04 | ✓ 59646e0 | split → 3 (OB17 deferred) | 06/07/08 |
| 05 | ✓ 87964e0 | split → 2 | 09/10 |
| 06 | ✓ 9f3cc59 | split → 2 (Constraint+Understand dropped) | 11/12 |
| 07 | ✓ 33113bc | split → 2 + Slogan #2 (Cost Constraint dropped) | 13/14 |
| 08 | ✓ da1a0f0 | split → 2 + F5 EPS chart | 15/16 |
| 09 | ✓ 2141647 | split → 3 | 17/18/19 |
| 10 | ✓ ca66b4e | split → 3 | 20/21/22 |
| 11 | ✓ ed84a1a | split → 3 (definitions condensed) | 23/24/25 |
| 12 | **NEXT** | likely split-first per audit | TBD |

## Mid-Course Corrections (logged)
- Slide 03: Hybrid override cut→split (E5)
- Slide 04: OB17 deferred to later section

## Notes
- Spec rule E1 wajib: split tanpa batas atas; tabel agregat 36px caption + flag
- Spec rule E2 wajib: tidak modifikasi konten substansi (out of scope)
- v6 sengaja "broken" sampai semua slide reflowed (E6) — jangan rollback
