import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


def box(ax, x, y, w, h, title, content="", linestyle="-"):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02",
        linewidth=1.2,
        linestyle=linestyle,
        facecolor="white",
        edgecolor="black"
    )
    ax.add_patch(patch)

    ax.text(
        x + w / 2,
        y + h - 0.25,
        title,
        ha="center",
        va="top",
        fontsize=10,
        fontweight="bold"
    )

    if content:
        ax.text(
            x + w / 2,
            y + h / 2 - 0.1,
            content,
            ha="center",
            va="center",
            fontsize=8,
            linespacing=1.4
        )


def arrow(ax, x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=1.2
        )
    )


fig, ax = plt.subplots(figsize=(12, 6))

ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis("off")


# ============================================================
# WAVES boundary
# ============================================================

waves = Rectangle(
    (0.4, 0.4),
    11.2,
    4.8,
    fill=False,
    linewidth=1.2,
    linestyle="--"
)

ax.add_patch(waves)

ax.text(
    0.6, 4.95,
    "WAVES Simulation Framework",
    fontsize=11,
    fontweight="bold"
)


# ============================================================
# Main simulation pipeline
# ============================================================

box(
    ax,
    0.9, 2.4, 2.3, 1.8,
    "VESSEL SOURCES",
    "Broadband noise\n"
    "Narrowband noise\n"
    "Propeller modulation"
)

box(
    ax,
    4.8, 2.4, 2.3, 1.8,
    "ACOUSTIC PROPAGATION",
    "Propagation interface\n"
    "Channel response"
)

box(
    ax,
    8.7, 2.4, 2.3, 1.8,
    "SONAR",
    "Hydrophones\n"
    "Sensitivity\n"
    "Directivity\n"
    "Signal acquisition"
)

arrow(ax, 3.2, 3.3, 4.8, 3.3)
arrow(ax, 7.1, 3.3, 8.7, 3.3)


# ============================================================
# Ambient noise
# ============================================================

box(
    ax,
    0.9, 0.8, 2.3, 1.1,
    "AMBIENT NOISE",
    "Turbulence | Shipping\nSea state | Rain"
)

arrow(
    ax,
    3.2, 1.35,
    8.7, 2.7
)


# ============================================================
# Scenario dynamics
# ============================================================

box(
    ax,
    4.0, 0.8, 4.2, 1.1,
    "SCENARIO DYNAMICS",
    "Position | Velocity | Acceleration | Doppler"
)


# ============================================================
# External environmental databases
# ============================================================

box(
    ax,
    2.0, 5.7, 4.0, 0.9,
    "ENVIRONMENTAL DATA",
    "SHOM | ETOPO | WOA18 | ERA5"
)

arrow(
    ax,
    4.8, 5.7,
    5.7, 4.2
)


# ============================================================
# External propagation models
# ============================================================

box(
    ax,
    7.2, 5.7, 2.5, 0.9,
    "PROPAGATION MODELS",
    "OASES | TRACEO"
)

arrow(
    ax,
    8.0, 5.7,
    6.5, 4.2
)


plt.tight_layout()

plt.savefig(
    "./results/plots/waves_architecture.pdf",
    bbox_inches="tight"
)

plt.savefig(
    "./results/plots/waves_architecture.svg",
    bbox_inches="tight"
)

plt.show()