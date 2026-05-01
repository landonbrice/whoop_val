# Stress Test: WHOOP 2025 Revenue Reconciliation

**Date:** April 16, 2026
**Purpose:** Stress-test the base case $725M recognized revenue estimate that anchors the valuation model. Determine whether the true trailing multiple at $10.1B is ~10x, ~14x, or ~20x.
**Status:** Complete (first pass)

---

## 1. The $260M Getlatka Figure: What It Actually Represents

### Getlatka's Methodology

Getlatka (Nathan Latka's SaaS database) sources revenue data primarily from **CEO-reported figures confirmed live on camera during podcast interviews**. Nathan Latka interviewed Will Ahmed on February 24, 2021. No evidence of a more recent Getlatka-specific WHOOP interview was found.

**Key finding:** The $260M figure is labeled "Jun 2025" on Getlatka's WHOOP page, with the headline "How Whoop hit $260M revenue with a 1.2K person team in 2025." However, there is **no evidence of a 2024-2025 podcast interview** where Ahmed confirmed this figure. Getlatka likely sourced this from secondary data (media reports, web scraping, or third-party estimates) rather than a direct CEO confirmation.

### What $260M Most Likely Represents

| Interpretation | Likelihood | Evidence |
|---|---|---|
| **Calendar 2024 recognized revenue** | **High (60%)** | Pitchbook shows $200M for 2024; Getlatka may use a slightly different cut-off or include partial Q1 2025. The ~30% premium over Pitchbook's $200M is consistent with a later data capture window. |
| **H1 2025 recognized revenue (annualizing to ~$520M)** | Medium (25%) | If Getlatka captured data through June 2025, this is plausible. Annualized: $520M. |
| **TTM recognized revenue as of mid-2025** | Medium (15%) | A TTM window ending June 2025 would blend some low pre-5.0 months with higher post-launch months. |
| **2025 full-year recognized revenue** | **Very low (<5%)** | Inconsistent with the $1.1B bookings run-rate and the 36Kr investor estimate of ">$500M." At $260M revenue with $1.1B bookings, the bookings-to-revenue ratio would be 4.2x — implausibly high for a subscription business. |

### Verdict on $260M

**The $260M is almost certainly stale data representing CY2024 or early-2025 recognized revenue, NOT full-year 2025.** Getlatka's methodology is optimized for SaaS companies with CEO-confirmed data; for WHOOP, it appears to be using secondary sources with a lag. The figure is directionally useful as a CY2024 baseline but should not be used as the 2025 revenue anchor.

**Confidence:** High that $260M is NOT 2025 full-year revenue.

---

## 2. Every Revenue Data Point Found

| # | Metric | Value | Source | Date | What It Measures | Confidence |
|---|---|---|---|---|---|---|
| 1 | "Bookings run-rate" (exit 2025) | $1.1B | TechCrunch / CEO Ahmed | Mar 2026 | Annualized December 2025 bookings | **High** |
| 2 | Pitchbook "Total Revenue" (2025 TTM) | $1.1B | Pitchbook | Apr 2026 | Likely mirrors company-reported bookings | **High** (but may conflate bookings/revenue) |
| 3 | Pitchbook "Total Revenue" (2024) | $200M | Pitchbook | Apr 2026 | CY2024 revenue (Pitchbook-sourced) | **High** |
| 4 | Getlatka revenue | $260M | Getlatka | Jun 2025 | Likely CY2024 or early-2025 revenue | **Medium** (stale) |
| 5 | 36Kr investor estimate | >$500M | 36Kr / Hard Krypton | Apr 2026 | Investor projection of 2025 revenue | **Medium** |
| 6 | CB Insights revenue (2025) | $1.1B | CB Insights | Apr 2026 | Mirrors Pitchbook; likely bookings conflated as revenue | **Medium** (likely not recognized revenue) |
| 7 | SaveDelete: "hit $1B in ARR" | $1.0B ARR | SaveDelete | Apr 2026 | Claims "annual recurring revenue by end of 2025" | **Low-Medium** (secondary source interpreting press) |
| 8 | SaveDelete: "10x ARR" | 10x | SaveDelete | Apr 2026 | Derives $10.1B / $1B ARR = 10x | **Low** (relies on ARR interpretation) |
| 9 | Implied ARPU x members | $655M-$758M | Bottom-up model | Apr 2026 | 2.5M members x $262-$303 ARPU | **Medium** (assumes all 2.5M are active) |
| 10 | Active member estimate (industry) | 1.2M-2.0M | Max Weinbach / X | Apr 2026 | Suggests active base may be smaller than 2.5M | **Low** (single analyst estimate) |

### Critical New Finding: The "ARR" Claim

SaveDelete explicitly states WHOOP "hit $1 billion in annual recurring revenue by the end of 2025" and derives "roughly 10x ARR" for the $10.1B valuation. This is the **only source** that uses the term "ARR" rather than "bookings run-rate."

**Assessment:** SaveDelete is a secondary tech news aggregator. The original TechCrunch article — the primary source based on direct Ahmed interview — uses "bookings run-rate," NOT "ARR." SaveDelete appears to have **re-interpreted** "bookings run-rate" as "ARR," which is a meaningful analytical error. ARR in SaaS means annualized subscription revenue, excluding one-time hardware sales. Bookings includes hardware. If the $1.1B is truly ARR (subscription-only), that is a much stronger signal than bookings. But the primary source does not support this interpretation.

**Verdict:** The $1.1B is **bookings run-rate**, not ARR. Do not treat it as recognized revenue or pure subscription ARR without additional evidence.

---

## 3. The Active Member Question: Is 2.5M Overstated?

### The Problem

The "2.5M+ members" figure comes from the Series G press release. But "members" could mean:
- (A) Current active paying subscribers
- (B) Members with any status (active + paused + recently churned)
- (C) Cumulative members who ever signed up

This matters enormously for the bottom-up revenue build:
- At 2.5M active subscribers x $262 ARPU = $655M subscription revenue
- At 1.5M active subscribers x $262 ARPU = $393M subscription revenue

### Evidence

| Source | Claim | Interpretation |
|---|---|---|
| Series G press release | "2.5M+ members" | Likely active members (companies report active for fundraising) |
| Max Weinbach (X/Twitter) | "Most estimates put Whoop at ~1.2-2M active members" | Lower range; from tech analyst |
| WHOOP Year in Review 2025 | References "members" broadly | Suggests 2.5M is the number WHOOP uses officially |
| Peloton parallel | Peloton reported "Connected Fitness Subscribers" as current active | Standard industry practice is to report active |

### Assessment

**Most likely:** The 2.5M figure represents **active members** (current paying subscribers), consistent with how subscription companies report for fundraising. However, this could include members on paused subscriptions or in a grace period. The Weinbach estimate of 1.2-2M is speculative and comes from a single tweet.

**For the model:** Use 2.5M as active members with a sensitivity range of 2.0M-2.5M.

**Risk factor:** If only 2.0M are truly active, subscription revenue drops from $655M to $524M, reducing total revenue estimate by ~$130M.

---

## 4. Bookings-to-Revenue Conversion Analysis

### How "Bookings Run-Rate" Works

CEO Ahmed's TechCrunch quote: "When you're shipping millions of hardware units around the world while running a subscription business, investors need to understand the cash dynamics of managing all of that simultaneously — inventory, hardware costs, and recurring revenue at once."

He explicitly chose "bookings" over "revenue." The $1.1B is the **annualized December 2025 monthly bookings x 12**.

### Decomposing the Bookings-to-Revenue Gap

Three factors create the gap between $1.1B bookings run-rate and recognized revenue:

#### Factor 1: Annualization Effect (~$150M-$250M gap)

The $1.1B is December 2025 monthly bookings annualized. But WHOOP grew 103% YoY, meaning January 2025 bookings were roughly half of December 2025. Cumulative 2025 bookings are lower than $1.1B.

**Math:** If bookings grew linearly from ~$550M annualized (Jan 2025) to $1.1B annualized (Dec 2025):
- Average monthly bookings rate across 2025: ~$825M annualized
- Cumulative 2025 bookings: ~$825M (not $1.1B)
- Annualization gap: ~$275M

**If bookings grew on an S-curve** (slower early, faster H2 due to WHOOP 5.0 May launch):
- Average rate: ~$750M annualized
- Cumulative 2025 bookings: ~$750M
- Annualization gap: ~$350M

#### Factor 2: Deferred Revenue (~$100M-$200M gap)

Under ASC 606, annual subscription revenue is recognized ratably. A customer signing up in December for a $239 annual plan generates only $20 in December recognized revenue, with $219 deferred.

At the December $1.1B annualized rate:
- Subscription share of bookings: ~85% = ~$935M annualized
- Annual plan share: ~60% = ~$561M annualized from annual plans
- Average remaining obligation at year-end: ~6 months = $280M deferred
- Net change in deferred revenue during 2025 (build-up from growth): ~$100M-$200M

#### Factor 3: Hardware Timing (~$50M-$100M gap)

Hardware ordered in late December but shipped/delivered in January is a booking in 2025 but revenue in 2026.

### Peer Calibration: Peloton's Deferred Revenue

Peloton's actual deferred revenue balances from 10-K filings (labeled "Unearned Revenue"):

| Period | Unearned Revenue | TTM Revenue | As % of TTM Revenue |
|---|---|---|---|
| FY2021 (Jun '21) | $164.8M | $4,022M | **4.1%** |
| FY2022 (Jun '22) | $201.1M | $3,582M | **5.6%** |
| FY2023 (Jun '23) | $187.3M | $2,800M | **6.7%** |
| FY2024 (Jun '24) | $163.7M | $2,701M | **6.1%** |
| FY2025 (Jun '25) | $150.7M | $2,491M | **6.0%** |

**Key insight:** Even during Peloton's hypergrowth (FY2021, +120% revenue growth), deferred revenue was only 4.1% of TTM revenue. For a declining business (FY2025), it's 6.0%.

**Applied to WHOOP:** If WHOOP's deferred revenue is 5-8% of recognized revenue (higher than Peloton due to annual-plan-heavy mix and faster growth), and we estimate recognized revenue of $700M, deferred balance would be ~$35M-$56M. The **net change** (build-up from growth) would be ~$50M-$100M.

**This is much smaller than our original $280M-$350M estimate.** The earlier reconciliation overestimated steady-state deferred balance by conflating it with the net change. Peloton's data calibrates this down significantly.

### Peer Calibration: Oura's Revenue vs. Bookings

Oura provides a powerful calibration point:
- **$1B in 2025 "sales"** (Oura CEO's language)
- **Revenue mix: ~80% hardware / ~20% subscription**
- Oura uses "revenue" or "sales" language, NOT "bookings"
- $11B valuation / $1B revenue = **11x revenue**

Oura appears to report recognized revenue, not bookings. With an 80/20 hardware/subscription mix, most revenue is recognized at point of sale (hardware delivery), minimizing the bookings-to-revenue gap. Oura's business is much more hardware-heavy than WHOOP's.

**Implication:** If WHOOP used similar reporting, its revenue would likely be closer to the $1.1B. The fact that Ahmed explicitly chose "bookings" suggests there IS a meaningful gap — otherwise he would have said "revenue."

### Typical Bookings-to-Revenue Ratios

For subscription businesses under ASC 606:

| Business Type | Typical Bookings/Revenue Ratio | Why |
|---|---|---|
| Monthly SaaS (pay-as-you-go) | 1.0x-1.05x | Revenue nearly equals bookings |
| Annual SaaS (paid upfront) | 1.1x-1.3x | Deferred revenue creates modest gap |
| Multi-year SaaS contracts | 1.5x-3.0x | Large deferred balance |
| Hardware + annual subscription | 1.1x-1.4x | Hardware recognized at delivery; subscription ratably |
| Fast-growing annual subscription (>100% growth) | 1.2x-1.6x | Growth compounds the deferred build-up |

**WHOOP's profile:** Hardware + annual subscription + fast growth = **1.2x-1.5x bookings-to-revenue ratio** is most defensible.

---

## 5. Stress-Tested Revenue Range

### Approach: Three Independent Methods, Then Triangulate

#### Method A: Top-Down from Bookings

| | Low | Base | High |
|---|---|---|---|
| Cumulative 2025 bookings (not run-rate) | $700M | $800M | $900M |
| Bookings-to-revenue ratio | 1.4x | 1.3x | 1.15x |
| **Implied recognized revenue** | **$500M** | **$615M** | **$783M** |

**Assumptions:**
- Low: Bookings ramped sharply in H2 (S-curve), most subscribers on annual plans with large deferred buildup
- Base: Linear ramp, ~60% annual plan mix
- High: Monthly-heavy plan mix, hardware recognized at delivery, minimal deferral

#### Method B: Bottom-Up from Members x ARPU

| | Low | Base | High |
|---|---|---|---|
| Active members | 2.0M | 2.3M | 2.5M |
| Subscription ARPU | $239 | $262 | $303 |
| Subscription revenue | $478M | $603M | $758M |
| Hardware revenue (new members x ASP) | $30M | $50M | $70M |
| Advanced Labs | $15M | $30M | $50M |
| Accessories | $20M | $37M | $50M |
| B2B / Unite | $30M | $60M | $100M |
| **Total recognized revenue** | **$573M** | **$780M** | **$1,028M** |

**Assumptions:**
- Low: 2.0M active (Weinbach estimate + buffer); value-heavy tier mix
- Base: 2.3M active (small haircut from 2.5M for paused/grace period); mid-market tier mix
- High: 2.5M all active; premium tier mix; strong Labs and B2B

#### Method C: Calibrate Against Known Data Points

| Data Point | What It Implies for 2025 Revenue |
|---|---|
| Pitchbook 2024 revenue: $200M | At 103% growth, 2025 = ~$406M. BUT 103% is bookings growth, not revenue growth. Revenue growth could be 150-250% if 2024 was depressed by pre-5.0 timing. Implies $400M-$600M. |
| 36Kr investor estimate: >$500M | Floor of $500M from an investor source. Plausible that investor had Q3 2025 data and extrapolated conservatively. |
| Getlatka $260M (if CY2024) | At 2x growth (below 103% bookings growth): $520M. At 2.5x growth: $650M. |
| Oura at $1B revenue on $11B = 11x | WHOOP at same 11x multiple on $10.1B = ~$918M revenue. |
| Pitchbook 9.18x multiple on $1.1B | Pitchbook is using $1.1B as the revenue denominator (= bookings). |

### Triangulation

| Method | Low | Base | High |
|---|---|---|---|
| A: Top-down from bookings | $500M | $615M | $783M |
| B: Bottom-up from members | $573M | $780M | $1,028M |
| C: Data point calibration | $400M-$500M | $520M-$650M | $780M-$918M |
| **Triangulated range** | **$500M-$550M** | **$615M-$725M** | **$800M-$950M** |

### Revised Scenarios

| Scenario | 2025 Recognized Revenue | Probability | Key Driver |
|---|---|---|---|
| **Bear** | $500M-$600M | 25% | Bookings-to-revenue ratio closer to 1.4x; active members closer to 2.0M; annual plan heavy mix creates large deferred balance; 36Kr investor was citing a conservative floor |
| **Base** | $600M-$750M | 50% | Bookings-to-revenue ratio of 1.2x-1.3x; 2.3M active members; moderate deferred revenue; consistent with 36Kr ">$500M" + growth through H2 |
| **Bull** | $750M-$950M | 25% | Bookings nearly equal revenue (monthly-plan-heavy mix); 2.5M all active; strong B2B and Labs; Oura comp calibration supports ~$900M |

**Probability-weighted point estimate:** $650M (= 0.25 x $550M + 0.50 x $675M + 0.25 x $850M)

### Comparison to Original Estimate

The original reconciliation estimated $650M-$800M with a base case of $725M. This stress test **modestly lowers** the base case:

| | Original | Stress-Tested | Change |
|---|---|---|---|
| Low | $500M | $500M | Unchanged |
| Base | $725M | $650M | **-$75M (-10%)** |
| High | $1,000M | $950M | -$50M |

**Why lower:** The Peloton deferred revenue calibration (4-6% of revenue, not our original ~40%) and the annualization effect analysis both suggest cumulative 2025 bookings were closer to $750M-$850M, not $1.1B. Combined with a 1.2x-1.3x bookings-to-revenue ratio, revenue is more likely $600M-$700M than $700M-$800M.

---

## 6. Implied Multiples Table

### At Each Revenue Scenario

| Revenue Basis | Value | EV/Revenue at $10.1B | Interpretation | Comp Reference |
|---|---|---|---|---|
| **Bookings run-rate** | $1,100M | **9.2x** | What investors signed up for | Oura at ~11x revenue |
| **Bull recognized revenue** | $850M | **11.9x** | Premium but within health-data range | iRhythm at ~10-12x |
| **Revised base recognized** | $650M | **15.5x** | Rich; requires growth premium justification | Dexcom at ~8-10x (but 20% growth) |
| **Original base** | $725M | **13.9x** | Moderately rich | Between Bucket 2 and Bucket 3 |
| **Bear recognized revenue** | $550M | **18.4x** | Very aggressive; hard to justify on comps | Above all health-data comps |
| **Forward 2026 recognized** | $1,100M-$1,400M | **7.2x-9.2x** | Reasonable forward multiple | Squarely in Bucket 3 range |
| **Getlatka $260M (stale)** | $260M | **38.8x** | Absurd; confirms this is NOT 2025 revenue | N/A |

### Sensitivity: Implied Multiple by Revenue and Valuation

| | $8B Val | $10.1B Val | $12B Val |
|---|---|---|---|
| $500M rev | 16.0x | 20.2x | 24.0x |
| $600M rev | 13.3x | 16.8x | 20.0x |
| $650M rev | 12.3x | 15.5x | 18.5x |
| $725M rev | 11.0x | 13.9x | 16.6x |
| $850M rev | 9.4x | 11.9x | 14.1x |
| $1,000M rev | 8.0x | 10.1x | 12.0x |
| $1,100M rev | 7.3x | 9.2x | 10.9x |

---

## 7. The Pitchbook Revenue Label Problem

Pitchbook labels WHOOP's 2025 TTM as "$1.1B Total Revenue" and derives a 9.18x deal multiple. This raises a critical question: **is Pitchbook treating bookings as revenue?**

### How Pitchbook Sources Private Company Revenue

Per Pitchbook's own methodology disclosure:
- Data comes from "public and self-reported data"
- Sources include "survey requests, regulatory filings, FOIA responses"
- Machine learning and web scraping supplement primary research
- Profiles are "regularly updated" with "comprehensive review of publicly available sources"

**Assessment:** For a private company like WHOOP, Pitchbook almost certainly received the $1.1B figure from WHOOP's fundraising materials or press release. WHOOP reported "$1.1B bookings run-rate." Pitchbook likely placed this in the "Total Revenue" field because it is the most prominent financial metric reported. Pitchbook's 9.18x multiple is calculated on this basis.

**Risk:** If Pitchbook's "Total Revenue" = bookings, the 9.18x multiple is a bookings multiple, not a revenue multiple. The true trailing revenue multiple is higher (13.9x-15.5x).

**Mitigation:** Series G investors likely understood this distinction. The 9.18x is the multiple investors actually paid, regardless of whether the denominator is GAAP revenue or bookings.

---

## 8. Verdict: Which Revenue Figure to Use as Model Anchor

### For Comp Analysis (denominator in EV/Revenue)

**Use recognized revenue, NOT bookings.** All public comps (Dexcom, iRhythm, Garmin, Peloton, Spotify) report GAAP revenue. Using WHOOP's bookings as the denominator would understate the implied multiple relative to comps.

**Recommended anchor: $650M** (revised base case, down from $725M)

**Rationale:**
1. The Peloton deferred revenue calibration (4-6% of revenue) suggests lower deferred build-up than originally modeled
2. The annualization effect is significant — cumulative 2025 bookings are ~$750M-$850M, not $1.1B
3. A 1.25x bookings-to-revenue ratio on $800M cumulative bookings = $640M
4. The 36Kr investor estimate of ">$500M" is a floor, not a ceiling
5. Bottom-up member x ARPU analysis supports $600M-$780M

### For the IC Memo Conclusion

The revenue uncertainty changes the framing:

| If Revenue Is... | Multiple Is... | IC Memo Framing |
|---|---|---|
| $500M-$600M | 17x-20x | **Overvalued.** Very hard to justify on comps even with 103% growth. Real-options layer is essential AND must be large. Requires Bucket 3 weighting >70%. |
| $600M-$750M | 13.5x-17x | **Richly valued but defensible.** Premium justified by growth, subscription quality, and healthcare optionality. Base + real options can bridge to $10.1B. |
| $750M-$950M | 10.6x-13.5x | **Fairly valued.** In line with Oura (~11x) and within Bucket 3 range. Series G mark is reasonable on fundamentals. |

**At the revised $650M base case, the trailing multiple is ~15.5x.** This is expensive but not irrational for a business growing 100%+ with high subscription mix and cash flow positive. The key question becomes whether Series G investors priced the company on trailing revenue (~15.5x) or forward 2026 revenue (~7-9x on projected $1.1B-$1.4B).

**Most likely investor framing:** Series G investors priced WHOOP at **8-10x forward 2026 revenue**, not 15x trailing. This is consistent with:
- Oura at 11x trailing (but Oura's growth is decelerating)
- Dexcom at 8-10x (but 20% growth vs. WHOOP's 100%+)
- Health data platform multiples of 6-12x

---

## 9. Key Assumptions and Confidence Levels

| # | Assumption | Value | Confidence | Impact if Wrong |
|---|---|---|---|---|
| 1 | $260M Getlatka is CY2024 data | CY2024 | High | If it's actually H1 2025, base revenue is higher ($700M+) |
| 2 | $1.1B is bookings run-rate, not ARR | Bookings | High | If it's truly ARR (subscription-only), revenue is much higher |
| 3 | 2.5M = active paying members | Active | Medium | If only 2.0M active, revenue drops ~$130M |
| 4 | Bookings-to-revenue ratio: 1.2x-1.3x | 1.25x | Medium | At 1.5x, revenue is $533M; at 1.1x, revenue is $727M |
| 5 | Annual plan mix: ~60% | 60% | Low | Higher annual % = more deferred = lower recognized revenue |
| 6 | Subscription ARPU: $262 | $262 | Medium | +-$40 ARPU = +-$100M revenue |
| 7 | B2B is ~7-8% of revenue | ~$60M | Low | If B2B is truly 20% (Sacra), revenue could be $100M+ higher |

---

## 10. Open Questions That Would Resolve the Uncertainty

1. **Does WHOOP report GAAP revenue in its fundraising materials?** Series G investors received audited or management-prepared financials. The recognized revenue figure exists — we just don't have it.
2. **What is the annual vs. monthly plan mix?** This directly determines the deferred revenue balance and thus the bookings-to-revenue gap.
3. **Is the 103% growth metric on bookings, revenue, or both?** If revenue also grew 103% from a $200M base, 2025 revenue = $406M. If from a higher CY2024 base, it's higher.
4. **What is the exact active subscriber count?** If we could confirm 2.5M as active paying, the bottom-up build becomes much tighter.
5. **What does the Sacra equity research PDF contain?** This Dec 2025 report likely has the most detailed third-party revenue analysis. It could resolve the question directly.

---

## Appendix A: Source Quality Assessment

| Source | Revenue Figure | Quality | Bias |
|---|---|---|---|
| TechCrunch (CEO interview) | $1.1B bookings run-rate | **Gold standard** — primary source, direct quote | Upward (CEO chooses most flattering metric) |
| Pitchbook | $1.1B "Total Revenue" | **High** but mislabeled — likely bookings in revenue field | Upward (mirrors company-reported) |
| 36Kr / Hard Krypton | >$500M (investor) | **Medium** — secondhand investor estimate | Conservative (investor being cautious) |
| SaveDelete | $1B ARR | **Low** — secondary interpretation of press | Upward (misinterprets bookings as ARR) |
| CB Insights | $1.1B (2025) | **Medium** — mirrors Pitchbook | Same caveat as Pitchbook |
| Getlatka | $260M | **Medium** — likely stale | Stale (CY2024 data) |
| Growjo | Not specific | **Low** — algorithmic estimate | Unknown |
| Bottom-up model | $573M-$1,028M | **Medium** — analytical estimate | Depends on assumptions |

## Appendix B: Oura as Revenue Calibration

Oura provides the most important calibration point because it is the nearest business model comp:

| Metric | Oura | WHOOP | Implication |
|---|---|---|---|
| 2025 revenue | $1.0B (confirmed) | $650M (est.) | Oura revenue is higher |
| Revenue language | "Sales" / "revenue" | "Bookings run-rate" | Oura reports recognized revenue; WHOOP does not |
| Revenue mix | 80% hardware / 20% subscription | ~15% hardware / 85% subscription | Oura's hardware-heavy mix means most revenue recognized at delivery |
| Valuation | $11.0B | $10.1B | Oura valued higher |
| EV/Revenue | 11.0x | 15.5x (on $650M est.) or 9.2x (on $1.1B bookings) | WHOOP more expensive on recognized revenue basis |
| Members / units | 5.5M rings sold; ~3M active subscribers (est.) | 2.5M members | Oura has larger installed base |

**Key insight:** Oura confidently uses "revenue" and "sales" language for its $1B figure. WHOOP deliberately uses "bookings." If WHOOP's recognized revenue were close to $1.1B, Ahmed would have said "revenue." The choice of "bookings" is informative — it strongly suggests recognized revenue is meaningfully lower than $1.1B.

---

*Last updated: April 16, 2026*

## Sources

- [TechCrunch — Whoop's valuation just tripled to $10 billion](https://techcrunch.com/2026/03/31/whoop-valuation-10b-series-g-fundraise/)
- [Getlatka — WHOOP](https://getlatka.com/companies/whoop.com)
- [36Kr / Hard Krypton — WHOOP Analysis](https://eu.36kr.com/en/p/3537536486907017)
- [SaveDelete — Whoop Raises $575M at $10.1B Valuation, Hits $1B ARR](https://savedelete.com/article/whoop-575m-10-billion-valuation-1b-arr/)
- [CB Insights — WHOOP Financials](https://www.cbinsights.com/company/bobo-analytics/financials)
- [Founded — WHOOP hits $10B valuation](https://www.founded.com/whoop-10b-valuation-series-g-funding/)
- [Sacra — WHOOP](https://sacra.com/c/whoop/)
- [Pitchbook — WHOOP](https://pitchbook.com/profiles/company/64325-80)
- [StockAnalysis — Peloton Balance Sheet](https://stockanalysis.com/stocks/pton/financials/balance-sheet/)
- [Morningstar — How PitchBook Gets Private Company Data](https://shareholders.morningstar.com/investor-relations/investor-qa/investor-qa-details/2020/How-does-PitchBook-get-the-data-on-private-companies-Does-any-of-the-data-come-from-the-investors-or-companies-themselves/default.aspx)
- [PitchBook — How PitchBook Collects Data](https://pitchbook.com/research-process)
- [CNBC — Oura $11B Valuation](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html)
- [CNBC — Oura Close to $2B in 2026 Sales](https://www.cnbc.com/2025/11/11/smart-ring-maker-oura-expects-close-to-2-billion-in-2026-sales-ceo.html)
- [BusinessWire — Oura Surpasses 5.5M Rings Sold](https://www.businesswire.com/news/home/20250922351288/en/URA-Surpasses-5.5-Million-Rings-Sold-and-Doubles-Revenue-for-the-Second-Year-in-a-Row-Empowering-Millions-to-Live-Better-Longer)
- [GuruFocus — WHOOP $575M at $10.1B](https://www.gurufocus.com/news/8762250/whoop-raises-575-million-at-101-billion-valuation-reports-103-growth)
- [Max Weinbach on X — WHOOP Active Members Estimate](https://x.com/MaxWinebach/status/1920632920827416582)
