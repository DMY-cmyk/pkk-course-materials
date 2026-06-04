# Assignment Rules — verbatim from `sources/assignment/Tugas_RMK_Kelompok.png`

OCR method: Claude native vision (tesseract not installed on this machine — documented substitution).
Source: WhatsApp screenshot from the lecturer ("~ Fik", +62 811-252-357), messages timestamped 18.27–18.35.

## Context messages
> "Selamat malam. Utk capaian perkuliahan, silakan bikin kelompok dg anggota per kelompok maksimum 4. Thanks" *(18.27 — group formation; note: Kelompok 2 has 6 members per the roster image, so the lecturer evidently revised or this rule predates final grouping — identity follows the roster, not this message)*

> "Utk **setiap** pertemuan […] tugas kelompok adalah membuat RMK Kelompok dengan ketentuan:" *(18.34; handwritten annotation "Setiap" overlaid on the screenshot)*

## THE FIVE FORMAT RULES (verbatim — HARD GATES)
1. **Ukuran kertas A4.**
2. **Jarak antar baris 1,5 spasi**
3. **Font size 12 calibri atau aptos.**
4. **Minimal RMK 8 halaman**
5. **Dibikin dalam format MS Word**

## Submission logistics
> "1 anggota mewakili semua anggota kelompok utk unggah RMK" *(below "*tugas", 18.35)*

⇒ One member uploads on behalf of the group ⇒ the document itself must carry **all six members' names + NIMs**.

## Validation mapping
| Rule | Gate in `rmk-validate` |
|---|---|
| A4 | docx sectPr page size = 11906×16838 twips (A4) |
| 1.5 spasi | paragraph spacing `line=360, lineRule=auto` throughout body |
| 12 pt Calibri/Aptos | run fonts + size across all body styles |
| ≥ 8 halaman | rendered page count ≥ 8 |
| MS Word | `.docx` (OOXML), opens in Word + LibreOffice |
| Identity | all 6 names + NIMs present on cover/identity block |
