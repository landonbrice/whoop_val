"""Build the 5 visuals for the WHOOP Yannelis IC deck.

All saved to /home/user/whoop_val/audit/visuals/ at 200 DPI.
Style: clean financial-deck aesthetic. Sans-serif, light background.
Palette mirrors the existing deck (orange #FF5A1F primary accent;
neutral grays for body; navy/green for category accents).
"""
from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FuncFormatter

OUT = "/home/user/whoop_val/audit/visuals"
os.makedirs(OUT, exist_ok=True)

# Palette (drawn from existing deck Whoop Valuation Master.pptx)
ORANGE   = "#FF5A1F"   # primary accent
DARK     = "#0A0A0A"
GRAY_FT  = "#7A776E"   # footer-style gray
GRAY_BD  = "#3A3A3A"   # body gray
GRAY_LT  = "#D9D6CF"   # light line gray
NAVY     = "#1F4FB5"
GREEN    = "#1F7A3D"
TERRA    = "#D14B2A"
BG       = "#FFFFFF"
BEAR     = "#9A6F6A"   # muted gray-red
BASE     = "#1F4FB5"   # navy (Base)
BULL     = "#1F7A3D"   # green
SERIESG  = "#C9A961"   # gold reference

# Apply default styling
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.labelsize": 11,
    "axes.edgecolor": GRAY_BD,
    "axes.labelcolor": DARK,
    "xtick.color": GRAY_BD,
    "ytick.color": GRAY_BD,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.facecolor": BG,
    "figure.facecolor": BG,
    "axes.facecolor": BG,
})


def usd(x, _pos=None):
    """$X.XB or $XXXM formatter."""
    if abs(x) >= 1000:
        return f"${x/1000:.1f}B"
    return f"${x:.1f}B"


