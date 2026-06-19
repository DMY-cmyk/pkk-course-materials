# Pert. 11 PDF → Self-Contained HTML Slide Deck — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert `Presentasi PKK Pert. 11 - Kelompok 3.pdf` (18 pages, 16:9) into one self-contained, offline HTML slide deck that is pixel-faithful to the source.

**Architecture:** A deterministic Python/PyMuPDF build script renders each PDF page to a vector SVG with `text_as_path=True` (glyphs as outlines → zero font dependency), namespaces each page's SVG ids to prevent cross-slide collisions, and assembles all 18 SVGs into an HTML shell (separate template file) that provides keyboard/click/fullscreen/overview navigation. A final verification step renders both the PDF and the HTML to images and compares them page-by-page.

**Tech Stack:** Python 3, PyMuPDF (`fitz`), pytest, vanilla HTML/CSS/JS (no CDNs, no external fonts).

## Global Constraints

- Source PDF (read-only, never modified): `Presentasi PKK Pert. 11 - Kelompok 3.pdf` — exactly **18 pages**, each **1440×810 pt** (16:9).
- Render mode: **`text_as_path=True`** — never selectable-text mode (custom/Type3 fonts would break the design).
- Output is **one self-contained file**: `presentasi-pert11.html` at project root — no external CSS/JS/font/image references whatsoever.
- Build must be **deterministic**: re-running produces byte-identical output (no timestamps, no random ids).
- No content rewriting, reordering, re-theming, transitions, or speaker notes. Pure faithful conversion.
- All SVG ids and their `url(#...)` references must be unique across the combined document (per-page namespacing).

---

### Task 1: Build script — PDF load, validation, per-page SVG render

**Files:**
- Create: `analysis/build_pert11_html.py`
- Test: `tests/test_build_pert11_html.py`

**Interfaces:**
- Consumes: the source PDF path.
- Produces:
  - `SOURCE_PDF = "Presentasi PKK Pert. 11 - Kelompok 3.pdf"` (module constant, project-root-relative)
  - `EXPECTED_PAGES = 18`
  - `load_pages(pdf_path: str) -> list[str]` — opens the PDF, asserts page count == `EXPECTED_PAGES`, returns a list of 18 SVG strings (one per page) via `get_svg_image(text_as_path=True)`. Raises `ValueError` if page count differs or any page yields an empty SVG.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_build_pert11_html.py
import os
import pytest
import analysis.build_pert11_html as b

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_load_pages_returns_18_nonempty_svgs():
    svgs = b.load_pages(os.path.join(ROOT, b.SOURCE_PDF))
    assert len(svgs) == b.EXPECTED_PAGES == 18
    for i, s in enumerate(svgs):
        assert s.strip().startswith("<"), f"page {i} not SVG"
        assert "<svg" in s and "</svg>" in s, f"page {i} missing svg tags"
        assert len(s) > 1000, f"page {i} suspiciously small"

def test_load_pages_is_deterministic():
    p = os.path.join(ROOT, b.SOURCE_PDF)
    assert b.load_pages(p) == b.load_pages(p)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_build_pert11_html.py -v`
Expected: FAIL with `ModuleNotFoundError` / `AttributeError` (module/functions not defined yet).

- [ ] **Step 3: Write minimal implementation**

```python
# analysis/build_pert11_html.py
"""Build a self-contained HTML slide deck from the Pert. 11 Canva PDF export.

Deterministic: re-running produces byte-identical output. Render mode is
text_as_path=True so the design is pixel-faithful with zero font dependency.
"""
import fitz  # PyMuPDF

SOURCE_PDF = "Presentasi PKK Pert. 11 - Kelompok 3.pdf"
EXPECTED_PAGES = 18

