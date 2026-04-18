use tera::{Context, Tera};
use crate::config::WeekConfig;

pub struct DeliverableMeta {
    pub type_key: &'static str,
    pub source_file: &'static str,
    pub output_folder: &'static str,
    pub output_file: &'static str,
    pub label: &'static str,
    pub template: &'static str,
}

pub const DELIVERABLES: &[DeliverableMeta] = &[
    DeliverableMeta {
        type_key: "study-guide",
        source_file: "study-guide.md",
        output_folder: "Study Guide - Aid",
        output_file: "index.html",
        label: "📖 Study Guide",
        template: "study-guide.html.tera",
    },
    DeliverableMeta {
        type_key: "summary",
        source_file: "summary.md",
        output_folder: "Main Summary - Ebook",
        output_file: "index.html",
        label: "📄 Main Summary",
        template: "summary.html.tera",
    },
    DeliverableMeta {
        type_key: "company-example",
        source_file: "company-example.md",
        output_folder: "Indonesian Company Examples",
        output_file: "examples.html",
        label: "🏢 Company Example",
        template: "company-example.html.tera",
    },
    DeliverableMeta {
        type_key: "review-sheet",
        source_file: "review-sheet.md",
        output_folder: "Review Sheet",
        output_file: "index.html",
        label: "📋 Review Sheet",
        template: "review-sheet.html.tera",
    },
    DeliverableMeta {
        type_key: "exercises",
        source_file: "exercises.md",
        output_folder: "Exercises",
        output_file: "index.html",
        label: "✏️ Exercises",
        template: "exercises.html.tera",
    },
];

pub fn build_context(
    week: u8,
    config: &WeekConfig,
    content_html: &str,
    meta: &DeliverableMeta,
    all_weeks: &[(u8, String)],
) -> Context {
    let mut ctx = Context::new();
    ctx.insert("week_num", &week);
    ctx.insert("week_pad", &format!("{:02}", week));
    ctx.insert("title", &config.title);
    ctx.insert("title_en", &config.title_en);
    ctx.insert("phase_label", &if config.phase == "pre-uts" { "Pra-UTS" } else { "Pasca-UTS" });
    ctx.insert("phase_class", &config.phase);
    ctx.insert("core_readings", &config.core_readings);
    ctx.insert("supplementary", &config.supplementary);
    ctx.insert("company_name", &config.company_name);
    ctx.insert("company_ticker", &config.company_ticker);
    ctx.insert("company_exchange", &config.company_exchange);
    ctx.insert("content_html", content_html);
    ctx.insert("deliverable_type", meta.type_key);
    ctx.insert("deliverable_label", meta.label);
    ctx.insert("deliverables", &DELIVERABLES.iter().map(|d| d.label).collect::<Vec<_>>());
    ctx.insert("all_weeks", all_weeks);
    ctx
}

pub fn render_template(tera: &Tera, template_name: &str, ctx: &Context) -> String {
    tera.render(template_name, ctx)
        .unwrap_or_else(|e| panic!("Template '{}' render failed: {}", template_name, e))
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::config::WeekConfig;

    fn stub_config() -> WeekConfig {
        WeekConfig {
            title: "Test Minggu".into(),
            title_en: "Test Week".into(),
            phase: "pre-uts".into(),
            core_readings: vec!["Wolk Ch.1".into()],
            supplementary: vec!["PSAK 1".into()],
            company_name: "Telkom Indonesia".into(),
            company_ticker: "TLKM".into(),
            company_exchange: "IDX".into(),
        }
    }

    #[test]
    fn test_context_phase_label_pre_uts() {
        let config = stub_config();
        let ctx = build_context(1, &config, "<p>content</p>", &DELIVERABLES[0], &[]);
        let label = ctx.get("phase_label").unwrap();
        assert!(label.to_string().contains("Pra-UTS"));
    }

    #[test]
    fn test_context_phase_label_post_uts() {
        let mut config = stub_config();
        config.phase = "post-uts".into();
        let ctx = build_context(8, &config, "", &DELIVERABLES[0], &[]);
        let label = ctx.get("phase_label").unwrap();
        assert!(label.to_string().contains("Pasca-UTS"));
    }

    #[test]
    fn test_week_pad_single_digit() {
        let config = stub_config();
        let ctx = build_context(3, &config, "", &DELIVERABLES[0], &[]);
        let pad = ctx.get("week_pad").unwrap();
        assert!(pad.to_string().contains("03"));
    }
}
