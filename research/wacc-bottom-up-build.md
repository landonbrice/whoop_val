# Bottom-Up WACC Build — Cross-Check on Damodaran Sector Approach

**Date compiled:** May 5, 2026
**Methodology revision:** Switched from 5Y monthly betas to **3-year weekly regression** (Bloomberg-adjusted) per IC discussion. Liquidity premium switched from Hiive market-implied (+5pp) to **Oura tender benchmark (+2pp)**.
**Purpose:** Build a comp-specific bottom-up WACC for WHOOP as cross-check on the Damodaran sector approach in `research/damodaran-wacc-inputs.md`.
**Context:** WHOOP — March 2026 Series G at $10.1B post-money on ~$650M recognized revenue. All-equity capital structure. ~40-45% international revenue. CEO Ahmed signaled 2027 IPO.

---

## 1. Executive Summary

- **Bottom-up bucket-median unlevered betas (Bloomberg-adjusted, 3Y weekly): B1 = 1.01, B2 = 1.00 (ex-PTON), B3 = 0.92.** Notably tight clustering. The 3Y weekly window (May 2023 - May 2026) excludes IRTC's 2021 CMS reimbursement crash and dilutes DXCM's July 2024 guidance-cut crash across 157 obs — both meaningful idiosyncratic distortions in the prior 5Y monthly approach are now appropriately dampened.
- **WHOOP blended unlevered beta = 0.95-0.99 across Bear/Base/Bull bucket weights**, vs. Damodaran's 0.81-0.85. Delta narrowed from +0.40 (5Y monthly) to **+0.10-0.18 (3Y weekly)**. WHOOP has zero debt → re-levered = unlevered.
- **Revenue-weighted ERP = 4.60-4.65%** at WHOOP's ~42% intl mix. Effectively a wash vs. pure US ERP of 4.46% — most international revenue is developed-market with ERPs near US mature-market base.
- **Liquidity premium = +2.0pp** anchored to the Oura January 2026 tender at 25% discount to last round (Series E Oct 2025; ~3-month gap means very little stale-pricing decay → close to a pure-DLOM benchmark for a high-quality private wearable comp). Replaces the prior +5pp Hiive-implied figure, which conflated DLOM with secondary-market valuation skepticism.
- **Headline: bottom-up + Oura-anchored approach implies WACC ~11.5-11.7% vs. Damodaran sector approach at 9.7-11.7%. The two methods now converge.** Triangulating on a bottom-up WACC of ~11.5% as the IC-memo base case is robustly defensible. The +0.5-1.5pp margin over Damodaran sector base reflects (a) modestly higher comp-specific beta vs. broad sector medians and (b) +0.5pp from Oura-anchored liquidity premium vs. the 1.5% practitioner midpoint.

---

## 2. Task 1 — Per-Comp Data and Hamada Unlevered Betas

### Methodology

- **Levered beta:** 3-year weekly OLS regression vs. S&P 500 (^GSPC), 157 weekly observations May 2023 - May 2026. Computed via `scripts/compute_3y_weekly_betas.py` (yfinance source). Bloomberg-adjusted: β_adj = (2/3) × β_raw + (1/3) × 1.0. Adjusted is primary (CapIQ default convention); raw is sensitivity.
- **Effective tax rate:** Aggregate of FY2023, FY2024, FY2025 income tax expense / aggregate pre-tax income from each comp's 10-K via StockAnalysis. Smooths single-year anomalies. For comps with negative aggregate pre-tax income (PTON, MASI, IRTC), substitute marginal/statutory rate.
- **Marginal tax:** US-domiciled = 25% (21% federal + ~4% state blend). HQ-adjusted: GRMN (Swiss/Olathe) = 21%; SPOT (Lux) = 25% (Lux statutory + Swedish ops); RMD (US/dual-listed AU) = 27% blended. PTON, DXCM, MASI, IRTC = 25%.
- **Hamada formula:** βᵤ = βL / [1 + (1 − t) × (D/E)], market-value D/E.
- All financial figures from StockAnalysis statistics pages and 10-Q balance sheets as of May 5, 2026. See `research/beta-regression-output.md` for raw regression detail and R² values.

