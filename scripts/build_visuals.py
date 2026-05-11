"""Build all visuals for the WHOOP Yannelis IC deck.

All saved to /home/user/whoop_val/audit/visuals/ at 200 DPI.
Style: clean financial-deck aesthetic. Sans-serif, light background.
Palette mirrors the existing deck (orange #FF5A1F primary accent;
neutral grays for body; navy/green for category accents).

Visuals built (in run order):
  1. funding_timeline.png      — Slide 1 title hero
  2. football_field.png        — Slide 10 triangulation (IPO range updated)
  3. scenario_dispersion.png   — Slide 8 dispersion
  4. jensens_gap.png           — Slide 9 (now with all 3 weight schemes)
  5. tornado.png               — kept for backup, not in deck anymore
  6. assumption_inventory.png  — Slide 4 NEW (Section 14)
  7. sensitivity_heatmap.png   — Slide 12 NEW (Grid 6 + driver sensitivities)
  8. comp_scatter.png          — Slide 13 NEW (X=growth, Y=EV/Rev)
  9. comp_bracketing.png       — Slide 13 NEW (T1/T2/T3 strip)
"""
from __future__ import annotations
import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FuncFormatter, MaxNLocator
from pathlib import Path

OUT = "/home/user/whoop_val/audit/visuals"
os.makedirs(OUT, exist_ok=True)

# Load anchors
M = json.loads(Path("/home/user/whoop_val/audit/model_outputs.json").read_text())

# Palette
ORANGE   = "#FF5A1F"
DARK     = "#0A0A0A"
GRAY_FT  = "#7A776E"
GRAY_BD  = "#3A3A3A"
GRAY_LT  = "#D9D6CF"
NAVY     = "#1F4FB5"
GREEN    = "#1F7A3D"
TERRA    = "#D14B2A"
BG       = "#FFFFFF"
BEAR     = "#9A6F6A"
BASE     = "#1F4FB5"
BULL     = "#1F7A3D"
SERIESG  = "#C9A961"

# Section colors (for assumption inventory)
SECTION_COLORS = {
    "§1": "#8B5A3C",   # Cohort
    "§2": "#1F4FB5",   # OpEx / SBC
    "§3": "#7A2E8E",   # FCF / Tax
    "§4": "#C9A961",   # WACC
    "§5": "#1F7A3D",   # TV
    "§10": "#D14B2A",  # ARPU / COGS
    "§12": "#FF5A1F",  # Members
}


def _section_color(section_str: str) -> str:
    if not section_str: return GRAY_BD
    for prefix, color in SECTION_COLORS.items():
        if section_str.startswith(prefix):
            return color
    return GRAY_BD


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
    if abs(x) >= 1000:
        return f"${x/1000:.1f}B"
    return f"${x:.1f}B"


# ===========================================================
# 1. Funding timeline — unchanged
# ===========================================================
def funding_timeline():
    fig, ax = plt.subplots(figsize=(15, 4.8))
    rounds = [
        ("Series A", "Jun 2014",  0.024),
        ("Series B", "Dec 2015",  0.048),
        ("Series C", "Mar 2018",  0.125),
        ("Series D", "Nov 2019",  0.237),
        ("Series E", "Oct 2020",  1.20),
        ("Series F", "Aug 2021",  3.60),
        ("Series G", "Mar 2026", 10.10),
    ]
    x = np.arange(len(rounds))
    y = np.array([r[2] for r in rounds])
    ax.plot(x, y, color=GRAY_FT, linewidth=1.5, zorder=1)
    for i, (lbl, dt, v) in enumerate(rounds):
        is_g = (lbl == "Series G")
        col = ORANGE if is_g else NAVY
        size = 320 if is_g else 140
        ax.scatter(i, v, color=col, s=size, zorder=3, edgecolor="white", linewidth=2)
        ax.text(i, -1.3, lbl, ha="center", va="top", fontsize=10.5, color=DARK, fontweight="bold")
        ax.text(i, -2.0, dt, ha="center", va="top", fontsize=9, color=GRAY_FT, family="monospace")
        txt = f"${v:.1f}B" if v >= 1 else f"${v*1000:.0f}M"
        ax.text(i, v + 0.55, txt, ha="center", fontsize=11, color=col, fontweight="bold")
    ax.annotate("", xy=(6, 9.4), xytext=(5, 4.0),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6,
                                connectionstyle="arc3,rad=-0.18"))
    ax.text(5.5, 6.2, "+2.8× step-up\n5.5× revenue growth\nmultiple compressed\n18× → 9×",
            ha="center", fontsize=9.5, color=ORANGE, fontweight="bold",
            bbox=dict(facecolor="#FFF7F0", edgecolor=ORANGE, boxstyle="round,pad=0.4", linewidth=1))
    ax.set_yscale("symlog", linthresh=0.05)
    ax.set_ylim(-2.5, 18)
    ax.set_xlim(-0.5, len(rounds) - 0.5)
    ax.set_xticks([])
    ax.set_yticks([0.025, 0.1, 0.5, 1, 3, 10])
    ax.set_yticklabels(["$25M", "$100M", "$500M", "$1B", "$3B", "$10B"], fontsize=10)
    ax.set_ylabel("Post-money valuation (log)", fontsize=11, color=GRAY_BD)
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


