# WHOOP Valuation — Master Assumption Inventory & Research Methodology

**Date:** April 16, 2026
**Status:** Design spec — approved, ready for research execution
**Scope:** 115 assumptions across 7 categories feeding 5 valuation methods

---

## Overview

This document defines every major assumption required to produce a triangulated private-company valuation of WHOOP Inc. against its March 2026 Series G mark of $10.1B. Assumptions are organized by category (not by valuation method) to surface shared dependencies and prevent redundant sourcing.

### Architecture

- **Valuation methods:** Intrinsic DCF, Trading Comps (3-bucket), Precedent Transactions, Last-Round Implied, Implied IPO Trading Range
- **DCF structure:** 7-year explicit forecast (2026-2033) + terminal, three phases (pre-IPO hypergrowth, post-IPO deceleration, scaling maturity), cross-checked with 5-year exit-multiple method
- **Real options:** Layered separately, never embedded in DCF base case
- **Revenue anchor:** $1.1B run-rate (given), with plan to build bottom-up bridge later
- **Sourcing standard:** Tier 1 (filings/official) preferred; fall back to Tier 2 (credible press/analyst) or Tier 3 (model inference/triangulation) with explicit tier labels

### Sourcing Stack

| Priority | Source | Access Method |
|---|---|---|
| 1 | Pitchbook (WHOOP, Oura, comps) | Playwright browser automation → open Chrome tab |
| 2 | SEC EDGAR (Peloton, Dexcom, Garmin 10-Ks) | Web search / direct access |
| 3 | Press & analyst reports (Sacra, Getlatka, TechCrunch, Bloomberg) | Web search |
| 4 | Public company filings (all comps) | SEC EDGAR / investor relations pages |
| 5 | Secondary market data (Forge, EquityZen) | Web search |
| 6 | Academic/reference (Damodaran, Kroll) | Web access |
| 7 | MCP financial APIs (S&P, FactSet, etc.) | Stretch goal — test as available |

### Methodological Exclusion: Take-Private LBO

Take-private LBO is deliberately excluded from the football field. Three 
structural reasons:

1. **Capital structure is wrong for LBO.** WHOOP is all VC preferred with
   minimal debt capacity. Leverage cannot be applied to a cash-flow-positive
   growth business at the scale LBO economics require (5-7x EBITDA).
2. **IPO path is locked in.** Series G included sovereign wealth 
   (QIA, Mubadala) and crossover investors. These parties require public-
   market liquidity, not another private hold period.
3. **Strategic acquirers are partially foreclosed.** Abbott chose investor
   path rather than acquirer path. Apple/Google face antitrust friction in
   wearables M&A at this scale.

Strategic acquisition (distinct from LBO) IS captured via precedent 
transactions and remains a non-zero-probability tail scenario.

### Summary Statistics

| Category | Assumptions | Critical | Unsourced | Locked |
|---|---|---|---|---|
| Section 1: Revenue & Growth | 19 | 7 | 6 | 2 |
| Section 2: Cost Structure & Margins | 17 | 7 | 6 | 1 |
| Section 3: Capital Structure & Cap Table | 17 | 5 | 10 | 0 |
| Section 4: Comparable Companies | 19 | 8 | 4 | 0 |
| Section 4B: IPO Trading Range | 6 | 2 | 2 | 0 |
| Section 5: DCF Mechanics | 29 | 12 | 3 | 0 |
| Section 6: Precedent Transactions | 8 | 1 | 1 | 4 |
| **Total** | **115** | **42 Critical** | **32 Unsourced** | **7 Locked** |

---

## Section 1: Revenue & Growth Assumptions

**Feeds:** DCF, Comps (growth-adjusted multiples), IPO back-solve, Last-round validation

| # | Assumption | Base Case | Priority | Methods | Best Source | Fallback Source | Status |
|---|---|---|---|---|---|---|---|
| R1 | 2025 revenue run-rate | $1.1B (given) | Critical | All 5 | CEO statement / Series G press | — | **Locked** |
| R2 | 2025 recognized revenue | $260M | High | DCF, Comps | Getlatka, press reports | Triangulate from R1 | Tier 2 |
| R3 | Paying members (current) | 2.5M+ | Critical | DCF build-up | Series G press release | Pitchbook | Tier 1 |
| R4 | Effective ARPU | **REVISED v2: $300/$338/$375 blended (5-component build)** | Critical | DCF build-up | Bottom-up tier × payment mix | Subscription pricing page | Tier 3 — see v2 build below |
| R5 | Subscription revenue % | ~85% | High | DCF, Comps | Business model analysis, press | Sacra equity research | Tier 2 |
| R6 | YoY subscription growth | 103% (2025) | Critical | DCF Phase 1, Comps | Series G press release | — | **Locked** |
| R7 | Growth deceleration curve (Phase 1-2-3) | TBD | Critical | DCF | Peer trajectories post-IPO (Peloton, Dexcom, Netflix) | Sell-side growth decay models | **Unsourced** |
| R8 | Non-subscription revenue mix | ~15% (accessories, Labs, Unite) | Medium | DCF | Press, product pricing page | Estimate from total minus sub | Tier 3 |
| R9 | International vs. domestic split | Heavily US-weighted, 56 countries | High | DCF, Real Options | Pitchbook, press | Peer int'l revenue splits | **Unsourced** |
| R10 | B2B/Unite revenue contribution | Unknown | Medium | DCF, Real Options | Pitchbook | Press mentions only | **Unsourced** |
| R11 | Churn rate by cohort (year 1, 2, 3+) | **REVISED v2: cohort-aged curve required, NOT flat annual.** Months 1-3: 4-5%/mo; Months 4-12: 2-2.5%/mo; Year 2: 1.5-2%/mo; Year 3+: 1-1.5%/mo. Blended annual is endogenous output. | **Critical** | DCF, Comps (quality adj) | Pitchbook tearsheet, S-1 when filed | Peer churn curves (Peloton S-1, Oura estimates) | **Unsourced — top priority; flat-annual implementation in current model is broken, see v2 directives below** |
| R12 | Gross adds vs. net adds | Unknown | **Critical** | DCF member build | Pitchbook, press on member milestones | Back-solve: 2.5M members + 103% growth → implied gross adds | **Unsourced** |
| R13 | Pricing tier mix (Core/Peak/Life) & trajectory | Est. 30/50/20 split → blended ~$265 sub-only | High | DCF (ARPU build), revenue bridge | WHOOP pricing page (current), press | Survey data, app store reviews | Tier 2 partial |
| R14 | Attach rates on premium products (Labs, BP, Healthspan) | Unknown — linchpin for bucket-3 weighting | **Critical for bucket-3** | Comps weighting, DCF, Real Options | Pitchbook, press on Labs uptake | Labs pricing ($199-$599) x estimated adoption | **Unsourced** |
| R15 | Annual price inflation | Historical pricing changes | Medium | DCF years 2-7 | Web Archive of WHOOP pricing page | CPI + premium brand pricing power | Tier 3 |
| R16 | TAM capture ceiling by geography | Market research data in brief ($31.4B wearables, $84.9B fitness trackers) | High (bounds Phase 3) | DCF terminal, Real Options | GlobeNewsWire, Towards Healthcare | Peer penetration rates by market | Tier 2 |
| R17 | Hardware upgrade cycle / refresh revenue | WHOOP 4.0-5.0 cycle ~2 years | Low | DCF (minor) | Product launch history | Peer device refresh cadence | Tier 2 |
| R18 | Deferred revenue / recognition mechanics | Prepaid subs recognized ratably under ASC 606 | Medium (accounting) | DCF, revenue bridge | S-1 when filed | ASC 606 standard treatment | Tier 3 |
| R19 | Non-subscription ARPU decomposition | $175/member gap between R4 ($440) and subscription-only math (~$265). Three candidate decompositions modeled (see below) | **Critical for bucket-3** | DCF (revenue mix), Comps (bucket weighting), Real Options (D19, D21) | Pitchbook, Labs pricing, press on Labs uptake | **Unsourced — load-bearing** |

