"""Generate theme-matched concept diagrams for the Pert.11 Canva deck.
Blue/yellow Studio-Shodwe-style palette. White background, crisp for Canva upload.
Deterministic (no Date metadata) so re-runs don't churn."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
import matplotlib.font_manager as fm

BLUE = "#1B4B8F"; BLUE_DK = "#143A6B"; YELLOW = "#F4C20D"
GREY = "#8A94A6"; RED = "#D64545"; INK = "#1A2230"; LIGHT = "#EAF0F8"

plt.rcParams["font.family"] = "DejaVu Sans"


def box(ax, x, y, w, h, text, fc, ec, tc, fs=15, bold=True):
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                       boxstyle="round,pad=0.02,rounding_size=0.06",
                       linewidth=2.5, edgecolor=ec, facecolor=fc, zorder=3)
    ax.add_patch(p)
    ax.text(x, y, text, ha="center", va="center", color=tc, fontsize=fs,
            fontweight="bold" if bold else "normal", zorder=4, wrap=True)


def arrow(ax, p0, p1, color=BLUE, ls="-", lw=3):
    a = FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=22,
                        linewidth=lw, color=color, linestyle=ls, zorder=2)
    ax.add_patch(a)


# ---------- 1. Figure 4.2 — concentric circles ----------
fig, ax = plt.subplots(figsize=(8, 8), dpi=200)
ax.add_patch(Circle((0, 0), 1.0, facecolor=LIGHT, edgecolor=BLUE, lw=4, zorder=1))
ax.add_patch(Circle((0, 0), 0.6, facecolor=YELLOW, edgecolor=BLUE_DK, lw=3, zorder=2))
ax.text(0, 0, "Harga Efisien\n(Informasi Publik)", ha="center", va="center",
        fontsize=15, fontweight="bold", color=INK, zorder=3)
ax.text(0, 0.82, "Fundamental Value", ha="center", va="center",
        fontsize=15, fontweight="bold", color=BLUE, zorder=3)
ax.annotate("Selisih =\nInformasi Orang Dalam", xy=(0.57, 0.57), xytext=(1.15, 1.15),
            fontsize=13, fontweight="bold", color=RED, ha="center",
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5))
ax.set_title("Figure 4.2 — Peran Pelaporan Keuangan", fontsize=17,
             fontweight="bold", color=BLUE_DK, pad=16)
ax.set_xlim(-1.5, 1.6); ax.set_ylim(-1.3, 1.5); ax.set_aspect("equal"); ax.axis("off")
fig.savefig("canva-custom-diagrams/fig42-nilai-fundamental.png", bbox_inches="tight",
            transparent=False, facecolor="white")
plt.close(fig)

# ---------- 2. Grossman broken loop ----------
fig, ax = plt.subplots(figsize=(9, 7), dpi=200)
pts = {1: (0.5, 0.85), 2: (0.85, 0.5), 3: (0.5, 0.15), 4: (0.15, 0.5)}
labels = {1: "Harga fully\ninformative", 2: "Insentif mencari\nlenyap",
          3: "Investor berhenti\nmencari", 4: "Harga tak lagi\ninformatif"}
cols = {1: YELLOW, 2: BLUE, 3: BLUE, 4: BLUE}
tcs = {1: INK, 2: "white", 3: "white", 4: "white"}
for k in pts:
    box(ax, pts[k][0], pts[k][1], 0.30, 0.18, labels[k], cols[k], BLUE_DK, tcs[k], fs=13)
arrow(ax, (0.66, 0.80), (0.80, 0.62))   # 1->2
arrow(ax, (0.80, 0.38), (0.66, 0.22))   # 2->3
arrow(ax, (0.34, 0.22), (0.20, 0.38))   # 3->4
arrow(ax, (0.20, 0.62), (0.34, 0.80), color=RED, ls=(0, (4, 3)))  # 4->1 broken
ax.text(0.33, 0.72, "X", fontsize=30, fontweight="bold", color=RED, ha="center", zorder=5)
ax.text(0.5, 0.5, "osilasi liar\ntak ada ekuilibrium", fontsize=13, color=RED,
        ha="center", va="center", fontweight="bold", style="italic")
ax.set_title("Paradoks Grossman (1976)", fontsize=18, fontweight="bold", color=BLUE_DK, pad=12)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.savefig("canva-custom-diagrams/grossman-loop.png", bbox_inches="tight",
            transparent=False, facecolor="white")
plt.close(fig)

# ---------- 3. Lemons / adverse selection flow ----------
fig, ax = plt.subplots(figsize=(12, 5.5), dpi=200)
steps = ["Pembeli tak bisa\nbedakan kualitas",
         "Pooling:\nharga = rata-rata",
         "Mobil bagus\ntersingkir",
         "Pasar bisa\nruntuh"]
xs = [0.12, 0.37, 0.62, 0.87]
for i, (x, s) in enumerate(zip(xs, steps)):
    fc = YELLOW if i == 0 else (RED if i == 3 else BLUE)
    tc = INK if i == 0 else "white"
    box(ax, x, 0.62, 0.165, 0.26, s, fc, BLUE_DK, tc, fs=13)
    if i < 3:
        arrow(ax, (x + 0.09, 0.62), (xs[i + 1] - 0.09, 0.62))
box(ax, 0.5, 0.16, 0.74, 0.16,
    "Antidot: sertifikat - garansi - reputasi  =  laporan keuangan berkualitas",
    LIGHT, BLUE, BLUE_DK, fs=14)
ax.set_title("Lemons Problem (Akerlof, 1970) - Adverse Selection",
             fontsize=17, fontweight="bold", color=BLUE_DK, pad=12)
ax.set_xlim(0, 1); ax.set_ylim(0, 0.85); ax.axis("off")
fig.savefig("canva-custom-diagrams/lemons-flow.png", bbox_inches="tight",
            transparent=False, facecolor="white")
plt.close(fig)

print("OK - 3 diagrams written to canva-custom-diagrams/")
