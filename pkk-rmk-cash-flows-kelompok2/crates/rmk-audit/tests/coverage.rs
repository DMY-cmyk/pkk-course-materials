use rmk_audit::{concept_ids, contains_ci, parse_doc, workspace_root};
use shared::{Exhibit, RenderType, Rubric, Section};
use std::collections::BTreeSet;
use std::fs;

fn rubric_paths() -> Vec<std::path::PathBuf> {
    let dir = workspace_root().join("rubrics");
    let mut v: Vec<_> = fs::read_dir(dir)
        .map(|rd| {
            rd.filter_map(|e| e.ok().map(|e| e.path()))
                .filter(|p| p.extension().is_some_and(|e| e == "md"))
                .collect()
        })
        .unwrap_or_default();
    v.sort();
    v
}

fn load_manifest() -> Vec<Exhibit> {
    let path = workspace_root().join("content/figures/manifest.yaml");
    serde_yaml::from_str(&fs::read_to_string(path).expect("manifest")).expect("manifest yaml")
}

#[test]
fn manifest_is_complete_and_consistent() {
    let manifest = load_manifest();
    let ids: BTreeSet<_> = manifest.iter().map(|e| e.id.as_str()).collect();
    assert_eq!(ids.len(), manifest.len(), "duplicate exhibit ids");
    for n in 1..=11 {
        assert!(
            ids.contains(format!("exhibit-13-{n:02}").as_str()),
            "missing 13.{n}"
        );
    }
    assert!(
        ids.contains("eq-13-1") && ids.contains("eq-13-2"),
        "missing equations"
    );
    for ex in &manifest {
        match ex.render_type {
            RenderType::Crop => {
                assert!(!ex.segments.is_empty(), "{}: crop without segments", ex.id);
                assert!(!ex.caption.is_empty(), "{}: crop without caption", ex.id);
            }
            RenderType::ResetTable => {
                let p = workspace_root().join(ex.reset_table.as_ref().expect("reset_table"));
                assert!(p.exists(), "{}: reset_table file missing", ex.id);
            }
            RenderType::ResetEquation => {
                assert!(
                    ex.reset_text.is_some() && ex.label.is_some(),
                    "{}: equation fields",
                    ex.id
                );
            }
        }
    }
}

#[test]
fn existing_sections_satisfy_their_rubrics() {
    let manifest = load_manifest();
    for rpath in rubric_paths() {
        let (rubric, _) = parse_doc::<Rubric>(&rpath).expect("rubric parses");
        let spath = workspace_root().join(format!("content/sections/{}.md", rubric.id));
        if !spath.exists() {
            continue; // section not yet written — strict test catches this at the end
        }
        let (section, body) = parse_doc::<Section>(&spath).expect("section parses");
        assert_eq!(section.id, rubric.id, "id mismatch in {}", spath.display());
        for kw in &rubric.required_keywords {
            assert!(
                contains_ci(&body, kw),
                "{}: missing required keyword {kw:?}",
                rubric.id
            );
        }
        for ex_id in &rubric.required_exhibits {
            assert!(
                section.embeds_exhibits.contains(ex_id),
                "{}: front matter missing exhibit {ex_id}",
                rubric.id
            );
            assert!(
                body.contains(&format!("{{{{exhibit:{ex_id}}}}}")),
                "{}: body missing directive for {ex_id}",
                rubric.id
            );
            assert!(
                manifest.iter().any(|m| &m.id == ex_id),
                "{}: exhibit {ex_id} not in manifest",
                rubric.id
            );
        }
    }
}

#[test]
#[ignore = "run in Phase 5: requires all 15 sections"]
fn strict_completeness() {
    let rubrics = rubric_paths();
    assert_eq!(rubrics.len(), 15, "expected 15 rubrics");
    let mut covered = Vec::new();
    for rpath in rubrics {
        let (rubric, _) = parse_doc::<Rubric>(&rpath).expect("rubric");
        let spath = workspace_root().join(format!("content/sections/{}.md", rubric.id));
        assert!(spath.exists(), "missing section {}", rubric.id);
        let (section, _) = parse_doc::<Section>(&spath).expect("section");
        covered.extend(section.covers_concepts.clone());
    }
    let unique: BTreeSet<_> = covered.iter().cloned().collect();
    assert_eq!(covered.len(), unique.len(), "concept assigned twice");
    let expected: BTreeSet<_> = concept_ids().into_iter().collect();
    assert_eq!(unique, expected, "concept coverage gap or surplus");
    // every manifest exhibit anchored by exactly one section that embeds it
    for ex in load_manifest() {
        let spath = workspace_root().join(format!("content/sections/{}.md", ex.anchor_section));
        let (section, body) = parse_doc::<Section>(&spath).expect("anchor section");
        assert!(
            section.embeds_exhibits.contains(&ex.id),
            "{} not embedded",
            ex.id
        );
        assert!(body.contains(&format!("{{{{exhibit:{}}}}}", ex.id)));
    }
}
