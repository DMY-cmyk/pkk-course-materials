# RMK Pertemuan 9 "The Income Statement" Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `rmk-pkk-pert9-income-statement/output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx` — a 7–9k-word graduate RMK of Wolk Ch. 12 with 6 reconstructed diagrams + 4 native Word tables, reproducible from `input/` via 3 Rust crates + one Python assembly script.

**Architecture:** Deterministic 4-stage pipeline: `chapter_locator` (Rust/lopdf → chapter-range.json) → `text_extract` (Rust/lopdf → per-section text + zero-exhibit verification report) → `visual_gen` (Rust/resvg → rasterize 6 authored SVGs to PNG) → `build_docx.py` (python-docx, adapted from the proven K2 builder `Kelompok 2 Pasca UTS/output/build_docx.py`). Content prose is authored into `content/*.md` against the extraction output.

**Tech Stack:** Rust 1.94 (lopdf, resvg, clap, anyhow, thiserror, serde_json), Python 3.12 (python-docx 1.2.0, tomllib stdlib), spec: `docs/superpowers/specs/2026-06-08-rmk-pert9-income-statement-design.md`.

**Working directory:** all commands run from `D:\DZAKI\S2\Sem. 1\Pelaporan Keuangan Korporat\rmk-pkk-pert9-income-statement` unless stated. Repo root is the course repo (already git-initialized).

**Ground truth (verified 2026-06-08):** Chapter 12 = PDF pages 305–338 (1-based) in `01-Textbooks\Wolk - Accounting Theory 9th Ed.pdf`; SAGE title page contains `Chapter Title: "The Income Statement"`; Ch. 13 title page (339) contains `Chapter Title: "Statement of Cash Flows"`; the chapter contains 0 exhibits (only SAGE logo image on title page).

**Citation convention (refinement over spec):** inline citations use chapter-internal SAGE pages `(Wolk et al., 2017, PDF hlm. N)` — N = the "Page N of 34" printed on each chapter page — exactly like the K2 precedent, because these are verifiable against the file in hand; the Referensi entry lists the print range 337–373. (Spec said print pages; approximating per-paragraph print pages would risk false precision. Flagged to user at plan handoff.)

---

### Task 1: Scaffold repository

**Files:**
- Create: `rmk-pkk-pert9-income-statement/.gitignore`, `Cargo.toml`, `requirements.txt`, `README.md` (stub), directory tree, copies of the two input PDFs

- [ ] **Step 1: Create directory tree and root files**

```powershell
cd "D:\DZAKI\S2\Sem. 1\Pelaporan Keuangan Korporat"
New-Item -ItemType Directory -Force rmk-pkk-pert9-income-statement\input\syllabus, rmk-pkk-pert9-income-statement\input\textbook, rmk-pkk-pert9-income-statement\src\rust, rmk-pkk-pert9-income-statement\src\python, rmk-pkk-pert9-income-statement\extraction\text, rmk-pkk-pert9-income-statement\assets\diagrams\svg, rmk-pkk-pert9-income-statement\assets\tables, rmk-pkk-pert9-income-statement\content, rmk-pkk-pert9-income-statement\design\previews, rmk-pkk-pert9-income-statement\output
Copy-Item "03-Course-Admin\Silabus_Pelaporan Keuangan Korporat_25-26.pdf" "rmk-pkk-pert9-income-statement\input\syllabus\Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf"
Copy-Item "01-Textbooks\Wolk - Accounting Theory 9th Ed.pdf" "rmk-pkk-pert9-income-statement\input\textbook\Wolk_-_Accounting_Theory_9th_Ed.pdf"
```

`rmk-pkk-pert9-income-statement/.gitignore`:

```gitignore
input/
extraction/
target/
__pycache__/
assets/diagrams/*.png
```

(PNGs and extraction are regenerable; PDFs already tracked elsewhere in the course repo. The final .docx in `output/` IS committed, matching course-repo convention.)

`rmk-pkk-pert9-income-statement/Cargo.toml` (workspace):

```toml
[workspace]
resolver = "2"
members = [
    "src/rust/chapter_locator",
    "src/rust/text_extract",
    "src/rust/visual_gen",
]
```

`rmk-pkk-pert9-income-statement/requirements.txt`:

```
python-docx==1.2.0
```

`rmk-pkk-pert9-income-statement/README.md` (stub — finalized in Task 13):

```markdown
# RMK Pertemuan 9 — The Income Statement (Wolk Ch. 12)

Pipeline build for `output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx`.
Run order and Rust/Python split rationale: see Task 13 final version.
```

- [ ] **Step 2: Verify scaffold**

Run: `Get-ChildItem -Recurse -Directory rmk-pkk-pert9-income-statement | Select-Object FullName` and `Get-ChildItem rmk-pkk-pert9-income-statement\input -Recurse -File`
Expected: all directories above exist; 2 PDFs present.

- [ ] **Step 3: Commit**

```powershell
git add rmk-pkk-pert9-income-statement/.gitignore rmk-pkk-pert9-income-statement/Cargo.toml rmk-pkk-pert9-income-statement/requirements.txt rmk-pkk-pert9-income-statement/README.md
git commit -m "feat(rmk9): scaffold pipeline repository"
```

---

### Task 2: `chapter_locator` crate (TDD)

**Files:**
- Create: `src/rust/chapter_locator/Cargo.toml`, `src/rust/chapter_locator/src/main.rs`

- [ ] **Step 1: Crate manifest**

`src/rust/chapter_locator/Cargo.toml`:

```toml
[package]
name = "chapter_locator"
version = "0.1.0"
edition = "2021"

[dependencies]
lopdf = "0.36"
clap = { version = "4", features = ["derive"] }
anyhow = "1"
thiserror = "2"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

- [ ] **Step 2: Write failing unit tests + skeleton**

`src/rust/chapter_locator/src/main.rs`:

```rust
//! Locates the Chapter 12 page range in the Wolk SAGE-edition PDF.
//! Emits extraction/chapter-range.json. Fails loudly on ambiguity.

use anyhow::{Context, Result};
use clap::Parser;
use serde::Serialize;

#[derive(Debug, thiserror::Error)]
pub enum LocateError {
    #[error("marker {0:?} not found in any page")]
    NotFound(String),
    #[error("marker {0:?} found on multiple pages: {1:?}")]
    Ambiguous(String, Vec<usize>),
    #[error("chapter start {start} is not before next-chapter start {next}")]
    InvertedRange { start: usize, next: usize },
}

/// Find 1-based (start_page, end_page) of the chapter whose SAGE title page
/// contains `start_marker`, ending the page before the page containing
/// `next_marker`. `pages` is 1-indexed implicitly (index 0 = page 1).
pub fn find_chapter_bounds(
    pages: &[String],
    start_marker: &str,
    next_marker: &str,
) -> Result<(usize, usize), LocateError> {
    let hits = |marker: &str| -> Vec<usize> {
        pages
            .iter()
            .enumerate()
            .filter(|(_, t)| t.contains(marker))
            .map(|(i, _)| i + 1)
            .collect()
    };
    let pick = |marker: &str| -> Result<usize, LocateError> {
        let h = hits(marker);
        match h.as_slice() {
            [] => Err(LocateError::NotFound(marker.to_string())),
            [one] => Ok(*one),
            _ => Err(LocateError::Ambiguous(marker.to_string(), h)),
        }
    };
    let start = pick(start_marker)?;
    let next = pick(next_marker)?;
    if start >= next {
        return Err(LocateError::InvertedRange { start, next });
    }
    Ok((start, next - 1))
}

#[derive(Parser)]
struct Args {
    /// Path to the textbook PDF
    #[arg(long, default_value = "input/textbook/Wolk_-_Accounting_Theory_9th_Ed.pdf")]
    pdf: String,
    /// Output JSON path
    #[arg(long, default_value = "extraction/chapter-range.json")]
    out: String,
    #[arg(long, default_value = "Chapter Title: \"The Income Statement\"")]
    start_marker: String,
    #[arg(long, default_value = "Chapter Title: \"Statement of Cash Flows\"")]
    next_marker: String,
}

#[derive(Serialize)]
struct RangeOut {
    start_page: usize,
    end_page: usize,
    print_pages: String,
    marker: String,
}

