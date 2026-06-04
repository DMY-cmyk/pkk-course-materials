"""python-docx bridge for the RMK pipeline.

Documented substitution for the docx skill (unavailable on this Windows host).
Invoked by crates/rmk-build. Phase 2 ships --smoke only; the full
markdown+manifest assembly lands in Phase 4.
"""
import argparse
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Mm, Pt

ROOT = Path(__file__).resolve().parent.parent

FONT = "Calibri"          # Phase 1 decision D3
FONT_SIZE_PT = 12
LINE_SPACING = 1.5
FULL_COLUMN_IN = 6.25     # Phase 1 decision D4


def base_doc() -> Document:
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)  # A4
    sec.top_margin = sec.bottom_margin = Mm(25.4)
    sec.left_margin = sec.right_margin = Mm(25.4)
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(FONT_SIZE_PT)
    normal.paragraph_format.line_spacing = LINE_SPACING
    normal.paragraph_format.space_after = Pt(6)
    return doc


def smoke() -> int:
    """Produce a stub docx proving A4 / 1.5 / Calibri 12 / image embedding."""
    test_image = ROOT / "previews" / "_fig" / "exhibit-13-10.png"
    if not test_image.exists():
        print(f"smoke: test image missing: {test_image}", file=sys.stderr)
        return 1
    doc = base_doc()
    doc.add_paragraph("Smoke test — A4, 1.5 spacing, Calibri 12 pt.")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(test_image), width=Inches(FULL_COLUMN_IN))
    out = ROOT / "output" / "_smoke.docx"
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)
    # verify round-trip
    check = Document(str(out))
    sec = check.sections[0]
    # Word stores page size in twips, so EMU round-trips within ~0.02 mm.
    assert abs(sec.page_width - Mm(210)) < Mm(0.05), "not A4 width"
    assert abs(sec.page_height - Mm(297)) < Mm(0.05), "not A4 height"
    assert check.styles["Normal"].font.name == FONT, "font mismatch"
    assert check.styles["Normal"].font.size == Pt(FONT_SIZE_PT), "size mismatch"
    assert check.styles["Normal"].paragraph_format.line_spacing == LINE_SPACING
    assert check.inline_shapes, "no embedded image"
    print(f"smoke OK: {out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--smoke", action="store_true", help="baseline smoke test")
    args = ap.parse_args()
    if args.smoke:
        return smoke()
    print("full build not yet implemented (Phase 4)", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
