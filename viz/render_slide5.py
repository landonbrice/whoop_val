"""
Slide 5 chart generation — DCF Build (v2 spec)
Renders two PNGs into output/charts/:
  - slide5_phases.png    (1920×1080) three-phase Rev/EBITDA/FCF
  - slide5_coststack.png (960×540)   cost composition stacked area

Data values pulled from model/Whoop Master Model 1.xlsx (Revenue Build, P&L, FCF tabs).
Spec source: whoop_slide_5_dcf_build_v2.md
"""
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import FancyBboxPatch

OUT_DIR = "/Users/landonbrice/Desktop/valuation_whoop/output/charts"
os.makedirs(OUT_DIR, exist_ok=True)

# ---------- Design tokens (from spec) ----------
NAVY = "#1a2540"
TEAL = "#5a8a9a"
GOLD = "#c9a961"
PHASE_1_FILL = "#e8edf2"
PHASE_2_FILL = "#f5f1e8"
PHASE_3_FILL = "#e8efe8"
SM_COLOR = "#d4824a"
RD_COLOR = "#5a8a9a"
GA_COLOR = "#888888"
TEXT_DARK = "#222222"
TEXT_MID = "#555555"
TEXT_LIGHT = "#888888"

# ---------- Data (from model) ----------
years = [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033]
revenue = [0.890, 1.142, 1.460, 1.802, 2.223, 2.647, 3.073, 3.568]
ebitda  = [0.162, 0.133, 0.305, 0.394, 0.529, 0.811, 0.977, 1.195]
fcf     = [0.151, 0.142, 0.233, 0.309, 0.427, 0.579, 0.730, 0.908]

sm_pct = [0.1781, 0.2338, 0.1877, 0.1944, 0.1946, 0.1596, 0.1637, 0.1636]
rd_pct = [0.2200, 0.2100, 0.2000, 0.1900, 0.1800, 0.1700, 0.1600, 0.1500]
ga_pct = [0.1500, 0.1443, 0.1386, 0.1329, 0.1271, 0.1214, 0.1157, 0.1100]