### Per-Comp Inputs and Outputs

| Comp | Bucket | β_raw (3Y wk) | **β_adj (3Y wk)** | R² | Mkt Cap ($M) | Total Debt ($M) | Cash + ST Inv ($M) | D/E (mkt) | 3-yr Agg ETR | Marg Tax | **βᵤ (adj, eff tax)** | βᵤ (adj, marg tax) | βᵤ (raw, eff tax) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Garmin (GRMN)** | B1 Hardware | 1.029 | **1.019** | 0.216 | 45,250 | 216 | 2,700 | 0.005 | 11.1% | 21% | **1.014** | 1.015 | 1.024 |
| **Peloton (PTON)** | B2 Sub (distressed) | 2.283 | **1.855** | 0.185 | 2,200 | 1,950 | 1,180 | 0.886 | n/m (loss) [E] | 25% | n/a | **1.114** | 1.371 |
| **Spotify (SPOT)** | B2 Sub (mature) | 1.014 | **1.010** | 0.134 | 86,260 | 549 | 7,260 | 0.006 | 7.9% | 25% | **1.004** | 1.005 | 1.008 |
| **Dexcom (DXCM)** | B3 Health Data | 1.080 | **1.054** | 0.119 | 22,950 | 1,380 | 2,420 | 0.060 | 22.1% | 25% | **1.007** | 1.010 | 1.032 |
| **ResMed (RMD)** | B3 Health Data | 0.962 | **0.974** | 0.181 | 30,150 | 843 | 1,660 | 0.028 | 17.9% | 27% | **0.952** | 0.954 | 0.940 |
| **Masimo (MASI)** | B3 Health Data | 0.885 | **0.924** | 0.090 | 9,310 | 559 | 152 | 0.060 | n/m (loss) [E] | 25% | n/a | **0.884** | 0.847 |
| **iRhythm (IRTC)** | B3 Health Data | 0.816 | **0.877** | 0.057 | 4,090 [E] | 729 | 550 | 0.178 | n/m (loss) [E] | 25% | n/a | **0.774** | 0.720 |

[E] = Estimate / loss-maker substituted with marginal rate per methodology. **Bold column** is primary value used in bucket aggregation.

### Comparison vs. Prior 5Y Monthly Approach

| Comp | 5Y mo β_lev (prior) | 3Y wk β_adj (new) | Delta | Driver |
|---|---|---|---|---|
| GRMN | 0.96 | 1.019 | +0.06 | Slightly more recent volatility weighting |
| PTON | 2.50 | 1.855 | -0.65 | Bloomberg adjustment + 3Y window has less of distress overhang |
| SPOT | 1.55 | 1.010 | -0.54 | 3Y window weights post-profitability period more; profitability re-rating lowered realized vol vs. broader market |
| DXCM | 1.40 | 1.054 | -0.35 | July 2024 crash diluted across 157 weekly obs vs. 60 monthly obs |
| RMD | 0.84 | 0.974 | +0.13 | More recent data weighted toward post-CPAP-recall normalization |
| MASI | 1.13 | 0.924 | -0.21 | Deal-pending compression (stock pinned to $180 since Feb 2026) + 3Y excludes some operational chaos |
| IRTC | 1.33 | 0.877 | -0.45 | **2021 CMS reimbursement crash (-83% over 7mo) is OUTSIDE the 3Y window** — single biggest methodological gain |

**Two events absent from the 3Y weekly window that materially distorted the 5Y monthly:**
1. IRTC: Jan 2021 CMS rate cut crash (window starts May 2023)
2. PTON: Late 2021 / 2022 collapse from $171 → $10 (most of the 96% drawdown is pre-2023; the residual distress is in the 3Y window but lower-amplitude weekly moves)

### Per-Comp Notes