### Key Dependencies
- R11 (churn) is the single highest-value Pitchbook scrape target
- R14 (attach rates) is unsourceable now but determines whether WHOOP deserves bucket-3 weighting — build as sensitivity rather than point estimate
- R4 (effective ARPU of ~$440) vs. bottom-up subscription math (~$265) creates a ~$175/member gap — decomposed in R19 below

### v2 ARPU Build (replaces single non-sub lump in current model)

| Component | $/member/yr (range) | Confidence | Basis |
|---|---|---|---|
| Base subscription (Core ~$239, weighted for monthly payers paying more) | $255-270 | Medium | Pricing page + plan mix estimate |
| Tier premium (Peak/Life upgrade above Core) | $15-30 | **Low** | Est. 30% on higher tiers, $50-100 premium |
| Accessories/straps | $20-35 | **Low** | Product catalog, estimated replacement cycle |
| Advanced Labs (attach rate × avg test price) | $10-30 | **Very low** | 5-10% attach × $200-400 avg |
| Other (WHOOP Coach included in sub, Unite B2B not per-consumer) | $0-10 | **Very low** | Marginal |
| **Blended ARPU** | **$300-375** | | Sum of above; bear $300 / base $338 / bull $375 |

**Critical model directive:** ARPU applies to AVERAGE members during the period (~2.25M for 2025), NOT year-end (2.5M). Apply 2.5M × $302 mistake produces a $100M phantom revenue gap. The internal consistency check R3_avg × R4 ≈ R1 must pass.

### v2 Churn Architecture (replaces flat annual rate in current model)

The current implementation uses a single annual churn rate (22 / 17 / 12%) per scenario. This is **structurally wrong** for a hypergrowth subscription business because:

1. New cohorts churn 3-5x faster than year-3+ cohorts (well-established subscription benchmark — Peloton S-1, Strava S-1, Spotify pre-IPO disclosures)
2. WHOOP's forecast adds ~2M new members in 2026-27, meaning year-1 cohorts dominate the base
3. Blended annual churn must therefore RISE during hypergrowth and stabilize as the cohort mix matures — flat-annual misses this dynamic entirely

**Required architecture:**
- Track cohort vintages (year of acquisition) separately
- Apply tenure-based monthly churn curve:

| Tenure | Monthly Churn (est.) | Cumulative Retention | Rationale |
|---|---|---|---|
| Month 1-3 | 4.0-5.0% | 86-88% (3-mo) | New member trial period; highest drop-off |
| Month 4-12 | 2.0-2.5% | 70-75% (12-mo) | Habit formation; seasonal attrition |
| Year 2 | 1.5-2.0% | 58-65% (24-mo) | Committed users, data lock-in |
| Year 3+ | 1.0-1.5% | 50-58% (36-mo) | Power users; very sticky |

- Blended annual churn = endogenous output, not input

**Bear/base/bull anchors:**
- Bull: WHOOP marketing claim holds (>85% 12-mo retention); Y3+ at 1.0%/mo
- Base: Sacra envelope (80-85% 12-mo retention); Y3+ at 1.25%/mo
- Bear: Peloton trajectory overlay (deteriorates from 0.73% → 1.8%/mo over 4 years)

**Note on the "<3% monthly Pro tier" data point:** This is a premium-tier statistic, not blended. Premium tiers always retain better than base. Blended monthly is plausibly 3-4%, not the 1.5% the current bull case implies. Stress-test accordingly.

### v2 Internal Consistency Check (must pass in rebuilt model)

R3_avg × R4 ≈ R1 within ±5%. One of {R1, R3_avg, R4} must be derived, not three independent inputs. The current model has all three as independent and fails this check by ~$100M.

### R19 Decomposition Candidates

| Candidate | Accessories | Labs | Plan Mix | Bucket-3 Implication |
|---|---|---|---|---|
| R19a — Accessories-heavy | $100 | $40 | $35 | Bucket 2 bias; WHOOP is a subscription-merch business |
| R19b — Labs-heavy | $40 | $110 | $25 | Strong bucket 3 bias; healthcare platform thesis validated |
| R19c — Plan-mix heavy | $50 | $50 | $75 | Neutral; tier upgrades driving ARPU, mixed thesis |

**The correct decomposition is a research target.** Until sourced, model 
all three as sensitivity scenarios. The choice directly affects bucket-3 
weighting (V11) and therefore the football field multiple range.

---

## Section 2: Cost Structure & Margins

**Feeds:** DCF (FCF build), Comps (margin-adjusted multiples), IPO back-solve (profitability story)

### Structural Design Decision

**GAAP gross margin vs. unit-economics gross margin must be modeled separately.** The hardware subsidy creates a deferred cost pattern that makes year-1 contribution margin negative even though the business is cash flow positive overall. Reported gross margin improves mechanically as growth decelerates (subsidy/recognition mismatch resolves), independent of real operating leverage. This is the same accounting dynamic that distorted Peloton's reported margins.

**Model architecture:**
1. Subscription gross margin separately from hardware gross margin
2. Hardware cost treated as customer acquisition cost for unit-economics view, as COGS for GAAP view
3. Both views computed; divergence during growth is expected and informative

### SBC Treatment (Locked Design Decision)

**SBC is included as a real cash cost in the DCF.** Excluding SBC from FCF while using current share count double-counts — it inflates FCF and deflates per-share value, and those errors don't cancel. Share dilution modeled separately for per-share equity value.

### Assumption Table

| # | Assumption | Prior Estimate | Priority | Methods | Source Plan | Status |
|---|---|---|---|---|---|---|
| C1 | Hardware BOM per device | $70-120 | Critical | DCF | Teardown analyses (Oura ~$50, Apple Watch higher; WHOOP 5.0 has HR, temp, SpO2, accelerometer, ECG) | Tier 3 |
| C2 | Loaded hardware cost (assembly, ship, warranty, returns) | $100-150 per member at acquisition | Critical | DCF, unit economics | Back-solve from C1 + logistics benchmarks | Tier 3 |
| C3 | GAAP treatment: hardware as COGS vs. CAC | **Model both views** | Structural | DCF | S-1 accounting policy; ASC 606 | **Design decision — locked** |
| C4 | Subscription delivery cost (infra, support) | 8-15% of sub rev, declining to 8% at scale | High | DCF | AWS/GCP benchmarks, peer SaaS margins | Tier 3 |
| C5 | Subscription gross margin (standalone) | 75-85% at steady state | Critical | DCF | Peer: pure SaaS ~80%, Dexcom ~64% | Tier 3 |

