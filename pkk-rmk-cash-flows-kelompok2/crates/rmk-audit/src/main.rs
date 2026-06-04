//! Phase 4: concept-coverage analysis — every C-01..C-62 concept must have a
//! home in `content/sections/`, and every rubric requirement must be met.

use anyhow::Result;
use clap::Parser;

/// Audit concept coverage and exhibit anchoring across content sections.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    /// Sections directory.
    #[arg(long, default_value = "content/sections")]
    sections: String,
}

fn main() -> Result<()> {
    let args = Args::parse();
    anyhow::bail!(
        "not yet implemented (Phase 4): will audit coverage in {}",
        args.sections
    )
}