# ============================================================
# CHART 1 — Three-phase Revenue / EBITDA / FCF
# ============================================================
def render_phases_chart():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Phase shading
    ax.axvspan(2025.5, 2027.5, color=PHASE_1_FILL, alpha=0.65, zorder=0)
    ax.axvspan(2027.5, 2030.5, color=PHASE_2_FILL, alpha=0.65, zorder=0)
    ax.axvspan(2030.5, 2033.5, color=PHASE_3_FILL, alpha=0.65, zorder=0)

    # Subtle vertical phase dividers
    for x in (2027.5, 2030.5):
        ax.axvline(x, color="#cccccc", linewidth=1, linestyle=":", alpha=0.7, zorder=1)

    # Lines
    ax.plot(years, revenue, color=NAVY, linewidth=3.6, marker="o",
            markersize=9, markeredgecolor="white", markeredgewidth=1.5,
            label="Revenue", zorder=6)
    ax.plot(years, ebitda, color=TEAL, linewidth=3.0, marker="o",
            markersize=8, markeredgecolor="white", markeredgewidth=1.2,
            label="EBITDA", zorder=6)
    ax.plot(years, fcf, color=GOLD, linewidth=3.0, marker="o",
            markersize=8, markeredgecolor="white", markeredgewidth=1.2,
            label="Unlevered FCF", zorder=6)

    # Axes
    ax.set_ylim(0, 4.2)
    ax.set_xlim(2025.5, 2033.7)
    ax.set_xticks(years)
    ax.set_xticklabels([str(y) for y in years], fontsize=14, color=TEXT_DARK)
    ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
    ax.set_yticklabels(
        ["$0", "$0.5B", "$1.0B", "$1.5B", "$2.0B", "$2.5B", "$3.0B", "$3.5B", "$4.0B"],
        fontsize=12, color=TEXT_MID,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")
    ax.tick_params(colors="#999999")
    ax.grid(axis="y", alpha=0.18, linestyle="--", linewidth=0.8, zorder=1)

    # Phase labels (top) — smart placement: above lines, in upper empty band
    label_y = 4.00
    anno_y = 3.78

    def phase_block(x_center, label, anno):
        ax.text(x_center, label_y, label,
                ha="center", va="center", fontsize=15, fontweight="bold",
                color=NAVY, zorder=8)
        ax.text(x_center, anno_y, anno,
                ha="center", va="center", fontsize=11.5, fontstyle="italic",
                color=TEXT_MID, zorder=8)

    phase_block(2026.5, "PHASE 1 · PRE-IPO HYPERGROWTH",
                "Series G deploys; member growth peaks +29% YoY in 2027")
    phase_block(2029.0, "PHASE 2 · MARGIN INFLECTION",
                "Operating leverage: EBITDA $0.31B → $0.53B")
    phase_block(2032.0, "PHASE 3 · TERMINAL ECONOMICS",
                "Stable. Rule of 40 ~50.")

    # Endpoint value labels (right side, 2033)
    end_x = 2033 + 0.12
    ax.text(end_x, revenue[-1], f"  ${revenue[-1]:.2f}B",
            color=NAVY, fontsize=13, fontweight="bold", va="center", zorder=7)
    ax.text(end_x, ebitda[-1], f"  ${ebitda[-1]:.2f}B",
            color=TEAL, fontsize=12, fontweight="bold", va="center", zorder=7)
    ax.text(end_x, fcf[-1], f"  ${fcf[-1]:.2f}B",
            color=GOLD, fontsize=12, fontweight="bold", va="center", zorder=7)

    # Series labels at left starting points (2026)
    start_x = 2026 - 0.18
    ax.text(start_x, revenue[0], "Revenue",
            color=NAVY, fontsize=12, fontweight="bold", va="center", ha="right", zorder=7)
    ax.text(start_x, ebitda[0], "EBITDA",
            color=TEAL, fontsize=11, fontweight="bold", va="center", ha="right", zorder=7)
    ax.text(start_x, fcf[0], "FCF",
            color=GOLD, fontsize=11, fontweight="bold", va="center", ha="right", zorder=7)

    # Subtle CAGR callouts in lower-right corner (Phase 3)
    cagr_rev = (revenue[-1] / revenue[0]) ** (1 / 7) - 1
    cagr_ebitda = (ebitda[-1] / ebitda[0]) ** (1 / 7) - 1
    cagr_fcf = (fcf[-1] / fcf[0]) ** (1 / 7) - 1
    cagr_text = (
        f"7-Yr CAGR\n"
        f"Revenue   {cagr_rev:5.1%}\n"
        f"EBITDA   {cagr_ebitda:5.1%}\n"
        f"FCF         {cagr_fcf:5.1%}"
    )
    ax.text(2026.0, 2.5, cagr_text,
            ha="left", va="top", fontsize=11, color=TEXT_DARK,
            family="monospace",
            bbox=dict(boxstyle="round,pad=0.6", facecolor="white",
                      edgecolor="#dddddd", linewidth=1),
            zorder=9)

    plt.subplots_adjust(left=0.06, right=0.96, top=0.97, bottom=0.06)
    out_path = os.path.join(OUT_DIR, "slide5_phases.png")
    plt.savefig(out_path, dpi=100, facecolor="white")
    plt.close()
    print(f"Wrote {out_path}")


# ============================================================
# CHART 2 — Cost stack stacked area
# ============================================================
def render_coststack_chart():
    fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Stacked area: bottom S&M, middle R&D, top G&A
    ax.fill_between(years, 0, sm_pct, color=SM_COLOR, alpha=0.78,
                    label="Sales & Marketing", zorder=2)
    sm_rd = [s + r for s, r in zip(sm_pct, rd_pct)]
    ax.fill_between(years, sm_pct, sm_rd, color=RD_COLOR, alpha=0.78,
                    label="R&D", zorder=2)
    sm_rd_ga = [a + g for a, g in zip(sm_rd, ga_pct)]
    ax.fill_between(years, sm_rd, sm_rd_ga, color=GA_COLOR, alpha=0.78,
                    label="G&A", zorder=2)

    # Top boundary line for clarity
    ax.plot(years, sm_rd_ga, color="#444444", linewidth=1.2, zorder=3)

    # Endpoint annotation: total OpEx start vs end
    ax.annotate(f"{sm_rd_ga[0]:.0%}", xy=(years[0], sm_rd_ga[0]),
                xytext=(-6, 8), textcoords="offset points",
                fontsize=11, fontweight="bold", color=TEXT_DARK, ha="right")
    ax.annotate(f"{sm_rd_ga[-1]:.0%}", xy=(years[-1], sm_rd_ga[-1]),
                xytext=(6, 8), textcoords="offset points",
                fontsize=11, fontweight="bold", color=TEXT_DARK, ha="left")

    # Title
    ax.set_title("Cost stack — operating leverage as scale absorbs fixed cost",
                 fontsize=12, color=TEXT_DARK, loc="left",
                 fontweight="bold", pad=14)

    # Axes
    ax.set_xlim(2026, 2033)
    ax.set_ylim(0, 0.65)
    ax.set_xticks(years)
    ax.set_xticklabels([str(y) for y in years], fontsize=9, color=TEXT_DARK)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0, decimals=0))
    ax.tick_params(axis="y", labelsize=9, colors=TEXT_MID)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")
    ax.grid(axis="y", alpha=0.20, linestyle="--", linewidth=0.7, zorder=1)

    # In-chart band labels (centered in mid-period)
    mid_idx = 4  # 2030
    sm_mid = sm_pct[mid_idx] / 2
    rd_mid = sm_pct[mid_idx] + rd_pct[mid_idx] / 2
    ga_mid = sm_pct[mid_idx] + rd_pct[mid_idx] + ga_pct[mid_idx] / 2
    ax.text(years[mid_idx], sm_mid, "S&M",
            ha="center", va="center", fontsize=11, fontweight="bold", color="white")
    ax.text(years[mid_idx], rd_mid, "R&D",
            ha="center", va="center", fontsize=11, fontweight="bold", color="white")
    ax.text(years[mid_idx], ga_mid, "G&A",
            ha="center", va="center", fontsize=11, fontweight="bold", color="white")

    # Right-side methodology callouts (kept brief)
    callouts = [
        ("S&M peaks 23% in 2027 IPO push", 0.585),
        ("R&D leverage: 22% → 15%", 0.555),
        ("G&A leverage: 15% → 11%", 0.525),
    ]
    for txt, y in callouts:
        ax.text(2033.05, y, txt, ha="left", va="center",
                fontsize=8.5, color=TEXT_MID, fontstyle="italic")

    plt.subplots_adjust(left=0.07, right=0.78, top=0.86, bottom=0.10)
    out_path = os.path.join(OUT_DIR, "slide5_coststack.png")
    plt.savefig(out_path, dpi=100, facecolor="white")
    plt.close()
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    render_phases_chart()
    render_coststack_chart()