**C5 rationale:** WHOOP subscription margin is structurally higher than 
Dexcom's because Dexcom's "subscription" revenue includes consumable 
sensor replacements (recurring hardware COGS), while WHOOP's subscription 
is pure software/data delivery with hardware treated as a separate 
one-time cost at acquisition. This is also why WHOOP's trading multiple 
is not directly comparable to Dexcom's at face value — WHOOP's recurring 
revenue is arguably higher quality (pure software margins), which 
supports a premium within the growth-adjusted framework.

| C6 | Hardware gross margin (standalone) | Negative to low-single-digits (subsidized) | Critical | DCF | Peloton hardware GM trajectory | Tier 3 |
| C7 | Blended reported GM by phase | Phase 1: 58-62%, Phase 2: 63-70%, Phase 3: 70-76%, Terminal: 75-78% | Critical | DCF | Derived from C5+C6+growth rate | Tier 3 |
| C8 | R&D as % of revenue | 20-25% today, declining to 12-15% at steady state | High | DCF | Pitchbook; peers: Dexcom 13-15%, Garmin 10-12%, growth SaaS 20-30% | **Unsourced** |
| C9a | S&M: Paid CAC per gross add | $130-220 (30-50% of first-year ARPU) | **Critical** | DCF, unit economics | Peer DTC CAC benchmarks | **Unsourced** |
| C9b | S&M: Athlete partnerships / brand | $30-100M/yr | High | DCF | Press, endorsement deal reporting | **Unsourced** |
| C9c | S&M total as % of revenue | 25-35% today, declining to 15-20% at steady state | **Critical** | DCF | **Peloton 10-K series 2019-2025 — priority research** | **Unsourced** |
| C10 | G&A as % of revenue | 12-18% today, 8-12% at steady state; IPO step-up of 200-300bps in 2027-2028 (SOX, IR, legal) | Medium | DCF | Peer pre/post-IPO G&A trajectories | Tier 3 |
| C11 | SBC as % of revenue | 12-18% today, normalizing to 6-10% post-IPO | High | DCF | Peer pre-IPO SBC intensity | **Unsourced** |
| C12 | SBC treatment in model | Real cost in FCF; dilution modeled separately | Structural | DCF | — | **Locked** |
| C13 | CapEx as % of revenue | 3-5% today, 2-4% at steady state (contract-mfg, asset-light) | Medium | DCF | Pitchbook | Tier 3 |
| C14 | Deferred revenue (working capital benefit) | Positive during growth (prepaid subs), reverses at deceleration | High | DCF | ASC 606, peer deferred rev balances | Tier 3 |
| C15 | Inventory balance / cash drag | $50-100M, grows with member adds | Medium | DCF | Peer inventory/revenue ratios | Tier 3 |
| C16 | Net working capital as % of incremental revenue | -5% to -10% (benefit from deferred rev > inventory drag) | High | DCF | Derived from C14+C15 | Tier 3 |
| C17 | Advanced Labs COGS | Quest/Labcorp margins ~30-40% on panels | High (bucket-3) | DCF, Comps weighting | Lab services pricing benchmarks | Tier 3 |

### Phase P&L Priors

| Line Item | Phase 1 (2026-2027) | Phase 2 (2028-2030) | Phase 3 (2031-2033) | Terminal (2034+) |
|---|---|---|---|---|
| Gross Margin (blended) | 58-62% | 63-70% | 70-76% | 75-78% |
| R&D | 22% | 18% | 14% | 13% |
| S&M | 30% | 22% | 18% | 16% |
| G&A | 15% | 12% | 10% | 9% |
| SBC (embedded) | 15% | 10% | 8% | 7% |
| EBITDA Margin | 0-5% | 10-18% | 20-28% | 28-32% |
| FCF Margin | 5-10% (WC benefit) | 12-22% | 20-26% | 25-28% |

### Unit Economics Validation Layer

These are derived from assumptions above, not independently sourced. They validate the top-down P&L:

| # | Metric | Derivation | Purpose |
|---|---|---|---|
| U1 | Year-1 contribution margin per new member | C1+C2 (hardware) + R4 (ARPU) - C4 (service cost) | Validate acquisition economics |
| U2 | Lifetime value by cohort vintage | R11 (churn) x R4 (ARPU) x C5 (sub margin) | Validate LTV:CAC claim (~4.5x) |
| U3 | Payback period on hardware subsidy | U1 / monthly contribution | Should be <6 months if model is healthy |
| U4 | Steady-state member economics (year 3+) | R4 - C4 (no hardware cost) | Shows mature unit profitability |

**Diagnostic test:** if the top-down model shows 25% EBITDA margins but the cohort model shows negative year-1 contribution margin with high churn, those can't both be true. The disagreement is the highest-leverage analytical work.

---

## Section 3: Capital Structure & Cap Table

**Feeds:** Last-round implied, IPO back-solve, DCF (equity value bridge), Precedent transactions (equity vs. enterprise value)

### Assumption Table

| # | Assumption | What We Know | Priority | Scenario Sensitivity | Source Plan | Status |
|---|---|---|---|---|---|---|
| S1 | Fully diluted shares outstanding | Unknown | **Critical** | All scenarios | Pitchbook cap table, S-1 | **Unsourced — Pitchbook priority** |
| S2 | Series A-G share prices & conversion ratios | G: $575M / $10.1B = ~5.7% dilution | **Critical** | All | Pitchbook round detail | Tier 2 partial |
| S3 | Liquidation preference stack (1x, participating, etc.) | ~$1.4B total raised; structure unknown | **Critical (bear)** | Dispositive below ~$6B exit | Pitchbook deal notes, S-1 | **Unsourced** |
| S4 | Total liquidation preference $ amount | Floor $1.4B if all 1x | High | Bear/distressed | Sum of rounds | Tier 2 |
| S5 | Participation rights | SoftBank historically takes participating; Series G lead likely forced cleanup | **High (bear)** | Below ~$6B | Pitchbook, SoftBank peer S-1s | **Unsourced** |
| S6 | Anti-dilution provisions | Likely weighted-average broad-based (standard) | Medium | Bear only | Pitchbook | **Unsourced** |
| S7 | Option pool size & strike prices | Typical 10-15% pre-IPO; 600-person hiring surge = aggressive granting | High | All (dilution) | Pitchbook, S-1 | **Unsourced** |
| S8 | Founder ownership (Ahmed) | **12-18% fully diluted** (7 rounds + pool refreshes over 14 years); possibly 8-12% with secondaries | Medium | Governance, alignment | Pitchbook, proxy | **Unsourced** |
| S9 | Common vs. preferred discount | Typical DLOM 20-35%; secondary pricing would narrow | High | Per-share value | 409A (future), Forge/EquityZen | **Unsourced** |
| S10 | Debt on balance sheet | Likely minimal/zero | Low | EV bridge | Pitchbook, press | Tier 2 |
| S11 | Cash post-Series G | $600-800M estimated (raise + operating cash) | Medium | EV bridge | Back-solve from raise + CFO+ status | Tier 3 |
| S12 | EV vs. equity value bridge | ~$9.3-9.5B EV implied | High | All methods | Derived from S10+S11 | Tier 3 |
| S13 | Recent 409A valuation | Unknown; unsourceable pre-S-1 | Medium | Per-share value | S-1, employee leaks (Blind/Glassdoor) | **Parked** |
| S14 | Secondary transactions / tender history | Unknown — would reveal common price signal + founder liquidity | **High** | Founder alignment, common pricing | Pitchbook, Forge/EquityZen, press | **Unsourced** |
| S15 | Series F ratchet / IPO adjustment provisions | Likely extinguished at Series G close (new lead would insist), but unconfirmed | **High (bear)** | Bear case waterfall only | SoftBank peer S-1s, Pitchbook deal notes | **Unsourced** |
| S16 | Dual-class share structure for IPO | Unknown — very common for founder-led tech IPOs (Meta, Snap, Airbnb) | High | Governance, control premium/discount | Pitchbook, S-1 | **Unsourced** |
| S17 | Financing activity 2022-2025 (gap period) | No announced rounds in 4 years — bull interpretation (didn't need capital) vs. bear (couldn't get up-round) | **High** | Validates or undermines Series G mark | Pitchbook (query extensions, converts, SAFEs specifically) | **Unsourced — Pitchbook priority** |