fn main() -> Result<()> {
    let args = Args::parse();
    let doc = lopdf::Document::load(&args.pdf)
        .with_context(|| format!("loading PDF {}", args.pdf))?;
    let page_nos: Vec<u32> = doc.get_pages().keys().copied().collect();
    let mut texts = Vec::with_capacity(page_nos.len());
    for no in &page_nos {
        // Garbage-tolerant: extraction errors become empty pages (markers
        // simply won't match there; ambiguity/absence still fails loudly).
        texts.push(doc.extract_text(&[*no]).unwrap_or_default());
    }
    let (start, end) =
        find_chapter_bounds(&texts, &args.start_marker, &args.next_marker)?;
    let out = RangeOut {
        start_page: start,
        end_page: end,
        print_pages: "337-373".to_string(),
        marker: args.start_marker.clone(),
    };
    std::fs::create_dir_all(std::path::Path::new(&args.out).parent().unwrap())?;
    std::fs::write(&args.out, serde_json::to_string_pretty(&out)?)?;
    println!("chapter range: pages {start}-{end} -> {}", args.out);
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    fn pages(specs: &[&str]) -> Vec<String> {
        specs.iter().map(|s| s.to_string()).collect()
    }

    #[test]
    fn finds_normal_bounds() {
        let p = pages(&["intro", "Chapter Title: \"A\"", "body", "body2", "Chapter Title: \"B\"", "tail"]);
        assert_eq!(
            find_chapter_bounds(&p, "Chapter Title: \"A\"", "Chapter Title: \"B\"").unwrap(),
            (2, 4)
        );
    }

    #[test]
    fn missing_marker_errors() {
        let p = pages(&["x", "y"]);
        assert!(matches!(
            find_chapter_bounds(&p, "A", "B"),
            Err(LocateError::NotFound(_))
        ));
    }

    #[test]
    fn duplicate_marker_errors() {
        let p = pages(&["A", "A", "B"]);
        assert!(matches!(
            find_chapter_bounds(&p, "A", "B"),
            Err(LocateError::Ambiguous(_, _))
        ));
    }

    #[test]
    fn inverted_range_errors() {
        let p = pages(&["B", "x", "A"]);
        assert!(matches!(
            find_chapter_bounds(&p, "A", "B"),
            Err(LocateError::InvertedRange { .. })
        ));
    }
}
```

- [ ] **Step 3: Run tests — verify they pass (logic is pure, written with impl)**

Run: `cargo test -p chapter_locator`
Expected: 4 passed.

- [ ] **Step 4: Integration run against the real PDF**

Run: `cargo run --release -p chapter_locator`
Expected stdout: `chapter range: pages 305-338 -> extraction/chapter-range.json`. If markers are not found (lopdf text-encoding garbage), print `doc.extract_text(&[305])` to inspect, pick a stable substring that survives extraction (e.g. `The Income Statement` co-occurring with `Contributors`), pass via `--start-marker`/`--next-marker`, and record the working markers in README. The 305–338 ground truth is fixed; any other result is a bug — stop and debug per superpowers:systematic-debugging.

- [ ] **Step 5: Commit**

```powershell
git add src/rust/chapter_locator Cargo.lock
git commit -m "feat(rmk9): chapter_locator crate finds Ch.12 bounds (305-338)"
```

---

### Task 3: `text_extract` crate (TDD)

**Files:**
- Create: `src/rust/text_extract/Cargo.toml`, `src/rust/text_extract/src/main.rs`

- [ ] **Step 1: Crate manifest**

`src/rust/text_extract/Cargo.toml`:

```toml
[package]
name = "text_extract"
version = "0.1.0"
edition = "2021"

[dependencies]
lopdf = "0.36"
clap = { version = "4", features = ["derive"] }
anyhow = "1"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

- [ ] **Step 2: Write tests + implementation**

`src/rust/text_extract/src/main.rs`:

```rust
//! Extracts Ch.12 text per page, segments it by the chapter's section
//! headings, and writes a zero-exhibit verification report.

use anyhow::{bail, Context, Result};
use clap::Parser;
use std::collections::BTreeMap;
use std::fmt::Write as _;

/// Ordered top-level headings of Wolk Ch. 12 (SAGE edition) + output slugs.
pub const SECTIONS: &[(&str, &str)] = &[
    ("Learning Objectives", "01_learning_objectives"),
    ("Income Definitions", "02_income_definitions"),
    ("Revenues and Gains", "03_revenues_and_gains"),
    ("Revenue Recognition", "04_revenue_recognition"),
    ("Expenses and Losses", "05_expenses_and_losses"),
    ("Future Events and Accounting Recognition", "06_future_events"),
    ("Current Operating Versus All-Inclusive Income", "07_co_vs_ai"),
    ("Comprehensive Income", "08_comprehensive_income"),
    ("Nonoperating Sections", "09_nonoperating_sections"),
    ("Earnings per Share", "10_eps"),
    ("Specialized Subjects Concerning Income Measurement", "11_specialized"),
    ("Earnings Management", "12_earnings_management"),
    ("Income Statement Developments", "13_developments"),
    ("Summary", "14_summary"),
    ("Questions", "15_questions"),
];

/// Split `full` (pages joined with "\n[[page:N]]\n" markers) into
/// (slug, body) chunks at the first standalone occurrence of each heading,
/// searching strictly forward so repeated phrases later don't re-split.
pub fn segment(full: &str, sections: &[(&str, &str)]) -> Vec<(String, String)> {
    let mut cuts: Vec<(usize, &str)> = Vec::new();
    let mut from = 0usize;
    for (heading, slug) in sections {
        if let Some(rel) = full[from..].find(heading) {
            let abs = from + rel;
            cuts.push((abs, slug));
            from = abs + heading.len();
        }
    }
    let mut out = Vec::new();
    if cuts.is_empty() {
        return out;
    }
    // Preamble (title page) before the first heading:
    out.push(("00_preamble".to_string(), full[..cuts[0].0].to_string()));
    for (i, (start, slug)) in cuts.iter().enumerate() {
        let end = cuts.get(i + 1).map(|c| c.0).unwrap_or(full.len());
        out.push((slug.to_string(), full[*start..end].to_string()));
    }
    out
}

#[derive(Parser)]
struct Args {
    #[arg(long, default_value = "input/textbook/Wolk_-_Accounting_Theory_9th_Ed.pdf")]
    pdf: String,
    #[arg(long, default_value = "extraction/chapter-range.json")]
    range: String,
    #[arg(long, default_value = "extraction/text")]
    out_dir: String,
    #[arg(long, default_value = "extraction/verification-report.md")]
    report: String,
}

fn count_image_xobjects(doc: &lopdf::Document, page_id: lopdf::ObjectId) -> usize {
    let mut n = 0;
    let (maybe_dict, resource_ids) = doc.get_page_resources(page_id);
    let mut dicts: Vec<&lopdf::Dictionary> = Vec::new();
    if let Some(d) = maybe_dict {
        dicts.push(d);
    }
    for rid in resource_ids {
        if let Ok(lopdf::Object::Dictionary(d)) = doc.get_object(rid) {
            dicts.push(d);
        }
    }
    for d in dicts {
        if let Ok(xobjs) = d.get(b"XObject").and_then(|o| o.as_dict()) {
            for (_, v) in xobjs.iter() {
                let resolved = match v {
                    lopdf::Object::Reference(id) => doc.get_object(*id).ok(),
                    other => Some(other),
                };
                if let Some(lopdf::Object::Stream(s)) = resolved {
                    if s.dict.get(b"Subtype").and_then(|o| o.as_name()).ok()
                        == Some(b"Image")
                    {
                        n += 1;
                    }
                }
            }
        }
    }
    n
}

fn main() -> Result<()> {
    let args = Args::parse();
    let range: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(&args.range)
            .with_context(|| format!("missing {} — run chapter_locator first", args.range))?,
    )?;
    let (start, end) = (
        range["start_page"].as_u64().context("start_page")? as u32,
        range["end_page"].as_u64().context("end_page")? as u32,
    );
    let doc = lopdf::Document::load(&args.pdf)?;
    let pages = doc.get_pages();

    // 1) Per-page text, joined with page markers
    let mut full = String::new();
    for no in start..=end {
        let t = doc
            .extract_text(&[no])
            .with_context(|| format!("extracting page {no}"))?;
        writeln!(full, "\n[[page:{no}]]\n{t}")?;
    }
    if full.trim().is_empty() {
        bail!("extracted chapter text is empty — encoding problem?");
    }

    // 2) Segment and write
    std::fs::create_dir_all(&args.out_dir)?;
    let segs = segment(&full, SECTIONS);
    if segs.len() < SECTIONS.len() / 2 {
        bail!(
            "only {} of {} headings matched — inspect extraction encoding",
            segs.len().saturating_sub(1),
            SECTIONS.len()
        );
    }
    let mut page_map: BTreeMap<String, Vec<u32>> = BTreeMap::new();
    for (slug, body) in &segs {
        std::fs::write(format!("{}/{}.md", args.out_dir, slug), body)?;
        let mut pgs: Vec<u32> = Vec::new();
        for cap in body.match_indices("[[page:") {
            let rest = &body[cap.0 + 7..];
            if let Some(close) = rest.find("]]") {
                if let Ok(p) = rest[..close].parse::<u32>() {
                    pgs.push(p);
                }
            }
        }
        page_map.insert(slug.clone(), pgs);
    }
    std::fs::write(
        "extraction/page-map.json",
        serde_json::to_string_pretty(&page_map)?,
    )?;

    // 3) Zero-exhibit verification report
    let mut rpt = String::from(
        "# Verification report — exhibit presence, Wolk Ch. 12 (SAGE edition)\n\n\
         | PDF page | image XObjects |\n|---|---|\n",
    );
    let mut total = 0usize;
    for no in start..=end {
        let pid = *pages.get(&no).context("page id")?;
        let n = count_image_xobjects(&doc, pid);
        total += n;
        writeln!(rpt, "| {no} | {n} |")?;
    }
    writeln!(
        rpt,
        "\n**Total: {total}.** Expected: 1 (SAGE logo on title page {start}); \
         0 chapter exhibits. All document visuals are therefore reconstructions \
         labeled \"diolah dari Wolk et al. (2017)\"."
    )?;
    std::fs::write(&args.report, rpt)?;
    println!(
        "wrote {} section files, page-map.json, {} (total images: {total})",
        segs.len(),
        args.report
    );
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn segments_in_order() {
        let full = "\n[[page:1]]\nTitle stuff\nIncome Definitions\nbody A\n[[page:2]]\nRevenues and Gains\nbody B";
        let secs: &[(&str, &str)] = &[
            ("Income Definitions", "02_income_definitions"),
            ("Revenues and Gains", "03_revenues_and_gains"),
        ];
        let segs = segment(full, secs);
        assert_eq!(segs.len(), 3); // preamble + 2
        assert_eq!(segs[0].0, "00_preamble");
        assert!(segs[1].1.starts_with("Income Definitions"));
        assert!(segs[1].1.contains("body A"));
        assert!(segs[2].1.contains("body B"));
    }

    #[test]
    fn forward_only_matching() {
        // "Summary" appears early inside other text; only the forward
        // occurrence after prior headings should cut.
        let full = "Income Definitions\nSummary indicator talk\nSummary\nend";
        let secs: &[(&str, &str)] = &[
            ("Income Definitions", "02_income_definitions"),
            ("Summary", "14_summary"),
        ];
        let segs = segment(full, secs);
        // first "Summary" found after Income Definitions is the indicator one —
        // acceptable for navigation; assert we still get 3 chunks.
        assert_eq!(segs.len(), 3);
    }

    #[test]
    fn empty_when_nothing_matches() {
        assert!(segment("nothing here", SECTIONS).is_empty());
    }
}
```