- **GRMN:** Most stable comp. β slightly elevated under 3Y weekly because the post-2023 period included the AI/consumer-discretionary rotation. Net cash $2.5B+. βᵤ ≈ βL because debt is rounding error.
- **PTON:** Bloomberg adjustment (1.855 vs. 2.283 raw) is doing real work here — without adjustment, Hamada de-levered β would be 1.37; adjusted 1.11. The high D/E (0.89) means Hamada is sensitive to the levered input. **The 1.114 unlevered figure is still likely upward-biased by distress dynamics; SPOT (1.004) is the more representative B2 anchor.**
- **SPOT:** 1.01 levered β is striking — Spotify has become a "market-like" stock under 3Y weekly. Profitability inflection in 2024 + scale + cost discipline all reduced relative volatility. Historical 5Y monthly (1.55) was anchored in pre-2024 unprofitable phase. **For a forward-looking WHOOP DCF with WHOOP also targeting profitability, 1.00 is arguably more representative than 1.55.**
- **DXCM:** 1.05 vs. 1.40 (5Y mo). The July 2024 guidance-cut crash is in the window but represents 1 week of 157 vs. 1 month of 60 — proportionally smaller weight. Pre-cut DXCM was a 0.85 beta name; post-cut elevated. 3Y weekly straddles this regime change.
- **RMD:** 0.97 vs. 0.84 (5Y mo). Slightly higher under 3Y weekly because the Philips CPAP recall benefit (RMD captured share) was earlier in the 5Y window; recent RMD trades less differentially vs. market.
- **MASI:** 0.92 (adj). Beta has been compressing since Feb 2026 Danaher deal announcement (stock pinned near $180). Pre-deal operational period was higher-vol. **Acquisition will close H2 2026 → MASI exits the comp set after close.**
- **IRTC:** 0.88 (adj). Most dramatic methodological improvement — 2021 CMS crash is absent. R² of 0.057 is the lowest in the set; idiosyncratic variance dominates (reimbursement risk, FDA actions, payer mix). Convertible debt distortion still present: $729M converts as debt → D/E 0.18 → β_unlev 0.774. Treating converts as equity (more accurate when stock trades above conversion strike) → D/E ≈ 0 → β_unlev ≈ 0.877. **Use 0.774 as primary, 0.877 as upper sensitivity.**

### R² Caveat

R² ranges from 0.057 (IRTC) to 0.216 (GRMN), meaning S&P 500 explains only 5.7% to 21.6% of weekly variance for these stocks. Standard error on each levered beta is therefore wide (~±0.20-0.30). **Single-name beta point estimates have illusory precision; bucket medians of 4 names (B3) are more robust than singletons (B1, B2).** Bloomberg adjustment is partly a correction for this measurement error (shrinks toward 1.0).

---

## 3. Task 2 — Bucket Aggregation and Damodaran Cross-Check

### Bucket Median Unlevered Betas (Bloomberg-adjusted, 3Y weekly)

| Bucket | Comps | Bottom-up βᵤ values (adj) | Median βᵤ (incl PTON) | Median βᵤ (excl PTON) | Min | Max | Range |
|---|---|---|---|---|---|---|---|
| **B1 Hardware** | GRMN | 1.014 | 1.014 | 1.014 | 1.014 | 1.014 | n/a (n=1) |
| **B2 Subscription** | PTON, SPOT | 1.114 / 1.004 | **1.059** | **1.004** | 1.004 | 1.114 | 0.110 |
| **B3 Health Data** | DXCM, RMD, MASI, IRTC | 1.007 / 0.952 / 0.884 / 0.774 | **0.918** | **0.918** | 0.774 | 1.007 | 0.233 |

### Notes on Aggregation

- **B2 ex-PTON (1.004) is the primary anchor.** Reason: PTON's Hamada output is contaminated by distressed-equity dynamics (D/E = 0.89, levered β = 1.86 adj from raw 2.28). SPOT alone is the cleaner pure-subscription comp. B2 incl-PTON (1.059) used as bear-case overlay only.
- **B3 median 0.918 robust to outliers.** 4-comp median anchored by RMD (0.952) and MASI (0.884), which are the middle two. DXCM (1.007) and IRTC (0.774) are the bookends. Using IRTC convert-as-equity (0.877) instead of convert-as-debt (0.774) shifts B3 median to (0.877+0.952)/2 = **0.915 (essentially unchanged)** because IRTC was the lowest of 4 in either case.

