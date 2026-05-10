# SLIDE 5 — DCF Build (v2)

**Status:** Locked content; ready for production
**Replaces:** Slide 5 in `whoop_slide_spec_v1.md`
**Methodology emphasis:** Heavy — this slide carries Yannelis-grade rigor for the entire DCF section

---

## Title and Thesis

**Slide title:** *Three phases, seven years.*

**Thesis line (subtitle, one sentence):**
> WHOOP isn't one business across the forecast — three phases, each a distinct operating thesis stitched together via unit economics.

---

## Layout Architecture (1440 × 810)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  TITLE BAND (height 90px)                                                     │
│  Three phases, seven years.                                                   │
│  WHOOP isn't one business across the forecast — three phases, each a         │
│  distinct operating thesis stitched together via unit economics.              │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                          │                    │
│  LEFT 2/3 — VISUAL SECTION                              │  RIGHT 1/3 —       │
│  (width 960px, height 600px)                            │  KEY DRIVERS       │
│                                                          │  PANEL             │
│  TOP HALF — Three-phase line/area chart                 │  (width 480px,     │
│  Revenue + EBITDA + FCF over 2026-2033                  │   height 600px)    │
│  Phase shading: 3 subtle background tints               │                    │
│  Phase labels above the chart                           │  (Five sub-blocks) │
│                                                          │                    │
│                                                          │                    │
│                                                          │                    │
│  BOTTOM HALF (split):                                   │                    │
│                                                          │                    │
│  Bottom-left — Unit Economics Chain (visual flow)       │                    │
│  Bottom-right — Cost Stack (stacked area inset)         │                    │
│                                                          │                    │
├──────────────────────────────────────────────────────────────────────────────┤
│  FOOTER BAND (height 40px)                                                    │
│  WACC: BOTTOM-UP CAPM + HAMADA RELEVER + OURA PRIVATE PREMIUM.               │
│  EXIT: SUBSCRIPTION-ANCHORED (3.5x). HEALTHCARE OPTIONALITY SEPARATE         │
│  IN REAL OPTIONS LAYER.                                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## LEFT 2/3 — Visual Section (three components)

### Component 1: Three-phase chart (top, ~280px height)

**Chart spec:**
- X-axis: years 2026–2033 (8 data points; 2026 = Y1)
- Y-axis: $B (left, primary, 0–$3.5B range)
- Three lines: Revenue (solid navy), EBITDA (solid teal), FCF (solid gold)
- Phase shading (3 background bands, subtle alpha 0.10):
  - Phase 1 band: 2026–2027 (warm gray-blue tint)
  - Phase 2 band: 2028–2030 (neutral cream tint)
  - Phase 3 band: 2031–2033 (soft sage tint)
- Phase labels above chart (in line with x-axis years):
  - "PHASE 1 · Pre-IPO Hypergrowth" (centered over 2026–2027)
  - "PHASE 2 · Margin Inflection" (centered over 2028–2030)
  - "PHASE 3 · Terminal Economics" (centered over 2031–2033)

**Data values (pull from Revenue Build / P&L / FCF tabs):**

| Year | Revenue ($B) | EBITDA ($B) | FCF ($B) |
|---|---|---|---|
| 2026 | 0.87 | 0.16 | 0.07 |
| 2027 | 1.13 | 0.20 | 0.11 |
| 2028 | 1.45 | 0.31 | 0.21 |
| 2029 | 1.83 | 0.46 | 0.34 |
| 2030 | 2.27 | 0.62 | 0.46 |
| 2031 | 2.69 | 0.86 | 0.66 |
| 2032 | 3.07 | 1.07 | 0.83 |
| 2033 | 3.27 | 1.22 | 0.95 |

*(Verify exact values from current model before rendering. These are illustrative based on prior context.)*

**Phase annotations (small text inside each phase band, top of chart):**
- Phase 1: "Series G deploys; member growth peaks at +50% YoY"
- Phase 2: "EBITDA margin: 18% → 28%"
- Phase 3: "Stable. Rule of 40 ~50."

---

### Component 2: Unit Economics Chain (bottom-left, ~280px height, ~480px width)

**This is the spine of the slide. Visual flow, left-to-right:**

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  MEMBERS    ×    ARPU    =    REVENUE    →    COST STACK   →   FCF │
│     ↓              ↓                              ↓                 │
│   2.5M →        $305 →                          (See              │
│   8.4M          $417                            inset →)          │
│                                                                     │
│   Bottom-up:    Bottom-up                                          │
│   gross adds =  reconciliation:                                    │
│   (rev × S&M%)  0.80 × $319                                       │
│      ÷ CAC      + 0.20 × $260                                     │
│                 = $307 implied                                     │
│                 vs $305 anchor                                     │
│                 (-0.7% variance)                                   │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

**Visual treatment:**
- Each step is a labeled block (rounded rectangle, 4 blocks total: Members, ARPU, Revenue, Cost Stack)
- Arrows connect blocks (× and = and →)
- Below each input block: small italic methodology note
- The methodology notes are the load-bearing element — they tell the audience each input is anchored, not chosen

**Specific text in each block:**

