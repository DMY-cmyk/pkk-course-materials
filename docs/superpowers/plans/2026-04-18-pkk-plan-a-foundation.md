# MNK202 — Plan A: Foundation + Pipeline

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete Rust `devassist` pipeline, Design B CSS system, and Tera HTML templates so that `cargo run -- all` renders all 70 course deliverables from stub markdown content.

**Architecture:** Rust CLI (`clap`) reads `configs/mapping.toml` for week metadata, parses markdown via `pulldown-cmark`, renders through `tera` templates, and writes self-contained HTML output files. CSS assets are copied alongside each output. Content generation (Plan B) is dispatched only after this pipeline is verified end-to-end.

**Tech Stack:** Rust 2021 edition, pulldown-cmark 0.11, tera 1.19, clap 4 (derive), serde 1 + toml 0.8, walkdir 2

**Spec:** `docs/superpowers/specs/2026-04-18-pkk-fresh-rebuild-design.md`

---

## File Map

```
Dev Assistant/
├── Cargo.toml                          ← crate manifest
├── src/
│   ├── main.rs                         ← CLI entry point
│   ├── config.rs                       ← MappingConfig, WeekConfig, load_config()
│   ├── markdown.rs                     ← render_markdown()
│   ├── renderer.rs                     ← build_context(), render_template()
│   ├── builder.rs                      ← build_week(), build_weeks_range(), build_all()
│   └── bundle.rs                       ← build_visual_companion(), build_master_bundle()
├── configs/
│   └── mapping.toml                    ← all 14 week metadata entries
├── templates/
│   ├── base.html.tera                  ← shared week hero + tab nav + sidebar shell
│   ├── study-guide.html.tera           ← extends base, study guide body
│   ├── summary.html.tera               ← extends base, main summary body
│   ├── company-example.html.tera       ← extends base, company example body
│   ├── review-sheet.html.tera          ← extends base, review sheet body
│   ├── exercises.html.tera             ← extends base, exercises body
│   ├── visual-companion.html.tera      ← standalone, week index + navigation
│   └── master-bundle.html.tera         ← standalone, all weeks concatenated
├── assets/
│   ├── css/
│   │   ├── base.css                    ← CSS variables, typography, Inter font-face
│   │   ├── screen.css                  ← week hero, body grid, cards, sidebar, chips
│   │   └── print.css                   ← @media print overrides, page-break rules
│   └── fonts/
│       └── inter-v.woff2               ← Inter Variable font (self-hosted)
└── content/
    └── week-NN/                        ← stub files created in Task 9
        ├── study-guide.md
        ├── summary.md
        ├── company-example.md
        ├── review-sheet.md
        └── exercises.md

course-materials/outputs/               ← written by pipeline, NOT manually edited
├── Study Guide - Aid/Week NN/
│   ├── index.html
│   ├── css/ (base.css, screen.css, print.css)
│   └── fonts/inter-v.woff2
├── Main Summary - Ebook/Week NN/       ← same structure
├── Indonesian Company Examples/Week NN/
│   ├── examples.html                   ← note: examples.html not index.html
│   ├── css/
│   └── fonts/
├── Review Sheet/Week NN/               ← same structure as Study Guide
├── Exercises/Week NN/                  ← same structure
├── Visual Companion/
│   ├── index.html
│   ├── css/
│   └── fonts/
└── Master Print Bundle/
    └── course-companion.html           ← single self-contained file, all CSS inlined
```

---

## Task 1: Git History Reset

**Files:**
- Delete: `.git/` (entire directory)
- Create: `.gitignore`
- Run: `git init`, initial commit

- [ ] **Step 1: Confirm working directory**

```bash
cd "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat"
pwd
ls
```

Expected: root directory with PDF files, docs/, syllabus PDF visible.

- [ ] **Step 2: Delete git history**

```bash
rm -rf .git
```

Expected: no output. `.git` folder is gone.

- [ ] **Step 3: Write .gitignore**

Write to `.gitignore`:

```gitignore
# Rust build artifacts
Dev Assistant/target/

# OS
.DS_Store
Thumbs.db

# Superpowers temp files
.superpowers/

# Node (if ever needed)
node_modules/

# Logs
*.log
```

- [ ] **Step 4: Init fresh repo and commit**

```bash
git init
git add .gitignore docs/superpowers/specs/2026-04-18-pkk-fresh-rebuild-design.md docs/superpowers/plans/2026-04-18-pkk-plan-a-foundation.md
git commit -m "chore: fresh start — MNK202 new build 2026-04-18

Spec: docs/superpowers/specs/2026-04-18-pkk-fresh-rebuild-design.md
Plan A: docs/superpowers/plans/2026-04-18-pkk-plan-a-foundation.md"
```

Expected: `[main (root-commit) xxxxxxx] chore: fresh start`

---

## Task 2: Rust Crate Scaffold

**Files:**
- Create: `Dev Assistant/Cargo.toml`
- Create: `Dev Assistant/src/main.rs`
- Create: `Dev Assistant/src/config.rs` (skeleton)
- Create: `Dev Assistant/src/markdown.rs` (skeleton)
- Create: `Dev Assistant/src/renderer.rs` (skeleton)
- Create: `Dev Assistant/src/builder.rs` (skeleton)
- Create: `Dev Assistant/src/bundle.rs` (skeleton)

- [ ] **Step 1: Create Cargo.toml**

Write to `Dev Assistant/Cargo.toml`:

```toml
[package]
name = "devassist"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "devassist"
path = "src/main.rs"

[dependencies]
pulldown-cmark = "0.11"
tera = { version = "1.19", default-features = false }
clap = { version = "4", features = ["derive"] }
serde = { version = "1", features = ["derive"] }
toml = "0.8"
walkdir = "2"
```

- [ ] **Step 2: Create src/main.rs**

Write to `Dev Assistant/src/main.rs`:

```rust
mod config;
mod markdown;
mod renderer;
mod builder;
mod bundle;

use clap::{Parser, Subcommand};
use tera::Tera;
use std::path::Path;

#[derive(Parser)]
#[command(name = "devassist", about = "MNK202 course content builder")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Build a single week (1–14)
    Week {
        number: u8,
    },
    /// Build a range of weeks, e.g. "1-7"
    Weeks {
        range: String,
    },
    /// Build all 14 weeks
    All,
    /// Build the Visual Companion web app
    VisualCompanion,
    /// Build the Master Print Bundle
    MasterBundle,
}

fn main() {
    let cli = Cli::parse();

    let manifest_dir = Path::new(env!("CARGO_MANIFEST_DIR"));
    let templates_glob = manifest_dir.join("templates/**/*.tera");
    let templates_str = templates_glob.to_str().unwrap();
    let tera = Tera::new(templates_str).expect("Failed to load Tera templates");

    let config_path = manifest_dir.join("configs/mapping.toml");
    let config_path_str = config_path.to_str().unwrap();

    let content_dir = manifest_dir.join("content");
    let content_dir_str = content_dir.to_str().unwrap();

    let assets_dir = manifest_dir.join("assets");
    let assets_dir_str = assets_dir.to_str().unwrap();

    // Output root is two levels up from Dev Assistant/
    let output_root = manifest_dir
        .parent().unwrap()  // repo root
        .join("course-materials/outputs");
    let output_root_str = output_root.to_str().unwrap();

    match cli.command {
        Commands::Week { number } => {
            println!("Building Week {:02}...", number);
            builder::build_week(number, &tera, config_path_str, content_dir_str, assets_dir_str, output_root_str);
        }
        Commands::Weeks { range } => {
            println!("Building weeks {}...", range);
            builder::build_weeks_range(&range, &tera, config_path_str, content_dir_str, assets_dir_str, output_root_str);
        }
        Commands::All => {
            println!("Building all 14 weeks...");
            builder::build_all(&tera, config_path_str, content_dir_str, assets_dir_str, output_root_str);
        }
        Commands::VisualCompanion => {
            println!("Building Visual Companion...");
            bundle::build_visual_companion(&tera, config_path_str, assets_dir_str, output_root_str);
        }
        Commands::MasterBundle => {
            println!("Building Master Bundle...");
            bundle::build_master_bundle(config_path_str, output_root_str);
        }
    }

    println!("Done.");
}
```

- [ ] **Step 3: Create skeleton modules**

Write `Dev Assistant/src/config.rs`:
```rust
// populated in Task 3
```

Write `Dev Assistant/src/markdown.rs`:
```rust
// populated in Task 4
```

Write `Dev Assistant/src/renderer.rs`:
```rust
// populated in Task 5
```

Write `Dev Assistant/src/builder.rs`:
```rust
// populated in Task 8
```

Write `Dev Assistant/src/bundle.rs`:
```rust
// populated in Task 9
```

- [ ] **Step 4: Verify crate compiles (skeleton)**

```bash
cd "Dev Assistant"
cargo check 2>&1
```

