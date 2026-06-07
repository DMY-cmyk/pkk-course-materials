# RMK Ch. 13 Visuals Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Insert 11 visuals (6 exhibits cropped from the Sage Ch. 13 PDF + 5 generated monochrome diagrams) into the Kelompok 2 RMK docx via the existing markdown→docx pipeline.

**Architecture:** Two committed asset scripts produce PNGs into `assets/` (PyMuPDF crops; matplotlib diagrams). The markdown grammar gains one construct — a full-line image directive — parsed by `parse_blocks` into an `("image", (caption, path))` block and rendered by `build_docx.py` as a centered 14.5 cm picture with a two-line caption. Image lines are inserted into `content/rmk-ch13.md` per the spec's placement map.

**Tech Stack:** Python 3, pymupdf (`fitz`) 1.27, matplotlib 3.10, Pillow, python-docx, pytest.

**Spec:** `docs/superpowers/specs/2026-06-07-rmk-ch13-visuals-design.md` (approved 2026-06-07)

---

## Verified environment facts

- pymupdf 1.27.1, matplotlib 3.10.8, pillow 12.1.1 all importable with the system `python`.
- Source PDF (READ-ONLY): `Kelompok 2 Pasca UTS/Sage Chapter 13.pdf` — 23 pages. PDF page N = fitz page index N−1.
- Exhibit locations (from `Kelompok 2 Pasca UTS/analysis/chapter-deep-read.md`): 13.2 → PDF pp. 7–8 (spans two pages), 13.3 → p. 8 (may extend to 9), 13.4 → p. 10, 13.5 → p. 13, 13.6 → p. 16, 13.9 → p. 20.
- Current pipeline (all tests green, docx builds): `Kelompok 2 Pasca UTS/content/rmk-ch13.md` → `Kelompok 2 Pasca UTS/output/build_docx.py` → `Kelompok 2 Pasca UTS/output/Kelompok 2_RMK Chapter 13 Statement of Cash Flows.docx`.

## File structure

```
Kelompok 2 Pasca UTS/
├── assets/
│   ├── crop_exhibits.py        # Task 2 — PDF → exhibit PNGs (300 DPI)
│   ├── make_diagrams.py        # Task 3 — matplotlib → diagram PNGs (300 DPI, grayscale)
│   ├── exhibit-13-2.png … exhibit-13-9.png   (6 files)
│   └── diagram-*.png           (5 files)
├── content/rmk-ch13.md         # Task 4 — +11 image lines (prose otherwise untouched)
└── output/
    ├── build_docx.py           # Task 1 — +image parsing & rendering
    └── test_build_docx.py      # Task 1 — +4 tests (total 9)
```

Do NOT `git add` the source PDFs/JPEG. Commit scripts AND generated PNGs (deliverable must build without re-cropping).

---

### Task 1: Image directive — parser + renderer (TDD)

**Files:**
- Modify: `Kelompok 2 Pasca UTS/output/test_build_docx.py` (append tests)
- Modify: `Kelompok 2 Pasca UTS/output/build_docx.py`

- [ ] **Step 1: Append failing tests**

Append to `Kelompok 2 Pasca UTS/output/test_build_docx.py`:

```python
from build_docx import split_caption


def test_image_block():
    md = "![Gambar 1. Judul Diagram | Sumber: Wolk (2017)](../assets/x.png)\n"
    assert parse_blocks(md) == [
        ("image", ("Gambar 1. Judul Diagram | Sumber: Wolk (2017)", "../assets/x.png")),
    ]


def test_image_block_between_paragraphs():
    md = "Paragraf satu.\n\n![Gambar 2. Judul](../assets/y.png)\n\nParagraf dua.\n"
    assert parse_blocks(md) == [
        ("para", "Paragraf satu."),
        ("image", ("Gambar 2. Judul", "../assets/y.png")),
        ("para", "Paragraf dua."),
    ]


def test_split_caption_with_source():
    assert split_caption("Gambar 1. Judul | Sumber: Wolk (2017)") == (
        "Gambar 1. Judul", "Sumber: Wolk (2017)")


def test_split_caption_without_source():
    assert split_caption("Gambar 2. Judul saja") == ("Gambar 2. Judul saja", None)
```

- [ ] **Step 2: Run tests — verify the 4 new ones fail**

Run: `python -m pytest "Kelompok 2 Pasca UTS/output/test_build_docx.py" -v`
Expected: 5 passed, 4 failed/errored (ImportError on `split_caption`, then assertion failures).