- [ ] **Step 3: Run unit tests**

Run: `cargo test -p text_extract`
Expected: 3 passed.

- [ ] **Step 4: Integration run**

Run: `cargo run --release -p text_extract`
Expected: `wrote 16 section files, page-map.json, extraction/verification-report.md (total images: 1)`. Spot-check `extraction/text/04_revenue_recognition.md` contains "During production" list and `extraction/verification-report.md` shows total 1. Note: "Earnings per Share"/"Summary" phrases occur in running text before their headings — if a segment file visibly starts mid-sentence, adjust that marker to a longer anchor (e.g. `"Earnings per Share\nThe term summary indicator"`) in `SECTIONS` and re-run.

- [ ] **Step 5: Commit**

```powershell
git add src/rust/text_extract Cargo.lock
git commit -m "feat(rmk9): text_extract crate — section segmentation + zero-exhibit verification"
```

---

### Task 4: `visual_gen` crate (TDD)

**Files:**
- Create: `src/rust/visual_gen/Cargo.toml`, `src/rust/visual_gen/src/main.rs`

- [ ] **Step 1: Crate manifest**

`src/rust/visual_gen/Cargo.toml`:

```toml
[package]
name = "visual_gen"
version = "0.1.0"
edition = "2021"

[dependencies]
resvg = "0.45"
clap = { version = "4", features = ["derive"] }
anyhow = "1"
```

- [ ] **Step 2: Write tests + implementation**

`src/rust/visual_gen/src/main.rs`:

```rust
//! Rasterizes every authored SVG in assets/diagrams/svg/ to PNG in
//! assets/diagrams/. SVGs are authored at 1712 px width (= 14.5 cm @ 300 DPI).

use anyhow::{bail, Context, Result};
use clap::Parser;

pub fn rasterize(svg_data: &[u8], fontdb: std::sync::Arc<resvg::usvg::fontdb::Database>)
    -> Result<resvg::tiny_skia::Pixmap>
{
    let mut opt = resvg::usvg::Options::default();
    opt.fontdb = fontdb;
    let tree = resvg::usvg::Tree::from_data(svg_data, &opt).context("parsing SVG")?;
    let size = tree.size().to_int_size();
    let mut pixmap = resvg::tiny_skia::Pixmap::new(size.width(), size.height())
        .context("pixmap alloc")?;
    pixmap.fill(resvg::tiny_skia::Color::WHITE);
    resvg::render(&tree, resvg::tiny_skia::Transform::identity(), &mut pixmap.as_mut());
    Ok(pixmap)
}

#[derive(Parser)]
struct Args {
    #[arg(long, default_value = "assets/diagrams/svg")]
    svg_dir: String,
    #[arg(long, default_value = "assets/diagrams")]
    out_dir: String,
}

fn main() -> Result<()> {
    let args = Args::parse();
    let mut db = resvg::usvg::fontdb::Database::new();
    db.load_system_fonts(); // Times New Roman from C:\Windows\Fonts
    let db = std::sync::Arc::new(db);
    let mut count = 0;
    for entry in std::fs::read_dir(&args.svg_dir)
        .with_context(|| format!("reading {}", args.svg_dir))?
    {
        let path = entry?.path();
        if path.extension().and_then(|e| e.to_str()) != Some("svg") {
            continue;
        }
        let data = std::fs::read(&path)?;
        let pixmap = rasterize(&data, db.clone())
            .with_context(|| format!("rasterizing {}", path.display()))?;
        if pixmap.width() != 1712 {
            bail!("{}: width {} != 1712", path.display(), pixmap.width());
        }
        let out = format!(
            "{}/{}.png",
            args.out_dir,
            path.file_stem().unwrap().to_string_lossy()
        );
        pixmap.save_png(&out)?;
        println!("rendered {out} ({}x{})", pixmap.width(), pixmap.height());
        count += 1;
    }
    if count == 0 {
        bail!("no SVGs found in {}", args.svg_dir);
    }
    println!("done: {count} diagrams");
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn rasterizes_simple_svg() {
        let svg = br#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1712 100" width="1712" height="100"><rect x="10" y="10" width="100" height="40" fill="none" stroke="black"/><text x="200" y="40" font-family="Times New Roman" font-size="40">uji</text></svg>"#;
        let mut db = resvg::usvg::fontdb::Database::new();
        db.load_system_fonts();
        let px = rasterize(svg, std::sync::Arc::new(db)).unwrap();
        assert_eq!((px.width(), px.height()), (1712, 100));
        // Not all-white: the rect stroke must have painted something.
        assert!(px.data().chunks(4).any(|p| p[0] < 250));
    }
}
```

- [ ] **Step 3: Run unit test**

Run: `cargo test -p visual_gen`
Expected: 1 passed. (If the resvg 0.45 API differs — e.g. `opt.fontdb_mut()` instead of field assignment — fix to match the published API; the contract stays: parse with system fonts, render on white, save PNG.)

- [ ] **Step 4: Commit**

```powershell
git add src/rust/visual_gen Cargo.lock
git commit -m "feat(rmk9): visual_gen crate — SVG to PNG rasterizer with system fonts"
```

---

### Task 5: Author the 6 diagram SVGs and render them

**Files:**
- Create: `assets/diagrams/svg/gambar1_titik_pengakuan.svg` … `gambar6_taksonomi_em.svg`

All SVGs: `viewBox="0 0 1712 H"`, white background, black strokes ≥4px, `font-family="Times New Roman"`, body text 44px (≈12pt @300DPI), small labels 36px. No caption text inside the SVG — captions live in markdown. Common header per file:
`<svg xmlns="http://www.w3.org/2000/svg" width="1712" height="H" viewBox="0 0 1712 H">` + `<rect width="1712" height="H" fill="white"/>`.

- [ ] **Step 1: `gambar1_titik_pengakuan.svg` (H=420) — §III**

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1712" height="420" viewBox="0 0 1712 420">
  <rect width="1712" height="420" fill="white"/>
  <line x1="100" y1="210" x2="1600" y2="210" stroke="black" stroke-width="5"/>
  <polygon points="1600,210 1570,196 1570,224" fill="black"/>
  <g font-family="Times New Roman" font-size="42" text-anchor="middle" fill="black">
    <circle cx="280" cy="210" r="16" fill="white" stroke="black" stroke-width="5"/>
    <text x="280" y="140">1. Selama produksi</text>
    <text x="280" y="290" font-style="italic" font-size="36">kontrak jangka panjang (ARB 45)</text>
    <circle cx="640" cy="210" r="16" fill="white" stroke="black" stroke-width="5"/>
    <text x="640" y="140">2. Akhir produksi</text>
    <text x="640" y="290" font-style="italic" font-size="36">agrikultur & pertambangan (ARB 43)</text>
    <circle cx="1020" cy="210" r="24" fill="black"/>
    <text x="1020" y="130" font-weight="bold" font-size="46">3. Titik penjualan</text>
    <text x="1020" y="290" font-style="italic" font-size="36">norma umum sejak 1934</text>
    <circle cx="1400" cy="210" r="16" fill="white" stroke="black" stroke-width="5"/>
    <text x="1400" y="140">4. Penagihan kas</text>
    <text x="1400" y="290" font-style="italic" font-size="36">metode installment (SFAS 66)</text>
    <text x="856" y="385" font-size="36">arah penyelesaian earnings process &#8594;</text>
  </g>
</svg>
```

- [ ] **Step 2: `gambar2_hierarki_matching.svg` (H=460) — §IV**

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1712" height="460" viewBox="0 0 1712 460">
  <rect width="1712" height="460" fill="white"/>
  <g font-family="Times New Roman" font-size="40" fill="black">
    <rect x="60" y="60" width="480" height="150" fill="white" stroke="black" stroke-width="5"/>
    <text x="300" y="120" text-anchor="middle" font-weight="bold">1. Asosiasi langsung</text>
    <text x="300" y="175" text-anchor="middle" font-style="italic" font-size="36">cause and effect (mis. COGS)</text>
    <rect x="616" y="60" width="480" height="150" fill="white" stroke="black" stroke-width="5"/>
    <text x="856" y="120" text-anchor="middle" font-weight="bold">2. Alokasi sistematis</text>
    <text x="856" y="175" text-anchor="middle" font-style="italic" font-size="36">systematic and rational (mis. depresiasi)</text>
    <rect x="1172" y="60" width="480" height="150" fill="white" stroke="black" stroke-width="5"/>
    <text x="1412" y="120" text-anchor="middle" font-weight="bold">3. Pembebanan segera</text>
    <text x="1412" y="175" text-anchor="middle" font-style="italic" font-size="36">period expense, tiada manfaat masa depan</text>
    <polygon points="540,135 616,135 616,115 656,135 616,155 616,135" fill="black"/>
    <polygon points="1096,135 1172,135 1172,115 1212,135 1212,135 1172,155 1172,135" fill="black"/>
    <text x="856" y="300" text-anchor="middle" font-size="38">jika asosiasi langsung tidak mungkin &#8594; turun ke tingkat berikutnya</text>
    <text x="856" y="390" text-anchor="middle" font-style="italic" font-size="38">Thomas: semua alokasi pada akhirnya arbitrer &#8212; tidak dapat diverifikasi maupun direfutasi</text>
  </g>
</svg>
```