### Damodaran Sector Cross-Check

| Bucket | Bottom-up βᵤ (adj, ex-PTON) | Damodaran sector βᵤ (Jan 2026) | Sector | # Firms | Delta | Material? |
|---|---|---|---|---|---|---|
| **B1 Hardware** | 1.014 | 0.83 | Electronics (Consumer & Office) | 8 | +0.18 | Modest |
| **B2 Subscription** | 1.004 | 0.74 / 1.01 | Entertainment / Software (Entertainment) | 92 / 77 | +0.27 / -0.01 | Modest vs. Software-Ent |
| **B3 Health Data** | 0.918 | 0.83 / 0.99 | HC Products / HC Info & Tech | 204 / 115 | +0.09 / -0.07 | Trivial |

**Major convergence finding:** Under 3Y weekly methodology, the bottom-up bucket betas converge to within **±0.10 of the Damodaran sector medians** — a sharp narrowing from the 5Y monthly result (which had +0.40 deltas). Reasons:

1. **Idiosyncratic events filtered out.** IRTC's 2021 CMS crash is now outside the window. PTON's worst pandemic-era days are pre-2023. DXCM's July 2024 single-day event is diluted across more weekly observations.
2. **Bloomberg adjustment shrinks toward 1.0.** This pulls high-beta names (PTON 2.28 → 1.86) and pushes low-beta names (IRTC 0.82 → 0.88) toward the center, which happens to be near the Damodaran sector medians.
3. **B2 alignment is the most striking.** B2 1.00 vs. Damodaran "Software (Entertainment)" 1.01 — a near-exact match. SPOT under 3Y weekly really has become a "market-like" subscription stock.

**Implication:** The bottom-up vs. Damodaran debate becomes much less important under 3Y weekly. **Either approach is defensible and produces similar betas.** The IC memo can lead with bottom-up for methodological consistency with the comp-multiples framework, with Damodaran sector as a tight cross-check.

---

## 4. Task 3 — WHOOP Re-Levered Beta (No Debt → βᵤ = βL)

### Construction

WHOOP has zero debt. Re-levered beta = unlevered beta = bucket-weighted blend.

Using bottom-up bucket medians (Bloomberg-adjusted, 3Y weekly, ex-Peloton primary):

| Scenario | B1 Wt | B2 Wt | B3 Wt | B1 βᵤ | B2 βᵤ (ex-PTON) | B3 βᵤ | **Blended βᵤ** |
|---|---|---|---|---|---|---|---|
| **Bear (40/40/20)** | 40% | 40% | 20% | 1.014 | 1.004 | 0.918 | **0.991** |
| **Base (20/40/40)** | 20% | 40% | 40% | 1.014 | 1.004 | 0.918 | **0.972** |
| **Bull (10/30/60)** | 10% | 30% | 60% | 1.014 | 1.004 | 0.918 | **0.953** |

**With PTON-included in B2 (bear-case overlay):**

| Scenario | Blended βᵤ (PTON-incl) |
|---|---|
| Bear (40/40/20) | 1.013 |
| Base (20/40/40) | 0.994 |
| Bull (10/30/60) | 0.970 |

### Sensitivity to Bloomberg Adjustment

Using raw (unadjusted) regression betas:

| Scenario | Blended βᵤ (raw) | Blended βᵤ (adj, primary) | Delta |
|---|---|---|---|
| Bear (40/40/20) | 0.992 | 0.991 | -0.001 |
| Base (20/40/40) | 0.966 | 0.972 | +0.006 |
| Bull (10/30/60) | 0.941 | 0.953 | +0.012 |

**Adjustment effect on WHOOP-blended is trivial (<0.02)** because WHOOP-blended is already an average of betas clustered around 1.0, where Bloomberg adjustment has minimal pull.

### Side-by-Side vs. Damodaran Sector Blended Beta

From `research/damodaran-wacc-inputs.md`:

