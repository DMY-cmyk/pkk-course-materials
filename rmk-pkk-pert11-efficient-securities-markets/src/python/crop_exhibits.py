"""
crop_exhibits.py
Crops Exhibits from "PKK Pert. 10 - Statement of Cashflow.pdf" (Wolk Ch.13)
into 300-DPI PNGs for the RMK docx.

Usage:
  python src/python/crop_exhibits.py --pages    # render full survey pages to assets/exhibits/tmp/
  python src/python/crop_exhibits.py            # crop using the EXHIBITS table below
"""

import os
import sys

import fitz  # pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, "..", "..", "input", "chapter", "PKK Pert. 10 - Statement of Cashflow.pdf")
ZOOM = 300 / 72  # 300 DPI
MAT = fitz.Matrix(ZOOM, ZOOM)

SURVEY_PAGES = [3, 4, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 20]  # exhibit-bearing pages (1-based)

# name -> list of (pdf_page_1based, fitz.Rect in PDF points).
# Multiple entries are stitched vertically (for an exhibit spanning pages).
# Page size is A4 (595 x 842 pt). Content column spans x ~50..545.
# SAGE convention: the "Exhibit 13.x" caption line sits ABOVE its table; the
# table may flow onto / live on the next page, so several exhibits are stitched
# from two page-clips ([caption page] + [table page]).
#
# Coordinates confirmed by:
#   - page.get_text("blocks") for text-only tables (y-bounds of caption + list items)
#   - page.get_text("rawdict") IMAGE bbox for embedded raster tables
EXHIBITS = {
    # Caption "Exhibit 13.1 Standard Format…" at p3 y=623–635; "Sources" subtitle
    # y=641–653; bulleted Sources list y=672–737 (bottom of page).
    # "Uses of Resources" header + bulleted Uses list at p4 y=72–168; body text
    # resumes at y=196 — stop there.
    "exhibit-13-1": [
        (3, fitz.Rect(48, 617, 550, 742)),
        (4, fitz.Rect(48, 66, 550, 175)),
    ],
    # caption + COMPANY M header + table start on p7, table body on p8 (stop
    # before the 13.3 caption at y=601).
    "exhibit-13-2": [
        (7, fitz.Rect(48, 696, 550, 770)),
        (8, fitz.Rect(48, 66, 550, 594)),
    ],
    # caption + reconciliation table on p8, tail rows on p9 (ends "Liabilities
    # assumed $630" at y=411).
    "exhibit-13-3": [
        (8, fitz.Rect(48, 596, 550, 770)),
        (9, fitz.Rect(48, 66, 550, 420)),
    ],
    # caption (y=242) + "Company ($000,000)" + embedded table image (y 266..367).
    "exhibit-13-4": [(10, fitz.Rect(48, 237, 550, 372))],
    # caption on p12 (y=465) + embedded table image on p13 (y 70..374.5).
    "exhibit-13-5": [
        (12, fitz.Rect(48, 459, 550, 478)),
        (13, fitz.Rect(48, 66, 550, 380)),
    ],
    # caption on p15 (y=656) + embedded table image on p16 (y 70..209).
    "exhibit-13-6": [
        (15, fitz.Rect(48, 650, 550, 670)),
        (16, fitz.Rect(48, 66, 550, 214)),
    ],
    # Exhibit 13.7 — Income Statement and Balance Sheet for ABC Company.
    # Caption at p18 y=80–91; IMAGE (raster) at p18 y=91.5–500.
    "exhibit-13-7": [(18, fitz.Rect(48, 74, 550, 506))],
    # Exhibit 13.8 — Statement of Cash Flows for ABC Company.
    # Caption at p18 y=687–697; IMAGE continues to p19 y=70–431.
    "exhibit-13-8": [
        (18, fitz.Rect(48, 681, 550, 702)),
        (19, fitz.Rect(48, 66, 550, 437)),
    ],
    # Exhibit 13.9 — Statement of Free Cash Flows for ABC Company.
    # Caption at p19 y=487–497; IMAGE on p20 y=70–610.
    "exhibit-13-9": [
        (19, fitz.Rect(48, 481, 550, 500)),
        (20, fitz.Rect(48, 66, 550, 615)),
    ],
    # Exhibit 13.10 — Computing Free Cash Flow From the SCF for ABC Company.
    # Caption at p20 y=627–637; IMAGE at p20 y=638–759.
    "exhibit-13-10": [(20, fitz.Rect(48, 621, 550, 765))],
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