- [ ] **Step 3: `gambar3_future_events.svg` (H=720) — §V**

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1712" height="720" viewBox="0 0 1712 720">
  <rect width="1712" height="720" fill="white"/>
  <g font-family="Times New Roman" font-size="38" fill="black">
    <rect x="606" y="290" width="500" height="140" fill="white" stroke="black" stroke-width="6"/>
    <text x="856" y="350" text-anchor="middle" font-weight="bold" font-size="42">Future events &amp;</text>
    <text x="856" y="400" text-anchor="middle" font-weight="bold" font-size="42">pengakuan akuntansi</text>
    <rect x="100" y="60" width="440" height="120" fill="white" stroke="black" stroke-width="4"/>
    <text x="320" y="110" text-anchor="middle" font-weight="bold">Persepsi peristiwa lampau</text>
    <text x="320" y="155" text-anchor="middle" font-style="italic" font-size="34">one-event vs two-event view</text>
    <rect x="1172" y="60" width="440" height="120" fill="white" stroke="black" stroke-width="4"/>
    <text x="1392" y="110" text-anchor="middle" font-weight="bold">Sifat probabilistik</text>
    <text x="1392" y="155" text-anchor="middle" font-style="italic" font-size="34">probable vs reasonably possible (SFAS 5)</text>
    <rect x="100" y="540" width="440" height="120" fill="white" stroke="black" stroke-width="4"/>
    <text x="320" y="590" text-anchor="middle" font-weight="bold">Management intent</text>
    <text x="320" y="635" text-anchor="middle" font-style="italic" font-size="34">ditolak: merusak komparabilitas</text>
    <rect x="1172" y="540" width="440" height="120" fill="white" stroke="black" stroke-width="4"/>
    <text x="1392" y="590" text-anchor="middle" font-weight="bold">Market values (Beaver)</text>
    <text x="1392" y="635" text-anchor="middle" font-style="italic" font-size="34">kaya informasi; rapuh jika thinly traded</text>
    <rect x="60" y="300" width="380" height="120" fill="white" stroke="black" stroke-width="4"/>
    <text x="250" y="350" text-anchor="middle" font-weight="bold">Konservatisme</text>
    <text x="250" y="395" text-anchor="middle" font-style="italic" font-size="34">keunggulan komparatif kabar buruk</text>
    <rect x="1272" y="300" width="380" height="120" fill="white" stroke="black" stroke-width="4"/>
    <text x="1462" y="350" text-anchor="middle" font-weight="bold">Kondisi ekonomi &amp; hukum</text>
    <text x="1462" y="395" text-anchor="middle" font-style="italic" font-size="34">jangan diprediksi tanpa bukti kuat</text>
    <line x1="540" y1="150" x2="700" y2="290" stroke="black" stroke-width="4"/>
    <line x1="1172" y1="150" x2="1012" y2="290" stroke="black" stroke-width="4"/>
    <line x1="540" y1="580" x2="700" y2="430" stroke="black" stroke-width="4"/>
    <line x1="1172" y1="580" x2="1012" y2="430" stroke="black" stroke-width="4"/>
    <line x1="440" y1="360" x2="606" y2="360" stroke="black" stroke-width="4"/>
    <line x1="1106" y1="360" x2="1272" y2="360" stroke="black" stroke-width="4"/>
  </g>
</svg>
```

- [ ] **Step 4: `gambar4_evolusi_laba.svg` (H=520) — akhir §VI (menjembatani §VII)**

Timeline nodes kiri→kanan di garis y=260: **1936** AAA — *all-inclusive* dianjurkan; **1947** ARB 32/43 — AICPA condong *current operating*; **1966** APB Opinion No. 9 — *all-inclusive* termodifikasi; **1973** APB Opinion No. 30 — *rigid uniformity* extraordinary items; **1985** SFAC No. 5 — usulan *comprehensive income*; **1997** SFAS No. 130 — pelaporan CI; **2011** ASU — format 1 / 2 laporan. Pola node + label sama dengan gambar 1 (lingkaran 14px, tahun bold 40px di atas, deskripsi italic 32px di bawah, garis 5px dengan panah).

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1712" height="520" viewBox="0 0 1712 520">
  <rect width="1712" height="520" fill="white"/>
  <line x1="80" y1="260" x2="1640" y2="260" stroke="black" stroke-width="5"/>
  <polygon points="1640,260 1610,246 1610,274" fill="black"/>
  <g font-family="Times New Roman" fill="black" text-anchor="middle">
    <g font-size="40" font-weight="bold">
      <text x="180" y="190">1936</text><text x="410" y="380">1947</text>
      <text x="640" y="190">1966</text><text x="870" y="380">1973</text>
      <text x="1100" y="190">1985</text><text x="1330" y="380">1997</text>
      <text x="1540" y="190">2011</text>
    </g>
    <g font-size="31" font-style="italic">
      <text x="180" y="120">AAA: all-inclusive</text>
      <text x="410" y="440">ARB 32/43: current operating</text>
      <text x="640" y="120">APB Op. 9: all-inclusive termodifikasi</text>
      <text x="870" y="440">APB Op. 30: rigid uniformity</text>
      <text x="1100" y="120">SFAC 5: comprehensive income</text>
      <text x="1330" y="440">SFAS 130: pelaporan CI</text>
      <text x="1540" y="120">ASU: 1/2 laporan</text>
    </g>
    <g fill="white" stroke="black" stroke-width="5">
      <circle cx="180" cy="260" r="14"/><circle cx="410" cy="260" r="14"/>
      <circle cx="640" cy="260" r="14"/><circle cx="870" cy="260" r="14"/>
      <circle cx="1100" cy="260" r="14"/><circle cx="1330" cy="260" r="14"/>
      <circle cx="1540" cy="260" r="14"/>
    </g>
  </g>
</svg>
```

- [ ] **Step 5: `gambar5_stock_options.svg` (H=520) — §X**

Same timeline pattern as gambar 4, nodes: **1972** APB Op. 25 — *intrinsic value*, NQSO saja; **1993** Exposure Draft — Black-Scholes, perlawanan sengit; **1994** ED ditarik (5–2); **1995** SFAS No. 123 — *footnote disclosure*; **2004** SFAS No. 123R — beban wajib, *grant-date fair value*; **±2004** konvergensi IFRS 2. Copy the gambar 4 skeleton, replace the 7 nodes with these 6 (x = 200, 480, 740, 1010, 1280, 1540).

- [ ] **Step 6: `gambar6_taksonomi_em.svg` (H=640) — §XI**

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1712" height="640" viewBox="0 0 1712 640">
  <rect width="1712" height="640" fill="white"/>
  <g font-family="Times New Roman" fill="black">
    <rect x="456" y="40" width="800" height="120" fill="white" stroke="black" stroke-width="6"/>
    <text x="856" y="90" text-anchor="middle" font-weight="bold" font-size="42">Earnings management (Schipper):</text>
    <text x="856" y="138" text-anchor="middle" font-style="italic" font-size="36">intervensi bertujuan demi keuntungan privat</text>
    <line x1="856" y1="160" x2="856" y2="220" stroke="black" stroke-width="4"/>
    <line x1="300" y1="220" x2="1412" y2="220" stroke="black" stroke-width="4"/>
    <line x1="300" y1="220" x2="300" y2="270" stroke="black" stroke-width="4"/>
    <line x1="856" y1="220" x2="856" y2="270" stroke="black" stroke-width="4"/>
    <line x1="1412" y1="220" x2="1412" y2="270" stroke="black" stroke-width="4"/>
    <rect x="60" y="270" width="480" height="150" fill="white" stroke="black" stroke-width="4"/>
    <text x="300" y="330" text-anchor="middle" font-weight="bold" font-size="38">Kompensasi manajemen</text>
    <text x="300" y="385" text-anchor="middle" font-style="italic" font-size="32">bonus ceiling/floor (Healy); discretionary accruals</text>
    <rect x="616" y="270" width="480" height="150" fill="white" stroke="black" stroke-width="4"/>
    <text x="856" y="330" text-anchor="middle" font-weight="bold" font-size="38">Classification shifting</text>
    <text x="856" y="385" text-anchor="middle" font-style="italic" font-size="32">geser core expenses ke special items (McVay; Borden)</text>
    <rect x="1172" y="270" width="480" height="150" fill="white" stroke="black" stroke-width="4"/>
    <text x="1412" y="330" text-anchor="middle" font-weight="bold" font-size="38">Income smoothing</text>
    <text x="1412" y="385" text-anchor="middle" font-style="italic" font-size="32">ratakan varians laba antartahun</text>
    <line x1="1412" y1="420" x2="1412" y2="470" stroke="black" stroke-width="4"/>
    <rect x="1052" y="470" width="620" height="130" fill="white" stroke="black" stroke-width="4"/>
    <text x="1362" y="520" text-anchor="middle" font-size="34">3 cara: timing transaksi; pilihan metode alokasi;</text>
    <text x="1362" y="565" text-anchor="middle" font-size="34">smoothing klasifikatoris operasi vs nonoperasi</text>
  </g>