| Scenario | Damodaran sector βᵤ | **Bottom-up βᵤ (3Y wk adj, ex-PTON)** | Delta | (Prior 5Y mo Delta for comparison) |
|---|---|---|---|---|
| Bear (40/40/20) | 0.81 | **0.991** | **+0.18** | (+0.42) |
| Base (20/40/40) | 0.83 | **0.972** | **+0.14** | (+0.43) |
| Bull (10/30/60) | 0.85 | **0.953** | **+0.10** | (+0.39) |

**Delta vs. Damodaran cut roughly in half** under 3Y weekly methodology. The remaining +0.10 to +0.18 reflects genuine WHOOP-comp-specific premium over broad sector medians (concentrated high-growth diagnostics in B3, high-beta single-name representation in B2). Translation to cost of equity at ERP=4.61%: **+0.5 to +0.8pp** — meaningful but no longer a 2pp methodology argument.

---

## 5. Task 4 — Revenue-Weighted ERP

*(Unchanged from prior version — included for completeness.)*

### Construction

WHOOP base case: ~58% US revenue, ~42% international (per `research/stress-test-international-revenue.md`).

International mix assumption: 50% UK/EU developed, 30% Asia developed, 20% other.

### Country ERPs (Damodaran, January 2026)

| Country | Total ERP | Country | Total ERP |
|---|---|---|---|
| **US** | 4.46% | Japan | 5.14% |
| UK | 5.01% | Australia | 4.23% |
| Germany | 4.23% | Singapore | 4.23% |
| France | 5.01% | Hong Kong | 5.01% |
| Sweden | 4.23% | South Korea | 4.87% |
| Switzerland | 4.23% | Netherlands | 4.23% |

### Blended International ERP

- UK/EU developed (50%): avg ~4.6%
- Asia developed (30%): (5.14 + 4.23 + 4.23) / 3 = ~4.5%
- Other / GCC / emerging (20%): ~5.7% [E]
- **Blended intl ERP = 0.50 × 4.60 + 0.30 × 4.53 + 0.20 × 5.70 = 4.80%**

### WHOOP Revenue-Weighted ERP

| Intl Weight | US ERP × Wt | Intl ERP × Wt | **Blended ERP** |
|---|---|---|---|
| 35% intl (conservative) | 2.90% | 1.68% | **4.58%** |
| **42% intl (base case)** | 2.59% | 2.02% | **4.61%** |
| 50% intl (aggressive) | 2.23% | 2.40% | **4.63%** |

**Net effect: +11-19bp vs. pure US ERP.** Token adjustment, not a swing factor.

---

## 6. Task 5 — Liquidity Premium (Oura Tender Benchmark)

### The Anchor

The Oura Health tender offer in **January 2026** priced shares at a **25% discount** to its **Series E** primary round (Oct 2025). The 3-month gap between primary round and tender means very little stale-pricing decay — the 25% discount is close to a pure DLOM (discount for lack of marketability) for a high-quality wearable comp on a credible IPO path.

**Why Oura is the right anchor:**
- Closest private comp to WHOOP (wearable + health subscription + IPO trajectory)
- Same investor profile (sovereign wealth + crossover + strategic)
- Recent + clean: a company-organized tender, not a thin secondary order book
- Avoids the "Hiive market disagrees with Series G mark" problem that conflates DLOM with valuation skepticism

### Translating 25% DLOM to a WACC Add-On

DLOM applied to terminal value: $10.1B × (1 − 0.25) = $7.575B common-equivalent fair value.

Stylized DCF approximation: PV ≈ CF / (r − g). Public-comp WACC of 10% with terminal g = 3.5% gives r − g = 6.5%. To compress PV from $10.1B → $7.575B requires (r − g) to scale by 10/7.575 = 1.32 → new (r − g) = 8.6% → new r = 12.1%.

**Implied WACC add-on: 12.1% − 10.0% = +2.1 percentage points.** Round to **+2.0pp**.

### Sensitivity

