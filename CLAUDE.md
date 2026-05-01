# WHOOP Private Company Valuation — Project Context

## Project Goal

Produce a rigorous, defensible private-company valuation of WHOOP Inc. as a corporate finance learning exercise. The deliverable is an investment-committee-style memo plus supporting Excel model, triangulating WHOOP's intrinsic value against its March 2026 Series G mark of $10.1B.

This is a learning project, not a real investment decision. The goal is to practice the full private-company valuation stack — research, cap structure analysis, segmented comps, scenario DCF, real-options layering, and triangulation — with AI-assisted workflows.

---

## Target Snapshot (as of April 2026)

- **Company:** WHOOP Inc., Boston-based wearable health company
- **Founded:** 2012 by Will Ahmed (CEO)
- **Last round:** Series G, March 31, 2026 — $575M at $10.1B post-money
- **Series G lead:** Collaborative Fund
- **Strategic investors:** Abbott Laboratories, Mayo Clinic
- **Sovereign wealth:** Qatar Investment Authority, Mubadala
- **Financial investors:** Macquarie Capital, IVP, Foundry, Accomplice, Affinity Partners, 2PointZero Group, Glade Brook, B-Flexion, Promus Ventures, Bullhound Capital
- **Key metrics:** 2.5M+ members; $1.1B bookings run-rate end of 2025 (**~$650M est. recognized revenue, stress-tested down from $725M**); 103% YoY subscription growth; cash flow positive in 2025
- **Revenue mix:** ~80% consumer subscription, ~20% B2B/Unite (up from ~5% earlier); **~40-45% international revenue (base case)** — see stress-test below
- **Products:** Wearable + subscription; FDA-cleared ECG; Blood Pressure Insights; Healthspan longevity; Advanced Labs blood biomarker analysis (350K+ waitlist); WHOOP Coach (generative AI)
- **Exit path:** Explicit IPO trajectory, likely 2027 ("last private round" per Ahmed)
- **Cap structure:** 537.9M authorized preferred / 361.2M outstanding common; all prefs 1x non-participating pari passu (Pitchbook); 49 investors across 10 rounds (Cap IQ)
- **Employees:** ~800 current, 600+ planned hires in 2026
- **CMS milestone:** WHOOP Physician Services PC selected for CMS Innovation Center Access Program (Apr 13, 2026)

---

## Central Thesis Framing

The $3.6B (2021) → $10.1B (2026) re-rating decomposes into three drivers:

1. **Growth that earned it.** Revenue grew ~5.5x; multiple actually *compressed* from ~18x to ~9x revenue
2. **Healthcare pivot became real.** FDA clearances + Abbott/Mayo investment = "health data platform" thesis materially more credible
3. **Rule of 40 elite status.** 103% growth + cash flow positive = premium multiple justified

**The paper's central question:** does intrinsic value plus real-option upside support the $10.1B mark, or is the mark ahead of fundamentals?

---

## The Football Field (5 methods)

1. **Intrinsic DCF** — scenario-based, with real-options layered on top of base case
2. **Trading comps, three buckets** — hardware / subscription / health-data (see below)
3. **Precedent transactions** — wearables and health-device M&A
4. **Last-round implied** — $10.1B Series G as a current market datapoint
5. **Implied IPO trading range** — back-solved from Series G investor required returns

**Take-private LBO leg is excluded.** Justification:
- Capital structure all VC preferred, no debt capacity for LBO leverage
- Sovereign wealth + crossover participation signals locked-in IPO path
- Natural strategic acquirers (Apple, Google) face antitrust; Abbott chose the investor path

---

## Three-Bucket Comp Framework (Finalized April 16, 2026)

| Bucket | Public Comps | Role | Multiple Range |
|---|---|---|---|
| **B1: Consumer hardware** | Garmin (GRMN) | Sole comp; Apple (AAPL) as reference only | **6.2–6.7x revenue** (observed Apr 2026; was 3-5x pre-research) |
| **B2: Consumer subscription** | Peloton (PTON), Spotify (SPOT) | Disaggregated, not averaged: Peloton = distressed end (~1.2x), Spotify = mature end (~5.1x) | **1.2–5.1x revenue** (was 0.8-4x; Spotify re-rated post-profitability) |
| **B3: Health data / medical device** | Dexcom (DXCM), ResMed (RMD), Masimo (MASI), iRhythm (IRTC) | Aspirational anchor; iRhythm added for cardiac wearable parallel | **5.0–6.4x revenue** (was 6-12x; Dexcom compression reset tier) |