**MEMBERS block:**
- Big number: `2.5M → 8.4M`
- Label: `Y1 → Y7`
- Methodology note: `Gross adds = (Prior Yr Rev × S&M %) ÷ CAC. Member growth falls out of unit economics, not picked.`

**ARPU block:**
- Big number: `$305 → $417`
- Label: `Y1 → Y7 (3.4% CAGR)`
- Methodology note: `0.80 × $319 + 0.20 × $260 = $307 implied. Anchor $305; -0.7% variance. Bottom-up reconciled.`

**REVENUE block:**
- Big number: `$0.87B → $3.27B`
- Label: `Y1 → Y7 (21% CAGR)`
- Methodology note: `Falls out of Members × ARPU. No standalone revenue assumption.`

**COST STACK block:**
- Big number: `EBITDA Margin 18% → 37%`
- Label: `Y1 → Y7`
- Methodology note: `S&M intensity declines 30% → 18%. R&D ~10%. GM 78% subscription-mix.`

---

### Component 3: Cost Stack inset (bottom-right, ~280px height, ~480px width)

**Stacked area chart — Operating expense composition over Y1–Y7:**

- X-axis: 2026–2033
- Y-axis: % of revenue, 0%–60% range
- Three stacked bands (bottom to top):
  - **S&M** (warm orange, alpha 0.7) — 30% → 18%
  - **R&D** (medium teal, alpha 0.7) — 12% → 10%
  - **G&A** (cool gray, alpha 0.7) — 12% → 7%
- Total OpEx: 54% → 35% (visual confirmation of operating leverage)

**Inset title:** *Cost stack — operating leverage as scale absorbs fixed cost.*

**Inline annotation (right side of chart):**
- "S&M intensity declines as deployment matures"
- "G&A compresses fastest (fixed-cost absorption)"
- "R&D steady — platform investment continues"

---

## RIGHT 1/3 — Key Drivers Panel

**Five vertically stacked sub-blocks, each ~110px height:**

### Block 1 — Top-Line

**Header:** TOP-LINE

| Driver | Value |
|---|---|
| Members (Y1 → Y7) | 2.5M → 8.4M |
| Member CAGR | 18% |
| Blended ARPU (Y1 → Y7) | $305 → $417 |
| ARPU CAGR | 3.4% |

**Methodology callout (small italic, below table):**
> *Members built bottom-up via S&M ÷ CAC formulation. ARPU reconciled to 80/20 consumer/Unite mix.*

---

### Block 2 — Margin

**Header:** MARGIN

| Driver | Value |
|---|---|
| Gross Margin (terminal) | 78% |
| Subscription COGS | 18-20% |
| Terminal EBITDA Margin | 37% |
| Terminal Rule of 40 | ~50 |

**Methodology callout:**
> *Terminal EBITDA anchored to Spotify post-profitability template (28%) plus WHOOP GM premium.*

---

### Block 3 — WACC Build *(load-bearing block)*

**Header:** WACC BUILD (Bottom-Up)

```
                                          %
Risk-Free Rate (10Y Treasury)         4.30%
+ Asset Beta × ERP                   +4.49%
   (β_U 0.97 × ERP 4.61% blended)
─────────────────────────────────────────
COST OF EQUITY (CAPM-pure)            8.79%
+ Private Company Premium            +2.00%
   (Oura tender benchmark Jan 2026)
─────────────────────────────────────────
WACC                                 10.79%
```

**Methodology callout (3 lines, italic small):**
> *(1) Bottom-up beta from comp regressions, not Damodaran sector medians. 3Y weekly Hamada-relevered.*
>
> *(2) +2pp anchored to Oura tender — real market-clearing event, not Hiive secondary quotes.*
>
> *(3) All-equity capital structure assumed pre-IPO. Sensitivity 9.8%-11.8%.*

---

### Block 4 — Exit Multiple

**Header:** EXIT MULTIPLE

| Anchor | Multiple |
|---|---|
| Spotify (LTM EV/Rev) | 4.1x |
| Roku (LTM EV/Rev) | 3.4x |
| **Subscription median** | **3.75x** |
| GM premium adjustment | -0.25x |
| **WHOOP exit multiple** | **3.5x** |

**Methodology callout:**
> *Subscription-anchored, NOT health-data. Healthcare optionality captured separately in real options to avoid double-count.*

---

### Block 5 — Terminal Growth

**Header:** TERMINAL GROWTH

| Driver | Value |
|---|---|
| Perpetual growth (g) | 3.0% |
| Anchor | Long-run US economy proxy |
| Gordon TV cross-check | $11.9B |
| Exit multiple TV cross-check | $11.4B |
| **Divergence** | **2.85% (within 5% threshold)** |

**Methodology callout:**
> *Two TV methods reconcile to within 3%. Robust terminal value mechanism.*

---

## Footer Band

**Full text (small caps, 11pt, centered):**
> WACC: BOTTOM-UP CAPM (LECTURE 1B) + HAMADA RELEVER (LECTURE 2B) + OURA PRIVATE PREMIUM. EXIT MULTIPLE: SUBSCRIPTION-ANCHORED (LECTURE 7 COMP FRAMEWORK). HEALTHCARE OPTIONALITY VALUED SEPARATELY IN REAL OPTIONS LAYER (LECTURE 3B).