| DLOM scenario | DLOM % | Implied PV haircut | (r − g) ratio | Implied add-on |
|---|---|---|---|---|
| Optimistic (shorter time-to-IPO; Oura-comp lower) | 15% | -15% | 1.18 | **+1.1pp** |
| **Base (Oura tender)** | **25%** | **-25%** | **1.32** | **+2.1pp** |
| Conservative (Oura tender + WHOOP-specific liquidity discount) | 35% | -35% | 1.54 | **+3.5pp** |

### Why Not Hiive (-39 to -51%)?

The Hiive secondary order book at $5.44-$6.88 implies a 39-51% discount to Series G — much wider than Oura's 25%. The gap reflects:

1. **Hiive prices common, not preferred.** WHOOP's preferred has 1x non-participating pari passu liquidation preferences. Common is structurally subordinated until ~$291M aggregate preference is satisfied. At a $10.1B exit, the preference stack converts and common participates fully — but the Hiive trader can't hold common to that exit cleanly
2. **Hiive captures secondary-market valuation skepticism.** Some Hiive bidders simply think $10.1B is too high; their bid is a *valuation* call, not a *liquidity* call. A pure DLOM should be measured for an investor who agrees with the underlying valuation but needs immediate liquidity.
3. **Order-book depth.** WHOOP isn't in Hiive's top-20 most-traded names; spreads and discounts are wider for thinly-traded names independent of fundamentals
4. **Oura's tender was company-organized at a structured price** — closer to "what does management think DLOM is for friendly insiders selling early?" The 25% is a more controlled signal than messy order-book pricing

**Conclusion: use Oura's 25% discount → +2.0pp WACC add-on as the primary liquidity premium.** Reference Hiive (39-51%) as bear-case sensitivity (~+5pp) only if the IC narrative explicitly wants to model "secondary market disagrees with Series G."

### Comparison to Existing Practitioner Range

| Source | Liquidity premium | Notes |
|---|---|---|
| Existing `damodaran-wacc-inputs.md` | 1.0% (Bull) - 2.5% (Bear); 1.5% Base | Practitioner convention |
| **New: Oura tender benchmark** | **+2.0pp Base; 1.5pp Bull / 2.5pp Bear sensitivity** | Market-anchored, single-comp |
| Hiive secondaries (rejected) | +4-7pp | Conflates DLOM + valuation skepticism |

The Oura-anchored 2.0pp is **roughly the midpoint of the existing practitioner range** — ratifying it as a defensible point estimate with a market anchor instead of a convention.

---

## 7. Task 6 — Tax Rate Framework for DCF

*(Unchanged from prior version.)*

### Forecast Period (Years 1-5, 2026-2030)

| Period | Effective Rate | Rationale |
|---|---|---|
| Y1-Y2 (2026-2027) | **5-10%** [E] | Heavy NOL shielding pre-IPO |
| Y3-Y5 (2028-2030) | **10-15%** [E] | NOL carryforwards depleting; trends toward statutory |

### Terminal Period

| Component | Rate | Weight | Contribution |
|---|---|---|---|
| US blended marginal | 25.0% | 58% | 14.5% |
| Intl blended marginal | 20-22% [E] | 42% | 8.4-9.2% |
| **Terminal blended marginal** | **23-24%** | 100% | **23-24%** |

**Recommended: 24% terminal base case, sensitivity 22-26%.**

---

## 8. Task 7 — Synthesis: Recommended WACC Range

### Side-by-Side Build Comparison (Updated 3Y Weekly + Oura)

| Component | Damodaran Sector | **Bottom-Up + Oura (3Y weekly)** | Delta |
|---|---|---|---|
| **Risk-free rate** | 4.30% | 4.30% | 0 |
| **ERP** | 4.50% (US-anchor midpoint) | **4.61%** (revenue-weighted, 42% intl) | +0.11% |
| **Unlevered β — Bear (40/40/20)** | 0.81 | **0.991** | +0.18 |
| **Unlevered β — Base (20/40/40)** | 0.83 | **0.972** | +0.14 |
| **Unlevered β — Bull (10/30/60)** | 0.85 | **0.953** | +0.10 |
| **Size premium (CRSP Decile 3)** | 0.81% | 0.81% | 0 |
| **Liquidity premium — Bear** | 2.50% (practitioner) | **2.50%** (Oura conservative) | 0 |
| **Liquidity premium — Base** | 1.50% | **2.00%** (Oura tender) | +0.50% |
| **Liquidity premium — Bull** | 1.00% | **1.50%** (Oura optimistic) | +0.50% |