**Private comps:** Oura (highest-signal comp — nearest business model match), Strava (reference if data available)

**Comps cut with rationale:** GoPro (action cameras, not wearables), Logitech (PC peripherals, zero overlap), Netflix (content-driven subscription, category error), Insulet (too specialized in insulin delivery), Abbott (WHOOP investor not peer, too diversified), Fitbit (distressed acquisition, story captured by Peloton), Under Armour/Lululemon (apparel-adjacent), Boston Scientific/Medtronic (too diversified/mature). See full rationale in spec.

**Peloton is the single most important cautionary comp.** Same subsidized-hardware + subscription structure, now trading at distressed multiples. The bull thesis must specifically address why WHOOP avoids Peloton's fate.

**Bucket weighting IS the thesis.** Each scheme makes a claim about what WHOOP is (recalibrated with observed Apr 2026 multiples):
- Bear (40/40/20): WHOOP is Peloton with better branding → **~4.6x revenue → $5.1B** (was 2-4x)
- Base (20/40/40): Subscription business with healthcare optionality → **~5.1x revenue → $5.6B** (was 4-7x)
- Bull (10/30/60): Health data platform that happens to use a wearable → **~5.4x revenue → $5.9B** (was 6-9x)
- Series G implied (~5/25/70): Market prices WHOOP as a health-data company → ~9x revenue

**Critical finding (Session 2):** No bucket-weighting scheme using current observed multiples reaches $10.1B. Max blended = ~5.4x → $5.9B. The gap requires a ~1.7x growth premium (WHOOP at 103% vs. comps at 10-26%) plus real-option value to bridge to $10.1B. This is the central tension the IC memo must address.

---

## Real-Options Layer

Base DCF models the core subscription business at current trajectory. Real options are **correlated, not independent** — model as outcome clusters:

| Cluster | Options Included | Value | Probability |
|---|---|---|---|
| Correlated success | Healthcare reimbursement + B2B clinical + Women's health cascade | $5-6B | 15-20% |
| Mixed outcomes | Geographic expansion works, healthcare stalls | $2-3B | 40-50% |
| Correlated failure | Healthcare thesis stalls, related options fail together | $0.5-1B | 30-40% |

Individual options: Healthcare/reimbursement (20-30% — **upgraded by CMS Innovation Center selection**), International expansion (40-60% — **note: ~60% of sales already international, partially in base case**), B2B enterprise (25-40% — **note: Unite already ~20% of recurring revenue, partially in base case**), Women's health (30-50%), Noninvasive glucose monitoring (3-7% — deliberately conservative, hardest unsolved problem in wearables).

**Session 1 finding:** International expansion and B2B enterprise options need re-scoping. Both are already partially captured in the base case (~60% intl sales, ~20% B2B revenue). Real-option value should reflect *incremental* upside beyond current trajectory, not total addressable opportunity.

**Do not bake into base case.** Option value is additive, never embedded in DCF.

---

## Key Open Questions

### Answered (Session 1)
- ~~What's the actual liquidation preference stack across Series A–G?~~ → **All 1x non-participating pari passu** (Pitchbook + Cap IQ). Simplified waterfall, favorable for common. FLAGGED: Cap IQ says 1x but doesn't specify participating/non-participating; Pitchbook says non-participating. **Assume non-participating (Pitchbook more specific).**
- ~~Breakdown of $1.1B bookings: US vs. international, consumer vs. emerging B2B?~~ → **~60% international / ~40% US** (Yahoo Finance/GuruFocus); **~80% consumer / ~20% B2B Unite** (Sacra/BMCT). Both need second-source verification.
- ~~Oura's last private valuation and trajectory as a direct comp?~~ → **$11B (Series E, Oct 2025); Pitchbook estimates $12.05B current.** Revenue: $398M (2024) → $927M (TTM Sep 2025). Profitable: 17% EBITDA margin. Trades at ~12x revenue vs. WHOOP's ~9x on bookings.
- ~~WHOOP 5.0 launch reception?~~ → **"Whoopgate" backlash (May 2025) over pricing/upgrade policy; company issued free upgrades within 48 hours.** Estimated $30-40M revenue gap from renewal timing. FDA warning letter on Blood Pressure Insights (Jul 2025). Despite backlash, 103% bookings growth sustained through 2025.
- ~~Was there any financing activity during the 2022-2025 gap?~~ → **Yes: 5 interim rounds** including mezzanine ($35.77M, May 2023), debt ($10.13M, Mar 2024), and later-stage VC (Jan 2025). Cap IQ shows Growth rounds in Aug 2023 and May 2024 with no change in common shares (likely non-dilutive).