- [ ] **Step 3: Implement parser changes in `build_docx.py`**

(a) Add near the other parsing functions:

```python
IMAGE_RE = re.compile(r'^!\[(.+?)\]\((.+?)\)$')


def split_caption(caption):
    """Split 'Title | Sumber: ...' into (title, source). Source is None if absent."""
    if " | " in caption:
        title, source = caption.split(" | ", 1)
        return title.strip(), source.strip()
    return caption.strip(), None
```

(b) In `parse_blocks`, add an image branch BEFORE the bullet branch (an image line is a full-line construct):

```python
        elif line.startswith("!["):
            m = IMAGE_RE.match(line.strip())
            if m:
                flush()
                blocks.append(("image", (m.group(1), m.group(2))))
            else:
                buf.append(line.strip())
```

(The `else: buf.append(...)` fallback keeps a malformed image line visible as text rather than silently dropping it.)

- [ ] **Step 4: Implement renderer changes in `build_docx.py`**

(a) Add `RGBColor` import is NOT needed; add this renderer helper after `add_blank`:

```python
def add_image_with_caption(doc, img_path, caption):
    """Insert a centered picture (14.5 cm wide) + 2-line caption below."""
    doc.add_picture(img_path, width=Cm(14.5))
    pic_para = doc.paragraphs[-1]
    pic_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic_para.paragraph_format.space_before = Pt(6)
    pic_para.paragraph_format.space_after = Pt(6)

    title, source = split_caption(caption)
    m = re.match(r'^(Gambar \d+\.)\s*(.*)$', title)
    if m:
        runs = [(m.group(1) + " ", True, False), (m.group(2), False, False)]
    else:
        runs = [(title, False, False)]
    _add_para(doc, runs, font_size=11,
              alignment=WD_ALIGN_PARAGRAPH.CENTER,
              space_before_pt=0, space_after_pt=0 if source else 12)
    if source:
        _add_para(doc, [(source, False, True)], font_size=11,
                  alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before_pt=0, space_after_pt=12)
```

(b) In `build()`, the content loop currently starts with `for kind, text in parse_blocks(md_text):` and immediately calls `parse_inline_runs(text)`. Restructure so image blocks are handled first (their payload is a tuple, not text):

```python
    for kind, text in parse_blocks(md_text):
        if kind == "image":
            caption, rel_path = text
            img_path = os.path.normpath(os.path.join(here, "..", "content", rel_path))
            add_image_with_caption(doc, img_path, caption)
            continue
        runs = parse_inline_runs(text)
        if kind == "heading":
            ...  # (existing branches unchanged)
```

- [ ] **Step 5: Run tests — all 9 pass**

Run: `python -m pytest "Kelompok 2 Pasca UTS/output/test_build_docx.py" -v`
Expected: **9 passed**.

- [ ] **Step 6: Regression-build (no image lines exist yet in the md — output must be unchanged in content)**

Run: `python "Kelompok 2 Pasca UTS/output/build_docx.py"`
Expected: `Saved:` + size ≈ 59 KB (same as before within a few bytes).

- [ ] **Step 7: Commit**

```powershell
git add "Kelompok 2 Pasca UTS/output/build_docx.py" "Kelompok 2 Pasca UTS/output/test_build_docx.py"
git commit -m "feat(k2-rmk): image directive in markdown-to-docx pipeline (parser + renderer, TDD)"
```

### Task 2: Crop the 6 exhibits — `assets/crop_exhibits.py`

**Files:**
- Create: `Kelompok 2 Pasca UTS/assets/crop_exhibits.py`
- Create (generated): `Kelompok 2 Pasca UTS/assets/exhibit-13-{2,3,4,5,6,9}.png`
- Read-only input: `Kelompok 2 Pasca UTS/Sage Chapter 13.pdf`

This task is iterative: rectangles cannot be known in advance. The script has two modes — `--pages` renders full pages for inspection; default mode crops.

- [ ] **Step 1: Write the script skeleton with survey mode**

Create `Kelompok 2 Pasca UTS/assets/crop_exhibits.py`:

