# Word Document — Academic Report Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate a 40–60 page Academic Report Word document (.docx) summarizing the 32-slide FASB CF × INDF 2024 presentation in Bahasa Indonesia, with Times New Roman typography, 23 embedded visuals, and a formal cover page.

**Architecture:** A Python entry-point (`scripts/generate_word_doc.py`) orchestrates module-based builders. The `word_doc/` package contains: `styles.py` (all font/paragraph helpers), `visuals.py` (12 matplotlib PNG generators), `cover.py`, `front_matter.py`, eight section modules (`sections/bagian_i.py` … `bagian_viii.py`), and `bibliography.py`. Each module exposes one public function that accepts a `Document` object and mutates it.

**Tech Stack:** Python 3.12, python-docx ≥ 1.1.0, matplotlib ≥ 3.8.0, Pillow ≥ 10.0.0, pytest ≥ 7.0.0

**Spec:** `docs/superpowers/specs/2026-04-24-word-document-design.md`

---

### Task 1: Scaffold — directory structure, stubs, requirements

**Files:**
- Create: `requirements.txt`
- Create: `scripts/__init__.py`
- Create: `scripts/word_doc/__init__.py`
- Create: `scripts/word_doc/styles.py` (stub)
- Create: `scripts/word_doc/visuals.py` (stub)
- Create: `scripts/word_doc/cover.py` (stub)
- Create: `scripts/word_doc/front_matter.py` (stub)
- Create: `scripts/word_doc/bibliography.py` (stub)
- Create: `scripts/word_doc/sections/__init__.py`
- Create: `scripts/word_doc/sections/bagian_i.py` (stub)
- Create: `scripts/word_doc/sections/bagian_ii.py` (stub)
- Create: `scripts/word_doc/sections/bagian_iii.py` (stub)
- Create: `scripts/word_doc/sections/bagian_iv.py` (stub)
- Create: `scripts/word_doc/sections/bagian_v.py` (stub)
- Create: `scripts/word_doc/sections/bagian_vi.py` (stub)
- Create: `scripts/word_doc/sections/bagian_vii.py` (stub)
- Create: `scripts/word_doc/sections/bagian_viii.py` (stub)
- Create: `scripts/generate_word_doc.py` (stub)
- Create: `tests/__init__.py`
- Create: `tests/test_word_doc.py`

- [ ] **Step 1.1: Create `requirements.txt`**

```
python-docx>=1.1.0
matplotlib>=3.8.0
Pillow>=10.0.0
pytest>=7.0.0
```

- [ ] **Step 1.2: Install dependencies**

Run from project root:
```
pip install -r requirements.txt
```
Expected: all four packages install successfully.

- [ ] **Step 1.3: Create directory structure**

```
mkdir -p scripts/word_doc/sections tests
```

- [ ] **Step 1.4: Create empty `__init__.py` files**

`scripts/__init__.py` — empty  
`scripts/word_doc/__init__.py` — empty  
`scripts/word_doc/sections/__init__.py` — empty  
`tests/__init__.py` — empty  

- [ ] **Step 1.5: Create stub modules** (each file contains only a pass-level stub so imports succeed)

`scripts/word_doc/styles.py`:
```python
# styles — implemented in Task 2
```

`scripts/word_doc/visuals.py`:
```python
# visuals — implemented in Task 3
```

`scripts/word_doc/cover.py`:
```python
# cover — implemented in Task 4
```

`scripts/word_doc/front_matter.py`:
```python
# front_matter — implemented in Task 5
```

`scripts/word_doc/bibliography.py`:
```python
# bibliography — implemented in Task 14
```

`scripts/word_doc/sections/bagian_i.py` through `bagian_viii.py`:
```python
# bagian_X — implemented in Task 6–13
def build(doc):
    pass
```

`scripts/generate_word_doc.py`:
```python
# entry point — implemented in Task 15
```

- [ ] **Step 1.6: Write import test**

`tests/test_word_doc.py`:
```python
import pytest


def test_all_modules_import():
    from scripts.word_doc import styles, visuals, cover, front_matter, bibliography
    from scripts.word_doc.sections import (
        bagian_i, bagian_ii, bagian_iii, bagian_iv,
        bagian_v, bagian_vi, bagian_vii, bagian_viii,
    )
```

- [ ] **Step 1.7: Run test**

```
pytest tests/test_word_doc.py::test_all_modules_import -v
```
Expected: PASSED

- [ ] **Step 1.8: Commit**

```
git add requirements.txt scripts/ tests/
git commit -m "feat(word-doc): scaffold module structure and stubs"
```

---

### Task 2: `styles.py` — all formatting helpers

**Files:**
- Modify: `scripts/word_doc/styles.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 2.1: Write failing tests**

Append to `tests/test_word_doc.py`:
```python
from docx import Document


def test_set_run_font_sets_times_new_roman():
    from scripts.word_doc.styles import set_run_font
    doc = Document()
    p = doc.add_paragraph()
    run = p.add_run("test")
    set_run_font(run, size_pt=12)
    assert run.font.name == "Times New Roman"
    assert run.font.size.pt == 12
    assert run.font.bold is None or run.font.bold is False


def test_add_section_heading_is_14pt_bold():
    from scripts.word_doc.styles import add_section_heading
    doc = Document()
    p = add_section_heading(doc, "I. TEST HEADING")
    run = p.runs[0]
    assert run.font.bold is True
    assert run.font.size.pt == 14


def test_add_body_paragraph_is_12pt():
    from scripts.word_doc.styles import add_body_paragraph
    doc = Document()
    p = add_body_paragraph(doc, "Some text here.")
    run = p.runs[0]
    assert run.font.size.pt == 12
    assert run.font.bold is None or run.font.bold is False


def test_add_table_with_headers_shape():
    from scripts.word_doc.styles import add_table_with_headers
    doc = Document()
    headers = ["Kolom A", "Kolom B", "Kolom C"]
    rows = [["a1", "b1", "c1"], ["a2", "b2", "c2"]]
    table = add_table_with_headers(doc, headers, rows)
    assert len(table.rows) == 3   # 1 header + 2 data
    assert len(table.columns) == 3
```

- [ ] **Step 2.2: Run tests (expect failures)**

```
pytest tests/test_word_doc.py -k "test_set_run_font or test_add_section or test_add_body or test_add_table" -v
```
Expected: 4 FAILED (ImportError or AttributeError)

- [ ] **Step 2.3: Implement `scripts/word_doc/styles.py`**

```python
import io
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


# ── Font helper ────────────────────────────────────────────────────────────────

def set_run_font(run, size_pt, bold=False, italic=False,
                 color_rgb=(0, 0, 0)):
    run.font.name = "Times New Roman"
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)
    # Suppress theme-font override so TNR is actually used
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Times New Roman")
    rFonts.set(qn("w:hAnsi"), "Times New Roman")
    run._r.get_or_add_rPr().append(rFonts)


# ── Paragraph borders ──────────────────────────────────────────────────────────

def _add_para_border(paragraph, sides, sz="6", color="000000"):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    for side in sides:
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), sz)
        el.set(qn("w:space"), "1")
        el.set(qn("w:color"), color)
        pBdr.append(el)
    pPr.append(pBdr)


# ── Typography hierarchy ───────────────────────────────────────────────────────

def add_doc_title(doc, text):
    """16pt Bold, centered — for cover page."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    set_run_font(run, 16, bold=True)
    return p


def add_section_heading(doc, text):
    """14pt Bold + bottom border, for numbered sections I, II, …"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(20)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run(text)
    set_run_font(run, 14, bold=True)
    _add_para_border(p, ["bottom"], sz="6", color="000000")
    return p


def add_sub_heading(doc, text):
    """12pt Bold, for sub-sections 1.1, 1.2, …"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    set_run_font(run, 12, bold=True)
    return p


def add_body_paragraph(doc, text):
    """12pt Regular, justify, 1.5 line spacing."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = Pt(18)   # 12pt × 1.5
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run(text)
    set_run_font(run, 12)
    return p


def add_caption(doc, text):
    """10pt Italic, centered — for tables and figures."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(10)
    run = p.add_run(text)
    set_run_font(run, 10, italic=True)
    return p


def add_footnote_text(doc, text):
    """10pt Regular with top border — for section footnotes."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    run = p.add_run(text)
    set_run_font(run, 10)
    _add_para_border(p, ["top"], sz="4", color="999999")
    return p


def add_page_break(doc):
    p = doc.add_paragraph()
    from docx.enum.text import WD_BREAK
    p.add_run().add_break(WD_BREAK.PAGE)
    return p


# ── Table helper ───────────────────────────────────────────────────────────────

def _set_cell_shading(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill_hex)
    tcPr.append(shd)


def add_table_with_headers(doc, headers, rows_data):
    """
    Build a Word table with black header row (white bold text) and
    alternating gray rows. All fonts are 11pt TNR.

    headers   : list[str]
    rows_data : list[list[str]]
    Returns   : docx.table.Table
    """
    n_cols = len(headers)
    n_rows = len(rows_data)
    table = doc.add_table(rows=1 + n_rows, cols=n_cols)
    table.style = "Table Grid"

    # Header row
    hdr_cells = table.rows[0].cells
    for i, hdr_text in enumerate(headers):
        cell = hdr_cells[i]
        cell.paragraphs[0].clear()
        run = cell.paragraphs[0].add_run(hdr_text)
        set_run_font(run, 11, bold=True, color_rgb=(255, 255, 255))
        _set_cell_shading(cell, "000000")

    # Data rows
    for row_idx, row_data in enumerate(rows_data):
        fill = "F5F5F5" if row_idx % 2 == 1 else "FFFFFF"
        cells = table.rows[row_idx + 1].cells
        for j, cell_text in enumerate(row_data):
            cell = cells[j]
            cell.paragraphs[0].clear()
            run = cell.paragraphs[0].add_run(cell_text)
            set_run_font(run, 11)
            if fill != "FFFFFF":
                _set_cell_shading(cell, fill)

    return table


# ── Document setup ─────────────────────────────────────────────────────────────

def setup_document(doc):
    """Apply A4 page size, 2.5 cm margins."""
    section = doc.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)


def add_page_numbers(doc):
    """Insert centered page number field in the footer."""
    section = doc.sections[0]
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    for tag, text in [("begin", None), (None, "PAGE"), ("end", None)]:
        if tag:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tag)
            run._r.append(el)
        else:
            instr = OxmlElement("w:instrText")
            instr.text = text
            run._r.append(instr)
```

- [ ] **Step 2.4: Run tests (expect pass)**

```
pytest tests/test_word_doc.py -k "test_set_run_font or test_add_section or test_add_body or test_add_table" -v
```
Expected: 4 PASSED

- [ ] **Step 2.5: Commit**

```
git add scripts/word_doc/styles.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement styles module with TNR helpers"
```

---

### Task 3: `visuals.py` — 12 matplotlib image generators

**Files:**
- Modify: `scripts/word_doc/visuals.py`
- Modify: `tests/test_word_doc.py`

Each function returns `io.BytesIO` positioned at offset 0, containing a 150 dpi PNG. Use `matplotlib.use('Agg')` to suppress display.

- [ ] **Step 3.1: Write failing tests**

Append to `tests/test_word_doc.py`:
```python
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _is_valid_png(buf):
    return buf.read(8) == PNG_MAGIC


def test_grafik_eps_is_png():
    from scripts.word_doc.visuals import generate_grafik_eps_indf
    buf = generate_grafik_eps_indf()
    assert _is_valid_png(buf)


def test_bagan_timeline_is_png():
    from scripts.word_doc.visuals import generate_bagan_timeline
    buf = generate_bagan_timeline()
    assert _is_valid_png(buf)


def test_all_visuals_return_bytesio():
    from scripts.word_doc import visuals
    funcs = [
        visuals.generate_bagan_timeline,
        visuals.generate_bagan_primary_users,
        visuals.generate_bagan_qc_sfac2,
        visuals.generate_bagan_qc_sfac8,
        visuals.generate_grafik_eps_indf,
        visuals.generate_bagan_ci_waterfall,
        visuals.generate_bagan_entry_exit_tree,
        visuals.generate_bagan_fs_hierarchy,
        visuals.generate_bagan_fasb_to_psak,
        visuals.generate_bagan_indf_org,
        visuals.generate_bagan_kepemilikan_pie,
        visuals.generate_bagan_matrix_relevance_fr,
    ]
    for fn in funcs:
        buf = fn()
        assert hasattr(buf, "read"), f"{fn.__name__} must return BytesIO"
        data = buf.read()
        assert data[:8] == PNG_MAGIC, f"{fn.__name__} must return PNG"
```

- [ ] **Step 3.2: Run tests (expect failures)**

```
pytest tests/test_word_doc.py -k "test_grafik or test_bagan or test_all_visuals" -v
```
Expected: FAILED (AttributeError / ImportError)

- [ ] **Step 3.3: Implement `scripts/word_doc/visuals.py`**

```python
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np


def _save_fig(fig) -> io.BytesIO:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return buf


# ── Bagan 1.1 — Timeline SFAC 1–8 ─────────────────────────────────────────────

def generate_bagan_timeline() -> io.BytesIO:
    events = [
        (1978, "SFAC 1\nTujuan"),
        (1980, "SFAC 2\nQC"),
        (1984, "SFAC 5\nPengakuan"),
        (1985, "SFAC 6\nElemen"),
        (2002, "Norwalk\nAgreement"),
        (2010, "SFAC 8\nCh.1–3"),
        (2018, "IASB CF\n2018"),
        (2024, "SFAC 8\nSept 2024"),
    ]
    fig, ax = plt.subplots(figsize=(9, 2.8))
    ax.set_xlim(1974, 2027)
    ax.set_ylim(-1.6, 1.8)
    ax.axhline(0, color="black", linewidth=1.5, xmin=0.01, xmax=0.99)
    for i, (year, label) in enumerate(events):
        ax.plot(year, 0, "o", color="black", markersize=7, zorder=5)
        y = 0.75 if i % 2 == 0 else -0.85
        va = "bottom" if y > 0 else "top"
        ax.annotate(
            label, xy=(year, 0), xytext=(year, y),
            fontsize=7.5, fontfamily="serif", ha="center", va=va,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="black", lw=0.6),
            arrowprops=dict(arrowstyle="-", color="gray", lw=0.7),
        )
    ax.set_title(
        "Bagan 1.1 — Evolusi Kerangka Konseptual FASB (1978–2024)",
        fontfamily="serif", fontsize=10, fontweight="bold",
    )
    ax.axis("off")
    return _save_fig(fig)


# ── Bagan 1.2 — Primary Users zones ───────────────────────────────────────────

def generate_bagan_primary_users() -> io.BytesIO:
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    # Outer box: all users
    outer = mpatches.FancyBboxPatch(
        (0.3, 0.3), 9.4, 4.4,
        boxstyle="round,pad=0.1", linewidth=1.5, edgecolor="black", facecolor="#f0f0f0"
    )
    ax.add_patch(outer)
    ax.text(5, 4.55, "Semua Pengguna Laporan Keuangan",
            ha="center", va="center", fontsize=9, fontfamily="serif", fontstyle="italic")

    # Inner box: primary users
    inner = mpatches.FancyBboxPatch(
        (1.5, 1.0), 7.0, 2.8,
        boxstyle="round,pad=0.1", linewidth=1.5, edgecolor="black", facecolor="#d0d0d0"
    )
    ax.add_patch(inner)
    ax.text(5, 3.65, "Pengguna Utama (Primary Users) — SFAC 8",
            ha="center", va="center", fontsize=9, fontfamily="serif", fontweight="bold")

    for x, label in [(3.0, "Investor\nSaat Ini &\nPotensial"),
                     (5.0, "Pemberi\nPinjaman\n(Lenders)"),
                     (7.0, "Kreditur\nLainnya")]:
        box = mpatches.FancyBboxPatch(
            (x - 0.8, 1.2), 1.6, 1.8,
            boxstyle="round,pad=0.15", linewidth=1, edgecolor="black", facecolor="white"
        )
        ax.add_patch(box)
        ax.text(x, 2.1, label, ha="center", va="center",
                fontsize=8, fontfamily="serif")

    ax.set_title(
        "Bagan 1.2 — Primary Users dan Zona Pengguna Laporan Keuangan (SFAC 8)",
        fontfamily="serif", fontsize=10, fontweight="bold",
    )
    return _save_fig(fig)


