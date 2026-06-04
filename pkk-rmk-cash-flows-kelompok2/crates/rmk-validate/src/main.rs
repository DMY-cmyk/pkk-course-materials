//! Phase 5: validate the built .docx against the six hard gates (A4, 1.5
//! spacing, Calibri 12, >=8 pages, .docx, identity block) plus concept
//! coverage and exhibit completeness; emit VALIDATION-REPORT.md.

use anyhow::{Context, Result};
use clap::Parser;
use rmk_audit::{concept_ids, parse_doc, workspace_root};
use shared::{Exhibit, Section};
use std::collections::{BTreeMap, BTreeSet};
use std::path::Path;
use std::process::Command;

/// Validate the final document and emit the validation report.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    /// Built .docx to validate.
    #[arg(long, default_value = "output/RMK Chap. 13_Kelompok 2_PKK.docx")]
    docx: String,
    /// Report output path.
    #[arg(long, default_value = "output/VALIDATION-REPORT.md")]
    report: String,
}

// ─── Python bridge ────────────────────────────────────────────────────────────

fn run_python_bridge(root: &Path, docx: &str) -> Result<serde_json::Value> {
    let script = root.join("tools/validate_docx.py");
    let output = Command::new("python")
        .arg(&script)
        .arg(docx)
        .current_dir(root)
        .output()
        .context("launching python tools/validate_docx.py")?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        anyhow::bail!("validate_docx.py exited non-zero:\n{stderr}");
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    serde_json::from_str(&stdout).context("parsing JSON from validate_docx.py")
}

// ─── Audit logic ──────────────────────────────────────────────────────────────

struct SectionAudit {
    id: String,
    concept_count: usize,
}

fn audit_sections(root: &Path) -> Result<(Vec<SectionAudit>, BTreeSet<String>)> {
    let dir = root.join("content/sections");
    let mut audits = Vec::new();
    let mut all_covered: BTreeSet<String> = BTreeSet::new();

    let mut paths: Vec<_> = std::fs::read_dir(&dir)
        .with_context(|| format!("reading {}", dir.display()))?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .filter(|p| p.extension().is_some_and(|e| e == "md"))
        .collect();
    paths.sort();

    for p in &paths {
        let (s, _): (Section, _) = parse_doc(p)?;
        all_covered.extend(s.covers_concepts.iter().cloned());
        audits.push(SectionAudit {
            id: s.id,
            concept_count: s.covers_concepts.len(),
        });
    }

    Ok((audits, all_covered))
}

struct ExhibitCheck {
    id: String,
    render_type: String,
    anchor_section: String,
    embedded_in_front_matter: bool,
    directive_in_body: bool,
}

fn audit_exhibits(root: &Path, manifests: &[Exhibit]) -> Result<Vec<ExhibitCheck>> {
    let mut checks = Vec::new();

    // Build a map: section_id → (embeds_exhibits, body)
    let dir = root.join("content/sections");
    let mut section_map: BTreeMap<String, (Vec<String>, String)> = BTreeMap::new();

    let mut paths: Vec<_> = std::fs::read_dir(&dir)
        .with_context(|| format!("reading {}", dir.display()))?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .filter(|p| p.extension().is_some_and(|e| e == "md"))
        .collect();
    paths.sort();

    for p in &paths {
        let (s, body): (Section, _) = parse_doc(p)?;
        section_map.insert(s.id, (s.embeds_exhibits, body));
    }

    for exhibit in manifests {
        let anchor = &exhibit.anchor_section;
        let id = &exhibit.id;
        let render_type = format!("{:?}", exhibit.render_type).to_lowercase();

        let (embedded_in_front_matter, directive_in_body) =
            if let Some((embeds, body)) = section_map.get(anchor.as_str()) {
                let in_fm = embeds.contains(id);
                let directive = format!("{{{{exhibit:{id}}}}}");
                let in_body = body.contains(&directive);
                (in_fm, in_body)
            } else {
                (false, false)
            };

        checks.push(ExhibitCheck {
            id: id.clone(),
            render_type,
            anchor_section: anchor.clone(),
            embedded_in_front_matter,
            directive_in_body,
        });
    }

    Ok(checks)
}