# ===========================================================
# 2. Football field — REFRESHED with new IPO range $13.2-19.7B
# ===========================================================
def football_field():
    fig, ax = plt.subplots(figsize=(13, 7.0))
    # Pull live values from the refreshed JSON
    ipo = M.get("ipo_range", {})
    ipo_lo  = float(ipo.get("bear",  13.24))
    ipo_b   = float(ipo.get("base",  14.69))
    ipo_hi  = float(ipo.get("bull",  19.71))

    ff = M.get("ff_rows", {})
    dcf_lo = ff.get("row_6", {}).get("low", M["bear_equity"]/1000)
    dcf_b  = ff.get("row_6", {}).get("base", M["base_equity"]/1000)
    dcf_hi = ff.get("row_6", {}).get("high", M["bull_equity"]/1000)
    sw_lo  = ff.get("row_9", {}).get("low", M["scen_pess"]/1000)
    sw_b   = ff.get("row_9", {}).get("base", M["scen_neu"]/1000)
    sw_hi  = ff.get("row_9", {}).get("high", M["scen_opt"]/1000)
    cmp_lo = ff.get("row_10", {}).get("low", 1.18)
    cmp_b  = ff.get("row_10", {}).get("base", 3.57)
    cmp_hi = ff.get("row_10", {}).get("high", 7.55)

    methods = [
        ("Implied IPO Trading Range",       ipo_lo, ipo_b, ipo_hi, 0.15, NAVY),
        ("Last-Round Implied (Series G)",   10.10, 10.10, 10.10,   0.10, "#000000"),
        ("Public Comps (3-bucket)",          cmp_lo, cmp_b, cmp_hi, 0.35, ORANGE),
        ("Scenario-Wtd DCF (Intrinsic)",     sw_lo, sw_b, sw_hi,    0.40, GREEN),
    ]
    n = len(methods)
    for i, (label, lo, base, hi, w, col) in enumerate(methods):
        ax.barh(i, hi - lo, left=lo, height=0.55,
                color=col, alpha=0.25, edgecolor=col, linewidth=1)
        ax.barh(i, 0.25, left=base - 0.125, height=0.55,
                color=col, edgecolor="white", linewidth=1)
        ax.text(lo - 0.3, i, f"${lo:.2f}B", va="center", ha="right",
                fontsize=9.5, color=GRAY_BD)
        ax.text(hi + 0.3, i, f"${hi:.2f}B", va="center", ha="left",
                fontsize=9.5, color=GRAY_BD)
        ax.text(base, i + 0.34, f"Base ${base:.2f}B", ha="center",
                fontsize=10, color=col, fontweight="bold")
        ax.text(-3.2, i, f"w={int(w*100)}%", va="center", ha="left",
                fontsize=10, color=GRAY_FT, family="monospace")

    # Series G ref
    ax.axvline(10.10, color=DARK, linestyle="--", linewidth=1.6, alpha=0.85)
    ax.text(10.10, n - 0.35, "  Series G $10.10B", color=DARK,
            fontsize=10.5, fontweight="bold", va="bottom")

    # FF weighted average line
    ff_wavg = float(M.get("ff_d18", 9.09))
    ax.axvline(ff_wavg, color=ORANGE, linestyle=":", linewidth=2.2, alpha=0.95)
    ax.text(ff_wavg, -0.85, f"FF Weighted Avg ${ff_wavg:.2f}B  ", color=ORANGE,
            fontsize=10.5, fontweight="bold", ha="right", va="center")

    ax.set_yticks(range(n))
    ax.set_yticklabels([m[0] for m in methods], fontsize=11.5, color=DARK)
    ax.set_xlim(-4.5, 22.0)
    ax.set_ylim(-1.4, n - 0.2)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, p: f"${int(x)}B" if x >= 0 else ""))
    ax.set_xlabel("Enterprise Value ($B)", fontsize=11, color=GRAY_BD)
    ax.set_title("Football Field — Triangulation across four methods",
                 fontsize=15, fontweight="bold", color=DARK, loc="left", pad=14)

    prem_int = (sw_b * 1000 / 10100) - 1
    prem_ff  = (ff_wavg * 1000 / 10100) - 1
    txt = (f"Intrinsic alone ${sw_b:.2f}B  →  {prem_int*100:+.1f}% vs Series G\n"
           f"FF weighted avg ${ff_wavg:.2f}B  →  {prem_ff*100:+.1f}% vs Series G")
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


