# RMK Ch. 13 "Statement of Cash Flows" — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce `output/RMK Chap. 13_Kelompok 2_PKK.docx` — a complete, graduate-level Indonesian RMK of Wolk Ch. 13 with all 11 exhibits + 2 equations embedded, satisfying the six hard gates (A4, 1.5 spacing, Calibri 12, ≥8 pages, .docx, 6-member identity).

**Architecture:** Markdown sections (`content/sections/`) + figure manifest (`content/figures/manifest.yaml`) are the single source of truth. `rmk-extract-figures` (Rust) crops exhibits 13.4–13.11 from the PDF; `rmk-build` (Rust) parses sections into a block-list JSON consumed by the python-docx bridge (`tools/build_docx.py`); `rmk-audit` enforces concept/keyword/exhibit coverage as `cargo test`; `rmk-validate` + `tools/validate_docx.py` enforce the format gates and emit `VALIDATION-REPORT.md`.

**Tech Stack:** Rust (serde/serde_yaml/serde_json/image/clap), poppler `pdftoppm`, Python 3.12 + python-docx (bridge), optional Word COM for page count.

**Key references for every executor:**
- Chapter text: `analysis/chapter13-raw.txt` (line refs below) — the ONLY content source.
- Concepts: `analysis/chapter13-concept-inventory.md` (C-01…C-62 with PDF page refs).
- Exhibit locations: `analysis/exhibit-map.md`.
- Style contract: `specs/rmk-spec.md` (§3 voice: Indonesian, professor-led, S2 — explain → interpret → connect; English technical terms italicized on first use; NO fabricated numbers; every number traceable to the chapter).
- All paths below are relative to `pkk-rmk-cash-flows-kelompok2/` (the workspace root inside the worktree). Run all commands from there.

**Conventions:**
- Section markdown: YAML front matter between `---` fences, then body.
- Exhibit placement directive: a line containing only `{{exhibit:<id>}}` — rmk-build replaces it with the image+caption / native table+caption / equation per the manifest.
- Cover centering directive: a line `{{center:<text>}}` → centered paragraph (bold if text wrapped in `**`).
- Inline markdown in body: `**bold**`, `*italic*`; pipe tables become Word tables.
- Commit after every task; `cargo test && cargo clippy --all-targets -- -D warnings && cargo fmt --check` must pass at every commit.

---

## Task 1: Figure manifest + re-set exhibit content (data)

**Files:**
- Create: `content/figures/manifest.yaml`
- Create: `content/figures/tables/exhibit-13-01.md`, `exhibit-13-02.md`, `exhibit-13-03.md`
- Modify: `crates/shared/src/lib.rs` (add `reset_text`/`reset_table` + `required_keywords`)

- [ ] **Step 1: Extend shared types.** In `crates/shared/src/lib.rs`, add to `struct Exhibit` (after `anchor_section`):

```rust
    /// For RenderType::ResetEquation: the literal equation text.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub reset_text: Option<String>,
    /// For RenderType::ResetTable: path (workspace-relative) to the markdown table.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub reset_table: Option<String>,
    /// Display label for equations, e.g. "(13.1)".
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub label: Option<String>,
```

And add to `struct Rubric` (after `depth_check`):

```rust
    /// Literal substrings (case-insensitive) that MUST appear in the section body.
    #[serde(default)]
    pub required_keywords: Vec<String>,
```

- [ ] **Step 2: Write `content/figures/manifest.yaml`** (crop boxes from `analysis/exhibit-map.md`; `box_pct` = [left, top, right, bottom] page fractions; whitespace-trim tightens them; visual verification in Task 3 adjusts):

```yaml
- id: eq-13-1
  caption: ""
  render_type: reset-equation
  target_width_in: 6.25
  anchor_section: 01-scfp-funds-flow
  reset_text: "transaction credits = transaction debits"
  label: "(13.1)"
- id: exhibit-13-01
  caption: "Exhibit 13.1 — Standard Format of the Statement of Changes in Financial Position (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: reset-table
  target_width_in: 6.25
  anchor_section: 01-scfp-funds-flow
  reset_table: content/figures/tables/exhibit-13-01.md
- id: exhibit-13-02
  caption: "Exhibit 13.2 — Illustration of the SCF in Accordance With SFAS No. 95 (Direct Method), Company M, FY 2000 (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: reset-table
  target_width_in: 6.25
  anchor_section: 05-direct-vs-indirect
  reset_table: content/figures/tables/exhibit-13-02.md
- id: exhibit-13-03
  caption: "Exhibit 13.3 — Indirect or Reconciliation Method of Presenting Net Cash Flows From Operating Activities (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: reset-table
  target_width_in: 6.25
  anchor_section: 05-direct-vs-indirect
  reset_table: content/figures/tables/exhibit-13-03.md
- id: exhibit-13-04
  caption: "Exhibit 13.4 — Comparison of Balance Sheet Changes and Working Capital Adjustments for 3M Company ($000,000) (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: crop
  segments: [{ page: 10, box_pct: [0.04, 0.285, 0.96, 0.465] }]
  target_width_in: 6.25
  anchor_section: 06-nonarticulation
- id: exhibit-13-05
  caption: "Exhibit 13.5 — Premium Allocation Between Operating and Financing Cash Flows (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: crop
  segments: [{ page: 13, box_pct: [0.04, 0.055, 0.96, 0.45] }]
  target_width_in: 6.25
  anchor_section: 07-classification-problems
- id: exhibit-13-06
  caption: "Exhibit 13.6 — Selected Items From WorldCom's Statement of Cash Flows ($000,000) (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: crop
  segments: [{ page: 16, box_pct: [0.04, 0.055, 0.96, 0.25] }]
  target_width_in: 6.25
  anchor_section: 10-scf-more-than-cfo
- id: eq-13-2
  caption: ""
  render_type: reset-equation
  target_width_in: 6.25
  anchor_section: 12-free-cash-flow
  reset_text: "FCF = NOPLAT − investment in operating invested capital"
  label: "(13.2)"
- id: exhibit-13-07
  caption: "Exhibit 13.7 — Income Statement and Balance Sheet for ABC Company (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: crop
  segments: [{ page: 18, box_pct: [0.04, 0.09, 0.96, 0.575] }]
  target_width_in: 6.25
  anchor_section: 12-free-cash-flow
- id: exhibit-13-08
  caption: "Exhibit 13.8 — Statement of Cash Flows for ABC Company (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: crop
  segments: [{ page: 19, box_pct: [0.04, 0.06, 0.96, 0.505] }]
  target_width_in: 6.25
  anchor_section: 12-free-cash-flow
- id: exhibit-13-09
  caption: "Exhibit 13.9 — Statement of Free Cash Flows for ABC Company (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: crop
  segments: [{ page: 20, box_pct: [0.04, 0.05, 0.96, 0.715] }]
  target_width_in: 6.25
  anchor_section: 12-free-cash-flow
- id: exhibit-13-10
  caption: "Exhibit 13.10 — Computing Free Cash Flow From the SCF for ABC Company (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: crop
  segments: [{ page: 20, box_pct: [0.04, 0.737, 0.96, 0.90] }]
  target_width_in: 6.25
  anchor_section: 12-free-cash-flow
- id: exhibit-13-11
  caption: "Exhibit 13.11 — A Comparison of Performance Measures for ABC Company (Wolk, Dodd & Rozycki, 2017, Ch. 13)"
  render_type: crop
  segments: [{ page: 21, box_pct: [0.04, 0.095, 0.96, 0.26] }]
  target_width_in: 6.25
  anchor_section: 12-free-cash-flow
```

- [ ] **Step 3: Write the three re-set tables** (reconstructed from `analysis/chapter13-raw.txt`; arithmetic verified: Exhibit 13.2 operating 13,850−12,000+20+55−220−325+15−30 = 1,365; investing 600+150−1,000−925 = −1,175; financing 300−125+400+500−200 = 875; 13.3 adjustments sum to 605, 760+605 = 1,365 = direct-method CFO).

`content/figures/tables/exhibit-13-01.md`:

```markdown
| **Sources of Resources (transaction credits)** |
| 1. Increases to the "fund balance" accounts |
| &nbsp;&nbsp;&nbsp;a. From net income |
| &nbsp;&nbsp;&nbsp;b. From other sources |
| 2. Other sources of resources |
| 3. Decrease, if any, in the fund balance for the period |
| **Uses of Resources (transaction debits)** |
| 1. Decreases to the "fund balance" accounts |
| &nbsp;&nbsp;&nbsp;a. From net losses |
| &nbsp;&nbsp;&nbsp;b. From other sources |
| 2. Other uses of resources |
| 3. Increase, if any, in the fund balance for the period |
```

`content/figures/tables/exhibit-13-02.md`:

```markdown
| **COMPANY M — Consolidated Statement of Cash Flows, For the Year Ended December 31, 2000** | |
| *Increase (Decrease) in Cash and Cash Equivalents* | |
| **Cash flows from operating activities** | |
| Cash received from customers | $13,850 |
| Cash paid to suppliers and employees | (12,000) |
| Dividend received from affiliate | 20 |
| Interest received | 55 |
| Interest paid (net of amount capitalized) | (220) |
| Income taxes paid | (325) |
| Insurance proceeds received | 15 |
| Cash paid to settle lawsuit for patent infringement | (30) |
| **Net cash provided by operating activities** | **$1,365** |
| **Cash flows from investing activities** | |
| Proceeds from sale of facility | $600 |
| Payment received on note for sale of plant | 150 |
| Capital expenditures | (1,000) |
| Payment for purchase of Company S, net of cash acquired | (925) |
| **Net cash used in investing activities** | **$(1,175)** |
| **Cash flows from financing activities** | |
| Net borrowings under line-of-credit agreement | $300 |
| Principal payments under capital lease obligation | (125) |
| Proceeds from issuance of long-term debt | 400 |
| Proceeds from issuance of common stock | 500 |
| Dividends paid | (200) |
| **Net cash provided by financing activities** | **$875** |
| **Net increase in cash and cash equivalents** | **$1,065** |
| Cash and cash equivalents at beginning of year | 600 |
| **Cash and cash equivalents at end of year** | **$1,665** |
```

NOTE for reviewer: the PDF text layer shows "Proceeds from sale of facility $6,001" — that is a footnote-marker artifact; $600 is required by the exhibit's own arithmetic (600+150−1,000−925 = −1,175 as printed). Verify against the 240-dpi render of PDF p. 8 in Stage 1 review and record the verification in the review file.

`content/figures/tables/exhibit-13-03.md`:

```markdown
| **Reconciliation of net income to net cash provided by operating activities** | | |
| Net income | | $760 |
| *Adjustments to reconcile net income to net cash provided by operating activities:* | | |
| Depreciation and amortization | $445 | |
| Provision for losses on accounts receivable | 200 | |
| Gain on sale of facility | (80) | |
| Undistributed earnings of affiliate | (25) | |
| Payment received on installment note receivable for sale of inventory | 100 | |
| *Change in assets and liabilities net of effects from purchase of Company S:* | | |
| Increase in accounts receivable | (215) | |
| Decrease in inventory | 205 | |
| Increase in prepaid expenses | (25) | |
| Decrease in accounts payable and accrued expenses | (250) | |
| Increase in interest and income taxes payable | 50 | |
| Increase in deferred taxes | 150 | |
| Increase in other liabilities | 50 | |
| **Total adjustments** | | **$605** |
| **Net cash provided by operating activities** | | **$1,365** |
| **Supplemental schedule of noncash investing and financing activities — purchase of Company S:** | | |
| Fair value of assets acquired | | $1,580 |
| Cash paid for the capital stock | | (950) |
| **Liabilities assumed** | | **$630** |
```