```python
"""
crop_exhibits.py
Crops Exhibits 13.2/13.3/13.4/13.5/13.6/13.9 from "Sage Chapter 13.pdf"
into 300-DPI PNGs for the RMK docx.

Usage:
  python crop_exhibits.py --pages    # render full pages 7,8,9,10,13,16,20 to tmp/ for inspection
  python crop_exhibits.py            # crop using the EXHIBITS table below
"""

import os
import sys

import fitz  # pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, "..", "Sage Chapter 13.pdf")
ZOOM = 300 / 72  # 300 DPI
MAT = fitz.Matrix(ZOOM, ZOOM)

SURVEY_PAGES = [7, 8, 9, 10, 13, 16, 20]  # PDF page numbers (1-based)

# name -> list of (pdf_page_1based, fitz.Rect in PDF points).
# Multiple entries are stitched vertically (for Exhibit 13.2 spanning pp. 7-8).
# RECTANGLES BELOW ARE PLACEHOLDER FULL-PAGE VALUES ON PURPOSE:
# step 2 of the task replaces them with measured values after viewing the
# survey renders. Do not commit until crops are visually verified.
EXHIBITS = {
    "exhibit-13-2": [(7, fitz.Rect(0, 0, 612, 792)), (8, fitz.Rect(0, 0, 612, 792))],
    "exhibit-13-3": [(8, fitz.Rect(0, 0, 612, 792))],
    "exhibit-13-4": [(10, fitz.Rect(0, 0, 612, 792))],
    "exhibit-13-5": [(13, fitz.Rect(0, 0, 612, 792))],
    "exhibit-13-6": [(16, fitz.Rect(0, 0, 612, 792))],
    "exhibit-13-9": [(20, fitz.Rect(0, 0, 612, 792))],
}


def render_clip(doc, page_1based, rect):
    page = doc[page_1based - 1]
    pix = page.get_pixmap(matrix=MAT, clip=rect)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def survey(doc):
    out_dir = os.path.join(HERE, "tmp")
    os.makedirs(out_dir, exist_ok=True)
    for p in SURVEY_PAGES:
        page = doc[p - 1]
        img = render_clip(doc, p, page.rect)
        path = os.path.join(out_dir, f"page-{p:02d}.png")
        img.save(path)
        print(f"page {p}: {page.rect}  -> {path}")


def crop(doc):
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
        out = os.path.join(HERE, f"{name}.png")
        combined.save(out)
        print(f"{name}: {combined.width}x{combined.height} -> {out}")


if __name__ == "__main__":
    document = fitz.open(PDF)
    if "--pages" in sys.argv:
        survey(document)
    else:
        crop(document)
```

- [ ] **Step 2: Survey — render and inspect pages**

Run: `python "Kelompok 2 Pasca UTS/assets/crop_exhibits.py" --pages`
Then use the **Read tool on each `assets/tmp/page-NN.png`** to view it. For each exhibit, note the bounding box of the exhibit (header line "Exhibit 13.x ..." through the last row) in PDF points: the printed `page.rect` gives full-page dimensions; estimate the clip rect proportionally from what you see (e.g., exhibit occupying the top 60% of a 612×792 page ≈ `fitz.Rect(50, 60, 562, 535)`). Record a rect per exhibit (two for 13.2 if it truly spans pages 7–8 — confirm from the renders where it starts and ends; if the whole exhibit sits on one page, use a single entry).

- [ ] **Step 3: Set rectangles, crop, inspect, iterate**

Edit `EXHIBITS` with the measured rects. Run: `python "Kelompok 2 Pasca UTS/assets/crop_exhibits.py"`
View each `assets/exhibit-*.png` with the Read tool. Acceptance per crop: entire exhibit including its "Exhibit 13.x" header line; no surrounding body text; no cut rows/columns; white margins ≤ ~20 px. Adjust rects and re-run until all 6 pass. Delete `assets/tmp/` when done:

```powershell
Remove-Item -Recurse -Force "Kelompok 2 Pasca UTS/assets/tmp"
```

- [ ] **Step 4: Commit**

```powershell
git add "Kelompok 2 Pasca UTS/assets/crop_exhibits.py" "Kelompok 2 Pasca UTS/assets/exhibit-13-2.png" "Kelompok 2 Pasca UTS/assets/exhibit-13-3.png" "Kelompok 2 Pasca UTS/assets/exhibit-13-4.png" "Kelompok 2 Pasca UTS/assets/exhibit-13-5.png" "Kelompok 2 Pasca UTS/assets/exhibit-13-6.png" "Kelompok 2 Pasca UTS/assets/exhibit-13-9.png"
git commit -m "feat(k2-rmk): crop 6 chapter exhibits to assets (300 DPI)"
```

