//! Phase 5: validate the built .docx against the six hard gates (A4, 1.5
//! spacing, Calibri 12, >=8 pages, .docx, identity block) plus concept
//! coverage and exhibit completeness; emit VALIDATION-REPORT.md.

use anyhow::Result;
use clap::Parser;

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

fn main() -> Result<()> {
    let args = Args::parse();
    anyhow::bail!(
        "not yet implemented (Phase 5): will validate {} and write {}",
        args.docx,
        args.report
    )
}