- [ ] **Step 4: Verify build + tests still green.** Run: `cargo test -p shared && cargo clippy --all-targets -- -D warnings && cargo fmt --check` → all pass (serde `default` keeps the round-trip test green).

- [ ] **Step 5: Commit.** `git add -A . && git commit -m "feat(rmk-ch13): figure manifest + re-set exhibit tables 13.1-13.3 (verified arithmetic)"`

---

## Task 2: Implement rmk-extract-figures (TDD)

**Files:**
- Modify: `crates/rmk-extract-figures/src/main.rs` (full rewrite)
- Create: `crates/rmk-extract-figures/src/lib.rs`

- [ ] **Step 1: Write failing unit tests.** Create `crates/rmk-extract-figures/src/lib.rs`:

```rust
//! Crop/trim/stack primitives for exhibit extraction.

use image::{Rgb, RgbImage};

const WHITE_THRESHOLD: u8 = 245;
const PAD_PX: u32 = 8;

/// Crop by [left, top, right, bottom] page fractions.
pub fn crop_pct(img: &RgbImage, box_pct: [f64; 4]) -> RgbImage {
    let (w, h) = img.dimensions();
    let x0 = (w as f64 * box_pct[0]) as u32;
    let y0 = (h as f64 * box_pct[1]) as u32;
    let x1 = ((w as f64 * box_pct[2]) as u32).min(w);
    let y1 = ((h as f64 * box_pct[3]) as u32).min(h);
    image::imageops::crop_imm(img, x0, y0, x1 - x0, y1 - y0).to_image()
}

/// Trim surrounding near-white border, keeping PAD_PX padding.
pub fn trim_white(img: &RgbImage) -> RgbImage {
    let (w, h) = img.dimensions();
    let is_ink = |p: &Rgb<u8>| p.0.iter().any(|&c| c < WHITE_THRESHOLD);
    let (mut x0, mut y0, mut x1, mut y1) = (w, h, 0u32, 0u32);
    for (x, y, p) in img.enumerate_pixels() {
        if is_ink(p) {
            x0 = x0.min(x);
            y0 = y0.min(y);
            x1 = x1.max(x);
            y1 = y1.max(y);
        }
    }
    if x0 > x1 {
        return img.clone(); // fully white: nothing to trim
    }
    let x0 = x0.saturating_sub(PAD_PX);
    let y0 = y0.saturating_sub(PAD_PX);
    let x1 = (x1 + PAD_PX + 1).min(w);
    let y1 = (y1 + PAD_PX + 1).min(h);
    image::imageops::crop_imm(img, x0, y0, x1 - x0, y1 - y0).to_image()
}

/// Stack images vertically, centered on white, width = widest part.
pub fn stack(parts: &[RgbImage]) -> RgbImage {
    let w = parts.iter().map(|p| p.width()).max().unwrap_or(1);
    let h: u32 = parts.iter().map(|p| p.height()).sum();
    let mut out = RgbImage::from_pixel(w, h.max(1), Rgb([255, 255, 255]));
    let mut y = 0i64;
    for p in parts {
        image::imageops::overlay(&mut out, p, ((w - p.width()) / 2) as i64, y);
        y += p.height() as i64;
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    fn white(w: u32, h: u32) -> RgbImage {
        RgbImage::from_pixel(w, h, Rgb([255, 255, 255]))
    }

    #[test]
    fn crop_pct_halves() {
        let img = white(100, 200);
        let c = crop_pct(&img, [0.25, 0.10, 0.75, 0.60]);
        assert_eq!(c.dimensions(), (50, 100));
    }

    #[test]
    fn trim_white_finds_ink_bbox() {
        let mut img = white(100, 100);
        img.put_pixel(40, 50, Rgb([0, 0, 0]));
        img.put_pixel(60, 55, Rgb([0, 0, 0]));
        let t = trim_white(&img);
        // ink bbox 21x6 plus 8px pad each side
        assert_eq!(t.dimensions(), (21 + 16, 6 + 16));
    }

    #[test]
    fn trim_all_white_is_identity() {
        let img = white(30, 30);
        assert_eq!(trim_white(&img).dimensions(), (30, 30));
    }

    #[test]
    fn stack_centers_and_sums_heights() {
        let s = stack(&[white(40, 10), white(60, 20)]);
        assert_eq!(s.dimensions(), (60, 30));
    }
}
```

- [ ] **Step 2: Run tests — they fail to compile (no lib target wired).** Run: `cargo test -p rmk-extract-figures` → compile error or 0 tests. Fix by ensuring `src/lib.rs` exists (cargo auto-detects).

- [ ] **Step 3: Rewrite `crates/rmk-extract-figures/src/main.rs`:**

```rust
//! Rasterize, crop, trim, and stack chapter exhibits per the figure manifest.

use anyhow::{Context, Result};
use clap::Parser;
use rmk_extract_figures::{crop_pct, stack, trim_white};
use shared::{Exhibit, RenderType};
use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;

/// Extract and crop chapter exhibits from the source PDF.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    #[arg(
        long,
        default_value = "sources/textbook-chapter/Sage_Chapter_13_Kelompok_2.pdf"
    )]
    pdf: String,
    #[arg(long, default_value = "content/figures")]
    out: String,
    #[arg(long, default_value = "content/figures/manifest.yaml")]
    manifest: String,
    #[arg(long, default_value_t = 240)]
    dpi: u32,
}

fn render_page(pdf: &str, page: u32, dpi: u32, tmp: &Path) -> Result<PathBuf> {
    let prefix = tmp.join(format!("p{page}"));
    let status = Command::new("pdftoppm")
        .args(["-png", "-r", &dpi.to_string()])
        .args(["-f", &page.to_string(), "-l", &page.to_string()])
        .arg(pdf)
        .arg(&prefix)
        .status()
        .context("running pdftoppm")?;
    anyhow::ensure!(status.success(), "pdftoppm failed for page {page}");
    let stem = format!("p{page}-");
    let png = fs::read_dir(tmp)?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .find(|p| {
            p.file_name()
                .and_then(|n| n.to_str())
                .is_some_and(|n| n.starts_with(&stem) && n.ends_with(".png"))
        })
        .with_context(|| format!("no pdftoppm output for page {page}"))?;
    Ok(png)
}

fn main() -> Result<()> {
    let args = Args::parse();
    let manifest: Vec<Exhibit> = serde_yaml::from_str(
        &fs::read_to_string(&args.manifest).context("reading manifest")?,
    )?;
    let out_dir = Path::new(&args.out);
    fs::create_dir_all(out_dir)?;
    let tmp = out_dir.join("_pages");
    fs::create_dir_all(&tmp)?;
    let mut extracted = 0u32;
    for ex in manifest.iter().filter(|e| e.render_type == RenderType::Crop) {
        anyhow::ensure!(!ex.segments.is_empty(), "{}: crop without segments", ex.id);
        let mut parts = Vec::new();
        for seg in &ex.segments {
            let page_png = render_page(&args.pdf, seg.page, args.dpi, &tmp)?;
            let img = image::open(&page_png)
                .with_context(|| format!("opening {}", page_png.display()))?
                .to_rgb8();
            parts.push(trim_white(&crop_pct(&img, seg.box_pct)));
        }
        let combined = stack(&parts);
        let dest = out_dir.join(format!("{}.png", ex.id));
        combined.save(&dest)?;
        println!(
            "{} -> {} ({}x{})",
            ex.id,
            dest.display(),
            combined.width(),
            combined.height()
        );
        extracted += 1;
    }
    fs::remove_dir_all(&tmp).ok();
    println!("extracted {extracted} crop exhibits");
    Ok(())
}
```

Add to `crates/rmk-extract-figures/Cargo.toml` under `[dependencies]` (no change needed — `image`, `shared`, `serde_yaml`, `anyhow`, `clap` already declared). Crate name with dash imports as `rmk_extract_figures`.

- [ ] **Step 4: Run tests.** `cargo test -p rmk-extract-figures` → 4 passed. `cargo clippy --all-targets -- -D warnings && cargo fmt --check` → clean.

- [ ] **Step 5: Commit.** `git commit -am "feat(rmk-ch13): implement rmk-extract-figures (crop/trim/stack, TDD)"`

---

## Task 3: Phase 3.5 — run extraction + visual verification loop

**Files:**
- Create: `content/figures/exhibit-13-{04..11}.png` (8 files)
- Possibly modify: `content/figures/manifest.yaml` (crop-box adjustments)

