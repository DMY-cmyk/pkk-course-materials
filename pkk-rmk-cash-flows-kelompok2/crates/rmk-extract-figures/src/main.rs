//! Phase 3.5: rasterize, crop, trim, and resize chapter exhibits per
//! `analysis/exhibit-map.md`, writing PNGs + `content/figures/manifest.yaml`.

use anyhow::Result;
use clap::Parser;

/// Extract and crop chapter exhibits from the source PDF.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    /// Source PDF path.
    #[arg(
        long,
        default_value = "sources/textbook-chapter/Sage_Chapter_13_Kelompok_2.pdf"
    )]
    pdf: String,
    /// Output directory for cropped figures.
    #[arg(long, default_value = "content/figures")]
    out: String,
}

fn main() -> Result<()> {
    let args = Args::parse();
    anyhow::bail!(
        "not yet implemented (Phase 3.5): will extract exhibits from {} into {}",
        args.pdf,
        args.out
    )
}