### Task 3: Generate the 5 diagrams — `assets/make_diagrams.py`

**Files:**
- Create: `Kelompok 2 Pasca UTS/assets/make_diagrams.py`
- Create (generated): `diagram-timeline.png`, `diagram-trichotomy.png`, `diagram-nonarticulation.png`, `diagram-fcf-waterfall.png`, `diagram-four-measures.png`
- Reference (numbers): `Kelompok 2 Pasca UTS/analysis/chapter-deep-read.md`

- [ ] **Step 1: Verify the FCF-bridge component numbers from the notes**

Open `analysis/chapter-deep-read.md`, section S9, Exhibit 13.10 entry. The bridge for 2005 must satisfy: CFO + after-tax interest − increase in operating cash + CFI = FCF. Expected from notes: CFO 527, after-tax interest 26, change in operating cash −56 (operating cash DECREASED, so the "− increase" term contributes +56), CFI −277, FCF 332 (sanity: 527+26+56−277 = 332). If the notes give different component values, use the notes' values in the waterfall code below and adjust the assert.

- [ ] **Step 2: Write the script**

Create `Kelompok 2 Pasca UTS/assets/make_diagrams.py`:

```python
"""
make_diagrams.py
Generates the 5 monochrome diagrams for the RMK docx (300 DPI PNGs).
All figures/dates sourced from analysis/chapter-deep-read.md - no invented data.
Style: grayscale only, serif, print-safe (spec: Akademik Monokrom).
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})

DARK, MID, LIGHT, PALE = "#1a1a1a", "#4d4d4d", "#8c8c8c", "#d9d9d9"


def save(fig, name):
    out = os.path.join(HERE, name)
    fig.savefig(out)
    plt.close(fig)
    print("saved", out)


def box(ax, x, y, w, h, text, fc, tc="white", fontsize=10, style="round,pad=0.02", ec=DARK, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style,
                                facecolor=fc, edgecolor=ec, linestyle=ls, linewidth=1))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color=tc, wrap=True)


def timeline():
    events = [
        ("1963", "APB Opinion No. 3\nSCFP direkomendasikan", DARK),
        ("1971", "SEC mewajibkan;\nAPB Opinion No. 19 (SCFP)", MID),
        ("1987", "SFAS No. 95\nStatement of Cash Flows", LIGHT),
        ("2008", "Discussion paper FASB-IASB\nklasifikasi “business”", "white"),
    ]
    fig, ax = plt.subplots(figsize=(9, 2.6))
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.plot([0.4, 9.6], [1.0, 1.0], color=MID, linewidth=2, zorder=1)
    xs = [1.2, 3.6, 6.0, 8.4]
    for (year, label, shade), x in zip(events, xs):
        dashed = shade == "white"
        ax.plot([x], [1.0], "o", color=DARK, markersize=7, zorder=3)
        box(ax, x - 1.0, 1.45, 2.0, 1.1, label, fc=shade if not dashed else "white",
            tc="white" if not dashed else DARK, fontsize=8.5,
            ls="--" if dashed else "-")
        ax.text(x, 0.55, year, ha="center", va="center", fontsize=11,
                fontweight="bold", color=DARK)
    save(fig, "diagram-timeline.png")


def trichotomy():
    fig, ax = plt.subplots(figsize=(9, 3.6))
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    cols = [
        (0.4, "AKTIVITAS\nOPERASI", DARK,
         "kas dari pelanggan\nkas ke pemasok/karyawan\npajak penghasilan\nbunga & dividen diterima*\nbunga dibayar*"),
        (4.2, "AKTIVITAS\nINVESTASI", MID,
         "pembelian/penjualan\naset jangka panjang\ninvestasi sekuritas\npinjaman kepada\npihak lain"),
        (8.0, "AKTIVITAS\nPENDANAAN", LIGHT,
         "penerbitan/pelunasan\nutang\npenerbitan saham\npembelian saham treasuri\npembayaran dividen"),
    ]
    for x, title, shade, items in cols:
        box(ax, x, 4.3, 3.4, 1.2, title, fc=shade, fontsize=10.5)
        box(ax, x, 0.9, 3.4, 3.1, items, fc="white", tc=DARK, fontsize=8.5, ec=MID)
    ax.text(6.0, 0.25,
            "* Klasifikasi yang diperdebatkan: tiga anggota FASB berpendapat bunga/dividen diterima = investasi (par. 22)\n"
            "dan bunga dibayar = pendanaan (par. 23) — SFAS No. 95 menempatkan keduanya di aktivitas operasi.",
            ha="center", va="center", fontsize=8, style="italic", color=DARK)
    save(fig, "diagram-trichotomy.png")


def nonarticulation():
    fig, ax = plt.subplots(figsize=(9, 3.8))
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.4)
    causes = [
        "Akuisisi anak perusahaan\ndi tengah tahun fiskal",
        "Transaksi modal kerja\nyang tidak memengaruhi kas\n(write-up/down, reklasifikasi)",
        "Satu akun utang usaha\nuntuk pos modal kerja\ndan non-modal kerja",
    ]
    for i, c in enumerate(causes):
        box(ax, 0.3, 4.6 - i * 2.0, 4.2, 1.5, c, fc="white", tc=DARK, fontsize=8.5, ec=MID)
        ax.add_patch(FancyArrowPatch((4.6, 5.35 - i * 2.0), (6.0, 3.4),
                                     arrowstyle="-|>", mutation_scale=14, color=MID))
    box(ax, 6.1, 2.55, 3.0, 1.7,
        "NONARTIKULASI\nΔ akun neraca ≠\npenyesuaian SCF\n(metode tidak langsung)", fc=DARK, fontsize=9)
    ax.add_patch(FancyArrowPatch((9.2, 3.4), (10.0, 3.4),
                                 arrowstyle="-|>", mutation_scale=14, color=MID))
    box(ax, 10.0, 2.35, 1.85, 2.1,
        "Angka SCF tidak dapat\nditelusuri ke neraca;\nterjadi pada ±75%\nperusahaan (Bahnson,\nMiller & Budge)",
        fc="white", tc=DARK, fontsize=7.5, ec=DARK)
    save(fig, "diagram-nonarticulation.png")


def fcf_waterfall():
    # ABC Company 2005, Exhibit 13.10 bridge (verify against notes before running):
    # CFO 527 + after-tax interest 26 - increase in operating cash (-56 -> +56) + CFI (-277) = FCF 332
    labels = ["CFO", "+ Bunga\nsetelah pajak", "− Kenaikan\nkas operasi", "+ CFI", "FCF"]
    deltas = [527, 26, 56, -277, None]
    assert 527 + 26 + 56 - 277 == 332
    fig, ax = plt.subplots(figsize=(8.5, 3.6))
    cum = 0
    shades = [MID, LIGHT, LIGHT, LIGHT, DARK]
    for i, (lab, d) in enumerate(zip(labels, deltas)):
        if d is None:  # final bar
            ax.bar(i, 332, bottom=0, color=shades[i], edgecolor=DARK)
            ax.text(i, 332 + 12, "$332", ha="center", fontsize=10, fontweight="bold", color=DARK)
        else:
            bottom = cum if d >= 0 else cum + d
            ax.bar(i, abs(d), bottom=bottom, color=shades[i], edgecolor=DARK)
            ax.text(i, cum + (d if d >= 0 else 0) + 12,
                    f"${d:+,}".replace("+", "+") if i else f"${d:,}",
                    ha="center", fontsize=10, color=DARK)
            cum += d
            ax.plot([i + 0.4, i + 0.6], [cum, cum], color=MID, linewidth=1)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("juta dolar AS", fontsize=9)
    ax.set_title("Jembatan CFO → FCF, ABC Company 2005", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "diagram-fcf-waterfall.png")


def four_measures():
    years = ["2005", "2006", "2007"]
    series = [
        ("Laba bersih", [320, 312, 331], DARK, ""),
        ("CFO", [527, 466, 434], MID, ""),
        ("CFO − CFI", [250, 157, 74], LIGHT, ""),
        ("FCF", [332, 99, 80], PALE, "//"),
    ]
    fig, ax = plt.subplots(figsize=(8.5, 3.6))
    w = 0.19
    for i, (name, vals, shade, hatch) in enumerate(series):
        xs = [j + (i - 1.5) * w for j in range(3)]
        ax.bar(xs, vals, width=w, label=name, color=shade,
               edgecolor=DARK, hatch=hatch)
    ax.set_xticks(range(3))
    ax.set_xticklabels(years)
    ax.set_ylabel("juta dolar AS", fontsize=9)
    ax.set_title("Empat ukuran kinerja ABC Company, 2005–2007", fontsize=11)
    ax.legend(fontsize=8, frameon=False, ncols=4, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "diagram-four-measures.png")


if __name__ == "__main__":
    timeline()
    trichotomy()
    nonarticulation()
    fcf_waterfall()
    four_measures()
```

