use std::fs;
use std::path::Path;
use tera::{Context, Tera};

use crate::builder::make_week_summaries;
use crate::config::load_config;
use crate::renderer::DELIVERABLES;

pub fn build_visual_companion(
    tera: &Tera,
    config_path: &str,
    assets_dir: &str,
    output_root: &str,
) {
    let config = load_config(config_path).expect("Failed to load config");
    let all_weeks = make_week_summaries(&config.weeks);

    let mut ctx = Context::new();
    ctx.insert("all_weeks", &all_weeks);

    let rendered = tera.render("visual-companion.html.tera", &ctx)
        .expect("Visual companion template render failed");

    let out_dir = format!("{}/Visual Companion", output_root);
    fs::create_dir_all(&out_dir).unwrap();
    fs::write(format!("{}/index.html", out_dir), &rendered).unwrap();

    let css_src = Path::new(assets_dir).join("css");
    let css_dst = Path::new(&out_dir).join("css");
    fs::create_dir_all(&css_dst).ok();
    for entry in fs::read_dir(&css_src).unwrap() {
        let entry = entry.unwrap();
        fs::copy(entry.path(), css_dst.join(entry.file_name())).ok();
    }
    let font_src = Path::new(assets_dir).join("fonts");
    let font_dst = Path::new(&out_dir).join("fonts");
    fs::create_dir_all(&font_dst).ok();
    if font_src.exists() {
        for entry in fs::read_dir(&font_src).unwrap() {
            let entry = entry.unwrap();
            fs::copy(entry.path(), font_dst.join(entry.file_name())).ok();
        }
    }

    println!("  ✓  Visual Companion → {}/index.html", out_dir);
}

pub fn build_master_bundle(config_path: &str, output_root: &str) {
    let css_source_dir = format!("{}/Study Guide - Aid/Week 01/css", output_root);
    let base_css   = fs::read_to_string(format!("{}/base.css",   css_source_dir)).unwrap_or_default();
    let screen_css = fs::read_to_string(format!("{}/screen.css", css_source_dir)).unwrap_or_default();
    let print_css  = fs::read_to_string(format!("{}/print.css",  css_source_dir)).unwrap_or_default();

    let mut bundle = String::new();
    bundle.push_str("<!DOCTYPE html>\n<html lang=\"id\">\n<head>\n");
    bundle.push_str("<meta charset=\"UTF-8\">\n");
    bundle.push_str("<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n");
    bundle.push_str("<title>MNK202 — Master Print Bundle</title>\n");
    bundle.push_str(&format!("<style>\n{}\n{}\n{}\n</style>\n", base_css, screen_css, print_css));
    bundle.push_str("</head>\n<body>\n");

    for week in 1u8..=14 {
        for meta in DELIVERABLES {
            let html_path = format!(
                "{}/{}/Week {:02}/{}",
                output_root, meta.output_folder, week, meta.output_file
            );
            if let Ok(content) = fs::read_to_string(&html_path) {
                let body_content = extract_body(&content);
                bundle.push_str(&format!(
                    "\n<div class=\"week-page-break\" id=\"w{:02}-{}\">",
                    week, meta.type_key
                ));
                bundle.push_str(&body_content);
                bundle.push_str("</div>\n");
            }
        }
    }

    bundle.push_str("</body>\n</html>\n");

    let out_dir = format!("{}/Master Print Bundle", output_root);
    fs::create_dir_all(&out_dir).unwrap();
    let out_path = format!("{}/course-companion.html", out_dir);
    fs::write(&out_path, &bundle).expect("Failed to write master bundle");

    let size_kb = bundle.len() / 1024;
    println!("  ✓  Master Bundle → {} ({} KB)", out_path, size_kb);
}

fn extract_body(html: &str) -> String {
    if let (Some(start), Some(end)) = (html.find("<body"), html.rfind("</body>")) {
        let body_open_end = html[start..].find('>').map(|i| start + i + 1).unwrap_or(start);
        return html[body_open_end..end].to_string();
    }
    html.to_string()
}