# ── Bagan 2.1 — QC tree SFAC 2 ────────────────────────────────────────────────

def generate_bagan_qc_sfac2() -> io.BytesIO:
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    def box(cx, cy, w, h, label, bold=False, fill="white"):
        r = mpatches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h,
            boxstyle="round,pad=0.1", lw=1, ec="black", fc=fill
        )
        ax.add_patch(r)
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=8, fontfamily="serif",
                fontweight="bold" if bold else "normal")

    def arrow(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="black", lw=0.8))

    # Root
    box(5, 5.3, 3.5, 0.7, "KEGUNAAN INFORMASI KEUANGAN", bold=True, fill="#d0d0d0")

    # Tier 1
    for cx, label in [(3, "Relevansi\n(Relevance)"), (7, "Keandalan\n(Reliability)")]:
        box(cx, 4.1, 2.4, 0.7, label, bold=True)
        arrow(5, 4.95, cx, 4.45)

    # Tier 2 — Relevance sub
    for cx, label in [(2, "Predictive\nValue"), (4, "Feedback\nValue")]:
        box(cx, 2.9, 1.8, 0.65, label)
        arrow(3, 3.75, cx, 3.23)

    # Tier 2 — Reliability sub
    for cx, label in [(6, "Representational\nFaithfulness"), (7.8, "Verifiability"), (9, "Neutrality")]:
        box(cx, 2.9, 1.7, 0.65, label)
        arrow(7, 3.75, cx, 3.23)

    # Threshold
    box(5, 1.6, 2.5, 0.6, "Materialitas (Threshold)", fill="#eeeeee")
    ax.text(5, 1.0, "↑ ambang batas relevansi",
            ha="center", fontsize=7.5, fontfamily="serif", fontstyle="italic")

    ax.set_title("Bagan 2.1 — Hierarki QC SFAC 2 (1980): Reliability sebagai Fundamental",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    return _save_fig(fig)


# ── Bagan 2.2 — QC tree SFAC 8 ────────────────────────────────────────────────

def generate_bagan_qc_sfac8() -> io.BytesIO:
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    def box(cx, cy, w, h, label, bold=False, fill="white"):
        r = mpatches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h,
            boxstyle="round,pad=0.1", lw=1, ec="black", fc=fill
        )
        ax.add_patch(r)
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=8, fontfamily="serif",
                fontweight="bold" if bold else "normal")

    def arrow(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="black", lw=0.8))

    box(5, 5.3, 3.5, 0.7, "KEGUNAAN INFORMASI KEUANGAN", bold=True, fill="#d0d0d0")

    # Fundamental QC
    for cx, label in [(3, "Relevansi\n(Relevance)"), (7, "Faithful\nRepresentation")]:
        box(cx, 4.1, 2.4, 0.7, label, bold=True)
        arrow(5, 4.95, cx, 4.45)

    # Relevance sub
    for cx, label in [(2, "Predictive\nValue"), (3, "Confirmatory\nValue"), (4, "Materiality")]:
        box(cx, 2.9, 1.6, 0.6, label)
        arrow(3, 3.75, cx, 3.2)

    # FR sub
    for cx, label in [(6, "Completeness"), (7.5, "Neutrality"), (9, "Free from\nError")]:
        box(cx, 2.9, 1.6, 0.6, label)
        arrow(7, 3.75, cx, 3.2)

    # Enhancing QC
    ax.text(5, 2.1, "QC Peningkat (Enhancing):", ha="center",
            fontsize=8, fontfamily="serif", fontweight="bold")
    for i, label in enumerate(["Comparability", "Verifiability*", "Timeliness", "Understandability"]):
        box(1.5 + i * 2.3, 1.45, 2.1, 0.55, label, fill="#eeeeee")
    ax.text(5, 0.7,
            "* Verifiability: diturunkan dari komponen Keandalan (SFAC 2) ke Enhancing QC (SFAC 8)",
            ha="center", fontsize=7, fontfamily="serif", fontstyle="italic")

    ax.set_title("Bagan 2.2 — Hierarki QC SFAC 8 (2010): Faithful Representation sebagai Fundamental",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    return _save_fig(fig)


# ── Grafik 2.1 — EPS INDF 2020–2024 ──────────────────────────────────────────

def generate_grafik_eps_indf() -> io.BytesIO:
    years = [2020, 2021, 2022, 2023, 2024]
    eps = [735, 873, 724, 928, 984]

    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    bars = ax.bar(years, eps, color="#333333", width=0.55, edgecolor="black", linewidth=0.6)
    for bar, val in zip(bars, eps):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
                f"Rp{val}", ha="center", va="bottom", fontsize=9, fontfamily="serif")
    ax.set_xlabel("Tahun", fontfamily="serif", fontsize=10)
    ax.set_ylabel("EPS (Rupiah per saham)", fontfamily="serif", fontsize=10)
    ax.set_title("Grafik 2.1 — Tren EPS PT Indofood Sukses Makmur Tbk, 2020–2024",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    ax.set_ylim(0, 1150)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rp{int(x):,}"))
    ax.set_xticks(years)
    for spine in ax.spines.values():
        spine.set_edgecolor("#333333")
    plt.tight_layout()
    return _save_fig(fig)


# ── Bagan 3.1 — CI Waterfall INDF 2024 ────────────────────────────────────────

def generate_bagan_ci_waterfall() -> io.BytesIO:
    # INDF 2024 figures (Rp triliun) — verify against AR 2024
    labels = ["Net Sales\n(Pendapatan)", "COGS\n(Beban Pokok)", "Gross Profit",
              "OpEx\n(Beban Operasi)", "Operating\nProfit", "Other\n(Net)", "Net Income\n(Laba Bersih)"]
    values = [115.79, -96.0, 19.79, -10.5, 9.29, -3.5, 5.79]  # illustrative; agent: verify from AR

    running = 0
    bottoms = []
    heights = []
    colors = []
    for v in values:
        if v >= 0:
            bottoms.append(running)
            heights.append(v)
            colors.append("#555555")
            running += v
        else:
            running += v
            bottoms.append(running)
            heights.append(-v)
            colors.append("#aaaaaa")

    fig, ax = plt.subplots(figsize=(8, 4))
    x = range(len(labels))
    ax.bar(x, heights, bottom=bottoms, color=colors, edgecolor="black", linewidth=0.6, width=0.6)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontfamily="serif", fontsize=8)
    ax.set_ylabel("Rp Triliun", fontfamily="serif", fontsize=10)
    ax.set_title("Bagan 3.1 — Waterfall Comprehensive Income PT INDF 2024 (Rp Triliun)",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rp{x:.0f}T"))
    plt.tight_layout()
    return _save_fig(fig)


# ── Bagan 4.1 — Entry vs Exit decision tree ───────────────────────────────────

def generate_bagan_entry_exit_tree() -> io.BytesIO:
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    def box(cx, cy, w, h, text, bold=False, fill="white"):
        r = mpatches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h,
            boxstyle="round,pad=0.15", lw=1, ec="black", fc=fill
        )
        ax.add_patch(r)
        ax.text(cx, cy, text, ha="center", va="center",
                fontsize=8, fontfamily="serif",
                fontweight="bold" if bold else "normal")

    def arrow(x1, y1, x2, y2, label=""):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="black", lw=0.8))
        if label:
            ax.text((x1+x2)/2 + 0.1, (y1+y2)/2, label,
                    fontsize=7.5, fontstyle="italic", fontfamily="serif")

    box(5, 5.3, 4.5, 0.75, "PEMILIHAN BASIS PENGUKURAN\n(SFAC 8 Ch.6, M30–M34)", bold=True, fill="#d0d0d0")
    box(5, 4.0, 4.0, 0.7, "Apakah aset/liabilitas\nmemiliki harga pasar unik?", fill="#eeeeee")
    arrow(5, 4.92, 5, 4.35)

    box(2.5, 2.6, 3.2, 0.75, "Entry Price\n(Harga Masuk)", bold=True, fill="white")
    arrow(5, 3.65, 2.5, 2.98, "YA — harga unik")

    box(7.5, 2.6, 3.2, 0.75, "Exit Price\n(Harga Keluar)", bold=True, fill="#eeeeee")
    arrow(5, 3.65, 7.5, 2.98, "TIDAK — tidak unik")

    for cx, items in [(2.5, ["Historical Cost", "Replacement Cost"]),
                      (7.5, ["Fair Value (IFRS 13)", "Net Realizable Value"])]:
        for i, label in enumerate(items):
            box(cx, 1.5 - i * 0.85, 2.8, 0.6, label)
            arrow(cx, 2.22 - i * 0, cx, 1.78 - i * 0.85)

    ax.set_title("Bagan 4.1 — Pohon Keputusan Basis Pengukuran (SFAC 8 Ch.6, M30–M34)",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    return _save_fig(fig)


# ── Bagan 4.2 — Financial Statement Hierarchy ─────────────────────────────────

def generate_bagan_fs_hierarchy() -> io.BytesIO:
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    levels = [
        (5, 5.2, 7.5, 0.75, "Laporan Keuangan (Financial Statements)", "#555555", "white"),
        (5, 4.1, 6.5, 0.7, "Catatan atas Laporan Keuangan (Notes)", "#888888", "white"),
        (5, 3.0, 5.5, 0.7, "Informasi Suplemen (Supplementary Info)", "#aaaaaa", "black"),
        (5, 1.9, 4.5, 0.7, "Informasi Lainnya (Other Info / MD&A)", "#cccccc", "black"),
    ]
    for cx, cy, w, h, label, fill, tc in levels:
        r = mpatches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h,
            boxstyle="round,pad=0.1", lw=1, ec="black", fc=fill
        )
        ax.add_patch(r)
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=8.5, fontfamily="serif", color=tc)

    ax.annotate("PR12: Notes ≠ Recognition\n(tidak dapat menggantikan pengakuan formal)",
                xy=(5, 3.75), xytext=(0.3, 2.5),
                fontsize=7.5, fontstyle="italic", fontfamily="serif",
                arrowprops=dict(arrowstyle="->", color="gray", lw=0.7))

    ax.set_title("Bagan 4.2 — Hierarki Laporan Keuangan (SFAC 8 Ch.7)",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    return _save_fig(fig)


# ── Bagan 5.1 — FASB → IASB → PSAK → INDF ────────────────────────────────────

def generate_bagan_fasb_to_psak() -> io.BytesIO:
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")

    nodes = [
        (1.2, 1.5, "FASB CF\n(SFAC 8\n2024)"),
        (3.5, 1.5, "Konvergensi\nFASB–IASB\n(2002–2010)"),
        (5.9, 1.5, "IASB CF\n2018"),
        (7.9, 1.5, "PSAK\n(KKPK IAI)"),
        (9.5, 1.5, "INDF\n2024"),
    ]
    for cx, cy, label in nodes:
        r = mpatches.FancyBboxPatch(
            (cx - 0.85, cy - 0.65), 1.7, 1.3,
            boxstyle="round,pad=0.1", lw=1, ec="black", fc="white"
        )
        ax.add_patch(r)
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=8, fontfamily="serif")

    for i in range(len(nodes) - 1):
        x1 = nodes[i][0] + 0.85
        x2 = nodes[i+1][0] - 0.85
        ax.annotate("", xy=(x2, 1.5), xytext=(x1, 1.5),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.2))

    ax.set_title("Bagan 5.1 — Jalur Pengaruh: FASB CF → IASB → PSAK → Praktik INDF",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    return _save_fig(fig)


# ── Bagan 6.1 — INDF Org Chart ────────────────────────────────────────────────

def generate_bagan_indf_org() -> io.BytesIO:
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    def box(cx, cy, w, h, label, bold=False, fill="white"):
        r = mpatches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h,
            boxstyle="round,pad=0.15", lw=1, ec="black", fc=fill
        )
        ax.add_patch(r)
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=7.5, fontfamily="serif",
                fontweight="bold" if bold else "normal")

    def arrow(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color="black", lw=0.8)

    box(5, 5.3, 4.5, 0.75,
        "PT Indofood Sukses Makmur Tbk (INDF)\nNet Sales: Rp115,79 T | EPS 2024: Rp984",
        bold=True, fill="#d0d0d0")

    divisi = [
        (1.5, 3.7, "Bogasari\n(Tepung Terigu)"),
        (3.8, 3.7, "Agribisnis\n(CPO & Karet)"),
        (6.2, 3.7, "CBP\n(ICBP — Mi Instan)"),
        (8.5, 3.7, "Distribusi\n& Lainnya"),
    ]
    for cx, cy, label in divisi:
        box(cx, cy, 2.3, 0.8, label)
        arrow(5, 4.92, cx, 4.1)

    # Key figures
    ax.text(5, 2.7, "Angka Kunci 2024:", ha="center",
            fontsize=9, fontfamily="serif", fontweight="bold")
    kv = [
        ("Total Goodwill", "Rp 52,2 T (26% total aset)"),
        ("NCI (Kepentingan Nonpengendali)", "Rp 43,077 T"),
        ("Pemegang Saham Mayoritas", "First Pacific Ltd. — 50,07%"),
        ("Auditor Independen", "Ernst & Young Purwantono, Sungkoro & Surja"),
    ]
    for i, (k, v) in enumerate(kv):
        ax.text(2.0, 2.1 - i * 0.55, f"• {k}: {v}",
                fontsize=8, fontfamily="serif")

    ax.set_title("Bagan 6.1 — Struktur Konglomerat & Angka Kunci PT INDF (2024)",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    return _save_fig(fig)


# ── Bagan 6.2 — Pie kepemilikan INDF ─────────────────────────────────────────

def generate_bagan_kepemilikan_pie() -> io.BytesIO:
    labels = ["First Pacific Ltd.\n50,07%", "Publik &\nInstitusional\n49,93%"]
    sizes = [50.07, 49.93]
    colors = ["#333333", "#aaaaaa"]

    fig, ax = plt.subplots(figsize=(5.5, 4))
    wedges, texts = ax.pie(
        sizes, labels=labels, colors=colors,
        startangle=90, wedgeprops={"edgecolor": "white", "linewidth": 1.5},
        textprops={"fontfamily": "serif", "fontsize": 9},
    )
    ax.set_title("Bagan 6.2 — Struktur Kepemilikan PT INDF per 31 Des 2024",
                 fontfamily="serif", fontsize=10, fontweight="bold")
    plt.tight_layout()
    return _save_fig(fig)


# ── Bagan 6.3 — 2×2 Matrix Relevance × FR ─────────────────────────────────────

def generate_bagan_matrix_relevance_fr() -> io.BytesIO:
    fig, ax = plt.subplots(figsize=(6.5, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Quadrant borders
    for x in [5]:
        ax.axvline(x, color="black", linewidth=1.2, ymin=0.07, ymax=0.87)
    for y in [3.5]:
        ax.axhline(y, color="black", linewidth=1.2, xmin=0.0, xmax=1.0,
                   ymin=0, ymax=1)

    ax.text(5, 6.5, "Matrix: Relevansi × Faithful Representation — Item LK INDF 2024",
            ha="center", fontsize=9.5, fontfamily="serif", fontweight="bold")

    # Axis labels
    ax.text(2.5, 0.2, "Relevansi Rendah", ha="center", fontsize=8.5, fontfamily="serif")
    ax.text(7.5, 0.2, "Relevansi Tinggi", ha="center", fontsize=8.5, fontfamily="serif")
    ax.text(0.3, 1.75, "FR\nRendah", ha="center", va="center", fontsize=8.5, fontfamily="serif")
    ax.text(0.3, 5.25, "FR\nTinggi", ha="center", va="center", fontsize=8.5, fontfamily="serif")

    # Quadrant labels + items
    quads = [
        (2.5, 5.25, "Q1: FR Tinggi, Rel. Rendah", ["Aset Biologis\n(Fair Value)"]),
        (7.5, 5.25, "Q2: Ideal — Tinggi Keduanya", ["EPS (Rp984)", "Revenue\n(Rp115,79T)"]),
        (2.5, 1.75, "Q3: Rendah Keduanya", ["Beban Tidak\nLangsung"]),
        (7.5, 1.75, "Q4: Rel. Tinggi, FR Rendah", ["Goodwill\n(Rp52,2T)"]),
    ]
    fills = ["#f0f0f0", "#d0d0d0", "#e8e8e8", "#eeeeee"]
    for (cx, cy, title, items), fill in zip(quads, fills):
        r = mpatches.Rectangle((cx - 2.3, cy - 1.2), 4.6, 2.4, lw=0, fc=fill)
        ax.add_patch(r)
        ax.text(cx, cy + 0.9, title, ha="center", fontsize=7.5,
                fontfamily="serif", fontweight="bold")
        for i, item in enumerate(items):
            ax.text(cx, cy + 0.15 - i * 0.7, item, ha="center",
                    fontsize=7.5, fontfamily="serif")

    return _save_fig(fig)
```

- [ ] **Step 3.4: Run tests**

```
pytest tests/test_word_doc.py -k "test_grafik or test_bagan or test_all_visuals" -v
```
Expected: 3 PASSED

- [ ] **Step 3.5: Commit**

```
git add scripts/word_doc/visuals.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement 12 matplotlib visual generators"
```

---

### Task 4: `cover.py` — formal cover page

**Files:**
- Modify: `scripts/word_doc/cover.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 4.1: Write failing tests**

Append to `tests/test_word_doc.py`:
```python
import os
BASE_DIR = os.path.join(
    os.path.dirname(__file__), ".."
)


def test_cover_adds_all_six_members():
    from docx import Document
    from scripts.word_doc.cover import build_cover
    doc = Document()
    logo_path = os.path.join(BASE_DIR, "STIE Logo.png")
    build_cover(doc, logo_path)
    full_text = "\n".join(p.text for p in doc.paragraphs)
    for name in [
        "Efri Nurmalinda", "Dzaki Muhammad Yusfian",
        "Nuradila", "Achmad Dimas Wibawa",
        "Adinda Putri Dewi", "Setiabudi Yudha Pratama",
    ]:
        assert name in full_text, f"Missing member: {name}"


def test_cover_contains_title_keywords():
    from docx import Document
    from scripts.word_doc.cover import build_cover
    doc = Document()
    logo_path = os.path.join(BASE_DIR, "STIE Logo.png")
    build_cover(doc, logo_path)
    full_text = "\n".join(p.text for p in doc.paragraphs)
    assert "KERANGKA KONSEPTUAL FASB" in full_text
    assert "MNK202" in full_text
```

- [ ] **Step 4.2: Run tests (expect failures)**

```
pytest tests/test_word_doc.py -k "test_cover" -v
```
Expected: FAILED

- [ ] **Step 4.3: Implement `scripts/word_doc/cover.py`**

```python
import os
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from scripts.word_doc.styles import set_run_font, _add_para_border


NAVY = "1E3A5F"


def _blue_rule(doc, side):
    """Paragraph with a thick navy border on top or bottom."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    _add_para_border(p, [side], sz="24", color=NAVY)
    return p


def _centered(doc, text, size_pt, bold=False, italic=False,
               space_before=6, space_after=6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    set_run_font(run, size_pt, bold=bold, italic=italic)
    return p


def build_cover(doc, logo_path: str) -> None:
    """
    Build the formal cover page (Opsi A — Formal Akademik Klasik).
    Mutates `doc` in place.
    """
    # Top blue rule
    _blue_rule(doc, "top")

    # Institution header
    _centered(doc,
              "PROGRAM MAGISTER AKUNTANSI — STIE YKPN YOGYAKARTA",
              size_pt=11, bold=True, space_before=18, space_after=12)

    # Logo
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(6)
        p_logo.paragraph_format.space_after = Pt(14)
        run = p_logo.add_run()
        run.add_picture(logo_path, height=Inches(1.4))
    else:
        _centered(doc, "[Logo STIE YKPN]", 10, italic=True)

    # Document title (two lines)
    _centered(doc,
              "KERANGKA KONSEPTUAL FASB:\nFONDASI STANDAR PELAPORAN KEUANGAN",
              size_pt=16, bold=True, space_before=10, space_after=8)

    # Subtitle
    _centered(doc,
              "PT Indofood Sukses Makmur Tbk (INDF) sebagai Studi Kasus",
              size_pt=12, italic=True, space_before=4, space_after=20)

    # Course info
    _centered(doc, "MNK202 Pelaporan Keuangan Korporat",
              size_pt=11, space_before=8, space_after=4)
    _centered(doc, "Kelompok 3  |  Tahun Akademik 2025/2026",
              size_pt=11, space_before=2, space_after=16)

    # Member list
    members = [
        ("1.", "Efri Nurmalinda",          "NIM: 1225 01049"),
        ("2.", "Dzaki Muhammad Yusfian",   "NIM: 1225 01079"),
        ("3.", "Nuradila",                 "NIM: 1225 01080"),
        ("4.", "Achmad Dimas Wibawa",      "NIM: 1225 01083"),
        ("5.", "Adinda Putri Dewi",        "NIM: 1225 01086"),
        ("6.", "Setiabudi Yudha Pratama",  "NIM: 1225 01098"),
    ]
    for no, name, nim in members:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(f"{no:<4}{name:<35}{nim}")
        set_run_font(run, 12)

    # Spacer
    _centered(doc, "", size_pt=10, space_before=20, space_after=0)

    # Bottom blue rule
    _blue_rule(doc, "bottom")
```

- [ ] **Step 4.4: Run tests**

```
pytest tests/test_word_doc.py -k "test_cover" -v
```
Expected: 2 PASSED

- [ ] **Step 4.5: Commit**

```
git add scripts/word_doc/cover.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement formal cover page with STIE logo"
```

---

### Task 5: `front_matter.py` — Kata Pengantar + Table of Contents

**Files:**
- Modify: `scripts/word_doc/front_matter.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 5.1: Write failing test**

Append to `tests/test_word_doc.py`:
```python
def test_front_matter_contains_kata_pengantar():
    from docx import Document
    from scripts.word_doc.front_matter import build_front_matter
    doc = Document()
    build_front_matter(doc)
    full_text = "\n".join(p.text for p in doc.paragraphs)
    assert "Kata Pengantar" in full_text
    assert "DAFTAR ISI" in full_text
```

- [ ] **Step 5.2: Run test (expect failure)**

```
pytest tests/test_word_doc.py::test_front_matter_contains_kata_pengantar -v
```
Expected: FAILED

- [ ] **Step 5.3: Implement `scripts/word_doc/front_matter.py`**

```python
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from scripts.word_doc.styles import (
    add_doc_title, add_body_paragraph, add_section_heading, add_page_break,
    set_run_font,
)


def _add_toc_field(doc):
    """
    Insert a Word TOC field. The user must press Ctrl+A → F9 (or right-click
    → Update Field) after opening the document to populate page numbers.
    """
    p = doc.add_paragraph()
    run = p.add_run()
    for tag, text in [("begin", None), (None, ' TOC \\o "1-3" \\h \\z \\u '), ("end", None)]:
        if tag:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tag)
            run._r.append(el)
        else:
            instr = OxmlElement("w:instrText")
            instr.set(qn("xml:space"), "preserve")
            instr.text = text
            run._r.append(instr)

    note = doc.add_paragraph()
    note.paragraph_format.space_before = Pt(6)
    run_note = note.add_run(
        "[Catatan: Klik kanan pada area ini → Update Field untuk memperbarui nomor halaman]"
    )
    set_run_font(run_note, 9, italic=True, color_rgb=(100, 100, 100))


def build_front_matter(doc) -> None:
    """Adds Daftar Isi (TOC) page then Kata Pengantar page."""

    # ── Page 2: Daftar Isi ─────────────────────────────────────────────────────
    p_toc_title = doc.add_paragraph()
    p_toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_title.paragraph_format.space_after = Pt(12)
    run = p_toc_title.add_run("DAFTAR ISI")
    set_run_font(run, 14, bold=True)

    _add_toc_field(doc)
    add_page_break(doc)

    # ── Page 3: Kata Pengantar ─────────────────────────────────────────────────
    p_kp_title = doc.add_paragraph()
    p_kp_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kp_title.paragraph_format.space_after = Pt(12)
    run = p_kp_title.add_run("Kata Pengantar")
    set_run_font(run, 14, bold=True)

    add_body_paragraph(
        doc,
        "Puji syukur kami panjatkan kepada Tuhan Yang Maha Esa atas terselesaikannya "
        "makalah kelompok ini dalam rangka memenuhi tugas mata kuliah MNK202 Pelaporan "
        "Keuangan Korporat, Program Magister Akuntansi STIE YKPN Yogyakarta. Makalah ini "
        "menyajikan analisis komprehensif terhadap Kerangka Konseptual Financial Accounting "
        "Standards Board (FASB) — mulai dari SFAC 1 (1978) hingga SFAC 8 edisi September "
        "2024 — serta mengaplikasikan kerangka tersebut pada laporan tahunan PT Indofood "
        "Sukses Makmur Tbk (INDF) tahun 2024 sebagai studi kasus empiris. Kami berharap "
        "dokumen ini dapat memberikan kontribusi pemahaman yang mendalam mengenai fondasi "
        "konseptual yang mendasari standar pelaporan keuangan modern."
    )
    add_body_paragraph(
        doc,
        "Penyusunan makalah ini tidak terlepas dari bimbingan dosen pengampu dan kontribusi "
        "seluruh anggota kelompok. Kami menyadari bahwa dokumen ini masih jauh dari sempurna "
        "dan terbuka untuk masukan konstruktif demi peningkatan kualitas pemahaman bersama."
    )

    p_ttd = doc.add_paragraph()
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_ttd = p_ttd.add_run("Yogyakarta, April 2026\n\nKelompok 3 — MNK202")
    set_run_font(run_ttd, 12)

    add_page_break(doc)
```

- [ ] **Step 5.4: Run test**

```
pytest tests/test_word_doc.py::test_front_matter_contains_kata_pengantar -v
```
Expected: PASSED

- [ ] **Step 5.5: Commit**

```
git add scripts/word_doc/front_matter.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement front matter (TOC + Kata Pengantar)"
```

---

### Task 6: `bagian_i.py` — Bagian I: Konteks & Evolusi CF

**Files:**
- Modify: `scripts/word_doc/sections/bagian_i.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 6.1: Write failing test**

Append to `tests/test_word_doc.py`:
```python
def test_bagian_i_contains_key_content():
    from docx import Document
    from scripts.word_doc.sections.bagian_i import build
    doc = Document()
    build(doc)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "SFAC 1" in text
    assert "Norwalk Agreement" in text
    assert "PSAK" in text
    # Tabel 1.1 and Tabel 1.2
    assert len(doc.tables) >= 2
```

- [ ] **Step 6.2: Run test (expect failure)**

```
pytest tests/test_word_doc.py::test_bagian_i_contains_key_content -v
```

- [ ] **Step 6.3: Implement `scripts/word_doc/sections/bagian_i.py`**

```python
import io
from docx.shared import Inches
from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph,
    add_caption, add_table_with_headers, add_footnote_text,
)
from scripts.word_doc.visuals import generate_bagan_timeline, generate_bagan_primary_users


def build(doc) -> None:
    """Bagian I — Konteks dan Evolusi Kerangka Konseptual FASB"""

    add_section_heading(doc, "I. KONTEKS DAN EVOLUSI KERANGKA KONSEPTUAL FASB")

    # ── I.1 Sejarah Perkembangan ───────────────────────────────────────────────
    add_sub_heading(doc, "I.1 Sejarah Perkembangan: SFAC 1 (1978) hingga SFAC 8 (2024)")
    add_body_paragraph(
        doc,
        "Kerangka Konseptual (Conceptual Framework/CF) FASB merupakan fondasi hierarkis "
        "yang mendasari seluruh standar pelaporan keuangan yang diterbitkan oleh Financial "
        "Accounting Standards Board (FASB). Berbeda dengan standar individual yang mengatur "
        "transaksi spesifik, kerangka konseptual menetapkan prinsip-prinsip dasar yang menjadi "
        "rujukan ketika standar yang ada tidak mencakup suatu transaksi tertentu — sebuah fungsi "
        "yang oleh Wolk, Dodd & Rozycki (2017) disebut sebagai 'panduan pengambilan keputusan "
        "ketika aturan spesifik tidak tersedia.'"
    )
    add_body_paragraph(
        doc,
        "Perjalanan CF FASB dimulai pada tahun 1978 dengan diterbitkannya SFAC 1 (Statement of "
        "Financial Accounting Concepts No. 1), yang untuk pertama kalinya menetapkan tujuan "
        "pelaporan keuangan secara eksplisit. Selama lebih dari empat dekade, FASB telah "
        "menerbitkan delapan SFAC, dengan edisi komprehensif terakhir SFAC 8 diterbitkan pada "
        "September 2024 — mengintegrasikan seluruh pembaruan konseptual termasuk definisi aset "
        "baru (Chapter 4), tiga kriteria pengakuan (Chapter 5), dua sistem pengukuran "
        "(Chapter 6), dan panduan penyajian (Chapter 7)."
    )

    # Timeline visual
    add_caption(doc, "Bagan 1.1 — Evolusi Kerangka Konseptual FASB (1978–2024)")
    p_img = doc.add_paragraph()
    p_img.alignment = 1  # CENTER
    p_img.add_run().add_picture(generate_bagan_timeline(), width=Inches(5.8))

    # Tabel 1.1 — 8 SFAC
    add_caption(doc, "Tabel 1.1 — Ringkasan Delapan Statement of Financial Accounting Concepts (SFAC)")
    add_table_with_headers(
        doc,
        headers=["No.", "Tahun", "Judul / Topik", "Status"],
        rows_data=[
            ["SFAC 1", "1978", "Tujuan Pelaporan Keuangan Bisnis",
             "Digantikan SFAC 8 (2010)"],
            ["SFAC 2", "1980", "Karakteristik Kualitatif Informasi Akuntansi",
             "Digantikan SFAC 8 (2010)"],
            ["SFAC 3", "1980", "Elemen Laporan Keuangan Bisnis",
             "Digantikan SFAC 6 (1985)"],
            ["SFAC 4", "1980", "Tujuan LK Entitas Non-Bisnis",
             "Aktif"],
            ["SFAC 5", "1984", "Pengakuan dan Pengukuran dalam LK Bisnis",
             "Aktif — dikritisi akademisi"],
            ["SFAC 6", "1985", "Elemen Laporan Keuangan (Revisi)",
             "Aktif"],
            ["SFAC 7", "2000", "Penggunaan Cash Flow dan Nilai Sekarang",
             "Aktif"],
            ["SFAC 8", "2010–2024", "Kerangka Konseptual (8 Chapters, Sept 2024)",
             "Aktif — edisi terkini"],
        ],
    )

    # ── I.2 SFAC 1 & Primary Users ────────────────────────────────────────────
    add_sub_heading(doc, "I.2 SFAC 1: Tujuan Pelaporan Keuangan dan Primary Users")
    add_body_paragraph(
        doc,
        "SFAC 1 (1978) menetapkan bahwa tujuan utama pelaporan keuangan adalah menyediakan "
        "informasi yang berguna bagi pengguna utama (primary users): investor saat ini dan "
        "potensial, serta kreditor. Informasi tersebut harus membantu mereka dalam mengevaluasi "
        "jumlah, waktu, dan ketidakpastian arus kas masa depan entitas — sebuah perspektif yang "
        "secara eksplisit menempatkan investor dan kreditur sebagai fokus utama, bukan manajemen "
        "atau regulator."
    )
    add_body_paragraph(
        doc,
        "SFAC 8 (2010) mempertegas konsep ini dengan mendefinisikan primary users sebagai "
        "mereka yang tidak dapat meminta laporan khusus dari entitas (cannot require entities "
        "to provide information directly). Definisi ini penting karena menetapkan batasan "
        "yang jelas mengenai siapa yang menjadi audiens utama laporan keuangan bertujuan "
        "umum (general purpose financial statements/GPFS)."
    )

    add_caption(doc, "Bagan 1.2 — Primary Users dan Zona Pengguna Laporan Keuangan (SFAC 8)")
    p_pu = doc.add_paragraph()
    p_pu.alignment = 1
    p_pu.add_run().add_picture(generate_bagan_primary_users(), width=Inches(5.0))

    # Tabel 1.2 — SFAC 1 vs SFAC 8 Ch.1
    add_caption(doc, "Tabel 1.2 — Perbandingan Tujuan Pelaporan Keuangan: SFAC 1 (1978) vs. SFAC 8 Ch.1 (2010)")
    add_table_with_headers(
        doc,
        headers=["Dimensi", "SFAC 1 (1978)", "SFAC 8 Ch.1 (2010)"],
        rows_data=[
            ["Tujuan Utama",
             "Informasi berguna untuk keputusan investasi dan kredit",
             "Informasi berguna bagi primary users untuk keputusan penyediaan sumber daya"],
            ["Definisi Primary Users",
             "Investor, kreditor, dan pengguna potensial",
             "Existing/potential investors, lenders, other creditors yang tidak dapat meminta info langsung"],
            ["Fokus Informasi",
             "Arus kas masa depan entitas",
             "Arus kas masa depan + posisi keuangan + kinerja (earning power)"],
            ["Perspektif",
             "Stewardship sebagai tujuan sekunder",
             "Stewardship (akuntabilitas manajemen) sebagai tujuan setara dengan keputusan"],
        ],
    )

    # ── I.3 Norwalk Agreement ─────────────────────────────────────────────────
    add_sub_heading(doc, "I.3 Norwalk Agreement (2002) dan Konvergensi FASB–IASB")
    add_body_paragraph(
        doc,
        "Tonggak penting dalam sejarah konvergensi standar akuntansi global adalah "
        "Norwalk Agreement pada 18 September 2002. Dalam perjanjian ini, FASB dan "
        "International Accounting Standards Board (IASB) secara resmi berkomitmen untuk "
        "mengembangkan standar akuntansi yang kompatibel secara internasional dan "
        "mengoordinasikan agenda kerja mereka. Salah satu produk langsung dari komitmen "
        "ini adalah proyek bersama pengembangan kerangka konseptual, yang menghasilkan "
        "SFAC 8 pada tahun 2010 — sebuah dokumen yang mencerminkan konsensus FASB dan IASB "
        "setelah hampir satu dekade deliberasi bersama."
    )

    # ── I.4 Relevansi untuk Indonesia ─────────────────────────────────────────
    add_sub_heading(doc, "I.4 Relevansi bagi Indonesia: IASB CF 2018 → PSAK")
    add_body_paragraph(
        doc,
        "Di Indonesia, Dewan Standar Akuntansi Keuangan — Ikatan Akuntan Indonesia (DSAK-IAI) "
        "mengadopsi Kerangka Konseptual Pelaporan Keuangan (KKPK) berdasarkan IASB Conceptual "
        "Framework for Financial Reporting 2018. Dengan demikian, terdapat jalur pengaruh yang "
        "jelas: FASB CF (SFAC 8) → Konvergensi FASB–IASB (2002–2010) → IASB CF 2018 → "
        "PSAK/KKPK IAI → Praktik pelaporan keuangan entitas Indonesia. PT Indofood Sukses "
        "Makmur Tbk, sebagai entitas yang menyusun laporan keuangan konsolidasi berdasarkan "
        "PSAK, merupakan manifestasi langsung dari rantai pengaruh konseptual ini."
    )

    add_footnote_text(
        doc,
        "¹ SFAC = Statement of Financial Accounting Concepts. PSAK = Pernyataan Standar "
        "Akuntansi Keuangan. KKPK = Kerangka Konseptual Pelaporan Keuangan (DSAK-IAI). "
        "Sumber utama: Wolk, Dodd & Rozycki (2017), Ch.7; SFAC 8 (September 2024)."
    )
```

- [ ] **Step 6.4: Run test**

```
pytest tests/test_word_doc.py::test_bagian_i_contains_key_content -v
```
Expected: PASSED

- [ ] **Step 6.5: Commit**

```
git add scripts/word_doc/sections/bagian_i.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement Bagian I — Konteks & Evolusi CF"
```

---

### Task 7: `bagian_ii.py` — Bagian II: Karakteristik Kualitatif

**Files:**
- Modify: `scripts/word_doc/sections/bagian_ii.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 7.1: Write failing test**

Append to `tests/test_word_doc.py`:
```python
def test_bagian_ii_contains_key_content():
    from docx import Document
    from scripts.word_doc.sections.bagian_ii import build
    doc = Document()
    build(doc)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "Faithful Representation" in text
    assert "Reliability" in text
    assert "BC3.27" in text
    assert len(doc.tables) >= 1
    assert len(doc.inline_shapes) >= 3   # 2 trees + 1 bar chart
```

- [ ] **Step 7.2: Run test (expect failure)**

```
pytest tests/test_word_doc.py::test_bagian_ii_contains_key_content -v
```

- [ ] **Step 7.3: Implement `scripts/word_doc/sections/bagian_ii.py`**

```python
import io
from docx.shared import Inches
from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph,
    add_caption, add_table_with_headers, add_footnote_text,
)
from scripts.word_doc.visuals import (
    generate_bagan_qc_sfac2, generate_bagan_qc_sfac8, generate_grafik_eps_indf,
)


def build(doc) -> None:
    """Bagian II — Karakteristik Kualitatif Informasi Keuangan"""

    add_section_heading(doc, "II. KARAKTERISTIK KUALITATIF INFORMASI KEUANGAN")

    # II.1 SFAC 2
    add_sub_heading(doc, "II.1 SFAC 2 (1980): Hierarki Keandalan (Reliability)")
    add_body_paragraph(
        doc,
        "SFAC 2 (1980) mendefinisikan dua karakteristik kualitatif fundamental informasi "
        "keuangan: Relevansi (Relevance) dan Keandalan (Reliability). Keandalan diurai lebih "
        "lanjut menjadi tiga komponen: Representational Faithfulness (ketepatan representasi), "
        "Verifiability (dapat diverifikasi pihak independen), dan Neutrality (kebebasan dari "
        "bias). Posisi Verifiability sebagai komponen setara dari Keandalan — bukan subordinat — "
        "mencerminkan paradigma akuntansi era 1980-an yang sangat menekankan objektivitas "
        "dan kemampuan audit."
    )
    add_body_paragraph(
        doc,
        "Selain dua karakteristik fundamental tersebut, SFAC 2 menempatkan Komparabilitas "
        "(Comparability) sebagai karakteristik interaktif yang meningkatkan kegunaan "
        "informasi ketika digunakan bersama relevansi dan keandalan. Materialitas berfungsi "
        "sebagai ambang batas (threshold) yang menentukan apakah suatu informasi cukup "
        "signifikan untuk diungkapkan — bukan sebagai karakteristik kualitatif itu sendiri."
    )
    add_caption(doc, "Bagan 2.1 — Hierarki QC SFAC 2 (1980): Reliability sebagai Karakteristik Fundamental")
    p1 = doc.add_paragraph()
    p1.alignment = 1
    p1.add_run().add_picture(generate_bagan_qc_sfac2(), width=Inches(5.5))

    # II.2 SFAC 8
    add_sub_heading(doc, "II.2 SFAC 8 (2010): Perubahan Fundamental ke Faithful Representation")
    add_body_paragraph(
        doc,
        "SFAC 8 (2010) melakukan perubahan konseptual yang paling signifikan dalam sejarah "
        "kerangka konseptual FASB: penggantian istilah Reliability dengan Faithful Representation "
        "(representasi tepat) sebagai karakteristik kualitatif fundamental kedua. Perubahan ini "
        "bukan sekadar pergantian nama — ia mencerminkan pergeseran paradigma mendasar dari "
        "pertanyaan 'dapatkah kita memverifikasi informasi ini?' menjadi 'apakah informasi ini "
        "merepresentasikan realitas ekonomi yang mendasarinya dengan tepat?' "
        "(Wolk, Dodd & Rozycki 2017, hal. 170–172)."
    )
    add_body_paragraph(
        doc,
        "Faithful Representation dalam SFAC 8 terdiri dari tiga sub-komponen: "
        "Completeness (kelengkapan informasi yang diperlukan untuk pemahaman), "
        "Neutrality (bebas dari bias dan pilihan kebijakan yang menguntungkan pihak tertentu), "
        "dan Free from Error (tidak terdapat kesalahan material dalam deskripsi fenomena). "
        "Sementara itu, empat karakteristik peningkat (Enhancing QCs) — Comparability, "
        "Verifiability, Timeliness, dan Understandability — berfungsi memaksimalkan kegunaan "
        "informasi yang sudah memenuhi dua QC fundamental."
    )
    add_caption(doc, "Bagan 2.2 — Hierarki QC SFAC 8 (2010): Faithful Representation sebagai Fundamental")
    p2 = doc.add_paragraph()
    p2.alignment = 1
    p2.add_run().add_picture(generate_bagan_qc_sfac8(), width=Inches(5.5))

    # II.3 Komparasi
    add_sub_heading(doc, "II.3 Analisis Komparatif: SFAC 2 vs. SFAC 8 — Perubahan Mendasar")
    add_body_paragraph(
        doc,
        "Penurunan status Verifiability dari komponen Keandalan (SFAC 2) menjadi Enhancing QC "
        "(SFAC 8) merupakan salah satu perubahan paling dramatis dalam evolusi kerangka "
        "konseptual. Implikasinya: informasi yang sangat mudah diverifikasi (seperti harga "
        "perolehan historis) tidak serta-merta superior dibandingkan informasi yang sulit "
        "diverifikasi tetapi lebih representatif (seperti nilai wajar aset yang diperdagangkan "
        "di pasar aktif). SFAC 8 secara eksplisit menempatkan representasi realitas ekonomi "
        "di atas kemudahan verifikasi."
    )
    add_body_paragraph(
        doc,
        "Penghapusan Conservatism (Konservatisme) dari SFAC 8 merupakan perubahan kedua yang "
        "paling diperdebatkan. FASB dalam Basis for Conclusions paragraf BC3.27–BC3.29 "
        "menjelaskan bahwa konservatisme bertentangan secara fundamental dengan Neutrality — "
        "komponen Faithful Representation. Sebuah kerangka konseptual tidak dapat sekaligus "
        "menuntut netralitas dan mengizinkan kecenderungan sistematis ke arah pesimisme "
        "(under-statement aset, over-statement liabilitas)."
    )
    add_caption(doc, "Tabel 2.1 — Perbandingan Hierarki QC: SFAC 2 (1980) vs. SFAC 8 (2010)")
    add_table_with_headers(
        doc,
        headers=["Dimensi", "SFAC 2 (1980)", "SFAC 8 (2010)", "Perubahan"],
        rows_data=[
            ["QC Fundamental 1", "Relevansi", "Relevansi", "Dipertahankan"],
            ["QC Fundamental 2", "Reliability (Keandalan)", "Faithful Representation",
             "Diganti nama + direkonstitusi"],
            ["Status Verifiability", "Komponen Keandalan (setara FR & Neutrality)",
             "Enhancing QC (subordinat)", "Diturunkan drastis"],
            ["Konservatisme", "Disebutkan sebagai 'konvensi yang berguna'",
             "Dihapus sepenuhnya (BC3.27–29)", "Konflik dengan Neutrality"],
            ["Materialitas", "Threshold bawah relevansi", "Threshold bawah relevansi",
             "Dipertahankan"],
        ],
    )

    # II.4–II.5 Relevansi & Enhancing — embed EPS chart here as application preview
    add_sub_heading(doc, "II.4 Relevansi dalam Konteks INDF: Tren EPS sebagai Ilustrasi")
    add_body_paragraph(
        doc,
        "Konsep Relevansi dalam SFAC 8 mencakup dua dimensi: Predictive Value (nilai "
        "prediktif — membantu pengguna memproyeksikan hasil masa depan) dan Confirmatory Value "
        "(nilai konfirmasi — mengkonfirmasi atau mengoreksi ekspektasi sebelumnya). Tren "
        "Earnings Per Share (EPS) PT Indofood Sukses Makmur Tbk selama 2020–2024 "
        "mendemonstrasikan kedua dimensi ini: EPS berfungsi sebagai indikator prediktif "
        "profitabilitas per saham sekaligus konfirmasi realisasi kinerja terhadap proyeksi analis."
    )
    add_caption(doc, "Grafik 2.1 — Tren EPS PT INDF 2020–2024 (Rp per saham)")
    p3 = doc.add_paragraph()
    p3.alignment = 1
    p3.add_run().add_picture(generate_grafik_eps_indf(), width=Inches(5.0))

    add_footnote_text(
        doc,
        "² Sumber EPS: Annual Report PT Indofood Sukses Makmur Tbk 2024. "
        "BC3.27–BC3.29 mengacu pada Basis for Conclusions SFAC 8 (September 2024). "
        "Wolk et al. (2017) Ch.7 Exhibit 7.1 (SFAC 2) dan Exhibit 7.5 (SFAC 8)."
    )
```

- [ ] **Step 7.4: Run test**

```
pytest tests/test_word_doc.py::test_bagian_ii_contains_key_content -v
```
Expected: PASSED

- [ ] **Step 7.5: Commit**

```
git add scripts/word_doc/sections/bagian_ii.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement Bagian II — Karakteristik Kualitatif"
```

---

### Task 8: `bagian_iii.py` — Bagian III: Elemen Laporan Keuangan

**Files:**
- Modify: `scripts/word_doc/sections/bagian_iii.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 8.1: Write failing test**

Append to `tests/test_word_doc.py`:
```python
def test_bagian_iii_contains_key_content():
    from docx import Document
    from scripts.word_doc.sections.bagian_iii import build
    doc = Document()
    build(doc)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "present right" in text
    assert "BC4.7" in text
    assert "Comprehensive Income" in text
    assert len(doc.tables) >= 2
```

- [ ] **Step 8.2: Run test (expect failure)**

```
pytest tests/test_word_doc.py::test_bagian_iii_contains_key_content -v
```

- [ ] **Step 8.3: Implement `scripts/word_doc/sections/bagian_iii.py`**

```python
from docx.shared import Inches
from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph,
    add_caption, add_table_with_headers, add_footnote_text,
)
from scripts.word_doc.visuals import generate_bagan_ci_waterfall


def build(doc) -> None:
    """Bagian III — Elemen-Elemen Laporan Keuangan"""

    add_section_heading(doc, "III. ELEMEN-ELEMEN LAPORAN KEUANGAN")

    # III.1 SFAC 6 — 10 elemen
    add_sub_heading(doc, "III.1 SFAC 6 (1985): Sepuluh Elemen Laporan Keuangan")
    add_body_paragraph(
        doc,
        "SFAC 6 (1985) mendefinisikan sepuluh elemen laporan keuangan yang membentuk "
        "kerangka dasar penyusunan neraca dan laporan laba rugi. Elemen-elemen ini bukan "
        "sekadar kategori akuntansi — masing-masing memiliki definisi konseptual yang presisi "
        "yang membedakannya dari elemen lain dan menentukan kondisi pengakuan dalam laporan "
        "keuangan."
    )
    add_caption(doc, "Tabel 3.1 — Sepuluh Elemen Laporan Keuangan (SFAC 6, 1985)")
    add_table_with_headers(
        doc,
        headers=["Elemen", "Definisi Konseptual (ringkas)", "Posisi dalam LK"],
        rows_data=[
            ["Assets", "Manfaat ekonomi masa depan yang mungkin diperoleh atau dikendalikan entitas",
             "Neraca (Aset)"],
            ["Liabilities", "Pengorbanan manfaat ekonomi masa depan yang probable dari kewajiban sekarang",
             "Neraca (Liabilitas)"],
            ["Equity", "Kepentingan residual aset setelah dikurangi liabilitas",
             "Neraca (Ekuitas)"],
            ["Investments by Owners", "Kenaikan ekuitas dari transfer aset oleh pemilik",
             "Laporan Ekuitas"],
            ["Distributions to Owners", "Penurunan ekuitas dari transfer ke pemilik",
             "Laporan Ekuitas"],
            ["Comprehensive Income (CI)", "Perubahan ekuitas dari transaksi non-pemilik",
             "Laporan Laba Rugi Komprehensif"],
            ["Revenues", "Arus masuk/peningkatan aset dari aktivitas utama entitas",
             "Laporan Laba Rugi"],
            ["Expenses", "Arus keluar/penggunaan aset dari aktivitas utama entitas",
             "Laporan Laba Rugi"],
            ["Gains", "Kenaikan ekuitas dari transaksi peripheral (bukan aktivitas utama)",
             "Laporan Laba Rugi"],
            ["Losses", "Penurunan ekuitas dari transaksi peripheral",
             "Laporan Laba Rugi"],
        ],
    )

    # III.2 SFAC 8 Ch.4 — definisi aset baru
    add_sub_heading(doc, "III.2 SFAC 8 Chapter 4 (Juli 2024): Redefinisi Fundamental Aset")
    add_body_paragraph(
        doc,
        "SFAC 8 Chapter 4 (Juli 2024) melakukan perubahan yang secara konseptual lebih radikal "
        "dari sekadar memperbarui bahasa: definisi aset diganti dari 'probable future economic "
        "benefits' (SFAC 6) menjadi 'a present right of the entity to an economic benefit.' "
        "Perubahan ini memiliki implikasi praktis yang substansial: kata 'probable' dan "
        "konsep 'kontrol' (control) dihapus dari definisi formal."
    )
    add_body_paragraph(
        doc,
        "Dalam Basis for Conclusions paragraf BC4.7, FASB menjelaskan bahwa definisi baru "
        "memberikan primasi konseptual pada hak hukum (present right) sebagai dasar pengakuan "
        "aset, bukan pada kemungkinan realisasi manfaat di masa depan. Implikasinya: suatu hak "
        "yang ada saat ini sudah cukup untuk memenuhi definisi aset, meskipun probabilitas "
        "realisasi manfaat ekonomi masih rendah. Penentuan apakah aset tersebut diakui dalam "
        "laporan keuangan merupakan fungsi dari kriteria pengakuan (Recognition — Chapter 5), "
        "bukan definisi elemen."
    )
    add_caption(doc, "Tabel 3.2 — Perbandingan Definisi Aset: SFAC 6 (1985) vs. SFAC 8 Ch.4 (Juli 2024)")
    add_table_with_headers(
        doc,
        headers=["Aspek", "SFAC 6 (1985)", "SFAC 8 Ch.4 (Juli 2024)"],
        rows_data=[
            ["Definisi Aset",
             "Probable future economic benefits obtained or controlled by an entity as a result of past transactions",
             "A present right of the entity to an economic benefit"],
            ["Kata Kunci", "'Probable' + 'controlled' + 'future benefits'",
             "'Present right' saja"],
            ["Dasar Pengakuan", "Kemungkinan (probability) manfaat masa depan",
             "Keberadaan hak hukum sekarang (present right)"],
            ["Konsep Kontrol", "Eksplisit sebagai bagian definisi",
             "Dihapus dari definisi; diatur di Chapter 5 (Recognition)"],
            ["Relevansi BC", "—",
             "BC4.7: 'present right' memberikan primasi konseptual pada hak hukum"],
        ],
    )

    # III.3 Comprehensive Income
    add_sub_heading(doc, "III.3 Comprehensive Income (CI) dan OCI: Hubungan Konseptual")
    add_body_paragraph(
        doc,
        "Comprehensive Income (CI) merupakan elemen yang paling luas mencakup seluruh perubahan "
        "ekuitas dari transaksi non-pemilik. CI terdiri dari: (1) Net Income — hasil aktivitas "
        "utama dan peripheral yang dilaporkan dalam Laporan Laba Rugi, dan (2) Other Comprehensive "
        "Income (OCI) — perubahan nilai yang belum direalisasi (unrealized gains/losses) yang "
        "dilaporkan terpisah. Contoh OCI: perubahan nilai investasi tersedia untuk dijual, "
        "translasi mata uang asing, dan re-measurement imbalan kerja."
    )
    add_body_paragraph(
        doc,
        "SFAC 8 Chapter 7, paragraf BC7.21, secara eksplisit menyatakan bahwa 'tidak terdapat "
        "basis konseptual yang jelas untuk pengklasifikasian item ke dalam OCI vs. Net Income.' "
        "Ini merupakan pengakuan FASB bahwa pemisahan OCI lebih bersifat pragmatis-politis "
        "ketimbang konseptual — entitas dan standar setter menggunakannya untuk menghindari "
        "volatilitas Laporan Laba Rugi dari perubahan nilai wajar jangka pendek."
    )

    # III.4 Aplikasi INDF — Goodwill
    add_sub_heading(doc, "III.4 Aplikasi di INDF 2024: Goodwill sebagai Aset Intangible")
    add_body_paragraph(
        doc,
        "PT Indofood Sukses Makmur Tbk mencatat Goodwill sebesar Rp52,2 triliun per "
        "31 Desember 2024, mewakili sekitar 26 persen dari total aset konsolidasi. "
        "Di bawah SFAC 6, Goodwill memenuhi definisi aset karena berasal dari transaksi masa "
        "lalu (akuisisi entitas anak) dan mengandung manfaat ekonomi masa depan yang diharapkan. "
        "Namun di bawah definisi SFAC 8 Ch.4, Goodwill dapat juga dipandang sebagai "
        "'present right' atas manfaat sinergistik yang diperoleh dari pengendalian entitas "
        "yang diakuisisi."
    )

    add_caption(doc, "Bagan 3.1 — Waterfall Comprehensive Income PT INDF 2024 (Rp Triliun, Ilustratif)")
    p_wf = doc.add_paragraph()
    p_wf.alignment = 1
    p_wf.add_run().add_picture(generate_bagan_ci_waterfall(), width=Inches(5.5))

    add_footnote_text(
        doc,
        "³ Catatan waterfall: nilai beban pokok dan beban operasi bersifat estimasi ilustratif "
        "— agent implementor harus memverifikasi angka aktual dari sumber: "
        "sources/indf-2024-ar.pdf. Goodwill Rp52,2T dan Net Sales Rp115,79T telah dikonfirmasi "
        "dari AR 2024. BC4.7 mengacu Basis for Conclusions SFAC 8 Ch.4 (Juli 2024)."
    )
```

- [ ] **Step 8.4: Run test**

```
pytest tests/test_word_doc.py::test_bagian_iii_contains_key_content -v
```
Expected: PASSED

- [ ] **Step 8.5: Commit**

```
git add scripts/word_doc/sections/bagian_iii.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement Bagian III — Elemen LK"
```

---

### Task 9: `bagian_iv.py` — Bagian IV: Pengakuan & Pengukuran

**Files:**
- Modify: `scripts/word_doc/sections/bagian_iv.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 9.1: Write failing test**

Append to `tests/test_word_doc.py`:
```python
def test_bagian_iv_contains_key_content():
    from docx import Document
    from scripts.word_doc.sections.bagian_iv import build
    doc = Document()
    build(doc)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "RD3" in text
    assert "M30" in text
    assert "Entry Price" in text
    assert "PR12" in text
    assert len(doc.tables) >= 2
```

- [ ] **Step 9.2: Run test (expect failure)**

```
pytest tests/test_word_doc.py::test_bagian_iv_contains_key_content -v
```

- [ ] **Step 9.3: Implement `scripts/word_doc/sections/bagian_iv.py`**

```python
from docx.shared import Inches
from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph,
    add_caption, add_table_with_headers, add_footnote_text,
)
from scripts.word_doc.visuals import generate_bagan_entry_exit_tree, generate_bagan_fs_hierarchy


