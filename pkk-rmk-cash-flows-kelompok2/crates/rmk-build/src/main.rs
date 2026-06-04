//! Phase 4/5: assemble `content/sections/*.md` + `content/figures/manifest.yaml`
//! into the final .docx via the python-docx bridge (`tools/build_docx.py`).

use anyhow::Result;
use clap::Parser;

/// Build the RMK .docx from markdown sections and the figure manifest.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    /// Output .docx path.
    #[arg(long, default_value = "output/RMK Chap. 13_Kelompok 2_PKK.docx")]
    output: String,
    /// Run the python-docx bridge smoke test only (Phase 2 baseline).
    #[arg(long)]
    smoke: bool,
}

fn main() -> Result<()> {
    let args = Args::parse();
    if args.smoke {
        let status = std::process::Command::new("python")
            .args(["tools/build_docx.py", "--smoke"])
            .status()?;
        anyhow::ensure!(status.success(), "python-docx bridge smoke test failed");
        println!("python-docx bridge smoke test OK");
        return Ok(());
    }
    anyhow::bail!(
        "not yet implemented (Phase 4): will assemble sections into {}",
        args.output
    )
}