### Partially Answered (Session 1)
- Cohort retention by tenure → **Directional only:** >80-85% annual retention, monthly churn <3% (Pro tier), monthly subscribers churn up to 10x faster than annual. **No cohort-level data.** Churn sensitivity grids built in `research/revenue-bookings-reconciliation.md`. Still the #1 gap.
- Hardware BOM cost → **2016 BOM was $250-$300/device** (Contrary Research). Current BOM unknown but likely $50-80 at scale given 10x processor efficiency gains and volume. **Estimated ~19-month payback period** on hardware subsidy.
- R19 ARPU decomposition → **Bottom-up model built:** blended subscription ARPU ~$262/yr (mid-market tier mix); total ARPU including Labs/accessories ~$302/yr. The $440 implied ARPU from bookings math is an artifact of the bookings definition, not real per-member revenue. See `research/revenue-bookings-reconciliation.md`.

### Still Open
- What are Abbott + Mayo specifically contracted to do? Distribution? Clinical studies? Co-branded products? → **Not publicly disclosed.** CMS Innovation Center selection (Apr 2026) is strongest signal of healthcare pathway.
- Does WHOOP plan dual-class share structure for IPO? → **Not disclosed.**
- Series F (SoftBank) ratchet provisions — extinguished at Series G or still live? → **Not found.** SoftBank notably absent from Series G syndicate. Open question whether they sold secondary or were diluted.
- Current runway given cash flow positive status and $575M infusion? → **Not quantified.** Cash flow positive + $575M = multi-year runway.
- Option pool size? → **Not disclosed in Cap IQ or Pitchbook.** Cap table shows ~11.7% gap between total preferred authorized and outstanding common, which may include option pool.

---

## Deliverables

| # | File | Status |
|---|---|---|
| 1 | `CLAUDE.md` — project context (living doc) | **Active** |
| 2 | `research/whoop-research-brief.md` — structured research brief | **Complete** |
| 3 | `research/valuation-trajectory-timeline.md` — valuation history across rounds | Pending |
| 4 | `docs/superpowers/specs/2026-04-16-assumption-inventory-design.md` — master assumption inventory (115 assumptions, 7 sections) | **Complete — v2** |
| 5 | `model/whoop-master-model.xlsx` — master Excel model (DCF + comps + waterfall) | Scaffold exists |
| 6 | `model/whoop-cap-table.xlsx` — cap table + waterfall at exit scenarios | Pending |
| 7 | `model/whoop-dcf.xlsx` — scenario DCF with real-options | Pending |
| 8 | `model/whoop-comps.xlsx` — three-bucket comp analysis | Pending |
| 9 | `model/whoop-football-field.xlsx` — triangulation summary | Pending |
| 10 | `output/whoop-ic-memo.docx` — 10–15 page IC-style write-up | Pending |
| 11 | `output/whoop-ic-deck.pptx` — presentation deck | Scaffold exists |
| 12 | `output/whoop-football-field.pptx` — one-slide summary | Pending |
| 13a | `research/whoop-pitchbook-data.md` — Pitchbook extraction (cap table, funding, financials) | **Complete — Session 1** |
| 13b | `research/whoop-capiq-data.md` — Capital IQ extraction (dilution waterfall, investors, key developments) | **Complete — Session 1** |
| 13c | `research/oura-pitchbook-data.md` — Oura private comp profile | **Complete — Session 1** |
| 13d | `research/peloton-10k-analysis.md` — Peloton cautionary comp deep dive | **Complete — Session 1** |
| 13e | `research/web-research-sweep.md` — market data, Damodaran, Forge, Garmin, Strava | **Complete — Session 1** |
| 13f | `research/revenue-bookings-reconciliation.md` — $1.1B bookings vs. revenue analysis, ARPU model, churn grids | **Complete — Session 1** |
| 13g | `research/investor-deep-research.md` — Collaborative Fund, IVP, SoftBank, conference/podcast mining | **Complete — Session 1** |
| 13h | `research/stress-test-international-revenue.md` — 60% intl claim verification | **Complete — Session 1** |
| 13i | `research/stress-test-revenue-reconciliation.md` — revenue estimate stress test (revised base: $650M) | **Complete — Session 1** |
| 14 | `research/comp-dexcom-dxcm.md` | **Complete — Session 2** |
| 14 | `research/comp-garmin-grmn.md` | **Complete — Session 2** |
| 15 | `research/comp-resmed-rmd.md` | **Complete — Session 2** |
| 16 | `research/comp-masimo-masi.md` | **Complete — Session 2** |
| 17 | `research/comp-irhythm-irtc.md` | **Complete — Session 2** |
| 18 | `research/comp-spotify-spot.md` | **Complete — Session 2** |
| 19 | `research/comp-peloton-pton.md` | **Complete — Session 2** |
| 20 | `research/comp-trading-multiples-summary.md` — consolidated multiples + bucket analysis | **Complete — Session 2** |
| 21 | `research/damodaran-wacc-inputs.md` — ERP, betas, risk-free rate, size premia | **Complete — Session 2** |
| 22 | `research/comp-historical-multiples-v19.md` — 3yr time variance for GRMN/PTON/DXCM | **Complete — Session 2** |
| 23 | `research/peloton-10k-gaps.md` — S&M vs G&A split (XBRL), SBC history | **Complete — Session 2** |
| 24 | `research/secondary-market-pricing.md` — Forge/Hiive/EquityZen, DLOM analysis | **Complete — Session 2** |
| 25 | `research/precedent-transactions.md` — 14 deals, 3-bucket M&A analysis | **Complete — Session 2** |