def build(doc) -> None:
    """Bagian IV — Pengakuan dan Pengukuran"""

    add_section_heading(doc, "IV. PENGAKUAN DAN PENGUKURAN")

    # IV.1 SFAC 5
    add_sub_heading(doc, "IV.1 SFAC 5 (1984): Empat Kriteria Pengakuan dan Kritiknya")
    add_body_paragraph(
        doc,
        "SFAC 5 (1984) menetapkan empat kriteria untuk pengakuan suatu item dalam laporan "
        "keuangan: (1) item memenuhi definisi elemen laporan keuangan; (2) memiliki atribut "
        "yang dapat diukur dengan cukup andal; (3) informasinya relevan bagi pengguna; dan "
        "(4) informasinya dapat diandalkan (representasi tepat, dapat diverifikasi, netral). "
        "Selain itu, SFAC 5 mengidentifikasi lima atribut pengukuran yang dapat digunakan: "
        "Historical Cost, Current Replacement Cost, Current Market Value, Net Realizable Value, "
        "dan Present Value of Future Cash Flows."
    )
    add_body_paragraph(
        doc,
        "Namun para akademisi mengkritik SFAC 5 sebagai 'Achilles' heel of the FASB's conceptual "
        "framework' (Solomons, dikutip dalam Wolk, Dodd & Rozycki 2017, Ch.7). Kritik utama: "
        "SFAC 5 bersifat terlalu deskriptif dan permisif — ia mendeskripsikan praktik yang ada "
        "daripada menetapkan standar normatif yang jelas. Akibatnya, standar ini gagal "
        "memberikan panduan definitif kapan suatu item harus diakui vs. diungkapkan saja, "
        "menjadikannya sumber ambiguitas yang berkelanjutan dalam penetapan standar."
    )
    add_caption(doc, "Tabel 4.1 — Kriteria Pengakuan: SFAC 5 (1984) vs. SFAC 8 Chapter 5 (Juli 2024)")
    add_table_with_headers(
        doc,
        headers=["Kriteria", "SFAC 5 (1984)", "SFAC 8 Ch.5 (Juli 2024)"],
        rows_data=[
            ["Jumlah Kriteria", "4 kriteria", "3 kriteria (lebih sederhana)"],
            ["Kriteria 1", "Memenuhi definisi elemen LK",
             "Memenuhi definisi elemen LK (sama)"],
            ["Kriteria 2", "Dapat diukur dengan atribut relevan yang andal",
             "Informasi relevan dan tersedia (terkait benefit vs. cost)"],
            ["Kriteria 3", "Relevansi — mempengaruhi keputusan pengguna",
             "Faithful representation — merepresentasikan realitas ekonomi"],
            ["Kriteria 4 (SFAC 5 saja)", "Reliability — dapat diukur andal",
             "Tidak ada — telah disederhanakan"],
            ["Prinsip Utama", "Recognition = memenuhi 4 kriteria",
             "RD3: Recognition = 'words + numbers' dalam LK formal"],
            ["Disclosure vs. Recognition", "Tidak dibedakan secara tegas",
             "PR12: Notes ≠ Recognition (tidak dapat menggantikan pengakuan formal)"],
        ],
    )

    # IV.2 SFAC 8 Ch.5
    add_sub_heading(doc, "IV.2 SFAC 8 Chapter 5 (Juli 2024): RD3 dan Prinsip Recognition")
    add_body_paragraph(
        doc,
        "SFAC 8 Chapter 5 (Juli 2024) menyederhanakan kerangka pengakuan menjadi tiga kriteria "
        "dan memperkenalkan Recognized Definition 3 (RD3): sebuah item diakui ketika informasi "
        "tentang item tersebut menghasilkan manfaat yang melebihi biaya penyajiannya, baik "
        "dalam Laporan Posisi Keuangan maupun Laporan Kinerja Keuangan. Implikasi RD3 adalah "
        "bahwa pengakuan (recognition) selalu melibatkan representasi ganda: dalam kata-kata "
        "(label dalam laporan) dan dalam angka (nilai terukur). Ini secara eksplisit membedakan "
        "recognition dari mere disclosure."
    )

    # IV.3 SFAC 8 Ch.6 — Pengukuran
    add_sub_heading(doc, "IV.3 SFAC 8 Chapter 6 (Juli 2024): Dua Sistem Pengukuran")
    add_body_paragraph(
        doc,
        "SFAC 8 Chapter 6 (Juli 2024) mengorganisasi atribut pengukuran ke dalam dua sistem "
        "yang berbeda secara konseptual: Entry Price (harga masuk) dan Exit Price (harga keluar). "
        "Entry Price mencerminkan perspektif akuisisi — berapa yang dibayarkan untuk memperoleh "
        "aset atau menerima liabilitas — mencakup Historical Cost, Current Replacement Cost, "
        "dan Value in Use (untuk aset). Exit Price mencerminkan perspektif pasar — berapa yang "
        "akan diterima jika aset dijual atau dibayarkan untuk menyelesaikan liabilitas — "
        "mencakup Fair Value (IFRS 13) dan Net Realizable Value."
    )
    add_body_paragraph(
        doc,
        "Paragraf M30–M34 SFAC 8 Ch.6 memberikan panduan pemilihan basis pengukuran: ketika "
        "suatu aset atau liabilitas memiliki harga pasar yang unik (unique market price) — "
        "artinya harga tersebut spesifik untuk situasi entitas — maka Entry Price lebih tepat "
        "digunakan. Sebaliknya, ketika harga tidak unik (non-unique), artinya aset/liabilitas "
        "dapat diperdagangkan di pasar yang aktif dan transparan, Exit Price (Fair Value) "
        "menjadi basis yang lebih representatif."
    )
    add_caption(doc, "Tabel 4.2 — Lima Atribut Pengukuran SFAC 5 dan Pemetaan ke SFAC 8 Ch.6")
    add_table_with_headers(
        doc,
        headers=["Atribut (SFAC 5)", "Sistem (SFAC 8 Ch.6)", "Contoh Aplikasi di INDF"],
        rows_data=[
            ["Historical Cost", "Entry Price", "Aset tetap (pabrik Bogasari, mesin CPO)"],
            ["Current Replacement Cost", "Entry Price", "Persediaan bahan baku (terigu, CPO)"],
            ["Net Realizable Value (entry)", "Entry Price",
             "Persediaan barang jadi (mi instan siap jual)"],
            ["Fair Value / Market Value", "Exit Price",
             "Aset keuangan diperdagangkan, investasi"],
            ["Present Value of Future CF", "Exit Price",
             "Goodwill impairment test (discounted CF)"],
        ],
    )

    add_caption(doc, "Bagan 4.1 — Pohon Keputusan Basis Pengukuran (SFAC 8 Ch.6, M30–M34)")
    p_tree = doc.add_paragraph()
    p_tree.alignment = 1
    p_tree.add_run().add_picture(generate_bagan_entry_exit_tree(), width=Inches(5.5))

    # IV.4 SFAC 8 Ch.7 — Penyajian
    add_sub_heading(doc, "IV.4 SFAC 8 Chapter 7 (Juli 2024): Penyajian dan Hierarki LK")
    add_body_paragraph(
        doc,
        "SFAC 8 Chapter 7 mengatur prinsip penyajian informasi dalam laporan keuangan. "
        "Prinsip kunci PR12 menegaskan: 'Notes to financial statements cannot substitute for "
        "recognition.' Catatan kaki (notes) hanya berfungsi sebagai suplemen penjelasan — "
        "bukan pengganti pengakuan formal yang memerlukan words + numbers dalam laporan utama. "
        "Implikasinya bagi praktik: entitas tidak dapat menghindari pengakuan suatu kewajiban "
        "dengan cara mengungkapkannya hanya dalam catatan kaki."
    )
    add_body_paragraph(
        doc,
        "Paragraf BC7.21 menyatakan bahwa 'tidak terdapat basis konseptual yang jelas untuk "
        "memisahkan item ke dalam Other Comprehensive Income (OCI) versus Net Income.' "
        "FASB mengakui bahwa pemisahan OCI lebih bersifat pragmatis dan historis, bukan "
        "merupakan prinsip konseptual yang koheren. Ini menjelaskan mengapa banyak analis "
        "keuangan menggunakan Total Comprehensive Income (bukan Net Income saja) sebagai "
        "ukuran kinerja yang lebih komprehensif."
    )
    add_caption(doc, "Bagan 4.2 — Hierarki Laporan Keuangan: SFAC 8 Ch.7")
    p_hier = doc.add_paragraph()
    p_hier.alignment = 1
    p_hier.add_run().add_picture(generate_bagan_fs_hierarchy(), width=Inches(4.5))

    add_footnote_text(
        doc,
        "⁴ RD3 = Recognized Definition 3, SFAC 8 Ch.5. M30–M34 = paragraf pengukuran "
        "SFAC 8 Ch.6. PR12 = paragraf penyajian SFAC 8 Ch.7. BC7.21 = Basis for Conclusions "
        "SFAC 8 Ch.7. Sumber: SFAC 8 (September 2024); Wolk et al. (2017) Ch.7."
    )