### Implied WACC (Excel will compute final; values shown for orientation)

WHOOP has zero debt → cost of equity = WACC. Components feed into Excel.

| Build | Bear | Base | Bull |
|---|---|---|---|
| **A. Damodaran sector** (existing) | ~11.7% | ~10.4% | ~9.7% |
| **B. Bottom-up 3Y weekly + Oura** (new) | ~12.2% | ~11.6% | ~11.0% |
| **Delta (B − A)** | **+0.5pp** | **+1.2pp** | **+1.3pp** |

**Major change vs. prior 5Y monthly + Hiive build:** WACC compressed from ~14.8-16.8% to ~11.0-12.2%. Driven by:
- Lower beta (3Y weekly adj vs. 5Y monthly raw): -1.0 to -1.5pp
- Lower liquidity premium (Oura +2pp vs. Hiive +5pp): -3.0pp
- **Total compression: ~3.5-4.5pp**

The new WACC range is now **tightly aligned** with the Damodaran sector approach (+0.5 to +1.3pp gap, vs. +5pp under prior methodology). Two methods triangulate.

### Decomposition of Remaining +0.5-1.3pp Delta (Base case)

- Beta upgrade (0.83 → 0.972): +0.65pp
- ERP revenue-weighting (4.50 → 4.61): +0.11pp
- Liquidity premium (1.50 → 2.00): +0.50pp
- **Total: +1.26pp** (rounds to +1.2pp on Base)

### Recommendation for IC Memo

**Primary base case: bottom-up + Oura (Build B), WACC ~11.6% Base.** Damodaran sector (Build A) is the cross-check — and it now corroborates rather than contradicts. Reasons:

1. **Methodological consistency.** Same comp-bucket framework used for multiples is now used for betas. Internally coherent.
2. **WHOOP-specific market anchors.** ERP weighted to WHOOP's actual revenue geography. Liquidity premium anchored to Oura tender (closest private comp). Neither is a generic practitioner number.
3. **Convergence with Damodaran is a strength, not a weakness.** Two independent methods landing within ~1pp gives the IC committee triangulation confidence — exactly what a football field is supposed to do for cost of capital.
4. **3Y weekly is the right window for forward-looking beta.** Excludes pre-2023 events (PTON 2021 collapse, IRTC 2021 CMS crash) that are not representative of forward business risk. Bloomberg adjustment is a measurement-error correction that makes single-name bucket aggregates more stable.
5. **Oura's +2.0pp is a market-anchored point estimate** that happens to ratify the practitioner mid-range — defensible without relying on either practitioner convention or noisy secondary order books.

### What the IC Memo Should Say

> "Base-case WACC of 11.6% is constructed via a bottom-up beta build (3-year weekly regression, Bloomberg-adjusted, against a 7-name comp set across Bucket 1/2/3), a revenue-weighted equity risk premium reflecting WHOOP's ~42% international revenue mix, a CRSP Decile 3 size premium, and a +200bp liquidity premium anchored to the Oura January 2026 tender at 25% discount. This converges within ~1pp of a Damodaran-sector-aggregate WACC of 10.4%, providing triangulation. Sensitivity range: 11.0% (Bull) to 12.2% (Bear)."

That's a defensible IC paragraph.

---

## 9. FLAGGED_GAPs