---

## Working Conventions

### My preferred response style
- Lead with the answer, then explain; go 2–3 layers deep to first principles
- Challenge my ideas; don't treat my words as correct by default
- Truth / accuracy / creativity are the goal; we are not optimizing for agreement
- Concision for direct questions; longer-form for project/open-ended work

### Modeling conventions
- **Blue font** for hard-coded inputs, **black** for formulas, **green** for links to other sheets
- Every assumption needs a sourced justification in a comments column or linked doc
- Sensitivity tables on all key valuation outputs
- Scenario analysis with explicit probability weights; no point estimates pretending to be the answer

### Citation discipline
- Every data point in the brief or model must cite its source
- Pitchbook / Cap IQ / web search sources get clear URLs or document references
- Sell-side estimates and seller-provided numbers are flagged as such
- Date-stamp everything because metrics move

---

## Data Sources Available

### Primary (confirmed working — Session 1)
1. **Playwright → Pitchbook** (authenticated via UChicago) — funding rounds, cap table, private comp data, financials
2. **Playwright → S&P Capital IQ** (authenticated via UChicago) — cap table detail, dilution waterfall, investor list, key developments, comps
3. **SEC EDGAR** — Peloton, Dexcom, Garmin, and other public comp 10-Ks (note: some direct filing pages return 403; use search or StockAnalysis.com as fallback)
4. **Web search + WebFetch** — press, analyst reports (Sacra, Getlatka, TechCrunch, Bloomberg, Contrary Research)
5. **Secondary market data** — Forge Global ($11.23/share), EquityZen (shares available, pricing requires accreditation)
6. **Academic/reference** — Damodaran (ERP 4.23%, betas, size premia); Kroll size premium is subscription-gated (FLAGGED_GAP)

### Confirmed Not Working / Limited
- **CNBC video transcripts** — 403 errors on video pages; rely on text articles covering same interviews
- **Getlatka** — 403 on direct access; data appears stale (reflects 2024 not 2025)
- **Sacra PDF** — binary PDF at S3 URL, cannot be parsed by WebFetch; paywall ($50/mo) for detailed model. **High-value target if budget available.**
- **Refinitiv Workspace** — login page visible in browser (tab 5) but not authenticated

### Stretch (MCP plugins — not yet authenticated)
- Daloopa, Morningstar, FactSet, Moody's, Aiera
- Test as available; do not build sourcing plans that depend on these

