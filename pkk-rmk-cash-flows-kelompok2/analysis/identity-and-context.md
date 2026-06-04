# Identity and Context — Tier 3 Audit

## Kelompok 2 Roster (verbatim from `sources/group/Kelompok_2_Member_NIMs.jpeg`)
OCR method: Claude native vision. The image matches the master prompt's roster **exactly** — no discrepancies.

| NIM | Name |
|---|---|
| 122501039 | Satriyo Nugroho |
| 122501048 | Mario Da Costa |
| 122501067 | Amelda Putri Zhany Wiguna |
| 122501078 | Ahmad Ramadhan |
| 122501084 | Nida Nur Cahyati |
| 122501094 | Priska Putri Parungky |

Note: the lecturer's group-formation message said "maksimum 4" per group, but the authoritative roster image lists 6 members. **The roster governs.**

## Syllabus confirmation (`sources/syllabus/Silabus_Pelaporan_Keuangan_Korporat_25-26.pdf`)
- Course: **Pelaporan Keuangan Korporat**, code **MNK202**, 3 SKS.
- Text "W" = Wolk, Harry I., James L. Dodd, John J. Rozycki, *Accounting Theory: Conceptual Issues in a Political and Economic Environment*, 9th ed., USA, Sage Publications, Inc. 2017.
- **Session IX (Tuesday): "Statement of Cash Flows" — W-13 — TT — HW 8 — Group** ⇒ this RMK is the Session-IX group deliverable, exactly the chapter in our source PDF.
- Course orientation: conceptual / decision-usefulness (Scott "S" is the other main text) ⇒ depth calibration: theory-led exposition (proprietary vs entity theory, allocation problem, decision usefulness), not procedural bookkeeping.

## Filename discrepancy flag (carry into Phase 1)
Requested deliverable name: `RMK Chap. 13_Kelompok 2_ALK.docx`. **"ALK"** (likely Analisis Laporan Keuangan) does not match this course (PKK / MNK202). Per the master prompt: preserve the requested name verbatim, but confirm with the user in Phase 1 before building.
- Filesystem check: the name contains no illegal Windows characters (the `.` and spaces are fine) — **no substitution needed**.

## Toolchain substitutions (to be carried into VALIDATION-REPORT.md)
1. `tesseract` not installed → Claude native vision used for both image OCR tasks (higher fidelity for WhatsApp screenshots than tesseract `ind+eng`).
2. `/mnt/skills/public/docx` (docx skill) not present on this Windows host → **python-docx** `build_docx.py` bridge, the pattern already proven in this repo (`ti4/output/build_docx.py`, `ti5/output/build_docx.py`). Single-source-of-truth architecture unchanged: Rust assembles markdown + manifest and shells out to the Python bridge.
3. poppler utilities provided by MiKTeX (`pdftotext`, `pdftoppm`, `pdfimages` all verified working).