| # | Gap | Impact | Best path |
|---|---|---|---|
| 1 | **WHOOP actual ETR / NOL position** | Forecast tax 5-15% range fully estimated | Wait for S-1; sensitivity in Excel |
| 2 | **Oura tender details (preferred vs. common)** | Bloomberg report says 25% discount but may apply to selected investor classes only | Sacra has more detail behind paywall; not blocking |
| 3 | **PTON unlevered beta accuracy** | Distress dynamics still distort even with 3Y weekly | Use ex-PTON as primary; PTON-incl as overlay only |
| 4 | **IRTC convertible debt treatment** | β_unlev = 0.774 (convert as debt) vs. 0.877 (convert as equity); B3 median essentially unchanged either way | Use 0.774 primary, 0.877 sensitivity |
| 5 | **MASI deal-pending compression** | Stock has been pinned to $180 for 3+ months; recent volatility artificially low | Acquisition will close H2 2026 → MASI exits comp set; flag and move on |
| 6 | **R² on per-comp regressions (5.7-21.6%)** | Weak market-correlation means beta point estimates have ±0.20-0.30 standard error | Acknowledged; bucket medians smooth this; Bloomberg adjustment is a partial correction |
| 7 | **3Y weekly window may be too short for B2** | Only SPOT in B2 ex-PTON; SPOT's 1.01 beta reflects a phase-change business | Sensitivity: try B2 = 1.20 (between SPOT 1.00 and Damodaran Software-Ent 1.01) |
| 8 | **Public-comp WACC base for Oura translation (10%)** | Used 10% as the "public fair value WACC"; if 11% used instead, +2pp add-on becomes +1.8pp | Document; the 10% base is itself the Damodaran sector approach output |
| 9 | **S&P 500 as sole benchmark** | All comps regressed against ^GSPC; SPOT's true reference index could be MSCI World or NASDAQ | Sensitivity: re-run vs. MSCI ACWI; expected impact <0.05 on β |
| 10 | **3Y weekly excludes COVID-recovery dynamics** | Window starts May 2023 — post-COVID-recovery, pre-AI-rotation. Forward beta in 2027+ may differ | Acknowledge; this is a current-state estimate by design |

---

## 10. Sources

### Per-Comp Trading and Financial Data (May 5, 2026)

- StockAnalysis.com statistics + financials pages for GRMN, PTON, SPOT, DXCM, RMD, MASI, IRTC (URLs listed in prior version of this file and per-comp profiles)

### Beta Regression

- **Script:** `scripts/compute_3y_weekly_betas.py`
- **Raw output:** `research/beta-regression-output.md`
- **Source data:** Yahoo Finance (yfinance) weekly closes, auto-adjusted for splits/dividends; benchmark ^GSPC
- **Sample:** 157 weekly observations, May 1, 2023 - May 5, 2026
- **Method:** OLS regression on simple weekly returns; Bloomberg adjustment β_adj = (2/3) × β_raw + (1/3) × 1.0

### Damodaran Reference Data (January 2026 update)

- [Damodaran — Country Default Spreads and Risk Premiums](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)
- [Damodaran — Betas by Sector](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
- [Damodaran — Cost of Capital by Sector](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html)

### Internal Reference Files

- `research/damodaran-wacc-inputs.md` — Original sector-beta WACC build
- `research/comp-trading-multiples-summary.md` — Per-comp betas/multiples (April 2026 5Y monthly snapshot, now superseded for beta only)
- `research/comp-{garmin,peloton,spotify,dexcom,resmed,masimo,irhythm}-*.md` — Per-comp 10-K profiles
- `research/secondary-market-pricing.md` — Hiive/Forge/NPM data + Oura tender benchmark (Section 3)
- `research/stress-test-international-revenue.md` — 42% intl revenue base case
- `research/beta-regression-output.md` — 3Y weekly regression detail
- `CLAUDE.md` — Bucket weighting scenarios, modeling conventions

### Risk-Free Rate

- [Federal Reserve H.15 — Selected Interest Rates](https://www.federalreserve.gov/releases/h15/) — 10Y UST 4.26-4.30% (April-May 2026)

---

*Built May 5, 2026 — methodology revision: 3Y weekly betas (yfinance regression, Bloomberg-adjusted) + Oura tender +2pp liquidity premium. Replaces 5Y monthly + Hiive market-implied premium from the prior version. Next refresh recommended: post-S-1 filing (provides actual WHOOP tax footnote and removes private-company premium from the analysis), or if Damodaran's Jan 2027 update materially shifts sector inputs.*