# ===========================================================
# 3. Scenario dispersion — refreshed numbers
# ===========================================================
def scenario_dispersion():
    fig, ax = plt.subplots(figsize=(13, 7.2))
    bear = M["bear_equity"] / 1000
    base = M["base_equity"] / 1000
    bull = M["bull_equity"] / 1000
    neu  = M["scen_neu"] / 1000

    scenarios = [
        (f"Bear\n'Consumer Wearable\nPlateau'",          bear,  BEAR),
        (f"Base\n'Durable Consumer\nSubscription'",      base,  BASE),
        (f"Bull\n'Healthcare Reimb.\n+ Platform Success'", bull, BULL),
    ]
    weighted = ("Scenario-Weighted\nNeutral 20/50/30", neu, ORANGE)

    labels  = [s[0] for s in scenarios] + [weighted[0]]
    values  = [s[1] for s in scenarios] + [weighted[1]]
    colors  = [s[2] for s in scenarios] + [weighted[2]]
    widths  = [0.7, 0.7, 0.7, 0.55]
    xpos    = [0, 1, 2, 3.4]
    edges   = [None, None, None, "white"]

    for x, v, c, w, e in zip(xpos, values, colors, widths, edges):
        ax.bar(x, v, width=w, color=c, alpha=0.92, edgecolor=e, linewidth=1.5)
    for x, v in zip(xpos, values):
        ax.text(x, v + 0.6, f"${v:.2f}B", ha="center", va="bottom",
                fontsize=13, fontweight="bold", color=DARK)
    ax.axhline(10.10, color=SERIESG, linestyle="--", linewidth=1.7)
    ax.text(3.95, 10.10, "  Series G $10.10B", color=SERIESG,
            fontsize=10.5, fontweight="bold", va="center", ha="left")
    ax.annotate("", xy=(3.05, 14.5), xytext=(2.45, 14.5),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6))
    ax.text(2.75, 15.3, "Probability\nweighting", color=ORANGE,
            fontsize=10, ha="center", fontweight="bold")
    ax.set_xticks(xpos)
    ax.set_xticklabels(labels, fontsize=10.5, color=DARK)
    ax.set_ylabel("DCF Equity Value ($B)", fontsize=11.5, color=DARK)
    ax.set_ylim(0, max(bull, 32) * 1.05)
    ax.set_title("Three scenarios, one collapse — dispersion before probability weighting",
                 fontsize=15, fontweight="bold", color=DARK, loc="left", pad=14)
    ax.grid(axis="y", color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    rng_text = (f"Range:  ${bear:.2f}B → ${bull:.2f}B  ·  {bull/bear:.1f}× spread\n"
                f"Weighted (Neutral 20/50/30):  ${neu:.2f}B")
    ax.text(0.01, 0.97, rng_text, transform=ax.transAxes,
            ha="left", va="top", fontsize=10.5, color=DARK,
            bbox=dict(facecolor="#F5F5F5", edgecolor=GRAY_FT,
                      boxstyle="round,pad=0.5", linewidth=1.0))
    fig.tight_layout()
    fig.savefig(f"{OUT}/scenario_dispersion.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built scenario_dispersion.png")


# ===========================================================
# 4. Jensen's gap — NOW WITH ALL 3 WEIGHT SCHEMES
# ===========================================================
def jensens_gap():
    fig, ax = plt.subplots(figsize=(13, 7.2))
    bear = M["bear_equity"] / 1000
    bull = M["bull_equity"] / 1000

    # Three scheme anchor points (x = bull-tilt, y = scen-wtd vs input-wtd)
    schemes = M["weight_schemes"]
    # X coordinate = relative bull weight tilt
    # Pessimistic: p_bull=0.15 → x≈0.20
    # Neutral:     p_bull=0.30 → x≈0.40
    # Optimistic:  p_bull=0.40 → x≈0.50
    pess = schemes["pessimistic"]
    neu  = schemes["neutral"]
    opt  = schemes["optimistic"]

    x = np.linspace(0, 1, 200)
    # Linear input-level curve (passes through input-level at each scheme)
    # Anchor: x=0 → Bear $B, x=1 → Bull $B
    linear = bear + (bull - bear) * x
    # Convex scenario-level curve fit through Pessimistic/Neutral/Optimistic + endpoints
    xs = np.array([0.0, 0.20, 0.40, 0.50, 1.0])
    ys = np.array([bear,
                   pess["scen_wtd"] / 1000,
                   neu["scen_wtd"] / 1000,
                   opt["scen_wtd"] / 1000,
                   bull])
    coeffs = np.polyfit(xs, ys, 4)
    convex = np.polyval(coeffs, x)

    # Plot curves
    ax.plot(x, linear, color=GRAY_BD, linewidth=2.0, linestyle="--",
            label="Input-level (single DCF on prob-weighted inputs)")
    ax.plot(x, convex, color=ORANGE, linewidth=2.8,
            label="Scenario-level (probability-weighted DCF outputs)")
    ax.fill_between(x, linear, convex,
                    where=(convex > linear), alpha=0.18, color=ORANGE)

    # Plot all 3 scheme markers (paired: input-level on dashed, scenario-level on convex)
    scheme_pts = [
        ("Pessimistic\n35/50/15", 0.20, pess["prob_wtd"]/1000, pess["scen_wtd"]/1000),
        ("Neutral\n20/50/30",     0.40, neu["prob_wtd"]/1000,  neu["scen_wtd"]/1000),
        ("Optimistic\n15/45/40",  0.50, opt["prob_wtd"]/1000,  opt["scen_wtd"]/1000),
    ]
    for lbl, sx, inp_y, sc_y in scheme_pts:
        # Input-level marker
        ax.scatter([sx], [inp_y], color=GRAY_BD, s=72, zorder=5,
                   edgecolor="white", linewidth=1.5)
        # Scenario-level marker
        ax.scatter([sx], [sc_y], color=ORANGE, s=110, zorder=5,
                   edgecolor="white", linewidth=1.6)
        # Gap connector
        ax.plot([sx, sx], [inp_y, sc_y], color=ORANGE, linewidth=1.5,
                linestyle=":", alpha=0.7, zorder=4)
        # Gap label
        gap = sc_y - inp_y
        ax.text(sx + 0.015, (inp_y + sc_y) / 2,
                f"${gap:.2f}B\ngap", color=ORANGE, fontsize=9,
                fontweight="bold", va="center")
        # Bottom scheme label
        ax.text(sx, inp_y - 1.0, lbl, ha="center", va="top",
                fontsize=9.0, color=GRAY_BD)

    # Highlight Neutral (headline)
    ax.scatter([0.40], [neu["scen_wtd"]/1000], color=ORANGE, s=220,
               zorder=6, edgecolor=DARK, linewidth=2, marker="o")
    ax.annotate(f"Headline\n${neu['scen_wtd']/1000:.2f}B",
                xy=(0.40, neu["scen_wtd"]/1000),
                xytext=(0.52, 15.5),
                fontsize=11, color=DARK, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=DARK, lw=1.2))

    # Series G ref
    ax.axhline(10.10, color=SERIESG, linestyle=":", linewidth=1.4)
    ax.text(0.99, 10.4, "Series G $10.10B", color=SERIESG,
            ha="right", fontsize=10, fontweight="bold")

    ax.set_xlabel("Probability mix tilt  →  Bull weight increasing",
                  fontsize=11.5, color=DARK)
    ax.set_ylabel("DCF Equity Value ($B)", fontsize=11.5, color=DARK)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, max(bull, 32) * 1.02)
    ax.set_xticks([0, 0.2, 0.4, 0.5, 1.0])
    ax.set_xticklabels(["Bear-only", "Pessim.\n35/50/15",
                        "Neutral\n20/50/30", "Optim.\n15/45/40", "Bull-only"],
                       fontsize=9.5)
    ax.set_title("Jensen's Gap — convexity widens with Bull weight; all three weight schemes show it",
                 fontsize=14, fontweight="bold", color=DARK, loc="left", pad=14)
    ax.legend(loc="upper left", frameon=True, fontsize=10.5)
    ax.grid(True, color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(f"{OUT}/jensens_gap.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built jensens_gap.png")


# ===========================================================
# 5. Tornado — kept for backup only (not embedded in deck)
# ===========================================================
def tornado():
    fig, ax = plt.subplots(figsize=(13, 7.2))
    center = M["scen_neu"] / 1000
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
    ax.barh(y, bear_deltas, left=center, color=BEAR, alpha=0.85,
            edgecolor="white", height=0.6, label="Bear input")
    ax.barh(y, bull_deltas, left=center, color=BULL, alpha=0.85,
            edgecolor="white", height=0.6, label="Bull input")
    for i, (lo, hi) in enumerate(zip(bear_deltas, bull_deltas)):
        ax.text(center + lo - 0.15, i, f"${center+lo:.1f}B", ha="right",
                va="center", fontsize=9.5, color=GRAY_BD)
        ax.text(center + hi + 0.15, i, f"${center+hi:.1f}B", ha="left",
                va="center", fontsize=9.5, color=GRAY_BD)
    ax.axvline(center, color=DARK, linewidth=1.8)
    ax.text(center, n - 0.4, f"  Neutral ${center:.2f}B",
            ha="left", fontsize=10.5, color=DARK, fontweight="bold")
    ax.axvline(10.10, color=SERIESG, linestyle="--", linewidth=1.4)
    ax.text(10.10, -0.7, " Series G $10.10B", color=SERIESG,
            ha="left", fontsize=10, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlim(7.0, 18.5)
    ax.set_xlabel("DCF Equity Value ($B)", fontsize=11.5, color=DARK)
    ax.set_title("Tornado — Members dominates by ~3× the next driver",
                 fontsize=14, fontweight="bold", color=DARK, loc="left", pad=14)
    ax.legend(loc="lower right", frameon=True, fontsize=10)
    ax.grid(axis="x", color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(f"{OUT}/tornado.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built tornado.png")


# ===========================================================
# 6. NEW — Assumption inventory (Section 14)
# ===========================================================
def assumption_inventory():
    """Two-panel view of all 20 ProbWeighted drivers.

    LEFT: scenario range as % of base (Bull-Bear)/|Base|, sorted descending
    RIGHT: numeric Bear/Base/Bull/Active table-as-figure for the SAME 20 drivers
    """
    inv = M.get("inventory", [])
    # Compute scenario range % for sorting
    def scen_pct(d):
        b = d.get("base")
        if not b or abs(b) < 1e-6: return 0
        spread = (d.get("bull") or 0) - (d.get("bear") or 0)
        return abs(spread) / abs(b)
    sorted_inv = sorted(inv, key=scen_pct, reverse=True)
    pcts = [scen_pct(d) for d in sorted_inv]

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(20, 9.0),
                                   gridspec_kw={"width_ratios": [1.0, 1.0]})

    # LEFT panel — ranked bar chart
    n = len(sorted_inv)
    y = np.arange(n)
    colors = [_section_color(d.get("section", "")) for d in sorted_inv]
    labels = [d.get("driver", "—") for d in sorted_inv]

    axL.barh(y, [p * 100 for p in pcts], color=colors, alpha=0.88,
             edgecolor="white", height=0.7)
    for i, p in enumerate(pcts):
        axL.text(p * 100 + 1.5, i, f"{p*100:.0f}%", va="center",
                 fontsize=9.5, color=GRAY_BD)
    axL.set_yticks(y)
    axL.set_yticklabels(labels, fontsize=9.5, color=DARK)
    axL.invert_yaxis()
    axL.set_xlabel("Scenario range (Bull − Bear) as % of |Base|",
                   fontsize=11, color=DARK)
    axL.set_title("Assumption inventory — drivers ranked by scenario sensitivity",
                  fontsize=13.5, fontweight="bold", color=DARK, loc="left", pad=12)
    axL.set_xlim(0, max(p * 100 for p in pcts) * 1.18)
    axL.grid(axis="x", color=GRAY_LT, linewidth=0.6, alpha=0.7)
    axL.set_axisbelow(True)

    # Section legend (top-right of left panel)
    legend_entries = [
        ("§1 Cohort",   SECTION_COLORS["§1"]),
        ("§2 OpEx/SBC", SECTION_COLORS["§2"]),
        ("§3 FCF/Tax",  SECTION_COLORS["§3"]),
        ("§4 WACC",     SECTION_COLORS["§4"]),
        ("§5 TV",       SECTION_COLORS["§5"]),
        ("§10 ARPU/COGS", SECTION_COLORS["§10"]),
        ("§12 Members", SECTION_COLORS["§12"]),
    ]
    patches = [mpatches.Patch(color=c, label=l) for l, c in legend_entries]
    axL.legend(handles=patches, loc="lower right", fontsize=8.5,
               frameon=True, ncol=2)

    # RIGHT panel — table-as-figure: driver / Bear / Base / Bull / Weighted
    axR.axis("off")
    axR.set_title("Bear · Base · Bull · ProbWeighted blend (live values)",
                  fontsize=13.5, fontweight="bold", color=DARK, loc="left", pad=12)

    # Header
    hdr_y = 0.97
    cols = ["Driver", "Bear", "Base", "Bull", "Wtd"]
    col_x = [0.02, 0.58, 0.69, 0.80, 0.92]
    aligns = ["left", "right", "right", "right", "right"]
    for cx, lbl, al in zip(col_x, cols, aligns):
        axR.text(cx, hdr_y, lbl, transform=axR.transAxes,
                 fontsize=10.5, fontweight="bold", color=GRAY_BD, ha=al)
    axR.plot([0.02, 0.98], [hdr_y - 0.015, hdr_y - 0.015],
             transform=axR.transAxes, color=GRAY_BD, linewidth=1)

    # Format helper — dispatch on magnitude
    def fmt_val(v, driver_name):
        if v is None: return "—"
        if isinstance(v, str): return v
        if "Multiple" in driver_name: return f"{v:.1f}×"
        if abs(v) < 1.5: return f"{v*100:.1f}%"
        return f"{v:.3g}"

    row_h = (hdr_y - 0.04) / max(n, 1)
    for i, d in enumerate(sorted_inv):
        y_pos = hdr_y - 0.025 - (i + 1) * row_h
        # Section color tag (small left bar)
        c = _section_color(d.get("section", ""))
        axR.add_patch(mpatches.Rectangle((0.0, y_pos - row_h * 0.32),
                                         0.012, row_h * 0.65,
                                         transform=axR.transAxes,
                                         facecolor=c, edgecolor="none"))
        axR.text(col_x[0], y_pos, d.get("driver", "—")[:36],
                 transform=axR.transAxes, fontsize=8.5, color=DARK, ha="left")
        axR.text(col_x[1], y_pos, fmt_val(d.get("bear"), d.get("driver", "")),
                 transform=axR.transAxes, fontsize=8.5, color=BEAR, ha="right")
        axR.text(col_x[2], y_pos, fmt_val(d.get("base"), d.get("driver", "")),
                 transform=axR.transAxes, fontsize=8.5,
                 color=NAVY, ha="right", weight="bold")
        axR.text(col_x[3], y_pos, fmt_val(d.get("bull"), d.get("driver", "")),
                 transform=axR.transAxes, fontsize=8.5, color=BULL, ha="right")
        axR.text(col_x[4], y_pos,
                 fmt_val(d.get("weighted"), d.get("driver", "")),
                 transform=axR.transAxes, fontsize=8.5, color=ORANGE, ha="right")

    fig.suptitle("", y=0.99)
    fig.tight_layout()
    fig.savefig(f"{OUT}/assumption_inventory.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built assumption_inventory.png")


# ===========================================================
# 7. NEW — Sensitivity heatmap + driver sensitivity panels
# ===========================================================
def sensitivity_heatmap():
    fig = plt.figure(figsize=(20, 9.0))
    gs = fig.add_gridspec(3, 3, height_ratios=[1, 1, 1],
                          width_ratios=[1.4, 0.05, 1.0], hspace=0.55, wspace=0.05)

    # ----- LEFT: Grid 6 — P_Bear × P_Bull heatmap (spans all 3 rows) -----
    axH = fig.add_subplot(gs[:, 0])
    g6 = M.get("grid6", {})
    p_bull_axis = g6.get("p_bull_axis", [0.2, 0.25, 0.30, 0.35, 0.40])
    rows = g6.get("rows", [])
    p_bear_axis = [r["p_bear"] for r in rows]
    Z = np.array([r["equity_b"] for r in rows], dtype=float)

    # Grid 6 stored in $M — convert to $B for display
    Z_B = Z / 1000.0
    im = axH.imshow(Z_B, cmap="RdYlGn", aspect="auto", origin="upper")
    # Cell labels
    vmid = (Z_B.min() + Z_B.max()) / 2
    for i in range(Z_B.shape[0]):
        for j in range(Z_B.shape[1]):
            val = Z_B[i, j]
            color = "white" if val > vmid + (Z_B.max() - vmid) * 0.55 else "black"
            axH.text(j, i, f"${val:.2f}B", ha="center", va="center",
                     fontsize=11, color=color, fontweight="bold")
    axH.set_xticks(range(len(p_bull_axis)))
    axH.set_xticklabels([f"{p*100:.0f}%" for p in p_bull_axis], fontsize=10.5)
    axH.set_yticks(range(len(p_bear_axis)))
    axH.set_yticklabels([f"{p*100:.0f}%" for p in p_bear_axis], fontsize=10.5)
    axH.set_xlabel("P(Bull)  →", fontsize=11.5, color=DARK)
    axH.set_ylabel("P(Bear)  ↓", fontsize=11.5, color=DARK)
    axH.set_title("Grid 6 — Scenario-weighted DCF equity ($B) across P_Bear × P_Bull",
                  fontsize=13, fontweight="bold", color=DARK, loc="left", pad=12)

    # Highlight Neutral 20/50/30 (P_Bear=0.20, P_Bull=0.30)
    try:
        bear_idx = p_bear_axis.index(0.20)
        bull_idx = p_bull_axis.index(0.30)
        axH.add_patch(mpatches.Rectangle(
            (bull_idx - 0.5, bear_idx - 0.5), 1, 1,
            fill=False, edgecolor=DARK, linewidth=3))
        axH.text(bull_idx, bear_idx - 0.62, "Headline 20/50/30",
                 ha="center", color=DARK, fontsize=10, fontweight="bold",
                 bbox=dict(facecolor="white", edgecolor=DARK, boxstyle="round,pad=0.2",
                           linewidth=1))
    except (ValueError, IndexError):
        pass

    # Colorbar
    cbar = fig.colorbar(im, ax=axH, fraction=0.04, pad=0.02)
    cbar.set_label("Equity ($B)", fontsize=10.5, color=DARK)
    cbar.ax.tick_params(labelsize=9)

    # ----- RIGHT: 3 driver sensitivity panels stacked -----
    # (A) Members (Grid 7) → EV
    axA = fig.add_subplot(gs[0, 2])
    g7 = M.get("grid7", [])
    if g7:
        # Use the "EV Coupled" column when present, else EV constant
        members  = [r["members_2033"] for r in g7]
        ev_vals  = [(r.get("ev_coupled") or r.get("ev_const") or 0) / 1000 for r in g7]
        labels   = [(r.get("lens") or "")[:32] for r in g7]
        axA.barh(range(len(members)), ev_vals, color=ORANGE, alpha=0.85,
                 edgecolor="white", height=0.7)
        axA.set_yticks(range(len(members)))
        axA.set_yticklabels(labels, fontsize=8.5)
        axA.invert_yaxis()
        for i, (m, e) in enumerate(zip(members, ev_vals)):
            axA.text(e + 0.15, i, f"{m:.1f}M → ${e:.1f}B",
                     va="center", fontsize=8.5, color=GRAY_BD)
        axA.set_xlabel("DCF Equity ($B)", fontsize=10, color=GRAY_BD)
        axA.set_title("Members lens — 2033 endpoint sensitivity (most material driver)",
                      fontsize=10.5, fontweight="bold", color=DARK, loc="left", pad=8)
        axA.axvline(M["base_equity"]/1000, color=NAVY, linestyle="--", linewidth=1.2)
        axA.set_xlim(0, max(ev_vals) * 1.30)
        axA.grid(axis="x", color=GRAY_LT, linewidth=0.5, alpha=0.7)
        axA.set_axisbelow(True)

    # (B) WACC (extracted from Grid 1 column at 3.5x exit multiple)
    axB = fig.add_subplot(gs[1, 2])
    g1 = M.get("grid1", {})
    exit_axis = g1.get("exit_mult_axis", [])
    g1_rows = g1.get("rows", [])
    if exit_axis and g1_rows:
        # Find the 3.5 column index
        try:
            col_35 = exit_axis.index(3.5)
        except ValueError:
            col_35 = min(range(len(exit_axis)), key=lambda i: abs(exit_axis[i] - 3.5))
        waccs = [r["wacc"] for r in g1_rows]
        evs   = [r["equity_b"][col_35] for r in g1_rows]
        # Bar chart vertical (WACC on x-axis, EV on y)
        axB.bar(range(len(waccs)), evs, color=BASE, alpha=0.85,
                edgecolor="white")
        axB.set_xticks(range(len(waccs)))
        axB.set_xticklabels([f"{w*100:.1f}%" for w in waccs], fontsize=8.5)
        axB.set_xlabel("WACC", fontsize=10, color=GRAY_BD)
        axB.set_ylabel("Equity ($B)", fontsize=9.5, color=GRAY_BD)
        axB.set_title("WACC sensitivity — at 3.5× exit multiple",
                      fontsize=10.5, fontweight="bold", color=DARK, loc="left", pad=8)
        for i, v in enumerate(evs):
            axB.text(i, v + 0.15, f"${v:.1f}B", ha="center",
                     fontsize=8, color=GRAY_BD)
        # Highlight base
        base_wacc = M.get("wacc_base", 0.1159)
        idx_base = min(range(len(waccs)), key=lambda i: abs(waccs[i] - base_wacc))
        axB.patches[idx_base].set_facecolor(ORANGE)
        axB.grid(axis="y", color=GRAY_LT, linewidth=0.5, alpha=0.7)
        axB.set_axisbelow(True)

    # (C) Terminal Multiple (extracted from Grid 1 row at base WACC)
    axC = fig.add_subplot(gs[2, 2])
    if exit_axis and g1_rows:
        base_wacc = M.get("wacc_base", 0.1159)
        idx_base_row = min(range(len(g1_rows)),
                           key=lambda i: abs(g1_rows[i]["wacc"] - base_wacc))
        mults = exit_axis
        evs2  = g1_rows[idx_base_row]["equity_b"]
        axC.bar(range(len(mults)), evs2, color=GREEN, alpha=0.85,
                edgecolor="white")
        axC.set_xticks(range(len(mults)))
        axC.set_xticklabels([f"{m:.1f}×" for m in mults], fontsize=8.5)
        axC.set_xlabel("Terminal EV/Revenue multiple", fontsize=10, color=GRAY_BD)
        axC.set_ylabel("Equity ($B)", fontsize=9.5, color=GRAY_BD)
        axC.set_title("Terminal multiple sensitivity — at base WACC",
                      fontsize=10.5, fontweight="bold", color=DARK, loc="left", pad=8)
        for i, v in enumerate(evs2):
            axC.text(i, v + 0.15, f"${v:.1f}B", ha="center",
                     fontsize=8, color=GRAY_BD)
        # Highlight 3.5x
        try:
            idx_35 = mults.index(3.5)
            axC.patches[idx_35].set_facecolor(ORANGE)
        except ValueError:
            pass
        axC.grid(axis="y", color=GRAY_LT, linewidth=0.5, alpha=0.7)
        axC.set_axisbelow(True)

    fig.suptitle("Sensitivity matrix — weight scheme (heatmap) + material drivers (Members · WACC · Terminal mult)",
                 fontsize=15, fontweight="bold", color=DARK, x=0.02, ha="left", y=0.995)
    fig.savefig(f"{OUT}/sensitivity_heatmap.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built sensitivity_heatmap.png")


# ===========================================================
# 8. NEW — Comp scatter (X=growth, Y=EV/Rev)
# ===========================================================
def comp_scatter():
    fig, ax = plt.subplots(figsize=(12, 7.5))
    comps = M.get("comps_full", [])

    tier_color = {
        "T1": "#FF5A1F",         # Oura, T1 private
        "T2": NAVY,              # Spotify, Dexcom, iRhythm, Roku, Garmin
        "T3": "#8B5A3C",         # Peloton, Sonos, GoPro, ResMed, Masimo
        "T4": GRAY_FT,           # Fitbit historical
    }

    for c in comps:
        growth = c.get("growth")
        evrev  = c.get("ev_rev")
        tier   = c.get("tier", "T2")
        name_raw = c.get("name", "")
        ticker   = c.get("ticker", "") or ""
        if name_raw.startswith("Oura"):
            label = "OURA (private)"
        elif "(IPO" in name_raw or "Google" in name_raw:
            label = name_raw
        else:
            label = ticker or name_raw
        if growth is None or evrev is None: continue
        color = tier_color.get(tier, NAVY)
        marker_size = 220 if name_raw.startswith("Oura") else 160
        ax.scatter(growth * 100, evrev, s=marker_size, color=color, alpha=0.85,
                   edgecolor="white", linewidth=1.6, zorder=3)
        offset_x, offset_y = 4, 0.18
        if ticker == "PTON": offset_x, offset_y =  4,  +0.85
        if ticker == "SONO": offset_x, offset_y =  4,  +0.20
        if ticker == "GPRO": offset_x, offset_y =  4,  -0.50
        if ticker == "DXCM": offset_x, offset_y = -11,  0
        if ticker == "GRMN": offset_x, offset_y =  4, +0.70
        if ticker == "RMD":  offset_x, offset_y =  4, -0.40
        if ticker == "MASI": offset_x, offset_y =  4, +0.40
        if ticker == "ROKU": offset_x, offset_y =  4, -0.40
        if ticker == "SPOT": offset_x, offset_y =  4, +0.40
        if ticker == "IRTC": offset_x, offset_y =  4, +0.40
        if name_raw.startswith("Oura"): offset_x, offset_y = -16, +0.40
        ax.text(growth * 100 + offset_x, evrev + offset_y, label,
                fontsize=10, color=color, fontweight="bold", va="center")

    # WHOOP at Series G implied — two points
    # On recognized rev: 10100 / 520.6 ≈ 19.4x at +103% growth (LTM bookings) ≈ 70% NTM
    whoop_growth = 0.70 * 100      # NTM growth (model)
    whoop_rec = 10100 / 520.6
    whoop_book = 10100 / 1100.0
    # Two markers, connected by a line
    ax.scatter([whoop_growth, whoop_growth], [whoop_rec, whoop_book],
               s=[300, 220], color=[ORANGE, ORANGE],
               edgecolor=DARK, linewidth=2.0, zorder=5,
               alpha=[0.95, 0.55])
    ax.plot([whoop_growth, whoop_growth], [whoop_rec, whoop_book],
            color=ORANGE, linewidth=1.5, linestyle=":", zorder=4)
    ax.annotate(f"WHOOP @ Series G\n{whoop_rec:.1f}× recognized\n{whoop_book:.1f}× bookings",
                xy=(whoop_growth, whoop_rec),
                xytext=(whoop_growth - 50, whoop_rec - 2),
                fontsize=11, color=DARK, fontweight="bold",
                bbox=dict(facecolor="#FFF7F0", edgecolor=ORANGE, linewidth=1.4,
                          boxstyle="round,pad=0.5"),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.4))

    ax.axhline(0, color=GRAY_BD, linewidth=0.8)
    ax.axvline(0, color=GRAY_BD, linewidth=0.8)
    ax.set_xlabel("NTM Revenue Growth (%)", fontsize=11.5, color=DARK)
    ax.set_ylabel("EV / NTM Revenue (×)", fontsize=11.5, color=DARK)
    ax.set_xlim(-15, 135)
    ax.set_ylim(-0.5, 22)
    ax.set_title("Comp positioning — growth vs multiple; WHOOP off the public surface",
                 fontsize=13.5, fontweight="bold", color=DARK, loc="left", pad=12)

    # Tier legend
    legend_entries = [
        ("T1 (best)",   tier_color["T1"]),
        ("T2 (relevant)", tier_color["T2"]),
        ("T3 (peer-of-last-resort)", tier_color["T3"]),
        ("T4 (historical ref)",     tier_color["T4"]),
    ]
    patches = [mpatches.Patch(color=c, label=l) for l, c in legend_entries]
    ax.legend(handles=patches, loc="upper right", fontsize=9.5,
              frameon=True, title="Comp tier", title_fontsize=10)

    ax.grid(True, color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(f"{OUT}/comp_scatter.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built comp_scatter.png")


# ===========================================================
# 9. NEW — Bucket bracketing strip (T1/T2/T3)
# ===========================================================
def comp_bracketing():
    fig, ax = plt.subplots(figsize=(13, 5.8))
    th = M.get("thesis_ranges", {})

    theses = [
        ("Thesis 3 — Healthcare Platform\n(Dexcom · iRhythm · ResMed · Masimo)",
         th.get("t3_healthcare", {}), GREEN),
        ("Thesis 2 — Subscription Executed\n(Spotify · Roku)",
         th.get("t2_sub_executed", {}), NAVY),
        ("Thesis 1 — Failed Pivot\n(Peloton · Sonos · GoPro)",
         th.get("t1_failed_pivot", {}), BEAR),
    ]
    n = len(theses)
    # Series G implied multiples
    sg_rec  = 10100 / 520.6     # ~19.4x
    sg_book = 10100 / 1100.0    # ~9.2x

    for i, (label, rng, col) in enumerate(theses):
        lo  = rng.get("low",  0)
        hi  = rng.get("high", 0)
        med = rng.get("median", 0)
        # Range bar
        ax.barh(i, hi - lo, left=lo, height=0.55, color=col, alpha=0.30,
                edgecolor=col, linewidth=1.2)
        # Median marker
        ax.barh(i, 0.10, left=med - 0.05, height=0.55, color=col,
                edgecolor="white", linewidth=1.2)
        # Endpoint labels
        ax.text(lo - 0.3, i, f"{lo:.2f}×", va="center", ha="right",
                fontsize=10, color=GRAY_BD)
        ax.text(hi + 0.3, i, f"{hi:.2f}×", va="center", ha="left",
                fontsize=10, color=GRAY_BD)
        ax.text(med, i + 0.36, f"Median {med:.2f}×", ha="center",
                fontsize=10, color=col, fontweight="bold")

    # Series G implied lines — labels placed BELOW the lines to avoid title clash
    ax.axvline(sg_book, color=ORANGE, linestyle="--", linewidth=2.0, alpha=0.9)
    ax.text(sg_book, -0.62, f"Series G @ bookings\n{sg_book:.1f}×",
            color=ORANGE, fontsize=10, fontweight="bold", va="top", ha="center")

    ax.axvline(sg_rec, color=DARK, linestyle=":", linewidth=2.0, alpha=0.9)
    ax.text(sg_rec, -0.62, f"Series G @ recognized\n{sg_rec:.1f}×",
            color=DARK, fontsize=10, fontweight="bold", va="top", ha="center")

    ax.set_yticks(range(n))
    ax.set_yticklabels([t[0] for t in theses], fontsize=10.5, color=DARK)
    ax.set_ylim(-1.4, n - 0.2)
    ax.set_xlim(-1.5, max(sg_rec + 1.5, 22))
    ax.set_xlabel("EV / NTM Revenue (×)", fontsize=11, color=GRAY_BD)
    ax.set_title("Three-thesis bracketing — Series G prices outside every public anchor",
                 fontsize=13.5, fontweight="bold", color=DARK, loc="left", pad=12)
    ax.grid(axis="x", color=GRAY_LT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(f"{OUT}/comp_bracketing.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Built comp_bracketing.png")


if __name__ == "__main__":
    funding_timeline()
    football_field()
    scenario_dispersion()
    jensens_gap()
    tornado()
    assumption_inventory()
    sensitivity_heatmap()
    comp_scatter()
    comp_bracketing()
