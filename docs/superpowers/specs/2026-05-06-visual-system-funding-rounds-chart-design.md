# Visual System & Funding-Rounds Chart — Design

**Date:** 2026-05-06
**Status:** Approved (user said "go for it" — proceeding to implementation without further review gate)
**Owner:** Landon Brice
**Author:** Claude (Opus 4.7, 1M)

---

## 1. Goal

Establish a reusable Python-based visualization system for the WHOOP IC deck so that every chart in the deck:
- Matches the existing HTML scaffold's brand language (`output/whoop-ic-deck.pptx` + `Whoop Valuation v2.html`).
- Is reproducible from source data, version-controlled, and re-renderable in seconds.
- Maintains visual consistency across all chart types (bar, line, scatter, fan, heatmap, football field) without per-chart styling drift.

The first chart this system produces is the **slide-1 funding-round chart**: a single-panel dual-axis combo chart showing post-money valuation and amount raised across Series A → G, with Series G highlighted as the focal datapoint.

The chart implicitly poses the slide's framing question: *each round has been a step up; is this one too far?*

## 2. Scope

### In scope (this spec)
- A shared style module `viz/whoop_style.py` capturing the deck's color palette, typography, axis/grid defaults, and a `register_fonts()` helper that registers Space Grotesk + JetBrains Mono with matplotlib.
- A single-chart script `viz/funding_rounds.py` that produces `output/charts/funding_rounds.png` from Pitchbook-locked data.
- Output dimensions: 1600×900 px @ 200 DPI (slide-friendly aspect, scales cleanly to half- or full-bleed in PowerPoint).

### Out of scope (future work)
- Other deck charts (football field, comp scatter, scenario fan, sensitivity heatmap, etc.). They will reuse `whoop_style.py` but each gets its own script + spec entry as built.
- Embedding the chart back into the HTML deck. The PNG is the deliverable; HTML edits happen separately.
- Updating the HTML deck's existing inline `.funding-chart` data values (which contain errors for Series C/D/E — see §6). Out of scope here; flagged for a separate cleanup task.

## 3. Data (Pitchbook-locked)

Source: `research/whoop-pitchbook-data.md` (Pitchbook scrape, Session 1).

| Round | Date | Post-money ($) | Amount raised ($) |
|---|---|---|---|
| Series A | 20-Jun-2014 | 23,500,000 | 6,000,000 |
| Series B | 31-Dec-2015 | 48,310,000 | 13,310,000 |
| Series C | 06-Mar-2018 | 125,000,000 | 25,000,000 |
| Series D | 12-Nov-2019 | 237,400,000 | 55,000,000 |
| Series E | 28-Oct-2020 | 1,200,000,000 | 100,000,000 |
| Series F | 30-Aug-2021 | 3,600,000,000 | 200,000,000 |
| **Series G** | **31-Mar-2026** | **10,100,000,000** | **575,000,000** |

Display labels:
- X-axis tick (top): round letter `A`–`G`, Space Grotesk semibold.
- X-axis tick (bottom): year, JetBrains Mono muted gray. Format: `2014`, `2015`, `2018`, `2019`, `2020`, `2021`, `Mar 2026`.
- Bar value labels: short form. `$23M`, `$48M`, `$125M`, `$237M`, `$1.2B`, `$3.6B`, `$10.1B`.
- Line value labels: optional, suppressed by default to keep the bars dominant; revisit if line is hard to read.

Data lives as a Python list-of-dicts at the top of `funding_rounds.py`. No external CSV — values are short and stable enough that inline is cleaner.

## 4. Visual specification

### Colors (from `Whoop Valuation v2.html` `:root`)

| Role | Hex | CSS var |
|---|---|---|
| Background | `#FFFFFF` | `--bg` |
| Foreground (default bars, primary text) | `#0A0A0A` | `--fg` |
| Secondary text | `#3A3A3A` | `--fg-2` |
| Muted text (axis ticks, footer) | `#7A776E` | `--fg-3` |
| Gridlines | `#E2DFD8` | `--line` |
| **WHOOP orange (Series G accent)** | **`#FF5A1F`** | `--accent` |

### Typography

- Body / titles / bar tick letters: **Space Grotesk** (300/400/500/600/700).
- Numerical / mono / axis ticks / eyebrow / footer: **JetBrains Mono** (300/400/500/600/700).
- Both are Google Fonts. Local copies will be downloaded by `register_fonts()` if not already cached at `~/.cache/whoop_viz_fonts/`.

### Layout

- Single panel. Margins: top 140 px (room for eyebrow + title), right 90 px, bottom 90 px, left 90 px.
- **Bars:** post-money valuation. Width = ~60% of category slot. A–F filled `#0A0A0A`; G filled `#FF5A1F`. No edge color.
- **Line + circle markers:** amount raised. Color `#7A776E`, line width 1.5, marker size 6, marker face white with `#7A776E` edge. Z-order above bars.
- **Left y-axis:** `$0` / `$2B` / `$4B` / `$6B` / `$8B` / `$10B` / `$12B`. Label "Post-money valuation" rotated 90°, JetBrains Mono small caps style (uppercase + tracked).
- **Right y-axis:** `$0` / `$100M` / `$200M` / `$400M` / `$600M`. Label "Amount raised" rotated 270°.
- **Gridlines:** horizontal only, `#E2DFD8`, behind bars.
- **Reference line:** dashed black at $10.1B across the chart (matches existing `.ref` pattern in HTML). Inline label "$10.1B — SERIES G" right-aligned at the line, JetBrains Mono uppercase tracked, white background, 1 px black border.
- **Series G bar value label** (`$10.1B`) sits above the bar in `#FF5A1F` Space Grotesk semibold, slightly larger than other bar labels.

