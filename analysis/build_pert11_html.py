"""Build a self-contained HTML slide deck from the Pert. 11 Canva PDF export.

Deterministic: re-running produces byte-identical output. Render mode is
text_as_path=True so the design is pixel-faithful with zero font dependency.
"""
import os
import re
import fitz  # PyMuPDF

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
TEMPLATE = os.path.join(_HERE, "pert11_shell_template.html")
CONTROLS = os.path.join(_HERE, "pert11_controls.js")
OUTPUT = os.path.join(_ROOT, "presentasi-pert11.html")

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

    svg = re.sub(r'(?P<attr>href|xlink:href)="#([^"]+)"',
                 lambda m: (f'{m.group("attr")}="#{prefix}{m.group(2)}"'
                            if m.group(2) in ids else m.group(0)),
                 svg)
    return svg

def build_html(pdf_path: str) -> str:
    svgs = load_pages(pdf_path)
    sections = []
    for idx, svg in enumerate(svgs, start=1):
        ns = namespace_svg_ids(svg, idx)
        sections.append(
            f'<section class="slide" data-index="{idx}">{ns}</section>'
        )
    slides = "\n".join(sections)
    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()
    with open(CONTROLS, encoding="utf-8") as f:
        js = f.read()
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
