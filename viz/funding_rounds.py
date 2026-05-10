"""WHOOP funding-round chart — slide 1 of the IC deck.

Renders a single-panel dual-axis combo chart:
  - Bars: post-money valuation per round (left y-axis, $B)
  - Line: amount raised per round (right y-axis, $M)

Series G is highlighted in WHOOP orange. A dashed reference line at $10.1B
calls out the focal datapoint.

Output: output/charts/funding_rounds.png  (1600x900 px)

Source: research/whoop-pitchbook-data.md (Pitchbook, Session 1).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

# Make `viz/` importable when running as a script from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from whoop_style import (
    ACCENT, BG, FG, FG_2, FG_3, LINE,
    FONT_BODY, FONT_MONO,
    apply_base_style, add_eyebrow_title, add_footer,
)

# ── Data (Pitchbook-locked) ──────────────────────────────────────────────────
ROUNDS = [
    # (letter, year_label, post_money_usd, raised_usd, post_label, raised_label)
    ("A",  "2014",      23_500_000,        6_000_000,   "$23M",   "$6M"),
    ("B",  "2015",      48_310_000,       13_310_000,   "$48M",   "$13M"),
    ("C",  "2018",     125_000_000,       25_000_000,   "$125M",  "$25M"),
    ("D",  "2019",     237_400_000,       55_000_000,   "$237M",  "$55M"),
    ("E",  "2020",   1_200_000_000,      100_000_000,   "$1.2B",  "$100M"),
    ("F",  "2021",   3_600_000_000,      200_000_000,   "$3.6B",  "$200M"),
    ("G",  "Mar 2026", 10_100_000_000,    575_000_000,   "$10.1B", "$575M"),
]

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "output" / "charts" / "funding_rounds.png"


def render():
    body, mono = apply_base_style()

    fig = plt.figure(figsize=(16, 9), dpi=100)  # 1600x900 logical; we save at higher dpi
    # Plot area: leave room above for eyebrow+title and below for x-axis ticks + footer.
    ax = fig.add_axes([0.06, 0.13, 0.88, 0.66])

    # ── Left axis: post-money bars ───────────────────────────────────────────
    n = len(ROUNDS)
    x = list(range(n))
    post_vals = [r[2] / 1e9 for r in ROUNDS]   # $B
    raised_vals = [r[3] / 1e6 for r in ROUNDS]  # $M
    bar_colors = [ACCENT if r[0] == "G" else FG for r in ROUNDS]

    bars = ax.bar(
        x, post_vals,
        width=0.55,
        color=bar_colors,
        edgecolor="none",
        zorder=2,
    )

    # Bar value labels — placed above whichever is higher: bar top or
    # line marker at that x. Prevents the line from cutting through labels
    # at small bars where bar height is much less than the right-axis line.
    RIGHT_MAX = 1000.0  # keep in sync with ax2.set_ylim below
    LEFT_MAX = 12.0
    for i, (rec, height) in enumerate(zip(ROUNDS, post_vals)):
        line_y_in_left_scale = (raised_vals[i] / RIGHT_MAX) * LEFT_MAX
        label_anchor = max(height, line_y_in_left_scale) + 0.25
        is_g = rec[0] == "G"
        ax.text(
            i, label_anchor, rec[4],
            ha="center", va="bottom",
            fontfamily=body,
            fontsize=14 if is_g else 11,
            fontweight="semibold" if is_g else "medium",
            color=ACCENT if is_g else FG,
            zorder=4,
        )

    # Left y-axis cosmetics
    ax.set_ylim(0, 12)
    ax.set_yticks([0, 2, 4, 6, 8, 10, 12])
    ax.set_yticklabels(["$0", "$2B", "$4B", "$6B", "$8B", "$10B", "$12B"],
                       fontfamily=mono, fontsize=10, color=FG_3)
    ax.set_ylabel("POST-MONEY VALUATION", fontfamily=mono, fontsize=10,
                  color=FG_3, labelpad=14)
    # Horizontal gridlines only
    ax.yaxis.grid(True, color=LINE, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)

    # X-axis: two-tier tick (round letter + year) — done as text annotations
    # so we can style each tier independently.
    ax.set_xticks(x)
    ax.set_xticklabels([])
    ax.set_xlim(-0.6, n - 0.4)
    for i, rec in enumerate(ROUNDS):
        is_g = rec[0] == "G"
        ax.text(
            i, -0.55, rec[0],
            ha="center", va="top",
            fontfamily=body, fontsize=18,
            fontweight="bold",
            color=ACCENT if is_g else FG,
            transform=ax.transData,
        )
        ax.text(
            i, -1.10, rec[1],
            ha="center", va="top",
            fontfamily=mono, fontsize=10,
            color=FG_3,
            transform=ax.transData,
        )

    # ── Right axis: amount-raised line ───────────────────────────────────────
    ax2 = ax.twinx()
    ax2.plot(
        x, raised_vals,
        color=FG_3, linewidth=1.5,
        marker="o", markersize=6,
        markerfacecolor=FG_3, markeredgecolor=FG_3,
        zorder=3,
    )
    ax2.set_ylim(0, 1000)
    ax2.set_yticks([0, 200, 400, 600, 800, 1000])
    ax2.set_yticklabels(["$0", "$200M", "$400M", "$600M", "$800M", "$1B"],
                        fontfamily=mono, fontsize=10, color=FG_3)
    ax2.set_ylabel("AMOUNT RAISED", fontfamily=mono, fontsize=10,
                   color=FG_3, labelpad=14, rotation=270, va="bottom")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_color(LINE)
    ax2.tick_params(axis="y", length=0)

    # Label only the Series G amount-raised marker — others read off the
    # right y-axis. Per-marker labels in the early rounds collided with
    # bar value labels (small bars + line near zero share the same vertical
    # space).
    g_idx = next(i for i, r in enumerate(ROUNDS) if r[0] == "G")
    ax2.annotate(
        ROUNDS[g_idx][5] + " raised",
        xy=(g_idx, raised_vals[g_idx]),
        xytext=(-18, 0), textcoords="offset points",
        ha="right", va="center",
        fontfamily=mono, fontsize=10, color=FG_2,
        zorder=4,
    )

    # ── Reference line at $10.1B ─────────────────────────────────────────────
    ax.axhline(y=10.1, color=FG, linestyle=(0, (4, 4)), linewidth=1, zorder=1)
    # Callout on left side, above the line (away from the Series G bar so labels
    # don't collide).
    ax.text(
        -0.45, 10.35, "$10.1B — SERIES G",
        ha="left", va="bottom",
        fontfamily=mono, fontsize=10, color=FG,
        fontweight="medium",
        zorder=5,
    )

    # ── Header + footer ──────────────────────────────────────────────────────
    add_eyebrow_title(
        fig,
        eyebrow="WHOOP — FUNDING TRAJECTORY",
        title="Each round has been a step up. Is this one too far?",
    )
    add_footer(fig, source="Pitchbook", as_of="May 2026")

    # ── Export ───────────────────────────────────────────────────────────────
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=100, facecolor=BG, edgecolor=BG)
    plt.close(fig)
    print(f"wrote {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    render()
