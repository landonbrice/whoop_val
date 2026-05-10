# WHOOP Valuation — Model Methodology (Master Reference)

**Purpose:** Persistent context document for any Claude instance (Code, Excel, chat) working on this valuation. Read this before touching the model. This document defines *what the model should do and why* — not specific cell references or row numbers, which change as the model evolves.

**Last updated:** May 2026

---

## 1. What We're Valuing and Why

WHOOP Inc. — private wearable-health company. Series G at $10.1B (March 2026), $575M raised, led by Collaborative Fund with Abbott, Mayo Clinic, QIA, Mubadala as strategics/sovereign. ~2.5M members, ~$1.1B exit-rate bookings (end 2025), 103% YoY subscription growth, cash flow positive.

**Central question:** Does intrinsic value plus real-option upside support the $10.1B mark?

**Central analytical move:** The Series G back-solve. At ~9x revenue, the market implicitly prices WHOOP as 60-70% health-data company (naive back-solve) or 30-40% health-data company plus growth premium (growth-adjusted). Which is correct determines whether the multiple holds or compresses as growth decelerates. That tension is the paper.

---

## 2. Five-Method Football Field

| Method | Role | Weight |
|---|---|---|
| Intrinsic DCF | Primary — fundamental value from unit economics | Core |
| Trading comps (3 buckets) | Market-derived multiple, segmented by business model | Core |
| Precedent transactions | Reality-check band, through-cycle and control premium | 5-10% |
| Last-round implied | $10.1B as market datapoint, decomposed | Anchor |
| Implied IPO trading range | Back-solved from Series G to public fair value ($13-15B) | Cross-check |

**Excluded:** Take-private LBO (wrong capital structure, locked IPO path, antitrust on strategic acquirers).

---

## 3. Revenue Architecture (The Core Design Decision)

**Revenue is computed from unit economics. It is never directly assumed.**

```
Members (cohort engine) × ARPU (decomposed) = Revenue (output)
Growth rate = diagnostic, not input
```

### Member Engine

Tracks members by cohort vintage (year-1, year-2, year-3+). Each vintage has its own churn rate. Gross adds are a direct input representing the marketing/acquisition thesis.

| Element | Type | Notes |
|---|---|---|
| Beginning members | Formula | = prior year ending |
| Gross adds | **Input** | Marketing thesis; compare against historical peak as sanity check |
| Churn (year-1) | **Input** | Highest churn; "try and quit" cohort. Bear 30%, Base 22%, Bull 15% |
| Churn (year-2) | **Input** | Stabilizing. Bear 18%, Base 14%, Bull 10% |
| Churn (year-3+) | **Input** | Retained core. Bear 12%, Base 8%, Bull 5% |
| Ending members | Formula | = survivors + new gross adds |
| Average members | Formula | = (beginning + ending) / 2. **Use this for revenue, not ending.** |

### ARPU Decomposition

Blended ARPU built from components, each with independent growth drivers:

| Component | ~2025 | Driver | Why It Matters |
|---|---|---|---|
| Base subscription | $255 | Annual price inflation (3%) | Stable floor |
| Tier premium | $20 | Core → Peak migration rate | Modest upside |
| Monthly plan premium | $15 | Share of monthly vs. annual payers | Stable |
| Accessories/straps | $25 | Replacement cycle | Minor |
| Advanced Labs | $15 | **Attach rate × avg test price** | **THE bucket-3 thesis variable** |
| BP/Healthspan | $5 | Attach rate × price | Growing |
| **Blended** | **~$335** | | |

**Labs attach rate is the single most important ARPU assumption.** It determines whether WHOOP is valued as a subscription company or a health-data platform. Bear 3%, Base 10%, Bull 25% attach — the difference swings ARPU by $80/member, which at scale is $400M+ of revenue.

### Revenue Reconciliation

```
2025: Average Members (~1.85M) × Blended ARPU (~$350) ≈ $650M recognized revenue ✓
```