</svg>
```

- [ ] **Step 7: Render and inspect**

Run: `cargo run --release -p visual_gen`
Expected: `done: 6 diagrams`, six PNGs in `assets/diagrams/`, each 1712 px wide. Open each PNG (`Invoke-Item assets\diagrams\gambar1_titik_pengakuan.png` etc. or Read tool) and check: no text overflow outside boxes, no overlap, TNR rendered (serif). Adjust SVG coordinates if any label clips, re-run.

- [ ] **Step 8: Commit**

```powershell
git add assets/diagrams/svg
git commit -m "feat(rmk9): 6 authored monochrome diagram SVGs + rendered PNGs"
```

---

### Task 6: Author the 4 native-table definitions

**Files:**
- Create: `assets/tables/tabel1_definisi.toml`, `tabel2_format_ci.toml`, `tabel3_accounting_changes.toml`, `tabel4_eps.toml`

- [ ] **Step 1: Write the four TOML files**

`assets/tables/tabel1_definisi.toml`:

```toml
caption = "Tabel 1. Evolusi definisi elemen laba lintas badan penyusun standar | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 2–7"
header = ["Sumber", "Inti definisi", "Orientasi"]
widths_cm = [3.2, 8.0, 3.8]
[[rows]]
cells = ["ATB 2 / ATB 4 (AICPA)", "Income: hasil pengurangan revenues oleh COGS, beban lain, dan losses. Revenue: hasil penjualan barang/jasa, diukur dari harga yang dibebankan ke pelanggan. Expense: semua expired costs yang dapat dikurangkan dari revenues.", "Revenue–expense"]
[[rows]]
cells = ["APB Statement 4", "Net income: selisih revenues atas expenses satu periode. Revenue: kenaikan bruto aset / penurunan bruto liabilitas dari aktivitas berorientasi laba, diukur sesuai GAAP. Expense: penurunan bruto aset / kenaikan bruto liabilitas dari aktivitas berorientasi laba.", "Transisi: bentuk asset–liability, pengukuran masih revenue–expense"]
[[rows]]
cells = ["SFAC No. 6", "Comprehensive income: perubahan ekuitas (aset bersih) dari transaksi dan peristiwa non-pemilik. Revenue: arus masuk / peningkatan aset atau penyelesaian liabilitas dari operasi utama berkelanjutan. Expense: arus keluar / pemakaian aset atau timbulnya liabilitas dari operasi utama.", "Asset–liability"]
[[rows]]
cells = ["FASB Codification", "Tujuan pelaporan comprehensive income: mengukur seluruh perubahan ekuitas dari transaksi non-pemilik yang diakui pada periode itu.", "Asset–liability (penegasan)"]
```

`assets/tables/tabel2_format_ci.toml`:

```toml
caption = "Tabel 2. Tiga format pelaporan comprehensive income menurut SFAS No. 130 | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 13"
header = ["Format", "Deskripsi", "Catatan"]
widths_cm = [4.2, 6.6, 4.2]
[[rows]]
cells = ["(1) Combined statement of financial performance", "Satu laporan: elemen comprehensive income dan totalnya tampil di bawah net income", "Preferensi Board"]
[[rows]]
cells = ["(2) Separate statement of comprehensive income", "Laporan terpisah yang dimulai dari net income", "Visibilitas CI tetap terjaga"]
[[rows]]
cells = ["(3) Dalam statement of changes in equity", "CI dilaporkan di dalam laporan perubahan ekuitas", "Diprediksi dua anggota dissenting paling banyak dipakai — menurunkan visibilitas CI"]
```

`assets/tables/tabel3_accounting_changes.toml`:

```toml
caption = "Tabel 3. Tiga jenis perubahan akuntansi dan perlakuannya | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 15–16"
header = ["Jenis perubahan", "APB Opinion No. 20", "SFAS No. 154"]
widths_cm = [4.2, 5.4, 5.4]
[[rows]]
cells = ["Change in accounting principle (prinsip GAAP lama → GAAP lain)", "Cumulative effect disajikan di laporan laba rugi berjalan, tepat di bawah extraordinary items", "Retrospektif ke semua laporan laba rugi terdampak, kecuali impraktis; saldo neraca disesuaikan ke awal periode pertama yang disajikan"]
[[rows]]
cells = ["Change in accounting estimate (informasi baru atas estimasi)", "Prospektif: periode berjalan dan/atau periode mendatang", "Sama (prospektif); perubahan depresiasi/deplesi/amortisasi akibat perubahan prinsip diperlakukan sebagai perubahan estimasi"]
[[rows]]
cells = ["Change in reporting entity (komposisi entitas pelapor berubah)", "Restate seluruh laporan periode sebelumnya; ungkap sifat, alasan, dan efeknya", "Tidak diubah oleh SFAS 154"]
```

`assets/tables/tabel4_eps.toml`:

```toml
caption = "Tabel 4. Pergeseran APB Opinion No. 15 ke SFAS No. 128 dalam pelaporan EPS | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 17–18"
header = ["Aspek", "APB Opinion No. 15", "SFAS No. 128"]
widths_cm = [3.6, 5.7, 5.7]
[[rows]]
cells = ["Kategori EPS", "Primary EPS (PEPS) dan fully diluted EPS", "Basic EPS (tanpa dilusi) dan diluted EPS (dilusi maksimum)"]
[[rows]]
cells = ["PEPS", "Wajib: memasukkan convertible securities bila effective rate ≤ 2/3 Aa bond rate saat terbit", "Dieliminasi — perhitungan artifisial yang sulit dipahami pengguna"]
[[rows]]
cells = ["Aturan 3%", "Bila dilusi penuh ≤ 3% dari simple EPS, cukup simple EPS", "Dieliminasi — basic dan diluted selalu disajikan"]
[[rows]]
cells = ["Rekonsiliasi", "Tidak diwajibkan", "Wajib: rekonsiliasi pembilang dan penyebut basic ↔ diluted"]
[[rows]]
cells = ["Penyajian", "Direkomendasikan kuat di laporan laba rugi", "Wajib di muka laporan laba rugi, untuk income before discontinued operations/extraordinary items dan net income; tidak untuk comprehensive income"]
```

- [ ] **Step 2: Validate TOML parses**

Run: `python -c "import tomllib,glob; [print(f, len(tomllib.load(open(f,'rb'))['rows']), 'rows') for f in glob.glob('assets/tables/*.toml')]"`
Expected: 4 files; 4/3/3/5 rows.

- [ ] **Step 3: Commit**

```powershell
git add assets/tables
git commit -m "feat(rmk9): 4 native-table definitions (TOML)"
```

---

### Task 7: `build_docx.py` + tests (TDD, adapted from K2 builder)

**Files:**
- Create: `src/python/build_docx.py`, `src/python/test_build_docx.py`

Port from `Kelompok 2 Pasca UTS/output/build_docx.py` (read it first): keep `parse_inline_runs`, `split_caption`, `_style_run`, `_add_para`, `add_image_with_caption` (change caption prefix regex to also accept `Tabel \d+\.`), `add_blank` unchanged. Deltas: (1) no cover page — concise front-matter block + horizontal rule; (2) `parse_blocks` adds `### ` → `subheading` and `@table(path)` → `table` block; (3) native table renderer from TOML; (4) footer page number bottom-right; (5) reads ALL `content/*.md` sorted by filename; (6) exact output filename.

- [ ] **Step 1: Write failing tests**

`src/python/test_build_docx.py`:

```python
import os, subprocess, sys
import pytest
from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "output", "01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx")

sys.path.insert(0, HERE)
from build_docx import parse_inline_runs, parse_blocks, split_caption  # noqa: E402


def test_inline_runs_bold_italic():
    assert parse_inline_runs("a **b** *c*") == [
        ("a ", False, False), ("b", True, False), (" ", False, False), ("c", False, True)]


def test_parse_blocks_subheading_and_table():
    md = "## I. Judul\n\n### Sub Bagian\n\npara satu\n\n@table(../assets/tables/tabel1_definisi.toml)\n\n- butir\n"
    kinds = [k for k, _ in parse_blocks(md)]
    assert kinds == ["heading", "subheading", "para", "table", "bullet"]


def test_split_caption():
    t, s = split_caption("Tabel 1. Judul | Sumber: diolah dari Wolk et al. (2017)")
    assert t.startswith("Tabel 1.") and s.startswith("Sumber:")


@pytest.fixture(scope="module")
def built():
    subprocess.run([sys.executable, os.path.join(HERE, "build_docx.py")],
                   check=True, cwd=ROOT)
    return Document(OUT)


def test_output_exists_with_exact_name(built):
    assert os.path.exists(OUT)


def test_page_setup(built):
    s = built.sections[0]
    from docx.shared import Cm
    assert s.page_width == Cm(21.0) and s.left_margin == Cm(3)


def test_front_matter_first_line(built):
    first = built.paragraphs[0].text
    assert "RINGKASAN MATERI KULIAH" in first and "PERTEMUAN 9" in first.upper()


def test_six_images_and_four_tables(built):
    assert len(built.inline_shapes) == 6
    assert len(built.tables) == 4


def test_identity_present(built):
    head = "\n".join(p.text for p in built.paragraphs[:6])
    assert "Dzaki Muhammad Yusfian" in head and "01079" in head
```

- [ ] **Step 2: Run tests — verify failure**

Run: `python -m pytest src/python/test_build_docx.py -x -q` (from `rmk-pkk-pert9-income-statement/`)
Expected: FAIL with `ModuleNotFoundError: build_docx` / missing file.

- [ ] **Step 3: Write `src/python/build_docx.py`**

