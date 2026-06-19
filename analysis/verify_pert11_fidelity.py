# analysis/verify_pert11_fidelity.py
"""Fidelity check: render each source PDF page and each slide's SVG via a real
Chromium browser (the deck's actual rendering path) to PNG, then compare them
page-by-page. Prints per-page mean-abs pixel difference and PASS/FAIL.

A browser is used deliberately: PyMuPDF's own SVG rasterizer renders gradients
differently from its PDF rasterizer and is NOT a valid fidelity oracle for a
browser-rendered deliverable. Requires Chrome or Edge, Pillow, and numpy.

Run from the project root as a module so the package import resolves:
    python -m analysis.verify_pert11_fidelity
"""
import os
import subprocess
import sys
import fitz
import numpy as np
from PIL import Image
import analysis.build_pert11_html as b

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "analysis", "_pert11_fidelity")
W, H = 1440, 810
MAD_THRESHOLD = 6.0    # mean abs pixel diff (0-255) tolerated per page
PCT_THRESHOLD = 12.0   # max % of pixels allowed to differ by > 20 levels

BROWSER_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def find_browser():
    for p in BROWSER_CANDIDATES:
        if os.path.exists(p):
            return p
    return None


def render_svg_png(browser, svg, idx):
    """Render one SVG full-bleed at WxH via headless Chromium; return PNG path."""
    html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        '<style>html,body{margin:0;padding:0;background:#fff}'
        'svg{display:block;width:%dpx;height:%dpx}</style></head>'
        '<body>%s</body></html>' % (W, H, svg)
    )
    html_path = os.path.join(OUT, "page_%02d.html" % idx)
    png_path = os.path.join(OUT, "chrome_%02d.png" % idx)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    subprocess.run(
        [
            browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", "--window-size=%d,%d" % (W, H),
            "--screenshot=%s" % png_path,
            "file:///" + html_path.replace("\\", "/"),
        ],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return png_path


def main():
    os.makedirs(OUT, exist_ok=True)
    browser = find_browser()
    if not browser:
        print("NO BROWSER FOUND - install Chrome or Edge to run the fidelity check")
        sys.exit(2)
    print("browser:", browser)
    pdf_path = os.path.join(ROOT, b.SOURCE_PDF)
    doc = fitz.open(pdf_path)
    svgs = b.load_pages(pdf_path)
    assert len(svgs) == doc.page_count, (
        "page count mismatch: %d svgs vs %d pdf pages"
        % (len(svgs), doc.page_count)
    )
    worst_mad = 0.0
    worst_pct = 0.0
    all_ok = True
    for i in range(doc.page_count):
        pdf_png = os.path.join(OUT, "pdf_%02d.png" % (i + 1))
        doc[i].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False).save(pdf_png)
        chrome_png = render_svg_png(browser, svgs[i], i + 1)
        a = np.asarray(Image.open(pdf_png).convert("RGB"), dtype=np.int16)
        chrome_img = Image.open(chrome_png).convert("RGB")
        if chrome_img.size != (W, H):
            print(
                "page %02d: SCREENSHOT SIZE %s != (%d, %d) - check display DPI/scale  CHECK"
                % (i + 1, chrome_img.size, W, H)
            )
            all_ok = False
            continue
        c = np.asarray(chrome_img, dtype=np.int16)
        diff = np.abs(a - c)
        mad = float(diff.mean())
        pct = float((diff.max(axis=2) > 20).mean() * 100)
        worst_mad = max(worst_mad, mad)
        worst_pct = max(worst_pct, pct)
        ok = mad <= MAD_THRESHOLD and pct <= PCT_THRESHOLD
        all_ok = all_ok and ok
        print(
            "page %02d: mean_abs_diff=%5.2f  pct>20=%5.2f%%  %s"
            % (i + 1, mad, pct, "OK" if ok else "CHECK")
        )
    print(
        "\nworst: mean_abs_diff=%.2f (<= %.1f), pct>20=%.2f%% (<= %.1f)"
        % (worst_mad, MAD_THRESHOLD, worst_pct, PCT_THRESHOLD)
    )
    print("RESULT:", "PASS" if all_ok else "REVIEW NEEDED")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
