"""WHOOP IC-deck visualization style system.

Single source of truth for brand palette, typography, and chart defaults.
Every chart in viz/ imports from here so the deck stays visually consistent.

Palette mirrors `:root` CSS vars in `Whoop Valuation v2.html`.
"""
from __future__ import annotations

import os
import sys
import urllib.request
from pathlib import Path

import matplotlib as mpl
import matplotlib.font_manager as fm

# ── Palette ──────────────────────────────────────────────────────────────────
BG       = "#FFFFFF"
BG_2     = "#F6F5F2"
BG_3     = "#EDEBE6"
LINE     = "#E2DFD8"
LINE_2   = "#C8C4BA"
FG       = "#0A0A0A"
FG_2     = "#3A3A3A"
FG_3     = "#7A776E"
ACCENT   = "#FF5A1F"   # WHOOP orange — focal accent only
ACCENT_2 = "#FF7A3D"
POS      = "#1F7A3D"
NEG      = "#FF5A1F"
# Bucket colors (reserved for comp/sensitivity charts)
BK_HARDWARE     = "#D14B2A"
BK_SUBSCRIPTION = "#1F4FB5"
BK_HEALTH       = "#1F7A3D"

# ── Fonts ────────────────────────────────────────────────────────────────────
FONT_BODY = "Space Grotesk"
FONT_MONO = "JetBrains Mono"

_FONT_CACHE = Path.home() / ".cache" / "whoop_viz_fonts"
_FONT_URLS = {
    "SpaceGrotesk-Regular.ttf":
        "https://raw.githubusercontent.com/floriankarsten/space-grotesk/master/fonts/ttf/static/SpaceGrotesk-Regular.ttf",
    "SpaceGrotesk-Medium.ttf":
        "https://raw.githubusercontent.com/floriankarsten/space-grotesk/master/fonts/ttf/static/SpaceGrotesk-Medium.ttf",
    "SpaceGrotesk-Bold.ttf":
        "https://raw.githubusercontent.com/floriankarsten/space-grotesk/master/fonts/ttf/static/SpaceGrotesk-Bold.ttf",
    "JetBrainsMono-Regular.ttf":
        "https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/fonts/ttf/JetBrainsMono-Regular.ttf",
    "JetBrainsMono-Medium.ttf":
        "https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/fonts/ttf/JetBrainsMono-Medium.ttf",
    "JetBrainsMono-SemiBold.ttf":
        "https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/fonts/ttf/JetBrainsMono-SemiBold.ttf",
}


def _registered_families() -> set[str]:
    return {f.name for f in fm.fontManager.ttflist}


def register_fonts(verbose: bool = True) -> tuple[str, str]:
    """Ensure WHOOP brand fonts are registered with matplotlib.

    Downloads to ~/.cache/whoop_viz_fonts/ on first run. Idempotent.
    Returns a (body_family, mono_family) tuple — falls back to matplotlib
    defaults if download fails.
    """
    families = _registered_families()
    if FONT_BODY in families and FONT_MONO in families:
        return FONT_BODY, FONT_MONO

    _FONT_CACHE.mkdir(parents=True, exist_ok=True)
    failures = []
    for filename, url in _FONT_URLS.items():
        target = _FONT_CACHE / filename
        if not target.exists():
            try:
                if verbose:
                    print(f"[whoop_style] downloading {filename}...", file=sys.stderr)
                urllib.request.urlretrieve(url, target)
            except Exception as exc:
                failures.append((filename, str(exc)))
                continue
        try:
            fm.fontManager.addfont(str(target))
        except Exception as exc:
            failures.append((filename, str(exc)))

    families = _registered_families()
    body = FONT_BODY if FONT_BODY in families else "DejaVu Sans"
    mono = FONT_MONO if FONT_MONO in families else "DejaVu Sans Mono"

    if failures and verbose:
        print(
            f"[whoop_style] WARNING: font setup had {len(failures)} failure(s); "
            f"falling back to body={body}, mono={mono}",
            file=sys.stderr,
        )
        for fn, msg in failures:
            print(f"  - {fn}: {msg}", file=sys.stderr)

    return body, mono


def apply_base_style() -> tuple[str, str]:
    """Set matplotlib rcParams to the WHOOP brand defaults.

    Call once near the top of every chart script.
    Returns the resolved (body_family, mono_family) so callers can reference
    the actual fonts in use (in case of fallback).
    """
    body, mono = register_fonts()
    mpl.rcParams.update({
        "font.family": body,
        "font.size": 11,
        "axes.facecolor": BG,
        "axes.edgecolor": LINE,
        "axes.linewidth": 0.8,
        "axes.labelcolor": FG_2,
        "axes.labelsize": 10,
        "axes.titlesize": 14,
        "axes.titleweight": "semibold",
        "axes.titlecolor": FG,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "xtick.color": FG_3,
        "ytick.color": FG_3,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "figure.facecolor": BG,
        "figure.edgecolor": BG,
        "savefig.facecolor": BG,
        "savefig.edgecolor": BG,
        "savefig.dpi": 200,
        "pdf.fonttype": 42,
    })
    return body, mono


# ── Format helpers ───────────────────────────────────────────────────────────

def format_dollars(value: float, scale: str = "auto") -> str:
    """Format a USD amount as $23M, $1.2B, $10.1B, etc.

    scale: 'auto' picks the smallest unit that keeps |value| >= 1.
    """
    abs_v = abs(value)
    if scale == "auto":
        if abs_v >= 1e9:
            scale = "B"
        elif abs_v >= 1e6:
            scale = "M"
        elif abs_v >= 1e3:
            scale = "K"
        else:
            scale = ""

    sign = "-" if value < 0 else ""
    if scale == "B":
        return f"{sign}${abs_v / 1e9:.1f}B"
    if scale == "M":
        return f"{sign}${abs_v / 1e6:.0f}M"
    if scale == "K":
        return f"{sign}${abs_v / 1e3:.0f}K"
    return f"{sign}${abs_v:.0f}"


# ── Layout helpers ───────────────────────────────────────────────────────────

def add_eyebrow_title(fig, eyebrow: str, title: str, *, x: float = 0.06, y_eyebrow: float = 0.94, y_title: float = 0.88):
    """Place the standard two-line header above the plot area."""
    fig.text(
        x, y_eyebrow, eyebrow.upper(),
        fontfamily=FONT_MONO, fontsize=11, color=ACCENT,
        fontweight="medium",
        # JetBrains Mono fallback inherits letter-spacing from rcParams; matplotlib
        # doesn't expose tracking directly, so we space manually:
    )
    fig.text(
        x, y_title, title,
        fontfamily=FONT_BODY, fontsize=22, color=FG,
        fontweight="semibold",
    )


def add_footer(fig, source: str, as_of: str, *, y: float = 0.04):
    """Place the standard footer (source left, as-of right)."""
    fig.text(
        0.06, y, f"SOURCE: {source.upper()}",
        fontfamily=FONT_MONO, fontsize=9, color=FG_3,
    )
    fig.text(
        0.94, y, f"AS OF {as_of.upper()}",
        fontfamily=FONT_MONO, fontsize=9, color=FG_3,
        ha="right",
    )


if __name__ == "__main__":
    # Smoke test: register fonts, print resolved families.
    body, mono = apply_base_style()
    print(f"body={body}, mono={mono}")
    print(f"format_dollars examples:  "
          f"{format_dollars(23_500_000)}, "
          f"{format_dollars(1_200_000_000)}, "
          f"{format_dollars(10_100_000_000)}")
