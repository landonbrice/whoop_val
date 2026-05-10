# WHOOP Valuation — Model Build Specification

**Purpose:** This document translates analytical decisions from the valuation design phase into Excel model architecture instructions. Hand this to Claude Code alongside CLAUDE.md and the assumption spec. CLAUDE.md is project context; the spec is the assumption inventory; this document is **how to build the model**.

**Date:** May 2026
**Target:** openpyxl-based Excel workbook, blue/black/green color coding, all formulas live (no hardcoded calculations), recalculated via scripts/recalc.py

---

## Core Architectural Principle

**Revenue emerges from unit economics. It is never directly assumed.**

The model does NOT have a cell where you type "70% growth." Growth is a *diagnostic output* — computed after the fact from the unit-level drivers. Every dollar of revenue traces to a specific member cohort and ARPU component. This is the single most important design decision in the entire model.

The architecture:
```
Assumptions (blue cells: churn rates, gross adds, ARPU components, attach rates)
    ↓
Unit Drivers (black formulas: cohort engine computes members, blended ARPU)
    ↓
Revenue (black formula: Average Members × Blended ARPU = Recognized Revenue)
    ↓
Growth Rate (black formula: diagnostic output, NOT an input)
```

---

## Workbook Structure (Tab Layout)

| Tab | Purpose | Color Code |
|---|---|---|
| **Cover** | Model metadata, version, date, scenario selector | — |
| **Assumptions** | ALL blue-cell inputs, organized by spec section (R, C, S, V, D, P, I series) | Blue text for all inputs |
| **Members** | Cohort-based member engine (gross adds, churn by vintage, ending/average members) | Black formulas, green links to Assumptions |
| **ARPU** | ARPU decomposition (base sub, tier premium, accessories, Labs attach, price inflation) | Black formulas, green links to Assumptions |
| **Revenue** | Revenue build: Average Members × Blended ARPU + deferred revenue adjustment | Black formulas, green links to Members + ARPU |
| **P&L** | Full income statement build (COGS split, opex by line, EBITDA, net income) | Black formulas, green links |
| **FCF** | Free cash flow: EBITDA → taxes → CapEx → NWC → unlevered FCF | Black formulas |
| **DCF** | Discount rate, PV of FCFs, terminal value (exit multiple + Gordon Growth), enterprise value | Black formulas |
| **Comps** | Three-bucket comp table with multiples, bucket weights, blended implied value | Blue inputs for multiples, black for calcs |
| **Precedents** | Precedent transaction multiples and implied value range | Blue inputs, black calcs |
| **Football** | Five-method triangulation summary + visualization data | Green links to all methods |
| **CapTable** | Cap table, waterfall at 3 exit values, preference analysis | Blue inputs for terms, black for waterfall |
| **RealOptions** | Probability-weighted option values by cluster | Blue inputs for probabilities/payoffs |
| **Scenarios** | Scenario toggle (Bear/Base/Bull) that feeds into Assumptions tab | Blue selector cell |
| **Sensitivity** | Three 2-variable grids + tornado chart data | Black formulas |
| **Checks** | Diagnostic checks, balance tests, cross-method reconciliation | Black formulas, red flags |

---

## Tab 1: Assumptions

### Layout Convention
- Column A: Assumption ID (R1, R2, C1, etc. — matches spec exactly)
- Column B: Assumption description
- Column C: Bear case value (blue text)
- Column D: Base case value (blue text)
- Column E: Bull case value (blue text)
- Column F: Active value (formula: pulls from C/D/E based on scenario selector)
- Column G: Source / tier label
- Column H: Status (Locked / Tier 1-3 / FLAGGED_GAP)
- Column I: Notes / rationale

### Scenario Selector
Single cell (e.g., Assumptions!B1) with value 1, 2, or 3 (Bear/Base/Bull). Column F uses:
```
=CHOOSE($B$1, C_row, D_row, E_row)
```
Every downstream tab references Column F only. Changing $B$1 switches the entire model between scenarios in one click.

---

## Tab 2: Members (The Cohort Engine)

