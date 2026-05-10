# WHOOP Comps Model — Methodology & Build Specification

**Date:** May 5, 2026
**Status:** Approved design — ready for Excel build
**Supersedes:** Three-bucket framework (Section 4 of 2026-04-16-assumption-inventory-design.md)
**Data source:** research/comps-refresh-may2026.md (all figures sourced May 5, 2026 from Cap IQ + Pitchbook)

---

## Why the Old Framework Failed

The three-bucket framework (hardware / subscription / health data) with subjective weighting collapsed under fresh data:

1. **Bucket convergence.** B1 (5.25x NTM), B2 growth tier (3.0-3.7x), and B3 (4.2-6.0x) now overlap. Weighting barely moves the needle — the entire output range is 3.9x-4.5x regardless of weights.
2. **EV/Revenue ignores margin quality.** A dollar of WHOOP subscription revenue (~75-80% GM) is structurally worth more than a dollar of Garmin hardware revenue (59% GM) or Spotify content revenue (32% GM). Blending raw EV/Revenue across margin profiles is a category error.
3. **No comp grows at 103%.** The fastest public comp (iRhythm, 26%) grows at one-quarter WHOOP's rate. Static multiples from 10-26% growers applied to a 103% grower systematically undervalue growth.
4. **Bucket weighting is thesis, not math.** Asking "what percentage health-data company is WHOOP?" produces a subjective input masquerading as analytical precision.

---

## 1. Multiple Selection

The comps model computes **three multiples** for every comp. Each multiple answers a different question. The analyst selects the anchor; the model presents all three.

### 1A. EV/Revenue (NTM)

**What it answers:** What does the market pay per dollar of forward revenue?

**When to use:** Default anchor. Universally computable, widely understood, standard for pre-profit and early-profit companies. Feeds the football field directly.

**Limitation:** Treats all revenue as equal regardless of margin structure. Penalizes high-margin businesses (WHOOP, iRhythm) relative to low-margin businesses (Spotify, Roku).

**WHOOP at $10.1B:** 9.2x on $1.1B bookings / ~15.5x on $650M recognized revenue.

### 1B. EV/Gross Profit (NTM)

**What it answers:** What does the market pay per dollar of gross profit — the revenue that actually flows toward operating income?

**When to use:** When comparing across different margin structures. This is the right multiple for asking "is WHOOP expensive or cheap relative to its comp set on an apples-to-apples basis?"

**Why it matters:** On EV/Revenue, WHOOP at $10.1B looks 2x richer than the comp median. On EV/Gross Profit, the gap narrows substantially because WHOOP's ~75-80% gross margin means more of each revenue dollar converts to profit. The comp set converges to a tighter 7-13x range on EV/Gross Profit, and WHOOP at $10.1B (~12x) lands at Spotify's level — defensible for a hypergrowth subscription business.

**Calculation:** TEV / (NTM Revenue x Gross Margin). For WHOOP, use estimated 75-80% gross margin based on peer inference (Peloton sub GM 68%, Oura implied ~50% blended, pure subscription businesses 70-85%).

### 1C. EV/Revenue / Growth (Growth-Adjusted)

**What it answers:** How much does the market charge per point of revenue growth? Controls for the elephant in the room — WHOOP grows 4-10x faster than any public comp.

**When to use:** To test whether the $10.1B mark is justified after adjusting for growth differential. This is the "is the growth premium reasonable?" check.

**Interpretation:**

| Company | EV/Rev NTM | NTM Growth | EV/Rev/Growth | Read |
|---|---|---|---|---|
| Garmin | 5.25x | 10% | 0.53 | Market pays 0.53x per point of growth |
| Roku | 3.02x | 17% | 0.18 | Cheapest per-growth-point |
| Spotify | 3.66x | 11% | 0.33 | Mid-range |
| Dexcom | 4.24x | 8% | 0.53 | Tied with Garmin |
| iRhythm | 4.65x | 12% | 0.39 | Mid-range |
| **Median** | — | — | **0.39** | — |
| WHOOP ($10.1B, bookings) | 9.2x | 103% | **0.09** | Cheap per growth point |
| WHOOP ($10.1B, recognized) | 15.5x | 103% | **0.15** | Still below median |

