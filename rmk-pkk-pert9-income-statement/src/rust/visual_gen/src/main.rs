//! Rasterizes every authored SVG in assets/diagrams/svg/ to PNG in
//! assets/diagrams/. SVGs are authored at 1712 px width (= 14.5 cm @ 300 DPI).

use anyhow::{bail, Context, Result};
use clap::Parser;

pub fn rasterize(
    svg_data: &[u8],
    fontdb: std::sync::Arc<resvg::usvg::fontdb::Database>,
) -> Result<resvg::tiny_skia::Pixmap> {
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
        pixmap
            .save_png(&out)
            .map_err(|e| anyhow::anyhow!("{}", e))?;
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