```

- [ ] **Step 9.4: Run test**

```
pytest tests/test_word_doc.py::test_bagian_iv_contains_key_content -v
```
Expected: PASSED

- [ ] **Step 9.5: Commit**

```
git add scripts/word_doc/sections/bagian_iv.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement Bagian IV — Pengakuan & Pengukuran"
```

---

### Task 10: `bagian_v.py` + `bagian_vi.py` — Catatan Kritis & Sintesis

**Files:**
- Modify: `scripts/word_doc/sections/bagian_v.py`
- Modify: `scripts/word_doc/sections/bagian_vi.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 10.1: Write failing tests**

Append to `tests/test_word_doc.py`:
```python
def test_bagian_v_contains_key_content():
    from docx import Document
    from scripts.word_doc.sections.bagian_v import build
    doc = Document()
    build(doc)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "Achilles" in text
    assert "pro-cyclicality" in text or "pro-siklikalitas" in text


def test_bagian_vi_contains_key_content():
    from docx import Document
    from scripts.word_doc.sections.bagian_vi import build
    doc = Document()
    build(doc)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "Chapter 8" in text or "Catatan" in text
    assert len(doc.tables) >= 1
```

- [ ] **Step 10.2: Run tests (expect failures)**

```
pytest tests/test_word_doc.py -k "test_bagian_v or test_bagian_vi" -v
```