### This is the most important tab in the model.

**Row structure (columns = years 2025-2033):**

```
SECTION 1: BEGINNING MEMBERS
Row 1:  Beginning Members (total)        = prior year Ending Members
Row 2:    of which: Year-1 cohort        = prior year Gross Adds (they're now in year 1)
Row 3:    of which: Year-2 cohort        = prior year Year-1 survivors
Row 4:    of which: Year-3+ cohort       = prior year Year-2 survivors + prior Year-3+

SECTION 2: CHURN (from Assumptions tab)
Row 5:  Year-1 churn rate               = green link to Assumptions (R10a)
Row 6:  Year-2 churn rate               = green link to Assumptions (R10b)
Row 7:  Year-3+ churn rate              = green link to Assumptions (R10c)

SECTION 3: CHURNED MEMBERS
Row 8:  Year-1 churned                  = Row 2 × Row 5
Row 9:  Year-2 churned                  = Row 3 × Row 6
Row 10: Year-3+ churned                 = Row 4 × Row 7
Row 11: Total churned                   = SUM(Row 8:10)

SECTION 4: SURVIVING MEMBERS (end of year, before new adds)
Row 12: Year-1 survivors                = Row 2 - Row 8
Row 13: Year-2 survivors                = Row 3 - Row 9
Row 14: Year-3+ survivors               = Row 4 - Row 10 + Row 13 (year-2 survivors graduate to 3+)

SECTION 5: NEW MEMBERS
Row 15: Gross Adds                      = green link to Assumptions (R12)

SECTION 6: ENDING MEMBERS
Row 16: Ending Members                  = Row 12 + Row 14 + Row 15
        (Note: Row 15 gross adds become next year's "Year-1 cohort" in Row 2)

SECTION 7: AVERAGE MEMBERS
Row 17: Average Members                 = (Row 1 + Row 16) / 2

SECTION 8: DIAGNOSTICS (output, not input)
Row 18: Net Adds                        = Row 15 - Row 11
Row 19: Net Member Growth %             = Row 18 / Row 1
Row 20: Blended Churn Rate              = Row 11 / Row 1
Row 21: Gross-to-Net Ratio              = Row 15 / Row 18
```

### Churn Rate Assumptions (from spec R10, expanded to cohort)

| Cohort | Bear | Base | Bull | Assumption ID |
|---|---|---|---|---|
| Year-1 (new members) | 30% | 22% | 15% | R10a |
| Year-2 | 18% | 14% | 10% | R10b |
| Year-3+ | 12% | 8% | 5% | R10c |

These go in the Assumptions tab as blue cells. The Members tab references them via green links.

### 2025 Starting Position (seed values, blue cells)

| Item | Value | Source |
|---|---|---|
| Beginning 2025 members | ~1.2M | Back-solved: ending 2.5M, ~103% growth implies ~1.2M start |
| Ending 2025 members | 2.5M | Series G press, Tier 1 |
| 2025 gross adds | ~1.7M | Back-solved from beginning, ending, and base churn |

### Gross Adds Assumptions (R12, by year)

Gross adds are a BLUE INPUT per year, not a formula. They represent the marketing/acquisition thesis. The implied CAC check (gross adds × assumed CAC vs. S&M budget) is computed on the Checks tab.

Rough priors for base case:
- 2026: 1.8-2.0M (Series G deployment, WHOOP 5.0 cycle)
- 2027: 1.6-1.8M (continued but decelerating)
- 2028: 1.3-1.5M (post-IPO normalization)
- 2029-2030: 1.1-1.3M (steady state acquisition)
- 2031-2033: 0.9-1.1M (mature, replacement + international)

---

## Tab 3: ARPU

### ARPU Decomposition (columns = years 2025-2033)