- [ ] **Step 3: Run and inspect**

Run: `python "Kelompok 2 Pasca UTS/assets/make_diagrams.py"`
Expected: 5 `saved ...` lines. View each PNG with the Read tool. Acceptance: text legible, nothing clipped/overlapping, grayscale only, every number/date matches `chapter-deep-read.md` (timeline dates 1963/1971/1987/2008; trichotomy dissent pars. 22/23; nonarticulation three causes + 75% Bahnson/Miller/Budge; waterfall components & 332; four measures NI 320/312/331, CFO 527/466/434, CFO−CFI 250/157/74, FCF 332/99/80). Fix layout/sizes and re-run as needed.

- [ ] **Step 4: Commit**

```powershell
git add "Kelompok 2 Pasca UTS/assets/make_diagrams.py" "Kelompok 2 Pasca UTS/assets/diagram-timeline.png" "Kelompok 2 Pasca UTS/assets/diagram-trichotomy.png" "Kelompok 2 Pasca UTS/assets/diagram-nonarticulation.png" "Kelompok 2 Pasca UTS/assets/diagram-fcf-waterfall.png" "Kelompok 2 Pasca UTS/assets/diagram-four-measures.png"
git commit -m "feat(k2-rmk): generate 5 monochrome diagrams for RMK"
```

