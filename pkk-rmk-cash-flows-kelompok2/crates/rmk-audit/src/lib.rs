//! Front-matter parsing + coverage checks shared by tests and the CLI.

use anyhow::{Context, Result};
use serde::de::DeserializeOwned;
use std::path::{Path, PathBuf};

/// Workspace root (= pkk-rmk-cash-flows-kelompok2/), resolved from this crate.
pub fn workspace_root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("../..")
        .canonicalize()
        .expect("workspace root")
}

/// Split a markdown file into (front-matter YAML, body).
/// Normalises CRLF → LF before parsing so the function works on Windows.
pub fn split_front_matter(text: &str) -> Result<(String, String)> {
    let normalised = text.replace('\r', "");
    let rest = normalised
        .strip_prefix("---\n")
        .context("missing front-matter opening '---'")?
        .to_owned();
    let end = rest
        .find("\n---")
        .context("missing front-matter closing '---'")?;
    let yaml = rest[..end].to_string();
    let body = rest[end + 4..].trim_start_matches('\n').to_string();
    Ok((yaml, body))
}

/// Parse a markdown file's front matter into T, returning (T, body).
pub fn parse_doc<T: DeserializeOwned>(path: &Path) -> Result<(T, String)> {
    let text =
        std::fs::read_to_string(path).with_context(|| format!("reading {}", path.display()))?;
    let (yaml, body) = split_front_matter(&text)?;
    let meta: T = serde_yaml::from_str(&yaml)
        .with_context(|| format!("front matter of {}", path.display()))?;
    Ok((meta, body))
}

/// The canonical 62 concept ids C-01..C-62.
pub fn concept_ids() -> Vec<String> {
    (1..=62).map(|i| format!("C-{i:02}")).collect()
}

/// Case-insensitive containment check.
pub fn contains_ci(haystack: &str, needle: &str) -> bool {
    haystack.to_lowercase().contains(&needle.to_lowercase())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn split_front_matter_works() {
        let doc = "---\nid: x\n---\nBody here";
        let (yaml, body) = split_front_matter(doc).unwrap();
        assert_eq!(yaml.trim(), "id: x");
        assert_eq!(body, "Body here");
    }

    #[test]
    fn split_front_matter_crlf() {
        let doc = "---\r\nid: x\r\n---\r\nBody here";
        let (yaml, body) = split_front_matter(doc).unwrap();
        assert_eq!(yaml.trim(), "id: x");
        assert_eq!(body, "Body here");
    }

    #[test]
    fn sixty_two_concepts() {
        let ids = concept_ids();
        assert_eq!(ids.len(), 62);
        assert_eq!(ids[0], "C-01");
        assert_eq!(ids[61], "C-62");
    }

    #[test]
    fn contains_ci_is_case_insensitive() {
        assert!(contains_ci("Survei McEnroe menemukan", "mcenroe"));
        assert!(!contains_ci("abc", "xyz"));
    }
}
