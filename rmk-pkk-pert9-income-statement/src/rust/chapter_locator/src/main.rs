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
    // NOTE: In this SAGE Knowledge edition each chapter is a self-contained
    // sub-document whose body text uses embedded fonts WITHOUT a ToUnicode
    // CMap, so `extract_text` returns nothing for the chapter title/body.
    // The ONLY reliably extractable text on each page is the per-chapter
    // running footer `Page <n> of <m>`. The chapter's own title page (footer
    // "Page 1 of m") also extracts empty. So we anchor on the unique
    // `Page 2 of <m>` footer of a chapter (and of the NEXT chapter) and shift
    // back by `title_page_offset` (=1) to land on each chapter's title page.
    // Ch.12 "The Income Statement" = 34-page chapter -> "Page 2 of 34".
    // Following chapter = 31-page chapter -> "Page 2 of 31".
    #[arg(long, default_value = "Page 2 of 34")]
    start_marker: String,
    #[arg(long, default_value = "Page 2 of 31")]
    next_marker: String,
    /// Pages to subtract so a chapter's "Page 2" anchor maps to its (empty)
    /// title page. SAGE chapters have exactly one preceding title page.
    #[arg(long, default_value = "1")]
    title_page_offset: usize,
    /// DEBUG: dump extracted text of this 1-based page and exit
    #[arg(long)]
    inspect: Option<usize>,
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
    if let Some(p) = args.inspect {
        eprintln!("total pages (lopdf get_pages): {}", texts.len());
        eprintln!("=== page {p} extracted text ({} chars) ===", texts.get(p - 1).map(|t| t.len()).unwrap_or(0));
        eprintln!("{}", texts.get(p - 1).cloned().unwrap_or_default());
        eprintln!("=== end page {p} ===");
        return Ok(());
    }
    // Locate the two "Page 2 of <m>" anchors, then shift back to the title
    // page of each chapter (the title page footer extracts empty).
    let (raw_start, raw_end) =
        find_chapter_bounds(&texts, &args.start_marker, &args.next_marker)?;
    let start = raw_start
        .checked_sub(args.title_page_offset)
        .filter(|s| *s >= 1)
        .with_context(|| format!("start anchor page {raw_start} minus offset {} underflows", args.title_page_offset))?;
    let end = raw_end
        .checked_sub(args.title_page_offset)
        .filter(|e| *e >= start)
        .with_context(|| format!("end anchor page {raw_end} minus offset {} underflows below start {start}", args.title_page_offset))?;
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