### Task 4: Insert the 11 image lines into the RMK markdown

**Files:**
- Modify: `Kelompok 2 Pasca UTS/content/rmk-ch13.md` (insert 11 standalone lines; NO prose changes)

- [ ] **Step 1: Insert each image line after its anchor paragraph**

Each line goes on its own line, blank lines before and after, immediately AFTER the paragraph found by the anchor search string. Read the file first; anchors are unique substrings of the target paragraph.

| # | Anchor (paragraph contains) | Exact line to insert |
|---|---|---|
| 1 | `APB Opinion No. 3` | `![Gambar 1. Lini masa evolusi pelaporan aliran dana, 1963–2008 \| Sumber: diolah dari Wolk, Dodd & Rozycki (2017), PDF hlm. 4, 10–11](../assets/diagram-timeline.png)` |
| 2 | `paragraf 23 Statement 95` | `![Gambar 2. Trikotomi aktivitas SFAS No. 95 dan pos-pos yang diperdebatkan \| Sumber: diolah dari Wolk, Dodd & Rozycki (2017), PDF hlm. 7](../assets/diagram-trichotomy.png)` |
| 3 | first paragraph containing `Exhibit 13.2` | `![Gambar 3. SCF metode langsung — Company M (Exhibit 13.2) \| Sumber: Wolk, Dodd & Rozycki (2017), Exhibit 13.2, PDF hlm. 7–8](../assets/exhibit-13-2.png)` |
| 4 | first paragraph containing `Exhibit 13.3` | `![Gambar 4. Rekonsiliasi metode tidak langsung — Company M (Exhibit 13.3) \| Sumber: Wolk, Dodd & Rozycki (2017), Exhibit 13.3, PDF hlm. 8](../assets/exhibit-13-3.png)` |
| 5 | first paragraph containing `Exhibit 13.4` | `![Gambar 5. Nonartikulasi pada 3M Company (Exhibit 13.4) \| Sumber: Wolk, Dodd & Rozycki (2017), Exhibit 13.4, PDF hlm. 10](../assets/exhibit-13-4.png)` |
| 6 | the paragraph listing the three causes (contains `akuisisi` and `utang usaha`) | `![Gambar 6. Tiga penyebab nonartikulasi dan konsekuensinya \| Sumber: diolah dari Wolk, Dodd & Rozycki (2017), PDF hlm. 9–10](../assets/diagram-nonarticulation.png)` |
| 7 | `Metode 4` | `![Gambar 7. Empat metode alokasi premi obligasi (Exhibit 13.5) \| Sumber: Wolk, Dodd & Rozycki (2017), Exhibit 13.5, PDF hlm. 13](../assets/exhibit-13-5.png)` |
| 8 | `WorldCom` (the paragraph with the $12 billion / $(12.313) discussion) | `![Gambar 8. Kinerja dan arus kas WorldCom (Exhibit 13.6) \| Sumber: Wolk, Dodd & Rozycki (2017), Exhibit 13.6, PDF hlm. 16](../assets/exhibit-13-6.png)` |
| 9 | first paragraph containing `Exhibit 13.9` | `![Gambar 9. Konstruksi free cash flow ABC Company (Exhibit 13.9) \| Sumber: Wolk, Dodd & Rozycki (2017), Exhibit 13.9, PDF hlm. 20](../assets/exhibit-13-9.png)` |
| 10 | the bridge paragraph (contains `Exhibit 13.10` or `jembatan`) | `![Gambar 10. Jembatan CFO menuju FCF, ABC Company 2005 \| Sumber: diolah dari Wolk, Dodd & Rozycki (2017), Exhibit 13.10, PDF hlm. 20](../assets/diagram-fcf-waterfall.png)` |
| 11 | the four-measures paragraph (contains `$320/312/331` or `empat ukuran`) | `![Gambar 11. Perbandingan empat ukuran kinerja ABC Company \| Sumber: diolah dari Wolk, Dodd & Rozycki (2017), Exhibit 13.11, PDF hlm. 18, 21](../assets/diagram-four-measures.png)` |