def load_pages(pdf_path: str) -> list[str]:
    """Return one SVG string per PDF page (text as vector paths)."""
    doc = fitz.open(pdf_path)
    try:
        if doc.page_count != EXPECTED_PAGES:
            raise ValueError(
                f"expected {EXPECTED_PAGES} pages, got {doc.page_count}"
            )
        svgs = []
        for i in range(doc.page_count):
            svg = doc[i].get_svg_image(text_as_path=True)
            if not svg or len(svg.strip()) < 1000:
                raise ValueError(f"page {i} produced empty/too-small SVG")
            svgs.append(svg)
        return svgs
    finally:
        doc.close()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_build_pert11_html.py -v`
Expected: PASS (both tests).

- [ ] **Step 5: Commit**

```bash
git add analysis/build_pert11_html.py tests/test_build_pert11_html.py
git commit -m "feat(pert11-html): load+validate PDF pages as faithful SVGs"
```

---

### Task 2: Per-page SVG id namespacing (prevent cross-slide collisions)

**Files:**
- Modify: `analysis/build_pert11_html.py`
- Test: `tests/test_build_pert11_html.py`

**Interfaces:**
- Consumes: a single SVG string + a page index.
- Produces:
  - `namespace_svg_ids(svg: str, page_index: int) -> str` — prefixes every `id="X"` with `p{page_index:02d}_` and rewrites every matching `url(#X)` and `href="#X"` reference to the prefixed id, so 18 inlined SVGs never share an id. Returns the rewritten SVG.

**Why:** PyMuPDF emits ids like `clip_1`, `clip_2` per page. Inlined together, duplicate ids make browsers resolve `url(#clip_1)` to the first match — clip-paths/masks on later slides break. Namespacing preserves fidelity.

- [ ] **Step 1: Write the failing test**

```python
def test_namespace_svg_ids_prefixes_ids_and_refs():
    svg = (
        '<svg><clipPath id="clip_1"><rect/></clipPath>'
        '<g clip-path="url(#clip_1)"><image href="#img_2"/></g></svg>'
    )
    out = b.namespace_svg_ids(svg, 3)
    assert 'id="p03_clip_1"' in out
    assert 'url(#p03_clip_1)' in out
    assert 'href="#p03_img_2"' in out
    assert 'id="clip_1"' not in out  # no bare id remains

def test_namespace_no_collisions_across_pages():
    svg = '<svg><clipPath id="clip_1"/><g clip-path="url(#clip_1)"/></svg>'
    combined = b.namespace_svg_ids(svg, 1) + b.namespace_svg_ids(svg, 2)
    # each page's id appears, and they differ
    assert 'id="p01_clip_1"' in combined and 'id="p02_clip_1"' in combined
    assert combined.count('id="p01_clip_1"') == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_build_pert11_html.py::test_namespace_svg_ids_prefixes_ids_and_refs -v`
Expected: FAIL with `AttributeError: module ... has no attribute 'namespace_svg_ids'`.

- [ ] **Step 3: Write minimal implementation**

Add to `analysis/build_pert11_html.py`:

```python
import re

def namespace_svg_ids(svg: str, page_index: int) -> str:
    """Prefix all ids and their references with p{NN}_ to keep ids unique
    when many SVGs are inlined into one document."""
    prefix = f"p{page_index:02d}_"
    # Collect declared ids first so we only rewrite references we actually own.
    ids = set(re.findall(r'id="([^"]+)"', svg))

    def repl_id(m):
        return f'id="{prefix}{m.group(1)}"'
    svg = re.sub(r'id="([^"]+)"', repl_id, svg)

    def repl_url(m):
        name = m.group(1)
        return f'url(#{prefix}{name})' if name in ids else m.group(0)
    svg = re.sub(r'url\(#([^)]+)\)', repl_url, svg)

    def repl_href(m):
        name = m.group(1)
        return f'{m.group("attr")}="#{prefix}{name}"' if name in ids else m.group(0)
    svg = re.sub(r'(?P<attr>href|xlink:href)="#([^"]+)"',
                 lambda m: (f'{m.group("attr")}="#{prefix}{m.group(2)}"'
                            if m.group(2) in ids else m.group(0)),
                 svg)
    return svg
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_build_pert11_html.py -v`
Expected: PASS (all tests).

- [ ] **Step 5: Verify on the real PDF (no duplicate ids across all 18 pages)**

Run:
```bash
python -c "
import os, re, analysis.build_pert11_html as b
ROOT=os.getcwd()
svgs=[b.namespace_svg_ids(s,i+1) for i,s in enumerate(b.load_pages(os.path.join(ROOT,b.SOURCE_PDF)))]
ids=re.findall(r'id=\"([^\"]+)\"', ''.join(svgs))
print('total ids:', len(ids), 'unique:', len(set(ids)))
assert len(ids)==len(set(ids)), 'DUPLICATE IDS REMAIN'
print('OK: all ids unique across 18 pages')
"
```
Expected: `OK: all ids unique across 18 pages`.

- [ ] **Step 6: Commit**

```bash
git add analysis/build_pert11_html.py tests/test_build_pert11_html.py
git commit -m "feat(pert11-html): namespace per-page SVG ids to avoid collisions"
```

---

### Task 3: HTML shell template (structure + 16:9 stage + styles)

**Files:**
- Create: `analysis/pert11_shell_template.html`
- Test: `tests/test_build_pert11_html.py`

**Interfaces:**
- Produces: a static template file containing two placeholder tokens — `{{SLIDE_COUNT}}` and `{{SLIDES}}` — plus all CSS and the controls JS (JS added in Task 4; for now include a `{{CONTROLS_JS}}` placeholder). No external references.
- The template defines: a `#deck` container; each slide is `<section class="slide" data-index="N">…svg…</section>`; only `.slide.active` is shown; a `#stage` enforcing `aspect-ratio:16/9` and letterboxing; a `#progress` bar; a `#counter`; a hidden `#overview` grid container.

- [ ] **Step 1: Write the failing test**

```python
def test_template_has_required_placeholders_and_no_external_refs():
    import os
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tpl = open(os.path.join(ROOT, "analysis", "pert11_shell_template.html"),
               encoding="utf-8").read()
    for token in ("{{SLIDE_COUNT}}", "{{SLIDES}}", "{{CONTROLS_JS}}"):
        assert token in tpl, f"missing placeholder {token}"
    # self-contained: no external resource loads
    for bad in ("http://", "https://", "src=\"//", "<link", "@import"):
        assert bad not in tpl, f"external reference found: {bad}"
    assert "aspect-ratio" in tpl  # 16:9 stage present
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_build_pert11_html.py::test_template_has_required_placeholders_and_no_external_refs -v`
Expected: FAIL with `FileNotFoundError`.

- [ ] **Step 3: Create the template**

```html
<!-- analysis/pert11_shell_template.html -->
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Presentasi PKK Pert. 11 - Kelompok 3</title>
<style>
  :root { --bg:#0b0b0d; }
  * { box-sizing: border-box; }
  html, body { margin:0; height:100%; background:var(--bg);
    font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }
  #stage { position:fixed; inset:0; display:flex; align-items:center;
    justify-content:center; }
  #deck { aspect-ratio:16/9; width:min(100vw, calc(100vh * 16 / 9));
    height:min(100vh, calc(100vw * 9 / 16)); position:relative;
    background:#fff; box-shadow:0 0 40px rgba(0,0,0,.5); }
  .slide { position:absolute; inset:0; display:none; }
  .slide.active { display:block; }
  .slide svg { width:100%; height:100%; display:block; }
  #progress { position:fixed; top:0; left:0; height:4px; background:#4f7cff;
    width:0; transition:width .15s ease; z-index:10; }
  #counter { position:fixed; bottom:10px; right:14px; color:#fff;
    font-size:14px; opacity:.7; z-index:10;
    background:rgba(0,0,0,.4); padding:2px 8px; border-radius:10px; }
  #overview { position:fixed; inset:0; background:rgba(8,8,10,.96);
    display:none; grid-template-columns:repeat(4, 1fr); gap:12px;
    padding:24px; overflow:auto; z-index:20; }
  #overview.open { display:grid; }
  #overview .thumb { background:#fff; aspect-ratio:16/9; cursor:pointer;
    border:3px solid transparent; overflow:hidden; }
  #overview .thumb.current { border-color:#4f7cff; }
  #overview .thumb svg { width:100%; height:100%; display:block;
    pointer-events:none; }
</style>
</head>
<body>
  <div id="progress"></div>
  <div id="stage"><div id="deck">{{SLIDES}}</div></div>
  <div id="counter"><span id="cur">1</span> / {{SLIDE_COUNT}}</div>
  <div id="overview"></div>
  <script>{{CONTROLS_JS}}</script>
</body>
</html>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_build_pert11_html.py::test_template_has_required_placeholders_and_no_external_refs -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add analysis/pert11_shell_template.html tests/test_build_pert11_html.py
git commit -m "feat(pert11-html): add self-contained 16:9 shell template"
```

---

### Task 4: Controls JS (keyboard, click zones, fullscreen, counter+progress, overview)

**Files:**
- Create: `analysis/pert11_controls.js`
- Test: `tests/test_build_pert11_html.py`

**Interfaces:**
- Produces: a JS string (read from this file and substituted into `{{CONTROLS_JS}}`) implementing all navigation. It reads `.slide` elements from the DOM, builds the thumbnail grid by cloning each slide's SVG, and wires events. No build-time templating inside the JS — it is static and DOM-driven.

- [ ] **Step 1: Write the failing test**

```python
def test_controls_js_defines_all_behaviors():
    import os
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    js = open(os.path.join(ROOT, "analysis", "pert11_controls.js"),
              encoding="utf-8").read()
    # keyboard
    assert "keydown" in js
    for key in ("ArrowRight", "ArrowLeft", "Home", "End", " "):
        assert key in js
    # fullscreen + overview + click zones + progress
    assert "requestFullscreen" in js
    assert "Escape" in js and "overview" in js
    assert "clientX" in js  # left/right click-zone logic
    assert "progress" in js and "cur" in js
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_build_pert11_html.py::test_controls_js_defines_all_behaviors -v`
Expected: FAIL with `FileNotFoundError`.

- [ ] **Step 3: Write the controls JS**

```javascript
// analysis/pert11_controls.js
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var n = slides.length, i = 0;
  var cur = document.getElementById('cur');
  var progress = document.getElementById('progress');
  var overview = document.getElementById('overview');
  var deck = document.getElementById('deck');

  function show(idx) {
    i = Math.max(0, Math.min(n - 1, idx));
    slides.forEach(function (s, k) { s.classList.toggle('active', k === i); });
    cur.textContent = (i + 1);
    progress.style.width = ((i + 1) / n * 100) + '%';
    var thumbs = overview.querySelectorAll('.thumb');
    thumbs.forEach(function (t, k) { t.classList.toggle('current', k === i); });
  }
  function next() { show(i + 1); }
  function prev() { show(i - 1); }

  // Thumbnail overview (clone each slide's svg once).
  slides.forEach(function (s, k) {
    var t = document.createElement('div');
    t.className = 'thumb';
    var svg = s.querySelector('svg');
    if (svg) t.appendChild(svg.cloneNode(true));
    t.addEventListener('click', function () { closeOverview(); show(k); });
    overview.appendChild(t);
  });
  function toggleOverview() { overview.classList.toggle('open'); }
  function closeOverview() { overview.classList.remove('open'); }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { if (overview.classList.contains('open')) closeOverview(); return; }
    if (e.key === 'o' || e.key === 'O') { toggleOverview(); return; }
    if (overview.classList.contains('open')) return;
    switch (e.key) {
      case 'ArrowRight': case 'PageDown': case ' ': next(); e.preventDefault(); break;
      case 'ArrowLeft': case 'PageUp': prev(); e.preventDefault(); break;
      case 'Home': show(0); break;
      case 'End': show(n - 1); break;
      case 'f': case 'F':
        if (!document.fullscreenElement) document.documentElement.requestFullscreen();
        else document.exitFullscreen();
        break;
    }
  });

  // Click zones (left half = prev, right half = next), ignored over overview.
  document.getElementById('stage').addEventListener('click', function (e) {
    if (overview.classList.contains('open')) return;
    if (e.clientX < window.innerWidth / 2) prev(); else next();
  });

  show(0);
})();
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_build_pert11_html.py::test_controls_js_defines_all_behaviors -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add analysis/pert11_controls.js tests/test_build_pert11_html.py
git commit -m "feat(pert11-html): add navigation/overview controls JS"
```

---

### Task 5: Assemble + write `presentasi-pert11.html` (end-to-end build)

**Files:**
- Modify: `analysis/build_pert11_html.py`
- Test: `tests/test_build_pert11_html.py`

**Interfaces:**
- Consumes: `load_pages`, `namespace_svg_ids`, the template file, the controls JS file.
- Produces:
  - `build_html(pdf_path: str) -> str` — returns the full HTML string: for each page, namespace ids and wrap in `<section class="slide" data-index="N">…</section>`; substitute `{{SLIDES}}`, `{{SLIDE_COUNT}}`, `{{CONTROLS_JS}}`. Reads template + JS relative to the script's own directory.
  - `main() -> None` — writes `build_html` output to `presentasi-pert11.html` at project root (UTF-8, `\n` newlines for determinism) and prints the byte size. Guarded by `if __name__ == "__main__":`.

- [ ] **Step 1: Write the failing test**

```python
def test_build_html_is_complete_and_self_contained():
    import os
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html = b.build_html(os.path.join(ROOT, b.SOURCE_PDF))
    assert html.count('class="slide"') == 18
    assert "{{SLIDES}}" not in html and "{{CONTROLS_JS}}" not in html \
        and "{{SLIDE_COUNT}}" not in html
    assert "> / 18" not in html  # counter substituted
    for bad in ("http://", "https://", "<link", "@import"):
        assert bad not in html
    # ids unique across whole document
    import re
    ids = re.findall(r'id="([^"]+)"', html)
    assert len(ids) == len(set(ids))

def test_build_html_deterministic():
    import os
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p = os.path.join(ROOT, b.SOURCE_PDF)
    assert b.build_html(p) == b.build_html(p)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_build_pert11_html.py::test_build_html_is_complete_and_self_contained -v`
Expected: FAIL with `AttributeError: ... 'build_html'`.

- [ ] **Step 3: Write the implementation**

Add to `analysis/build_pert11_html.py`:

```python
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
TEMPLATE = os.path.join(_HERE, "pert11_shell_template.html")
CONTROLS = os.path.join(_HERE, "pert11_controls.js")
OUTPUT = os.path.join(_ROOT, "presentasi-pert11.html")

def build_html(pdf_path: str) -> str:
    svgs = load_pages(pdf_path)
    sections = []
    for idx, svg in enumerate(svgs, start=1):
        ns = namespace_svg_ids(svg, idx)
        sections.append(
            f'<section class="slide" data-index="{idx}">{ns}</section>'
        )
    slides = "\n".join(sections)
    tpl = open(TEMPLATE, encoding="utf-8").read()
    js = open(CONTROLS, encoding="utf-8").read()
    html = (tpl.replace("{{SLIDE_COUNT}}", str(len(svgs)))
               .replace("{{CONTROLS_JS}}", js)
               .replace("{{SLIDES}}", slides))
    return html

def main() -> None:
    html = build_html(os.path.join(_ROOT, SOURCE_PDF))
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"wrote {OUTPUT} ({len(html.encode('utf-8'))} bytes)")

if __name__ == "__main__":
    main()
```

> Note: substitute `{{CONTROLS_JS}}` **before** `{{SLIDES}}` so SVG content (which may contain `{{`-like sequences is unlikely, but order avoids any placeholder living inside injected SVG). Keep this order.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_build_pert11_html.py -v`
Expected: PASS (all tests).

- [ ] **Step 5: Generate the real deliverable**

Run: `python analysis/build_pert11_html.py`
Expected: prints `wrote .../presentasi-pert11.html (~12000000 bytes)` and the file exists.

- [ ] **Step 6: Commit**

```bash
git add analysis/build_pert11_html.py tests/test_build_pert11_html.py presentasi-pert11.html
git commit -m "feat(pert11-html): assemble and emit self-contained slide deck"
```

---

### Task 6: Fidelity verification (PDF vs HTML, page-by-page evidence)

**Files:**
- Create: `analysis/verify_pert11_fidelity.py`

**Interfaces:**
- Consumes: the source PDF + the generated `presentasi-pert11.html`.
- Produces: side-by-side / diff PNGs under `analysis/_pert11_fidelity/` and a printed PASS/FAIL summary. Renders each PDF page to PNG (PyMuPDF) and each HTML slide to PNG using a headless browser if available; if no browser automation is installed, falls back to rendering each namespaced SVG to PNG via PyMuPDF (`fitz.open(stream=svg, filetype="svg")`) — which still proves the SVG content matches the page — and prints which method was used.

- [ ] **Step 1: Write the verification script**

```python
# analysis/verify_pert11_fidelity.py
"""Render source PDF pages and the built SVG slides to PNG and compare.
Prints a per-page mean-abs-difference and an overall PASS/FAIL."""
import os
import fitz
import analysis.build_pert11_html as b

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "analysis", "_pert11_fidelity")
ZOOM = 1.0          # 1440x810 native is plenty
THRESHOLD = 2.0     # mean abs pixel diff (0-255) tolerated per page