---

## Speaker Notes (~90 seconds, 3 beats)

### Beat 1 — Forecast structure (~30 sec)

> "Seven-year forecast in three phases — and the phases aren't arbitrary tertiles. Phase 1 is pre-IPO hypergrowth, ending at the IPO event we expect in 2027. Phase 2 is margin inflection — the three-to-four-year period where post-IPO discipline drives margin expansion, similar to Spotify's 2024 profitability turn. Phase 3 is terminal economics — three years of stable mature subscription, long enough to defend the terminal value mechanic. Seven years is the *minimum* window that reaches all three; five years wouldn't get us to steady-state, and ten years overforecasts Phase 2 dynamics."

### Beat 2 — Unit economics (~30 sec)

> "Revenue is members times ARPU, both built bottom-up. Members come out of the unit economics — gross adds equal prior-year revenue times S&M intensity divided by blended CAC. We don't pick member growth; it falls out of marketing efficiency. ARPU at $305 is bottom-up justified — 80% consumer subscription at $319 plus 20% B2B Unite at $260 implies $307. We anchor at $305; the variance is 0.7%, which is rounding. The point isn't the number — it's that the number is anchored, not chosen."

### Beat 3 — WACC and exit (~30 sec)

> "WACC at 10.8% is the most contested number in any DCF, so we surface the build. CAPM-pure gives us 8.8% — risk-free rate 4.3% plus asset beta 0.97 times equity risk premium 4.6%. Asset beta is bottom-up from comp regressions, three-year weekly, Hamada-relevered. We add 2 percentage points for private illiquidity, anchored to the Oura tender — a real market-clearing event in January 2026, not a practitioner convention. Exit multiple is 3.5x, anchored to subscription comps explicitly. We do *not* anchor to health-data comps because that would double-count the healthcare optionality we separately value as a real option in the next slide. Each method has a clean identity. No double-counting."

**Total target: 90 seconds. Practice cuts to 80 if other slides need recovery time.**

---

## Chart Generation Specs (for Python local build)

### Chart 1: Three-phase line chart

```python
# Inputs
years = [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033]
revenue = [0.87, 1.13, 1.45, 1.83, 2.27, 2.69, 3.07, 3.27]   # $B
ebitda  = [0.16, 0.20, 0.31, 0.46, 0.62, 0.86, 1.07, 1.22]   # $B
fcf     = [0.07, 0.11, 0.21, 0.34, 0.46, 0.66, 0.83, 0.95]   # $B

# Visual params
phase_1_xrange = (2025.5, 2027.5)
phase_2_xrange = (2027.5, 2030.5)
phase_3_xrange = (2030.5, 2033.5)

# Colors (hex from existing deck design tokens — confirm before rendering)
NAVY  = "#1a2540"   # Revenue
TEAL  = "#5a8a9a"   # EBITDA
GOLD  = "#c9a961"   # FCF

PHASE_1_FILL = "#e8edf2"  # warm gray-blue, alpha 0.10
PHASE_2_FILL = "#f5f1e8"  # neutral cream, alpha 0.10
PHASE_3_FILL = "#e8efe8"  # soft sage, alpha 0.10

# Output: PNG at 1920×1080 (oversample for retina), saved as slide5_phases.png
```

### Chart 2: Cost stack stacked area

```python
# Inputs
years = [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033]
sm_pct  = [0.30, 0.28, 0.26, 0.23, 0.21, 0.19, 0.18, 0.18]
rd_pct  = [0.12, 0.12, 0.11, 0.11, 0.10, 0.10, 0.10, 0.10]
ga_pct  = [0.12, 0.11, 0.10, 0.09, 0.08, 0.07, 0.07, 0.07]

# Verify these against your P&L tab. Adjust if model has different splits.

# Colors
SM_COLOR  = "#d4824a"   # warm orange
RD_COLOR  = "#5a8a9a"   # medium teal (matches EBITDA in chart 1)
GA_COLOR  = "#888888"   # cool gray

# Output: PNG at 960×540, saved as slide5_coststack.png
```

---

## Production Checklist

- [ ] Pull exact revenue/EBITDA/FCF values from current model (Revenue Build, P&L, FCF tabs)
- [ ] Pull exact S&M/R&D/G&A breakdown from P&L tab
- [ ] Confirm asset beta (β_U) value — we discussed 0.97 (raw 3Y weekly bucket median, ex-PTON); verify against current WACC Bottom-Up tab
- [ ] Confirm ARPU bottom-up reconciliation values match current ARPU tab
- [ ] Confirm exit multiple still 3.5x (or update if you moved to 4.0x)
- [ ] Generate two PNG charts via Python (matplotlib) locally
- [ ] Drop charts into PPTX placeholders during production phase
- [ ] Verify all class anchors (Lecture 1B / 2B / 3B / 7) are accurate to syllabus

---

**End of v2 spec for Slide 5.**

When this is locked, next slide for spec build is Slide 6 (DCF Output) — same methodology-emphasis approach.
