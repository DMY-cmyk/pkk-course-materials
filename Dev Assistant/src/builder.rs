use std::fs;
use std::path::Path;
use tera::Tera;

use crate::config::load_config;
use crate::markdown::render_markdown;
use crate::renderer::{build_context, render_template, WeekSummary, DELIVERABLES};

pub fn build_week(
    week: u8,
    tera: &Tera,
    config_path: &str,
    content_dir: &str,
    assets_dir: &str,
    output_root: &str,
) {
    let config = load_config(config_path).expect("Failed to load mapping.toml");
    let all_weeks = make_week_summaries(&config.weeks);

    let week_config = config.weeks.get(&week)
        .unwrap_or_else(|| panic!("Week {} not found in mapping.toml", week));

    for meta in DELIVERABLES {
        let source_path = format!("{}/week-{:02}/{}", content_dir, week, meta.source_file);
        let md = fs::read_to_string(&source_path).unwrap_or_else(|_| {
            format!(
                "# {} — Minggu {:02}\n\n*Konten sedang disiapkan.*\n",
                meta.label, week
            )
        });

        let content_html = render_markdown(&md);
        let ctx = build_context(week, week_config, &content_html, meta, &all_weeks);
        let rendered = render_template(tera, meta.template, &ctx);

        let out_dir = format!("{}/{}/Week {:02}", output_root, meta.output_folder, week);
        fs::create_dir_all(&out_dir).expect("Failed to create output directory");

        let out_path = format!("{}/{}", out_dir, meta.output_file);
        fs::write(&out_path, &rendered).expect("Failed to write HTML output");

        copy_assets(&out_dir, assets_dir);

        println!("  ✓  W{:02}  {}  →  {}", week, meta.type_key, out_path);
    }
}

pub fn build_weeks_range(
    range: &str,
    tera: &Tera,
    config_path: &str,
    content_dir: &str,
    assets_dir: &str,
    output_root: &str,
) {
    let parts: Vec<u8> = range
        .split('-')
        .map(|s| s.trim().parse::<u8>().expect("Invalid week number in range"))
        .collect();
    assert_eq!(parts.len(), 2, "Range must be in format 'N-M', e.g. '1-7'");
    assert!(parts[0] <= parts[1], "Range start must not exceed end: '{}'", range);
    for week in parts[0]..=parts[1] {
        build_week(week, tera, config_path, content_dir, assets_dir, output_root);
    }
}

pub fn build_all(
    tera: &Tera,
    config_path: &str,
    content_dir: &str,
    assets_dir: &str,
    output_root: &str,
) {
    for week in 1u8..=14 {
        println!("\nBuilding Week {:02}...", week);
        build_week(week, tera, config_path, content_dir, assets_dir, output_root);
    }
}

pub(crate) fn make_week_summaries(
    weeks: &std::collections::HashMap<u8, crate::config::WeekConfig>,
) -> Vec<WeekSummary> {
    let mut summaries: Vec<WeekSummary> = (1u8..=14)
        .filter_map(|w| {
            weeks.get(&w).map(|c| WeekSummary {
                week_num: w,
                week_pad: format!("{:02}", w),
                title: c.title.clone(),
                phase_key: if c.phase == "pre-uts" { "pre".into() } else { "post".into() },
                phase_label: if c.phase == "pre-uts" { "Pra-UTS".into() } else { "Pasca-UTS".into() },
                company_ticker: c.company_ticker.clone(),
                company_name: c.company_name.clone(),
            })
        })
        .collect();
    summaries.sort_by_key(|s| s.week_num);
    summaries
}

pub(crate) fn copy_assets(out_dir: &str, assets_dir: &str) {
    let css_src = Path::new(assets_dir).join("css");
    let css_dst = Path::new(out_dir).join("css");
    fs::create_dir_all(&css_dst).ok();
    if !css_src.exists() { return; }
    for entry in fs::read_dir(&css_src).expect("Cannot read assets/css") {
        let entry = entry.unwrap();
        let dst = css_dst.join(entry.file_name());
        fs::copy(entry.path(), dst).ok();
    }

    let font_src = Path::new(assets_dir).join("fonts");
    let font_dst = Path::new(out_dir).join("fonts");
    fs::create_dir_all(&font_dst).ok();
    if font_src.exists() {
        for entry in fs::read_dir(&font_src).expect("Cannot read assets/fonts") {
            let entry = entry.unwrap();
            let dst = font_dst.join(entry.file_name());
            fs::copy(entry.path(), dst).ok();
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_weeks_range_parses_correctly() {
        let range = "1-7";
        let parts: Vec<u8> = range.split('-').map(|s| s.trim().parse().unwrap()).collect();
        assert_eq!(parts, vec![1u8, 7u8]);
    }
}
