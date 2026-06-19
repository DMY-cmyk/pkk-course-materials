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