### Header block (above plot area)

- Eyebrow: `WHOOP — FUNDING TRAJECTORY` in `#FF5A1F`, JetBrains Mono 11pt uppercase, letter-spacing 0.16em.
- Title: `Each round has been a step up. Is this one too far?` in `#0A0A0A`, Space Grotesk semibold 22pt.

### Footer

- Left: `SOURCE: PITCHBOOK` in `#7A776E`, JetBrains Mono 9pt uppercase tracked.
- Right: `AS OF MAY 2026` in `#7A776E`, same style.

### Output

- Path: `output/charts/funding_rounds.png`.
- Size: 1600×900 px.
- DPI: 200 (matplotlib `figsize=(8,4.5)`, `dpi=200`).
- `bbox_inches='tight'` is **disabled** to preserve exact dimensions; padding controlled via `subplots_adjust`.

## 5. File structure

```
viz/
  whoop_style.py        # palette, fonts, axis defaults, register_fonts()
  funding_rounds.py     # this chart's script
output/
  charts/
    funding_rounds.png  # exported PNG
```

### `whoop_style.py` exports

- Constants: `BG`, `FG`, `FG_2`, `FG_3`, `LINE`, `LINE_2`, `ACCENT`, `ACCENT_2`, `POS`, `NEG`, `BK_HARDWARE`, `BK_SUBSCRIPTION`, `BK_HEALTH`.
- Fonts: `FONT_BODY = "Space Grotesk"`, `FONT_MONO = "JetBrains Mono"`.
- Functions:
  - `register_fonts()` — downloads + registers both font families with matplotlib if not already present. Idempotent. Called once at module import.
  - `apply_base_style()` — sets matplotlib rcParams (font.family, axes.edgecolor, axes.labelcolor, etc.) so every chart inherits brand defaults.
  - `add_eyebrow_title(fig, eyebrow, title)` — places the standard two-line header.
  - `add_footer(fig, source, as_of)` — places the standard two-side footer.
  - `format_dollars(value, scale='auto')` — returns `$23M`, `$1.2B`, `$10.1B` style strings.

These helpers are **the** brand-discipline mechanism. Future charts call them; the brand never has to be re-decided.

## 6. Decisions and rationale

| Decision | Choice | Rationale |
|---|---|---|
| Tooling | matplotlib + style module | Reproducible, version-controlled, fits existing Python workflow (`build_master_model.py`, `wire_*.py`). Plotly's interactivity is wasted for a static PNG; PPT-native loses brand discipline. |
| Y-axis scale | Linear (both axes) | Per user. Linear emphasizes the visual scale jump at G. Log was the alternative (would show "step-up" pattern more cleanly across early rounds) — explicitly rejected. |
| Two metrics, one chart | Dual-axis bars (val) + line (raised) | Matches Sacra reference style. Bars carry the headline metric; line is secondary. Side-by-side grouped bars reject because the two metrics' scales differ ~17× ($600M vs. $10.1B). |
| Data source | Pitchbook post-money values, not the HTML deck's inline values | The HTML's existing inline values for Series C, D, E are wrong (e.g., C shows $200M; Pitchbook says $125M). Pitchbook is the cited source; deck HTML will be corrected separately. |
| Color of Series A–F bars | Charcoal `#0A0A0A`, not orange | Orange is reserved for the focal accent (Series G). Using orange for all bars dilutes the highlight. |
| Title framing | "Each round has been a step up. Is this one too far?" | Per CLAUDE.md framing of slide 1's central question. Implicit not editorial — chart shows the data; viewer draws the conclusion. |

## 7. Open / deferred items

- HTML deck slide-1 inline values for Series B/C/D/E need correction (out of scope here). Flag as a follow-up cleanup task.
- Font installation: if Space Grotesk/JetBrains Mono fail to download in a sandboxed environment, `register_fonts()` falls back to closest matplotlib defaults (DejaVu Sans / DejaVu Sans Mono) and prints a warning. Acceptable degradation.
- Future: same `whoop_style.py` will support football field, comp scatter, sensitivity heatmap, scenario fan, churn-cohort overlay, etc. None designed yet — they get individual specs as built.

## 8. Acceptance criteria

The chart is done when:
1. `python viz/funding_rounds.py` produces `output/charts/funding_rounds.png` with no errors.
2. PNG is 1600×900 px, white background, file size < 500 KB.
3. All seven Pitchbook values render correctly (visual spot-check against §3 table).
4. Series G bar is `#FF5A1F`; all other bars are `#0A0A0A`.
5. Eyebrow + title + footer all render in Space Grotesk / JetBrains Mono (or documented fallback).
6. Dashed reference line at $10.1B with the inline label is present and readable.
7. Visual side-by-side comparison with the HTML deck's `.funding-chart` shows the PNG looks like it belongs in the same deck.