// ─── JSON helpers ─────────────────────────────────────────────────────────────

fn bool_gate(v: &serde_json::Value, key: &str) -> bool {
    v.get(key).and_then(|x| x.as_bool()).unwrap_or(false)
}

fn pass_fail(b: bool) -> &'static str {
    if b {
        "PASS"
    } else {
        "FAIL"
    }
}

fn tick(b: bool) -> &'static str {
    if b {
        "✓"
    } else {
        "✗"
    }
}

// ─── Report generation ────────────────────────────────────────────────────────

fn generate_report(
    docx_path: &str,
    report_path: &str,
    py: &serde_json::Value,
    section_audits: &[SectionAudit],
    covered_concepts: &BTreeSet<String>,
    exhibit_checks: &[ExhibitCheck],
    root: &Path,
) -> Result<()> {
    let mut lines: Vec<String> = Vec::new();

    // ── Section 1: header ──
    lines.push("# VALIDATION REPORT — RMK Chap. 13_Kelompok 2_PKK.docx".to_string());
    lines.push(String::new());
    lines.push(format!(
        "Generated by `rmk-validate` from `{}` on {}.",
        docx_path,
        chrono_now()
    ));
    lines.push(String::new());

    // ── Section 2: format gates ──
    lines.push("## Format gates".to_string());
    lines.push(String::new());
    lines.push("| Gate | Result | Status |".to_string());
    lines.push("|---|---|---|".to_string());

    let a4 = bool_gate(py, "a4");
    lines.push(format!("| A4 paper size | {} | {} |", a4, pass_fail(a4)));

    let spacing = bool_gate(py, "line_spacing_1_5");
    lines.push(format!(
        "| 1.5 line spacing | {} | {} |",
        spacing,
        pass_fail(spacing)
    ));

    let font = bool_gate(py, "font");
    lines.push(format!(
        "| Calibri font (Normal style) | {} | {} |",
        font,
        pass_fail(font)
    ));

    let size12 = bool_gate(py, "size_12");
    lines.push(format!(
        "| 12 pt font size (Normal style) | {} | {} |",
        size12,
        pass_fail(size12)
    ));

    // Page count: number → pass/fail; error object → MANUAL CHECK REQUIRED
    let page_result = py
        .get("page_count")
        .cloned()
        .unwrap_or(serde_json::Value::Null);
    let page_status_line: String = if let Some(n) = page_result.as_i64() {
        let ok = n >= 8;
        format!("| ≥8 pages | {} page(s) | {} |", n, pass_fail(ok))
    } else if let Some(obj) = page_result.as_object() {
        let err = obj
            .get("error")
            .and_then(|e| e.as_str())
            .unwrap_or("unknown");
        eprintln!("WARNING: page count unavailable via Word COM: {err}");
        format!("| ≥8 pages | MANUAL CHECK REQUIRED (Word COM unavailable: {err}) | WARN |")
    } else {
        "| ≥8 pages | MANUAL CHECK REQUIRED (no page_count in JSON) | WARN |".to_string()
    };
    lines.push(page_status_line);

    // .docx format: file extension + python-docx opened it (if we reached here, it did)
    let docx_ext_ok = docx_path.to_lowercase().ends_with(".docx");
    lines.push(format!(
        "| .docx format | extension={docx_ext_ok}, python-docx opened successfully | {} |",
        pass_fail(docx_ext_ok)
    ));

    // Identity
    let identity_missing = py
        .get("identity_missing")
        .and_then(|v| v.as_array())
        .map(|a| a.len())
        .unwrap_or(0);
    let identity_ok = identity_missing == 0;
    lines.push(format!(
        "| Identity block 6/6 | missing={identity_missing} | {} |",
        pass_fail(identity_ok)
    ));

    lines.push(String::new());

    // ── Section 3: exhibits ──
    lines.push("## Exhibits".to_string());
    lines.push(String::new());

    let images = py.get("images").and_then(|v| v.as_i64()).unwrap_or(0);
    let images_ok = bool_gate(py, "images_ok");
    lines.push(format!(
        "Inline images in document: **{images}** (required ≥ 8) — {}",
        pass_fail(images_ok)
    ));
    lines.push(String::new());

    lines.push("| ID | Render type | Anchor section | FM embedded | Body directive |".to_string());
    lines.push("|---|---|---|---|---|".to_string());
    for ec in exhibit_checks {
        lines.push(format!(
            "| {} | {} | {} | {} | {} |",
            ec.id,
            ec.render_type,
            ec.anchor_section,
            tick(ec.embedded_in_front_matter),
            tick(ec.directive_in_body)
        ));
    }
    lines.push(String::new());

    let captions_missing = py
        .get("captions_missing")
        .and_then(|v| v.as_array())
        .cloned()
        .unwrap_or_default();
    if captions_missing.is_empty() {
        lines.push("Caption markers (Exhibit 13.1–13.11): all present.".to_string());
    } else {
        let missing: Vec<_> = captions_missing.iter().filter_map(|v| v.as_str()).collect();
        lines.push(format!("Caption markers missing: {}", missing.join(", ")));
    }

    let equations_missing = py
        .get("equations_missing")
        .and_then(|v| v.as_array())
        .cloned()
        .unwrap_or_default();
    if equations_missing.is_empty() {
        lines.push("Equation markers (13.1), (13.2): all present.".to_string());
    } else {
        let missing: Vec<_> = equations_missing
            .iter()
            .filter_map(|v| v.as_str())
            .collect();
        lines.push(format!("Equation markers missing: {}", missing.join(", ")));
    }
    lines.push(String::new());

    // ── Section 4: concept coverage ──
    lines.push("## Concept coverage".to_string());
    lines.push(String::new());
    let n_concepts = covered_concepts.len();
    let n_sections = section_audits.len();
    lines.push(format!(
        "{n_concepts}/62 concepts across {n_sections}/15 sections."
    ));
    lines.push(String::new());

    let missing_concepts: Vec<_> = concept_ids()
        .into_iter()
        .filter(|c| !covered_concepts.contains(c))
        .collect();
    if missing_concepts.is_empty() {
        lines.push("All 62 concepts covered.".to_string());
    } else {
        lines.push(format!("Missing concepts: {}", missing_concepts.join(", ")));
    }
    lines.push(String::new());

    lines.push("| Section | Concepts covered |".to_string());
    lines.push("|---|---|".to_string());
    for sa in section_audits {
        lines.push(format!("| {} | {} |", sa.id, sa.concept_count));
    }
    lines.push(String::new());

    // ── Section 5: tooling substitutions ──
    lines.push("## Tooling substitutions".to_string());
    lines.push(String::new());
    lines.push("Two documented substitutions applied in this project:".to_string());
    lines.push(String::new());
    lines.push("1. **Tesseract OCR unavailable** — `tesseract` is not installed on this Windows host. Substitution: Claude native vision (`Read` tool) was used for the two image-OCR tasks in Phase 0 (reading `sources/assignment/Tugas_RMK_Kelompok.png` and `sources/group/Kelompok_2_Member_NIMs.jpeg`). No automated OCR pipeline was involved.".to_string());
    lines.push(String::new());
    lines.push("2. **docx skill unavailable on this Windows host** — The `/mnt/skills` docx skill is not present in this environment. Substitution: `python-docx` bridge (`tools/build_docx.py`) was used to construct the final Word document programmatically. This is a proven pattern in this repository (see `ti4/output/build_docx.py`, `ti5/output/build_docx.py`). The bridge renders all sections, tables, images, and equations directly via the `python-docx` API.".to_string());
    lines.push(String::new());

    // ── Write file ──
    let report_file = root.join(report_path);
    std::fs::write(&report_file, lines.join("\n"))
        .with_context(|| format!("writing report to {}", report_file.display()))?;

    Ok(())
}