- [ ] **Step 10.3: Implement `scripts/word_doc/sections/bagian_v.py`**

```python
from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph, add_footnote_text,
)


def build(doc) -> None:
    """Bagian V — Catatan Kritis dan Perspektif Akademis"""

    add_section_heading(doc, "V. CATATAN KRITIS DAN PERSPEKTIF AKADEMIS")

    # V.1 SFAC 5 Critique
    add_sub_heading(doc, "V.1 SFAC 5 sebagai 'Achilles' Heel': Kritik Solomons")
    add_body_paragraph(
        doc,
        "David Solomons, salah satu arsitek intelektual kerangka konseptual FASB, pada akhirnya "
        "menyebut SFAC 5 sebagai 'Achilles' heel of the FASB's conceptual framework' — sebuah "
        "kritik yang dikutip secara luas oleh Wolk, Dodd & Rozycki (2017, Ch.7). Solomons "
        "berargumen bahwa SFAC 5 pada dasarnya merupakan 'cop-out' — sebuah dokumen yang "
        "mendeskripsikan apa yang sudah dilakukan praktisi, bukan menetapkan apa yang seharusnya "
        "dilakukan. Akibatnya, kerangka konseptual yang seharusnya memberikan panduan normatif "
        "untuk penetapan standar justru menjadi cermin deskriptif dari status quo."
    )
    add_body_paragraph(
        doc,
        "Respons FASB terhadap kritik ini terlihat dalam SFAC 8 Chapter 5 yang memperkenalkan "
        "prinsip cost-benefit sebagai pertimbangan utama dalam pengakuan — sebuah pendekatan "
        "yang lebih normatif. Namun demikian, SFAC 5 tetap berlaku hingga hari ini dan menjadi "
        "referensi bagi standar akuntansi AS yang ada, menciptakan ketegangan antara framework "
        "baru (SFAC 8) dan standar lama yang masih mengacu SFAC 5."
    )

    # V.2 Fair Value Debate
    add_sub_heading(doc, "V.2 Perdebatan Fair Value: Relevansi vs. Reliabilitas dalam Praktik")
    add_body_paragraph(
        doc,
        "Perdebatan tentang Fair Value (nilai wajar) mencerminkan ketegangan abadi antara dua "
        "karakteristik kualitatif: Relevansi dan Faithful Representation. Pendukung Fair Value "
        "berargumen bahwa nilai pasar kini lebih relevan bagi investor karena mencerminkan "
        "kondisi ekonomi terkini, bukan biaya historis yang mungkin sudah usang. Namun "
        "para kritikus mengidentifikasi risiko pro-siklikalitas (pro-cyclicality): pada periode "
        "krisis keuangan, penurunan Fair Value memaksa pengakuan kerugian yang memperbesar "
        "tekanan pada lembaga keuangan, menciptakan spiral negatif yang memperburuk krisis "
        "(bank run → asset write-down → capital shortfall → lebih banyak write-down)."
    )

    # V.3 Konservatisme
    add_sub_heading(doc, "V.3 Penghapusan Konservatisme: Implikasi untuk Praktik")
    add_body_paragraph(
        doc,
        "Penghapusan Conservatism dari SFAC 8 (BC3.27–29) merupakan keputusan yang paling "
        "kontroversial dalam sejarah kerangka konseptual FASB. Konservatisme tradisional — "
        "'anticipate no profits, but anticipate all losses' — telah menjadi panduan praktis "
        "akuntansi selama berabad-abad. FASB berargumen bahwa konservatisme sistematis "
        "bertentangan dengan Neutrality (salah satu komponen Faithful Representation) "
        "karena ia mendorong bias ke arah under-statement aset. Namun sejumlah akademisi "
        "mempertanyakan apakah Neutrality tanpa konservatisme justru membuka ruang yang lebih "
        "besar bagi manajemen untuk melakukan income smoothing dan overstatement aset."
    )

    # V.4 Implikasi Indonesia
    add_sub_heading(doc, "V.4 Implikasi untuk Standard Setter Indonesia")
    add_body_paragraph(
        doc,
        "DSAK-IAI, sebagai adopter IASB CF 2018, mewarisi sekaligus ketegangan-ketegangan "
        "konseptual yang belum sepenuhnya terselesaikan dalam SFAC 8. Tantangan spesifik untuk "
        "konteks Indonesia meliputi: (1) keterbatasan pasar aktif untuk pengukuran Fair Value "
        "aset tertentu, yang mengurangi reliabilitas Exit Price; (2) kompleksitas struktur "
        "konglomerat (seperti INDF dengan empat divisi utama) dalam pengujian impairment "
        "Goodwill; dan (3) ketegangan antara kebutuhan konservatisme untuk perlindungan "
        "kreditur dan tuntutan Neutrality dari kerangka konseptual modern."
    )

    add_footnote_text(
        doc,
        "⁵ Kutipan 'Achilles' heel' dan 'cop-out': Wolk, Dodd & Rozycki (2017), "
        "Accounting Theory: Conceptual Issues in a Political and Economic Environment, "
        "Ch.7, hal. 175. Pro-cyclicality Fair Value: lihat Plantin, Sapra & Shin (2008); "
        "Allen & Carletti (2008)."
    )
```

