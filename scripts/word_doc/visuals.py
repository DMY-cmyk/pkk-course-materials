"""
Visual generators for Word document: 150 dpi PNG charts and diagrams.

Each function returns io.BytesIO at position 0, ready for embedding in
python-docx. Uses matplotlib Agg backend for headless rendering.
"""
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker


def _save_fig(fig) -> io.BytesIO:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return buf


def _draw_box(ax, cx, cy, w, h, label, bold=False, fill="white", fontsize=8):
    """Draw a rounded box with centered text."""
    r = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle="round,pad=0.1", lw=1, ec="black", fc=fill
    )
    ax.add_patch(r)
    ax.text(cx, cy, label, ha="center", va="center",
            fontsize=fontsize, fontfamily="serif",
            fontweight="bold" if bold else "normal")


def _draw_arrow(ax, x1, y1, x2, y2, label="", fontsize=7.5):
    """Draw an annotated arrow."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8))
    if label:
        ax.text((x1 + x2) / 2 + 0.1, (y1 + y2) / 2, label,
                fontsize=fontsize, fontstyle="italic", fontfamily="serif")


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

    outer = mpatches.FancyBboxPatch(
        (0.3, 0.3), 9.4, 4.4,
        boxstyle="round,pad=0.1", linewidth=1.5, edgecolor="black", facecolor="#f0f0f0"
    )
    ax.add_patch(outer)
    ax.text(5, 4.55, "Semua Pengguna Laporan Keuangan",
            ha="center", va="center", fontsize=9, fontfamily="serif", fontstyle="italic")

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

    _draw_box(ax, 5, 5.3, 3.5, 0.7, "KEGUNAAN INFORMASI KEUANGAN", bold=True, fill="#d0d0d0")

    for cx, label in [(3, "Relevansi\n(Relevance)"), (7, "Keandalan\n(Reliability)")]:
        _draw_box(ax, cx, 4.1, 2.4, 0.7, label, bold=True)
        _draw_arrow(ax, 5, 4.92, cx, 4.45)

    for cx, label in [(2, "Predictive\nValue"), (4, "Feedback\nValue")]:
        _draw_box(ax, cx, 2.9, 1.8, 0.65, label)
        _draw_arrow(ax, 3, 3.75, cx, 3.23)

    for cx, label in [(6, "Representational\nFaithfulness"), (7.8, "Verifiability"), (9, "Neutrality")]:
        _draw_box(ax, cx, 2.9, 1.7, 0.65, label)
        _draw_arrow(ax, 7, 3.75, cx, 3.23)

    _draw_box(ax, 5, 1.6, 2.5, 0.6, "Materialitas (Threshold)", fill="#eeeeee")
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

    _draw_box(ax, 5, 5.3, 3.5, 0.7, "KEGUNAAN INFORMASI KEUANGAN", bold=True, fill="#d0d0d0")

    for cx, label in [(3, "Relevansi\n(Relevance)"), (7, "Faithful\nRepresentation")]:
        _draw_box(ax, cx, 4.1, 2.4, 0.7, label, bold=True)
        _draw_arrow(ax, 5, 4.92, cx, 4.45)

    for cx, label in [(2, "Predictive\nValue"), (3, "Confirmatory\nValue"), (4, "Materiality")]:
        _draw_box(ax, cx, 2.9, 1.6, 0.6, label)
        _draw_arrow(ax, 3, 3.75, cx, 3.2)

    for cx, label in [(6, "Completeness"), (7.5, "Neutrality"), (9, "Free from\nError")]:
        _draw_box(ax, cx, 2.9, 1.6, 0.6, label)
        _draw_arrow(ax, 7, 3.75, cx, 3.2)

    ax.text(5, 2.1, "QC Peningkat (Enhancing):", ha="center",
            fontsize=8, fontfamily="serif", fontweight="bold")
    for i, label in enumerate(["Comparability", "Verifiability*", "Timeliness", "Understandability"]):
        _draw_box(ax, 1.5 + i * 2.3, 1.45, 2.1, 0.55, label, fill="#eeeeee")
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
    labels = ["Net Sales\n(Pendapatan)", "COGS\n(Beban Pokok)", "Gross Profit",
              "OpEx\n(Beban Operasi)", "Operating\nProfit", "Other\n(Net)", "Net Income\n(Laba Bersih)"]
    values = [115.79, -96.0, 19.79, -10.5, 9.29, -3.5, 5.79]

    running = 0
    bottoms = []
    heights = []
    colors_list = []
    for v in values:
        if v >= 0:
            bottoms.append(running)
            heights.append(v)
            colors_list.append("#555555")
            running += v
        else:
            running += v
            bottoms.append(running)
            heights.append(-v)
            colors_list.append("#aaaaaa")

    fig, ax = plt.subplots(figsize=(8, 4))
    x = range(len(labels))
    ax.bar(x, heights, bottom=bottoms, color=colors_list, edgecolor="black", linewidth=0.6, width=0.6)
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

    _draw_box(ax, 5, 5.3, 4.5, 0.75, "PEMILIHAN BASIS PENGUKURAN\n(SFAC 8 Ch.6, M30–M34)", bold=True, fill="#d0d0d0")
    _draw_box(ax, 5, 4.0, 4.0, 0.7, "Apakah aset/liabilitas\nmemiliki harga pasar unik?", fill="#eeeeee")
    _draw_arrow(ax, 5, 4.92, 5, 4.35)

    _draw_box(ax, 2.5, 2.6, 3.2, 0.75, "Entry Price\n(Harga Masuk)", bold=True, fill="white")
    _draw_arrow(ax, 5, 3.65, 2.5, 2.98, "YA — harga unik")

    _draw_box(ax, 7.5, 2.6, 3.2, 0.75, "Exit Price\n(Harga Keluar)", bold=True, fill="#eeeeee")
    _draw_arrow(ax, 5, 3.65, 7.5, 2.98, "TIDAK — tidak unik")

    for cx, items in [(2.5, ["Historical Cost", "Replacement Cost"]),
                      (7.5, ["Fair Value (IFRS 13)", "Net Realizable Value"])]:
        for i, label in enumerate(items):
            y_leaf = 1.5 - i * 0.85
            _draw_box(ax, cx, y_leaf, 2.8, 0.6, label)
            _draw_arrow(ax, cx, 2.22, cx, y_leaf + 0.3)

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

    _draw_box(ax, 5, 5.3, 4.5, 0.75,
        "PT Indofood Sukses Makmur Tbk (INDF)\nNet Sales: Rp115,79 T | EPS 2024: Rp984",
        bold=True, fill="#d0d0d0", fontsize=7.5)

    divisi = [
        (1.5, 3.7, "Bogasari\n(Tepung Terigu)"),
        (3.8, 3.7, "Agribisnis\n(CPO & Karet)"),
        (6.2, 3.7, "CBP\n(ICBP — Mi Instan)"),
        (8.5, 3.7, "Distribusi\n& Lainnya"),
    ]
    for cx, cy, label in divisi:
        _draw_box(ax, cx, cy, 2.3, 0.8, label, fontsize=7.5)
        ax.plot([5, cx], [4.92, 4.1], color="black", lw=0.8)

    ax.text(5, 2.7, "Angka Kunci 2024:", ha="center",
            fontsize=9, fontfamily="serif", fontweight="bold")
    kv = [
        ("Total Goodwill", "Rp 52,2 T (26% total aset)"),
        ("NCI (Kepentingan Nonpengendali)", "Rp 43,077 T"),
        ("Pemegang Saham Mayoritas", "First Pacific Ltd. — 50,07%"),
        ("Auditor Independen", "Ernst & Young (Purwantono, Sungkoro & Surja)"),
    ]
    for i, (k, v) in enumerate(kv):
        ax.text(0.5, 2.1 - i * 0.55, f"• {k}: {v}",
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
    ax.pie(
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

    ax.plot([5, 5], [0.5, 6.1], color="black", linewidth=1.2)
    ax.plot([0.2, 9.8], [3.5, 3.5], color="black", linewidth=1.2)

    ax.text(5, 6.5, "Matrix: Relevansi × Faithful Representation — Item LK INDF 2024",
            ha="center", fontsize=9.5, fontfamily="serif", fontweight="bold")

    ax.text(2.5, 0.2, "Relevansi Rendah", ha="center", fontsize=8.5, fontfamily="serif")
    ax.text(7.5, 0.2, "Relevansi Tinggi", ha="center", fontsize=8.5, fontfamily="serif")
    ax.text(0.3, 1.75, "FR\nRendah", ha="center", va="center", fontsize=8.5, fontfamily="serif")
    ax.text(0.3, 5.25, "FR\nTinggi", ha="center", va="center", fontsize=8.5, fontfamily="serif")

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