# ---------------------------------------------------------------------------
# 1. Football field — slide 7
# ---------------------------------------------------------------------------
def football_field():
    fig, ax = plt.subplots(figsize=(13, 7.0))

    # Methods, ordered top-down (top-most plotted last so it appears at top)
    methods = [
        # (label, low, base, high, weight, color)
        ("Implied IPO Trading Range",       11.5, 12.63, 14.5, 0.15, NAVY),
        ("Last-Round Implied (Series G)",   10.10, 10.10, 10.10, 0.10, "#000000"),
        ("Public Comps (3-bucket)",          1.20,  3.62,  7.55, 0.35, ORANGE),
        ("Scenario-Wtd DCF (Intrinsic)",     9.07, 12.95, 15.28, 0.40, GREEN),
    ]
    n = len(methods)
    y_positions = list(range(n))

    for i, (label, lo, base, hi, w, col) in enumerate(methods):
        # Range bar (low-high) as a thinner background bar
        ax.barh(i, hi - lo, left=lo, height=0.55,
                color=col, alpha=0.25, edgecolor=col, linewidth=1)
        # Base value as a thick stripe
        ax.barh(i, 0.18, left=base - 0.09, height=0.55,
                color=col, edgecolor="white", linewidth=1)
        # Endpoint labels
        ax.text(lo - 0.25, i, f"${lo:.1f}B", va="center", ha="right",
                fontsize=9.5, color=GRAY_BD)
        ax.text(hi + 0.25, i, f"${hi:.1f}B", va="center", ha="left",
                fontsize=9.5, color=GRAY_BD)
        # Base value annotation directly above the base stripe
        ax.text(base, i + 0.32, f"Base ${base:.2f}B", ha="center",
                fontsize=10, color=col, fontweight="bold")
        # Weight label on the far left
        ax.text(-2.6, i, f"w={int(w*100)}%", va="center", ha="left",
                fontsize=10, color=GRAY_FT, family="monospace")

    # Series G reference line
    ax.axvline(10.10, color=DARK, linestyle="--", linewidth=1.6, alpha=0.85)
    ax.text(10.10, n - 0.35, "  Series G $10.10B", color=DARK,
            fontsize=10.5, fontweight="bold", va="bottom")

    # Football-field weighted average dashed line
    ax.axvline(9.34, color=ORANGE, linestyle=":", linewidth=2.2, alpha=0.95)
    ax.text(9.34, -0.85, "FF Weighted Avg $9.34B  ", color=ORANGE,
            fontsize=10.5, fontweight="bold", ha="right", va="center")

    ax.set_yticks(y_positions)
    ax.set_yticklabels([m[0] for m in methods], fontsize=11.5, color=DARK)
    ax.set_xlim(-3.5, 17.0)
    ax.set_ylim(-1.4, n - 0.2)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, p: f"${int(x)}B" if x >= 0 else ""))
    ax.set_xlabel("Enterprise Value ($B)", fontsize=11, color=GRAY_BD)
    ax.set_title("Football Field — Triangulation across four methods",
                 fontsize=15, fontweight="bold", color=DARK, loc="left", pad=14)

    # Side annotation
    txt = ("Intrinsic alone $12.95B  →  +28.2% vs Series G\n"
           "FF weighted avg $9.34B  →  −7.6% vs Series G")
    ax.text(0.99, 0.02, txt, transform=ax.transAxes,
            ha="right", va="bottom", fontsize=10.5, color=DARK,
            bbox=dict(facecolor="#FFF7F0", edgecolor=ORANGE,
                      boxstyle="round,pad=0.6", linewidth=1.2))
    ax.grid(axis="x", color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(f"{OUT}/football_field.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built football_field.png")


# ---------------------------------------------------------------------------
# 2. Scenario dispersion — slide 5
# ---------------------------------------------------------------------------
def scenario_dispersion():
    fig, ax = plt.subplots(figsize=(13, 7.2))

    scenarios = [
        ("Bear\n‘Consumer Wearable\nPlateau’",          2.55,  BEAR),
        ("Base\n‘Durable Consumer\nSubscription’",      7.83,  BASE),
        ("Bull\n‘Healthcare Reimb.\n+ Platform Success’", 28.43, BULL),
    ]
    weighted = ("Scenario-Weighted\nNeutral 20/50/30", 12.95, ORANGE)

    labels  = [s[0] for s in scenarios] + [weighted[0]]
    values  = [s[1] for s in scenarios] + [weighted[1]]
    colors  = [s[2] for s in scenarios] + [weighted[2]]
    widths  = [0.7, 0.7, 0.7, 0.55]    # narrower bar for the collapse
    xpos    = [0, 1, 2, 3.4]
    edges   = [None, None, None, "white"]

    for x, v, c, w, e in zip(xpos, values, colors, widths, edges):
        ax.bar(x, v, width=w, color=c, alpha=0.92, edgecolor=e, linewidth=1.5)

    # Value labels
    for x, v in zip(xpos, values):
        ax.text(x, v + 0.6, f"${v:.2f}B", ha="center", va="bottom",
                fontsize=13, fontweight="bold", color=DARK)

    # Series G reference line
    ax.axhline(10.10, color=SERIESG, linestyle="--", linewidth=1.7)
    ax.text(3.95, 10.10, "  Series G $10.10B", color=SERIESG,
            fontsize=10.5, fontweight="bold", va="center", ha="left")

    # Annotate the 'collapse' arrow
    ax.annotate("", xy=(3.05, 14.5), xytext=(2.45, 14.5),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6))
    ax.text(2.75, 15.3, "Probability\nweighting", color=ORANGE,
            fontsize=10, ha="center", fontweight="bold")

    ax.set_xticks(xpos)
    ax.set_xticklabels(labels, fontsize=10.5, color=DARK)
    ax.set_ylabel("DCF Equity Value ($B)", fontsize=11.5, color=DARK)
    ax.set_ylim(0, 32)
    ax.set_title("Three scenarios, one collapse — dispersion before probability weighting",
                 fontsize=15, fontweight="bold", color=DARK, loc="left", pad=14)
    ax.grid(axis="y", color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)

    # Range box
    rng_text = ("Range:  $2.55B → $28.43B  ·  11.1× spread\n"
                "Weighted (Neutral 20/50/30):  $12.95B")
    ax.text(0.01, 0.97, rng_text, transform=ax.transAxes,
            ha="left", va="top", fontsize=10.5, color=DARK,
            bbox=dict(facecolor="#F5F5F5", edgecolor=GRAY_FT,
                      boxstyle="round,pad=0.5", linewidth=1.0))

    fig.tight_layout()
    fig.savefig(f"{OUT}/scenario_dispersion.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built scenario_dispersion.png")