```
SECTION 1: SUBSCRIPTION ARPU
Row 1:  Base subscription (Core tier equivalent)     = green link to Assumptions
Row 2:  Tier premium (Peak/Life upgrade above Core)  = green link
Row 3:  Monthly plan premium (monthly payers pay more per year) = green link
Row 4:  Subscription ARPU                            = SUM(Row 1:3)

SECTION 2: NON-SUBSCRIPTION ARPU
Row 5:  Accessories / straps                         = green link
Row 6:  Advanced Labs (attach rate × avg test price)  = green link
Row 7:  Blood Pressure / Healthspan upsells           = green link
Row 8:  Non-subscription ARPU                         = SUM(Row 5:7)

SECTION 3: BLENDED
Row 9:  Blended ARPU                                 = Row 4 + Row 8
Row 10: Subscription mix %                           = Row 4 / Row 9

SECTION 4: GROWTH DIAGNOSTICS
Row 11: YoY ARPU growth                              = (Row 9 current / Row 9 prior) - 1
Row 12: ARPU growth from price                       = inflation component
Row 13: ARPU growth from mix shift                   = tier + attach component
```

### Key Assumptions for ARPU (blue cells on Assumptions tab)

| Component | 2025 Base | 2033 Base | Driver |
|---|---|---|---|
| Base subscription | $255 | $310 | 3% annual price inflation |
| Tier premium | $20 | $45 | Migration from Core to Peak (10%/yr of Core base) |
| Monthly plan premium | $15 | $15 | Stable (monthly payers are a fixed share) |
| Accessories | $25 | $30 | Replacement cycle, modest growth |
| Labs attach | $15 | $60 | Attach rate: 5% → 20% at $300 avg test |
| BP / Healthspan | $5 | $25 | Attach rate: 2% → 12% at $200 avg |
| **Blended ARPU** | **$335** | **$485** | |

### Labs Attach Rate (R14) — The Bucket-3 Thesis in a Cell

This is the single most important ARPU assumption. It determines whether WHOOP is valued as a subscription company or a health-data platform.

```
Labs Revenue per Member = Labs Attach Rate × Average Labs Price per Test

Bear: 3% attach × $250 avg = $7.50/member
Base: 10% attach × $300 avg = $30/member  
Bull: 25% attach × $350 avg = $87.50/member
```

The difference between bear and bull Labs attach swings blended ARPU by $80/member, which at 5M+ members is $400M+ of revenue. This single cell is worth more sensitivity analysis than the entire WACC discussion.

---

## Tab 4: Revenue

### Revenue Build (columns = years 2025-2033)

```
Row 1: Average Members                    = green link to Members!Row 17
Row 2: Blended ARPU                       = green link to ARPU!Row 9
Row 3: Implied Revenue (Members × ARPU)   = Row 1 × Row 2
Row 4: Deferred Revenue Adjustment        = green link to Assumptions
       (growth periods: recognized < booked; deceleration: recognized > booked)
Row 5: Recognized Revenue                 = Row 3 + Row 4

DIAGNOSTICS:
Row 6: YoY Revenue Growth %               = (Row 5 current / Row 5 prior) - 1
Row 7: Implied Bookings                   = Ending Members × Blended ARPU (annualized)
Row 8: Book-to-Revenue Ratio              = Row 7 / Row 5
Row 9: Revenue per Member Growth          = Row 2 growth (ARPU component)
Row 10: Member-Driven Growth              = Row 1 growth (volume component)
```

**Critical reconciliation (2025):**
```
Average Members (1.85M) × Blended ARPU ($350) = $648M ≈ R1 base ($650M) ✓
```

If this doesn't reconcile within 5%, something is wrong with member or ARPU assumptions. The Checks tab should flag this automatically.

### Deferred Revenue Treatment

For a 103% growth company selling annual subs upfront:
- **During growth:** recognized revenue < bookings (deferred balance grows)
- **At deceleration:** recognized revenue catches up and can briefly exceed new bookings pace
- **At steady state:** recognized ≈ bookings

Model as: Deferred Revenue Balance = Ending Members × ARPU × (avg months remaining / 12). Change in deferred balance flows through as an adjustment. In early years this is a ~5-15% drag on recognized vs. booked; at steady state it approaches zero.

---

## Tab 5: P&L

### Income Statement Build