**Key distinction:** "$1.1B run-rate" = December 2025 monthly bookings × 12 (exit velocity). Full-year 2025 recognized revenue ≈ $650M due to (a) growth ramp through the year and (b) ASC 606 deferred recognition of prepaid subscriptions. These are different numbers answering different questions. Use $650M as the 2025 denominator for comp multiples. Use $1.1B as the 2026 starting pace.

---

## 4. DCF Structure

### Three Phases

| Phase | Years | What's Happening | Growth Driver |
|---|---|---|---|
| Phase 1: Pre-IPO | 2026-2027 | Hypergrowth, Series G deployment | Gross adds acceleration |
| Phase 2: Post-IPO | 2028-2030 | Deceleration, margin expansion | Churn stabilization, ARPU expansion, international |
| Phase 3: Maturity | 2031-2033 | Scaling to steady state | TAM ceiling, healthcare attach resolution |
| Terminal | 2034+ | Perpetuity | GDP + inflation (3-5%) |

Growth rates are NOT inputs. They emerge from: gross adds trajectory + cohort churn curve + ARPU component growth. Phase labels are descriptive, not prescriptive.

**Peer trajectories as sanity check (not derivation):**
- Bear ≈ Peloton shape (sharp deceleration, S&M stuck high)
- Base ≈ Netflix shape (steady deceleration over 6 years)
- Bull ≈ Dexcom shape (sustained growth from new clinical indications)

### Scenario Structure

Three scenarios varying: growth drivers (gross adds, churn, ARPU), margin expansion path, S&M efficiency, and bucket weighting. WACC held constant across scenarios (methodological choice — flagged in memo as marginally overstating bear-case value by 10-15%).

Probability weights (25/50/25) are themselves a sensitivity. Report all three scenario EVs explicitly, not just the weighted average.

### Terminal Value

**Primary:** Exit multiple on terminal year revenue or EBITDA (at terminal-year growth rates, NOT current multiples — apply 40-60% compression from current comp multiples).

**Cross-check:** Gordon Growth (perpetuity rate 3-5% on terminal FCF).

**Diagnostic:** If exit multiple and Gordon Growth diverge >25%, an assumption is inconsistent. If TV > 75% of total EV, explicit forecast is doing too little work.

**Additional cross-check:** 5-year DCF with exit multiple at year 5. If 7-year DCF exceeds 5-year by >30%, years 6-7 are suspiciously valuable.

### Real Options (Separate, Never Embedded in Base Case)

Modeled as correlated outcome clusters:

| Cluster | What | Value | Probability |
|---|---|---|---|
| Correlated success | Healthcare/regulatory platform works, options cascade | $5-6B | 15-20% |
| Mixed | International works, healthcare stalls | $2-3B | 40-50% |
| Correlated failure | Healthcare thesis stalls, related options fail | $0.5-1B | 30-40% |

Added to base DCF EV, not embedded within it.

---

## 5. Comps Framework

### Three Buckets

| Bucket | Comps | Typical Multiple | Role |
|---|---|---|---|
| 1: Consumer Hardware | Garmin (+ Apple as reference only) | 1-3x rev | Floor |
| 2: Consumer Subscription | Peloton, Spotify (disaggregated, not averaged) | 0.8-4x rev | Cautionary range |
| 3: Health Data / MedDevice | Dexcom, ResMed, Masimo, iRhythm (+ Oura private reference) | 6-10x rev | Aspirational |

**Bucket weights are the thesis.** Bear 40/40/20, Base 20/40/40, Bull 10/30/60.

**Growth-adjusted multiples** (EV/Rev ÷ growth) are the analytical anchor. Normalizes across different growth profiles. WHOOP at 9x/103% = 0.09x is cheap vs. Dexcom at 12x/20% = 0.6x.

**Dual back-solve:** Naive (60-70% bucket 3 needed for 9x) vs. growth-adjusted (30-40% bucket 3 after stripping growth premium). Report both.

**Time variance:** Pull comp multiples at 4 time points (today, 6mo, 12mo, 3yr) to check regime sensitivity.

---