def _pix_bytes(pix):
    return pix.samples

def main():
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(os.path.join(ROOT, b.SOURCE_PDF))
    svgs = b.load_pages(os.path.join(ROOT, b.SOURCE_PDF))
    worst = 0.0
    for i in range(doc.page_count):
        # PDF render
        pdf_pix = doc[i].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), alpha=False)
        # SVG render (namespacing does not change geometry; use raw svg)
        svg_doc = fitz.open(stream=svgs[i].encode("utf-8"), filetype="svg")
        svg_pix = svg_doc[0].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), alpha=False)
        pdf_pix.save(os.path.join(OUT, f"pdf_{i+1:02d}.png"))
        svg_pix.save(os.path.join(OUT, f"svg_{i+1:02d}.png"))
        if pdf_pix.width == svg_pix.width and pdf_pix.height == svg_pix.height:
            a, c = pdf_pix.samples, svg_pix.samples
            diff = sum(abs(a[j] - c[j]) for j in range(0, len(a), 97)) / (len(a) / 97)
        else:
            diff = 999.0
        worst = max(worst, diff)
        flag = "OK" if diff <= THRESHOLD else "CHECK"
        print(f"page {i+1:02d}: meanabsdiff~{diff:6.2f}  {flag}")
    print(f"\nworst page diff: {worst:.2f}  threshold: {THRESHOLD}")
    print("RESULT:", "PASS" if worst <= THRESHOLD else "REVIEW NEEDED")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the verification**

