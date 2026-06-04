//! Markdown-subset -> block-list compiler for the docx bridge.

use serde::Serialize;
use shared::{Exhibit, RenderType};

#[derive(Debug, PartialEq, Serialize)]
#[serde(tag = "type", rename_all = "kebab-case")]
pub enum Block {
    Heading { level: u8, text: String },
    Para { runs: Vec<Run> },
    Center { runs: Vec<Run> },
    Image { path: String, width_in: f64 },
    Caption { text: String },
    Table { rows: Vec<Vec<String>> },
    Equation { label: String, text: String },
}

#[derive(Debug, PartialEq, Serialize)]
pub struct Run {
    pub text: String,
    pub bold: bool,
    pub italic: bool,
}

/// Parse `**bold**` / `*italic*` inline markup into runs.
pub fn parse_runs(s: &str) -> Vec<Run> {
    let mut runs = Vec::new();
    let mut rest = s;
    while !rest.is_empty() {
        if let Some(r) = rest.strip_prefix("**") {
            if let Some(end) = r.find("**") {
                runs.push(Run {
                    text: r[..end].into(),
                    bold: true,
                    italic: false,
                });
                rest = &r[end + 2..];
                continue;
            }
        }
        if let Some(r) = rest.strip_prefix('*') {
            if let Some(end) = r.find('*') {
                runs.push(Run {
                    text: r[..end].into(),
                    bold: false,
                    italic: true,
                });
                rest = &r[end + 1..];
                continue;
            }
        }
        let next = rest[1..].find('*').map(|i| i + 1).unwrap_or(rest.len());
        runs.push(Run {
            text: rest[..next].into(),
            bold: false,
            italic: false,
        });
        rest = &rest[next..];
    }
    runs
}

fn parse_table_row(line: &str) -> Vec<String> {
    line.trim()
        .trim_start_matches('|')
        .trim_end_matches('|')
        .split('|')
        .map(|c| c.trim().replace("&nbsp;", "\u{00A0}"))
        .collect()
}

fn is_separator_row(line: &str) -> bool {
    let t: String = line.chars().filter(|c| !c.is_whitespace()).collect();
    !t.is_empty() && t.chars().all(|c| matches!(c, '|' | '-' | ':'))
}

