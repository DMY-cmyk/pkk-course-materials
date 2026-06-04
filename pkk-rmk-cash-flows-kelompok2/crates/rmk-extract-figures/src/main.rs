//! Rasterize, crop, trim, and stack chapter exhibits per the figure manifest.

use anyhow::{Context, Result};
use clap::Parser;
use rmk_extract_figures::{crop_pct, stack, trim_white};
use shared::{Exhibit, RenderType};
use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;

/// Extract and crop chapter exhibits from the source PDF.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    #[arg(
        long,
        default_value = "sources/textbook-chapter/Sage_Chapter_13_Kelompok_2.pdf"
    )]
    pdf: String,
    #[arg(long, default_value = "content/figures")]
    out: String,
    #[arg(long, default_value = "content/figures/manifest.yaml")]
    manifest: String,
    #[arg(long, default_value_t = 240)]
    dpi: u32,
}

fn render_page(pdf: &str, page: u32, dpi: u32, tmp: &Path) -> Result<PathBuf> {
    let prefix = tmp.join(format!("p{page}"));
    let status = Command::new("pdftoppm")
        .args(["-png", "-r", &dpi.to_string()])
        .args(["-f", &page.to_string(), "-l", &page.to_string()])
        .arg(pdf)
        .arg(&prefix)
        .status()
        .context("running pdftoppm")?;
    anyhow::ensure!(status.success(), "pdftoppm failed for page {page}");
    let stem = format!("p{page}-");
    let png = fs::read_dir(tmp)?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .find(|p| {
            p.file_name()
                .and_then(|n| n.to_str())
                .is_some_and(|n| n.starts_with(&stem) && n.ends_with(".png"))
        })
        .with_context(|| format!("no pdftoppm output for page {page}"))?;
    Ok(png)
}

fn main() -> Result<()> {
    let args = Args::parse();
    let manifest: Vec<Exhibit> =
        serde_yaml::from_str(&fs::read_to_string(&args.manifest).context("reading manifest")?)?;
    let out_dir = Path::new(&args.out);
    fs::create_dir_all(out_dir)?;
    let tmp = out_dir.join("_pages");
    fs::create_dir_all(&tmp)?;
    let mut extracted = 0u32;
    for ex in manifest
        .iter()
        .filter(|e| e.render_type == RenderType::Crop)
    {
        anyhow::ensure!(!ex.segments.is_empty(), "{}: crop without segments", ex.id);
        let mut parts = Vec::new();
        for seg in &ex.segments {
            let page_png = render_page(&args.pdf, seg.page, args.dpi, &tmp)?;
            let img = image::open(&page_png)
                .with_context(|| format!("opening {}", page_png.display()))?
                .to_rgb8();
            parts.push(trim_white(&crop_pct(&img, seg.box_pct)));
        }
        let combined = stack(&parts);
        let dest = out_dir.join(format!("{}.png", ex.id));
        combined.save(&dest)?;
        println!(
            "{} -> {} ({}x{})",
            ex.id,
            dest.display(),
            combined.width(),
            combined.height()
        );
        extracted += 1;
    }
    fs::remove_dir_all(&tmp).ok();
    println!("extracted {extracted} crop exhibits");
    Ok(())
}