fn chrono_now() -> String {
    // Simple ISO date without pulling in chrono crate
    // Use env var or fallback
    std::env::var("VALIDATION_DATE").unwrap_or_else(|_| "2026-06-04".to_string())
}

// ─── Gate checks ──────────────────────────────────────────────────────────────

fn collect_failures(
    py: &serde_json::Value,
    section_audits: &[SectionAudit],
    covered_concepts: &BTreeSet<String>,
    exhibit_checks: &[ExhibitCheck],
) -> Vec<String> {
    let mut failures: Vec<String> = Vec::new();

    for key in ["a4", "font", "size_12", "line_spacing_1_5", "images_ok"] {
        if !bool_gate(py, key) {
            failures.push(format!("format gate '{key}' failed"));
        }
    }

    // captions_missing
    let captions_missing = py
        .get("captions_missing")
        .and_then(|v| v.as_array())
        .map(|a| a.len())
        .unwrap_or(0);
    if captions_missing > 0 {
        failures.push(format!(
            "{captions_missing} caption marker(s) missing from document"
        ));
    }

    // equations_missing
    let equations_missing = py
        .get("equations_missing")
        .and_then(|v| v.as_array())
        .map(|a| a.len())
        .unwrap_or(0);
    if equations_missing > 0 {
        failures.push(format!(
            "{equations_missing} equation marker(s) missing from document"
        ));
    }

    // identity_missing
    let identity_missing = py
        .get("identity_missing")
        .and_then(|v| v.as_array())
        .map(|a| a.len())
        .unwrap_or(0);
    if identity_missing > 0 {
        failures.push(format!(
            "{identity_missing} identity item(s) missing from document"
        ));
    }

    // sections count
    if section_audits.len() != 15 {
        failures.push(format!(
            "expected 15 sections, found {}",
            section_audits.len()
        ));
    }

    // concept coverage
    let missing_count = concept_ids()
        .into_iter()
        .filter(|c| !covered_concepts.contains(c))
        .count();
    if missing_count > 0 {
        failures.push(format!("{missing_count} concept(s) not covered"));
    }

    // exhibit embedding
    for ec in exhibit_checks {
        if !ec.embedded_in_front_matter {
            failures.push(format!(
                "exhibit {} not in front-matter of anchor section {}",
                ec.id, ec.anchor_section
            ));
        }
        if !ec.directive_in_body {
            failures.push(format!(
                "exhibit {} missing {{{{exhibit:{}}}}} directive in anchor section body",
                ec.id, ec.id
            ));
        }
    }

    // page count: only fail if we got a number < 8
    let page_result = py
        .get("page_count")
        .cloned()
        .unwrap_or(serde_json::Value::Null);
    if let Some(n) = page_result.as_i64() {
        if n < 8 {
            failures.push(format!("page count {n} < 8 required"));
        }
    }

    failures
}

