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
- **Key metrics:** 2.5M+ members; $1.1B revenue run-rate end of 2025; 103% YoY subscription growth; cash flow positive in 2025
- **Products:** Wearable + subscription; FDA-cleared ECG; Blood Pressure Insights; Healthspan longevity; Advanced Labs blood biomarker analysis; WHOOP Coach (generative AI)
- **Exit path:** Explicit IPO trajectory, likely 2027

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
| **B1: Consumer hardware** | Garmin (GRMN) | Sole comp; Apple (AAPL) as reference only | 3–5x revenue |
| **B2: Consumer subscription** | Peloton (PTON), Spotify (SPOT) | Disaggregated, not averaged: Peloton = distressed end (~0.5-1x), Spotify = mature end (~3-4x) | 0.8–4x revenue |
| **B3: Health data / medical device** | Dexcom (DXCM), ResMed (RMD), Masimo (MASI), iRhythm (IRTC) | Aspirational anchor; iRhythm added for cardiac wearable parallel | 6–12x revenue |

**Private comps:** Oura (highest-signal comp — nearest business model match), Strava (reference if data available)

**Comps cut with rationale:** GoPro (action cameras, not wearables), Logitech (PC peripherals, zero overlap), Netflix (content-driven subscription, category error), Insulet (too specialized in insulin delivery), Abbott (WHOOP investor not peer, too diversified), Fitbit (distressed acquisition, story captured by Peloton), Under Armour/Lululemon (apparel-adjacent), Boston Scientific/Medtronic (too diversified/mature). See full rationale in spec.

**Peloton is the single most important cautionary comp.** Same subsidized-hardware + subscription structure, now trading at distressed multiples. The bull thesis must specifically address why WHOOP avoids Peloton's fate.

**Bucket weighting IS the thesis.** Each scheme makes a claim about what WHOOP is:
- Bear (40/40/20): WHOOP is Peloton with better branding → 2-4x revenue
- Base (20/40/40): Subscription business with healthcare optionality → 4-7x revenue
- Bull (10/30/60): Health data platform that happens to use a wearable → 6-9x revenue
- Series G implied (~5/25/70): Market prices WHOOP as a health-data company → ~9x revenue

---

## Real-Options Layer

Base DCF models the core subscription business at current trajectory. Real options are **correlated, not independent** — model as outcome clusters:

| Cluster | Options Included | Value | Probability |
|---|---|---|---|
| Correlated success | Healthcare reimbursement + B2B clinical + Women's health cascade | $5-6B | 15-20% |
| Mixed outcomes | Geographic expansion works, healthcare stalls | $2-3B | 40-50% |
| Correlated failure | Healthcare thesis stalls, related options fail together | $0.5-1B | 30-40% |

Individual options: Healthcare/reimbursement (20-30%), International expansion (40-60%), B2B enterprise (25-40%), Women's health (30-50%), Noninvasive glucose monitoring (3-7% — deliberately conservative, hardest unsolved problem in wearables).

**Do not bake into base case.** Option value is additive, never embedded in DCF.

---

## Key Open Questions

- What's the actual liquidation preference stack across Series A–G?
- Cohort retention by tenure — what's the churn curve after year 1, year 2, year 3?
- Hardware BOM cost and payback period per member?
- What are Abbott + Mayo specifically contracted to do? Distribution? Clinical studies? Co-branded products?
- Breakdown of $1.1B bookings: US vs. international, consumer vs. emerging B2B?
- Oura's last private valuation and trajectory as a direct comp?
- WHOOP 5.0 launch reception — any reported sales or member acquisition acceleration?
- Current runway given cash flow positive status and $575M infusion?
- Was there any financing activity (bridge, SAFE, convertible) during the 2022-2025 gap?
- Does WHOOP plan dual-class share structure for IPO?
- What is the R19 ARPU decomposition — accessories-heavy, Labs-heavy, or plan-mix-heavy?
- Series F (SoftBank) ratchet provisions — extinguished at Series G or still live?

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

### Primary (confirmed working)
1. **Playwright → Pitchbook** (open Chrome tab) — funding rounds, cap table, private comp data, M&A deals
2. **SEC EDGAR** — Peloton, Dexcom, Garmin, and other public comp 10-Ks
3. **Web search** — press, analyst reports (Sacra, Getlatka, TechCrunch, Bloomberg)
4. **Public company filings** — investor relations pages for all comps
5. **Secondary market data** — Forge Global, EquityZen for pricing signals
6. **Academic/reference** — Damodaran (ERP, betas), Kroll (size premia)

### Stretch (MCP plugins — not yet authenticated)
- S&P Global / Capital IQ, Daloopa, Morningstar, FactSet, Moody's, Aiera
- Test as available; do not build sourcing plans that depend on these

### Via UChicago library
- Pitchbook web access (backup to Playwright)
- Capital IQ
- Bloomberg Terminal (if accessible)

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

## Current Project Phase: Research Execution

**Assumption inventory is complete** (115 assumptions, 42 critical, 32 unsourced, 7 locked). Full spec at `docs/superpowers/specs/2026-04-16-assumption-inventory-design.md`.

### Immediate Next Steps
1. Confirm Playwright + Pitchbook authentication end-to-end
2. Create research log template in `/research/`
3. Set up Excel model scaffold linked to spec assumption numbers

### Research Sessions (per Section 7 time-boxing policy)
- **Session 1:** Peloton 10-Ks + WHOOP Pitchbook + Oura Pitchbook (~9 hrs)
- **Session 2:** Dexcom 10-K + comp multiples pull + WHOOP cap table (~9 hrs)
- **Session 3:** Forge/EquityZen + Damodaran + pricing history + remaining 10-Ks + precedent M&A (~9 hrs)
- **Gap closure:** Review FLAGGED_GAPs, finalize research findings summary

### Model Construction (after research)
1. Excel DCF build from research outputs
2. Cap table + waterfall model
3. Comps + precedent transactions workbook
4. Football field synthesis + sensitivity tables

### Key Analytical Moves to Execute
- Dual back-solve (naive vs. growth-adjusted) on Series G implied bucket weights
- Three-stage discount framework ($10.1B → $11.2B IPO → $13-15B public fair value)
- Peloton S&M/revenue overlay chart as bear-case anchor
- Churn × ARPU sensitivity grid (WHOOP-specific unit economics)
- Top-down P&L vs. bottoms-up cohort model validation

---

## Living Document Note

This file is the persistent memory for the project. Update it as:
- Thesis evolves based on new data
- Open questions get answered
- Deliverables get completed
- Assumptions get sourced and locked

Every Claude Code session loads this automatically. Keep it current.
