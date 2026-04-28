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