/// Compile one markdown body into blocks, resolving exhibit directives.
/// `reset_table_base` is the directory against which Exhibit.reset_table paths resolve.
pub fn compile_body(
    body: &str,
    manifest: &[Exhibit],
    figures_dir: &str,
    reset_table_base: &std::path::Path,
) -> anyhow::Result<Vec<Block>> {
    let mut blocks = Vec::new();
    let lines: Vec<&str> = body.lines().collect();
    let mut i = 0;
    while i < lines.len() {
        let trimmed = lines[i].trim();
        if trimmed.is_empty() {
            i += 1;
            continue;
        }
        if let Some(h) = trimmed.strip_prefix("## ") {
            blocks.push(Block::Heading {
                level: 2,
                text: h.into(),
            });
        } else if let Some(h) = trimmed.strip_prefix("# ") {
            blocks.push(Block::Heading {
                level: 1,
                text: h.into(),
            });
        } else if let Some(c) = trimmed
            .strip_prefix("{{center:")
            .and_then(|s| s.strip_suffix("}}"))
        {
            blocks.push(Block::Center {
                runs: parse_runs(c),
            });
        } else if let Some(id) = trimmed
            .strip_prefix("{{exhibit:")
            .and_then(|s| s.strip_suffix("}}"))
        {
            let ex = manifest
                .iter()
                .find(|e| e.id == id)
                .ok_or_else(|| anyhow::anyhow!("unknown exhibit id {id}"))?;
            match ex.render_type {
                RenderType::Crop => {
                    blocks.push(Block::Image {
                        path: format!("{figures_dir}/{}.png", ex.id),
                        width_in: ex.target_width_in,
                    });
                    blocks.push(Block::Caption {
                        text: ex.caption.clone(),
                    });
                }
                RenderType::ResetTable => {
                    let rel = ex.reset_table.as_ref().expect("reset_table path");
                    let table_md = std::fs::read_to_string(reset_table_base.join(rel))?;
                    let rows = table_md
                        .lines()
                        .filter(|l| l.trim().starts_with('|') && !is_separator_row(l))
                        .map(parse_table_row)
                        .collect();
                    blocks.push(Block::Table { rows });
                    blocks.push(Block::Caption {
                        text: ex.caption.clone(),
                    });
                }
                RenderType::ResetEquation => blocks.push(Block::Equation {
                    label: ex.label.clone().unwrap_or_default(),
                    text: ex.reset_text.clone().unwrap_or_default(),
                }),
            }
        } else if trimmed.starts_with('|') {
            let mut rows = Vec::new();
            while i < lines.len() && lines[i].trim().starts_with('|') {
                if !is_separator_row(lines[i]) {
                    rows.push(parse_table_row(lines[i]));
                }
                i += 1;
            }
            blocks.push(Block::Table { rows });
            continue;
        } else {
            let mut para = String::from(trimmed);
            while i + 1 < lines.len() {
                let n = lines[i + 1].trim();
                if n.is_empty() || n.starts_with('#') || n.starts_with('|') || n.starts_with("{{") {
                    break;
                }
                para.push(' ');
                para.push_str(n);
                i += 1;
            }
            blocks.push(Block::Para {
                runs: parse_runs(&para),
            });
        }
        i += 1;
    }
    Ok(blocks)
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::path::Path;

    #[test]
    fn runs_parse_bold_italic() {
        let r = parse_runs("a **b** c *d*");
        assert_eq!(r.len(), 4);
        assert!(r[1].bold && r[1].text == "b");
        assert!(r[3].italic && r[3].text == "d");
    }

    #[test]
    fn heading_and_para() {
        let b = compile_body(
            "# Judul\n\nIsi satu\nlanjutan.",
            &[],
            "content/figures",
            Path::new("."),
        )
        .unwrap();
        assert_eq!(b.len(), 2);
        assert!(matches!(&b[0], Block::Heading { level: 1, text } if text == "Judul"));
        assert!(matches!(&b[1], Block::Para { runs } if runs[0].text == "Isi satu lanjutan."));
    }

    #[test]
    fn pipe_table_parses() {
        let b = compile_body(
            "| A | B |\n| --- | --- |\n| 1 | 2 |",
            &[],
            "f",
            Path::new("."),
        )
        .unwrap();
        assert!(
            matches!(&b[0], Block::Table { rows } if rows.len() == 2 && rows[1] == vec!["1", "2"])
        );
    }

    #[test]
    fn equation_directive_resolves() {
        let manifest = vec![Exhibit {
            id: "eq-13-1".into(),
            caption: String::new(),
            render_type: RenderType::ResetEquation,
            segments: vec![],
            target_width_in: 6.25,
            anchor_section: "01-scfp-funds-flow".into(),
            reset_text: Some("transaction credits = transaction debits".into()),
            reset_table: None,
            label: Some("(13.1)".into()),
        }];
        let b = compile_body("{{exhibit:eq-13-1}}", &manifest, "f", Path::new(".")).unwrap();
        assert!(matches!(&b[0], Block::Equation { label, .. } if label == "(13.1)"));
    }

    #[test]
    fn unknown_exhibit_errors() {
        assert!(compile_body("{{exhibit:nope}}", &[], "f", Path::new(".")).is_err());
    }

    #[test]
    fn center_directive_parses() {
        let b = compile_body("{{center:**Judul Tengah**}}", &[], "f", Path::new(".")).unwrap();
        assert!(
            matches!(&b[0], Block::Center { runs } if runs[0].bold && runs[0].text == "Judul Tengah")
        );
    }
}