### Scenario Framing for Modeling Effort

| Scenario | Exit Range | Cap Structure Impact | Modeling Depth |
|---|---|---|---|
| **Bull / Base** | $10-20B+ IPO | Noise — all preferred converts, preferences don't bite | Simple: EV - debt + cash / FD shares |
| **Bear** | $3-6B exit | **Dispositive** — participating preferred, ratchets, and preferences materially reduce common value | Full waterfall required |
| **Distressed** | <$2B | Binary — preferences consume all proceeds, common approaches zero | Waterfall + option value = zero check |

### Waterfall Modeling Approach

Run waterfall at three exit scenarios ($5B bear, $10B base, $20B bull) with both:
- 1x non-participating (standard)
- 1x participating (SoftBank-style)

If the spread between participating and non-participating is <5% of common value at base case, the preference structure is noise. If >15%, flag as key uncertainty.

### Analytical Interpretation (for IC Memo)

**Series G syndicate composition as a valuation signal:** The absence of traditional growth-equity crossover investors (Tiger, Coatue, D1) and presence of sovereign wealth + healthcare strategics suggests WHOOP is deliberately constructing a healthcare-narrative IPO. Collaborative Fund as lead — an impact-oriented fund — signals the company negotiated from strength and chose investors who validate the long-duration health-platform thesis. This syndicate is evidence for higher bucket-3 weighting in the comps framework.

