use serde::Deserialize;
use std::collections::HashMap;

#[derive(Deserialize, Debug, Clone)]
pub struct MappingConfig {
    pub weeks: HashMap<String, WeekConfig>,
}

#[derive(Deserialize, Debug, Clone)]
pub struct WeekConfig {
    pub title: String,
    pub title_en: String,
    pub phase: String,
    pub core_readings: Vec<String>,
    pub supplementary: Vec<String>,
    pub company_name: String,
    pub company_ticker: String,
    pub company_exchange: String,
}

pub fn load_config(path: &str) -> Result<MappingConfig, Box<dyn std::error::Error>> {
    let content = std::fs::read_to_string(path)
        .map_err(|e| format!("Cannot read config {}: {}", path, e))?;
    let config: MappingConfig = toml::from_str(&content)
        .map_err(|e| format!("Cannot parse config {}: {}", path, e))?;
    Ok(config)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_load_config_w1() {
        let manifest = env!("CARGO_MANIFEST_DIR");
        let path = format!("{}/configs/mapping.toml", manifest);
        let config = load_config(&path).unwrap();
        let w1 = config.weeks.get("1").expect("week 1 must exist in mapping.toml");
        assert_eq!(w1.company_ticker, "TLKM");
        assert_eq!(w1.phase, "pre-uts");
    }

    #[test]
    fn test_all_14_weeks_present() {
        let manifest = env!("CARGO_MANIFEST_DIR");
        let path = format!("{}/configs/mapping.toml", manifest);
        let config = load_config(&path).unwrap();
        for w in 1u8..=14 {
            assert!(config.weeks.contains_key(&w.to_string()), "Week {} missing from config", w);
        }
    }
}