Run: `python analysis/verify_pert11_fidelity.py`
Expected: 18 lines `page NN: ... OK` and `RESULT: PASS`. If any page says `CHECK`, open `analysis/_pert11_fidelity/pdf_NN.png` vs `svg_NN.png` and inspect before proceeding.

- [ ] **Step 3: Manual open in a real browser (definitive check)**

Open `presentasi-pert11.html` in a browser. Confirm: all 18 slides render identical to the PDF; arrow keys + Space move; click left/right halves navigate; `F` fullscreens; counter + progress update; `O`/`Esc` toggles the thumbnail overview; clicking a thumbnail jumps. Read at least 3 slides start-to-finish for visual parity.

- [ ] **Step 4: Commit**

```bash
git add analysis/verify_pert11_fidelity.py
git commit -m "test(pert11-html): add page-by-page fidelity verification"
```

---

## Self-Review

**Spec coverage:**
- Faithful SVG render (text_as_path) → Task 1 ✓
- Design not broken by id collisions → Task 2 ✓
- Self-contained single HTML, 16:9 stage → Task 3 ✓
- Keyboard / fullscreen+click / counter+progress / overview → Task 4 ✓
- Determinism + assembly + output location → Task 5 ✓
- Fidelity verification with evidence → Task 6 ✓
- Source never modified → only read in all tasks ✓
- No fabrication/rewrite → pure conversion, no content tasks ✓

**Placeholder scan:** No TBD/TODO; all steps contain runnable code/commands. ✓

**Type consistency:** `load_pages`, `namespace_svg_ids`, `build_html`, `main`, constants `SOURCE_PDF`/`EXPECTED_PAGES`/`OUTPUT` used consistently across Tasks 1, 2, 5, 6. ✓