- [ ] **Step 10.4: Implement `scripts/word_doc/sections/bagian_vi.py`**

```python
from docx.shared import Inches
from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph,
    add_caption, add_table_with_headers, add_footnote_text,
)
from scripts.word_doc.visuals import generate_bagan_fasb_to_psak


def build(doc) -> None:
    """Bagian VI — Sintesis Teori: SFAC 8 Keseluruhan"""

    add_section_heading(doc, "VI. SINTESIS TEORI: SFAC 8 SEBAGAI KERANGKA KONSEPTUAL KOMPREHENSIF")

    add_sub_heading(doc, "VI.1 Peta Delapan Chapters SFAC 8 (September 2024)")
    add_body_paragraph(
        doc,
        "SFAC 8 edisi September 2024 merupakan konsolidasi menyeluruh dari kerangka konseptual "
        "FASB dalam satu dokumen terpadu dengan delapan chapter. Setiap chapter menangani "
        "lapisan konseptual yang berbeda — dari tujuan paling mendasar (Chapter 1) hingga "
        "peran catatan keuangan (Chapter 8) — membentuk arsitektur hierarkis yang koheren."
    )
    add_caption(doc, "Tabel 5.1 — Delapan Chapters SFAC 8 (September 2024): Ringkasan")
    add_table_with_headers(
        doc,
        headers=["Ch.", "Judul", "Tanggal", "Isi Pokok"],
        rows_data=[
            ["1", "The Objective of General Purpose Financial Reporting",
             "2010", "Tujuan GPFR; primary users; stewardship"],
            ["2", "The Reporting Entity", "2018",
             "Definisi entitas pelaporan; batas konsolidasi"],
            ["3", "Qualitative Characteristics of Useful Financial Information",
             "2010", "QC Fundamental (Relevansi + FR) + Enhancing"],
            ["4", "Elements of Financial Statements", "Juli 2024",
             "Definisi 10 elemen; aset = 'present right'; BC4.7"],
            ["5", "Recognition and Derecognition", "Juli 2024",
             "3 kriteria pengakuan; RD3; Disclosure ≠ Recognition"],
            ["6", "Measurement", "Juli 2024",
             "Entry Price vs. Exit Price; M30–M34 decision guidance"],
            ["7", "Presentation and Disclosure", "Juli 2024",
             "PR12: Notes ≠ Recognition; BC7.21: basis OCI tidak jelas"],
            ["8", "Notes to Financial Statements", "Agustus 2023",
             "Fungsi catatan; 4 limitasi; D32 adverse consequences"],
        ],
    )

    add_sub_heading(doc, "VI.2 Jalur Pengaruh: FASB → IASB → PSAK → Praktik INDF")
    add_body_paragraph(
        doc,
        "Pemahaman SFAC 8 FASB secara langsung relevan bagi entitas Indonesia karena "
        "terdapat jalur pengaruh yang linear: (1) SFAC 8 FASB menjadi basis dialog konvergensi "
        "dalam Norwalk Agreement 2002; (2) konvergensi tersebut menghasilkan IASB Conceptual "
        "Framework for Financial Reporting 2018 yang selaras dengan SFAC 8; (3) DSAK-IAI "
        "mengadopsi IASB CF 2018 menjadi KKPK (Kerangka Konseptual Pelaporan Keuangan) IAI; "
        "(4) seluruh PSAK berbasis IFRS yang diterbitkan DSAK-IAI berlandaskan pada KKPK "
        "tersebut; dan (5) PT Indofood Sukses Makmur Tbk menyusun laporan keuangan "
        "konsolidasinya berdasarkan PSAK — merupakan manifestasi akhir dari rantai pengaruh ini."
    )
    add_caption(doc, "Bagan 5.1 — Jalur Pengaruh: FASB CF → IASB → PSAK → Praktik PT INDF")
    p_flow = doc.add_paragraph()
    p_flow.alignment = 1
    p_flow.add_run().add_picture(generate_bagan_fasb_to_psak(), width=Inches(5.8))

    add_footnote_text(
        doc,
        "⁶ KKPK = Kerangka Konseptual Pelaporan Keuangan, DSAK-IAI 2022 (adopsi IASB CF 2018). "
        "SFAC 8 September 2024 tersedia di fasb.org. Sumber: Wolk et al. (2017) Ch.7."
    )
```

- [ ] **Step 10.5: Run tests**

```
pytest tests/test_word_doc.py -k "test_bagian_v or test_bagian_vi" -v
```
Expected: 2 PASSED

- [ ] **Step 10.6: Commit**

```
git add scripts/word_doc/sections/bagian_v.py scripts/word_doc/sections/bagian_vi.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement Bagian V (Catatan Kritis) dan Bagian VI (Sintesis)"
```

---

### Task 11: `bagian_vii.py` — Bagian VII: Studi Kasus INDF 2024

**Files:**
- Modify: `scripts/word_doc/sections/bagian_vii.py`
- Modify: `tests/test_word_doc.py`

This is the largest section (~12–16 pages). It covers all 10 INDF sub-sections.

- [ ] **Step 11.1: Write failing test**

Append to `tests/test_word_doc.py`:
```python
def test_bagian_vii_contains_key_content():
    from docx import Document
    from scripts.word_doc.sections.bagian_vii import build
    doc = Document()
    build(doc)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "115,79" in text or "115.79" in text   # Net Sales
    assert "52,2" in text or "52.2" in text        # Goodwill
    assert "First Pacific" in text
    assert "43,077" in text or "43.077" in text    # NCI
    assert len(doc.tables) >= 4
    assert len(doc.inline_shapes) >= 3             # org, pie, matrix
```

- [ ] **Step 11.2: Run test (expect failure)**

```
pytest tests/test_word_doc.py::test_bagian_vii_contains_key_content -v
```

- [ ] **Step 11.3: Implement `scripts/word_doc/sections/bagian_vii.py`**