```
Revenue                              = green link to Revenue!Row 5
  (-) Hardware COGS                  = Gross Adds × Loaded Hardware Cost (C2)
  (-) Subscription Delivery Cost     = Revenue × Sub Delivery % (C4)
  (-) Labs COGS                      = Labs Revenue × Labs COGS % (C17)
Gross Profit
  Gross Margin %                     = diagnostic

  (-) R&D                           = Revenue × R&D % (C8)
  (-) S&M                           = Revenue × S&M % (C9c)
      of which: Paid CAC             = Gross Adds × CAC per Add (C9a)
      of which: Brand/Athlete        = Assumptions (C9b)
      of which: Other S&M            = residual
  (-) G&A                           = Revenue × G&A % (C10)
  (-) SBC                           = Revenue × SBC % (C11)
EBITDA
  EBITDA Margin %

  (-) D&A                           = Revenue × D&A % or fixed schedule
EBIT
  (-) Tax                            = EBIT × Tax Rate (23-25%)
NOPAT
```

### Hardware COGS Design Decision

Hardware COGS is driven by GROSS ADDS (new members getting a device), NOT by total members or revenue. This is critical — it means:
- High-growth years have disproportionate hardware COGS (many new members)
- GAAP gross margin improves mechanically as growth slows (fewer gross adds per dollar of revenue)
- This is not operating leverage — it's an accounting artifact of the subsidy model

The model should compute BOTH:
- **GAAP Gross Margin** (hardware COGS included as COGS)
- **Unit Economics Gross Margin** (hardware COGS treated as acquisition cost, below the line)

Both are on the P&L tab; the GAAP version is the primary view; unit economics version is a memo line.

### S&M Consistency Check (on Checks tab)

```
Implied Paid CAC Spend   = Gross Adds × CAC per Add
Total S&M Budget          = Revenue × S&M %
Non-Paid S&M              = Total S&M - Paid CAC Spend

If Non-Paid S&M < $0: ERROR — growth requires more paid CAC than S&M budget allows.
If Non-Paid S&M < Brand Budget (C9b): WARNING — no room for performance marketing beyond base brand spend.
```

This check is what catches the "70% growth requires $380M marketing" problem. If the check fires, either growth assumptions are too aggressive or S&M % is too low.

---

## Tab 6: FCF

```
EBITDA                               = green link to P&L
  (-) Cash Taxes                     = Tax on EBIT (not EBITDA)
  (-) CapEx                          = Revenue × CapEx % (C13)
  (-) Change in NWC                  = ΔDeferred Revenue - ΔInventory - ΔOther WC
  (+) Add back SBC (if using GAAP EBITDA that excluded it... but we include SBC as real cost, so NO add-back)
Unlevered Free Cash Flow

FCF Margin %                         = diagnostic
```

### SBC Treatment Reminder
SBC is already included as a real cost in the P&L. Do NOT add it back in FCF. The model treats SBC as cash-equivalent compensation expense. Dilution from share issuance is modeled separately on the CapTable tab when converting enterprise value to per-share equity value.

---

## Tab 7: DCF

