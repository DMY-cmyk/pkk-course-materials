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
| 11 | (pending) | — | — | — | — |
| 12 | (pending) | — | — | — | — |
| 13 | (pending) | — | — | — | — |
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

(pending — populated as exceptions are flagged during Phase 2)

## Mid-Course Corrections

- **Slide 03 (2026-04-27T09:05):** User-approved override Hybrid policy (cut-first → split-first) for slide 03 only. Reason: 3 distinct content elements (timeline, cards, SFAC table) with substantive value; cut-first would drop SFAC table entirely (potential E1 conflict). Result: slide 03 → 03 + 04 + 05. Deck count grows by 2. Subsequent slide chrome page-numbers will require cascade update — flagged in Out-of-Scope.
- **Slide 04 (2026-04-27T09:30):** Split per audit T6 + Hybrid policy. v5 slide 04 → v6 slides 06 + 07 + 08. **OB17 (Basis Akrual) deferred:** the OB17 sub-callout in v5 slide 04 was content-cut (would not fit in slide 06 with Winston-compliant sizing); reintegrate at Pengakuan & Pengukuran section (target slide v5-14 to v5-17, v6 numbering TBD).

## Out-of-Scope Flags

- **Chrome page-number cascade after slide 03 split (2026-04-27T09:05):** Original slides 04-32 chrome still display "/32" with their old slide numbers (04/32, 05/32, dst.). Slide 03 split adds 2 slides; chrome should cascade to "/34" with appropriate renumbering. Two options for handling: (a) update each downstream slide's chrome opportunistically as we reflow it (mid-stream catch-up); (b) defer to Task AI bulk update after all slides reflowed. Decision deferred — current state is acceptable transitional inconsistency per E6 (v6 is broken until Phase 2 completes).
- **`presentation-design-spec.md` block structure update (pre-flagged from spec V4):** Block boundaries (Opening 1-3, Proof 4-29, Close 30-32) no longer match post-split deck count. Defer to separate brainstorming session.
