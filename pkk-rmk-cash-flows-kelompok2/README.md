# RMK Chapter 13 — Statement of Cash Flows (Kelompok 2)

From-scratch, exhibit-rich RMK of Wolk, Dodd & Rozycki Ch. 13 for Pelaporan
Keuangan Korporat (MNK202). Final deliverable:
`output/RMK Chap. 13_Kelompok 2_PKK.docx`.

- Governing docs: `.claude/CLAUDE.md`, `specs/rmk-spec.md`, `specs/design-decisions.md`
- Phase 0 audit: `analysis/`
- Pipeline: Cargo workspace (`crates/`) + python-docx bridge (`tools/build_docx.py`)

## Commands
```
cargo run -p rmk-extract-figures        # Phase 3.5: crop exhibits -> content/figures/
cargo run -p rmk-audit                  # concept-coverage audit
cargo run -p rmk-build -- --smoke       # bridge smoke test (Phase 2 baseline)
cargo run -p rmk-build -- --output "output/RMK Chap. 13_Kelompok 2_PKK.docx"
cargo run -p rmk-validate -- --report output/VALIDATION-REPORT.md
cargo test && cargo clippy -- -D warnings && cargo fmt --check
```