---

## Things NOT to Do

- **Do not compute WACC or DCF math in an LLM turn.** Always use Excel or a deterministic script.
- **Do not accept management forecasts at face value.** Recast with independent assumptions.
- **Do not treat the $10.1B as ground truth.** It is a market datapoint, one of five triangulation inputs.
- **Do not generate placeholder numbers.** If data is unavailable, flag and ask — never fabricate.
- **Do not reconstruct copyrighted article content verbatim.** Paraphrase and cite.
- **Do not bake real-option upside into the DCF base case.** Option value is additive.
- **Do not default to generic comp sets.** The three-bucket framework is load-bearing — respect it.
- **Do not use a single flat gross margin line.** Model subscription GM and hardware GM separately; blended GM is derived and varies with growth rate.
- **Do not exclude SBC from FCF.** SBC is a real cost; dilution modeled separately.
- **Do not average Bucket 2 comps.** Peloton and Spotify are disaggregated; the range is the insight.
- **Do not sum real-option expected values as if independent.** Options are correlated; model as clusters.
- **Do not report a single probability-weighted EV as "the answer."** Report all scenarios + weight sensitivity.

---

## Current Project Phase: Research Complete → Model Construction

**Assumption inventory is complete** (115 assumptions, 42 critical, ~20 still unsourced, 7 locked). Full spec at `docs/superpowers/specs/2026-04-16-assumption-inventory-design.md`.

### Research Session Status

- **Session 1:** WHOOP Pitchbook + Cap IQ + Oura + Peloton 10-K + web sweep + revenue reconciliation + investor deep research — **Complete** (9 research files)
- **Session 2:** All 7 public comp 10-K profiles + trading multiples + WACC inputs + historical multiples + Peloton S&M split + secondary market pricing + precedent transactions — **Complete** (13 research files)
- **Session 3:** Gap closure + model construction handoff — **Scope absorbed into Session 2; remaining gaps are minor**

### Session 1 — Key Research Findings

1. **Revenue reconciliation:** $1.1B is bookings run-rate (annualized December exit rate). Real 2025 recognized revenue est. ~$650-$800M (base: $725M). The $260M Getlatka figure is stale 2024 data. True trailing EV/Revenue ~14x; forward 2026 ~6.7-8.4x.
2. **Cap structure:** All prefs 1x non-participating pari passu. 537.9M auth preferred / 361.2M outstanding common. Full dilution waterfall from Cap IQ (Seed through Series F).
3. **Oura comp:** $11-12B valuation on ~$927M TTM revenue. Profitable (17% EBITDA margin). Trades at ~12x revenue — HIGHER than WHOOP's ~9x on bookings, suggesting $10.1B may be conservative vs. nearest private comp.
4. **Geographic mix:** ~60% international (was assumed US-heavy). Requires re-weighting of international expansion real-option.
5. **B2B Unite:** ~20% of recurring revenue (was assumed ~5%). Material enterprise business line.
6. **CMS Innovation Center:** WHOOP Physician Services selected Apr 13, 2026. Strongest healthcare reimbursement signal to date.
7. **SoftBank absent from Series G:** Not listed in syndicate. Status of their position unknown.
8. **Peloton cautionary data:** Churn 6x'd (0.31% → 1.9%), SG&A peaked 55% of revenue, subscribers peaked 3.03M now 2.66M.

### Session 1 — Data Inconsistencies to Resolve