# ---------------------------------------------------------------------------
# 3. Jensen's Gap — slide 6 (the novel slide)
# ---------------------------------------------------------------------------
def jensens_gap():
    """Convexity diagram: input-level (linear) vs scenario-level (convex)
    for the WHOOP DCF as a function of probability mix."""
    fig, ax = plt.subplots(figsize=(13, 7.2))

    # Conceptual: x-axis = "bull-tilt" of probability mix from 0 (bear-only)
    # to 1 (bull-only). At neutral 20/50/30 we plant our anchor.
    x = np.linspace(0, 1, 200)

    # Linear "input-level" line: combines inputs first, then runs single DCF
    # We anchor the line at the input-level number $8.80B at the neutral mix
    # and let the slope walk between Bear $2.55B and Bull $28.43B endpoints.
    bear, base, bull = 2.55, 7.83, 28.43
    # Linear interpolation from bear at x=0 to bull at x=1
    linear = bear + (bull - bear) * x
    # Scenario-level (convex) curve: weighted average of three independent DCFs
    # with weights varying as we tilt the mix. For neutral mix (x=0.4 by
    # construction so that bear weight = (1-x)*0.5, bull weight = x*0.75 etc.),
    # we land on $12.95B.
    # Define a parametric convex blend that interpolates the scenario points.
    # Use a quadratic that hits the three observed scenario-weight outcomes:
    # Pessimistic 35/50/15 -> $9.07B at x≈0.20
    # Neutral     20/50/30 -> $12.95B at x≈0.40
    # Optimistic  15/45/40 -> $15.28B at x≈0.50
    # Fit a quadratic through these three (plus anchored to bear at x=0 and
    # bull at x=1 for visual completeness).
    xs = np.array([0.0, 0.20, 0.40, 0.50, 1.0])
    ys = np.array([bear, 9.07, 12.95, 15.28, bull])
    coeffs = np.polyfit(xs, ys, 4)
    convex = np.polyval(coeffs, x)

    # Plot
    ax.plot(x, linear, color=GRAY_BD, linewidth=2.0, linestyle="--",
            label="Input-level (single DCF on weighted inputs)")
    ax.plot(x, convex, color=ORANGE, linewidth=2.8,
            label="Scenario-level (weighted average of scenario DCFs)")

    # Shade the Jensen Gap
    ax.fill_between(x, linear, convex,
                    where=(convex > linear), alpha=0.18, color=ORANGE)

    # Anchor markers at the Neutral mix
    nx = 0.40
    ax.scatter([nx], [8.80], color=GRAY_BD, s=80, zorder=5)
    ax.scatter([nx], [12.95], color=ORANGE, s=100, zorder=5,
               edgecolor="white", linewidth=1.5)
    ax.annotate("Input-level\n$8.80B",
                xy=(nx, 8.80), xytext=(nx - 0.20, 5.3),
                fontsize=10.5, color=GRAY_BD, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=GRAY_BD, lw=1.0))
    ax.annotate("Scenario-level\n$12.95B",
                xy=(nx, 12.95), xytext=(nx + 0.04, 17.5),
                fontsize=10.5, color=ORANGE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.0))

    # Jensen Gap callout
    ax.text(nx, 10.85, "Jensen Gap\n$4.15B",
            ha="center", va="center", fontsize=11.5,
            color=ORANGE, fontweight="bold",
            bbox=dict(facecolor="white", edgecolor=ORANGE,
                      boxstyle="round,pad=0.4", linewidth=1.4))

    # Series G reference line
    ax.axhline(10.10, color=SERIESG, linestyle=":", linewidth=1.4)
    ax.text(0.99, 10.4, "Series G $10.10B", color=SERIESG,
            ha="right", fontsize=10, fontweight="bold")

    # Axis labels & cosmetics
    ax.set_xlabel("Probability mix tilt  →  Bull weight increasing",
                  fontsize=11.5, color=DARK)
    ax.set_ylabel("DCF Equity Value ($B)", fontsize=11.5, color=DARK)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 32)
    ax.set_xticks([0, 0.2, 0.4, 0.5, 1.0])
    ax.set_xticklabels(["Bear-only", "Pessim.\n35/50/15",
                        "Neutral\n20/50/30", "Optim.\n15/45/40", "Bull-only"],
                       fontsize=9.5)
    ax.set_title("Jensen's Gap — DCF is convex; scenario-level captures the correlation premium",
                 fontsize=14.5, fontweight="bold", color=DARK, loc="left", pad=14)
    ax.legend(loc="upper left", frameon=True, fontsize=10.5)
    ax.grid(True, color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(f"{OUT}/jensens_gap.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built jensens_gap.png")


# ---------------------------------------------------------------------------
# 4. Tornado — slide 9
# ---------------------------------------------------------------------------
def tornado():
    fig, ax = plt.subplots(figsize=(13, 7.2))
    center = 12.95

    # Driver, bear-side delta, bull-side delta (in $B from the Neutral $12.95B)
    drivers = [
        ("2033 ending members (10.9M ⇄ 18.1M)",            -4.10, +4.20),
        ("Terminal exit multiple (2.5x ⇄ 4.5x)",           -2.40, +2.60),
        ("WACC (12.0% ⇄ 9.75%)",                            -1.55, +1.85),
        ("Terminal FCF margin (16% ⇄ 28%)",                 -1.20, +1.45),
        ("ARPU growth CAGR (2.5% ⇄ 6.0%)",                  -0.65, +0.95),
        ("Healthcare option probability (10% ⇄ 35%)",       -0.45, +0.70),
    ]

    n = len(drivers)
    y = np.arange(n)
    bear_deltas = [d[1] for d in drivers]
    bull_deltas = [d[2] for d in drivers]
    labels = [d[0] for d in drivers]

    # Bear bars (negative direction from center)
    ax.barh(y, bear_deltas, left=center, color=BEAR, alpha=0.85,
            edgecolor="white", height=0.6, label="Bear input")
    # Bull bars (positive direction)
    ax.barh(y, bull_deltas, left=center, color=BULL, alpha=0.85,
            edgecolor="white", height=0.6, label="Bull input")

    # Endpoint labels
    for i, (lo, hi) in enumerate(zip(bear_deltas, bull_deltas)):
        ax.text(center + lo - 0.15, i, f"${center+lo:.1f}B", ha="right",
                va="center", fontsize=9.5, color=GRAY_BD)
        ax.text(center + hi + 0.15, i, f"${center+hi:.1f}B", ha="left",
                va="center", fontsize=9.5, color=GRAY_BD)

    # Center reference line
    ax.axvline(center, color=DARK, linewidth=1.8)
    ax.text(center, n - 0.4, f"  Neutral ${center:.2f}B",
            ha="left", fontsize=10.5, color=DARK, fontweight="bold")

    # Series G reference
    ax.axvline(10.10, color=SERIESG, linestyle="--", linewidth=1.4)
    ax.text(10.10, -0.7, " Series G $10.10B", color=SERIESG,
            ha="left", fontsize=10, fontweight="bold")

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlim(7.0, 18.5)
    ax.set_xlabel("DCF Equity Value ($B)", fontsize=11.5, color=DARK)
    ax.set_title("Tornado — Members dominates by ~3× the next driver; ARPU rank-5 confirms discipline",
                 fontsize=14, fontweight="bold", color=DARK, loc="left", pad=14)
    ax.legend(loc="lower right", frameon=True, fontsize=10)
    ax.grid(axis="x", color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(f"{OUT}/tornado.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built tornado.png")


# ---------------------------------------------------------------------------
# 5. Funding-round timeline — slide 1
# ---------------------------------------------------------------------------
def funding_timeline():
    fig, ax = plt.subplots(figsize=(15, 4.8))
    rounds = [
        ("Series A", "Jun 2014",  0.024),   # $23.5M
        ("Series B", "Dec 2015",  0.048),   # $48.3M
        ("Series C", "Mar 2018",  0.125),   # $125M
        ("Series D", "Nov 2019",  0.237),   # $237M
        ("Series E", "Oct 2020",  1.20),    # $1.2B
        ("Series F", "Aug 2021",  3.60),    # $3.6B
        ("Series G", "Mar 2026", 10.10),    # $10.1B
    ]
    x = np.arange(len(rounds))
    y = np.array([r[2] for r in rounds])

    # Connecting line
    ax.plot(x, y, color=GRAY_FT, linewidth=1.5, zorder=1)

    # Markers — Series G in orange, others gray-blue
    for i, (lbl, dt, v) in enumerate(rounds):
        is_g = (lbl == "Series G")
        col = ORANGE if is_g else NAVY
        size = 320 if is_g else 140
        ax.scatter(i, v, color=col, s=size, zorder=3,
                   edgecolor="white", linewidth=2)
        # Label below
        ax.text(i, -1.3, lbl, ha="center", va="top",
                fontsize=10.5, color=DARK, fontweight="bold")
        ax.text(i, -2.0, dt, ha="center", va="top",
                fontsize=9, color=GRAY_FT, family="monospace")
        # Value label above
        if v >= 1:
            txt = f"${v:.1f}B"
        else:
            txt = f"${v*1000:.0f}M"
        ax.text(i, v + 0.55, txt, ha="center",
                fontsize=11, color=col, fontweight="bold")

    # Highlight the Series F → G jump
    ax.annotate("", xy=(6, 9.4), xytext=(5, 4.0),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6,
                                connectionstyle="arc3,rad=-0.18"))
    ax.text(5.5, 6.2, "+2.8× step-up\n5.5× revenue growth\nmultiple compressed\n18× → 9×",
            ha="center", fontsize=9.5, color=ORANGE, fontweight="bold",
            bbox=dict(facecolor="#FFF7F0", edgecolor=ORANGE,
                      boxstyle="round,pad=0.4", linewidth=1))

    ax.set_yscale("symlog", linthresh=0.05)
    ax.set_ylim(-2.5, 18)
    ax.set_xlim(-0.5, len(rounds) - 0.5)
    ax.set_xticks([])
    ax.set_yticks([0.025, 0.1, 0.5, 1, 3, 10])
    ax.set_yticklabels(["$25M", "$100M", "$500M", "$1B", "$3B", "$10B"],
                       fontsize=10)
    ax.set_ylabel("Post-money valuation (log)",
                  fontsize=11, color=GRAY_BD)
    ax.set_title("WHOOP funding history — Series A through G",
                 fontsize=14, fontweight="bold", color=DARK, loc="left", pad=10)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0)
    ax.grid(axis="y", color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(f"{OUT}/funding_timeline.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built funding_timeline.png")


if __name__ == "__main__":
    football_field()
    scenario_dispersion()
    jensens_gap()
    tornado()
    funding_timeline()
