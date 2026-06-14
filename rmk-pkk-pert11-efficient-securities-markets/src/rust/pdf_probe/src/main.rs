//! pdf_probe — page-count confirmation + image XObject inventory for a
//! standalone single-chapter SAGE PDF.
//!
//! Writes:
//!   extraction/chapter-range.json   — {start_page, end_page, print_pages}
//!   extraction/verification-report.md — per-page image table + summary

use anyhow::{Context, Result};
use clap::Parser;
use lopdf::Object;
use serde::Serialize;
use std::collections::BTreeMap;
use std::path::Path;

// ── CLI args ──────────────────────────────────────────────────────────────────

#[derive(Parser, Debug)]
#[command(about = "Probe a standalone chapter PDF: page count + image XObject inventory")]
struct Args {
    /// Path to the chapter PDF
    #[arg(long, default_value = "input/chapter/Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf")]
    pdf: String,

    /// Output JSON path
    #[arg(long, default_value = "extraction/chapter-range.json")]
    out: String,

    /// Output Markdown report path
    #[arg(long, default_value = "extraction/verification-report.md")]
    report: String,

    /// Authoritative print-page range for this chapter (e.g. "120-152")
    #[arg(long, default_value = "120-152")]
    print_pages: String,
}

// ── Pure helper ───────────────────────────────────────────────────────────────

/// Returns a print-page range string like "375-409" (or "375" for a single page).
pub fn print_page_range(start_print: u32, n_pages: u32) -> String {
    if n_pages <= 1 {
        start_print.to_string()
    } else {
        format!("{}-{}", start_print, start_print + n_pages - 1)
    }
}

// ── Image counting (best-effort per-page) ─────────────────────────────────────

/// Count Image-subtype XObjects in a page's Resources dictionary.
/// Returns 0 on any error (best-effort, advisory only).
fn count_page_images(doc: &lopdf::Document, page_id: lopdf::ObjectId) -> u32 {
    // Walk: Page → Resources → XObject → entries with /Subtype /Image
    let page_obj = match doc.get_object(page_id) {
        Ok(o) => o,
        Err(_) => return 0,
    };
    let page_dict = match page_obj.as_dict() {
        Ok(d) => d,
        Err(_) => return 0,
    };

    // Resources may be a direct dict or an indirect reference
    let resources_obj = match page_dict.get(b"Resources") {
        Ok(r) => r,
        Err(_) => return 0,
    };
    let resources_obj = match resources_obj {
        Object::Reference(id) => match doc.get_object(*id) {
            Ok(o) => o,
            Err(_) => return 0,
        },
        other => other,
    };
    let resources = match resources_obj.as_dict() {
        Ok(d) => d,
        Err(_) => return 0,
    };

    let xobject_obj = match resources.get(b"XObject") {
        Ok(x) => x,
        Err(_) => return 0,
    };
    let xobject_obj = match xobject_obj {
        Object::Reference(id) => match doc.get_object(*id) {
            Ok(o) => o,
            Err(_) => return 0,
        },
        other => other,
    };
    let xobject_dict = match xobject_obj.as_dict() {
        Ok(d) => d,
        Err(_) => return 0,
    };

    let mut count = 0u32;
    for (_key, val) in xobject_dict.iter() {
        // Each value is typically an indirect reference to a stream
        let target = match val {
            Object::Reference(id) => match doc.get_object(*id) {
                Ok(o) => o,
                Err(_) => continue,
            },
            other => other,
        };
        // Check if it's a stream with /Subtype /Image
        if let Ok(stream) = target.as_stream() {
            if let Ok(subtype) = stream.dict.get(b"Subtype") {
                match subtype {
                    Object::Name(n) if n == b"Image" => count += 1,
                    _ => {}
                }
            }
        }
    }
    count
}

// ── JSON output ───────────────────────────────────────────────────────────────

#[derive(Serialize)]
struct RangeOut {
    start_page: u32,
    end_page: u32,
    print_pages: String,
}

// ── main ──────────────────────────────────────────────────────────────────────

fn main() -> Result<()> {
    let args = Args::parse();

    // Load PDF
    let doc = lopdf::Document::load(&args.pdf)
        .with_context(|| format!("loading PDF: {}", args.pdf))?;

    // Collect page IDs in logical order (BTreeMap keys are 1-based page numbers)
    let pages_map: BTreeMap<u32, lopdf::ObjectId> = doc.get_pages();
    let n_pages = pages_map.len() as u32;
    anyhow::ensure!(n_pages > 0, "PDF has no pages");

    // Per-page image count
    let mut per_page: Vec<(u32, u32)> = Vec::with_capacity(n_pages as usize);
    for (page_num, page_id) in &pages_map {
        let img_count = count_page_images(&doc, *page_id);
        per_page.push((*page_num, img_count));
    }
    let total_images: u32 = per_page.iter().map(|(_, c)| c).sum();

    // ── Write chapter-range.json ──────────────────────────────────────────────
    let range_out = RangeOut {
        start_page: 1,
        end_page: n_pages,
        print_pages: args.print_pages.clone(),
    };
    let out_path = Path::new(&args.out);
    std::fs::create_dir_all(out_path.parent().unwrap_or(Path::new(".")))?;
    std::fs::write(out_path, serde_json::to_string_pretty(&range_out)?)?;

    // ── Write verification-report.md ──────────────────────────────────────────
    let report_path = Path::new(&args.report);
    std::fs::create_dir_all(report_path.parent().unwrap_or(Path::new(".")))?;

    let mut md = String::new();
    md.push_str("# PDF Probe — Verification Report\n\n");
    md.push_str(&format!("- **PDF:** `{}`\n", args.pdf));
    md.push_str(&format!("- **Page count:** {}\n", n_pages));
    md.push_str(&format!("- **Print-page range:** {}\n", args.print_pages));
    md.push_str("\n## Per-page Image XObject Count\n\n");
    md.push_str("| PDF page | image count |\n");
    md.push_str("|----------|-------------|\n");
    for (page_num, img_count) in &per_page {
        md.push_str(&format!("| {} | {} |\n", page_num, img_count));
    }
    md.push_str(&format!(
        "\n**Total image XObjects: {}.** \
         Pages with images are exhibit-bearing; cross-check against \
         crop_exhibits.py rectangles.\n",
        total_images
    ));

    std::fs::write(report_path, &md)?;

    // ── Summary ───────────────────────────────────────────────────────────────
    println!(
        "pdf_probe: {} pages, print range {}, {} total image XObjects → {} | {}",
        n_pages, args.print_pages, total_images, args.out, args.report
    );

    Ok(())
}

// ── Unit tests ────────────────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn print_range_inclusive() {
        assert_eq!(print_page_range(375, 35), "375-409");
    }

    #[test]
    fn single_page_range() {
        assert_eq!(print_page_range(375, 1), "375");
    }
}