| # | Inconsistency | Source A | Source B | Resolution Needed |
|---|---|---|---|---|
| 1 | **Total funding raised** | $990.52M (Cap IQ) | $1.03B (Pitchbook) / $1.376B (Sacra) / $958.9M (Forge) | Likely definitional — does it include debt rounds? Cap IQ and Pitchbook are closest; **use Pitchbook $1.03B for equity raised** |
| 2 | **Employee count** | 500 (Cap IQ) / 600 (Pitchbook) / 725 (PremierAlts) / 800 (Boston Globe) / 1,200 (Getlatka) | — | Cap IQ data is stale. Boston Globe ($800, Mar 2026) + WHOOP press (600+ planned hires) most credible. **Use ~800 current.** |
| 3 | **Liq pref type** | 1.00x multiple, type unspecified (Cap IQ) | 1x non-participating pari passu (Pitchbook) | Pitchbook is more granular. **Use non-participating.** Verify at S-1 filing. |
| 4 | **2024 revenue** | $200M (Pitchbook) | $260M (Getlatka, labeled Jun 2025) | Getlatka likely includes partial 2025 or uses different cut-off. **Use Pitchbook $200M for CY2024.** |
| 5 | **International revenue %** | "60% of new sales" (InsiderFinance) / "60% of sales" (Techmeme/NYT) | "Heavily US-weighted" (original research brief) | **RESOLVED via stress test:** Original source is NYT DealBook (Niko Gallogly). Key ambiguity: "60% of NEW sales" (member acquisitions) vs. "60% of total sales." Most likely 60% of new member adds are intl, but total revenue is ~40-45% intl due to US-heavy legacy base. Absent from official press release. **Use 40-45% intl revenue as base case.** See `research/stress-test-international-revenue.md`. |
| 6 | **B2B Unite % of revenue** | "~20% of recurring" (Sacra/BMCT) | "~5%" (earlier estimates) | May reflect real growth over time, not a conflict. **Use 15-20% range; model as sensitivity.** |
| 7 | **Oura employee count** | 900 (Pitchbook) | 1,268 (Tracxn, Mar 2026) | Different scrape dates/methods. Not model-critical. |
| 8 | **Series G date** | Mar 31, 2026 (press/Pitchbook) | Feb 26, 2026 (Cap IQ) | Cap IQ may reflect signing date vs. announcement/close. **Use Mar 31, 2026 (public announcement).** |

### Session 2 — Completed
1. All 7 public comp 10-K/20-F profiles with 3-5yr financial history
2. Consolidated trading multiples summary with bucket analysis, growth-adjusted multiples, beta table
3. Implied WHOOP valuations by bucket weighting (finding: max ~$5.9B without growth premium)
4. Bucket range recalibration (B1: 6.2-6.7x, B2: 1.2-5.1x, B3: 5.0-6.4x)

### Session 2 — Data Gaps (Resolved / Accepted)
- ~~Peloton S&M vs. G&A historical split~~ — **RESOLVED via XBRL. research/peloton-10k-gaps.md**
- ~~Historical multiples (V19)~~ — **RESOLVED. research/comp-historical-multiples-v19.md**
- Peloton FY2021/FY2022 segment revenue — **Accepted as estimates** (±5% accuracy sufficient for comp analysis)
- Dexcom & Masimo S&M vs. G&A — **Not separately reported in filings; accepted as combined SG&A**
- iRhythm FY2025 convertible notes balance — **Minor; EV estimate uses FY2024 balance as proxy**

### Session 2 — Remaining Work (ALL COMPLETE)
1. ~~Pull Damodaran ERP + betas + risk-free rate (D1, D2, D3, D4)~~ — **Complete. research/damodaran-wacc-inputs.md**
2. ~~Pull historical multiples for V19 time variance~~ — **Complete. research/comp-historical-multiples-v19.md**
3. ~~Update spec with recalibrated bucket ranges~~ — **Complete**
4. ~~Peloton 10-K deep pull for S&M/G&A split + SBC~~ — **Complete. research/peloton-10k-gaps.md. S&M from XBRL: peaked $1,019M (28.4%) FY2022, collapsed to $422M (16.9%) FY2025. SBC $230M (9.2%) FY2025.**
5. ~~Forge/EquityZen secondary pricing (S9, S14)~~ — **Complete. research/secondary-market-pricing.md. DLOM 20-25% base; Hiive $5.44-6.88 (39-51% discount)**
6. ~~Precedent transactions (Section 6)~~ — **Complete. research/precedent-transactions.md. 14 deals; B3 medtech 6.6-10.1x; implied WHOOP $5-8B**