**The 4-year financing gap (2021-2026)** is consistent with the bull interpretation (achieved cash flow positive, didn't need capital) but cannot be confirmed without Pitchbook verification. If bridge/SAFE activity is discovered, the $10.1B mark should be interpreted with more skepticism as it may embed catch-up dilution.

---

## Section 4: Comparable Company Assumptions

**Feeds:** Trading comps (directly), DCF terminal value (exit multiple), IPO back-solve (expected trading range), Precedent transactions (M&A multiples)

### Final Comp Set

**Bucket 1 — Consumer Hardware**

| Comp | Ticker | Role |
|---|---|---|
| Garmin | GRMN | **Sole comp — hardware-only anchor** |
| Apple | AAPL | Reference only (not in blended calc) — wearables segment for TAM framing |

**Bucket 2 — Consumer Subscription Hybrid**

| Comp | Ticker | Role |
|---|---|---|
| Peloton | PTON | **Cautionary anchor — distressed end of range (~1.2x rev, observed Apr 2026)** |
| Spotify | SPOT | **Mature subscription — high end of range (~5.1x rev, observed Apr 2026; re-rated from ~3x post-profitability inflection)** |
| Oura | Private | **Highest-signal comp in universe — closest business model match** |
| Strava | Private | Reference if data available |

**Bucket 2 treatment: Disaggregated, not averaged.** Report Peloton and Spotify separately. The range (1.2x to 5.1x, observed Apr 2026) is the insight — where WHOOP falls within it signals market belief about execution quality. **Note:** Spotify's 5.1x exceeds original 3-4x framing; reflects post-profitability re-rating. For benchmarking pre-profit WHOOP, historical unprofitable-era Spotify multiples (2-3x) may be more appropriate.

**Bucket 3 — Health Data / Medical Device**

| Comp | Ticker | Role |
|---|---|---|
| Dexcom | DXCM | **Aspirational anchor** — CGM, subscription-like, FDA-regulated |
| ResMed | RMD | Structural parallel — connected device + software/data platform |
| Masimo | MASI | Sensor-relevant — pulse ox, consumer health pivot (W1 watch) |
| iRhythm | IRTC | **Cardiac wearable + SaaS** — closest to WHOOP's ECG ambitions |

### Comps Cut (with rationale for memo reference)

| Comp | Why Cut |
|---|---|
| GoPro (GPRO) | Action cameras, not wearables. Different TAM, customer base, failed subscription pivot. |
| Logitech (LOGI) | PC peripherals. Shares "consumer hardware" label but zero overlap in use case or growth profile. |
| Netflix (NFLX) | Mature content-driven subscription priced on content ROI, not hardware-sub economics. Same category error as using Apple for Garmin. Margin aspiration better captured in one sentence in risks section. |
| Insulet (PODD) | Insulin delivery (Omnipod) too specialized. Not a wearable health platform. |
| Abbott (ABT) | WHOOP investor, not peer. Too diversified (pharma, nutrition, diagnostics). Abbott Libre CGM is relevant as sub-segment reference only. |
| Fitbit | Acquired by Google at ~1.3x (distressed). Failed subscription story already captured by Peloton. |
| Under Armour / Lululemon | Apparel-adjacent, fundamentally different economics. |
| Boston Scientific / Medtronic | Too diversified and mature to inform pre-IPO growth company multiple. |

### Multiple Selection

| # | Assumption | Priority | Source | Status |
|---|---|---|---|---|
| V6 | Primary: EV/Revenue (NTM) | **Critical** | Public filings, financial data | **Sourced — see research/comp-trading-multiples-summary.md** |
| V7 | Secondary: EV/ARR | High | Derived from V6 + sub revenue % | Needs calc |
| V8 | Growth-adjusted: EV/Rev / YoY growth | **Critical — anchors the memo** | Derived | **Sourced — see trading multiples summary** |
| V9 | Rule of 40 score (growth + FCF margin) | High | Public filings | **Sourced — all 7 comps** |
| V10 | Observation date: trailing 30-day average | Medium | — | Design decision |
| V19 | **Multiple time variance: today, 6mo, 12mo, 3yr** | **High** | Historical pricing data | **Sourced — research/comp-historical-multiples-v19.md. Key finding: Dexcom compressed 60% (13.8x→5.0x) over 3yr; 2023 multiples support $10.1B, current multiples support ~$4.5B** |

**V19 implementation:** For Garmin, Peloton, and Dexcom, pull EV/Revenue at four time points. Report the range. If Q1 2026 was a local peak in health-tech multiples, the Series G looks rich vs. through-cycle. Half a page of analysis that adds real defensive rigor.

**Why EV/Revenue not EV/EBITDA:** WHOOP is pre-profit. Most comps in buckets 2-3 have thin or negative EBITDA during growth. EV/Revenue is the only multiple consistently computable across all three buckets.

### Bucket Weighting

| # | Assumption | Priority | Status |
|---|---|---|---|
| V11 | Bucket weighting scheme | **Critical — this IS the thesis** | Design decision |
| V12 | Weighting sensitivity range | **Critical** | Needs scenario build |
| V13 | Qualitative evidence for weighting | High | Partially sourced (Series G syndicate, FDA status, product mix) |

**The bucket weights are not free parameters. They are the thesis.** Each scheme makes a claim about what WHOOP is:

| Scenario | B1 (Hardware) | B2 (Subscription) | B3 (Health Data) | Thesis Implied | Blended Multiple (observed Apr 2026) | Blended Multiple (pre-research est.) |
|---|---|---|---|---|---|---|
| Bear | 40% | 40% | 20% | WHOOP is Peloton with better branding | **~4.6x revenue → $5.1B** | 2-4x revenue |
| Base | 20% | 40% | 40% | Subscription business with healthcare optionality | **~5.1x revenue → $5.6B** | 4-7x revenue |
| Bull | 10% | 30% | 60% | Health data platform that happens to use a wearable | **~5.4x revenue → $5.9B** | 6-9x revenue |
| Series G implied | ~5% | ~25% | ~70% | Market prices WHOOP as a health-data company | **~5.4x static; ~9.2x with growth premium** | ~9x revenue |

**Session 2 recalibration (April 16, 2026):** Observed multiples — B1: 6.7x (Garmin), B2: 1.2-5.1x (Peloton-Spotify), B3: 5.0-6.4x (median 5.8x). No static bucket weighting reaches $10.1B. The Series G mark requires a ~1.7x growth premium (WHOOP 103% growth vs. comps 10-26%) plus real-option value. Full analysis in `research/comp-trading-multiples-summary.md`.

### Dual Back-Solve (Key Analytical Move)

**Naive back-solve:** To hit 9x blended, Bucket 3 must weight 60-70%. Implication: market prices WHOOP as a healthcare company.

**Growth-adjusted back-solve:** If 2-3x of the 9x multiple is growth premium (WHOOP at 103% vs. comps at 10-25%), the underlying business-mix multiple is ~6x. To hit 6x, Bucket 3 weights only 30-40%. Implication: market prices WHOOP as a subscription business with growth premium; healthcare is still an open call option.

**Report both.** The gap between them is the central tension: does the $10.1B mark reflect what WHOOP *is* (healthcare platform) or what WHOOP *is doing* (growing 103%)?

### Three-Stage Discount Framework

Replaces simple DLOM/DLOC assumptions with a layered approach:

| Stage | Question Answered | Calculation | Estimated Range |
|---|---|---|---|
| **Stage 1: Public market fair value** | What would WHOOP trade at if public today? | Comp multiples x metrics, no discounts | Raw output |
| **Stage 2: IPO pricing** | What does the IPO price at? | Stage 1 x (1 - IPO discount) | 15-25% below Stage 1 |
| **Stage 3: Current private value** | What is WHOOP worth today, pre-IPO? | Stage 2 x (1 - illiquidity/timing discount) | 5-15% below Stage 2 |

**Series G investors' implicit belief:** If $10.1B is Stage 3, backing out discounts:
- Stage 2 (IPO price): ~$11.2B
- Stage 1 (public fair value): ~$13-15B

**$13-15B is the number the DCF and comps need to support or contest.** Not $10.1B — that's the discounted private mark.

### IPO Trading Range Assumptions (Numbered)

| # | Assumption | Base Case | Priority | Source | Status |
|---|---|---|---|---|---|
| I1 | IPO timing window | 12-18 months from Series G (Q2 2027 - Q1 2028) | High | Press, Series G investor commentary | Tier 2 |
| I2 | IPO pricing discount (to Stage 1 fair value) | 15-25% | Critical | IPO pricing studies (Loughran/Ritter), recent tech IPO performance | Tier 2 |
| I3 | Illiquidity/timing discount (current private vs. IPO price) | 5-15% | High | Academic literature on pre-IPO DLOM shrinkage near IPO window | Tier 3 |
| I4 | Series G required investor IRR | 20-30% over 3-5 year hold | Medium | Late-stage growth equity return expectations | Tier 3 |
| I5 | Implied Stage 1 public fair value | $13-15B (from back-solve) | Derived | Calculated from $10.1B / (1 - I3) / (1 - I2) | Derived |
| I6 | Sensitivity on Stage 1 | Report range across I2 and I3 bounds | High | Derived | Needs build |

**Interpretation:** The $10.1B Series G mark, backed out through I2 and I3, 
implies Series G investors are underwriting a public-market fair value of 
$13-15B. This is the number the intrinsic DCF and comps analysis need to 
support or contest — not the $10.1B private mark.

### Oura Priority

Oura deserves disproportionate research time. It's the only near-identical business model (consumer biometric wearable, recurring revenue, similar TAM, similar sophistication). If Pitchbook has Oura's last round at, say, 6x revenue while WHOOP is at 9x, the question becomes tightly focused: "is WHOOP genuinely 50% better than Oura, and on which dimensions?" That's answerable.

---

## Section 5: DCF-Specific Assumptions

**Feeds:** Intrinsic DCF (directly), IPO back-solve (required return), Football field (DCF leg)

### Part A: Discount Rate / WACC

| # | Assumption | Treatment | Estimate | Source | Status |
|---|---|---|---|---|---|
| D1 | Risk-free rate | **Point estimate** | **4.30%** (10yr UST, Apr 14 2026) | Fed H.15 | **Sourced — Tier 1** |
| D2 | Equity risk premium | **Point estimate** | **4.23-4.50%** (Damodaran 4.23%; Kroll 5.0%; base case 4.5%) | Damodaran Jan 2026 + Kroll | **Sourced — Tier 1. NOTE: materially below prior 5.7% estimate** |
| D3 | Beta | **Sensitivity axis** (0.9, 1.0, 1.1, 1.3) | Damodaran sector betas: Healthcare Products 0.83, Healthcare IT 0.99, Electronics 0.83, Entertainment 0.74, Recreation 0.70. Blended WHOOP beta ~0.81-0.85 across scenarios — **beta is NOT the swing factor** | Damodaran Jan 2026 + comp-derived | **Sourced — Tier 1** |
| D4 | Size premium | **Point estimate** | **~0.81%** (CRSP Decile 3 at $10B). Private co. premium adds 1.0-2.5% | Kroll/Duff & Phelps (Decile 3: $7.3-13.5B) | **Sourced — Tier 2 (Kroll detail paywalled)** |
| D5 | Company-specific risk premium | **Sensitivity axis** (1%, 2%, 3%) | Pre-IPO execution risk, private company | Academic literature + judgment | Tier 3 |
| D6 | Cost of debt | N/A | Irrelevant — minimal/no debt | — | N/A |
| D7 | Capital structure weights | Point estimate | ~100% equity | Derived from S10 | Tier 2 |
| D8 | **Resulting WACC** | **4x3 sensitivity grid** (beta x CSRP) | ~10-15% range | Derived | **Needs build in Excel** |

**The beta problem:** WHOOP has no trading history. Comp-derived unlevered beta (weighted by bucket weights from V11) is the point estimate. This makes WACC itself a function of the thesis — intellectually honest but circular. The 4x3 grid (beta x CSRP) isolates where uncertainty actually lives rather than bracketing the entire WACC.

**Component estimates (updated April 16, 2026 with sourced data):**

| Component | Pre-Research Est. | Sourced Value | Source |
|---|---|---|---|
| Risk-free rate | ~4.3% | **4.30%** | Fed H.15, Apr 14 2026 |
| ERP | ~5.7% | **4.23-4.50%** | Damodaran Jan 2026 (4.23%); Kroll (5.0%) |
| Unlevered comp beta | ~1.0-1.3 | **~0.81-0.85** (bucket-weighted) | Damodaran sector betas; individual comp betas |
| Size premium | ~0.75% | **~0.81%** | Kroll CRSP Decile 3 |
| CSRP (private co.) | 1-3% | **1.0-2.5%** | Kroll private company premium |
| **Implied cost of equity** | **~11-15%** | **~9.5-12.0%** (base ~10.0-10.5%) | Derived |

**Key finding:** WACC compressed ~200bps from prior estimate, driven by (a) ERP drop from 5.7% to 4.2-4.5% and (b) comp-derived beta landing at 0.81-0.85 rather than 1.0-1.3. Lower WACC mechanically increases DCF value by ~15-25% — partially offsetting the Bucket 3 multiple compression. Beta is NOT the swing factor across scenarios; the private company premium (CSRP) is.

### Part B: Terminal Value

| # | Assumption | Priority | Approach | Status |
|---|---|---|---|---|
| D9 | Terminal value method — primary | **Critical** | Exit multiple: apply comps-derived EV/Rev or EV/EBITDA to terminal year metrics | Design decision |
| D10 | Terminal value method — cross-check | **Critical** | Gordon Growth: perpetuity growth rate on terminal year FCF | Design decision |
| D11 | Terminal year exit multiple (EV/Revenue) | **Critical** | Comps-derived at *terminal year* growth rates, not current | Needs calc |
| D12 | Terminal year exit multiple (EV/EBITDA) | High | More stable than revenue multiple at maturity | Needs calc |
| D13 | Perpetuity growth rate (Gordon Growth) | **Critical** | GDP growth (2-3%) + inflation. Cannot exceed WACC. | Macro data, Tier 2 |
| D14 | TV as % of total EV | Diagnostic | If >75%, explicit forecast is doing too little work | Derived |
| D28 | **Multiple compression assumption** | **Critical** | Terminal multiples are ~40-60% lower than current comp multiples, reflecting deceleration from 20-30% growth to 10-15% | Explicit assumption |

**Multiple compression logic:** If Dexcom today trades at 12x revenue at 20% growth, terminal Dexcom-adjacent multiple at 10% growth should be ~6-7x (holding growth-adjusted multiple roughly constant). Section 4's growth-adjusted multiple work sets this up naturally.

**Divergence check:** If exit multiple method and Gordon Growth disagree by >25%, an assumption is inconsistent. Finding the source of divergence is itself analytical work worth reporting.

### Part C: Scenario Structure

**Three scenarios: Bear, Base, Bull**

| Assumption | Varies Across Scenarios? | Why |
|---|---|---|
| Revenue growth trajectory (R6, R7) | **Yes** | Core scenario driver |
| Churn by cohort (R11) | **Yes** | Directly drives revenue |
| Margin expansion path (C7, C9) | **Yes** | Determines FCF |
| S&M efficiency trajectory (C9c) | **Yes** | Bear: stuck at 25%+; Bull: drops to 15% |
| Bucket weighting (V11) | **Yes** | Drives terminal multiple |
| WACC | **No — hold constant** | Methodological choice (see note below) |
| Tax rate | **No** | 23-25% effective; international expansion creates mix-shift complexity (note in passing) |
| Terminal growth rate (D13) | **No** | GDP-linked |
| Capital structure (Section 3) | **Partially** | Waterfall matters in bear; irrelevant in bull |

**Constant WACC note for memo:** "Varying WACC by scenario would raise bear-case discount rate by ~150-200bps, reducing bear-case DCF by an additional 10-15%. We hold constant for methodological consistency, which marginally overstates bear-case value. This is a methodological choice, not a self-evident truth."

**D&A note:** Minimal given asset-light model. Jumps materially if WHOOP does M&A with the $575M (e.g., biomarker startup acquisition). Flag as scenario-dependent.

### Scenario Probability Weights

| # | Assumption | Priority | Status |
|---|---|---|---|
| D16 | Scenario probability weights | **Critical** | Priors below; weights are themselves a finding |
| D29 | **Probability weight sensitivity** | **Critical** | Must report the swing |

| Scenario | Weight | Thesis |
|---|---|---|
| Bear | 25% | WHOOP is Peloton 2.0 — growth decelerates, margins stall, healthcare thesis fails |
| Base | 50% | Subscription executes, healthcare optionality partially materializes, successful IPO |
| Bull | 25% | Health data platform proven — FDA clearances, Abbott/Mayo distribution, enterprise adoption |

**Reporting discipline:** Do not report a single probability-weighted EV. Report all three scenario values explicitly, then show the weight sensitivity:

| Weight Scheme | Bear/Base/Bull | Expected Value (illustrative) |
|---|---|---|
| Pessimistic | 35/50/15 | ~$9B |
| Neutral | 25/50/25 | ~$11.5B |
| Optimistic | 15/55/30 | ~$13B |

The range is more informative than the weighted average. The probability-weighted EV is one triangulation input on the football field, not the answer.

### Part D: Phase-Specific Growth

| Phase | Years | Bear | Base | Bull | Driver |
|---|---|---|---|---|---|
| **Phase 1: Pre-IPO Hypergrowth** | 2026-2027 | 50-60% | 70-80% | 90-100% | Member acquisition pace, WHOOP 5.0 reception |
| **Phase 2: Post-IPO Deceleration** | 2028-2030 | 15-20% | 25-35% | 40-50% | Churn stabilization, international, B2B traction |
| **Phase 3: Scaling Maturity** | 2031-2033 | 5-10% | 12-18% | 20-25% | TAM ceiling, competitive response, healthcare attach |

**Deceleration sourced from peer trajectories:**
- Peloton: 100%+ to negative in 3 years (catastrophic)
- Dexcom: 25-35% sustained 5+ years (gradual)
- Netflix: 25% to 10% over ~6 years post-IPO (steady)
- Garmin: 10-15% steady state

Bear case = Peloton-like (without going negative). Base = Netflix curve. Bull = Dexcom sustained growth.

### Part E: Real Options Layer

**Per CLAUDE.md: "Do not bake real-option upside into the DCF base case. Option value is additive."**

Real options are correlated, not independent — success/failure clusters because options share underlying drivers (FDA regulatory capability, clinical validation, scaled data platform, enterprise sales motion).

| Outcome Cluster | What Happens | Total Option Value | Probability |
|---|---|---|---|
| **Correlated success** | Healthcare/regulatory platform works; D19+D21+D22 cascade; glucose possibly follows | $5-6B | 15-20% |
| **Mixed outcomes** | Geographic expansion works (D20), healthcare stalls | $2-3B | 40-50% |
| **Correlated failure** | Healthcare thesis stalls; related options fail together | $0.5-1B | 30-40% |

**Individual option detail (for reference):**

| # | Option | Probability | Payoff | Expected Value |
|---|---|---|---|---|
| D19 | Healthcare reimbursement pathway | 20-30% | $2-5B incremental EV | $0.4-1.5B |
| D20 | International expansion (EU, Gulf, Asia) | 40-60% | $1-3B incremental EV | $0.4-1.8B |
| D21 | B2B enterprise / clinical deployment | 25-40% | $0.5-2B incremental EV | $0.1-0.8B |
| D22 | Women's health / fertility | 30-50% | $0.5-1.5B incremental EV | $0.15-0.75B |
| D23 | Noninvasive glucose monitoring | **3-7%** | $3-8B incremental EV | $0.1-0.55B |

**D23 note:** Probability deliberately conservative. This is the hardest unsolved problem in wearables — Apple has worked on it for a decade without shipping. But even at 3-7% probability, the payoff is so large it's material. Abbott's investment makes more sense in this frame: Abbott has CGM expertise (Libre) and may be providing technology access.

### Part F: 5-Year Exit Multiple Cross-Check

| # | Assumption | Priority | Status |
|---|---|---|---|
| D24 | Exit year | Medium | 2030 (5 years from base) |
| D25 | Exit multiple at year 5 | High | Comps-derived at 2030 projected growth |
| D26 | Discount rate | Same as D8 | Hold constant |

**Diagnostic:** If 7-year DCF says $12B and 5-year exit multiple says $8B, either years 6-7 are doing too much value creation (suspicious) or the 7-year terminal multiple is too generous. The disagreement is the finding.

### Part G: Sensitivity Analysis Structure

| # | Assumption | Priority | Status |
|---|---|---|---|
| D27 | Sensitivity analysis structure | **Structural** | Design decision below |

**Core 2-variable grids:**

| Grid | X-Axis | Y-Axis | What It Reveals |
|---|---|---|---|
| 1 | WACC (beta-driven) | Terminal multiple | Terminal value sensitivity |
| 2 | Revenue growth rate | EBITDA margin | Operating value sensitivity |
| 3 | **Churn rate** | **ARPU** | **WHOOP-specific unit economics** |

**Tornado chart:** Rank-order every key assumption by valuation impact per unit of variation. Identifies which assumptions are genuinely load-bearing vs. noise, and where to allocate additional research effort.

**Scenario vs. sensitivity distinction:** Scenarios are coherent stories (bear/base/bull). Sensitivity is mechanical perturbation of individual variables. Both useful; they answer different questions. Scenarios give range of plausible outcomes; sensitivity identifies which assumptions drive those outcomes most.

**Monte Carlo:** Skip for this project. Intellectually rigorous but diminishing returns for course work and tends to produce false precision.

---

## Section 6: Precedent Transactions

**Feeds:** Football field (precedent transactions leg, 5-10% triangulation weight), 
Cross-check on trading comp regime, Strategic-acquirer scenario as tail option.

**Role:** Narrow-band reality check rather than primary triangulation input. 
Precedent transactions answer two questions trading comps cannot: 
(1) what do acquirers pay with control premium embedded, and 
(2) what through-cycle multiples look like across different macro regimes.

### Part A: Deal Set Assumptions

| # | Assumption | Base Case | Priority | Source | Status |
|---|---|---|---|---|---|
| P1 | Deal inclusion window | Last 5 years (2021-2026), with 3-year primary focus | High | Design decision | Locked |
| P2 | Deal inclusion criteria | Wearables, digital health, consumer subscription, medical device — matched to three-bucket framework | High | Design decision | Locked |
| P3 | Deal size threshold | $500M+ enterprise value (small deals have multiples distorted by synergy math) | Medium | Design decision | Locked |
| P4 | Initial deal set | See Part B | Critical | Pitchbook M&A module, press | **Unsourced** |
| P5 | Multiple extraction method | EV / LTM revenue at announcement date; EV / NTM revenue where available | High | Per-deal research | Needs pull |
| P6 | Control premium treatment | Embedded in precedent multiples; do NOT add additional premium on top | Structural | Design decision | Locked |
| P7 | Regime classification per deal | Tag each deal as ZIRP-peak / transition / current-regime | Medium | Judgment + macro data | Design decision |
| P8 | Outlier exclusion policy | Exclude deals where strategic synergies drove multiple 2x+ above peer median | Medium | Per-deal judgment | Design decision |

### Part B: Initial Deal Set

Organized by bucket to match comps framework:

**Bucket 1 analog (Consumer Hardware):**
- Fitbit / Google (2021) — ~$2.1B / ~1.3x revenue — distressed, failed subscription pivot
- Garmin / Firstbeat Analytics (2020) — small tuck-in, reference only

**Bucket 2 analog (Consumer Subscription):**
- Peloton / Precor (2020) — $420M / hardware manufacturing play
- Any Mirror/Tonal-era fitness M&A if applicable
- Strava acquisitions if available

**Bucket 3 analog (Health Data / Medical Device):**
- Masimo / Sound United (2022) — ~$1B / consumer audio + connected health
- Dexcom / Pops Diabetes Care (2022) — ~$900M / diabetes software
- Boston Scientific / BTG (2019) — reference for medical device multiples
- iRhythm / ZIO patent deals if any
- Beddit / Apple (2017) — small but relevant to sleep-tech acquisition patterns

### Part C: Analytical Outputs

| Output | Purpose |
|---|---|
| Median + IQR multiple by bucket | Direct application to WHOOP's bucket-weighted metrics |
| Through-cycle multiple range | Ground check on 2026 trading comp multiples |
| Strategic premium inference | Benchmark for tail scenario if Abbott/Apple/Google steps in |

### Research Budget

**2-3 hours total.** Lower than comps or DCF because the method is a 
reality check, not a core triangulation input. Pull deals, compute 
multiples, produce range. Move on.

---

## Section 7: Research Execution Policy

This section defines how research is executed, when to stop, what to do 
when data is unavailable, and how to handle mid-project surprises. Designed 
for both manual work sessions and autonomous overnight runs on 
Mac Mini with Playwright.

### Part A: Time-Boxing

| Rule | Specification |
|---|---|
| Per-target time box | **3 hours maximum per priority research target** |
| Total research budget | **~30-40 hours across all priority targets** |
| Per-target minimum | Must produce at least a Tier 3 estimate before moving to next target |
| Overnight run limits | Each overnight session: max 4 targets; auto-checkpoint every 30 min |

**Rationale for 3-hour box:** tight enough to enforce discipline, loose 
enough to accommodate research dead-ends and retries. 2 hours is too 
aggressive for Pitchbook scraping + triangulation; 4+ hours enables 
rabbit-holing.

### Part B: Data Sourcing Fallback Logic

For each unsourced assumption, follow this cascade:

```
Tier 1 (Primary):     Pitchbook / Capital IQ / official filings
          ↓ (if unavailable after 90 min)
Tier 2 (Triangulated): Credible press (Bloomberg, TechCrunch, Sacra) + analyst estimates
          ↓ (if still unavailable)
Tier 3 (Reasoned):    Peer data + first-principles estimate, with explicit logic trail
          ↓ (if even this is unreliable)
FLAGGED_GAP:          Mark as "sensitivity only" — model range, do not commit to point
```

Every assumption must land at Tier 3 or better, OR be explicitly marked 
as FLAGGED_GAP. Do not fabricate. Do not leave blank.

### Part C: Research Failure Protocol

When a priority target cannot be sourced within its 3-hour box:

1. **Log what was found** (even if partial) in a dated research note
2. **Commit to Tier 3 estimate** using the fallback logic above
3. **Flag as "low confidence"** in the model with a comment
4. **Continue to next target** — do not block on unresolvable data
5. **Revisit only if modeling surfaces the assumption as load-bearing**

For the Mac Mini overnight run specifically: if Playwright hits 
authentication failure on Pitchbook, skip to SEC filing targets and log 
the Pitchbook failure. Do not spend overnight cycles retrying failed 
authentications.

### Part D: Model Diagnostic Protocol

When the DCF, comps, and precedent methods produce divergent valuations 
(>50% spread between highest and lowest method), triage as follows:

1. **First, check terminal value dominance.** If DCF terminal value is 
   >75% of enterprise value, the explicit forecast is doing too little 
   work. Revisit growth deceleration curves.
2. **Second, check multiple compression.** If terminal multiples are 
   close to current comp multiples, you forgot compression. Apply the 
   40-60% compression factor per D28.
3. **Third, check growth-adjusted multiples.** If comp set has widely 
   varying growth rates (Dexcom 20%, Garmin 10%), raw multiples are 
   misleading. Normalize per V8.
4. **Fourth, check WACC consistency.** If WACC is held constant across 
   scenarios but business risk differs materially, bear case is 
   under-discounted.
5. **If divergence persists**, the assumption inconsistency is itself 
   the finding. Document which methods disagree, what assumption bridges 
   them, and what would have to be true for reconciliation. This is 
   publishable analytical content.

### Part E: Unknowable Assumption Protocol

Some assumptions cannot be sourced at any tier (R11 churn, R14 attach 
rates, S3 preferences without S-1 access). These are genuinely unknowable 
from public data.

Policy:
1. **Do not pretend** to have sourced them. Mark as "Tier 3: estimated, 
   genuinely unknown"
2. **Model as sensitivity ranges**, not point estimates
3. **Report the sensitivity in the memo** — show how the valuation moves 
   across the plausible range of the unknown assumption
4. **Use peer data as ceiling/floor**, not as point estimate (e.g., 
   Peloton churn ~45% as upper bound, Dexcom ~10% as lower bound, 
   WHOOP somewhere in between with honest uncertainty)
5. **For the memo**: the existence of unknowable assumptions is itself 
   a finding. State explicitly: "the central range of $X-Y billion 
   contains $Z billion of sensitivity to unknowable assumptions, which 
   is why the Series G syndicate demanded participation rights / FDA 
   milestones / etc."

### Part F: Framework Revision Protocol

If research surfaces something that challenges the spec itself (e.g., 
WHOOP has a major product line not in the framework; or a regulatory 
event materially changes the bucket-3 weighting):

1. **Stop research.** Do not continue pulling data based on a framework 
   that no longer fits reality.
2. **Document the discovery** in a dated research note with specific 
   citation.
3. **Propose a spec revision** — which assumptions change, which 
   remain, what new assumptions are needed.
4. **Request approval before proceeding** if working collaboratively; 
   log and continue with flagged change if solo.
5. **Update CLAUDE.md** to reflect the new framework state.

**Do not silently adapt** the framework based on new information. The 
spec's value comes from being a commitment device; changing it silently 
undermines the commitment.

### Part G: Definition of Done (Research Phase)

Research phase is complete when ALL of the following are true:

- [ ] All 10-11 priority research targets have been attempted (not 
      necessarily sourced, but attempted)
- [ ] Every CRITICAL assumption has either a Tier 1-2 source OR an 
      explicit FLAGGED_GAP marker with sensitivity range
- [ ] Total research hours ≤ 40
- [ ] Research log is complete, dated, and linkable from spec
- [ ] A "research findings summary" document exists, one paragraph per 
      priority target, with source attribution

When all boxes are checked, move to model construction. Do not keep 
researching to close the last 10% of gaps; remaining gaps become 
sensitivity ranges in the model.

---

## Priority Research Targets (Ranked)

| Priority | Target | Time Box | What It Unlocks | Source |
|---|---|---|---|---|
| 1 | **Peloton 10-Ks (2019-2025)** | 3 hrs | S&M trajectory, GM decomposition, churn disclosures | SEC EDGAR |
| 2 | **Pitchbook: WHOOP tearsheet** | 3 hrs | Churn, retention, unit economics, gap financing | Playwright → Pitchbook |
| 3 | **Pitchbook: Oura profile** | 3 hrs | Closest private comp — valuation, revenue, implied multiple | Playwright → Pitchbook |
| 4 | **Dexcom 10-K** | 2 hrs | R&D intensity, GM structure, regulatory pathway | SEC EDGAR |
| 5 | **Comp multiples pull** (7 public comps) | 3 hrs | Current + historical EV/Rev at 4 time points | Public data |
| 6 | **Pitchbook: WHOOP cap table** | 3 hrs | Shares, preferences, option pool, secondary activity | Playwright → Pitchbook |
| 7 | **Forge/EquityZen: WHOOP secondary** | 2 hrs | Common share price signal | Web search |
| 8 | **Damodaran ERP + beta data** | 1 hr | WACC inputs | Damodaran website |
| 9 | **WHOOP pricing history** | 1 hr | Historical pricing changes | Web Archive |
| 10 | **Remaining 10-Ks** (GRMN, RMD, MASI, IRTC) | 3 hrs | Complete comp profiles | SEC EDGAR |
| 11 | **Precedent M&A deals** | 2 hrs | Precedent transactions leg + regime check | Pitchbook M&A, press |

**Total time budget:** 26 hours. Remaining 4-14 hours available for 
retries, triangulation, and gap closure per Section 7 policy.

---

## Next Steps

### Immediate (before first research session)

1. Confirm Playwright + Pitchbook authentication works end-to-end on a 
   throwaway query (e.g., pull Peloton's Pitchbook page as test)
2. Create research log template in /research/ directory
3. Set up Excel model scaffold skeleton with assumption cells linked to 
   this spec by assumption number

### Research Phase (per Section 7 policy)

1. **Session 1 (overnight):** Targets 1, 2, 3 — Peloton 10-Ks, WHOOP 
   Pitchbook, Oura Pitchbook. ~9 hours wall time; Playwright for 
   Pitchbook, SEC for Peloton.
2. **Session 2 (overnight):** Targets 4, 5, 6 — Dexcom 10-K, comp 
   multiples, WHOOP cap table. ~9 hours wall time.
3. **Session 3 (manual or overnight):** Targets 7-11. ~9 hours wall time.
4. **Gap closure (manual):** Review all FLAGGED_GAP assumptions, 
   triangulate Tier 3 estimates, finalize research findings summary.

### Model Construction (after research phase)

1. Excel DCF build — populate scaffold from research outputs
2. Cap table + waterfall model
3. Comps + precedent transactions workbook
4. Football field synthesis
5. Sensitivity tables per D27 specifications

### Synthesis

1. IC memo draft
2. Football field slide
3. Peer review cycle