On a growth-adjusted basis, WHOOP is cheap relative to every public comp — even on recognized revenue. The $10.1B mark implicitly prices WHOOP's growth at roughly 1/3 the per-point value that public comps receive. This is the illiquidity/private-market discount in action.

**Limitation:** Assumes linear relationship between growth and multiple. In practice, the relationship is concave — the market pays disproportionately more for the first 10 points of growth than the 90th-100th. The ratio also breaks down for low/negative growth comps (Peloton, Sonos, GoPro).

---

## 2. Comp Grouping

Comps are organized along two axes: **tier** (how much to trust each comp) and **dimension** (which part of WHOOP's business it illuminates).

### Tier Definitions

| Tier | Role | How It's Used in Model |
|---|---|---|
| **T1: Direct Comp** | Near-identical business model. Primary valuation anchor. | Produces the central estimate. |
| **T2: Structural Analogues** | Partial business model overlap. Inform specific assumptions. | Produce dimension-specific median and range. |
| **T3: Boundary Markers** | Floor and ceiling references. Define the extremes. | Shown alongside T2 ranges but excluded from median/mean calculations. |
| **T4: Historical Reference** | Exited or acquired comps. Not in live model. | Footnote evidence for narrative support. |

### Comp Map

**Tier 1 — Direct Comp**

| Company | Dimension | What It Tells You |
|---|---|---|
| **Oura** | Hardware + Subscription + Health Data | Only comp with near-identical business model (wearable + subscription + health + consumer + private + hypergrowth). Primary anchor at $12.1B / $927M rev / 17% EBITDA margin. |

**Tier 2 — Structural Analogues (by dimension)**

| Dimension | Company | Ticker | What It Tells You About WHOOP |
|---|---|---|---|
| **Hardware** | Garmin | GRMN | Ceiling for hardware margin; what a premium diversified device brand trades at. Fitness segment (~33% growth) is the relevant sub-unit. |
| **Subscription** | Spotify | SPOT | Post-profitability re-rating template. Went from 1.9x (unprofitable, 2023) to 6.0x (profitable, Oct 2025), now 4.1x. If WHOOP proves sustained profitability, this is the trajectory. |
| **Subscription** | Roku | ROKU | Platform model with hardware as customer acquisition vehicle. Mid-range growth comp (17%). Profitability inflection in progress. |
| **Health Data** | Dexcom | DXCM | FDA-regulated wearable subscription. The multiple compression cautionary case (13.8x → 4.6x in 3 years). Demonstrates what happens when the health-data-platform thesis loses credibility. |
| **Health Data** | iRhythm | IRTC | Cardiac wearable + SaaS. Closest to WHOOP's ECG/clinical monitoring lane. Similar compression trajectory (10.7x → 5.2x). |

**Tier 3 — Boundary Markers (by dimension)**

| Dimension | Company | Ticker | Role | Current NTM Multiple |
|---|---|---|---|---|
| **Hardware floor** | GoPro | GPRO | Failed subscription pivot, terminal decline | 0.4x |
| **Hardware floor** | Fitbit | — | Best-case pure wearable peaked at 2.2x (2015 IPO); acquired at 1.5x (2021) | Historical |
| **Subscription floor** | Peloton | PTON | Growth-to-decline cautionary case | 1.22x |
| **Subscription floor** | Sonos | SONO | Hardware-dominant consumer brand in revenue decline | 1.07x |
| **Health data ceiling** | ResMed | RMD | Mature profitable medtech, stable compounder | 5.23x |
| **Health data ceiling** | Masimo | MASI | Highest current health-data multiple, sensor-first | 5.96x |

### Why These Comps, Why Not Others

| Excluded | Rationale |
|---|---|
| Apple (AAPL) | TAM framing only. Too diversified to produce a usable multiple. |
| Netflix (NFLX) | Content-driven subscription priced on content ROI. Category error. |
| Abbott (ABT) | WHOOP investor, not peer. Too diversified. |
| Insulet (PODD) | Insulin delivery too specialized. Not a wearable platform. |
| Logitech (LOGI) | PC peripherals. Zero business model overlap. |

---

## 3. Data Inputs (Per Comp)

Every comp row in the model carries these fields:

### Identification
- Company name, ticker, tier (T1-T4), dimension(s) (Hardware / Subscription / Health Data)

### Market Data (as of May 5, 2026)
- Share price (or last known valuation for private)
- Shares outstanding
- Market capitalization
- Cash & short-term investments
- Total debt
- Enterprise value (TEV)

### Financial Data
- LTM revenue
- NTM revenue (consensus estimate, or Pitchbook estimate for private)
- LTM revenue growth
- NTM revenue growth (consensus)
- Gross profit (LTM)
- Gross margin (LTM)
- EBITDA (LTM)
- EBITDA margin (LTM)
- Rule of 40 score (revenue growth + EBITDA margin)

### Computed Multiples
- EV/Revenue (LTM)
- EV/Revenue (NTM)
- EV/Gross Profit (LTM)
- EV/Gross Profit (NTM)
- EV/Revenue / Growth (growth-adjusted)
- EV/EBITDA (LTM) — where positive

### Historical Regime (V19, Tier 2 only)
- Current multiple
- 6 months ago
- 12 months ago
- 3 years ago
- 52-week high / low price

---

## 4. Output Structure

The comps model produces three deliverables.

### 4A. Master Comp Table

One table, all comps, all fields from Section 3. Tagged by tier and dimension. Filterable both ways. This is the raw data layer — everything else derives from it.

### 4B. Summary Panels (Three Sets — One Per Multiple)

For each multiple (EV/Revenue, EV/Gross Profit, EV/Revenue/Growth):

**By-Dimension Summary (Tier 2 only):**

| Dimension | Comps | Median | Low | High |
|---|---|---|---|---|
| Hardware | Garmin | X.Xx | — | — |
| Subscription | Spotify, Roku | X.Xx | X.Xx | X.Xx |
| Health Data | Dexcom, iRhythm | X.Xx | X.Xx | X.Xx |
| **T2 Overall** | All 5 | **X.Xx** | X.Xx | X.Xx |

Below each dimension: Tier 3 boundary markers shown as floor/ceiling reference lines, not included in median.

**Implied WHOOP Valuation:**

For each dimension, apply the Tier 2 median and range to WHOOP's financials:

| Basis | WHOOP Metric | At T2 Median | At T2 Low | At T2 High | At Oura (T1) |
|---|---|---|---|---|---|
| EV/Revenue (bookings $1.1B) | $1,100M | $X.XB | $X.XB | $X.XB | $X.XB |
| EV/Revenue (recognized $650M) | $650M | $X.XB | $X.XB | $X.XB | $X.XB |
| EV/Gross Profit (est. 77.5% GM) | $504M / $853M | $X.XB | $X.XB | $X.XB | $X.XB |

### 4C. Growth-Adjusted Scatter (Chart)

Single chart. All Tier 2 + Tier 3 comps plotted.

- **X-axis:** NTM revenue growth rate
- **Y-axis:** EV/Gross Profit (NTM)
- **Each comp:** labeled dot, colored by dimension
- **WHOOP:** plotted at 103% growth with the $10.1B implied EV/GP multiple
- **Regression line** through Tier 2 comps only (5 points)
- **Annotation:** WHOOP's distance above/below the regression line = the unexplained premium or discount

This is the single most important visual in the comps workbook. It answers: "after controlling for growth rate and margin quality, is $10.1B rich, fair, or cheap?"

---

## 5. How Comps Feed the Broader Model

The comps model is one of five valuation methods. Its outputs feed the football field and cross-check the DCF. Specifically:

| Comps Output | Where It Goes | How It's Used |
|---|---|---|
| T2 median EV/Revenue (NTM) | Football field | One bar: "Public comp median" |
| T2 range EV/Revenue (NTM) | Football field | Range endpoints for the comp bar |
| Oura-implied valuation | Football field | Separate bar: "Private comp anchor" |
| Growth-adjusted scatter position | IC memo narrative | "After controlling for growth, WHOOP is above/below the regression line by X%" |
| T2 Health Data median (NTM) | DCF terminal multiple | Sanity-check on exit multiple assumption |
| Tier 3 floors (Peloton, Sonos) | DCF bear case | "If growth stalls, WHOOP trades at 1.1-1.2x" |
| V19 historical regime data | IC memo narrative | "Series G investors may have anchored to 2023-era multiples that have since compressed 50-67%" |

---

## 6. Current Data Snapshot (May 5, 2026)

All data below sourced from S&P Capital IQ (public comps) and Pitchbook (Oura) on May 5, 2026. Full sourcing detail in research/comps-refresh-may2026.md.

### 6A. Tier 1

| Company | TEV | NTM Rev | GM | EV/Rev NTM | EV/GP NTM | EV/Rev/Growth | Rule of 40 |
|---|---|---|---|---|---|---|---|
| **Oura** | ~$12.1B [E] | ~$1.1B [E] | ~50% [E] | ~11.0x | ~22.0x | ~0.09 | ~146 [E] |

Note: Oura financials are Pitchbook estimates. NTM revenue estimated from TTM $927M + ~129% growth rate trajectory. Gross margin estimated; not disclosed. TEV uses Pitchbook valuation estimate of $12.06B. Rule of 40 = ~129% growth + ~17% EBITDA margin.

### 6B. Tier 2

| Company | Ticker | Dim. | TEV ($B) | NTM Rev ($B) | NTM Growth | GM | EV/Rev NTM | EV/GP NTM | EV/Rev/G | R40 |
|---|---|---|---|---|---|---|---|---|---|---|
| Garmin | GRMN | HW | $41.9 | $8.0 | 10% | 59% | **5.25x** | **8.9x** | 0.53 | ~34 |
| Spotify | SPOT | Sub | $83.3 | $22.8 | 11% | 32% | **3.66x** | **11.4x** | 0.33 | ~27 |
| Roku | ROKU | Sub | $16.7 | $5.5 | 17% | 44% | **3.02x** | **6.9x** | 0.18 | ~25 |
| Dexcom | DXCM | Health | $22.1 | $5.2 | 8% | 60% | **4.24x** | **7.1x** | 0.53 | ~39 |
| iRhythm | IRTC | Health | $4.1 | $0.9 | 12% | 71% | **4.65x** | **6.5x** | 0.39 | ~35 |

**Tier 2 Medians:**

| Multiple | Hardware | Subscription | Health Data | Overall T2 |
|---|---|---|---|---|
| EV/Revenue NTM | 5.25x | 3.34x | 4.45x | **4.24x** |
| EV/Gross Profit NTM | 8.9x | 9.2x | 6.8x | **7.1x** |
| EV/Rev/Growth | 0.53 | 0.26 | 0.46 | **0.39** |

### 6C. Tier 3

| Company | Ticker | Dim. | Role | EV/Rev NTM | EV/GP NTM |
|---|---|---|---|---|---|
| GoPro | GPRO | HW floor | Terminal decline | 0.4x | 1.2x |
| Peloton | PTON | Sub floor | Growth stall | 1.22x | 2.9x |
| Sonos | SONO | Sub floor | Revenue decline | 1.07x | 2.4x |
| ResMed | RMD | Health ceiling | Mature compounder | 5.23x | 8.9x |
| Masimo | MASI | Health ceiling | Sensor premium | 5.96x | 9.5x |

### 6D. Implied WHOOP Valuations

**Using Tier 2 medians applied to WHOOP financials:**

| Multiple | WHOOP Metric | At T2 Median | At T2 Low | At T2 High | At Oura (T1) | Series G |
|---|---|---|---|---|---|---|
| **EV/Revenue** (bookings) | $1.1B | **$4.7B** | $3.3B | $5.8B | $12.1B | $10.1B |
| **EV/Revenue** (recognized) | $650M | **$2.8B** | $2.0B | $3.4B | $7.1B [adj] | $10.1B |
| **EV/Gross Profit** (bookings, 77.5% GM) | $853M | **$6.1B** | $5.6B | $7.6B | $10.2B [adj] | $10.1B |
| **EV/Gross Profit** (recognized, 77.5% GM) | $504M | **$3.6B** | $3.3B | $4.5B | $6.0B [adj] | $10.1B |
| **Growth-adjusted** (median 0.39 x 103%) | — | **$44.2B** [bookings] | — | — | — | $10.1B |

[adj] = Oura multiple adjusted for WHOOP revenue base (Oura's ~11x EV/Rev applied to WHOOP revenue; Oura's ~22x EV/GP applied to WHOOP gross profit).

Note: Growth-adjusted multiple produces an absurdly high number ($44B) because the linear relationship breaks at extreme growth rates. This confirms the ratio's value as a "is the growth premium reasonable?" check rather than a standalone valuation tool. At $10.1B, WHOOP's ratio is 0.09 — well below the 0.39 median — meaning the market is pricing WHOOP's growth at a steep discount to public comps. This is expected for a private, pre-IPO company.

**Key read:** EV/Revenue says $2.8-4.7B. EV/Gross Profit says $3.6-6.1B. Oura-relative says $6-12B. Series G says $10.1B. The gross-profit-adjusted range is the most analytically sound and narrows the gap to ~60% of the Series G mark on bookings. The remaining gap is growth premium + real-option value + Oura private-market reference.

### 6E. Historical Regime (V19) — Tier 2 Only

| Company | May 2026 | Oct 2025 | Apr 2025 | Apr 2023 | 3yr Change | 52wk Range |
|---|---|---|---|---|---|---|
| Garmin | 5.6x | ~6.5x | ~5.5x | ~3.5x | +60% | $180-$275 |
| Spotify | 4.1x | ~6.0x | ~4.9x | ~1.9x | +116% | $405-$785 |
| Dexcom | 4.6x | ~5.9x | ~5.8x | ~13.8x | **-67%** | $55-$85 |
| iRhythm | 5.2x | ~10.0x | ~6.9x | ~10.7x | **-51%** | $93-$212 |
| Roku | 3.4x | — | — | — | — | — |

**Read:** 4 of 5 Tier 2 comps are near 52-week lows. Current multiples may reflect cyclical trough. But the health-data compression (Dexcom -67%, iRhythm -51%) is structural, not cyclical — the market has permanently de-rated the "health data platform" thesis. Spotify's trajectory (+116%) shows the opposite: profitability proof drives re-rating. WHOOP's path to the Series G mark runs through Spotify's template, not Dexcom's.

---

## 7. Model Construction Notes (for Excel Build)

### Tab Structure
1. **Data Input** — Raw comp data from Section 6, blue-font hard-coded inputs. One row per comp, one column per field.
2. **EV/Revenue Analysis** — Computed multiples, dimension medians, implied WHOOP valuations. Black-font formulas only.
3. **EV/Gross Profit Analysis** — Same structure, gross-profit-adjusted.
4. **Growth-Adjusted Analysis** — Scatter data, regression, WHOOP positioning.
5. **Historical Regime** — V19 time-series data, 52-week ranges.
6. **Output Summary** — Pulls from tabs 2-4. Feeds football field. One-page dashboard.

### Formatting Conventions
- **Blue font:** Hard-coded inputs (prices, shares, revenue)
- **Black font:** Formulas
- **Green font:** Links to other tabs/workbooks
- Comments column on every assumption with source citation

### WHOOP Assumptions (Blue-Font Inputs on Data Tab)
- Revenue run-rate: $1,100M (bookings) / $650M (recognized) — model both
- Estimated gross margin: 77.5% (sensitivity: 70%, 75%, 80%, 85%)
- NTM growth rate: 103% (for growth-adjusted multiple)
- Series G valuation: $10,100M
- Oura valuation: $12,060M (Pitchbook estimate)

### What This Model Does NOT Do
- Does not produce a single point estimate of WHOOP's value
- Does not weight buckets or blend multiples across dimensions
- Does not embed growth premiums or real-option value
- Does not replace the DCF

The comps model produces **a range and context**. The DCF produces the intrinsic estimate. The football field synthesizes both. The IC memo explains why.
