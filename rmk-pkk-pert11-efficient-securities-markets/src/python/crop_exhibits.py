"""
crop_exhibits.py
Crops figures/tables from Scott, Financial Accounting Theory (7th ed.), Ch. 4
"Efficient Securities Markets — Pert. 11 (Kel. 3 Baru).pdf"
into 300-DPI PNGs for the RMK docx.

Four visuals:
  fig-4-1   Figure 4.1  — Organisation of Chapter 4 (flowchart, vector, p.1)
  table-4-1 Table 4.1   — Beaver football-forecasting results (text table, p.5)
  tip-4-1   Theory in Practice 4.1 — Malkiel / WSJ dartboard / Reg FD (box, p.6)
  fig-4-2   Figure 4.2  — Role of Financial Reporting (concentric circles, p.22)

IMPORTANT: This PDF has ZERO embedded raster images — all figures are vector
graphics + text. Crops are taken by RECTANGLE from rasterised pages, not from
image XObjects.

Usage:
  python src/python/crop_exhibits.py --pages    # render full survey pages to assets/exhibits/tmp/
  python src/python/crop_exhibits.py            # crop using the EXHIBITS table below
"""

import os
import sys

import fitz  # pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, "..", "..", "input", "chapter",
                   "Efficient Securities Market - Pert. 11 (Kel. 3 Baru).pdf")
ZOOM = 300 / 72  # 300 DPI
MAT = fitz.Matrix(ZOOM, ZOOM)

SURVEY_PAGES = [1, 2, 5, 6, 22]  # exhibit-bearing pages (1-based) + immediate neighbours

# name -> list of (pdf_page_1based, fitz.Rect in PDF points).
# Multiple entries are stitched vertically (for an exhibit spanning pages).
# Page size is A4 (595 x 842 pt). Content column spans x ~48..550.
# Scott 7th-ed convention: caption line is PART of the figure area; include it.
#
# Coordinates confirmed by:
#   - page.get_text("blocks") for text-only tables/boxes (y-bounds of caption + rows)
#   - page.get_drawings() bounding boxes for vector figures (circles/boxes/arrows)
EXHIBITS = {
    # Figure 4.1 — Organisation of Chapter 4.
    # Caption "Figure 4.1 Organization of Chapter 4" at p1 y=221–231.
    # Vector drawings span y=240..434 (boxes, arrows, text labels inside figure).
    # Body text ("4.1 OVERVIEW") resumes at y=446 — stop before it.
    "fig-4-1": [(1, fitz.Rect(48, 215, 550, 445))],

    # Table 4.1 — Forecasting Outcomes of Football Games (Beaver, 1981).
    # Caption at p5 y=382–393; table rows y=401–528; footnote + source y=552–605.
    "table-4-1": [(5, fitz.Rect(48, 376, 550, 612))],

    # Theory in Practice 4.1 — Malkiel / WSJ dartboard / Regulation FD.
    # Box caption at p6 y=293–304; box body y=320–594 (two-column text).
    # Body text resumes above (y<293) — exclude it.
    "tip-4-1": [(6, fitz.Rect(38, 287, 450, 602))],

    # Figure 4.2 — Role of Financial Reporting in an Efficient Market.
    # Caption "Figure 4.2 Role of Financial Reporting…" at p22 x=37.6 y=398–408.
    # Vector drawings (concentric ovals) span y=419..612; text labels inside.
    # Prose continues at p23 y=76 — figure fully fits on p22.
    # x0=32 to avoid clipping the leading space before "Figure 4.2".
    "fig-4-2": [(22, fitz.Rect(32, 392, 500, 622))],
}


def render_clip(doc, page_1based, rect):
    page = doc[page_1based - 1]
    pix = page.get_pixmap(matrix=MAT, clip=rect)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def survey(doc):
    out_dir = os.path.join(HERE, "..", "..", "assets", "exhibits", "tmp")
    os.makedirs(out_dir, exist_ok=True)
    for p in SURVEY_PAGES:
        page = doc[p - 1]
        img = render_clip(doc, p, page.rect)
        path = os.path.join(out_dir, f"page-{p:02d}.png")
        img.save(path)
        print(f"page {p}: {page.rect}  -> {path}")


def crop(doc):
    out_dir = os.path.join(HERE, "..", "..", "assets", "exhibits")
    os.makedirs(out_dir, exist_ok=True)
    for name, parts in EXHIBITS.items():
        images = [render_clip(doc, p, r) for p, r in parts]
        if len(images) == 1:
            combined = images[0]
        else:
            width = max(im.width for im in images)
            images = [im if im.width == width
                      else im.resize((width, int(im.height * width / im.width)))
                      for im in images]
            combined = Image.new("RGB", (width, sum(im.height for im in images)), "white")
            y = 0
            for im in images:
                combined.paste(im, (0, y))
                y += im.height
        out = os.path.join(out_dir, f"{name}.png")
        combined.save(out)
        print(f"{name}: {combined.width}x{combined.height} -> {out}")


if __name__ == "__main__":
    document = fitz.open(PDF)
    if "--pages" in sys.argv:
        survey(document)
    else:
        crop(document)
