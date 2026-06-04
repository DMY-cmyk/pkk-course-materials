//! Shared domain types for the RMK Ch. 13 pipeline.

use serde::{Deserialize, Serialize};

/// A single chapter concept (C-01..C-62) from the Phase 0 inventory.
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct Concept {
    /// e.g. "C-29"
    pub id: String,
    pub description: String,
    /// e.g. "Wolk Ch.13, PDF p.9"
    pub wolk_ref: String,
    /// Section id that owns this concept, e.g. "06-nonarticulation"
    pub section: String,
}

/// How an exhibit reaches the final document (Phase 1 decisions D5/D7).
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "kebab-case")]
pub enum RenderType {
    /// Cropped from the source PDF at 240 dpi (Exhibits 13.4-13.11).
    Crop,
    /// Rebuilt as a native Word table (Exhibits 13.1-13.3).
    ResetTable,
    /// Rebuilt as a centered bold text line (Equations 13.1/13.2).
    ResetEquation,
}

/// One crop segment: source page + [left, top, right, bottom] page fractions.
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct CropSegment {
    pub page: u32,
    pub box_pct: [f64; 4],
}

/// A figure-manifest entry (content/figures/manifest.yaml).
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct Exhibit {
    /// e.g. "exhibit-13-04" or "eq-13-1"
    pub id: String,
    pub caption: String,
    pub render_type: RenderType,
    /// Crop segments (empty for reset-* render types).
    #[serde(default)]
    pub segments: Vec<CropSegment>,
    /// Embed width in inches (Phase 1 decision D4: 6.25 for crops).
    pub target_width_in: f64,
    /// e.g. "06-nonarticulation"
    pub anchor_section: String,
}

/// A content section (content/sections/*.md front matter).
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct Section {
    /// e.g. "05-direct-vs-indirect"
    pub id: String,
    pub title: String,
    #[serde(default)]
    pub covers_concepts: Vec<String>,
    #[serde(default)]
    pub embeds_exhibits: Vec<String>,
    /// e.g. "rubrics/05-direct-vs-indirect.md"
    pub rubric: String,
}

/// A per-section rubric (rubrics/*.md front matter).
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct Rubric {
    pub id: String,
    #[serde(default)]
    pub required_concepts: Vec<String>,
    #[serde(default)]
    pub required_exhibits: Vec<String>,
    #[serde(default)]
    pub wolk_refs: Vec<String>,
    #[serde(default)]
    pub format_rules: Vec<String>,
    #[serde(default)]
    pub depth_check: Vec<String>,
}

/// One of the lecturer's five hard format gates (plus the identity rule).
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct FormatRule {
    /// e.g. "a4", "line-spacing-1-5", "font-calibri-12", "min-8-pages", "docx"
    pub id: String,
    pub description: String,
}

impl FormatRule {
    /// The five lecturer gates plus the identity rule, in canonical order.
    pub fn hard_gates() -> Vec<FormatRule> {
        let gates = [
            ("a4", "Ukuran kertas A4"),
            ("line-spacing-1-5", "Jarak antar baris 1,5 spasi"),
            (
                "font-calibri-12",
                "Font size 12 Calibri (Phase 1 decision D3)",
            ),
            ("min-8-pages", "Minimal RMK 8 halaman"),
            ("docx", "Dibikin dalam format MS Word (.docx)"),
            (
                "identity",
                "Seluruh 6 anggota + NIM tercantum pada halaman identitas",
            ),
        ];
        gates
            .into_iter()
            .map(|(id, description)| FormatRule {
                id: id.to_string(),
                description: description.to_string(),
            })
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn exhibit_manifest_yaml_roundtrip() {
        let exhibit = Exhibit {
            id: "exhibit-13-04".to_string(),
            caption: "Exhibit 13.4 — Comparison of Balance Sheet Changes and Working \
                      Capital Adjustments for 3M Company ($000,000) (Wolk, Dodd & \
                      Rozycki, 2017, Ch. 13)"
                .to_string(),
            render_type: RenderType::Crop,
            segments: vec![CropSegment {
                page: 10,
                box_pct: [0.0, 0.27, 1.0, 0.46],
            }],
            target_width_in: 6.25,
            anchor_section: "06-nonarticulation".to_string(),
        };
        let yaml = serde_yaml::to_string(&exhibit).expect("serialize");
        let back: Exhibit = serde_yaml::from_str(&yaml).expect("deserialize");
        assert_eq!(exhibit, back);
        assert!(yaml.contains("render_type: crop"));
    }

    #[test]
    fn render_type_kebab_case() {
        let yaml = "reset-table";
        let rt: RenderType = serde_yaml::from_str(yaml).expect("parse");
        assert_eq!(rt, RenderType::ResetTable);
    }

    #[test]
    fn six_hard_gates() {
        let gates = FormatRule::hard_gates();
        assert_eq!(gates.len(), 6);
        assert_eq!(gates[0].id, "a4");
        assert_eq!(gates[3].id, "min-8-pages");
    }
}