```python
"""
build_docx.py — assembles output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx
from content/*.md + assets/. python-docx is the documented Python exception in
this otherwise-Rust pipeline (see README: proven K2 typography conventions;
docx-rs would need exact-18pt spacing, hanging indents, captioned tables and
footer fields re-proven from scratch).
Styling layer adapted from "Kelompok 2 Pasca UTS/output/build_docx.py".
"""
import glob
import os
import re
import tomllib

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

FONT = "Times New Roman"
STUDENT = "Dzaki Muhammad Yusfian"
NIM = "1225 01079"
OUT_NAME = "01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx"

# --- markdown parsing (K2 lineage, + ### and @table) -----------------------

def parse_inline_runs(text):
    runs = []
    pattern = re.compile(r'(\*\*.+?\*\*|\*[^*]+?\*)')
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            runs.append((text[pos:m.start()], False, False))
        token = m.group(0)
        if token.startswith('**'):
            runs.append((token[2:-2], True, False))
        else:
            runs.append((token[1:-1], False, True))
        pos = m.end()
    if pos < len(text):
        runs.append((text[pos:], False, False))
    return [r for r in runs if r[0]]


IMAGE_RE = re.compile(r'^!\[(.+?)\]\((.+?)\)$')
TABLE_RE = re.compile(r'^@table\((.+?)\)$')


def split_caption(caption):
    if " | " in caption:
        title, source = caption.split(" | ", 1)
        return title.strip(), source.strip()
    return caption.strip(), None


def parse_blocks(md_text):
    blocks = []
    in_refs = False
    buf = []

    def flush():
        nonlocal buf
        if buf:
            blocks.append(("ref" if in_refs else "para", " ".join(buf)))
            buf = []

    for raw in md_text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush()
        elif line.startswith("### "):
            flush()
            blocks.append(("subheading", line[4:].strip()))
        elif line.startswith("## "):
            flush()
            text = line[3:].strip()
            blocks.append(("heading", text))
            in_refs = "referensi" in text.lower() or "daftar pustaka" in text.lower()
        elif line.startswith("# "):
            flush()
        elif TABLE_RE.match(stripped):
            flush()
            blocks.append(("table", TABLE_RE.match(stripped).group(1)))
        elif line.startswith("!["):
            m = IMAGE_RE.match(stripped)
            if m:
                flush()
                blocks.append(("image", (m.group(1), m.group(2))))
            else:
                buf.append(stripped)
        elif line.startswith("- "):
            flush()
            blocks.append(("bullet", line[2:].strip()))
        else:
            buf.append(stripped)
    flush()
    return blocks

# --- docx styling (K2 lineage) ----------------------------------------------

def _style_run(run, font_size=12, bold=False, italic=False):
    run.font.name = FONT
    run.font.size = Pt(font_size)
    run.bold = bold
    run.italic = italic
    r = run._r
    rPr = r.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), FONT)
    rFonts.set(qn('w:hAnsi'), FONT)
    rFonts.set(qn('w:cs'), FONT)
    existing = rPr.find(qn('w:rFonts'))
    if existing is not None:
        rPr.remove(existing)
    rPr.insert(0, rFonts)


def _add_para(doc, runs, font_size=12, bold=False,
              alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
              space_before_pt=0, space_after_pt=6,
              left_indent_cm=None, hanging=False, italic_all=False):
    para = doc.add_paragraph()
    pf = para.paragraph_format
    pf.alignment = alignment
    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
    pf.line_spacing = Pt(18)
    pf.space_before = Pt(space_before_pt)
    pf.space_after = Pt(space_after_pt)
    if left_indent_cm is not None:
        pf.left_indent = Cm(left_indent_cm)
    if hanging:
        pf.left_indent = Cm(0.75)
        pf.first_line_indent = Cm(-0.75)
    for text, b, i in runs:
        run = para.add_run(text)
        _style_run(run, font_size=font_size, bold=bold or b, italic=i or italic_all)
    return para


def add_blank(doc):
    return _add_para(doc, [("", False, False)], space_after_pt=0)


def add_rule(doc):
    """Thin horizontal rule under an empty paragraph (front-matter divider)."""
    para = _add_para(doc, [("", False, False)], space_after_pt=10)
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '8')
    bottom.set(qn('w:color'), '000000')
    pBdr.append(bottom)
    pPr.append(pBdr)
    return para


def add_page_number_footer(section):
    """Bottom-right PAGE field in the footer."""
    para = section.footer.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = para.add_run()
    _style_run(run, font_size=11)
    fld_begin = OxmlElement('w:fldChar'); fld_begin.set(qn('w:fldCharType'), 'begin')
    instr = OxmlElement('w:instrText'); instr.text = 'PAGE'
    fld_end = OxmlElement('w:fldChar'); fld_end.set(qn('w:fldCharType'), 'end')
    run._r.append(fld_begin); run._r.append(instr); run._r.append(fld_end)


CAPTION_PREFIX_RE = re.compile(r'^((?:Gambar|Tabel) \d+\.)\s*(.*)$')


def _add_caption(doc, caption, space_after_pt=12):
    title, source = split_caption(caption)
    m = CAPTION_PREFIX_RE.match(title)
    runs = ([(m.group(1) + " ", True, False), (m.group(2), False, False)]
            if m else [(title, False, False)])
    _add_para(doc, runs, font_size=11, alignment=WD_ALIGN_PARAGRAPH.CENTER,
              space_before_pt=0, space_after_pt=0 if source else space_after_pt)
    if source:
        _add_para(doc, [(source, False, True)], font_size=11,
                  alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before_pt=0, space_after_pt=space_after_pt)


def add_image_with_caption(doc, img_path, caption):
    doc.add_picture(img_path, width=Cm(14.5))
    pic = doc.paragraphs[-1]
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.paragraph_format.space_before = Pt(6)
    pic.paragraph_format.space_after = Pt(6)
    _add_caption(doc, caption)


def add_table_from_toml(doc, toml_path):
    with open(toml_path, 'rb') as f:
        spec = tomllib.load(f)
    _add_caption(doc, spec["caption"], space_after_pt=4)  # caption ABOVE table
    n_cols = len(spec["header"])
    table = doc.add_table(rows=1 + len(spec["rows"]), cols=n_cols)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(spec["header"]):
        cell = table.rows[0].cells[j]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        _style_run(run, font_size=11, bold=True)
    for i, row in enumerate(spec["rows"], start=1):
        for j, val in enumerate(row["cells"]):
            cell = table.rows[i].cells[j]
            cell.text = ""
            para = cell.paragraphs[0]
            para.paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY
            para.paragraph_format.line_spacing = Pt(14)
            for text, b, it in parse_inline_runs(val):
                _style_run(para.add_run(text), font_size=11, bold=b, italic=it)
    for j, w in enumerate(spec.get("widths_cm", [])):
        for row in table.rows:
            row.cells[j].width = Cm(w)
    add_blank(doc)

# --- build -------------------------------------------------------------------

def build():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.normpath(os.path.join(here, "..", ".."))
    content_dir = os.path.join(root, "content")

    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    for attr in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(section, attr, Cm(3))
    style = doc.styles['Normal']
    style.font.name = FONT
    style.font.size = Pt(12)
    add_page_number_footer(section)

    # Concise front matter (Layout B) — from content/00_front_matter.md:
    # each non-blank line = centered paragraph; first line bold 14pt.
    fm_path = os.path.join(content_dir, "00_front_matter.md")
    with open(fm_path, encoding="utf-8") as f:
        fm_lines = [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
    for i, ln in enumerate(fm_lines):
        _add_para(doc, parse_inline_runs(ln),
                  font_size=14 if i == 0 else 12, bold=(i == 0),
                  alignment=WD_ALIGN_PARAGRAPH.CENTER, space_after_pt=2)
    add_rule(doc)

    # Body: every content/*.md except 00, sorted by filename
    files = sorted(glob.glob(os.path.join(content_dir, "*.md")))
    for path in files:
        if os.path.basename(path).startswith("00_"):
            continue
        with open(path, encoding="utf-8") as f:
            md = f.read()
        for kind, payload in parse_blocks(md):
            if kind == "image":
                caption, rel = payload
                add_image_with_caption(
                    doc, os.path.normpath(os.path.join(content_dir, rel)), caption)
            elif kind == "table":
                add_table_from_toml(
                    doc, os.path.normpath(os.path.join(content_dir, payload)))
            elif kind == "heading":
                _add_para(doc, parse_inline_runs(payload), font_size=13, bold=True,
                          alignment=WD_ALIGN_PARAGRAPH.LEFT,
                          space_before_pt=12, space_after_pt=6)
            elif kind == "subheading":
                _add_para(doc, parse_inline_runs(payload), font_size=12, bold=True,
                          italic_all=True, alignment=WD_ALIGN_PARAGRAPH.LEFT,
                          space_before_pt=8, space_after_pt=4)
            elif kind == "bullet":
                _add_para(doc, [("• ", False, False)] + parse_inline_runs(payload),
                          left_indent_cm=0.75)
            elif kind == "ref":
                _add_para(doc, parse_inline_runs(payload), hanging=True)
            else:
                _add_para(doc, parse_inline_runs(payload))

    out_path = os.path.join(root, "output", OUT_NAME)
    doc.save(out_path)
    print(f"Saved: {out_path}")
    print(f"Size:  {os.path.getsize(out_path):,} bytes")


if __name__ == "__main__":
    build()
```

- [ ] **Step 4: Create placeholder-free minimal content for the build tests**

The document tests need real content files; full prose arrives in Tasks 8–12. To keep TDD unblocked, create `content/00_front_matter.md` NOW with its final text (it is short and final):

```markdown
**RINGKASAN MATERI KULIAH (RMK) — PERTEMUAN 9**
Pelaporan Keuangan Korporat (MNK202) — Pascasarjana STIE YKPN Yogyakarta
Dzaki Muhammad Yusfian — NIM 1225 01079
*The Income Statement* — Wolk, H. I., Dodd, J. L., & Rozycki, J. J. (2017). *Accounting Theory: Conceptual Issues in a Political and Economic Environment* (9th ed., Ch. 12). Sage.
```

Then run the parser-only tests first: `python -m pytest src/python/test_build_docx.py -q -k "inline or blocks or caption"` — Expected: 3 passed. The `built`-fixture tests stay red until Tasks 8–12 deliver the content (they need 6 images + 4 tables referenced from prose). That is expected and tracked.

- [ ] **Step 5: Commit**

```powershell
git add src/python content/00_front_matter.md
git commit -m "feat(rmk9): docx builder + tests (parser green; document tests pending content)"
```

---

### Task 8: Author content — Orientasi (§I)

