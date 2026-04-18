mod config;
mod markdown;
mod renderer;
mod builder;
mod bundle;

use clap::{Parser, Subcommand};
use tera::Tera;
use std::path::Path;

#[derive(Parser)]
#[command(name = "devassist", about = "MNK202 course content builder")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Build a single week (1–14)
    Week {
        number: u8,
    },
    /// Build a range of weeks, e.g. "1-7"
    Weeks {
        range: String,
    },
    /// Build all 14 weeks
    All,
    /// Build the Visual Companion web app
    VisualCompanion,
    /// Build the Master Print Bundle
    MasterBundle,
}

fn main() {
    let cli = Cli::parse();

    let manifest_dir = Path::new(env!("CARGO_MANIFEST_DIR"));
    let templates_glob = manifest_dir.join("templates/**/*.tera");
    let templates_str = templates_glob.to_str().unwrap();
    let tera = Tera::new(templates_str).expect("Failed to load Tera templates");

    let config_path = manifest_dir.join("configs/mapping.toml");
    let config_path_str = config_path.to_str().unwrap();

    let content_dir = manifest_dir.join("content");
    let content_dir_str = content_dir.to_str().unwrap();

    let assets_dir = manifest_dir.join("assets");
    let assets_dir_str = assets_dir.to_str().unwrap();

    // Output root is one level up from Dev Assistant/ (repo root), then into course-materials/outputs
    let output_root = manifest_dir
        .parent().unwrap()  // repo root
        .join("course-materials/outputs");
    let output_root_str = output_root.to_str().unwrap();

    match cli.command {
        Commands::Week { number } => {
            println!("Building Week {:02}...", number);
            builder::build_week(number, &tera, config_path_str, content_dir_str, assets_dir_str, output_root_str);
        }
        Commands::Weeks { range } => {
            println!("Building weeks {}...", range);
            builder::build_weeks_range(&range, &tera, config_path_str, content_dir_str, assets_dir_str, output_root_str);
        }
        Commands::All => {
            println!("Building all 14 weeks...");
            builder::build_all(&tera, config_path_str, content_dir_str, assets_dir_str, output_root_str);
        }
        Commands::VisualCompanion => {
            println!("Building Visual Companion...");
            bundle::build_visual_companion(&tera, config_path_str, assets_dir_str, output_root_str);
        }
        Commands::MasterBundle => {
            println!("Building Master Bundle...");
            bundle::build_master_bundle(assets_dir_str, output_root_str);
        }
    }

    println!("Done.");
}