## 6. Cost & Margin Architecture

### Key Design Decisions

- **Hardware COGS driven by gross adds, not revenue.** New members get devices; existing members don't. This means GAAP gross margin improves mechanically as growth slows — accounting artifact, not operating leverage.
- **Model both GAAP GM and unit-economics GM.** GAAP includes hardware as COGS. Unit economics treats hardware as acquisition cost. Both views are informative.
- **SBC is a real cost, not an add-back.** Include in P&L as cash-equivalent expense. Do NOT add back in FCF. Dilution modeled separately on cap table.
- **S&M consistency check required.** Gross adds × CAC must not exceed total S&M budget. If it does, growth and cost assumptions are inconsistent.

### Phase Margin Trajectory (priors, not locked)

| Metric | Phase 1 | Phase 2 | Phase 3 | Terminal |
|---|---|---|---|---|
| Gross Margin | 58-62% | 63-70% | 70-76% | 75-78% |
| EBITDA Margin | 0-5% | 10-18% | 20-28% | 28-32% |
| FCF Margin | 5-10% | 12-22% | 20-26% | 25-28% |

---

## 7. Capital Structure

**Matters in bear case, noise in base/bull.** At $10B+ IPO all preferred converts; preferences don't bite. Below $5-6B, participating preferred and ratchets become dispositive.

Key inputs: ~$1.4B total raised as preference floor, waterfall at three exit scenarios ($5B/$10B/$20B), Ahmed ownership 12-18% fully diluted.

---

## 8. WACC

Cost of equity only (no debt). Build from:
- Risk-free (~4.3%, point estimate)
- ERP (~5.7%, point estimate)
- Beta (0.9-1.5, sensitivity axis — comp-derived, varies with bucket weighting)
- Size premium (~0.75%, point estimate)
- CSRP (1-3%, sensitivity axis)

Report as 4×3 grid (beta × CSRP), not a single number. Resulting range ~10-15%.

---

## 9. Model Integrity Checks

These should exist somewhere in the model and be verified before any output is trusted:

| Check | Condition | Flag |
|---|---|---|
| Members × ARPU ≈ Revenue | Divergence > 5% | Error |
| S&M ≥ Paid CAC + Brand spend | Negative residual | Error |
| TV < 75% of EV | TV% > 75% | Warning |
| Exit multiple ↔ Gordon Growth | Divergence > 25% | Warning |
| 7yr DCF vs 5yr cross-check | Divergence > 30% | Warning |
| Gross adds vs. historical peak | > 2x peak | Warning |
| Cohort vintages sum to total members | ≠ ending members | Error |
| Cap table waterfall sums to 100% | ≠ 100% | Error |
| Rule of 40 by Phase 3 | < 20 | Warning |

---

## 10. Formatting Conventions

- **Blue text:** Hardcoded inputs / assumptions
- **Black text:** All formulas
- **Green text:** Cross-sheet links
- **Yellow highlight:** FLAGGED_GAP assumptions needing attention
- Revenue/costs in $M, members in thousands, ARPU in $, rates in 0.0%, multiples in 0.0x
- Years as text ("2025" not "2,025"), negatives in parentheses

---

## 11. What Any Claude Instance Should Know

- **Never hardcode a calculated value.** Use Excel formulas so the model stays dynamic.
- **Never fabricate data.** If an assumption is unsourced, flag it as FLAGGED_GAP with a sensitivity range.
- **Revenue is computed, not assumed.** If you're tempted to type a growth rate into a revenue cell, stop. Growth emerges from the member engine.
- **Every assumption is a thesis.** "We assume 17% churn" means "we believe WHOOP's retention is similar to a mature fitness subscription with 24/7 wearable engagement, bounded by Peloton (worse) and Dexcom (better)." If you can't state the thesis, the assumption isn't grounded.
- **The $10.1B is a market datapoint, not ground truth.** The model's job is to produce an independent estimate and compare it to the market's price.
- **This document supersedes any conflicting instructions in individual conversations.** It is the canonical methodology reference.