### Structure
```
SECTION 1: DISCOUNT RATE
  Risk-free rate (D1)                = green link to Assumptions
  ERP (D2)                           = green link
  Beta (D3)                          = green link (sensitivity axis)
  Size premium (D4)                  = green link
  CSRP (D5)                          = green link (sensitivity axis)
  Cost of equity / WACC (D8)         = D1 + D2×D3 + D4 + D5
  (No debt component — 100% equity)

SECTION 2: PV OF EXPLICIT PERIOD FCFs
  Year 1-7 FCF                       = green link to FCF tab
  Discount factor                    = 1 / (1 + WACC)^n
  PV of each year FCF                = FCF × discount factor
  Sum of PV (explicit)               = SUM

SECTION 3: TERMINAL VALUE — EXIT MULTIPLE (primary)
  Terminal year revenue               = green link to Revenue tab, year 7
  Terminal year EBITDA                = green link to P&L tab, year 7
  Exit multiple EV/Revenue (D11)     = green link to Assumptions
  Exit multiple EV/EBITDA (D12)      = green link to Assumptions
  Terminal value (revenue method)    = TV Rev × Exit multiple
  Terminal value (EBITDA method)     = TV EBITDA × Exit multiple
  PV of terminal value               = TV / (1 + WACC)^7

SECTION 4: TERMINAL VALUE — GORDON GROWTH (cross-check)
  Terminal year FCF                   = green link
  Perpetuity growth rate (D13)       = green link to Assumptions
  Gordon Growth TV                    = FCF × (1+g) / (WACC - g)
  PV of Gordon TV                    = Gordon TV / (1 + WACC)^7

SECTION 5: ENTERPRISE VALUE
  EV (exit multiple method)          = Sum PV explicit + PV TV (multiple)
  EV (Gordon Growth method)          = Sum PV explicit + PV TV (Gordon)
  Divergence %                       = |(multiple - Gordon)| / average
  FLAG if divergence > 25%

SECTION 6: TV DIAGNOSTICS
  TV as % of total EV                = PV TV / EV
  FLAG if > 75%
  Implied terminal growth from exit multiple = back-solve g from TV = FCF(1+g)/(WACC-g)
  Implied exit multiple from Gordon Growth   = back-solve multiple from Gordon TV / terminal metric

SECTION 7: EQUITY VALUE BRIDGE
  Enterprise Value
  (+) Cash (S11)                     = green link
  (-) Debt (S10)                     = green link (likely ~0)
  (-) Minority interests             = 0 (no subsidiaries)
  Equity Value
  (/) Fully diluted shares (S1)      = green link to CapTable
  Per-Share Value
```

### 5-Year Cross-Check (D24-D26)
Build as a separate section on the same tab:
- Same FCF stream, but only years 1-5
- Apply exit multiple to year-5 metrics (not year-7)
- Compare the two EV outputs
- If 7-year > 5-year by >30%, years 6-7 are doing suspiciously much value creation

---

## Tab 8: Comps

### Three-Bucket Layout

```
BUCKET 1: CONSUMER HARDWARE
  Garmin | EV | Revenue | EV/Rev (today, 6mo, 12mo, 3yr) | Growth | Rule of 40

BUCKET 2: CONSUMER SUBSCRIPTION
  Peloton | same columns (disaggregated, NOT averaged with Spotify)
  Spotify | same columns

BUCKET 3: HEALTH DATA / MEDICAL DEVICE
  Dexcom | same columns
  ResMed | same columns
  Masimo | same columns
  iRhythm | same columns

PRIVATE REFERENCE (not in blended calc):
  Oura | last round valuation, implied multiple

SYNTHESIS:
  Bucket medians
  Growth-adjusted multiples (EV/Rev ÷ Growth) per bucket
  Bucket weights (blue cells — Bear/Base/Bull/Series-G-implied)
  Weighted blended multiple
  WHOOP implied EV = blended multiple × WHOOP revenue metric
```

### Dual Back-Solve Section

```
NAIVE: What bucket-3 weight produces 9x blended? → ~65%
GROWTH-ADJUSTED: Strip growth premium (~2-3x), what bucket-3 weight produces ~6x? → ~35%
```

Both are formulas, not hardcoded. Changing comp multiples automatically updates the back-solve.

---

## Tab 14: Sensitivity

### Three 2-Variable Grids

**Grid 1: WACC × Terminal Multiple**
- Rows: WACC from 10% to 15% in 50bp steps
- Cols: Terminal EV/Revenue from 3x to 8x in 1x steps
- Cells: Enterprise Value

**Grid 2: Revenue Growth × EBITDA Margin**
- Rows: Phase 2 growth from 15% to 40% in 5pp steps
- Cols: Terminal EBITDA margin from 20% to 35% in 5pp steps
- Cells: Enterprise Value

**Grid 3: Churn × ARPU (WHOOP-specific)**
- Rows: Blended annual churn from 10% to 25% in 3pp steps
- Cols: 2033 blended ARPU from $350 to $550 in $50 steps
- Cells: Enterprise Value

