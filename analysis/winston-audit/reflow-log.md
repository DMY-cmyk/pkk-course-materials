# Typography Reflow Log — v6-winston.html

**Spec:** `docs/superpowers/specs/2026-04-27-typography-redesign-design.md`
**Tokens:** `specs/typography-tokens.md`
**v5 baseline (control sample):** md5 `fb0816fe4c4987e235fd06a31b5cd94a`

## Phase 1 — Token Substitution

- **Commit SHA:** 5b15a6090f94678167ad506769529e9ffdfeea48
- **Timestamp:** 2026-04-27T08:45
- **Tokens replaced:** 12 (per `specs/typography-tokens.md`)

## Phase 2 — Per-Slide Reflow

| Slide | Strategy | Splits | Exception | Approved | Commit |
|-------|----------|--------|-----------|----------|--------|
| 01 | cut-first | — | — | 2026-04-27T08:50 | (see git log slide-01) |
| 02 | cut-first | — | E1 (table 36px caption-tier) | 2026-04-27T08:55 | (see git log slide-02) |
| 03 | split-first (override Hybrid) | 3 (03/04/05) | E1 SFAC table 36px caption-tier | 2026-04-27T09:05 | (see git log slide-03-split) |
| 04 | split-first | 3 (06/07/08) | E1 evolution table 36px caption-tier; OB17 deferred | 2026-04-27T09:30 | (see git log slide-04-split) |
| 05 | split-first | 2 (09/10) | E1 subsidiary cards 42px sub-Winston for 4-col grid | 2026-04-27T09:50 | (see git log slide-05-split) |
| 06 | split-first | 2 (11/12) | E1 components+ancillary boxes 28-36px label/caption-tier; Constraints+Understandability dropped (verbal mention) | 2026-04-27T10:10 | (see git log slide-06-split) |
| 07 | split-first | 2 (13/14) | E1 components+cards 28-36px caption-tier; Cost Constraint dropped (verbal) | 2026-04-27T10:30 | (see git log slide-07-split) |
| 08 | split-first | 2 (15/16) | E1 3-col cards body 36px caption-tier; F5 active (slide kasus INDF) | 2026-04-27T10:50 | (see git log slide-08-split) |
| 09 | split-first | 3 (17/18/19) | E1 3-col components 36px caption-tier; description body 36px in slides 17/18 | 2026-04-27T11:10 | (see git log slide-09-split) |
| 10 | split-first | 3 (20/21/22) | E1 2-col cards body 36px caption-tier; h4-tier 48px on card titles | 2026-04-27T11:30 | (see git log slide-10-split) |
| 11 | split-first | 3 (23/24/25) | E1 table body 36px caption-tier; SFAC definitions condensed from v5 (formal-faithful) | 2026-04-27T11:50 | (see git log slide-11-split) |
| 12 | split-first | 3 (12/13/14) | E1 asset table 36px caption-tier (Primasi row dropped — covered by BC4.7 on slide 13); E1 goodwill table 36px caption-tier; E1 BC4.7 body 36px caption-tier (2-line content, tightened); E1 INDF resolution callout 36px caption-tier; E1 liability sub-note 36px caption-tier; F5 active (INDF goodwill case Rp52,2T); slack ≥159px (13) and ≥180px (14) post-tightening | 2026-04-27T19:55 | (see git log slide-12-split + tightening follow-up) |
| 13 | split-first | 3 (15/16/17) | E1 sub-card body 36px caption-tier (slides 15/16); OCI explainer dropped (redundant with pill labels); lead phrases compressed for 1-line headers; F5 active (INDF CI Waterfall Rp13,08T NI / Rp531,4M OCI / Rp12,55T CI) | 2026-04-27T20:30 | (see git log slide-13-split + slide-17-token-align) |
| 14 | (pending) | — | — | — | — |
| 15 | (pending) | — | — | — | — |
| 16 | (pending) | — | — | — | — |
| 17 | (pending) | — | — | — | — |
| 18 | (pending) | — | — | — | — |
| 19 | (pending) | — | — | — | — |
| 20 | (pending) | — | — | — | — |
| 21 | (pending) | — | — | — | — |
| 22 | (pending) | — | — | — | — |
| 23 | (pending) | — | — | — | — |
| 24 | (pending) | — | — | — | — |
| 25 | (pending) | — | — | — | — |
| 26 | (pending) | — | — | — | — |
| 27 | (pending) | — | — | — | — |
| 28 | (pending) | — | — | — | — |
| 29 | (pending) | — | — | — | — |
| 30 | (pending) | — | — | — | — |
| 31 | (pending) | — | — | — | — |
| 32 | (pending) | — | — | — | — |

## Exceptions