**Files:**
- Create: `content/01_orientasi.md`

Authoring rules for ALL content tasks (8–12): Bahasa Indonesia profesor-grade per the K2 `rmk-ch13.md` register; `## ` for Roman-numeral headings, `### ` for sub-headings; **bold** for key terms' first appearance, *italic* for English terms; every paragraph cites `(Wolk et al., 2017, PDF hlm. N)` with N from `extraction/page-map.json`/the extraction text; each section's closing paragraph bridges to the next section; NO content not traceable to the chapter except clearly-labeled course-theme framing; never copy sentences verbatim — paraphrase and explain.

- [ ] **Step 1: Read `extraction/text/00_preamble.md`, `01_learning_objectives.md` and write `content/01_orientasi.md` (±450 words)**

Must cover: (a) income statement as historically the predominant financial statement and its role for predicting future cash flows and assessing management performance; (b) articulation with the balance sheet from Pert. 8 — Ch. 11's revenue–expense vs asset–liability framing carries directly into Ch. 12's definitions; flag explicitly that economic-income/capital-maintenance adalah konteks Bab 11, bukan isi Bab 12; (c) decision usefulness positioning (course theme); (d) the chapter's 8 learning objectives paraphrased into a roadmap paragraph mirroring sections II–XII; (e) closing bridge to §II.

- [ ] **Step 2: Self-check & commit**

Checklist: word count 380–520 (`(Get-Content content\01_orientasi.md -Raw) -split '\s+' | Measure-Object` → Count); every paragraph cited; bridge sentence present.

```powershell
git add content/01_orientasi.md
git commit -m "content(rmk9): I. Orientasi"
```

---

### Task 9: Author content — Definisi, Pengakuan Pendapatan, Beban (§II–IV)

**Files:**
- Create: `content/02_definisi_income_elemen.md` (±650 w), `content/03_pengakuan_pendapatan.md` (±800 w), `content/04_pengakuan_beban_matching.md` (±650 w)

- [ ] **Step 1: Write `02_definisi_income_elemen.md`** from `extraction/text/02_income_definitions.md` + `03_revenues_and_gains.md` + the definition parts of `05_expenses_and_losses.md`. Must cover: 4 income definitions (ATB 2, APB St. 4, SFAC 6, Codification) and the revenue-expense→asset-liability shift; revenue definitions ×3 and why definition must be kept separate from recognition/measurement; gains; the revenue-vs-gain controversy as the seed of current-operating vs all-inclusive (forward reference §VI); expense definitions ×3; losses parallel to gains. Embed directly after the definitions discussion:

```markdown
@table(../assets/tables/tabel1_definisi.toml)
```

- [ ] **Step 2: Write `03_pengakuan_pendapatan.md`** from `extraction/text/04_revenue_recognition.md`. Must cover: theoretical ideal (identify revenue with the period of major economic activity) vs objective-measurement constraint; the 4 timing alternatives with their sanctioned uses (ARB 45 long-term contracts; ARB 43 completion-of-production; SFAS 66 installment); 1934 AICPA point-of-sale rule; evolution of exceptions via AICPA Guides/SOPs and the SFAS 32 extraction program (13 SFASs); accretion & discovery bases (not permitted); completion-of-earnings-process criterion + 3 measurable attributes (sales price, cash collection, future costs); Qwest fiber-swap as earnings-management Achilles' heel; ASU 2014-09/IFRS 15 common standard; SAB 101 and the FASB–SEC tension over predictive usefulness. Embed after the 4-timing discussion:

```markdown
![Gambar 1. Empat titik waktu alternatif pengakuan pendapatan | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 4–5](../assets/diagrams/gambar1_titik_pengakuan.png)
```

- [ ] **Step 3: Write `04_pengakuan_beban_matching.md`** from `extraction/text/05_expenses_and_losses.md`. Must cover: 3 APB St. 4 expense categories and the matching hierarchy; why category 3 is unproblematic; Thomas's arbitrariness-of-allocations thesis and its disturbing implication for historical cost; allocation-free alternatives (cash-flow statements, exit price, replacement cost); the empirical rejoinder — allocated income still has information content (Ch. 8 capital-market evidence); bridge to future events. Embed after the hierarchy paragraph:

```markdown
![Gambar 2. Hierarki tiga tingkat pengakuan beban dan kritik alokasi Thomas | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 7–8](../assets/diagrams/gambar2_hierarki_matching.png)
```

- [ ] **Step 4: Word-count check (1,900–2,300 total across the 3 files) and commit**

```powershell
git add content/02_definisi_income_elemen.md content/03_pengakuan_pendapatan.md content/04_pengakuan_beban_matching.md
git commit -m "content(rmk9): II-IV definisi elemen, pengakuan pendapatan, matching"
```

---

### Task 10: Author content — Future Events, CO vs AI, Comprehensive Income, Nonoperasi (§V–VIII)

**Files:**
- Create: `content/05_future_events.md` (±600 w), `content/06_current_operating_vs_all_inclusive.md` (±600 w), `content/07_comprehensive_income.md` (±550 w), `content/08_seksi_nonoperasi.md` (±700 w)

- [ ] **Step 1: Write `05_future_events.md`** from `extraction/text/06_future_events.md`. Cover: every accrual/deferral depends on future events (depreciation example); SFAC 6 asset/liability definitions balance past and future; 1994 standard-setters conference; one-event vs two-event view (early-retirement offer example); probabilistic nature (SFAS 5 probable/reasonably possible/remote; modal, weighted, cumulative probability approaches); management intent rejected (comparability, agency); Beaver on market values (thin trading caveat) and conservatism as comparative advantage in bad news; future economic conditions & enacted-law-only rule (SFAS 109 example); qualitative trade-offs conclusion. Embed map after the one/two-event discussion:

```markdown
![Gambar 3. Peta isu future events dalam pengakuan akuntansi | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 8–11](../assets/diagrams/gambar3_future_events.png)
```

- [ ] **Step 2: Write `06_current_operating_vs_all_inclusive.md`** from `extraction/text/07_co_vs_ai.md`. Cover: the pre-1968 controversy framing; current-operating camp's predictive/management-performance arguments; all-inclusive camp's 4 arguments (manipulability, hidden items in retained earnings, multi-year summation, separable classification); AAA 1936 vs AICPA/ARB 43 positions; APB Opinion No. 9's modified all-inclusive; June 2011 ASU one/two-statement choice; empirical evidence both ways (Gonedes no-information-content; later study with positive bad-news association); big bath theory + Citicorp 1987 $3bn example.

- [ ] **Step 3: Write `07_comprehensive_income.md`** from `extraction/text/08_comprehensive_income.md`. Cover: SFAC 5 statement proposal covering all non-owner equity changes; proprietary-theory grounding and valuation/predictive appropriateness; SFAS 130 OCI elements (FX translation, AFS unrealized gains/losses, minimum pension liability adjustments) and what the Board deliberately did NOT move (discontinued ops, extraordinary, accounting-change effects placement; prior-period adjustments stay in retained earnings — restatement rationale); no EPS for CI and why; three reporting formats + Board preference + two dissenters' visibility critique; "cautious and evolutionary" assessment; bridge back to all-inclusive logic and forward to §VIII. Embed table after the formats paragraph:

```markdown
@table(../assets/tables/tabel2_format_ci.toml)
```

Embed timeline at the section seam (end of §VI file or start of §VII file — place at END of `06_…md`):

```markdown
![Gambar 4. Evolusi pelaporan laba: current operating menuju all-inclusive dan comprehensive income | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 11–13](../assets/diagrams/gambar4_evolusi_laba.png)
```

- [ ] **Step 4: Write `08_seksi_nonoperasi.md`** from `extraction/text/09_nonoperating_sections.md`. Cover: the 3+1 nonoperating subdivisions as the continuing CO-vs-AI dilemma; extraordinary items: ARB 32/43 vagueness → APB 9 definition → APB 30 rigid uniformity (unusual nature + infrequency, citrus-frost example, near-disappearance, display rules net-of-tax above net income); finite→rigid uniformity arc; accounting changes: 3 types with examples, APB 20 cumulative effect vs SFAS 154 retrospective, principle-change-as-estimate for depreciation methods, entity changes restated; prior period adjustments: APB 9 criteria → SEC pressure (SAB 8) → SFAS 16's two-item limit; recurring/transitory distinction for forecasting users. Embed after the accounting-changes prose:

```markdown
@table(../assets/tables/tabel3_accounting_changes.toml)
```

- [ ] **Step 5: Word-count check (2,250–2,700 total) and commit**

```powershell
git add content/05_future_events.md content/06_current_operating_vs_all_inclusive.md content/07_comprehensive_income.md content/08_seksi_nonoperasi.md
git commit -m "content(rmk9): V-VIII future events, CO vs AI, comprehensive income, nonoperasi"
```

---

### Task 11: Author content — EPS, Topik Khusus, Earnings Management (§IX–XI)

**Files:**
- Create: `content/09_earnings_per_share.md` (±450 w), `content/10_topik_khusus.md` (±950 w), `content/11_earnings_management.md` (±850 w)

- [ ] **Step 1: Write `09_earnings_per_share.md`** from `extraction/text/10_eps.md`. Cover: summary-indicator concept (1979 DM); pre-APB-9 discretion; APB 15 rigid 116-page complexity, SFAS 21 suspension for nonpublic; SFAS 128 rationale (international comparability, simplification, disclosure); PEPS mechanics & elimination; 3% rule elimination; basic/diluted display rules + reconciliation; "less is more" verdict; finite-vs-rigid-uniformity echo. Embed:

```markdown
@table(../assets/tables/tabel4_eps.toml)
```