### Tornado Chart Data
For each key assumption, compute EV at assumption ± 1 standard deviation (or ± 20% of base). Rank by absolute EV swing. Output as a data table that can be charted.

---

## Tab 15: Checks

### Automated Diagnostic Checks

| Check | Formula | Flag Condition |
|---|---|---|
| Members × ARPU = Revenue | Revenue!Row3 vs Revenue!Row5 | Divergence > 5% |
| S&M budget ≥ Paid CAC + Brand | P&L S&M - (Gross Adds × CAC) - Brand | < 0 |
| TV < 75% of EV | DCF TV% | > 75% |
| Exit multiple ↔ Gordon Growth | DCF divergence | > 25% |
| 7-year vs 5-year cross-check | DCF comparison | > 30% |
| Gross adds achievable | Gross Adds vs. historical peak | > 2x historical = warning |
| Rule of 40 trajectory | Growth + FCF margin by year | < 20 by Phase 3 = warning |
| ARPU > subscription price | Blended ARPU vs. lowest plan | < lowest plan = error |
| Churn × base > gross adds | Net adds negative | Flag |
| Cap table waterfall sums to 100% | CapTable validation | ≠ 100% |

---

## Formatting Conventions

### Color Coding (per xlsx skill standard)
- **Blue text (0,0,255):** All hardcoded inputs on Assumptions tab and any blue-cell inputs elsewhere
- **Black text (0,0,0):** ALL formulas and calculations
- **Green text (0,128,0):** Cross-sheet references (Members linking to Assumptions, Revenue linking to Members, etc.)
- **Red text (255,0,0):** External links (if any)
- **Yellow background (255,255,0):** FLAGGED_GAP assumptions needing attention

### Number Formatting
- Revenue/costs in $M with one decimal: "$#,##0.0"
- Members in thousands: "#,##0" with header "(000s)"
- ARPU in dollars: "$#,##0"
- Growth rates / margins: "0.0%"
- Multiples: "0.0x"
- Years as text strings: "2025" not "2,025"
- Negatives in parentheses: "$#,##0;($#,##0);-"

### Layout
- Row 1: Section headers (bold, merged where appropriate)
- Row 2: Sub-headers
- Row 3+: Data
- Freeze panes: Column A (labels) + Row 2 (headers) frozen on all tabs
- Print area set on key output tabs (DCF, Football, Comps)

---

## Build Sequence

1. **Assumptions tab first.** Populate all blue cells from spec. Scenario selector working.
2. **Members tab.** Build cohort engine. Verify 2025 ending = 2.5M.
3. **ARPU tab.** Build decomposition. Verify 2025 blended ≈ $350.
4. **Revenue tab.** Link Members × ARPU. Verify 2025 recognized ≈ $650M.
5. **P&L tab.** Build from Revenue down. Verify 2025 EBITDA margin ≈ 0-5%.
6. **FCF tab.** Build from P&L. Verify 2025 FCF positive (matches "cash flow positive" claim).
7. **DCF tab.** Discount FCFs, compute terminal value both ways, bridge to equity.
8. **Comps tab.** Populate from research. Compute bucket-weighted implied values.
9. **CapTable + Waterfall.** Build from Pitchbook data.
10. **Football tab.** Link all five methods.
11. **Sensitivity tab.** Build three grids + tornado.
12. **Checks tab.** Wire all diagnostics. Fix any flags before proceeding.
13. **Recalculate:** `python scripts/recalc.py whoop-valuation.xlsx`
14. **Verify zero formula errors before delivery.**

---

## What This Document Does NOT Cover

- **Specific numerical values for most assumptions.** Those are in the spec and research outputs. This document defines architecture, not content.
- **The IC memo or presentation.** Those are output-layer deliverables built after the model is complete.
- **Research methodology.** That's in the spec's Section 7 (Research Execution Policy).

This document is the bridge between "what we decided analytically" and "how to build it in Excel." It should be read alongside CLAUDE.md (project context) and the assumption spec (what goes in each cell).