- **Slide 12 (Aset table):** E1 caption-tier 36px on table body cells (3-col aspect/old/new comparison). Primasi row dropped — moved to BC4.7 callout on slide 13.
- **Slide 13 (Liabilitas + BC4.7):** E1 caption-tier 36px on liability sub-note (`(1) present obligation; (2) transfer economic benefit — "Probable" & "past transaction" DIHAPUS.`). E1 caption-tier 36px on BC4.7 body. Quote line-height tightened 1.25 → 1.18; card padding tightened 32px 44px → 24px 36px; trailing "Memperkuat balance sheet approach." sentence dropped (BC4.7 primacy is the load-bearing claim — substance preserved). Final slack ~159px.
- **Slide 14 (INDF Goodwill F5):** E1 caption-tier 36px on goodwill comparison table body (4-col karakteristik/old/new/status). E1 caption-tier 36px on resolution callout body. Table row padding 14px → 11px; row line-height 1.3 → 1.25. Callout padding 24×36 → 18×30; callout line-height 1.3 → 1.2; callout text condensed (`berdasarkan KEDUA definisi` → `di KEDUA versi`; final clause restructured to em-dash form). Final slack ~180px.
- **Slide 15 (Pendapatan vs Keuntungan, SFAC 6):** E1 caption-tier 36px (`.t-body-sm`) on both sub-card definitions ("Operasi UTAMA/SENTRAL — berulang, prediktabel.") and INDF examples ("Penjualan bersih Rp115,79T..."). Lead phrase compressed: `Operasi sentral berulang vs. transaksi periferal — aplikasi INDF 2024` → `Operasi sentral vs. transaksi periferal — INDF 2024` (2-line target, comfortable). Definitions verbatim from v5 / SFAC 6 elements. Slack ~186px.
- **Slide 16 (Beban vs Kerugian, SFAC 6):** E1 caption-tier 36px on both sub-card definitions and INDF examples. Lead compressed: `Biaya operasi utama vs. penurunan dari transaksi periferal` → `Biaya operasi utama vs. penurunan periferal — INDF 2024`. Definitions verbatim from v5. Slack ~186px.
- **Slide 17 (CI Waterfall + OCI INDF F5):** F5 active. Waterfall amounts aligned to `.t-h5` 53px / line-height 1.20 (system token); meta labels at `.t-meta` 28px. Amber "Mengapa OCI negatif?" callout aligned to `.t-body-sm` 36px / line-height 1.30 (V3 floor compliance — no body <36px). OCI definition in card.blue header was DROPPED (redundant with the per-pill meta labels which already name "Selisih kurs translasi" etc.). Lead compressed: `Rp13,08T NI + (Rp531,4M) OCI = Rp12,55T CI` → `Waterfall: NI → OCI → CI` (1-line; specific amounts already prominent in waterfall pills). Amber body shortened: `INDF punya operasi luar negeri besar (Pinehill di Afrika, Timur Tengah, Asia Tenggara) — depresiasi mata uang asing terhadap Rupiah menghasilkan kerugian translasi. Implikasi: Laba Rp13,08T tidak mencerminkan total perubahan kekayaan sepenuhnya.` → `Operasi luar negeri INDF (Pinehill: Afrika, Timur Tengah, Asia Tenggara) — depresiasi mata uang asing menghasilkan kerugian translasi. Implikasi: Laba Rp13,08T tidak mencerminkan total perubahan kekayaan.` Card padding tightened (24→20 vertical; pills 15→10 vertical). All F5 INDF amounts verbatim (Rp115,79T elsewhere; Rp13.077,5M; Rp531,4M; Rp12.546,1M; Rp13,08T). Slack ~107px after token-alignment follow-up (was ~146px before; 48→53 amounts and 32→36 callout consume ~39px). No exceptions remain — slide is fully token-compliant.

## Mid-Course Corrections

- **Slide 03 (2026-04-27T09:05):** User-approved override Hybrid policy (cut-first → split-first) for slide 03 only. Reason: 3 distinct content elements (timeline, cards, SFAC table) with substantive value; cut-first would drop SFAC table entirely (potential E1 conflict). Result: slide 03 → 03 + 04 + 05. Deck count grows by 2. Subsequent slide chrome page-numbers will require cascade update — flagged in Out-of-Scope.
- **Slide 04 (2026-04-27T09:30):** Split per audit T6 + Hybrid policy. v5 slide 04 → v6 slides 06 + 07 + 08. **OB17 (Basis Akrual) deferred:** the OB17 sub-callout in v5 slide 04 was content-cut (would not fit in slide 06 with Winston-compliant sizing); reintegrate at Pengakuan & Pengukuran section (target slide v5-14 to v5-17, v6 numbering TBD).

## Out-of-Scope Flags

- **Chrome page-number cascade after slide 03 split (2026-04-27T09:05):** Original slides 04-32 chrome still display "/32" with their old slide numbers (04/32, 05/32, dst.). Slide 03 split adds 2 slides; chrome should cascade to "/34" with appropriate renumbering. Two options for handling: (a) update each downstream slide's chrome opportunistically as we reflow it (mid-stream catch-up); (b) defer to Task AI bulk update after all slides reflowed. Decision deferred — current state is acceptable transitional inconsistency per E6 (v6 is broken until Phase 2 completes).
- **`presentation-design-spec.md` block structure update (pre-flagged from spec V4):** Block boundaries (Opening 1-3, Proof 4-29, Close 30-32) no longer match post-split deck count. Defer to separate brainstorming session.