Expected: errors about empty modules (that's OK at this stage — just confirm `cargo check` runs without toolchain errors). If Rust is not installed, run `rustup show` and install if needed.

- [ ] **Step 5: Commit scaffold**

```bash
cd ..
git add "Dev Assistant/"
git commit -m "chore(rust): crate scaffold — devassist CLI skeleton"
```

---

## Task 3: Config Module + mapping.toml

**Files:**
- Write: `Dev Assistant/src/config.rs`
- Write: `Dev Assistant/configs/mapping.toml`

- [ ] **Step 1: Write config.rs**

Write to `Dev Assistant/src/config.rs`:

```rust
use serde::Deserialize;
use std::collections::HashMap;

#[derive(Deserialize, Debug, Clone)]
pub struct MappingConfig {
    pub weeks: HashMap<u8, WeekConfig>,
}

#[derive(Deserialize, Debug, Clone)]
pub struct WeekConfig {
    pub title: String,
    pub title_en: String,
    pub phase: String,
    pub core_readings: Vec<String>,
    pub supplementary: Vec<String>,
    pub company_name: String,
    pub company_ticker: String,
    pub company_exchange: String,
}

pub fn load_config(path: &str) -> Result<MappingConfig, Box<dyn std::error::Error>> {
    let content = std::fs::read_to_string(path)
        .map_err(|e| format!("Cannot read config {}: {}", path, e))?;
    let config: MappingConfig = toml::from_str(&content)
        .map_err(|e| format!("Cannot parse config {}: {}", path, e))?;
    Ok(config)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_load_config_w1() {
        let manifest = env!("CARGO_MANIFEST_DIR");
        let path = format!("{}/configs/mapping.toml", manifest);
        let config = load_config(&path).unwrap();
        let w1 = config.weeks.get(&1).unwrap();
        assert_eq!(w1.company_ticker, "TLKM");
        assert_eq!(w1.phase, "pre-uts");
    }

    #[test]
    fn test_all_14_weeks_present() {
        let manifest = env!("CARGO_MANIFEST_DIR");
        let path = format!("{}/configs/mapping.toml", manifest);
        let config = load_config(&path).unwrap();
        for w in 1u8..=14 {
            assert!(config.weeks.contains_key(&w), "Week {} missing from config", w);
        }
    }
}
```

- [ ] **Step 2: Write mapping.toml**

Write to `Dev Assistant/configs/mapping.toml`:

```toml
[weeks.1]
title = "Pengantar & Perspektif Historis Akuntansi"
title_en = "Introduction and Historical Perspective of Accounting"
phase = "pre-uts"
core_readings = ["Wolk Ch.1 §1.1–1.4", "Silabus MNK202"]
supplementary = ["IASB CF 2018", "Sejarah BAPEPAM-LK", "TLKM AR 2024"]
company_name = "Telkom Indonesia"
company_ticker = "TLKM"
company_exchange = "IDX"

[weeks.2]
title = "Kontrak Efisien, Asimetri Informasi & Pengukuran"
title_en = "Efficient Contracting, Information Asymmetry and Measurement"
phase = "pre-uts"
core_readings = ["Wolk Ch.1", "Wolk Ch.2"]
supplementary = ["Jensen & Meckling (1976)", "PSAK 1 rev.2023", "BBRI AR 2025"]
company_name = "Bank Rakyat Indonesia"
company_ticker = "BBRI"
company_exchange = "IDX"

[weeks.3]
title = "Perkembangan Struktur Kelembagaan Akuntansi Keuangan"
title_en = "Development of the Institutional Structure of Financial Accounting"
phase = "pre-uts"
core_readings = ["Wolk Ch.3"]
supplementary = ["Peraturan OJK", "Sejarah DSAK-IAI", "GIAA AR 2024"]
company_name = "Garuda Indonesia"
company_ticker = "GIAA"
company_exchange = "IDX"

[weeks.4]
title = "Postulat, Prinsip, dan Konsep Akuntansi"
title_en = "Postulates, Principles, and Concepts"
phase = "pre-uts"
core_readings = ["Wolk Ch.5"]
supplementary = ["PSAK 72", "PSAK 16", "ASII AR 2025"]
company_name = "Astra International"
company_ticker = "ASII"
company_exchange = "IDX"

[weeks.5]
title = "Kerangka Konseptual FASB / IASB"
title_en = "The FASB's Conceptual Framework"
phase = "pre-uts"
core_readings = ["Wolk Ch.7"]
supplementary = ["IASB CF 2018 (lengkap)", "Kerangka Konseptual IAI", "UNVR AR 2024"]
company_name = "Unilever Indonesia"
company_ticker = "UNVR"
company_exchange = "IDX"

[weeks.6]
title = "Kegunaan Informasi Akuntansi bagi Investor & Kreditur"
title_en = "Usefulness of Accounting Information to Investors and Creditors"
phase = "pre-uts"
core_readings = ["Wolk Ch.8"]
supplementary = ["Scott Ch.3 (supp.)", "Ohlson (1995)", "PSAK 71", "BBCA AR 2025"]
company_name = "Bank Central Asia"
company_ticker = "BBCA"
company_exchange = "IDX"

[weeks.7]
title = "Keseragaman dan Pengungkapan: Arah Kebijakan Standar"
title_en = "Uniformity and Disclosure: Some Policy-Making Directions"
phase = "pre-uts"
core_readings = ["Wolk Ch.9"]
supplementary = ["PSAK 5 (segmen operasi)", "PSAK 7 (transaksi pihak berelasi)", "ICBP AR 2024"]
company_name = "Indofood CBP Sukses Makmur"
company_ticker = "ICBP"
company_exchange = "IDX"

[weeks.8]
title = "Neraca / Laporan Posisi Keuangan"
title_en = "The Balance Sheet"
phase = "post-uts"
core_readings = ["Wolk Ch.11"]
supplementary = ["PSAK 71 ECL", "PSAK 68 (nilai wajar)", "BBCA AR 2025"]
company_name = "Bank Central Asia"
company_ticker = "BBCA"
company_exchange = "IDX"

[weeks.9]
title = "Laporan Laba Rugi & Kualitas Laba"
title_en = "The Income Statement"
phase = "post-uts"
core_readings = ["Wolk Ch.12"]
supplementary = ["PSAK 72 (pengakuan pendapatan)", "PSAK 24 (imbalan kerja)", "UNVR AR 2024"]
company_name = "Unilever Indonesia"
company_ticker = "UNVR"
company_exchange = "IDX"

[weeks.10]
title = "Laporan Arus Kas & Kualitas Akrual"
title_en = "Statement of Cash Flows"
phase = "post-uts"
core_readings = ["Wolk Ch.13"]
supplementary = ["PSAK 2 (laporan arus kas)", "Dechow (1994)", "TLKM AR 2024"]
company_name = "Telkom Indonesia"
company_ticker = "TLKM"
company_exchange = "IDX"

[weeks.11]
title = "Pasar Sekuritas Efisien (EMH)"
title_en = "Efficient Securities Markets"
phase = "post-uts"
core_readings = ["Scott Ch.4"]
supplementary = ["Fama (1970)", "Fama (1991)", "Data harga IDX BBRI", "BBRI AR 2025"]
company_name = "Bank Rakyat Indonesia"
company_ticker = "BBRI"
company_exchange = "IDX"

[weeks.12]
title = "Manajemen Laba (Earnings Management)"
title_en = "Earnings Management"
phase = "post-uts"
core_readings = ["Scott Ch.11"]
supplementary = ["Healy & Wahlen (1999)", "Jones (1991)", "GIAA AR 2024"]
company_name = "Garuda Indonesia"
company_ticker = "GIAA"
company_exchange = "IDX"

[weeks.13]
title = "Presentasi Term Paper (Sesi 1)"
title_en = "Term Paper Presentation — Session 1"
phase = "post-uts"
core_readings = ["Journal papers (per kelompok)"]
supplementary = ["Panduan UAS", "Rubrik presentasi"]
company_name = "Student-selected"
company_ticker = "—"
company_exchange = "—"

[weeks.14]
title = "Presentasi Term Paper (Sesi 2) & Review UAS"
title_en = "Term Paper Presentation — Session 2 & UAS Review"
phase = "post-uts"
core_readings = ["Journal papers (per kelompok)"]
supplementary = ["Review komprehensif W1–W12", "Peta framework UAS"]
company_name = "Student-selected"
company_ticker = "—"
company_exchange = "—"
```

- [ ] **Step 3: Run config tests**

```bash
cd "Dev Assistant"
cargo test config 2>&1
```

Expected:
```
test config::tests::test_load_config_w1 ... ok
test config::tests::test_all_14_weeks_present ... ok

test result: ok. 2 passed
```

- [ ] **Step 4: Commit**

```bash
cd ..
git add "Dev Assistant/src/config.rs" "Dev Assistant/configs/mapping.toml"
git commit -m "feat(config): week mapping config — 14 weeks, TOML parsing, tests pass"
```

---

## Task 4: Markdown Rendering Module

**Files:**
- Write: `Dev Assistant/src/markdown.rs`

- [ ] **Step 1: Write markdown.rs**

Write to `Dev Assistant/src/markdown.rs`:

```rust
use pulldown_cmark::{html, Options, Parser};

pub fn render_markdown(input: &str) -> String {
    let mut options = Options::empty();
    options.insert(Options::ENABLE_TABLES);
    options.insert(Options::ENABLE_STRIKETHROUGH);
    options.insert(Options::ENABLE_HEADING_ATTRIBUTES);
    let parser = Parser::new_ext(input, options);
    let mut html_output = String::new();
    html::push_html(&mut html_output, parser);
    html_output
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_heading() {
        let result = render_markdown("# Hello");
        assert!(result.contains("<h1>Hello</h1>"));
    }

    #[test]
    fn test_bold() {
        let result = render_markdown("**bold**");
        assert!(result.contains("<strong>bold</strong>"));
    }

    #[test]
    fn test_table() {
        let md = "| A | B |\n|---|---|\n| 1 | 2 |";
        let result = render_markdown(md);
        assert!(result.contains("<table>"));
        assert!(result.contains("<td>1</td>"));
    }

    #[test]
    fn test_empty_input() {
        let result = render_markdown("");
        assert_eq!(result, "");
    }
}
```

- [ ] **Step 2: Run markdown tests**

```bash
cd "Dev Assistant"
cargo test markdown 2>&1
```

Expected: 4 tests pass.

- [ ] **Step 3: Commit**

```bash
cd ..
git add "Dev Assistant/src/markdown.rs"
git commit -m "feat(markdown): pulldown-cmark renderer with table + heading support"
```

---

## Task 5: Renderer Module

**Files:**
- Write: `Dev Assistant/src/renderer.rs`

- [ ] **Step 1: Write renderer.rs**

Write to `Dev Assistant/src/renderer.rs`:

```rust
use tera::{Context, Tera};
use crate::config::WeekConfig;

pub struct DeliverableMeta {
    pub type_key: &'static str,    // "study-guide"
    pub source_file: &'static str, // "study-guide.md"
    pub output_folder: &'static str, // "Study Guide - Aid"
    pub output_file: &'static str,   // "index.html"
    pub label: &'static str,         // "📖 Study Guide"
    pub template: &'static str,      // "study-guide.html.tera"
}

pub const DELIVERABLES: &[DeliverableMeta] = &[
    DeliverableMeta {
        type_key: "study-guide",
        source_file: "study-guide.md",
        output_folder: "Study Guide - Aid",
        output_file: "index.html",
        label: "📖 Study Guide",
        template: "study-guide.html.tera",
    },
    DeliverableMeta {
        type_key: "summary",
        source_file: "summary.md",
        output_folder: "Main Summary - Ebook",
        output_file: "index.html",
        label: "📄 Main Summary",
        template: "summary.html.tera",
    },
    DeliverableMeta {
        type_key: "company-example",
        source_file: "company-example.md",
        output_folder: "Indonesian Company Examples",
        output_file: "examples.html",
        label: "🏢 Company Example",
        template: "company-example.html.tera",
    },
    DeliverableMeta {
        type_key: "review-sheet",
        source_file: "review-sheet.md",
        output_folder: "Review Sheet",
        output_file: "index.html",
        label: "📋 Review Sheet",
        template: "review-sheet.html.tera",
    },
    DeliverableMeta {
        type_key: "exercises",
        source_file: "exercises.md",
        output_folder: "Exercises",
        output_file: "index.html",
        label: "✏️ Exercises",
        template: "exercises.html.tera",
    },
];

pub fn build_context(
    week: u8,
    config: &WeekConfig,
    content_html: &str,
    meta: &DeliverableMeta,
    all_weeks: &[(u8, String)],
) -> Context {
    let mut ctx = Context::new();
    ctx.insert("week_num", &week);
    ctx.insert("week_pad", &format!("{:02}", week));
    ctx.insert("title", &config.title);
    ctx.insert("title_en", &config.title_en);
    ctx.insert("phase_label", &if config.phase == "pre-uts" { "Pra-UTS" } else { "Pasca-UTS" });
    ctx.insert("phase_class", &config.phase);
    ctx.insert("core_readings", &config.core_readings);
    ctx.insert("supplementary", &config.supplementary);
    ctx.insert("company_name", &config.company_name);
    ctx.insert("company_ticker", &config.company_ticker);
    ctx.insert("company_exchange", &config.company_exchange);
    ctx.insert("content_html", content_html);
    ctx.insert("deliverable_type", meta.type_key);
    ctx.insert("deliverable_label", meta.label);
    ctx.insert("deliverables", &DELIVERABLES.iter().map(|d| d.label).collect::<Vec<_>>());
    ctx.insert("all_weeks", all_weeks);
    ctx
}

pub fn render_template(tera: &Tera, template_name: &str, ctx: &Context) -> String {
    tera.render(template_name, ctx)
        .unwrap_or_else(|e| panic!("Template '{}' render failed: {}", template_name, e))
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::config::WeekConfig;

    fn stub_config() -> WeekConfig {
        WeekConfig {
            title: "Test Minggu".into(),
            title_en: "Test Week".into(),
            phase: "pre-uts".into(),
            core_readings: vec!["Wolk Ch.1".into()],
            supplementary: vec!["PSAK 1".into()],
            company_name: "Telkom Indonesia".into(),
            company_ticker: "TLKM".into(),
            company_exchange: "IDX".into(),
        }
    }

    #[test]
    fn test_context_phase_label_pre_uts() {
        let config = stub_config();
        let ctx = build_context(1, &config, "<p>content</p>", &DELIVERABLES[0], &[]);
        let label = ctx.get("phase_label").unwrap();
        assert!(label.to_string().contains("Pra-UTS"));
    }

    #[test]
    fn test_context_phase_label_post_uts() {
        let mut config = stub_config();
        config.phase = "post-uts".into();
        let ctx = build_context(8, &config, "", &DELIVERABLES[0], &[]);
        let label = ctx.get("phase_label").unwrap();
        assert!(label.to_string().contains("Pasca-UTS"));
    }

    #[test]
    fn test_week_pad_single_digit() {
        let config = stub_config();
        let ctx = build_context(3, &config, "", &DELIVERABLES[0], &[]);
        let pad = ctx.get("week_pad").unwrap();
        assert!(pad.to_string().contains("03"));
    }
}
```

- [ ] **Step 2: Run renderer tests**

```bash
cd "Dev Assistant"
cargo test renderer 2>&1
```

Expected: 3 tests pass.

- [ ] **Step 3: Commit**

```bash
cd ..
git add "Dev Assistant/src/renderer.rs"
git commit -m "feat(renderer): Tera context builder + DELIVERABLES registry"
```

---

## Task 6: Design B CSS System

**Files:**
- Write: `Dev Assistant/assets/css/base.css`
- Write: `Dev Assistant/assets/css/screen.css`
- Write: `Dev Assistant/assets/css/print.css`
- Note: `Dev Assistant/assets/fonts/inter-v.woff2` — download Inter Variable font from https://rsms.me/inter/ (or use system-ui fallback if not available)

- [ ] **Step 1: Write base.css**

Write to `Dev Assistant/assets/css/base.css`:

```css
/* ── MNK202 Design B — Base: variables, typography, font-face ── */

@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
  src: url('../fonts/inter-v.woff2') format('woff2');
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  /* Palette */
  --c-bg:          #f1f5f9;
  --c-surface:     #ffffff;
  --c-border:      #e2e8f0;
  --c-border-soft: #f1f5f9;
  --c-text:        #0f172a;
  --c-text-2:      #374151;
  --c-text-3:      #64748b;
  --c-text-muted:  #94a3b8;

  /* Brand accent */
  --c-blue:        #2563eb;
  --c-blue-soft:   #eff6ff;
  --c-purple:      #7c3aed;
  --c-purple-soft: #faf5ff;
  --c-cyan:        #0891b2;
  --c-green:       #16a34a;
  --c-green-soft:  #f0fdf4;
  --c-amber:       #b45309;
  --c-amber-soft:  #fffbeb;
  --c-red:         #c2410c;
  --c-red-soft:    #fff7ed;

  /* Concept box colors */
  --cb-blue-bg:   #eff6ff; --cb-blue-border: #bfdbfe; --cb-blue-h: #1d4ed8;
  --cb-purple-bg: #faf5ff; --cb-purple-border: #ddd6fe; --cb-purple-h: #7c3aed;
  --cb-green-bg:  #f0fdf4; --cb-green-border: #bbf7d0; --cb-green-h: #15803d;
  --cb-amber-bg:  #fffbeb; --cb-amber-border: #fde68a; --cb-amber-h: #b45309;

  /* Gradient accent bar */
  --grad-accent: linear-gradient(90deg, #2563eb 0%, #7c3aed 50%, #0891b2 100%);

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;

  /* Radii */
  --r-sm: 4px;
  --r-md: 6px;
  --r-lg: 10px;
  --r-pill: 20px;

  /* Shadows */
  --shadow-card: 0 1px 3px rgba(0,0,0,.08);
  --shadow-md:   0 4px 12px rgba(0,0,0,.1);

  /* Typography */
  --font-sans: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
  --font-mono: 'Consolas', 'Menlo', monospace;
}

body {
  font-family: var(--font-sans);
  background: var(--c-bg);
  color: var(--c-text);
  font-size: 14px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

h1 { font-size: 26px; font-weight: 800; line-height: 1.2; }
h2 { font-size: 20px; font-weight: 700; line-height: 1.3; }
h3 { font-size: 15px; font-weight: 700; line-height: 1.4; }
h4 { font-size: 13px; font-weight: 700; }
h5 { font-size: 13px; font-weight: 600; }

p  { font-size: 13px; color: var(--c-text-2); line-height: 1.7; margin-bottom: 12px; }
p:last-child { margin-bottom: 0; }

strong { font-weight: 700; color: var(--c-text); }
em     { font-style: italic; }

a { color: var(--c-blue); text-decoration: none; }
a:hover { text-decoration: underline; }

table { width: 100%; border-collapse: collapse; margin-bottom: 16px; }
thead th { background: var(--c-text); color: #fff; font-size: 11px; font-weight: 700;
           text-transform: uppercase; letter-spacing: .8px; padding: 10px 12px; text-align: left; }
tbody td { padding: 10px 12px; font-size: 12px; border-bottom: 1px solid var(--c-border-soft); }
tbody tr:hover { background: var(--c-bg); }

ul, ol { padding-left: 20px; margin-bottom: 12px; }
li     { font-size: 13px; color: var(--c-text-2); line-height: 1.6; margin-bottom: 4px; }

code { font-family: var(--font-mono); font-size: 12px; background: var(--c-bg);
       padding: 2px 5px; border-radius: var(--r-sm); border: 1px solid var(--c-border); }

pre  { background: var(--c-text); color: #e2e8f0; padding: 16px; border-radius: var(--r-md);
       overflow-x: auto; margin-bottom: 16px; }
pre code { background: none; border: none; padding: 0; color: inherit; font-size: 12px; }

blockquote { border-left: 3px solid var(--c-blue); background: var(--c-bg); padding: 12px 16px;
             border-radius: 0 var(--r-md) var(--r-md) 0; margin-bottom: 14px; }
blockquote p { color: #1e3a5f; font-style: italic; margin: 0; }

hr { border: none; border-top: 1px solid var(--c-border); margin: 20px 0; }
```

- [ ] **Step 2: Write screen.css**

Write to `Dev Assistant/assets/css/screen.css`:

```css
/* ── MNK202 Design B — Screen: layout, hero, cards, sidebar ── */

/* ── Week Hero ── */
.week-hero {
  background: var(--c-surface);
  border-bottom: 1px solid var(--c-border);
  padding: var(--space-xl) var(--space-xl) 0;
  position: relative;
  overflow: hidden;
}
.week-hero::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: var(--grad-accent);
}
.hero-top { display: flex; justify-content: space-between; align-items: flex-start; gap: var(--space-lg); }
.hero-badge { display: flex; align-items: center; gap: var(--space-sm); margin-bottom: 10px; }

.pill { font-size: 11px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;
        padding: 4px 12px; border-radius: var(--r-pill); }
.pill-week     { background: var(--c-blue-soft); color: var(--c-blue); }
.pill-pre-uts  { background: var(--c-blue-soft); color: var(--c-blue); }
.pill-post-uts { background: var(--c-green-soft); color: var(--c-green); }

.hero-title    { font-size: 26px; font-weight: 800; color: var(--c-text); line-height: 1.2; max-width: 620px; margin-bottom: 6px; }
.hero-subtitle { font-size: 14px; color: var(--c-text-3); max-width: 540px; line-height: 1.6; }
.hero-watermark { font-size: 72px; font-weight: 900; color: var(--c-border); line-height: 1; font-variant-numeric: tabular-nums; }

/* Reference chips */
.ref-chips { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 14px; }
.chip { display: inline-block; font-size: 10px; font-weight: 700; padding: 3px 10px;
        border-radius: var(--r-sm); border: 1px solid; }
.chip-book   { background: var(--c-purple-soft); color: var(--c-purple); border-color: #ddd6fe; }
.chip-psak   { background: var(--c-red-soft);    color: var(--c-red);    border-color: #fed7aa; }
.chip-co     { background: var(--c-green-soft);  color: var(--c-green);  border-color: #bbf7d0; }
.chip-supp   { background: var(--c-bg);          color: var(--c-text-3); border-color: var(--c-border); }

/* Tab nav */
.tab-nav { display: flex; margin-top: var(--space-lg); border-top: 1px solid var(--c-border); }
.tab     { padding: 12px 18px; font-size: 12px; font-weight: 600; color: var(--c-text-3);
           border-bottom: 2px solid transparent; cursor: pointer; white-space: nowrap; }
.tab.active { color: var(--c-blue); border-bottom-color: var(--c-blue); }

/* ── Body Layout ── */
.body-grid {
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: var(--space-lg);
  padding: var(--space-xl) var(--space-xl);
  max-width: 1200px;
}

/* ── Section Cards ── */
.section-card { background: var(--c-surface); border-radius: var(--r-lg); border: 1px solid var(--c-border);
                box-shadow: var(--shadow-card); overflow: hidden; margin-bottom: var(--space-lg); }
.section-header { padding: 14px 20px; border-bottom: 1px solid var(--c-border-soft);
                  display: flex; align-items: center; gap: 10px; }
.section-icon { width: 28px; height: 28px; border-radius: var(--r-md);
                display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; }
.icon-blue   { background: var(--c-blue-soft); }
.icon-purple { background: var(--c-purple-soft); }
.icon-green  { background: var(--c-green-soft); }
.icon-amber  { background: var(--c-amber-soft); }
.section-title { font-size: 13px; font-weight: 700; color: var(--c-text); }
.section-sub   { font-size: 11px; color: var(--c-text-muted); margin-top: 1px; }
.section-body  { padding: 20px; }

/* Concept grid */
.concept-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 18px; }
.concept-box  { border-radius: var(--r-md); padding: 14px; border: 1px solid; }
.cb-blue   { background: var(--cb-blue-bg);   border-color: var(--cb-blue-border); }
.cb-purple { background: var(--cb-purple-bg); border-color: var(--cb-purple-border); }
.cb-green  { background: var(--cb-green-bg);  border-color: var(--cb-green-border); }
.cb-amber  { background: var(--cb-amber-bg);  border-color: var(--cb-amber-border); }
.cb-blue   h4 { color: var(--cb-blue-h);   font-size: 12px; margin-bottom: 6px; }
.cb-purple h4 { color: var(--cb-purple-h); font-size: 12px; margin-bottom: 6px; }
.cb-green  h4 { color: var(--cb-green-h);  font-size: 12px; margin-bottom: 6px; }
.cb-amber  h4 { color: var(--cb-amber-h);  font-size: 12px; margin-bottom: 6px; }
.concept-box p { font-size: 12px; line-height: 1.6; color: var(--c-text-2); margin: 0; }

/* Flow diagram */
.flow-row   { display: flex; align-items: center; overflow-x: auto; margin-bottom: 16px; gap: 0; }
.flow-node  { background: var(--c-surface); border: 1.5px solid var(--c-blue); border-radius: var(--r-md);
              padding: 10px 14px; text-align: center; flex-shrink: 0; min-width: 110px; }
.flow-node h5 { font-size: 11px; font-weight: 700; color: var(--c-blue); margin-bottom: 3px; }
.flow-node p  { font-size: 10px; color: var(--c-text-3); line-height: 1.4; margin: 0; }
.flow-arrow   { font-size: 18px; color: var(--c-text-muted); padding: 0 6px; flex-shrink: 0; }

/* Quote block */
.quote-block { border-left: 3px solid var(--c-blue); background: var(--c-bg);
               padding: 14px 18px; border-radius: 0 var(--r-md) var(--r-md) 0; margin-bottom: 16px; }
.quote-block p       { color: #1e3a5f; font-style: italic; }
.quote-source { font-size: 11px; color: var(--c-text-3); margin-top: 6px; font-weight: 600; font-style: normal; }

/* Reading steps */
.read-steps { list-style: none; padding: 0; }
.read-step  { display: flex; gap: 14px; align-items: flex-start;
              padding: 12px 0; border-bottom: 1px solid var(--c-border-soft); }
.read-step:last-child { border-bottom: none; }
.step-num { width: 24px; height: 24px; background: var(--c-blue); color: #fff; border-radius: 50%;
            display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700;
            flex-shrink: 0; margin-top: 1px; }
.step-text h5 { font-size: 13px; font-weight: 600; color: var(--c-text); margin-bottom: 3px; }
.step-text p  { font-size: 12px; color: var(--c-text-3); line-height: 1.5; margin: 0; }
.step-tag { display: inline-block; font-size: 10px; font-weight: 600; padding: 2px 8px;
            border-radius: var(--r-sm); background: var(--c-blue-soft); color: var(--c-blue); margin-top: 5px; }

/* ── Sidebar ── */
.sidebar { display: flex; flex-direction: column; gap: var(--space-md); }
.side-card { background: var(--c-surface); border-radius: var(--r-lg); border: 1px solid var(--c-border);
             box-shadow: var(--shadow-card); overflow: hidden; }
.side-header { padding: 12px 16px; font-size: 11px; font-weight: 700; letter-spacing: 1px;
               text-transform: uppercase; color: var(--c-text-3); border-bottom: 1px solid var(--c-border-soft); }
.side-body { padding: 14px 16px; }

/* Deliverable grid */
.deliv-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.deliv-btn  { display: flex; flex-direction: column; align-items: center; padding: 12px 8px;
              border-radius: var(--r-md); border: 1.5px solid var(--c-border); gap: 6px; text-align: center; }
.deliv-btn.active { border-color: var(--c-blue); background: var(--c-blue-soft); }
.deliv-btn span  { font-size: 11px; font-weight: 600; color: var(--c-text-2); }
.deliv-btn.active span { color: var(--c-blue); }
.deliv-btn-full { grid-column: 1 / -1; }

/* Company card */
.co-logo { width: 44px; height: 44px; border-radius: var(--r-md); display: flex; align-items: center;
           justify-content: center; color: #fff; font-weight: 800; font-size: 13px; flex-shrink: 0; }
.co-name { font-size: 14px; font-weight: 700; color: var(--c-text); }
.co-sub  { font-size: 11px; color: var(--c-text-3); margin-top: 2px; }
.co-ticker { display: inline-block; background: var(--c-blue-soft); color: var(--c-blue);
             font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: var(--r-sm); margin-top: 4px; }

.metric-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 12px 0; }
.metric-box  { background: var(--c-bg); border-radius: var(--r-md); padding: 10px;
               border: 1px solid var(--c-border-soft); }
.metric-val  { font-size: 16px; font-weight: 800; color: var(--c-text); }
.metric-lbl  { font-size: 10px; color: var(--c-text-muted); margin-top: 2px; }

/* Progress bar */
.prog-label  { display: flex; justify-content: space-between; margin-bottom: 5px; }
.prog-bar    { height: 6px; background: var(--c-border-soft); border-radius: 3px; overflow: hidden; margin-bottom: 10px; }
.prog-fill   { height: 100%; border-radius: 3px; }
.prog-pre    { background: linear-gradient(90deg, var(--c-blue), var(--c-purple)); }
.prog-post   { background: linear-gradient(90deg, var(--c-cyan), var(--c-green)); }

/* Reference list */
.ref-item { display: flex; gap: 10px; padding: 10px 0; border-bottom: 1px solid var(--c-border-soft); }
.ref-item:last-child { border-bottom: none; }
.ref-dot  { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; margin-top: 5px; }
.ref-text { font-size: 12px; color: var(--c-text-2); line-height: 1.5; }
.ref-text strong { color: var(--c-text); display: block; font-size: 12px; margin-bottom: 1px; }

/* Lecture note callout */
.lecture-callout { background: var(--c-amber-soft); border: 1px solid var(--cb-amber-border);
                   border-radius: var(--r-md); padding: 14px 16px; margin-bottom: 14px; }
.lecture-callout strong { color: var(--c-amber); display: block; font-size: 12px; margin-bottom: 6px; }
.lecture-callout p { font-size: 12px; color: var(--c-text-2); margin: 0; }

/* Key term */
.term-table td:first-child { font-weight: 700; color: var(--c-text); width: 30%; }
.term-table td:nth-child(2) { color: var(--c-text-3); font-style: italic; width: 25%; }

/* Exercise problem */
.exercise-num { display: inline-flex; width: 28px; height: 28px; background: var(--c-blue);
                color: #fff; border-radius: 50%; align-items: center; justify-content: center;
                font-size: 12px; font-weight: 700; margin-right: 10px; flex-shrink: 0; }
.exercise-block { display: flex; align-items: flex-start; margin-bottom: 20px; }
.difficulty { font-size: 10px; font-weight: 600; padding: 2px 7px; border-radius: var(--r-sm); margin-left: 8px; }
.diff-l1 { background: var(--c-green-soft); color: var(--c-green); }
.diff-l2 { background: var(--c-amber-soft); color: var(--c-amber); }
.diff-l3 { background: var(--c-red-soft);   color: var(--c-red); }

/* Footer */
.page-footer { text-align: center; padding: 20px; font-size: 11px; color: var(--c-text-muted);
               border-top: 1px solid var(--c-border); background: var(--c-surface); margin-top: 8px; }
```

- [ ] **Step 3: Write print.css**

Write to `Dev Assistant/assets/css/print.css`:

```css
/* ── MNK202 Design B — Print: PDF-ready overrides ── */

@media print {
  * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }

  body { background: #fff !important; font-size: 12px; }

  /* Hero */
  .week-hero { border-bottom: 2px solid #0f172a; padding: 20px 24px 0; }
  .week-hero::before { height: 3px; }

  /* Body: single column */
  .body-grid { display: block; padding: 16px 24px; }
  .sidebar { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 20px; }

  /* Tab nav: hide */
  .tab-nav { display: none; }

  /* Cards */
  .section-card { box-shadow: none; border: 1px solid #e2e8f0; margin-bottom: 14px; }

  /* Never break inside these elements */
  .concept-box, .flow-row, .quote-block, .read-step,
  .metric-box, .ref-item, .exercise-block,
  .section-card { break-inside: avoid; }

  /* Section headers don't orphan */
  .section-header { break-after: avoid; }

  /* Force page break before each week (used in master bundle) */
  .week-page-break { break-before: page; }

  /* Chips and pills: flatten */
  .chip, .pill { border: 1px solid #ccc !important; }

  /* Prog bars: print flat */
  .prog-fill { print-color-adjust: exact; }

  /* Links: show URL */
  a[href]::after { content: none; }

  /* Footer */
  .page-footer { border-top: 1px solid #e2e8f0; }
}
```

- [ ] **Step 4: Download Inter Variable font**

Download `inter-v.woff2` from https://rsms.me/inter/ (the variable font file). Save to `Dev Assistant/assets/fonts/inter-v.woff2`.

If the download is not possible in the current environment, create an empty placeholder file — the system falls back to `system-ui` via the CSS stack in base.css.

```bash
# Check if font file needs to be placed
ls "Dev Assistant/assets/fonts/" 2>/dev/null || mkdir -p "Dev Assistant/assets/fonts"
```

- [ ] **Step 5: Commit CSS**

```bash
git add "Dev Assistant/assets/"
git commit -m "feat(css): Design B screen + print CSS system, CSS variables, Inter font-face"
```

---

## Task 7: HTML Templates (Base + 5 Deliverables)

**Files:**
- Write: `Dev Assistant/templates/base.html.tera`
- Write: `Dev Assistant/templates/study-guide.html.tera`
- Write: `Dev Assistant/templates/summary.html.tera`
- Write: `Dev Assistant/templates/company-example.html.tera`
- Write: `Dev Assistant/templates/review-sheet.html.tera`
- Write: `Dev Assistant/templates/exercises.html.tera`

- [ ] **Step 1: Write base.html.tera**

Write to `Dev Assistant/templates/base.html.tera`:

```html
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>W{{ week_pad }} — {{ title }} | MNK202</title>
<link rel="stylesheet" href="css/base.css">
<link rel="stylesheet" href="css/screen.css">
<link rel="stylesheet" href="css/print.css">
</head>
<body>

<!-- ══ WEEK HERO ══ -->
<div class="week-hero">
  <div class="hero-top">
    <div>
      <div class="hero-badge">
        <span class="pill pill-week">Minggu {{ week_pad }}</span>
        <span class="pill pill-{{ phase_class }}">{{ phase_label }}</span>
      </div>
      <h1 class="hero-title">{{ title }}</h1>
      <p class="hero-subtitle">{{ title_en }}</p>
      <div class="ref-chips">
        {% for r in core_readings %}<span class="chip chip-book">{{ r }}</span>{% endfor %}
        {% for s in supplementary %}<span class="chip chip-supp">{{ s }}</span>{% endfor %}
        {% if company_ticker != "—" %}<span class="chip chip-co">{{ company_ticker }} · {{ company_name }}</span>{% endif %}
      </div>
    </div>
    <div class="hero-watermark">{{ week_pad }}</div>
  </div>

  <nav class="tab-nav">
    <div class="tab {% if deliverable_type == 'study-guide' %}active{% endif %}">📖 Study Guide</div>
    <div class="tab {% if deliverable_type == 'summary' %}active{% endif %}">📄 Main Summary</div>
    <div class="tab {% if deliverable_type == 'company-example' %}active{% endif %}">🏢 Company Example</div>
    <div class="tab {% if deliverable_type == 'review-sheet' %}active{% endif %}">📋 Review Sheet</div>
    <div class="tab {% if deliverable_type == 'exercises' %}active{% endif %}">✏️ Exercises</div>
  </nav>
</div>

<!-- ══ BODY GRID ══ -->
<div class="body-grid">
  <div class="main-col">
    {% block main %}{% endblock main %}
  </div>
  <aside class="sidebar">
    {% block sidebar %}
    <!-- Deliverable switcher -->
    <div class="side-card">
      <div class="side-header">📂 Deliverables</div>
      <div class="side-body">
        <div class="deliv-grid">
          <div class="deliv-btn {% if deliverable_type == 'study-guide' %}active{% endif %}">
            <span>📖</span><span>Study Guide</span>
          </div>
          <div class="deliv-btn {% if deliverable_type == 'summary' %}active{% endif %}">
            <span>📄</span><span>Main Summary</span>
          </div>
          <div class="deliv-btn {% if deliverable_type == 'company-example' %}active{% endif %}">
            <span>🏢</span><span>Company Example</span>
          </div>
          <div class="deliv-btn {% if deliverable_type == 'review-sheet' %}active{% endif %}">
            <span>📋</span><span>Review Sheet</span>
          </div>
          <div class="deliv-btn deliv-btn-full {% if deliverable_type == 'exercises' %}active{% endif %}">
            <span>✏️</span><span>Exercises</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Anchor Company -->
    {% if company_ticker != "—" %}
    <div class="side-card">
      <div class="side-header">🏢 Anchor Company</div>
      <div class="side-body">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
          <div class="co-logo" style="background:linear-gradient(135deg,#1d4ed8,#2563eb);">
            {{ company_ticker | truncate(length=3, end="") }}
          </div>
          <div>
            <div class="co-name">{{ company_name }}</div>
            <div class="co-sub">{{ company_exchange }}</div>
            <div class="co-ticker">{{ company_exchange }}: {{ company_ticker }}</div>
          </div>
        </div>
        {% block company_sidebar %}{% endblock company_sidebar %}
      </div>
    </div>
    {% endif %}

    <!-- References -->
    <div class="side-card">
      <div class="side-header">📚 Referensi</div>
      <div class="side-body">
        {% for r in core_readings %}
        <div class="ref-item">
          <div class="ref-dot" style="background:#7c3aed;"></div>
          <div class="ref-text"><strong>{{ r }}</strong>Core required reading</div>
        </div>
        {% endfor %}
        {% for s in supplementary %}
        <div class="ref-item">
          <div class="ref-dot" style="background:#94a3b8;"></div>
          <div class="ref-text">{{ s }}</div>
        </div>
        {% endfor %}
      </div>
    </div>

    <!-- Progress -->
    <div class="side-card">
      <div class="side-header">📈 Progress Semester</div>
      <div class="side-body">
        {% set pre_done = [week_num, 7] | min %}
        {% set post_done = [week_num - 7, 0] | max %}
        <div>
          <div class="prog-label"><span style="font-size:12px;">Pra-UTS (W1–7)</span><span style="font-size:11px;color:#64748b;">{{ pre_done }} / 7</span></div>
          <div class="prog-bar"><div class="prog-fill prog-pre" style="width:{{ pre_done * 100 / 7 }}%;"></div></div>
        </div>
        <div>
          <div class="prog-label"><span style="font-size:12px;">Pasca-UTS (W8–14)</span><span style="font-size:11px;color:#64748b;">{{ post_done }} / 7</span></div>
          <div class="prog-bar"><div class="prog-fill prog-post" style="width:{{ post_done * 100 / 7 }}%;"></div></div>
        </div>
      </div>
    </div>
    {% endblock sidebar %}
  </aside>
</div>

<footer class="page-footer">
  MNK202 Pelaporan Keuangan Korporat · Pascasarjana STIE YKPN 2025/2026 · Minggu {{ week_pad }}
</footer>

</body>
</html>
```

- [ ] **Step 2: Write study-guide.html.tera**

Write to `Dev Assistant/templates/study-guide.html.tera`:

```html
{% extends "base.html.tera" %}

{% block main %}
<div class="section-card">
  <div class="section-header">
    <div class="section-icon icon-blue">🗺️</div>
    <div>
      <div class="section-title">Study Guide — Minggu {{ week_pad }}</div>
      <div class="section-sub">Panduan belajar terstruktur untuk minggu ini</div>
    </div>
  </div>
  <div class="section-body">
    {{ content_html | safe }}
  </div>
</div>
{% endblock main %}
```

- [ ] **Step 3: Write summary.html.tera**

Write to `Dev Assistant/templates/summary.html.tera`:

```html
{% extends "base.html.tera" %}

{% block main %}
<div class="section-card">
  <div class="section-header">
    <div class="section-icon icon-purple">📄</div>
    <div>
      <div class="section-title">Main Summary — Minggu {{ week_pad }}</div>
      <div class="section-sub">Ringkasan akademis bab teks yang ditugaskan</div>
    </div>
  </div>
  <div class="section-body">
    {{ content_html | safe }}
  </div>
</div>
{% endblock main %}
```

- [ ] **Step 4: Write company-example.html.tera**

Write to `Dev Assistant/templates/company-example.html.tera`:

```html
{% extends "base.html.tera" %}

{% block main %}
<div class="section-card">
  <div class="section-header">
    <div class="section-icon icon-green">🏢</div>
    <div>
      <div class="section-title">Indonesian Company Example — {{ company_name }}</div>
      <div class="section-sub">Analisis primer berdasarkan Annual Report teraudit · {{ company_exchange }}: {{ company_ticker }}</div>
    </div>
  </div>
  <div class="section-body">
    {{ content_html | safe }}
  </div>
</div>
{% endblock main %}
```

- [ ] **Step 5: Write review-sheet.html.tera**

Write to `Dev Assistant/templates/review-sheet.html.tera`:

```html
{% extends "base.html.tera" %}

{% block main %}
<div class="section-card">
  <div class="section-header">
    <div class="section-icon icon-amber">📋</div>
    <div>
      <div class="section-title">Review Sheet — Minggu {{ week_pad }}</div>
      <div class="section-sub">Referensi cepat · target 1–2 halaman A4</div>
    </div>
  </div>
  <div class="section-body">
    {{ content_html | safe }}
  </div>
</div>
{% endblock main %}
```

- [ ] **Step 6: Write exercises.html.tera**

Write to `Dev Assistant/templates/exercises.html.tera`:

```html
{% extends "base.html.tera" %}

{% block main %}
<div class="section-card">
  <div class="section-header">
    <div class="section-icon icon-blue">✏️</div>
    <div>
      <div class="section-title">Exercises — Minggu {{ week_pad }}</div>
      <div class="section-sub">Soal latihan gaya UTS/UAS · 5–8 soal per minggu</div>
    </div>
  </div>
  <div class="section-body">
    {{ content_html | safe }}
  </div>
</div>
{% endblock main %}
```

- [ ] **Step 7: Commit templates**

```bash
git add "Dev Assistant/templates/"
git commit -m "feat(templates): base + 5 deliverable Tera templates, Design B hero + sidebar"
```

---

## Task 8: Builder Module

**Files:**
- Write: `Dev Assistant/src/builder.rs`

- [ ] **Step 1: Write builder.rs**

Write to `Dev Assistant/src/builder.rs`:

```rust
use std::fs;
use std::path::Path;
use tera::Tera;

use crate::config::{load_config, MappingConfig};
use crate::markdown::render_markdown;
use crate::renderer::{build_context, render_template, DELIVERABLES};

pub fn build_week(
    week: u8,
    tera: &Tera,
    config_path: &str,
    content_dir: &str,
    assets_dir: &str,
    output_root: &str,
) {
    let config = load_config(config_path).expect("Failed to load mapping.toml");
    let all_weeks: Vec<(u8, String)> = (1u8..=14)
        .filter_map(|w| config.weeks.get(&w).map(|c| (w, c.title.clone())))
        .collect();

    let week_config = config.weeks.get(&week)
        .unwrap_or_else(|| panic!("Week {} not found in mapping.toml", week));

    for meta in DELIVERABLES {
        let source_path = format!("{}/week-{:02}/{}", content_dir, week, meta.source_file);
        let md = fs::read_to_string(&source_path).unwrap_or_else(|_| {
            format!(
                "# {} — Minggu {:02}\n\n*Konten sedang disiapkan.*\n",
                meta.label, week
            )
        });

        let content_html = render_markdown(&md);
        let ctx = build_context(week, week_config, &content_html, meta, &all_weeks);
        let rendered = render_template(tera, meta.template, &ctx);

        let out_dir = format!("{}/{}/Week {:02}", output_root, meta.output_folder, week);
        fs::create_dir_all(&out_dir).expect("Failed to create output directory");

        let out_path = format!("{}/{}", out_dir, meta.output_file);
        fs::write(&out_path, &rendered).expect("Failed to write HTML output");

        copy_assets(&out_dir, assets_dir);

        println!("  ✓  W{:02}  {}  →  {}", week, meta.type_key, out_path);
    }
}

pub fn build_weeks_range(
    range: &str,
    tera: &Tera,
    config_path: &str,
    content_dir: &str,
    assets_dir: &str,
    output_root: &str,
) {
    let parts: Vec<u8> = range
        .split('-')
        .map(|s| s.trim().parse::<u8>().expect("Invalid week number in range"))
        .collect();
    assert_eq!(parts.len(), 2, "Range must be in format 'N-M', e.g. '1-7'");
    for week in parts[0]..=parts[1] {
        build_week(week, tera, config_path, content_dir, assets_dir, output_root);
    }
}

pub fn build_all(
    tera: &Tera,
    config_path: &str,
    content_dir: &str,
    assets_dir: &str,
    output_root: &str,
) {
    for week in 1u8..=14 {
        println!("\nBuilding Week {:02}...", week);
        build_week(week, tera, config_path, content_dir, assets_dir, output_root);
    }
}

fn copy_assets(out_dir: &str, assets_dir: &str) {
    let css_src = Path::new(assets_dir).join("css");
    let css_dst = Path::new(out_dir).join("css");
    fs::create_dir_all(&css_dst).ok();
    for entry in fs::read_dir(&css_src).expect("Cannot read assets/css") {
        let entry = entry.unwrap();
        let dst = css_dst.join(entry.file_name());
        fs::copy(entry.path(), dst).ok();
    }

    let font_src = Path::new(assets_dir).join("fonts");
    let font_dst = Path::new(out_dir).join("fonts");
    fs::create_dir_all(&font_dst).ok();
    if font_src.exists() {
        for entry in fs::read_dir(&font_src).expect("Cannot read assets/fonts") {
            let entry = entry.unwrap();
            let dst = font_dst.join(entry.file_name());
            fs::copy(entry.path(), dst).ok();
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_weeks_range_parses_correctly() {
        // Just test parsing — don't actually build
        let range = "1-7";
        let parts: Vec<u8> = range.split('-').map(|s| s.trim().parse().unwrap()).collect();
        assert_eq!(parts, vec![1u8, 7u8]);
    }
}
```

- [ ] **Step 2: Run builder tests**

```bash
cd "Dev Assistant"
cargo test builder 2>&1
```

Expected: 1 test passes.

- [ ] **Step 3: Commit**

```bash
cd ..
git add "Dev Assistant/src/builder.rs"
git commit -m "feat(builder): build_week / build_weeks_range / build_all + asset copy"
```

---

## Task 9: Bundle Module (Visual Companion + Master Bundle)

**Files:**
- Write: `Dev Assistant/src/bundle.rs`
- Write: `Dev Assistant/templates/visual-companion.html.tera`
- Write: `Dev Assistant/templates/master-bundle.html.tera`

- [ ] **Step 1: Write visual-companion.html.tera**

Write to `Dev Assistant/templates/visual-companion.html.tera`:

```html
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Visual Companion — MNK202 Pelaporan Keuangan Korporat</title>
<link rel="stylesheet" href="css/base.css">
<link rel="stylesheet" href="css/screen.css">
<link rel="stylesheet" href="css/print.css">
<style>
  .vc-header { background: #0f172a; color: #f8fafc; padding: 32px 40px;
               border-bottom: 4px solid; border-image: linear-gradient(90deg,#2563eb,#7c3aed,#0891b2) 1; }
  .vc-title  { font-size: 28px; font-weight: 800; margin-bottom: 6px; }
  .vc-sub    { font-size: 14px; color: #94a3b8; }
  .vc-grid   { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
               gap: 16px; padding: 32px 40px; max-width: 1200px; margin: 0 auto; }
  .vc-card   { background: #fff; border-radius: 10px; border: 1px solid #e2e8f0;
               box-shadow: 0 1px 3px rgba(0,0,0,.08); overflow: hidden; }
  .vc-week-num { font-size: 48px; font-weight: 900; color: #e2e8f0; line-height: 1; }
  .vc-card-top { padding: 20px; border-bottom: 1px solid #f1f5f9; }
  .vc-card-body { padding: 16px 20px; }
  .vc-pill-pre  { background: #eff6ff; color: #2563eb; }
  .vc-pill-post { background: #f0fdf4; color: #16a34a; }
  .vc-links { display: flex; flex-wrap: wrap; gap: 6px; }
  .vc-link  { font-size: 11px; padding: 4px 10px; border-radius: 4px; border: 1px solid #e2e8f0;
              color: #374151; text-decoration: none; background: #f8fafc; }
  .vc-link:hover { background: #eff6ff; border-color: #2563eb; color: #2563eb; }
</style>
</head>
<body>
<div class="vc-header">
  <div class="vc-title">Visual Companion</div>
  <div class="vc-sub">MNK202 Pelaporan Keuangan Korporat · Pascasarjana STIE YKPN 2025/2026 · 14 Pertemuan</div>
</div>
<div class="vc-grid">
  {% for week in all_weeks %}
  <div class="vc-card">
    <div class="vc-card-top" style="display:flex;justify-content:space-between;align-items:flex-start;">
      <div>
        <span class="pill {{ week.phase_class | replace(from='-', to='-') }} vc-pill-{{ week.phase_key }}" style="font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-block;margin-bottom:8px;">
          {{ week.phase_label }}
        </span>
        <div style="font-size:14px;font-weight:700;color:#0f172a;line-height:1.3;">{{ week.title }}</div>
        <div style="font-size:11px;color:#64748b;margin-top:3px;">{{ week.company_ticker }} · {{ week.company_name }}</div>
      </div>
      <div class="vc-week-num">{{ week.week_pad }}</div>
    </div>
    <div class="vc-card-body">
      <div style="font-size:10px;color:#94a3b8;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Deliverables</div>
      <div class="vc-links">
        <a class="vc-link" href="../Study Guide - Aid/Week {{ week.week_pad }}/index.html">📖 Study Guide</a>
        <a class="vc-link" href="../Main Summary - Ebook/Week {{ week.week_pad }}/index.html">📄 Summary</a>
        <a class="vc-link" href="../Indonesian Company Examples/Week {{ week.week_pad }}/examples.html">🏢 Company</a>
        <a class="vc-link" href="../Review Sheet/Week {{ week.week_pad }}/index.html">📋 Review</a>
        <a class="vc-link" href="../Exercises/Week {{ week.week_pad }}/index.html">✏️ Exercises</a>
      </div>
    </div>
  </div>
  {% endfor %}
</div>
<footer class="page-footer">
  MNK202 · Visual Companion · Generated by devassist
</footer>
</body>
</html>
```

- [ ] **Step 2: Write bundle.rs**

Write to `Dev Assistant/src/bundle.rs`:

```rust
use std::fs;
use std::path::Path;
use tera::{Context, Tera};

use crate::config::load_config;
use crate::renderer::DELIVERABLES;

pub fn build_visual_companion(
    tera: &Tera,
    config_path: &str,
    assets_dir: &str,
    output_root: &str,
) {
    let config = load_config(config_path).expect("Failed to load config");

    #[derive(serde::Serialize)]
    struct WeekEntry {
        week_num: u8,
        week_pad: String,
        title: String,
        company_name: String,
        company_ticker: String,
        phase_label: String,
        phase_key: String,
    }

    let all_weeks: Vec<WeekEntry> = (1u8..=14)
        .filter_map(|w| {
            config.weeks.get(&w).map(|c| WeekEntry {
                week_num: w,
                week_pad: format!("{:02}", w),
                title: c.title.clone(),
                company_name: c.company_name.clone(),
                company_ticker: c.company_ticker.clone(),
                phase_label: if c.phase == "pre-uts" { "Pra-UTS".into() } else { "Pasca-UTS".into() },
                phase_key: if c.phase == "pre-uts" { "pre".into() } else { "post".into() },
            })
        })
        .collect();

    let mut ctx = Context::new();
    ctx.insert("all_weeks", &all_weeks);

    let rendered = tera.render("visual-companion.html.tera", &ctx)
        .expect("Visual companion template render failed");

    let out_dir = format!("{}/Visual Companion", output_root);
    fs::create_dir_all(&out_dir).unwrap();

    fs::write(format!("{}/index.html", out_dir), &rendered).unwrap();

    // Copy assets
    let css_src = Path::new(assets_dir).join("css");
    let css_dst = Path::new(&out_dir).join("css");
    fs::create_dir_all(&css_dst).ok();
    for entry in fs::read_dir(&css_src).unwrap() {
        let entry = entry.unwrap();
        fs::copy(entry.path(), css_dst.join(entry.file_name())).ok();
    }
    let font_src = Path::new(assets_dir).join("fonts");
    let font_dst = Path::new(&out_dir).join("fonts");
    fs::create_dir_all(&font_dst).ok();
    if font_src.exists() {
        for entry in fs::read_dir(&font_src).unwrap() {
            let entry = entry.unwrap();
            fs::copy(entry.path(), font_dst.join(entry.file_name())).ok();
        }
    }

    println!("  ✓  Visual Companion → {}/index.html", out_dir);
}

pub fn build_master_bundle(config_path: &str, output_root: &str) {
    // Concatenate all week HTML files into a single self-contained file
    // with CSS inlined from the first available week's css/ directory.
    let config = load_config(config_path).expect("Failed to load config");

    let css_source_dir = format!(
        "{}/Study Guide - Aid/Week 01/css",
        output_root
    );

    let base_css   = fs::read_to_string(format!("{}/base.css",   css_source_dir)).unwrap_or_default();
    let screen_css = fs::read_to_string(format!("{}/screen.css", css_source_dir)).unwrap_or_default();
    let print_css  = fs::read_to_string(format!("{}/print.css",  css_source_dir)).unwrap_or_default();

    let mut bundle = String::new();
    bundle.push_str("<!DOCTYPE html>\n<html lang=\"id\">\n<head>\n");
    bundle.push_str("<meta charset=\"UTF-8\">\n");
    bundle.push_str("<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n");
    bundle.push_str("<title>MNK202 — Master Print Bundle</title>\n");
    bundle.push_str(&format!("<style>\n{}\n{}\n{}\n</style>\n", base_css, screen_css, print_css));
    bundle.push_str("</head>\n<body>\n");

    for week in 1u8..=14 {
        for meta in DELIVERABLES {
            let html_path = format!(
                "{}/{}/Week {:02}/{}",
                output_root, meta.output_folder, week, meta.output_file
            );
            if let Ok(content) = fs::read_to_string(&html_path) {
                // Strip <html>, <head>, <body> wrapper — extract body content
                let body_content = extract_body(&content);
                bundle.push_str(&format!(
                    "\n<div class=\"week-page-break\" id=\"w{:02}-{}\">",
                    week, meta.type_key
                ));
                bundle.push_str(&body_content);
                bundle.push_str("</div>\n");
            }
        }
    }

    bundle.push_str("</body>\n</html>\n");

    let out_dir = format!("{}/Master Print Bundle", output_root);
    fs::create_dir_all(&out_dir).unwrap();
    let out_path = format!("{}/course-companion.html", out_dir);
    fs::write(&out_path, &bundle).expect("Failed to write master bundle");

    let size_kb = bundle.len() / 1024;
    println!("  ✓  Master Bundle → {} ({} KB)", out_path, size_kb);
}

fn extract_body(html: &str) -> String {
    // Extract content between <body> and </body> tags
    if let (Some(start), Some(end)) = (html.find("<body"), html.rfind("</body>")) {
        let body_open_end = html[start..].find('>').map(|i| start + i + 1).unwrap_or(start);
        return html[body_open_end..end].to_string();
    }
    html.to_string()
}
```

- [ ] **Step 3: Compile check**

```bash
cd "Dev Assistant"
cargo build 2>&1
```

Expected: `Finished` with no errors. Warnings about unused variables are acceptable at this stage.

- [ ] **Step 4: Commit**

```bash
cd ..
git add "Dev Assistant/src/bundle.rs" "Dev Assistant/templates/visual-companion.html.tera"
git commit -m "feat(bundle): visual-companion + master-bundle generators"
```

---

## Task 10: Stub Content + Directories

**Files:**
- Create: `Dev Assistant/content/week-NN/*.md` for all 14 weeks (stub files)

- [ ] **Step 1: Create stub content for all 14 weeks**

Run this bash loop to create stub markdown files for all 14 weeks:

```bash
cd "Dev Assistant"
for w in $(seq -w 1 14); do
  mkdir -p "content/week-${w}"
  for f in study-guide summary company-example review-sheet exercises; do
    if [ ! -f "content/week-${w}/${f}.md" ]; then
      echo "# Minggu ${w} — ${f}" > "content/week-${w}/${f}.md"
      echo "" >> "content/week-${w}/${f}.md"
      echo "*Konten sedang disiapkan. File ini adalah stub untuk pengujian pipeline.*" >> "content/week-${w}/${f}.md"
    fi
  done
done
echo "Stub files created."
ls content/week-01/
```

Expected output:
```
Stub files created.
company-example.md  exercises.md  review-sheet.md  study-guide.md  summary.md
```

- [ ] **Step 2: Commit stub content**

```bash
cd ..
git add "Dev Assistant/content/"
git commit -m "chore(content): stub markdown files for all 14 weeks — pipeline test scaffold"
```

---

## Task 11: End-to-End Smoke Test

**Goal:** Verify the complete pipeline renders all 70 deliverables, the Visual Companion, and the Master Bundle from stub content with no errors.

- [ ] **Step 1: Build all 14 weeks**

```bash
cd "Dev Assistant"
cargo run --release -- all 2>&1
```

Expected: 70 lines of `✓  W01  study-guide  →  ...` etc., no panics, no errors.

- [ ] **Step 2: Count output files**

```bash
find "../course-materials/outputs" -name "*.html" | wc -l
```

Expected: at least 70 HTML files (Study Guide + Summary + Company + Review + Exercises × 14 weeks).

- [ ] **Step 3: Build Visual Companion**

```bash
cargo run --release -- visual-companion 2>&1
```

Expected: `✓  Visual Companion → .../Visual Companion/index.html`

- [ ] **Step 4: Build Master Bundle**

```bash
cargo run --release -- master-bundle 2>&1
```

Expected: `✓  Master Bundle → .../Master Print Bundle/course-companion.html (NNN KB)`

- [ ] **Step 5: Open in browser and verify**

Open `course-materials/outputs/Study Guide - Aid/Week 01/index.html` in a browser. Verify:
- Week Hero renders with gradient top bar
- "Minggu 01" watermark visible
- "Pra-UTS" pill visible
- Tab nav shows 5 tabs
- Sidebar shows Deliverables grid and References

Open `course-materials/outputs/Visual Companion/index.html`. Verify:
- 14 week cards visible
- Each card shows week number, title, company, phase

- [ ] **Step 6: Commit final pipeline**

```bash
cd ..
git add -A
git commit -m "feat: complete devassist pipeline — 70 deliverables + Visual Companion + Master Bundle render from stub content

Pipeline verified end-to-end. Ready for Plan B content generation."
```

---

## Handoff: Plan B — Content Generation

Plan A is complete when Task 11 passes. The pipeline is proven. Now content subagents fill in the real academic material.

**Plan B is dispatched using `superpowers:dispatching-parallel-agents`.**

Each subagent receives:
1. Its week number (1–14)
2. The assigned textbook chapter(s) — from `mapping.toml`
3. The anchor company AR PDF path
4. The 13-section template for `company-example.md`
5. The content spec for each of the 5 markdown files (from Section 6 of the design spec)

After all 14 subagents complete, run:
```bash
cd "Dev Assistant"
cargo run --release -- all
cargo run --release -- visual-companion
cargo run --release -- master-bundle
```

Then commit the final output.

**See:** `docs/superpowers/specs/2026-04-18-pkk-fresh-rebuild-design.md` Section 6 for full per-deliverable content requirements.

---

## Self-Review Checklist

- [x] **Spec coverage:** Architecture (§2) ✓, file structure (§3) ✓, CSS system (§4) ✓, mapping.toml (§5) ✓, deliverable specs (§6) ✓, language policy (§7) ✓, git reset (§9) ✓, Rust pipeline (§10) ✓, success criteria (§11) — all covered.
- [x] **Placeholder scan:** No TBDs, no "implement later". Every step has actual code or exact commands.
- [x] **Type consistency:** `DELIVERABLES` constant defined in `renderer.rs` Task 5, used correctly in `builder.rs` Task 8 and `bundle.rs` Task 9. `WeekConfig` defined in Task 3, used in Task 5 (`build_context`), Task 8 (`build_week`). `MappingConfig.weeks: HashMap<u8, WeekConfig>` consistent throughout. `build_week` signature in `builder.rs` matches `main.rs` call site.
- [x] **Scope check:** This plan produces a working pipeline. Content (Plan B) is explicitly deferred to parallel subagents post-Task-11. No ambiguous requirements remain.