```python
from docx.shared import Inches
from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph,
    add_caption, add_table_with_headers, add_footnote_text,
)
from scripts.word_doc.visuals import (
    generate_bagan_indf_org, generate_bagan_kepemilikan_pie,
    generate_bagan_matrix_relevance_fr,
)


def build(doc) -> None:
    """Bagian VII — Studi Kasus: PT Indofood Sukses Makmur Tbk (INDF) 2024"""

    add_section_heading(
        doc,
        "VII. STUDI KASUS: PT INDOFOOD SUKSES MAKMUR TBK (INDF) 2024"
    )

    # VII.1 Profil Perusahaan
    add_sub_heading(doc, "VII.1 Profil Perusahaan: Struktur Konglomerat INDF")
    add_body_paragraph(
        doc,
        "PT Indofood Sukses Makmur Tbk (INDF) merupakan salah satu perusahaan makanan terbesar "
        "di Asia Tenggara dengan struktur konglomerat yang terdiri dari empat divisi utama: "
        "Bogasari (penggilingan terigu), Agribisnis (kelapa sawit dan karet), Consumer Branded "
        "Products/CBP (terutama melalui PT Indofood CBP Sukses Makmur Tbk/ICBP yang memproduksi "
        "mi instan Indomie), dan Distribusi. Kerumitan struktur ini — dengan entitas induk, "
        "entitas anak yang tercatat di bursa (ICBP), dan kepentingan nonpengendali yang "
        "substansial — menjadikan INDF sebagai kasus studi yang kaya untuk aplikasi kerangka "
        "konseptual FASB."
    )
    add_body_paragraph(
        doc,
        "Per 31 Desember 2024, INDF mencatat pendapatan bersih (net sales) sebesar "
        "Rp115,79 triliun. Pemegang saham pengendali utama adalah First Pacific Limited, "
        "sebuah perusahaan investasi yang berkantor pusat di Hong Kong, dengan kepemilikan "
        "sebesar 50,07 persen. Laporan keuangan konsolidasi INDF 2024 diaudit oleh "
        "Kantor Akuntan Publik Purwantono, Sungkoro & Surja — anggota Ernst & Young Global."
    )
    add_caption(doc, "Bagan 6.1 — Struktur Konglomerat dan Angka Kunci PT INDF (2024)")
    p_org = doc.add_paragraph()
    p_org.alignment = 1
    p_org.add_run().add_picture(generate_bagan_indf_org(), width=Inches(5.8))

    add_caption(doc, "Bagan 6.2 — Struktur Kepemilikan PT INDF per 31 Desember 2024")
    p_pie = doc.add_paragraph()
    p_pie.alignment = 1
    p_pie.add_run().add_picture(generate_bagan_kepemilikan_pie(), width=Inches(4.0))

    # VII.2 Primary Users di INDF
    add_sub_heading(doc, "VII.2 Identifikasi Primary Users: Konteks INDF")
    add_body_paragraph(
        doc,
        "Menerapkan konsep primary users (SFAC 8 Ch.1) pada INDF menghasilkan identifikasi "
        "yang spesifik. Primary users utama INDF adalah: (1) First Pacific Ltd. sebagai "
        "pemegang saham pengendali yang memonitor kinerja dan nilai investasinya; "
        "(2) investor publik dan institusional pemegang saham minoritas yang bergantung pada "
        "GPFS untuk keputusan beli/jual/tahan; (3) pemegang obligasi dan bank kreditur INDF "
        "yang menilai kemampuan pembayaran utang; dan (4) pemegang kepentingan nonpengendali "
        "(Non-Controlling Interest/NCI) sebesar Rp43,077 triliun yang merupakan pemegang "
        "saham minoritas di entitas anak INDF (terutama ICBP)."
    )

    # VII.3 Relevansi
    add_sub_heading(doc, "VII.3 Relevansi Informasi Keuangan INDF")
    add_body_paragraph(
        doc,
        "Informasi keuangan INDF mendemonstrasikan dua dimensi relevansi SFAC 8 secara "
        "bersamaan. Dari sisi Predictive Value: tren EPS 2020–2024 (Rp735 → Rp873 → Rp724 "
        "→ Rp928 → Rp984) memberikan basis bagi analis untuk memproyeksikan profitabilitas "
        "masa depan — tren kenaikan jangka panjang dengan volatilitas 2022 yang dapat "
        "dijelaskan oleh kenaikan harga komoditas (CPO, terigu). Dari sisi Confirmatory Value: "
        "Net Sales Rp115,79 triliun 2024 mengkonfirmasi proyeksi analis mengenai pemulihan "
        "volume penjualan pasca-pandemi dan normalisasi harga bahan baku."
    )

    # VII.4 Faithful Representation
    add_sub_heading(doc, "VII.4 Faithful Representation dalam Laporan Konsolidasi INDF")
    add_body_paragraph(
        doc,
        "Tantangan Faithful Representation yang paling kompleks di INDF berkaitan dengan "
        "konsolidasi laporan keuangan empat divisi dengan model bisnis yang berbeda: "
        "penggilingan terigu (Bogasari, margin relatif stabil), perkebunan (Agribisnis, "
        "sangat terpengaruh harga komoditas), consumer goods (CBP/ICBP, margin konsisten "
        "tinggi), dan distribusi. Kerangka SFAC 8 mensyaratkan bahwa laporan konsolidasi "
        "merepresentasikan realitas ekonomi group secara keseluruhan, termasuk dampak "
        "kepentingan nonpengendali."
    )
    add_body_paragraph(
        doc,
        "NCI sebesar Rp43,077 triliun mencerminkan kepentingan pemegang saham minoritas "
        "entitas anak (terutama ICBP) yang tidak dikendalikan INDF. Penyajian NCI secara "
        "terpisah dalam laporan konsolidasi — sesuai PSAK 65 dan SFAC 8 Ch.7 — merupakan "
        "implementasi Faithful Representation: pembaca laporan dapat memahami bahwa bagian "
        "substansial ekuitas bukan milik pemegang saham INDF (parent)."
    )

    # VII.5 Goodwill / Aset
    add_sub_heading(doc, "VII.5 Aset dan Goodwill: Implikasi Definisi SFAC 8 Ch.4")
    add_body_paragraph(
        doc,
        "Goodwill INDF sebesar Rp52,2 triliun (sekitar 26 persen dari total aset konsolidasi) "
        "merupakan salah satu Goodwill terbesar di antara emiten Indonesia. Goodwill ini "
        "muncul terutama dari akuisisi Bogasari dan berbagai entitas anak lainnya. "
        "Di bawah definisi SFAC 8 Ch.4, Goodwill merupakan 'present right' atas manfaat "
        "sinergistik yang diperoleh dari pengendalian entitas yang diakuisisi — sebuah "
        "interpretasi yang lebih kuat dari basis konseptual Goodwill dibandingkan SFAC 6."
    )
    add_caption(doc, "Tabel 6.1 — Pengujian Penurunan Nilai (Impairment Test) Goodwill INDF 2024")
    add_table_with_headers(
        doc,
        headers=["Unit Penghasil Kas (UPK)", "Nilai Tercatat (Rp T)", "Metode Uji", "Indikasi"],
        rows_data=[
            ["Bogasari (Tepung Terigu)", "[lihat AR 2024]", "Value in Use (DCF)",
             "[lihat AR 2024]"],
            ["Agribisnis (CPO & Karet)", "[lihat AR 2024]", "Value in Use (DCF)",
             "[lihat AR 2024]"],
            ["CBP / ICBP (Mi Instan)", "[lihat AR 2024]", "Value in Use (DCF)",
             "[lihat AR 2024]"],
            ["Total Goodwill INDF", "Rp 52,2 T", "Berbasis DCF", "Tidak ada penurunan nilai 2024"],
        ],
    )
    add_body_paragraph(
        doc,
        "Catatan kepada implementor: Isi nilai tercatat per UPK di atas harus diverifikasi dari "
        "Catatan atas Laporan Keuangan INDF 2024 (sources/indf-2024-ar.pdf). Kolom 'Indikasi' "
        "juga harus diverifikasi dari laporan audit."
    )

    # VII.6 Liabilitas & Ekuitas
    add_sub_heading(doc, "VII.6 Liabilitas dan Ekuitas: Klasifikasi NCI")
    add_body_paragraph(
        doc,
        "Salah satu isu klasifikasi yang relevan di INDF adalah apakah kepentingan "
        "nonpengendali (NCI) harus diklasifikasikan sebagai Ekuitas atau sebagai suatu bentuk "
        "Liabilitas. Kerangka konseptual SFAC 8 Ch.4 — sejalan dengan PSAK 65 — menempatkan "
        "NCI sebagai bagian dari Ekuitas konsolidasi (bukan liabilitas), karena NCI merupakan "
        "residual interest pemegang saham minoritas entitas anak, bukan kewajiban kontraktual "
        "entitas induk. NCI INDF sebesar Rp43,077 triliun dilaporkan sebagai bagian Ekuitas "
        "dalam Laporan Posisi Keuangan konsolidasi."
    )

    # VII.7 Pengakuan
    add_sub_heading(doc, "VII.7 Pengakuan di INDF: Tiga Kriteria SFAC 8 Ch.5")
    add_body_paragraph(
        doc,
        "Menerapkan tiga kriteria pengakuan SFAC 8 Ch.5 pada item-item laporan keuangan INDF "
        "menghasilkan penilaian sebagai berikut. Pendapatan (Revenue) memenuhi ketiga kriteria: "
        "definisi elemen terpenuhi (pendapatan dari penjualan barang), informasi relevan "
        "(prediktif arus kas masa depan), dan representasi tepat (pendapatan direalisasi dari "
        "transaksi aktual dengan pihak ketiga). Goodwill memenuhi kriteria definisi (present "
        "right atas sinergi) dan relevansi, namun representasi tepatnya lebih dipertanyakan "
        "karena nilai Goodwill sangat bergantung pada asumsi DCF yang subjektif."
    )

    # VII.8 Pengukuran
    add_sub_heading(doc, "VII.8 Pengukuran di INDF: Pemetaan Entry vs. Exit Price")
    add_caption(doc, "Tabel 6.2 — Peta Basis Pengukuran Item LK INDF 2024 (SFAC 8 Ch.6)")
    add_table_with_headers(
        doc,
        headers=["Item LK", "Basis Pengukuran", "Sistem", "Referensi SFAC 8 Ch.6"],
        rows_data=[
            ["Aset Tetap (mesin, pabrik)", "Historical Cost — net of depreciation",
             "Entry Price", "M30: harga unik"],
            ["Goodwill", "Cost less accumulated impairment",
             "Entry Price", "M30: tidak ada pasar aktif"],
            ["Persediaan (terigu, CPO)", "Cost atau NRV, yang lebih rendah",
             "Entry Price", "M31: replacement cost"],
            ["Investasi efek diperdagangkan", "Fair Value (IFRS 13)",
             "Exit Price", "M34: harga tidak unik"],
            ["Piutang usaha", "Amortized Cost",
             "Entry Price", "M30: nilai khusus entitas"],
            ["Liabilitas keuangan jangka panjang", "Amortized Cost (EIR)",
             "Entry Price", "M30: harga khusus pada originasi"],
            ["Aset Biologis (kelapa sawit)", "Fair Value less cost to sell",
             "Exit Price", "M34: pasar komoditas aktif"],
        ],
    )

    # VII.9 Penyajian
    add_sub_heading(doc, "VII.9 Penyajian (Presentation): SFAC 8 Ch.7 di Laporan INDF")
    add_body_paragraph(
        doc,
        "Laporan keuangan konsolidasi INDF 2024 menyajikan komponen utama sesuai dengan "
        "hierarki penyajian SFAC 8 Ch.7: Laporan Posisi Keuangan, Laporan Laba Rugi dan "
        "Penghasilan Komprehensif Lain (yang memisahkan Net Income dari OCI), Laporan Arus Kas, "
        "Laporan Perubahan Ekuitas, dan Catatan atas Laporan Keuangan. Penerapan PR12 "
        "(Notes ≠ Recognition) terlihat dalam cara INDF mengakui kewajiban imbalan kerja "
        "(PSAK 24) langsung dalam laporan keuangan, bukan hanya dalam catatan — suatu praktik "
        "yang selaras dengan prinsip bahwa pengakuan formal tidak dapat digantikan oleh "
        "pengungkapan semata."
    )

    # VII.10 Catatan (Notes)
    add_sub_heading(doc, "VII.10 Catatan atas LK: Empat Limitasi dan D32 di Konteks INDF")
    add_body_paragraph(
        doc,
        "SFAC 8 Chapter 8 (Agustus 2023) mengidentifikasi empat limitasi inherent dari catatan "
        "atas laporan keuangan: (1) catatan tidak dapat menggantikan pengakuan; (2) catatan "
        "dapat menjadi terlalu panjang sehingga mengurangi kegunaan (information overload); "
        "(3) beberapa informasi dalam catatan mungkin terlalu sensitif untuk diungkapkan secara "
        "penuh (D32: adverse consequences); dan (4) catatan kurang terstandarisasi "
        "dibandingkan laporan utama. Catatan atas LK INDF 2024 mencakup lebih dari 60 "
        "item pengungkapan — termasuk penjelasan Goodwill, analisis sensitivitas DCF, "
        "dan transaksi pihak berelasi — yang relevan dengan limitasi (2) di atas."
    )
    add_caption(doc, "Tabel 6.3 — Penilaian Disclosure INDF 2024 vs. Standar SFAC 8 Ch.8")
    add_table_with_headers(
        doc,
        headers=["Area Disclosure", "Standar SFAC 8 Ch.8", "Praktik INDF 2024", "Penilaian"],
        rows_data=[
            ["Goodwill — basis pengukuran", "Wajib diungkapkan metode & asumsi",
             "Diungkapkan di Catatan (DCF, WACC)", "Sesuai"],
            ["NCI — komposisi kepemilikan", "Wajib diungkapkan terpisah",
             "Diungkapkan di Neraca & Catatan", "Sesuai"],
            ["Risiko keuangan (FX, bunga)", "Wajib kuantitatif (IFRS 7)",
             "Analisis sensitivitas tersedia", "Sesuai"],
            ["Transaksi pihak berelasi", "Wajib diungkapkan nilai & syarat",
             "Tersedia di Catatan", "Sesuai"],
            ["Asumsi DCF impairment test", "Wajib — namun rentan D32",
             "Sebagian diungkapkan (range WACC)",
             "Parsial — potensi information gap"],
        ],
    )

    add_caption(doc, "Bagan 6.3 — Matrix Relevansi × Faithful Representation: Item LK INDF 2024")
    p_mat = doc.add_paragraph()
    p_mat.alignment = 1
    p_mat.add_run().add_picture(generate_bagan_matrix_relevance_fr(), width=Inches(5.0))

    add_footnote_text(
        doc,
        "⁷ Semua angka INDF (Net Sales Rp115,79T; Goodwill Rp52,2T; NCI Rp43,077T; "
        "EPS 2024 Rp984) bersumber dari Annual Report PT Indofood Sukses Makmur Tbk 2024 "
        "(sources/indf-2024-ar.pdf). Nilai per UPK Goodwill dalam Tabel 6.1 harus diverifikasi "
        "implementor dari halaman Catatan LK yang relevan. "
        "D32 = paragraf D32, SFAC 8 Ch.8 (Agustus 2023) — 'Adverse Consequences of Disclosure.'"
    )
```

- [ ] **Step 11.4: Run test**

```
pytest tests/test_word_doc.py::test_bagian_vii_contains_key_content -v
```
Expected: PASSED