- [ ] **Step 1: Run.** `cargo run -p rmk-extract-figures` → prints 8 lines + "extracted 8 crop exhibits".
- [ ] **Step 2: Visual verification (MANDATORY).** Read each `content/figures/exhibit-13-NN.png` with the Read tool. Per the spec checklist, each crop must be: legible at 6.25″, undistorted, fully bounded (no clipped rows/columns), free of neighboring body text, and free of the printed exhibit-title line (captions come from the manifest). The in-image source notes ("Source: 3M Company 10-K…", "Source: Mergent Online…", "Source: Based on Vent, Cowling, and Sevalstad (1995)") are PART of the exhibits — keep them.
- [ ] **Step 3: Adjust + re-run until clean.** Edit `box_pct` values in the manifest for any defective crop, re-run Step 1, re-read. Repeat until all 8 pass.
- [ ] **Step 4: Commit.** `git add -A . && git commit -m "feat(rmk-ch13): Phase 3.5 - extract and verify exhibit crops 13.4-13.11"` (PNGs are gitignored by the parent repo's `*.png` rule — force-add them: `git add -f content/figures/*.png` before committing.)

---

## Task 4: Shared content fragments

**Files:**
- Create: `content/_shared/activity-classification.md`, `content/_shared/indirect-method-logic.md`

These are reference texts for section authors (NOT assembled into the docx; rmk-build reads only `content/00-cover.md` + `content/sections/`). They guarantee DRY, consistent definitions across §4, §5, §6, §7, §9.

- [ ] **Step 1: Write `content/_shared/activity-classification.md`:** canonical Indonesian definitions (3 short paragraphs) of aktivitas operasi / investasi / pendanaan exactly as the chapter frames them (SCF trichotomy, p. 7 of `analysis/chapter13-raw.txt` lines 311–334), including: cash = kas + *cash equivalents*; *all-inclusive/all-resources* (transaksi nonkas dilaporkan sebagai suplemen); interest/dividen diterima dan interest dibayar masuk operasi menurut SFAS 95 (catat dissent 3-dari-7).
- [ ] **Step 2: Write `content/_shared/indirect-method-logic.md`:** canonical Indonesian explanation (2 short paragraphs) of the accrual→cash adjustment logic: mulai laba bersih; tambah beban nonkas (depresiasi); keluarkan keuntungan/kerugian nonoperasi; sesuaikan perubahan modal kerja (kenaikan piutang = pengurang, penurunan persediaan = penambah, dst.) per lines 396–451.
- [ ] **Step 3: Commit.** `git commit -am "feat(rmk-ch13): shared content fragments (DRY definitions)"`

---

## Task 5: Implement rmk-audit (coverage test harness, TDD)

**Files:**
- Create: `crates/rmk-audit/src/lib.rs`
- Modify: `crates/rmk-audit/src/main.rs`
- Create: `crates/rmk-audit/tests/coverage.rs`

- [ ] **Step 1: Write `crates/rmk-audit/src/lib.rs`:**

```rust
//! Front-matter parsing + coverage checks shared by tests and the CLI.

use anyhow::{Context, Result};
use serde::de::DeserializeOwned;
use std::path::{Path, PathBuf};

/// Workspace root (= pkk-rmk-cash-flows-kelompok2/), resolved from this crate.
pub fn workspace_root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("../..")
        .canonicalize()
        .expect("workspace root")
}

/// Split a markdown file into (front-matter YAML, body).
pub fn split_front_matter(text: &str) -> Result<(&str, &str)> {
    let rest = text
        .strip_prefix("---")
        .context("missing front-matter opening '---'")?;
    let end = rest
        .find("\n---")
        .context("missing front-matter closing '---'")?;
    let yaml = &rest[..end];
    let body = rest[end + 4..].trim_start_matches(['\r', '\n']);
    Ok((yaml, body))
}

/// Parse a markdown file's front matter into T, returning (T, body).
pub fn parse_doc<T: DeserializeOwned>(path: &Path) -> Result<(T, String)> {
    let text = std::fs::read_to_string(path)
        .with_context(|| format!("reading {}", path.display()))?;
    let (yaml, body) = split_front_matter(&text)?;
    let meta: T =
        serde_yaml::from_str(yaml).with_context(|| format!("front matter of {}", path.display()))?;
    Ok((meta, body.to_string()))
}

/// The canonical 62 concept ids C-01..C-62.
pub fn concept_ids() -> Vec<String> {
    (1..=62).map(|i| format!("C-{i:02}")).collect()
}

/// Case-insensitive containment check.
pub fn contains_ci(haystack: &str, needle: &str) -> bool {
    haystack.to_lowercase().contains(&needle.to_lowercase())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn split_front_matter_works() {
        let doc = "---\nid: x\n---\nBody here";
        let (yaml, body) = split_front_matter(doc).unwrap();
        assert_eq!(yaml.trim(), "id: x");
        assert_eq!(body, "Body here");
    }

    #[test]
    fn sixty_two_concepts() {
        let ids = concept_ids();
        assert_eq!(ids.len(), 62);
        assert_eq!(ids[0], "C-01");
        assert_eq!(ids[61], "C-62");
    }

    #[test]
    fn contains_ci_is_case_insensitive() {
        assert!(contains_ci("Survei McEnroe menemukan", "mcenroe"));
        assert!(!contains_ci("abc", "xyz"));
    }
}
```

- [ ] **Step 2: Run.** `cargo test -p rmk-audit` → 3 passed.

- [ ] **Step 3: Write `crates/rmk-audit/tests/coverage.rs`** (incremental: validates every rubric/section pair that EXISTS, so it stays green from the first section onward; `strict_completeness` is `#[ignore]` until Phase 5):

```rust
use rmk_audit::{concept_ids, contains_ci, parse_doc, workspace_root};
use shared::{Exhibit, RenderType, Rubric, Section};
use std::collections::BTreeSet;
use std::fs;

fn rubric_paths() -> Vec<std::path::PathBuf> {
    let dir = workspace_root().join("rubrics");
    let mut v: Vec<_> = fs::read_dir(dir)
        .map(|rd| {
            rd.filter_map(|e| e.ok().map(|e| e.path()))
                .filter(|p| p.extension().is_some_and(|e| e == "md"))
                .collect()
        })
        .unwrap_or_default();
    v.sort();
    v
}

fn load_manifest() -> Vec<Exhibit> {
    let path = workspace_root().join("content/figures/manifest.yaml");
    serde_yaml::from_str(&fs::read_to_string(path).expect("manifest")).expect("manifest yaml")
}

#[test]
fn manifest_is_complete_and_consistent() {
    let manifest = load_manifest();
    let ids: BTreeSet<_> = manifest.iter().map(|e| e.id.as_str()).collect();
    assert_eq!(ids.len(), manifest.len(), "duplicate exhibit ids");
    for n in 1..=11 {
        assert!(ids.contains(format!("exhibit-13-{n:02}").as_str()), "missing 13.{n}");
    }
    assert!(ids.contains("eq-13-1") && ids.contains("eq-13-2"), "missing equations");
    for ex in &manifest {
        match ex.render_type {
            RenderType::Crop => {
                assert!(!ex.segments.is_empty(), "{}: crop without segments", ex.id);
                assert!(!ex.caption.is_empty(), "{}: crop without caption", ex.id);
            }
            RenderType::ResetTable => {
                let p = workspace_root().join(ex.reset_table.as_ref().expect("reset_table"));
                assert!(p.exists(), "{}: reset_table file missing", ex.id);
            }
            RenderType::ResetEquation => {
                assert!(ex.reset_text.is_some() && ex.label.is_some(), "{}: equation fields", ex.id);
            }
        }
    }
}

#[test]
fn existing_sections_satisfy_their_rubrics() {
    let manifest = load_manifest();
    for rpath in rubric_paths() {
        let (rubric, _) = parse_doc::<Rubric>(&rpath).expect("rubric parses");
        let spath = workspace_root().join(format!("content/sections/{}.md", rubric.id));
        if !spath.exists() {
            continue; // section not yet written — strict test catches this at the end
        }
        let (section, body) = parse_doc::<Section>(&spath).expect("section parses");
        assert_eq!(section.id, rubric.id, "id mismatch in {}", spath.display());
        for kw in &rubric.required_keywords {
            assert!(
                contains_ci(&body, kw),
                "{}: missing required keyword {kw:?}",
                rubric.id
            );
        }
        for ex_id in &rubric.required_exhibits {
            assert!(
                section.embeds_exhibits.contains(ex_id),
                "{}: front matter missing exhibit {ex_id}",
                rubric.id
            );
            assert!(
                body.contains(&format!("{{{{exhibit:{ex_id}}}}}")),
                "{}: body missing directive for {ex_id}",
                rubric.id
            );
            assert!(
                manifest.iter().any(|m| &m.id == ex_id),
                "{}: exhibit {ex_id} not in manifest",
                rubric.id
            );
        }
    }
}

#[test]
#[ignore = "run in Phase 5: requires all 15 sections"]
fn strict_completeness() {
    let rubrics = rubric_paths();
    assert_eq!(rubrics.len(), 15, "expected 15 rubrics");
    let mut covered = Vec::new();
    for rpath in rubrics {
        let (rubric, _) = parse_doc::<Rubric>(&rpath).expect("rubric");
        let spath = workspace_root().join(format!("content/sections/{}.md", rubric.id));
        assert!(spath.exists(), "missing section {}", rubric.id);
        let (section, _) = parse_doc::<Section>(&spath).expect("section");
        covered.extend(section.covers_concepts.clone());
    }
    let unique: BTreeSet<_> = covered.iter().cloned().collect();
    assert_eq!(covered.len(), unique.len(), "concept assigned twice");
    let expected: BTreeSet<_> = concept_ids().into_iter().collect();
    assert_eq!(unique, expected, "concept coverage gap or surplus");
    // every manifest exhibit anchored by exactly one section that embeds it
    for ex in load_manifest() {
        let spath = workspace_root().join(format!("content/sections/{}.md", ex.anchor_section));
        let (section, body) = parse_doc::<Section>(&spath).expect("anchor section");
        assert!(section.embeds_exhibits.contains(&ex.id), "{} not embedded", ex.id);
        assert!(body.contains(&format!("{{{{exhibit:{}}}}}", ex.id)));
    }
}
```

- [ ] **Step 4: Replace `crates/rmk-audit/src/main.rs`:**

```rust
//! Concept-coverage + exhibit-anchoring audit CLI (human-readable report).

use anyhow::Result;
use clap::Parser;
use rmk_audit::{concept_ids, parse_doc, workspace_root};
use shared::Section;
use std::collections::BTreeSet;

/// Audit concept coverage across content sections.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    /// Fail if any concept or section is missing (Phase 5 gate).
    #[arg(long)]
    strict: bool,
}

fn main() -> Result<()> {
    let args = Args::parse();
    let dir = workspace_root().join("content/sections");
    let mut covered = BTreeSet::new();
    let mut sections = 0u32;
    if dir.exists() {
        let mut paths: Vec<_> = std::fs::read_dir(&dir)?
            .filter_map(|e| e.ok().map(|e| e.path()))
            .filter(|p| p.extension().is_some_and(|e| e == "md"))
            .collect();
        paths.sort();
        for p in paths {
            let (s, _) = parse_doc::<Section>(&p)?;
            println!("{}: {} concepts, {} exhibits", s.id, s.covers_concepts.len(), s.embeds_exhibits.len());
            covered.extend(s.covers_concepts);
            sections += 1;
        }
    }
    let missing: Vec<_> = concept_ids().into_iter().filter(|c| !covered.contains(c)).collect();
    println!("sections: {sections}/15 — concepts covered: {}/62", covered.len());
    if !missing.is_empty() {
        println!("missing: {}", missing.join(", "));
    }
    if args.strict {
        anyhow::ensure!(sections == 15 && missing.is_empty(), "coverage incomplete");
    }
    Ok(())
}
```

- [ ] **Step 5: Run all gates.** `cargo test && cargo clippy --all-targets -- -D warnings && cargo fmt --check` → green (coverage tests pass vacuously: no rubrics yet; manifest test passes from Task 1).
- [ ] **Step 6: Commit.** `git commit -am "feat(rmk-ch13): rmk-audit coverage harness (incremental + strict tests)"`

---

## Tasks 6–21: Content sections (RED → GREEN → REFACTOR → COMMIT each)

**Shared procedure for every section task** (referenced as Steps A–E; the data below each task is complete and self-sufficient):

- **Step A (RED):** Write the rubric file exactly as given. Run `cargo test -p rmk-audit --test coverage` — still green (section absent = skipped); the rubric defines the failure conditions the section must now satisfy.
- **Step B (GREEN):** Write `content/sections/<id>.md` with the given front matter and a body that follows the **content directives**, reading ONLY the given line range of `analysis/chapter13-raw.txt` (plus `content/_shared/` fragments). Body language: Indonesian, professor-led S2 voice per `specs/rmk-spec.md` §3. Every `{{exhibit:…}}` directive on its own line at the marked position. Every number must come from the chapter extract.
- **Step C:** Run `cargo test -p rmk-audit --test coverage` → `existing_sections_satisfy_their_rubrics` PASSES with the new section included. If it fails, fix the section (not the rubric).
- **Step D (REFACTOR):** Re-read the body against the rubric's `depth_check`. Deepen: every exhibit explained in prose (what it shows + at least one number read through); transitions connect to the previous section; no list-like paraphrase. Re-run Step C.
- **Step E:** `cargo test && cargo clippy --all-targets -- -D warnings && cargo fmt --check` then `git add -A . && git commit -m "feat(rmk-ch13): section <id>"`.

**Target lengths** (Calibri 12, 1.5 spacing; prose only, exhibits add height on top): heavy ≈ 450–600 words, medium ≈ 280–380, light ≈ 180–260.

---

### Task 6: `00-cover` (no rubric — validated by rmk-validate identity gate)

**Files:** Create: `content/00-cover.md`

- [ ] **Step 1:** Write `content/00-cover.md` exactly:

```markdown
---
id: 00-cover
title: "Halaman Identitas"
rubric: ""
---
{{center:**RINGKASAN MATERI KULIAH (RMK)**}}
{{center:**Statement of Cash Flows**}}
{{center:Wolk, Dodd & Rozycki — Accounting Theory: Conceptual Issues in a Political and Economic Environment, 9th ed., Chapter 13 (SAGE, 2017)}}
{{center:Mata Kuliah: Pelaporan Keuangan Korporat (MNK202)}}
{{center:**Kelompok 2**}}

| NIM | Nama |
| --- | --- |
| 122501039 | Satriyo Nugroho |
| 122501048 | Mario Da Costa |
| 122501067 | Amelda Putri Zhany Wiguna |
| 122501078 | Ahmad Ramadhan |
| 122501084 | Nida Nur Cahyati |
| 122501094 | Priska Putri Parungky |
```

- [ ] **Step 2:** Commit: `git add -A . && git commit -m "feat(rmk-ch13): cover/identity block"`

---

### Task 7: `00-pendahuluan` — Pendahuluan (light-medium; raw lines 26–71)

- [ ] **Step A:** `rubrics/00-pendahuluan.md`:

```markdown
---
id: 00-pendahuluan
required_concepts: ["C-01", "C-02", "C-03"]
required_exhibits: []
wolk_refs: ["Ch.13 opening, PDF p.2"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["The Music Man", "kas", "APB", "SFAS No. 95", "1987", "SCFP", "1971"]
depth_check:
  - "Membuka dengan motif The Music Man dan tesis kas-bukan-laba"
  - "Menjelaskan busur historis SCFP (APB 19, 1971) -> SCF (SFAS 95, 1987) sebagai pergeseran kepentingan FASB ke pelaporan basis kas"
  - "Memetakan struktur RMK (dua masalah besar: nonartikulasi & klasifikasi; lalu FCF, riset, rekomendasi)"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik Pendahuluan: tesis pembuka, busur historis, peta jalan RMK.
```

- [ ] **Step B:** `content/sections/00-pendahuluan.md` front matter:

```yaml
---
id: 00-pendahuluan
title: "1. Pendahuluan: Kas, Bukan Laba, yang Membayar Tagihan"
covers_concepts: ["C-01", "C-02", "C-03"]
embeds_exhibits: []
rubric: rubrics/00-pendahuluan.md
---
```

**Content directives:** (1) Buka dengan adegan *The Music Man* (para penjual menuntut "cash for the merchandise…") dan tarik tesisnya: tagihan, utang, dan dividen dibayar dengan kas, bukan laba; perusahaan yang gagal menghasilkan kas menghadapi kepunahan. (2) Busur historis: APB Opinion No. 19 (1971) mewajibkan SCFP ("funds flow"); SFAS No. 95 (1987) menggantikannya dengan SCF — transisi yang mencerminkan minat FASB pada pelaporan basis kas sebagai suplemen laporan akrual. (3) Tutup dengan peta jalan RMK yang mengikuti urutan bab: SCFP → motivasi & tujuan → struktur SCF & dua masalah besarnya (nonartikulasi; klasifikasi) → kegunaan analitis → FCF → riset → rekomendasi perbaikan. Sebutkan enam *learning objectives* bab secara naratif (bukan daftar).

- [ ] **Steps C–E** per shared procedure; commit message `feat(rmk-ch13): section 00-pendahuluan`.

---

### Task 8: `01-scfp-funds-flow` — SCFP dan Pendahulunya (heavy; raw lines 73–182)

- [ ] **Step A:** `rubrics/01-scfp-funds-flow.md`:

```markdown
---
id: 01-scfp-funds-flow
required_concepts: ["C-04", "C-05", "C-06", "C-07", "C-08", "C-09", "C-10"]
required_exhibits: ["eq-13-1", "exhibit-13-01"]
wolk_refs: ["Ch.13 SCFP section, PDF pp.3-4"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["funds flow", "APB Opinion No. 19", "derivatif", "transaction credits", "transaction debits", "all-inclusive", "quick assets", "modal kerja", "Exhibit 13.1", "SEC", "APB Opinion No. 3"]
depth_check:
  - "Menjelaskan MENGAPA SCFP disebut laporan derivatif"
  - "Membaca Exhibit 13.1: funds flow lama = butir 1a/1b; butir 2 menjadikannya all-inclusive"
  - "Menjelaskan mengapa mayoritas memilih net working capital (biaya penyusunan minimal)"
  - "Identitas (13.1) dijelaskan dari struktur debit-kredit"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik SCFP: pendahulu, tiga tujuan APB 19, sumber/penggunaan, empat definisi dana.
```

- [ ] **Step B:** front matter:

```yaml
---
id: 01-scfp-funds-flow
title: "2. Statement of Changes in Financial Position (SCFP) dan Pendahulunya"
covers_concepts: ["C-04", "C-05", "C-06", "C-07", "C-08", "C-09", "C-10"]
embeds_exhibits: ["eq-13-1", "exhibit-13-01"]
rubric: rubrics/01-scfp-funds-flow.md
---
```

**Content directives:** (1) *Funds flow statement* sebagai pendahulu SCFP: akun modal kerja sebagai *fund balance*; fokus likuiditas. (2) Tiga tujuan pelaporan APB Opinion No. 19 (lengkapi pengungkapan perubahan posisi keuangan; ringkas aktivitas pendanaan & investasi; laporkan *funds flow* dari operasi) dan mengapa ketiganya tak terbaca langsung dari laba rugi + neraca komparatif. (3) Sifat **derivatif**: bergantung pada definisi/pengukuran elemen dari dua laporan lain. Tempatkan `{{exhibit:eq-13-1}}` setelah paragraf ini, lalu jelaskan: *sources of resources* = *transaction credits* (kenaikan ekuitas, penurunan aset); *uses* = *transaction debits*. (4) Tempatkan `{{exhibit:exhibit-13-01}}` dan BACA strukturnya: funds flow lama hanya butir 1a/1b; menambah butir 2 menghasilkan SCFP *all-inclusive/all-resources* — beri contoh transaksi nonfund (konversi utang konversi, saham untuk aset nonmoneter, dividen properti, pertukaran nonmoneter). (5) Empat definisi dana yang diizinkan (kas; kas + *near cash*; *quick assets*; modal kerja) sebagai contoh fleksibilitas; jelaskan mengapa definisi modal kerja meminimalkan biaya → mayoritas memilihnya. (6) Garis waktu pengakuan: APB Opinion No. 3 (1963, anjuran) → SEC wajib (1971) → APB Opinion No. 19 (1971).

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 01-scfp-funds-flow`.

---

### Task 9: `02-motivation-scf` — Motivasi Menuju SCF (light; raw lines 184–203)

- [ ] **Step A:** `rubrics/02-motivation-scf.md`:

```markdown
---
id: 02-motivation-scf
required_concepts: ["C-11", "C-12"]
required_exhibits: []
wolk_refs: ["Ch.13 Motivation, PDF pp.4-5"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["net working capital", "deferred", "siklus operasi", "cash is cash"]
depth_check:
  - "Tiga alasan modal kerja neto buruk sebagai ukuran likuiditas dijelaskan DAN ditafsirkan"
  - "Menghubungkan ke keputusan FASB mendefinisikan dana = kas"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik motivasi: konsensus dana=kas; tiga kelemahan modal kerja neto.
```

- [ ] **Step B:** front matter (same pattern, `title: "3. Motivasi Menuju Laporan Arus Kas"`, concepts/exhibits per rubric). **Content directives:** Konsensus deliberasi FASB: dana harus didefinisikan sebagai kas, bukan modal kerja neto. Tiga alasan (jelaskan + tafsirkan masing-masing): (a) *deferred charges/credits* masuk modal kerja tetapi tanpa konsekuensi kas; (b) konversi aset lancar menjadi kas bisa lebih dari setahun pada siklus operasi panjang; (c) persediaan dicatat atas dasar biaya sehingga tidak mengukur potensi arus kasnya. Tutup dengan daya tarik literal pelaporan kas: "*cash is cash is cash*".

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 02-motivation-scf`.

---

### Task 10: `03-objectives` — Tujuan (medium-heavy; raw lines 205–300)

- [ ] **Step A:** `rubrics/03-objectives.md`:

```markdown
---
id: 03-objectives
required_concepts: ["C-13", "C-14", "C-15", "C-16", "C-17", "C-18", "C-19", "C-20"]
required_exhibits: []
wolk_refs: ["Ch.13 Objectives, PDF pp.5-6"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["SFAC No. 1", "SFAC No. 5", "quality of income", "komparabilitas", "fleksibilitas", "likuiditas", "exit-price", "prediksi"]
depth_check:
  - "Enam butir discussion memorandum dinarasikan sebagai jawaban atas keterbatasan akuntansi akrual"
  - "Quality of income didefinisikan presisi (korelasi laba-arus kas)"
  - "Kritik neraca sebagai panduan likuiditas yang buruk dijelaskan dengan alasan-alasannya"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik tujuan: SFAC 1 & 5, enam butir DM, quality of income, kritik neraca, exit-price.
```

- [ ] **Step B:** `title: "4. Tujuan Pelaporan Keuangan dan Tujuan SCF"`. **Content directives:** (1) Tiga tujuan SFAC No. 1 (decision-usefulness; sumber daya neto & perubahannya; penilaian arus kas masa depan) → motivasi 1980-an. (2) Klaim SFAC No. 5 tentang SCF (kutip substansinya: kas dari operasi untuk bayar utang/dividen/reinvestasi; pendanaan; investasi; menilai likuiditas, fleksibilitas, profitabilitas, risiko). (3) Enam butir *discussion memorandum* — narasikan (umpan balik; relasi laba–kas; *quality of income*; komparabilitas; fleksibilitas & likuiditas; prediksi) dan tunjukkan benang merahnya: semuanya menjawab keterbatasan akrual. (4) Definisi presisi *quality of income*: makin tinggi korelasi laba akuntansi dengan arus kas, makin tinggi kualitas laba. (5) Komparabilitas: CFO tunduk pada lebih sedikit pilihan kebijakan arbitrer daripada laba. (6) Definisi *financial flexibility* vs *liquidity*; kritik klasifikasi lancar–tak lancar neraca sebagai "peringkat likuiditas yang kasar" (deferred items; persediaan lambat; bukan NRV). (7) *Exit-price accounting* hanya indikator kasar — kecepatan konversi yang menentukan; perusahaan menambah modal secara inkremental. (8) Prediksi: belum tuntas apakah arus kas, arus dana, atau laba prediktor terbaik; filosofi *expanded disclosure*.

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 03-objectives`.

---

### Task 11: `04-structure-trichotomy` — Struktur SCF (light-medium; raw lines 302–334; gunakan `_shared/activity-classification.md`)

- [ ] **Step A:** `rubrics/04-structure-trichotomy.md`:

```markdown
---
id: 04-structure-trichotomy
required_concepts: ["C-21", "C-22", "C-23", "C-24"]
required_exhibits: []
wolk_refs: ["Ch.13 Structure, PDF p.7"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["trikotomi", "cash equivalents", "all-inclusive", "dissent", "operasi", "investasi", "pendanaan"]
depth_check:
  - "Kontras biner sumber/penggunaan vs trikotomi dijelaskan sebagai kenaikan konsistensi klasifikasi"
  - "Dissent 3-dari-7 dijelaskan substantif (bunga/dividen diterima = investasi; bunga dibayar = pendanaan, selaras disiplin keuangan)"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik struktur: trikotomi, kas & setara kas, suplemen nonkas, dissent.
```

- [ ] **Step B:** `title: "5. Struktur SCF: Trikotomi Operasi–Investasi–Pendanaan"`. **Content directives:** (1) Dari kerangka biner *sources/uses* SCFP ke trikotomi operasi–investasi–pendanaan: kategori yang lebih bermakna, konsistensi klasifikasi lebih tinggi, komparabilitas lebih besar (pakai definisi kanonik `_shared/activity-classification.md`). (2) Definisi kas: kas di tangan/giro + *cash equivalents* (investasi jangka pendek sangat likuid yang dapat dikonversi ke jumlah kas yang diketahui). (3) Konsep *all-inclusive* dipertahankan: transaksi investasi/pendanaan nonkas dilaporkan sebagai suplemen (skedul atau naratif). (4) Dissent tiga dari tujuh anggota FASB: bunga & dividen diterima berasal dari aktivitas investasi, bunga dibayar adalah elemen pendanaan — selaras pemikiran disiplin keuangan; rujuk ¶22–23 SFAS 95. Jembatani ke §6 (metode penyajian operasi).

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 04-structure-trichotomy`.

---

### Task 12: `05-direct-vs-indirect` — Metode Langsung vs Tidak Langsung (heavy + synthesis table; raw lines 336–451; gunakan `_shared/indirect-method-logic.md`)

- [ ] **Step A:** `rubrics/05-direct-vs-indirect.md`:

```markdown
---
id: 05-direct-vs-indirect
required_concepts: ["C-25", "C-26", "C-27", "C-28"]
required_exhibits: ["exhibit-13-02", "exhibit-13-03"]
wolk_refs: ["Ch.13 Requirements, PDF pp.7-9"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["metode langsung", "rekonsiliasi", "plug number", "McEnroe", "56%", "Exhibit 13.2", "Exhibit 13.3", "1.365"]
depth_check:
  - "Menjelaskan mengapa kedua metode menghasilkan CFO yang sama ($1.365 pada Company M)"
  - "Membaca Exhibit 13.2 (minimal: CFO $1.365 dari kas pelanggan $13.850 dst.) dan Exhibit 13.3 (laba $760 + penyesuaian $605)"
  - "Trade-off biaya-vs-keterpahaman dirumuskan tajam; praktik plug number disebut"
  - "Tabel sintesis langsung-vs-tidak-langsung hadir"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik metode: definisi keduanya, preferensi FASB, biaya, McEnroe, kewajiban rekonsiliasi.
```

- [ ] **Step B:** `title: "6. Metode Langsung versus Metode Tidak Langsung"`. **Content directives:** (1) Definisi keduanya (metode langsung = arus kas literal per klasifikasi laba rugi; tidak langsung/rekonsiliasi = laba akrual disesuaikan pos nonkas — pakai `_shared/indirect-method-logic.md`). (2) Preferensi FASB pada metode langsung (informasi lebih kaya) vs pengakuan argumen biaya; praktik *plug number* yang tidak disebut FASB. (3) Tempatkan `{{exhibit:exhibit-13-02}}`; baca: kas dari pelanggan $13.850 dikurangi pembayaran $12.000 dst. menghasilkan CFO $1.365; tunjukkan trikotomi bekerja (investasi −$1.175; pendanaan +$875; kenaikan kas $1.065). (4) Kewajiban skedul rekonsiliasi bila metode langsung dipakai; tempatkan `{{exhibit:exhibit-13-03}}`; baca: laba bersih $760 + total penyesuaian $605 = $1.365 — angka CFO yang SAMA, jalan yang berbeda. (5) Praktik: mayoritas besar perusahaan AS memilih tidak langsung (digerakkan biaya); survei McEnroe 282 responden: 56% vs 44%. (6) Rumuskan trade-off: mudah dipahami/sulit disusun vs mudah disusun/sulit dipahami. (7) Tabel sintesis (pipe table 3 kolom: Dimensi | Metode Langsung | Metode Tidak Langsung — baris: yang dilaporkan; preferensi FASB; biaya penyusunan; keterpahaman pengguna; kewajiban rekonsiliasi). Penomoran Indonesia: gunakan $1.365 (titik ribuan) konsisten.

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 05-direct-vs-indirect`.

---

### Task 13: `06-nonarticulation` — Nonartikulasi (heavy; raw lines 453–525)

- [ ] **Step A:** `rubrics/06-nonarticulation.md`:

```markdown
---
id: 06-nonarticulation
required_concepts: ["C-29", "C-30", "C-31", "C-32", "C-33", "C-34"]
required_exhibits: ["exhibit-13-04"]
wolk_refs: ["Ch.13 Nonarticulation, PDF pp.9-11"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["nonartikulasi", "Bahnson", "75%", "3M", "akuisisi", "accounts payable", "Exhibit 13.4", "300"]
depth_check:
  - "Definisi nonartikulasi presisi (perubahan akun modal kerja konsolidasi != penyesuaian modal kerja di seksi operasi)"
  - "Membaca Exhibit 13.4: selisih piutang 3M ~300% bahkan beda tanda"
  - "Tiga penyebab dijelaskan dengan mekanismenya, termasuk contoh utang usaha bersama (persediaan=operasi vs peralatan=investasi)"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik nonartikulasi: temuan BMB 75%, kasus 3M, tiga penyebab, DP 2008.
```

- [ ] **Step B:** `title: "7. Masalah Nonartikulasi"`. **Content directives:** (1) Temuan Bahnson, Miller & Budge: dengan metode tidak langsung, arus kas dari perubahan akun modal kerja konsolidasi ≠ penyesuaian modal kerja di seksi operasi; terjadi pada 75% sampel; SCF tampak tak konsisten dengan neraca. (2) Tempatkan `{{exhibit:exhibit-13-04}}`; baca: untuk 3M, selisih piutang usaha mencapai sekitar 300% — bahkan tanda bisa berbeda. (3) Penyebab 1: akuisisi tengah tahun (saldo modal kerja awal-tahun perusahaan terakuisisi tak masuk neraca konsolidasi awal). (4) Penyebab 2: transaksi modal kerja nonkas (write-up/down saat akuisisi pembelian; alokasi depresiasi ke persediaan manufaktur; reklasifikasi lancar/tak lancar). (5) Penyebab 3: satu akun utang usaha untuk pembelian operasi (persediaan) DAN investasi (peralatan) — jelaskan mekanismenya sampai tuntas. (6) Discussion paper FASB–IASB 2008: diskresi manajemen bertambah; nilai tambah diragukan; namun klasifikasi "business" tunggal bermanfaat menekan *classification shifting* (jembatan ke §8/§10).

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 06-nonarticulation`.

---

### Task 14: `07-classification-problems` — Masalah Klasifikasi (heavy + synthesis table; raw lines 527–636)

- [ ] **Step A:** `rubrics/07-classification-problems.md`:

```markdown
---
id: 07-classification-problems
required_concepts: ["C-35", "C-36", "C-37", "C-38", "C-39", "C-40", "C-41"]
required_exhibits: ["exhibit-13-05"]
wolk_refs: ["Ch.13 Classification Problems, PDF pp.11-13"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["Nurnberg", "proprietary", "entity", "IAS 7", "premium", "Vent", "SFAS No. 34", "SFAS No. 104", "fineness", "Exhibit 13.5", "lease", "$550"]
depth_check:
  - "Kontras teori proprietary vs entity dijelaskan sebagai akar masalah klasifikasi"
  - "Pengaruh industri perbankan dijelaskan (menghindari CFO negatif)"
  - "Membaca Exhibit 13.5: obligasi 8% $10.000 dijual $11.000; beban bunga $550; Metode 1 pilihan penulis; Metode 4 paling tidak masuk akal"
  - "Pertanyaan nature-vs-purpose dirumuskan untuk bunga dikapitalisasi dan lease"
  - "Tabel sintesis Metode 1-4 hadir"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik klasifikasi: Nurnberg, proprietary/entity, perbankan, IAS 7, premi/diskon, SFAS 34, lease, SFAS 104.
```

- [ ] **Step B:** `title: "8. Masalah Klasifikasi SFAS No. 95"`. **Content directives:** (1) Kritik Nurnberg: trikotomi diklaim mengikuti literatur keuangan, tetapi SFAS 95 menempatkan bunga/dividen diterima sebagai arus masuk operasi dan bunga dibayar sebagai arus keluar operasi — menurut literatur keuangan keduanya investasi dan pendanaan. (2) Akar teorinya: orientasi *proprietary* (mengikuti format laba rugi) vs pendekatan *entity*; pertimbangan praktis: industri perbankan menghindari CFO negatif. (3) IAS 7: fleksibel (operasi/investasi/pendanaan asal konsisten antarperiode) — kontras dengan orientasi proprietary SFAS 95; keseragaman intra-industri bila bank memilih operasi. (4) Premi/diskon obligasi & notes: contoh kerja Vent, Cowling & Sevalstad — obligasi kupon 8% empat tahun, nilai nominal $10.000, dijual $11.000 (31 Des 2000); amortisasi garis lurus; beban bunga tahunan $550 ($800 − $250). Tempatkan `{{exhibit:exhibit-13-05}}`; baca keempat metode: Metode 1 paling mudah & hampir pasti dipakai metode langsung (premi $1.000 = arus pendanaan tahun 2000, sehingga jumlah arus operasi ≠ beban bunga akrual); Metode 2 menempatkan premi ke operasi tahun pembayaran (2004), Metode 3 ke tahun penerbitan (2000), Metode 4 mengalokasikannya selama umur obligasi — paling tidak masuk akal (memecah arus kas $800 tahunan menjadi dua segmen); ini contoh lain masalah alokasi. (5) Bunga dikapitalisasi (SFAS No. 34, via Munter): keluar dari operasi, masuk investasi sebagai biaya perolehan aset — pertanyaan *basic nature* vs *ultimate purpose*. (6) Lease: operasi (seluruh pembayaran = operasi) vs kapital (porsi bunga = operasi; pelunasan pokok = pendanaan) — pertanyaan yang sama, belum terjawab. (7) SFAS No. 104: fleksibilitas hedging (klasifikasi mengikuti pos neraca yang dilindung nilai atau investasi); Nurnberg & Largay: komparabilitas turun tetapi mungkin dibenarkan sebagai kenaikan *fineness*; rujuk ASC 230-10-45. (8) Tabel sintesis Metode 1–4 (pipe table: Metode | Perlakuan premi | Penilaian penulis).

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 07-classification-problems`.

---

### Task 15: `08-analytical-usefulness` — Kegunaan Analitis (light; raw lines 638–668)

- [ ] **Step A:** `rubrics/08-analytical-usefulness.md`:

```markdown
---
id: 08-analytical-usefulness
required_concepts: ["C-42"]
required_exhibits: []
wolk_refs: ["Ch.13 Analytical Usefulness, PDF pp.13-14"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["Ingram", "Lee", "leverage", "1974", "1992"]
depth_check:
  - "Mekanisme firma bertumbuh (laba naik, CFO tertekan oleh persediaan & piutang) dijelaskan kausal, bukan deskriptif"
  - "Simetri firma berkontraksi dijelaskan; temuan leverage disebut"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik Ingram & Lee: laba rugi + SCF digunakan bersama; ~1.000 firma 1974-1992.
```

- [ ] **Step B:** `title: "9. Kegunaan Analitis Laporan Arus Kas"`. **Content directives:** Riset Ingram & Lee — laba rugi dan SCF dibaca bersama. Firma bertumbuh: laba lebih tinggi tetapi CFO lebih rendah (persediaan & piutang membengkak, sebagian diimbangi utang usaha; perubahan laba melebihi perubahan CFO); arus investasi keluar; arus pendanaan masuk; dividen rendah. Firma berkontraksi: hubungan berbalik. Analisis statistik ±1.000 firma (1974–1992) mendukung; temuan tambahan: firma yang berekspansi cenderung memiliki *leverage* lebih besar. Tafsirkan: pola lintas-seksi SCF adalah sidik jari siklus hidup perusahaan — jembatan ke §10 (apa yang terjadi bila pola itu direkayasa).

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 08-analytical-usefulness`.

---

### Task 16: `09-misclassification` — Misklasifikasi (medium; raw lines 670–725)

- [ ] **Step A:** `rubrics/09-misclassification.md`:

```markdown
---
id: 09-misclassification
required_concepts: ["C-43", "C-44", "C-45", "C-46"]
required_exhibits: []
wolk_refs: ["Ch.13 Issues Relating to Rules, PDF pp.14-15"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["Tyco", "Ford", "General Motors", "Harley-Davidson", "Navistar", "notes receivable", "7,6"]
depth_check:
  - "Logika pergeseran (total kas tetap, persepsi membaik) dijelaskan"
  - "Kasus Tyco dijelaskan sampai kontras kontrak-dibeli vs kontrak-internal (rigid uniformity yang layak)"
  - "Angka GM: CFO $7,6 miliar vs $3,5 miliar bila operasi"
  - "Kontras Navistar dikutip/diparafrase dengan maknanya: fleksibilitas melemahkan komparabilitas tanpa melanggar aturan"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik misklasifikasi: shifting, Tyco, industri otomotif, Navistar.
```

- [ ] **Step B:** `title: "10. Misklasifikasi dan Manipulasi Klasifikasi"`. **Content directives:** (1) SCF lebih sulit dimanipulasi daripada laba, tetapi tidak kebal: karena CFO menjadi fokus pengguna, ada aktivitas menggeser arus keluar operasi→investasi dan arus masuk investasi→operasi; total kas tak berubah, persepsi membaik. (2) Tyco (Maremont): kontrak dealer yang dibeli diperlakukan sebagai "akuisisi" dengan pengakuan arus keluar operasi jauh lebih lambat daripada kontrak alarm internal — kasus di mana *rigid uniformity* justru layak. (3) Industri otomotif (Mulford, WSJ): Ford, General Motors, Harley-Davidson meminjamkan ke dealer via *notes receivable* untuk membeli persediaan; pendapatan diakui, pinjaman diklasifikasikan investasi → CFO terkerek; GM: CFO dilaporkan $7,6 miliar vs $3,5 miliar bila notes receivable diperlakukan operasi. (4) Kontras Navistar: hasil konsolidasi MEreklasifikasi notes receivable anak pembiayaan ke CFO — "we define ourselves as a manufacturing company with a finance subsidiary". (5) Simpulan: bahkan tanpa pelanggaran aturan, kelenturan penerapan membuat perusahaan seindustri memberi gambaran sangat berbeda; komparabilitas lemah. Solusi parsial menyusul (§11).

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 09-misclassification`.

---

### Task 17: `10-scf-more-than-cfo` — WorldCom (medium; raw lines 727–776)

- [ ] **Step A:** `rubrics/10-scf-more-than-cfo.md`:

```markdown
---
id: 10-scf-more-than-cfo
required_concepts: ["C-47", "C-48"]
required_exhibits: ["exhibit-13-06"]
wolk_refs: ["Ch.13 SCF Is More Than CFO, PDF pp.15-16"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["WorldCom", "Chapter 11", "Exhibit 13.6", "12", "2001", "CFO", "CFI"]
depth_check:
  - "Mekanisme WorldCom dijelaskan: kapitalisasi beban operasi -> CFO terkerek -> laba tampak kredibel"
  - "Membaca Exhibit 13.6: CFO-CFI negatif tiga dari empat tahun; kumulatif ~$12 miliar pada 31 Des 2001"
  - "Pelajaran dirumuskan: SCF harus dibaca utuh; pengguna yang mengabaikan satu seksi menanggung risikonya"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik WorldCom: tiga seksi sama penting; lubang $12 miliar.
```

- [ ] **Step B:** `title: "11. SCF Lebih dari Sekadar Arus Kas Operasi: Pelajaran WorldCom"`. **Content directives:** (1) Perhatian berlebih pada CFO problematik; ketiga seksi penting. (2) WorldCom: petisi Chapter 11 pada 21 Juli 2002; sebelum bangkrut mengkapitalisasi beban yang seharusnya operasi → CFO terkerek, laba tampak kredibel. (3) Tempatkan `{{exhibit:exhibit-13-06}}`; baca: laba bersih positif tiga tahun sebelum kebangkrutan, tetapi CFO−CFI menunjukkan perusahaan "berdarah" kas pada tiga dari empat tahun; kumulatif menggali lubang ±$12 miliar per 31 Desember 2001. (4) Tafsir: bahkan bila investasi dianggap sah, berapa lama pola itu bisa berlanjut — kapan lubang berhenti dalam dan bagaimana memanjat keluar? (5) Pelajaran: SCF, dibaca utuh, memberi gambaran kemampuan neto menghasilkan kas; "investors who ignore one or more parts do so at their peril."

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 10-scf-more-than-cfo`.

---

### Task 18: `11-user-needs` — Kebutuhan Pengguna (light-medium; raw lines 778–825)

- [ ] **Step A:** `rubrics/11-user-needs.md`:

```markdown
---
id: 11-user-needs
required_concepts: ["C-49", "C-50"]
required_exhibits: []
wolk_refs: ["Ch.13 Cash Flow Needs, PDF pp.16-17"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["Buffett", "Berkshire", "intrinsik", "NPV", "1988"]
depth_check:
  - "Tiga pertanyaan Buffett dipetakan ke valuasi, kredit, dan stewardship"
  - "Definisi nilai intrinsik Buffett diparafrase akurat (nilai diskonto kas yang dapat diambil; estimasi, bukan angka pasti)"
  - "Kerangka NPV/penganggaran modal dihubungkan ke pembelian saham"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik kebutuhan pengguna: Buffett 1988, intrinsic value, NPV.
```

- [ ] **Step B:** `title: "12. Kebutuhan Arus Kas Berbagai Pengguna"`. **Content directives:** (1) Surat Buffett 1988 (Berkshire Hathaway): tiga pertanyaan kunci — nilai perusahaan; kemampuan memenuhi kewajiban; kualitas kerja manajemen "given the hand they have been dealt" — petakan ke valuasi, keputusan kredit, dan penilaian kinerja manajerial; stewardship butuh arus kas historis akurat; kredit/valuasi butuh prediksi tak bias (selaras SFAC No. 1). (2) Investasi = keputusan alokasi modal; kriteria penganggaran modal: terima bila NPV positif; pembelian saham layak bila nilai kini per saham arus kas harapan (*intrinsic value*) > harga pasar. (3) Definisi intrinsik Buffett ("Owner's Manual"): nilai diskonto kas yang dapat diambil dari bisnis selama sisa umurnya — estimasi yang berubah bila suku bunga atau prakiraan berubah. (4) Pertanyaan penghubung ke §13: arus kas APA yang didiskontokan? — jawabannya FCF.

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 11-user-needs`.

---

### Task 19: `12-free-cash-flow` — FCF + ABC Company (heaviest + synthesis table; raw lines 820–929)

- [ ] **Step A:** `rubrics/12-free-cash-flow.md`:

```markdown
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
```

- [ ] **Step B:** `title: "13. Free Cash Flow dan Ilustrasi ABC Company"`. **Content directives:** (1) FCF = analog firma dari arus kas penganggaran modal; Mulford & Comiskey: "free" = tiadanya klaim yang lebih senior; popularitas naik sebagai reaksi skandal manajemen laba; beberapa definisi beredar — bab mengikuti *entity theory* (arus kas kepada firma). (2) Tempatkan `{{exhibit:eq-13-2}}`; jelaskan komponen: NOPLAT = *net operating profit less adjusted taxes* (≈ laba operasi setelah pajak); investasi pada *operating invested capital* = modal kerja operasi neto + aset tak lancar; bunga DIKECUALIKAN (beban pendanaan); kas operasi diperlakukan sebagai bagian *invested capital*. (3) FCF tidak terbaca langsung dari SCF — harus dikonstruksi. (4) Alur ABC Company sebagai SATU narasi konstruksi: `{{exhibit:exhibit-13-07}}` (laba rugi + neraca 2004–2007 — bahan baku); `{{exhibit:exhibit-13-08}}` (SCF: baca CFO 2005 $527, CFI $(277), CFF $(306)); `{{exhibit:exhibit-13-09}}` (laporan FCF: dari pajak basis kas atas laba operasi sampai *free cash flows from operating assets* lalu ke ekuitas); `{{exhibit:exhibit-13-10}}` (jembatan: CFO $527 + bunga setelah pajak $26 − kenaikan kas operasi $56 + CFI $(277)* = FCF $332 untuk 2005 — *baca tanda-tanda persis dari exhibit*); `{{exhibit:exhibit-13-11}}` (empat ukuran dibandingkan: laba bersih $320; CFO $527; CFO−CFI $250; FCF $332 pada 2005). (5) Tafsir 13.11: pilihan ukuran bergantung waktu/sumber daya/tujuan; CFO "terkontaminasi" bunga; CFO−CFI menetralkan misklasifikasi beban-sebagai-investasi; nilai intrinsik = FCF prakiraan didiskontokan pada WACC; "the real world is never simple". (6) Tabel sintesis empat ukuran (pipe table: Ukuran | Apa yang ditangkap | Keterbatasan). PERIKSA semua angka terhadap crop exhibit hasil Phase 3.5 — bukan dari ingatan.

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 12-free-cash-flow`.

---

### Task 20: `13-research` — Riset (light; raw lines 930–956)

- [ ] **Step A:** `rubrics/13-research.md`:

```markdown
---
id: 13-research
required_concepts: ["C-56", "C-57", "C-58"]
required_exhibits: []
wolk_refs: ["Ch.13 Cash and Funds Flow Research, PDF p.21"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["Lawson", "Lee", "akrual", "komplementer"]
depth_check:
  - "Kutipan Lee diparafrase tepat (profit abstraksi; kas sumber daya fisik)"
  - "Sintesis komplementaritas dirumuskan: kas dan akrual lebih berguna bersama; dekomposisi memberi informasi baru"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik riset: Lawson & Lee, bukti pasar modal, survei FAF.
```

- [ ] **Step B:** `title: "14. Riset Arus Kas dan Arus Dana"`. **Content directives:** (1) Lawson & Lee: laporan arus kas perlu untuk melaporkan kinerja; Lee: "Cash flow and not profit is the end result of entity activity. Profit is an abstraction; cash is a physical resource." (2) Model valuasi arus kas dari ekonomika keuangan sejalan; NAMUN bukti riset pasar modal: akrual memberi informasi DI ATAS arus kas literal terhadap harga sekuritas. (3) Sintesis: keduanya lebih berguna bersama — SCF komplementer terhadap laporan akrual; dekomposisi data akrual ke komponen kas + akrual menghasilkan informasi baru. (4) Survei: analisis profitabilitas akrual masih dominan, tetapi survei FAF menunjukkan arus dana menanjak dan akrual menurun kepentingannya.

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 13-research`.

---

### Task 21: `14-improving-scf` — Perbaikan + Sintesis (medium; raw lines 958–1051)

- [ ] **Step A:** `rubrics/14-improving-scf.md`:

```markdown
---
id: 14-improving-scf
required_concepts: ["C-59", "C-60", "C-61", "C-62"]
required_exhibits: []
wolk_refs: ["Ch.13 Improving the SCF + Summary, PDF pp.21-23"]
format_rules: ["1.5 spacing", "12 pt Calibri"]
required_keywords: ["Broome", "rekonsiliasi", "metode langsung", "akuisisi", "Adelphia", "rekomendasi"]
depth_check:
  - "Tiga rekomendasi Broome dinarasikan dengan alasannya"
  - "Rekomendasi para penulis dibedakan dari Broome (skedul transaksi nonkas modal kerja; rekonsiliasi akuisisi tengah tahun; jelaskan sumber nonartikulasi)"
  - "Sintesis penutup mengikat seluruh RMK: derivatif-namun-informatif; proprietary vs entity; dua masalah; FCF; arah ke depan"
verification: ["cargo test -p rmk-audit --test coverage"]
---
Rubrik perbaikan: Broome x3, rekomendasi penulis, sintesis bab.
```

- [ ] **Step B:** `title: "15. Memperbaiki SCF dan Sintesis Penutup"`. **Content directives:** (1) Broome: SCF krusial bagi analisis sekuritas; pasca Adelphia, Dynegy, Qwest, Tyco, WorldCom ia berargumen SCF bisa dan harus diperbaiki; penyesuaian metode tidak langsung sulit dipahami, memberi keleluasaan manipulasi, kerap tak terekonsiliasi dengan perubahan neraca. (2) Tiga rekomendasi Broome: wajibkan metode langsung DAN rekonsiliasinya; pedoman klasifikasi lebih banyak; balik arah rekonsiliasi (mulai dari CFO menuju laba bersih). (3) Rekomendasi penulis: setuju metode langsung diwajibkan; bila pilihan dipertahankan — wajibkan skedul transaksi nonkas yang menyentuh modal kerja; untuk akuisisi tengah tahun, skedul rekonsiliasi penyesuaian modal kerja terhadap perubahan neraca; umumnya, jelaskan sumber nonartikulasi. (4) Sintesis penutup (dari Summary bab): SCF = kasus khusus SCFP dengan dana = kas; derivatif namun informatif lewat dekomposisi kas/akrual dan trikotomi; pilihan proprietary dan konsekuensi klasifikasinya; nonartikulasi dan misklasifikasi sebagai dua masalah menetap; IAS fleksibel; riset mendukung kandungan informasi; FCF tumbuh (konsisten bunga = pendanaan); penilaian penulis: transisi ke SCF menaikkan konsistensi, daya prediksi, dan komparabilitas — SCF akan semakin penting karena bebas dari "kesewenang-wenangan" laba.

- [ ] **Steps C–E**; commit `feat(rmk-ch13): section 14-improving-scf`.

---

## Task 22: Implement rmk-build + full python-docx bridge

**Files:**
- Create: `crates/rmk-build/src/lib.rs`
- Modify: `crates/rmk-build/src/main.rs`, `crates/rmk-build/Cargo.toml` (add `serde_json`)
- Modify: `tools/build_docx.py` (add `--spec` mode)
- Modify: root `Cargo.toml` (add `serde_json = "1"` to `[workspace.dependencies]`)

- [ ] **Step 1: Write failing parser tests** in `crates/rmk-build/src/lib.rs` (tests first, then the code in the same file):

```rust
//! Markdown-subset -> block-list compiler for the docx bridge.

use serde::Serialize;
use shared::{Exhibit, RenderType};

#[derive(Debug, PartialEq, Serialize)]
#[serde(tag = "type", rename_all = "kebab-case")]
pub enum Block {
    Heading { level: u8, text: String },
    Para { runs: Vec<Run> },
    Center { runs: Vec<Run> },
    Image { path: String, width_in: f64 },
    Caption { text: String },
    Table { rows: Vec<Vec<String>> },
    Equation { label: String, text: String },
}

#[derive(Debug, PartialEq, Serialize)]
pub struct Run {
    pub text: String,
    pub bold: bool,
    pub italic: bool,
}

/// Parse `**bold**` / `*italic*` inline markup into runs.
pub fn parse_runs(s: &str) -> Vec<Run> {
    let mut runs = Vec::new();
    let mut rest = s;
    while !rest.is_empty() {
        if let Some(r) = rest.strip_prefix("**") {
            if let Some(end) = r.find("**") {
                runs.push(Run { text: r[..end].into(), bold: true, italic: false });
                rest = &r[end + 2..];
                continue;
            }
        }
        if let Some(r) = rest.strip_prefix('*') {
            if let Some(end) = r.find('*') {
                runs.push(Run { text: r[..end].into(), bold: false, italic: true });
                rest = &r[end + 1..];
                continue;
            }
        }
        let next = rest[1..].find(['*']).map(|i| i + 1).unwrap_or(rest.len());
        runs.push(Run { text: rest[..next].into(), bold: false, italic: false });
        rest = &rest[next..];
    }
    // merge adjacent plain runs is unnecessary; python concatenates faithfully
    runs
}

fn parse_table_row(line: &str) -> Vec<String> {
    line.trim()
        .trim_start_matches('|')
        .trim_end_matches('|')
        .split('|')
        .map(|c| c.trim().replace("&nbsp;", "\u{00A0}"))
        .collect()
}

fn is_separator_row(line: &str) -> bool {
    let t: String = line.chars().filter(|c| !c.is_whitespace()).collect();
    !t.is_empty() && t.chars().all(|c| matches!(c, '|' | '-' | ':'))
}

/// Compile one markdown body into blocks, resolving exhibit directives.
pub fn compile_body(body: &str, manifest: &[Exhibit], figures_dir: &str) -> anyhow::Result<Vec<Block>> {
    let mut blocks = Vec::new();
    let lines: Vec<&str> = body.lines().collect();
    let mut i = 0;
    while i < lines.len() {
        let line = lines[i].trim_end();
        let trimmed = line.trim();
        if trimmed.is_empty() {
            i += 1;
            continue;
        }
        if let Some(h) = trimmed.strip_prefix("## ") {
            blocks.push(Block::Heading { level: 2, text: h.into() });
        } else if let Some(h) = trimmed.strip_prefix("# ") {
            blocks.push(Block::Heading { level: 1, text: h.into() });
        } else if let Some(c) = trimmed.strip_prefix("{{center:").and_then(|s| s.strip_suffix("}}")) {
            blocks.push(Block::Center { runs: parse_runs(c) });
        } else if let Some(id) = trimmed.strip_prefix("{{exhibit:").and_then(|s| s.strip_suffix("}}")) {
            let ex = manifest
                .iter()
                .find(|e| e.id == id)
                .ok_or_else(|| anyhow::anyhow!("unknown exhibit id {id}"))?;
            match ex.render_type {
                RenderType::Crop => {
                    blocks.push(Block::Image {
                        path: format!("{figures_dir}/{}.png", ex.id),
                        width_in: ex.target_width_in,
                    });
                    blocks.push(Block::Caption { text: ex.caption.clone() });
                }
                RenderType::ResetTable => {
                    let table_md = std::fs::read_to_string(
                        ex.reset_table.as_ref().expect("reset_table path"),
                    )?;
                    let rows = table_md
                        .lines()
                        .filter(|l| l.trim().starts_with('|') && !is_separator_row(l))
                        .map(parse_table_row)
                        .collect();
                    blocks.push(Block::Table { rows });
                    blocks.push(Block::Caption { text: ex.caption.clone() });
                }
                RenderType::ResetEquation => blocks.push(Block::Equation {
                    label: ex.label.clone().unwrap_or_default(),
                    text: ex.reset_text.clone().unwrap_or_default(),
                }),
            }
        } else if trimmed.starts_with('|') {
            let mut rows = Vec::new();
            while i < lines.len() && lines[i].trim().starts_with('|') {
                if !is_separator_row(lines[i]) {
                    rows.push(parse_table_row(lines[i]));
                }
                i += 1;
            }
            blocks.push(Block::Table { rows });
            continue;
        } else {
            // paragraph: join consecutive non-blank, non-special lines
            let mut para = String::from(trimmed);
            while i + 1 < lines.len() {
                let n = lines[i + 1].trim();
                if n.is_empty() || n.starts_with('#') || n.starts_with('|') || n.starts_with("{{") {
                    break;
                }
                para.push(' ');
                para.push_str(n);
                i += 1;
            }
            blocks.push(Block::Para { runs: parse_runs(&para) });
        }
        i += 1;
    }
    Ok(blocks)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn runs_parse_bold_italic() {
        let r = parse_runs("a **b** c *d*");
        assert_eq!(r.len(), 4);
        assert!(r[1].bold && r[1].text == "b");
        assert!(r[3].italic && r[3].text == "d");
    }

    #[test]
    fn heading_and_para() {
        let b = compile_body("# Judul\n\nIsi satu\nlanjutan.", &[], "content/figures").unwrap();
        assert_eq!(b.len(), 2);
        assert!(matches!(&b[0], Block::Heading { level: 1, text } if text == "Judul"));
        assert!(matches!(&b[1], Block::Para { runs } if runs[0].text == "Isi satu lanjutan."));
    }

    #[test]
    fn pipe_table_parses() {
        let b = compile_body("| A | B |\n| --- | --- |\n| 1 | 2 |", &[], "f").unwrap();
        assert!(matches!(&b[0], Block::Table { rows } if rows.len() == 2 && rows[1] == vec!["1", "2"]));
    }

    #[test]
    fn equation_directive_resolves() {
        let manifest = vec![Exhibit {
            id: "eq-13-1".into(),
            caption: String::new(),
            render_type: RenderType::ResetEquation,
            segments: vec![],
            target_width_in: 6.25,
            anchor_section: "01-scfp-funds-flow".into(),
            reset_text: Some("transaction credits = transaction debits".into()),
            reset_table: None,
            label: Some("(13.1)".into()),
        }];
        let b = compile_body("{{exhibit:eq-13-1}}", &manifest, "f").unwrap();
        assert!(matches!(&b[0], Block::Equation { label, .. } if label == "(13.1)"));
    }

    #[test]
    fn unknown_exhibit_errors() {
        assert!(compile_body("{{exhibit:nope}}", &[], "f").is_err());
    }
}
```

- [ ] **Step 2: Run** `cargo test -p rmk-build` → 5 passed (compile errors first; fix until green). Add `serde_json = { workspace = true }` to `crates/rmk-build/Cargo.toml` and `serde_json = "1"` to root `[workspace.dependencies]`.

- [ ] **Step 3: Rewrite `crates/rmk-build/src/main.rs`:** keep `--smoke` behavior; full mode: read manifest; compile `content/00-cover.md` body, then every `content/sections/*.md` (sorted) — for each section emit `Block::Heading{level:1, text: front_matter.title}` then its compiled body; serialize all blocks to `output/build-spec.json` (`serde_json::to_string_pretty`); run `python tools/build_docx.py --spec output/build-spec.json --output <args.output>`; ensure exit success. Front-matter parsing: reuse `rmk_audit::parse_doc` — add `rmk-audit = { path = "../rmk-audit" }` to `crates/rmk-build/Cargo.toml` dependencies.

```rust
//! Assemble content into the final .docx via the python-docx bridge.

use anyhow::{Context, Result};
use clap::Parser;
use rmk_audit::{parse_doc, workspace_root};
use rmk_build::{compile_body, Block};
use shared::{Exhibit, Section};
use std::fs;
use std::process::Command;

/// Build the RMK .docx from markdown sections and the figure manifest.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    #[arg(long, default_value = "output/RMK Chap. 13_Kelompok 2_PKK.docx")]
    output: String,
    /// Run the python-docx bridge smoke test only.
    #[arg(long)]
    smoke: bool,
}

fn main() -> Result<()> {
    let args = Args::parse();
    let root = workspace_root();
    if args.smoke {
        let status = Command::new("python")
            .arg(root.join("tools/build_docx.py"))
            .arg("--smoke")
            .current_dir(&root)
            .status()?;
        anyhow::ensure!(status.success(), "python-docx bridge smoke test failed");
        println!("python-docx bridge smoke test OK");
        return Ok(());
    }
    let manifest: Vec<Exhibit> = serde_yaml::from_str(&fs::read_to_string(
        root.join("content/figures/manifest.yaml"),
    )?)?;
    let figures_dir = "content/figures";
    let mut blocks: Vec<Block> = Vec::new();
    let (_, cover_body) = parse_doc::<Section>(&root.join("content/00-cover.md"))?;
    blocks.extend(compile_body(&cover_body, &manifest, figures_dir)?);
    let mut section_paths: Vec<_> = fs::read_dir(root.join("content/sections"))?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .filter(|p| p.extension().is_some_and(|e| e == "md"))
        .collect();
    section_paths.sort();
    for p in &section_paths {
        let (meta, body) = parse_doc::<Section>(p)?;
        blocks.push(Block::Heading { level: 1, text: meta.title });
        blocks.extend(compile_body(&body, &manifest, figures_dir)?);
    }
    fs::create_dir_all(root.join("output"))?;
    let spec_path = root.join("output/build-spec.json");
    fs::write(&spec_path, serde_json::to_string_pretty(&blocks)?)?;
    println!("compiled {} blocks from {} sections", blocks.len(), section_paths.len());
    let status = Command::new("python")
        .arg(root.join("tools/build_docx.py"))
        .args(["--spec", spec_path.to_str().context("path")?])
        .args(["--output", &args.output])
        .current_dir(&root)
        .status()?;
    anyhow::ensure!(status.success(), "docx bridge failed");
    println!("built {}", args.output);
    Ok(())
}
```

NOTE: `compile_body` resolves `reset_table` paths relative to the process CWD; run `rmk-build` from the workspace root (the `current_dir(&root)` covers the bridge; for the Rust side, the executor runs `cargo run -p rmk-build` from the workspace root, where `content/...` resolves). If path issues arise, prefix with `workspace_root()` in `compile_body` calls by passing absolute `figures_dir` — keep it simple and run from the root.

- [ ] **Step 4: Extend `tools/build_docx.py`** — add `--spec`/`--output` mode rendering the block list (keep `--smoke` and `base_doc()` unchanged):

```python
def render_spec(spec_path: str, output: str) -> int:
    import json
    blocks = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    doc = base_doc()
    for st, size in (("Heading 1", 14), ("Heading 2", 12)):
        s = doc.styles[st]
        s.font.name, s.font.size, s.font.bold = FONT, Pt(size), True
        from docx.shared import RGBColor
        s.font.color.rgb = RGBColor(0, 0, 0)
        s.paragraph_format.line_spacing = LINE_SPACING
    def add_runs(p, runs):
        for r in runs:
            run = p.add_run(r["text"])
            run.bold, run.italic = r.get("bold", False), r.get("italic", False)
    for b in blocks:
        t = b["type"]
        if t == "heading":
            doc.add_heading(b["text"], level=b["level"])
        elif t == "para":
            add_runs(doc.add_paragraph(), b["runs"])
        elif t == "center":
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_runs(p, b["runs"])
        elif t == "image":
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(b["path"], width=Inches(b["width_in"]))
        elif t == "caption":
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(b["text"])
            r.italic = True
        elif t == "table":
            rows = b["rows"]
            ncols = max(len(r) for r in rows)
            tbl = doc.add_table(rows=0, cols=ncols)
            tbl.style = "Table Grid"
            for row in rows:
                cells = tbl.add_row().cells
                for j in range(ncols):
                    text = row[j] if j < len(row) else ""
                    para = cells[j].paragraphs[0]
                    para.paragraph_format.line_spacing = LINE_SPACING
                    for r in parse_md_runs(text):
                        run = para.add_run(r[0])
                        run.bold, run.italic = r[1], r[2]
            if len(rows) > 1 and ncols == 1:
                pass  # single-column exhibit boxes keep grid style
        elif t == "equation":
            lbl = doc.add_paragraph(b["label"])
            lbl.paragraph_format.space_after = Pt(0)
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run(b["text"]).bold = True
        else:
            raise ValueError(f"unknown block type {t}")
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)
    print(f"built {out}")
    return 0


def parse_md_runs(s: str):
    """Minimal **bold** / *italic* splitter for table cells -> [(text, bold, italic)]."""
    out, rest = [], s
    while rest:
        if rest.startswith("**") and "**" in rest[2:]:
            end = rest.index("**", 2)
            out.append((rest[2:end], True, False))
            rest = rest[end + 2:]
        elif rest.startswith("*") and "*" in rest[1:]:
            end = rest.index("*", 1)
            out.append((rest[1:end], False, True))
            rest = rest[end + 1:]
        else:
            nxt = rest.find("*", 1)
            cut = len(rest) if nxt == -1 else nxt
            out.append((rest[:cut], False, False))
            rest = rest[cut:]
    return out
```

Wire into `main()`: add `ap.add_argument("--spec")`, `ap.add_argument("--output")`; `if args.spec and args.output: return render_spec(args.spec, args.output)`.

- [ ] **Step 5: End-to-end check** (works as soon as ≥1 section exists): `cargo run -p rmk-build` → docx builds; open `output/RMK Chap. 13_Kelompok 2_PKK.docx` in Word — cover renders centered, member table grid, sections in order, exhibits inline with captions.
- [ ] **Step 6: Gates + commit.** `cargo test && cargo clippy --all-targets -- -D warnings && cargo fmt --check` → green. `git commit -am "feat(rmk-ch13): rmk-build block compiler + full docx bridge"`

---

## Task 23: Implement rmk-validate + validate_docx.py

**Files:**
- Create: `tools/validate_docx.py`
- Modify: `crates/rmk-validate/src/main.rs`, `crates/rmk-validate/Cargo.toml` (add `serde_json`)

- [ ] **Step 1: Write `tools/validate_docx.py`** — inspects the built docx with python-docx and prints a JSON result:

```python
"""Validate the built RMK docx against the hard gates. Prints JSON to stdout."""
import json
import sys
from pathlib import Path

from docx import Document
from docx.shared import Mm, Pt

MEMBERS = ["122501039", "122501048", "122501067", "122501078", "122501084", "122501094"]
NAMES = ["Satriyo Nugroho", "Mario Da Costa", "Amelda Putri Zhany Wiguna",
         "Ahmad Ramadhan", "Nida Nur Cahyati", "Priska Putri Parungky"]
CAPTION_MARKERS = [f"Exhibit 13.{n}" for n in range(1, 12)]
EQUATION_MARKERS = ["(13.1)", "(13.2)"]


def all_text(doc):
    parts = [p.text for p in doc.paragraphs]
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                parts.append(cell.text)
    return "\n".join(parts)


def page_count(path):
    try:
        import win32com.client  # type: ignore
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        d = word.Documents.Open(str(Path(path).resolve()), ReadOnly=True)
        n = d.ComputeStatistics(2)  # wdStatisticPages
        d.Close(False)
        word.Quit()
        return n
    except Exception as e:  # noqa: BLE001 — report, don't crash
        return {"error": str(e)}


def main(path):
    doc = Document(path)
    sec = doc.sections[0]
    text = all_text(doc)
    normal = doc.styles["Normal"]
    result = {
        "a4": abs(sec.page_width - Mm(210)) < Mm(0.5) and abs(sec.page_height - Mm(297)) < Mm(0.5),
        "font": normal.font.name == "Calibri",
        "size_12": normal.font.size == Pt(12),
        "line_spacing_1_5": normal.paragraph_format.line_spacing == 1.5,
        "images": len(doc.inline_shapes),
        "images_ok": len(doc.inline_shapes) >= 8,
        "captions_missing": [m for m in CAPTION_MARKERS if m not in text],
        "equations_missing": [m for m in EQUATION_MARKERS if m not in text],
        "identity_missing": [m for m in MEMBERS + NAMES if m not in text],
        "page_count": page_count(path),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
```

- [ ] **Step 2: Rewrite `crates/rmk-validate/src/main.rs`:** add `serde_json = { workspace = true }` and `rmk-audit = { path = "../rmk-audit" }` to its Cargo.toml. Logic: (1) run `python tools/validate_docx.py <docx>` and parse the JSON (`serde_json::Value`); (2) re-run the audit logic (sections=15, concepts 62/62 — reuse `rmk_audit` functions exactly as in the audit binary's strict mode); (3) write `output/VALIDATION-REPORT.md` with: format-gate checklist table (A4/spacing/font/pages/docx/identity, ✓ or ✗ from JSON), exhibit checklist table (each of the 13 manifest ids → anchor section → embedded ✓ — captions/equations from JSON missing-lists must be empty; images ≥ 8), concept-coverage line (62/62 + per-section counts), page count (number, or the COM error + "verify manually in Word"), and the two documented tooling substitutions (vision OCR for tesseract; python-docx bridge for the docx skill). Exit nonzero if any boolean gate is false, any missing-list non-empty, or coverage incomplete. Page count: if JSON returned a number < 8 → fail; if COM error → print warning and leave the report line "page_count: MANUAL CHECK REQUIRED" without failing (the human gate in Phase 5 covers it).
- [ ] **Step 3: Run** `cargo run -p rmk-validate` after a full build → inspect `output/VALIDATION-REPORT.md`.
- [ ] **Step 4: Gates + commit.** `cargo test && cargo clippy --all-targets -- -D warnings && cargo fmt --check`; `git commit -am "feat(rmk-ch13): rmk-validate + docx gate inspection"`

---

## Task 24: Full assembly, strict audit, page-count remediation

- [ ] **Step 1:** `cargo run -p rmk-audit -- --strict` → "sections: 15/15 — concepts covered: 62/62".
- [ ] **Step 2:** `cargo test -- --ignored` (runs `strict_completeness`) → PASS. Then full `cargo test` → all green.
- [ ] **Step 3:** `cargo run -p rmk-build` → final docx.
- [ ] **Step 4:** `cargo run -p rmk-validate` → all gates ✓. **If page_count < 8:** deepen the REFACTOR of the heavy sections (§§2, 6, 7, 8, 13 — more interpretation and read-throughs, never filler), then rebuild and re-validate. Do NOT touch margins/spacing/font to game the count.
- [ ] **Step 5:** Open the docx in Word AND LibreOffice; visually confirm: cover identity table, every exhibit adjacent to its explanation, no exhibit split awkwardly across a page break, captions beneath every exhibit.
- [ ] **Step 6:** Commit: `git commit -am "feat(rmk-ch13): full RMK assembly passing all gates"`. Hand off to Phase 5 (`finishing-a-development-branch` + two-stage content review per section is performed during Tasks 6–21; Phase 5 runs the final review + delivery options).

---

## Self-review notes (spec → plan)

- Spec §1 filename → Task 22 default arg + Task 24. Spec §2 gates → bridge `base_doc` + Task 23 checks. Spec §3 voice → Step B directives + rubric `depth_check`. Spec §4 exhibit policy → Tasks 1–3 (crops exclude printed titles; captions from manifest; 6.25″; adjacency enforced by directives placed mid-argument + Task 24 Step 5 visual check). Spec §5 structure/weights → Tasks 6–21 target lengths + synthesis tables in §5/§7/§12 directives. Spec §6 identity → Task 6 + Task 23. Spec §7 architecture → Tasks 1, 2, 5, 22, 23. Spec §8 verification → rmk-audit tests (incremental + strict), two-stage review during Phase 4 execution, Task 24.
- All 62 concepts assigned across Tasks 7–21 rubrics: 3+7+2+8+4+4+6+7+1+4+2+2+5+3+4 = 62. ✓
- All 13 manifest ids anchored: eq-13-1 + 13.1 (Task 8); 13.2 + 13.3 (Task 12); 13.4 (Task 13); 13.5 (Task 14); 13.6 (Task 17); eq-13-2 + 13.7–13.11 (Task 19). ✓
- Type consistency: `Exhibit.reset_text/reset_table/label` defined Task 1, consumed Tasks 5/22; `Rubric.required_keywords` defined Task 1, consumed Task 5; `parse_doc`/`workspace_root` defined Task 5, consumed Tasks 22/23; `Block`/`Run`/`compile_body` defined Task 22 lib, consumed Task 22 main. ✓