### Session 2 — Key Findings Summary
- **Bucket 3 compressed 60%:** Dexcom 13.8x→5.0x over 3yr. No static comp weighting reaches $10.1B.
- **WACC lower than expected:** ERP 4.23% (was 5.7%), beta 0.81-0.85 (was 1.0-1.3), base WACC ~10.0-10.5% (was 11-15%). Lifts DCF ~15-25%.
- **Growth premium is the bridge:** $10.1B requires ~1.7x premium over static comps. At 2023 multiples the mark works; at current multiples needs 125% premium.
- **Peloton S&M trajectory:** S&M peaked 28.4% of revenue (FY2022), crashed to 16.9% (FY2025). Overlay chart data now complete for bear-case anchor.
- **Secondary market says $5-7B:** Hiive order book at $5.44-6.88 (39-51% discount to Series G). Oura tender at 25% discount = best DLOM anchor.
- **Precedent M&A says $5-8B base:** B3 medtech deals at 6.6-10.1x; all connected-fitness deals value-destructive.
- **Triangulation converging:** Static comps $5-6B, precedent txns $5-8B, secondary market $5-7B. DCF is the tiebreaker.

### Next Phase: Model Construction
Research is substantially complete. Remaining gaps are minor (Peloton official ARPU KPI, EquityZen locked pricing). Ready for:
1. Excel DCF build from research outputs
2. Cap table + waterfall model  
3. Comps + precedent transactions workbook
4. Football field synthesis + sensitivity tables

### Remaining Minor Gaps (not blocking model construction)
- Sacra PDF access ($50/mo subscription) — highest-value paywall for ARPU/churn data
- EquityZen specific pricing (requires accredited investor account)
- Peloton official ARPU KPI from 10-K MD&A (derived estimates sufficient: $42-49/month)
- Cross-source reconciliation items from Session 1 (see table above — all have working resolutions)

### Session 1 — Critical Gaps Remaining (prioritized)

| # | Gap | Impact | Best Path |
|---|---|---|---|
| 1 | **Cohort churn curves (Y1/Y2/Y3)** | Changes LTV by ~40%, cascades to DCF | Sacra PDF, or wait for S-1 |
| 2 | **Subscription vs. hardware gross margin** | Drives blended margin trajectory in DCF | Peer inference (Peloton sub GM ~68%, hw GM ~14%) + model sensitivity |
| 3 | **Abbott/Mayo contract specifics** | Determines healthcare reimbursement option probability | Not publicly disclosed; monitor for press |
| 4 | **SoftBank Series F ratchet provisions** | Could affect waterfall economics | Not found; SoftBank's Series G absence is circumstantial |
| 5 | **Option pool size** | Needed for fully-diluted share count | Cap IQ shows ~11.7% gap; estimate as 10-15% |
| 6 | **Kroll size premium** | WACC input for private company premium | Subscription-gated; use Damodaran small-cap premium as proxy |
| 7 | **Second source for 60% intl revenue** | Load-bearing for geographic assumptions | Search for additional Series G press coverage |

### Model Construction (after research)
1. Excel DCF build from research outputs
2. Cap table + waterfall model
3. Comps + precedent transactions workbook
4. Football field synthesis + sensitivity tables

### Key Analytical Moves to Execute
- Dual back-solve (naive vs. growth-adjusted) on Series G implied bucket weights — **partially done in trading summary; needs formalization**
- Three-stage discount framework ($10.1B → $11.2B IPO → $13-15B public fair value)
- Growth premium quantification: what premium did Dexcom/Peloton command at peak growth? Grounds the ~1.7x premium needed to bridge to $10.1B. **Session 2 V19 data shows Dexcom at 13.8x (2023) vs. 5.0x (2026) — peak-growth multiples DO support $10.1B**
- Peloton S&M/revenue overlay chart as bear-case anchor — **S&M data now complete (research/peloton-10k-gaps.md); ready for chart build**
- ~~Churn × ARPU sensitivity grid (WHOOP-specific unit economics)~~ — **Complete in revenue-bookings-reconciliation.md**
- Top-down P&L vs. bottoms-up cohort model validation — **Bottom-up revenue build complete ($808-872M); top-down pending**
- **NEW: Oura vs. WHOOP comp analysis** — Oura at $12B / ~12x rev vs. WHOOP at $10.1B / ~14x recognized rev. Why does Oura command a premium despite inverted revenue mix (80% hardware)? Profitability? Ring form factor? Needs explicit analysis.
- **NEW: Revenue bridge from $725M (2025) to forward estimates** — need 2026/2027 projections for forward multiple analysis and IPO back-solve

---

## Living Document Note

This file is the persistent memory for the project. Update it as:
- Thesis evolves based on new data
- Open questions get answered
- Deliverables get completed
- Assumptions get sourced and locked

Every Claude Code session loads this automatically. Keep it current.
