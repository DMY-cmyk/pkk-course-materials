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
    blocks.extend(compile_body(&cover_body, &manifest, figures_dir, &root)?);
    let mut section_paths: Vec<_> = fs::read_dir(root.join("content/sections"))?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .filter(|p| p.extension().is_some_and(|e| e == "md"))
        .collect();
    section_paths.sort();
    for p in &section_paths {
        let (meta, body) = parse_doc::<Section>(p)?;
        blocks.push(Block::Heading {
            level: 1,
            text: meta.title,
        });
        blocks.extend(compile_body(&body, &manifest, figures_dir, &root)?);
    }
    fs::create_dir_all(root.join("output"))?;
    let spec_path = root.join("output/build-spec.json");
    fs::write(&spec_path, serde_json::to_string_pretty(&blocks)?)?;
    println!(
        "compiled {} blocks from {} sections",
        blocks.len(),
        section_paths.len()
    );
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
