//! Concept-coverage + exhibit-anchoring audit CLI (human-readable report).

use anyhow::Result;
use clap::Parser;
use rmk_audit::{concept_ids, parse_doc, workspace_root};
use shared::Section;
use std::collections::BTreeSet;

/// Audit concept coverage across content sections.
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    /// Fail if any concept or section is missing (Phase 5 gate).
    #[arg(long)]
    strict: bool,
}

fn main() -> Result<()> {
    let args = Args::parse();
    let dir = workspace_root().join("content/sections");
    let mut covered = BTreeSet::new();
    let mut sections = 0u32;
    if dir.exists() {
        let mut paths: Vec<_> = std::fs::read_dir(&dir)?
            .filter_map(|e| e.ok().map(|e| e.path()))
            .filter(|p| p.extension().is_some_and(|e| e == "md"))
            .collect();
        paths.sort();
        for p in paths {
            let (s, _) = parse_doc::<Section>(&p)?;
            println!(
                "{}: {} concepts, {} exhibits",
                s.id,
                s.covers_concepts.len(),
                s.embeds_exhibits.len()
            );
            covered.extend(s.covers_concepts);
            sections += 1;
        }
    }
    let missing: Vec<_> = concept_ids()
        .into_iter()
        .filter(|c| !covered.contains(c))
        .collect();
    println!(
        "sections: {sections}/15 — concepts covered: {}/62",
        covered.len()
    );
    if !missing.is_empty() {
        println!("missing: {}", missing.join(", "));
    }
    if args.strict {
        anyhow::ensure!(sections == 15 && missing.is_empty(), "coverage incomplete");
    }
    Ok(())
}