NOTE: the `\|` in the table above is markdown-escaping for THIS plan file only — the actual inserted lines use a plain `|` (e.g. `![Gambar 1. ... | Sumber: ...](...)`).

Verify document order = numbering order (Gambar 1 appears before Gambar 2, etc.). If an anchor matches in the wrong section, prefer the occurrence in the section listed in the spec's placement map (II, IV, V, V, VI, VI, VII, VIII, IX, IX, IX).

- [ ] **Step 2: Verify insertion count and order**

```powershell
(Select-String -Path "Kelompok 2 Pasca UTS/content/rmk-ch13.md" -Pattern '^!\[Gambar' -Encoding UTF8).Count
```
Expected: **11**. Also confirm the Gambar numbers appear in ascending order top-to-bottom (read the matches).

- [ ] **Step 3: Rebuild**

Run: `python -m pytest "Kelompok 2 Pasca UTS/output/test_build_docx.py" -q` → 9 passed.
Run: `python "Kelompok 2 Pasca UTS/output/build_docx.py"` → Saved; size now ≫ 59 KB (images embedded; expect 1–4 MB).

- [ ] **Step 4: Commit**

```powershell
git add "Kelompok 2 Pasca UTS/content/rmk-ch13.md" "Kelompok 2 Pasca UTS/output/Kelompok 2_RMK Chapter 13 Statement of Cash Flows.docx"
git commit -m "feat(k2-rmk): place 11 visuals in RMK per placement map"
```

### Task 5: Docx integrity verification

**Files:** none new (verification only; fixes loop back to earlier tasks)

- [ ] **Step 1: Programmatic integrity check**

```powershell
python -c "
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx import Document
d = Document(r'Kelompok 2 Pasca UTS\output\Kelompok 2_RMK Chapter 13 Statement of Cash Flows.docx')
print('inline images:', len(d.inline_shapes))
caps = [p.text for p in d.paragraphs if re.match(r'^Gambar \d+\.', p.text)]
print('captions:', len(caps))
nums = [int(re.match(r'^Gambar (\d+)\.', t).group(1)) for t in caps]
print('numbering ok:', nums == list(range(1, 12)))
leak = [p.text[:60] for p in d.paragraphs if '![' in p.text]
print('leaked image syntax:', leak)
"
```
Expected: `inline images: 11`, `captions: 11`, `numbering ok: True`, `leaked image syntax: []`.

- [ ] **Step 2: Visual sanity of the rendered document**

Convert nothing — instead spot-open the docx with python-docx and confirm each caption is preceded by an image (inline shape order matches captions). Simpler accepted check: the Step 1 output passes AND each `exhibit-*.png`/`diagram-*.png` was already visually accepted in Tasks 2–3. Then ask the user to open the docx in Word for the final visual check (image sizes, page flow).

- [ ] **Step 3: Final commit (only if fixes were applied)**

```powershell
git status --short "Kelompok 2 Pasca UTS/"
```
If anything is modified: add + commit with `fix(k2-rmk): integrity fixes for visuals`.

Report to user: deliverable path, image count, file size, and request the Word visual check.