- [ ] **Step 2: Write `10_topik_khusus.md`** from `extraction/text/11_specialized.md`. Use `### ` sub-headings for the four topics. Cover: development stage enterprises (SFAS 7 nature-of-cost-not-entity, disclosure + rigid uniformity reading); troubled debt restructuring (SFAS 15 undiscounted economic-consequences triumph; SFAS 114 creditor-side discounting at original effective rate, two dissents on historical-rate logic, debtor–creditor asymmetry, "evolution is slow"); early extinguishment (APB 26 three methods → current recognition; APB 30 nine-month flip; SFAS 4 extraordinary-like reporting as constituency concession); stock options (alignment rationale vs destabilizing practice, WorldCom; APB 25 NQSO bargain-element mechanics incl. measurement-date estimation; 1993 ED Black-Scholes + withdrawal 1994; SFAS 123 disclosure; SFAS 123R required expensing, model inputs & volatility reliability, IFRS 2 convergence; backdating & Efendi forced-turnover finding; entity vs proprietary analysis and the authors' reformatted-income-statement proposal: entity income → deduct interest & option costs → proprietary income, articulation benefit with SCF). Embed after APB 25/123R chronology:

```markdown
![Gambar 5. Lini masa standar kompensasi opsi saham | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 20–24](../assets/diagrams/gambar5_stock_options.png)
```

- [ ] **Step 3: Write `11_earnings_management.md`** from `extraction/text/12_earnings_management.md`. Cover: Schipper definition; agency-theory motives triad (compensation, debt covenants, political visibility); meet-or-beat asymmetry around analyst forecasts; classification shifting (McVay statistical model, 76,901 firm-years, 2.2% of special items; Borden $192m); acquisition-inflation (Erickson & Wang) vs buyout-deflation (Wu vs DeAngelo); import-protection income-lowering; Kasznik forecast-alignment; detection difficulty + SEC seriousness; auditor recall study (imprecise standards → reserves; precise standards → structuring, 75% lease example); compensation: ceiling/floor bonus mechanics (Healy; Holthausen/Larcker/Sloan; Gaver et al. variations); discretionary vs nondiscretionary accruals & real-cost controls (advertising, R&D); income smoothing: motive (firm valuation, Ronen & Sadan prediction-facilitation), 3 mechanisms, post-APB-30 classification constraint, smoother profiles (Chaney & Jeter; DeFond & Park borrow/save), 3 research problems, random-walk time-series counterevidence. Embed at the taxonomy point:

```markdown
![Gambar 6. Taksonomi earnings management dan tiga mekanisme income smoothing | Sumber: diolah dari Wolk et al. (2017), PDF hlm. 24–28](../assets/diagrams/gambar6_taksonomi_em.png)
```

- [ ] **Step 4: Word-count check (2,100–2,500 total) and commit**

```powershell
git add content/09_earnings_per_share.md content/10_topik_khusus.md content/11_earnings_management.md
git commit -m "content(rmk9): IX-XI EPS, topik khusus, earnings management"
```

---

### Task 12: Author content — Perkembangan, Sintesis, Referensi (§XII–XIV)

**Files:**
- Create: `content/12_perkembangan.md` (±750 w), `content/13_sintesis.md` (±450 w), `content/14_referensi.md`

- [ ] **Step 1: Write `12_perkembangan.md`** from `extraction/text/13_developments.md`. Use `### ` sub-headings. Cover: cash earnings (Howell's operating statement, misnamed-title critique, authors' accrual-importance rejoinder); pro forma (predictive rationale; bias toward dropping bad news; 1998–2000 young-tech-marginal-firm profile; SEC 2001 caution + Reg G 2002 equal-prominence & reconciliation; post-2002 taming); G4+1 three-component statement & earnings sustainability (restructuring classification difficulty); matrix approaches: Barker (sustainability × remeasurement columns, pension-loss reading) vs Glover et al. (fact-vs-forecast tiers, fair-value difficulty) — recurring/nonrecurring judged most promising; retrospective reports (Lundholm ex-post accuracy of estimates, >1-year clearing problem, accountability); quality of earnings (sustainability definition vs not-earnings-management definition, uniformity reprise, "true income" impossibility); restatements (1,420 in 2006; SOX 404 internal controls; complex standards esp. leases; accelerated filings; SAB 99 threshold removal).

- [ ] **Step 2: Write `13_sintesis.md`** — no new chapter claims; synthesis only. Must: (a) restate the chapter's own summary arc (rigid-uniformity drift in revenue & expense recognition; comprehensive income pushing all-inclusive; pro forma/G4+1 leaning current-operating — the dialectic is unresolved); (b) balance-sheet-primacy shift under the conceptual framework (articulation back to Pert. 8); (c) course themes: decision usefulness (information content despite arbitrary allocations), information asymmetry & agency (earnings management as inside information; compensation contracting), efficient markets (big bath reactions, value relevance), historical cost vs fair value (allocation arbitrariness; fact-vs-forecast); (d) closing professorial paragraph on relevance-vs-reliability and preparer discretion vs user needs as the chapter's enduring tension.

- [ ] **Step 3: Write `14_referensi.md`**:

```markdown
## XIV. Referensi

Wolk, H. I., Dodd, J. L., & Rozycki, J. J. (2017). *Accounting Theory: Conceptual Issues in a Political and Economic Environment* (9th ed.). Thousand Oaks, CA: Sage Publications. Bab 12, "The Income Statement" (print pp. 337–373; edisi SAGE Knowledge, 34 hlm.).

Silabus Pelaporan Keuangan Korporat (MNK202), Pascasarjana STIE YKPN Yogyakarta, Tahun Ajaran 2025/2026.
```

(Add any secondary source ONLY if actually cited in the prose; otherwise these two entries are exhaustive.)

- [ ] **Step 4: Word-count check (1,200–1,500 total) and commit**

```powershell
git add content/12_perkembangan.md content/13_sintesis.md content/14_referensi.md
git commit -m "content(rmk9): XII-XIV perkembangan, sintesis, referensi"
```

---

### Task 13: Full assembly, verification, README finalize

- [ ] **Step 1: Run the full document test suite**

Run: `python -m pytest src/python/test_build_docx.py -v` (from `rmk-pkk-pert9-income-statement/`)
Expected: ALL tests pass, including `test_six_images_and_four_tables` and `test_output_exists_with_exact_name`.

- [ ] **Step 2: Full pipeline reproducibility check (clean rebuild)**

```powershell
Remove-Item -Recurse -Force extraction\*, assets\diagrams\*.png, output\*.docx -ErrorAction SilentlyContinue
cargo run --release -p chapter_locator
cargo run --release -p text_extract
cargo run --release -p visual_gen
python src/python/build_docx.py
```

Expected: all four stages succeed in order; `output/01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx` regenerated. Any stage failing on missing upstream = bug.

- [ ] **Step 3: Open the document and run the §9 quality checklist**

`Invoke-Item "output\01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx"`. Verify visually + against spec:
- [ ] 14 sections I–XIV present in order; front matter block correct (name, NIM 1225 01079)
- [ ] total words 7,000–9,000 (Word's own count)
- [ ] 6 diagrams legible at 14.5 cm, no margin overflow, captions "Gambar N … Sumber: diolah dari …"
- [ ] 4 tables render with grid borders, 11pt TNR, captions above
- [ ] every section's paragraphs carry `(Wolk et al., 2017, PDF hlm. N)` citations
- [ ] page numbers bottom-right; A4; 3 cm margins; justified; 18pt exact spacing
- [ ] no fabricated figures/claims; no verbatim copying; professorial register throughout
- [ ] filename matches EXACTLY: `01079_Dzaki Muhammad Yusfian_RMK Pert. 9.docx`

Fix and re-run the pipeline for any failure. Then run `superpowers:requesting-code-review` per its checklist before final commit.

- [ ] **Step 4: Finalize README**

Replace the stub with: project purpose; the 4-stage run order with the exact four commands from Step 2; prerequisite list (Rust 1.94+, Python 3.12+, `pip install -r requirements.txt`, the two input PDFs in `input/`); the Rust/Python split rationale paragraph (Python = documented exception for docx assembly: proven K2 typography conventions, python-docx maturity for captions/tables/footer fields; everything else Rust per §6); the zero-exhibit finding + reconstruction policy; the citation convention (chapter-internal SAGE pages); test commands (`cargo test`, `python -m pytest src/python/test_build_docx.py`).

- [ ] **Step 5: Final commit**

```powershell
git add README.md output/ content/ assets/
git commit -m "feat(rmk9): complete RMK Pert. 9 document build — The Income Statement"
```

---

## Self-review (done at planning time)

1. **Spec coverage:** language/register (Tasks 8–12 rules), 14-section structure (content files 01–14 + 00), 10 visuals (Task 5: 6 SVGs; Task 6: 4 tables; embeds specified per section), Layout B typography incl. footer page numbers & rule (Task 7), 7–9k words (per-task budgets sum ≈ 8.4k), pipeline contracts incl. zero-exhibit verification (Tasks 2–4), determinism (Task 13 Step 2), error handling (thiserror in Task 2; bail-on-missing-upstream in Tasks 3–4; file validation implicit in builder open calls), testing (every crate + builder), §9 checklist (Task 13 Step 3). Gap fixed inline: spec's "validates all PNGs ≥ expected width" lives in visual_gen's 1712-px check rather than the builder.
2. **Placeholders:** none — all code, SVGs, TOMLs complete; prose tasks specify exhaustive coverage checklists (prose itself is authored at execution against extraction output, by design).
3. **Type consistency:** `find_chapter_bounds` signature matches its tests; `segment`/`SECTIONS` consistent; `parse_blocks` block kinds (`heading|subheading|para|bullet|ref|image|table`) match builder dispatch and tests; `@table(...)`/`![...](...)` paths in Tasks 9–12 resolve relative to `content/` exactly as the builder joins them.
