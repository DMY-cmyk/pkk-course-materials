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
    fig, ax = plt.subplots(figsize=(9.6, 2.6))
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3)
    ax.plot([0.4, 11.6], [1.0, 1.0], color=MID, linewidth=2, zorder=1)
    xs = [1.6, 4.4, 7.2, 10.0]
    for (year, label, shade), x in zip(events, xs):
        dashed = shade == "white"
        ax.plot([x], [1.0], "o", color=DARK, markersize=7, zorder=3)
        box(ax, x - 1.35, 1.45, 2.7, 1.1, label, fc=shade if not dashed else "white",
            tc="white" if not dashed else DARK, fontsize=7.5,
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
    ax.set_xlim(0, 12.4)
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
    ax.add_patch(FancyArrowPatch((9.2, 3.4), (9.9, 3.4),
                                 arrowstyle="-|>", mutation_scale=14, color=MID))
    box(ax, 9.95, 2.25, 2.35, 2.3,
        "Angka SCF tidak dapat\nditelusuri ke neraca;\nterjadi pada ±75%\nperusahaan (Bahnson,\nMiller & Budge)",
        fc="white", tc=DARK, fontsize=7.5, ec=DARK)
    save(fig, "diagram-nonarticulation.png")


def fcf_waterfall():
    # ABC Company 2005, Exhibit 13.10 bridge (verified against notes):
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
                    f"${d:+,}" if i else f"${d:,}",
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
