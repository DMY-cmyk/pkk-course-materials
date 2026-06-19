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