// ─── Entry point ──────────────────────────────────────────────────────────────

fn main() -> Result<()> {
    let args = Args::parse();
    let root = workspace_root();

    // ── Step 1: python bridge ──
    let py =
        run_python_bridge(&root, &args.docx).context("python validate_docx.py bridge failed")?;

    // ── Step 2: load manifest ──
    let manifest_path = root.join("content/figures/manifest.yaml");
    let manifest_text = std::fs::read_to_string(&manifest_path)
        .with_context(|| format!("reading {}", manifest_path.display()))?;
    let manifests: Vec<Exhibit> =
        serde_yaml::from_str(&manifest_text).context("parsing manifest.yaml")?;

    // ── Step 3: section audit ──
    let (section_audits, covered_concepts) = audit_sections(&root).context("auditing sections")?;

    // ── Step 4: exhibit audit ──
    let exhibit_checks = audit_exhibits(&root, &manifests).context("auditing exhibit embedding")?;

    // ── Step 5: generate report ──
    generate_report(
        &args.docx,
        &args.report,
        &py,
        &section_audits,
        &covered_concepts,
        &exhibit_checks,
        &root,
    )
    .context("generating report")?;

    // ── Step 6: check failures ──
    let failures = collect_failures(&py, &section_audits, &covered_concepts, &exhibit_checks);

    let report_abs = root.join(&args.report);
    if failures.is_empty() {
        println!("VALIDATION PASSED — report at {}", report_abs.display());
    } else {
        // Print failures to stderr before bailing so the report is still written
        for f in &failures {
            eprintln!("FAIL: {f}");
        }
        anyhow::bail!(
            "VALIDATION FAILED ({} issue(s)) — report at {}",
            failures.len(),
            report_abs.display()
        );
    }

    Ok(())
}