- [ ] **Step 11.5: Commit**

```
git add scripts/word_doc/sections/bagian_vii.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement Bagian VII — Studi Kasus INDF 2024"
```

---

### Task 12: `bagian_viii.py` + `bibliography.py`

**Files:**
- Modify: `scripts/word_doc/sections/bagian_viii.py`
- Modify: `scripts/word_doc/bibliography.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 12.1: Write failing tests**

Append to `tests/test_word_doc.py`:
```python
def test_bagian_viii_contains_conclusion():
    from docx import Document
    from scripts.word_doc.sections.bagian_viii import build
    doc = Document()
    build(doc)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "Kesimpulan" in text or "KESIMPULAN" in text
    assert "DSAK" in text or "OJK" in text


def test_bibliography_parses_txt_file():
    import os
    from docx import Document
    from scripts.word_doc.bibliography import build_bibliography
    txt_path = os.path.join(
        os.path.dirname(__file__), "..",
        "Daftar Pustaka — Presentasi Kelompok 3.txt"
    )
    doc = Document()
    build_bibliography(doc, txt_path)
    text = "\n".join(p.text for p in doc.paragraphs)
    assert "Daftar Pustaka" in text or "DAFTAR PUSTAKA" in text
    # At least some reference entries should be present
    assert len([p for p in doc.paragraphs if p.text.strip()]) > 5
```

- [ ] **Step 12.2: Run tests (expect failures)**

```
pytest tests/test_word_doc.py -k "test_bagian_viii or test_bibliography" -v
```

- [ ] **Step 12.3: Implement `scripts/word_doc/sections/bagian_viii.py`**

```python
from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph, add_footnote_text,
)


def build(doc) -> None:
    """Bagian VIII — Kesimpulan"""

    add_section_heading(doc, "VIII. KESIMPULAN")

    add_sub_heading(doc, "VIII.1 Sintesis: CF sebagai Fondasi Hierarki Standar → Praktik")
    add_body_paragraph(
        doc,
        "Kerangka Konseptual FASB — dalam manifestasinya yang paling mutakhir sebagai SFAC 8 "
        "edisi September 2024 — membuktikan dirinya sebagai fondasi arsitektur yang koheren "
        "dan berjenjang bagi seluruh standar akuntansi modern. Perjalanan dari SFAC 1 (1978) "
        "yang menetapkan tujuan pelaporan keuangan, hingga SFAC 8 September 2024 yang "
        "merevisi definisi aset, kriteria pengakuan, dan panduan pengukuran, mencerminkan "
        "evolusi pemikiran akuntansi yang responsif terhadap kritik akademisi dan tuntutan "
        "praktik pasar global."
    )
    add_body_paragraph(
        doc,
        "Empat perubahan konseptual paling signifikan dalam evolusi ini — (1) pergantian "
        "Reliability dengan Faithful Representation, (2) penurunan status Verifiability, "
        "(3) penghapusan Conservatism, dan (4) redefinisi aset menjadi 'present right' — "
        "secara konsisten menunjukkan arah yang sama: dari orientasi objektivitas-verifikasi "
        "menuju orientasi representasi-realitas-ekonomi. SFAC 8 menempatkan relevansi "
        "ekonomi di atas kemudahan audit, sebuah pilihan konseptual yang terus diperdebatkan "
        "dalam literatur akademik."
    )

    add_sub_heading(doc, "VIII.2 INDF 2024 sebagai Cerminan Teori: Keselarasan dan Gap")
    add_body_paragraph(
        doc,
        "Laporan keuangan PT Indofood Sukses Makmur Tbk 2024 mendemonstrasikan implementasi "
        "kerangka konseptual yang umumnya baik: penyajian NCI yang transparan, pengukuran "
        "aset tetap berbasis Historical Cost (Entry Price) yang konsisten dengan M30, "
        "pengakuan pendapatan yang memenuhi tiga kriteria SFAC 8 Ch.5, dan disclosure Goodwill "
        "yang komprehensif di catatan kaki. Namun terdapat gap yang perlu diperhatikan: "
        "Goodwill sebesar Rp52,2 triliun (26% total aset) mengandalkan asumsi DCF yang "
        "tidak sepenuhnya transparan, menciptakan ketegangan dengan prinsip Faithful "
        "Representation — khususnya dimensi Completeness dan Free from Error."
    )

    add_sub_heading(doc, "VIII.3 Implikasi untuk Standard Setter dan Praktisi Indonesia")
    add_body_paragraph(
        doc,
        "Bagi DSAK-IAI sebagai adopter IASB CF 2018, pemahaman mendalam tentang SFAC 8 "
        "memberikan konteks historis dan konseptual yang berharga. Ketika DSAK-IAI "
        "mempertimbangkan amendemen PSAK — misalnya terkait Goodwill accounting, IFRS 17 "
        "Insurance Contracts, atau IFRS 16 Leases — landasan konseptual SFAC 8 memberikan "
        "kerangka argumentasi yang terstruktur. Bagi OJK sebagai regulator pasar modal, "
        "pemahaman tentang limitasi Fair Value (pro-cyclicality) dan keterbatasan catatan kaki "
        "(D32) dapat menginformasikan kebijakan pengungkapan emiten."
    )
    add_body_paragraph(
        doc,
        "Kesimpulan akhir: studi kasus INDF 2024 menegaskan bahwa kerangka konseptual FASB "
        "bukan sekadar dokumen akademis — ia adalah panduan operasional yang secara langsung "
        "mempengaruhi bagaimana Goodwill Rp52,2 triliun diukur, bagaimana NCI Rp43,077 "
        "triliun diklasifikasikan, dan bagaimana tren EPS Rp984 per saham diinterpretasikan "
        "oleh investor. Memahami fondasi konseptual ini adalah prasyarat untuk memahami "
        "realitas laporan keuangan korporasi modern."
    )
```

- [ ] **Step 12.4: Implement `scripts/word_doc/bibliography.py`**

```python
import os
from scripts.word_doc.styles import set_run_font, add_page_break
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH


def build_bibliography(doc, txt_path: str) -> None:
    """
    Parse Daftar Pustaka .txt file and add formatted bibliography section.
    Expected file: 'Daftar Pustaka — Presentasi Kelompok 3.txt'
    """
    add_page_break(doc)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(16)
    run = p_title.add_run("DAFTAR PUSTAKA")
    set_run_font(run, 14, bold=True)

    if not os.path.exists(txt_path):
        p_warn = doc.add_paragraph()
        run_w = p_warn.add_run(
            f"[Peringatan: File daftar pustaka tidak ditemukan di: {txt_path}]"
        )
        set_run_font(run_w, 11, italic=True)
        return

    with open(txt_path, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        stripped = line.rstrip("\n")
        if not stripped.strip():
            # Empty line — add small spacer
            doc.add_paragraph()
            continue

        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)

        # Detect category headers (lines ending with ':' or all-caps headers)
        if stripped.endswith(":") or (stripped.isupper() and len(stripped) < 60):
            p.paragraph_format.space_before = Pt(10)
            run = p.add_run(stripped)
            set_run_font(run, 11, bold=True)
        else:
            # Hanging indent for bibliography entries
            p.paragraph_format.first_line_indent = Pt(-24)
            p.paragraph_format.left_indent = Pt(24)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            run = p.add_run(stripped)
            set_run_font(run, 11)
```

- [ ] **Step 12.5: Run tests**

```
pytest tests/test_word_doc.py -k "test_bagian_viii or test_bibliography" -v
```
Expected: 2 PASSED

- [ ] **Step 12.6: Commit**

```
git add scripts/word_doc/sections/bagian_viii.py scripts/word_doc/bibliography.py tests/test_word_doc.py
git commit -m "feat(word-doc): implement Bagian VIII (Kesimpulan) and bibliography parser"
```

---

### Task 13: `generate_word_doc.py` — Main assembly and final run

**Files:**
- Modify: `scripts/generate_word_doc.py`
- Modify: `tests/test_word_doc.py`

- [ ] **Step 13.1: Write failing integration test**

Append to `tests/test_word_doc.py`:
```python
import tempfile


def test_generate_full_document_produces_docx():
    import subprocess, sys, os
    output_dir = tempfile.mkdtemp()
    output_path = os.path.join(output_dir, "test_output.docx")
    result = subprocess.run(
        [sys.executable, "scripts/generate_word_doc.py", "--output", output_path],
        capture_output=True, text=True, timeout=120
    )
    assert result.returncode == 0, f"Script failed:\n{result.stderr}"
    assert os.path.exists(output_path), "Output .docx not created"
    # Verify it opens as valid docx
    from docx import Document
    doc = Document(output_path)
    assert len(doc.paragraphs) > 50, "Document too short"
```

- [ ] **Step 13.2: Run test (expect failure)**

```
pytest tests/test_word_doc.py::test_generate_full_document_produces_docx -v
```

- [ ] **Step 13.3: Implement `scripts/generate_word_doc.py`**

```python
"""
generate_word_doc.py — Academic Report Word Document Generator
Usage: python scripts/generate_word_doc.py [--output PATH]

Output default: <project_root>/01079_Dzaki Muhammad Yusfian_Tugas Kelompok PKK.docx
"""

import argparse
import os
import sys

# Ensure project root is on the path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from docx import Document
from scripts.word_doc.styles import setup_document, add_page_numbers, add_page_break
from scripts.word_doc.cover import build_cover
from scripts.word_doc.front_matter import build_front_matter
from scripts.word_doc.sections import (
    bagian_i, bagian_ii, bagian_iii, bagian_iv,
    bagian_v, bagian_vi, bagian_vii, bagian_viii,
)
from scripts.word_doc.bibliography import build_bibliography


def main(output_path: str) -> None:
    doc = Document()
    setup_document(doc)
    add_page_numbers(doc)

    logo_path = os.path.join(PROJECT_ROOT, "STIE Logo.png")
    bib_path = os.path.join(
        PROJECT_ROOT, "Daftar Pustaka — Presentasi Kelompok 3.txt"
    )

    print("[1/12] Cover page …")
    build_cover(doc, logo_path)
    add_page_break(doc)

    print("[2/12] Front matter (ToC + Kata Pengantar) …")
    build_front_matter(doc)

    print("[3/12] Bagian I — Konteks & Evolusi CF …")
    bagian_i.build(doc)
    add_page_break(doc)

    print("[4/12] Bagian II — Karakteristik Kualitatif …")
    bagian_ii.build(doc)
    add_page_break(doc)

    print("[5/12] Bagian III — Elemen LK …")
    bagian_iii.build(doc)
    add_page_break(doc)

    print("[6/12] Bagian IV — Pengakuan & Pengukuran …")
    bagian_iv.build(doc)
    add_page_break(doc)

    print("[7/12] Bagian V — Catatan Kritis …")
    bagian_v.build(doc)
    add_page_break(doc)

    print("[8/12] Bagian VI — Sintesis Teori …")
    bagian_vi.build(doc)
    add_page_break(doc)

    print("[9/12] Bagian VII — Studi Kasus INDF 2024 …")
    bagian_vii.build(doc)
    add_page_break(doc)

    print("[10/12] Bagian VIII — Kesimpulan …")
    bagian_viii.build(doc)

    print("[11/12] Daftar Pustaka …")
    build_bibliography(doc, bib_path)

    print(f"[12/12] Saving to: {output_path}")
    doc.save(output_path)
    print(f"Done. File: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Academic Report Word document")
    default_output = os.path.join(
        PROJECT_ROOT,
        "01079_Dzaki Muhammad Yusfian_Tugas Kelompok PKK.docx"
    )
    parser.add_argument("--output", default=default_output,
                        help="Output .docx file path")
    args = parser.parse_args()
    main(args.output)
```

- [ ] **Step 13.4: Run integration test**

```
pytest tests/test_word_doc.py::test_generate_full_document_produces_docx -v
```
Expected: PASSED (may take 30–60 seconds to generate matplotlib charts)

- [ ] **Step 13.5: Run the full test suite**

```
pytest tests/test_word_doc.py -v
```
Expected: All tests PASSED

- [ ] **Step 13.6: Run the script directly and verify the output file**

```
python scripts/generate_word_doc.py
```
Expected output:
```
[1/12] Cover page …
[2/12] Front matter (ToC + Kata Pengantar) …
…
[12/12] Saving to: …/01079_Dzaki Muhammad Yusfian_Tugas Kelompok PKK.docx
Done. File: …/01079_Dzaki Muhammad Yusfian_Tugas Kelompok PKK.docx
```

Verify: open the file in Microsoft Word and check:
- Cover page displays STIE logo, all 6 member names, blue borders
- Daftar Isi field placeholder is present (needs F9 refresh in Word)
- All 8 sections appear with proper headings and sub-headings
- All tables render with black header rows
- All charts are embedded as inline images
- Font throughout is Times New Roman

- [ ] **Step 13.7: Commit final**

```
git add scripts/generate_word_doc.py tests/test_word_doc.py
git commit -m "feat(word-doc): complete implementation — 40+ page academic report generator"
```

---

## Self-Review

**Spec coverage check:**

| Spec Section | Implemented In | Status |
|---|---|---|
| Cover (Opsi A, logo, 6 members, blue borders) | Task 4 (`cover.py`) | ✓ |
| Daftar Isi (ToC field) | Task 5 (`front_matter.py`) | ✓ |
| Kata Pengantar (~150–200 kata) | Task 5 (`front_matter.py`) | ✓ |
| Bagian I — 4 sub-sections, Bagan 1.1/1.2, Tabel 1.1/1.2 | Task 6 | ✓ |
| Bagian II — 5 sub-sections, Bagan 2.1/2.2, Tabel 2.1, Grafik 2.1 | Task 7 | ✓ |
| Bagian III — 4 sub-sections, Tabel 3.1/3.2, Bagan 3.1 | Task 8 | ✓ |
| Bagian IV — 4 sub-sections, Tabel 4.1/4.2, Bagan 4.1/4.2 | Task 9 | ✓ |
| Bagian V — 4 sub-sections, catatan kritis | Task 10 | ✓ |
| Bagian VI — 2 sub-sections, Tabel 5.1, Bagan 5.1 | Task 10 | ✓ |
| Bagian VII — 10 sub-sections, Bagan 6.1/6.2/6.3, Tabel 6.1/6.2/6.3 | Task 11 | ✓ |
| Bagian VIII — 3 sub-sections | Task 12 | ✓ |
| Daftar Pustaka (dari .txt file) | Task 12 (`bibliography.py`) | ✓ |
| Typography: TNR, 16/14/12/11/10pt | Task 2 (`styles.py`) | ✓ |
| A4 margins 2.5cm | Task 2 (`styles.py`) | ✓ |
| Page numbers in footer | Task 2 (`styles.py`) | ✓ |
| 12 matplotlib image visuals | Task 3 (`visuals.py`) | ✓ |
| STIE Logo.png integration | Task 4 (`cover.py`) | ✓ |
| `python scripts/generate_word_doc.py` entry point | Task 13 | ✓ |

**Placeholder scan:** No "TBD" or "TODO" in implementation code. Tabel 6.1 (Goodwill per UPK) contains `[lihat AR 2024]` for values that must be verified from the source PDF — this is intentional data-integrity protection, not a code placeholder.

**Type consistency:** All visual functions return `io.BytesIO`. All section `build()` functions accept `doc: Document` and return `None`. `add_table_with_headers(doc, headers, rows_data)` is called with matching signatures across all tasks. `set_run_font(run, size_pt, bold, italic, color_rgb)` is called consistently throughout.

**Scope:** Single deliverable — one `.docx` file from one Python script. Appropriately scoped.
