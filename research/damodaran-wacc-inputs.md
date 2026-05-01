# WACC Inputs — Damodaran & Market Data

## Date Pulled: April 16, 2026

All Damodaran data as of January 2026 update. Treasury yield as of April 14, 2026.

---

## Risk-Free Rate (D1)

| Source | Date | 10-Year UST Yield |
|--------|------|--------------------|
| Federal Reserve H.15 | April 14, 2026 | **4.26%** |
| CNBC / Trading Economics | April 10, 2026 | 4.31-4.34% |

**Recommended input: 4.30%** (rounded mid-April average; use spot rate at model date)

Note: Following the Moody's US downgrade to Aa1, Damodaran adjusts the risk-free rate by subtracting a 0.23% US default spread from the Treasury yield. His adjusted risk-free rate = 4.26% - 0.23% = ~4.03%. For our purposes, we use the unadjusted Treasury yield as the conventional risk-free rate input, and note the Damodaran adjustment as context.

**Source:** [Federal Reserve H.15 — Selected Interest Rates](https://www.federalreserve.gov/releases/h15/)

---

## Equity Risk Premium (D2)

### Damodaran Implied ERP (FCFE-based)

| Year | Implied ERP |
|------|-------------|
| 2022 | 5.94% |
| 2023 | 4.60% |
| 2024 | 4.33% |
| 2025 (Jan 2026 update) | **4.23%** |

**Damodaran's mature market ERP: 4.23%**

The US-specific ERP on his country premium page is 4.46%, which adds a 0.23% US default spread to the 4.23% mature market base.

### Kroll Recommended ERP

| Date | Kroll Recommended US ERP |
|------|--------------------------|
| February 2025 (most recent public) | **5.0%** |

Kroll lowered from 5.5% to 5.0% in their most recent update. Kroll's ERP is a "conditional" or normalized figure, not a pure implied premium — it tends to be higher than Damodaran's implied calculation.

### Recommended Range

| Approach | ERP |
|----------|-----|
| Damodaran implied (Jan 2026) | 4.23% |
| Damodaran US-specific (incl. default spread) | 4.46% |
| Kroll recommended (Feb 2025) | 5.00% |
| **Recommended for WHOOP model** | **4.5% base case (sensitivity: 4.0% - 5.5%)** |

**Sources:**
- [Damodaran — Historical Implied ERP](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html)
- [Damodaran — Country Risk Premiums](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)
- [Kroll — Recommended US ERP](https://www.kroll.com/en/reports/cost-of-capital/recommended-us-equity-risk-premium-and-corresponding-risk-free-rates) (paywall; 5.0% figure from [BVResources](https://www.bvresources.com/articles/bvwire/kroll-lowers-recommended-us-erp-to-50))

---

## Unlevered Betas by Sector (D3)

### Primary Comp Sectors (January 2026)

| Sector | # Firms | Levered Beta | D/E Ratio | Tax Rate | Unlevered Beta | Bucket Mapping |
|--------|---------|--------------|-----------|----------|----------------|----------------|
| Healthcare Products | 204 | 0.91 | 12.79% | 4.85% | **0.83** | B3: Health data / medical device |
| Healthcare Info & Technology | 115 | 1.11 | 15.74% | 6.38% | **0.99** | B3: Health data platform |
| Electronics (Consumer & Office) | 8 | 0.87 | 5.80% | 0.00% | **0.83** | B1: Consumer hardware |
| Entertainment | 92 | 0.83 | 15.91% | 3.30% | **0.74** | B2: Consumer subscription |
| Recreation | 49 | 1.02 | 62.99% | 11.45% | **0.70** | B1: Consumer hardware (alt) |

### Secondary / Reference Sectors

| Sector | # Firms | Levered Beta | D/E Ratio | Tax Rate | Unlevered Beta | Relevance |
|--------|---------|--------------|-----------|----------|----------------|-----------|
| Software (System & Application) | 309 | 1.28 | 5.58% | 5.51% | **1.23** | SaaS/subscription platform analogy |
| Software (Entertainment) | 77 | 1.03 | 2.04% | 5.29% | **1.01** | Consumer digital subscription |
| Healthcare Support Services | 104 | 0.87 | 35.43% | 9.80% | **0.69** | B2B healthcare services |
| Computers/Peripherals | 36 | 1.35 | 4.62% | 5.91% | **1.31** | Hardware reference |
| Computer Services | 64 | 1.09 | 25.10% | 10.53% | **0.92** | Tech services reference |
| Drugs (Pharmaceutical) | 228 | 0.98 | 14.54% | 2.99% | **0.89** | Healthcare reference |
| Software (Internet) | 29 | 1.69 | 12.30% | 3.05% | **1.55** | High-growth tech reference |
| Information Services | 15 | 0.92 | 33.17% | 18.16% | **0.74** | Data platform reference |

### WHOOP Beta Estimate by Bucket Weighting

WHOOP has no debt, so levered beta = unlevered beta for the company.

| Scenario | B1 Weight | B1 Beta | B2 Weight | B2 Beta | B3 Weight | B3 Beta | Blended Unlevered Beta |
|----------|-----------|---------|-----------|---------|-----------|---------|----------------------|
| Bear (40/40/20) | 40% | 0.83 | 40% | 0.74 | 20% | 0.91 | **0.81** |
| Base (20/40/40) | 20% | 0.83 | 40% | 0.74 | 40% | 0.91 | **0.83** |
| Bull (10/30/60) | 10% | 0.83 | 30% | 0.74 | 60% | 0.91 | **0.85** |

Note: B3 beta uses a blend of Healthcare Products (0.83) and Healthcare Info & Tech (0.99). For the table above, Healthcare Products (0.91 levered / 0.83 unlevered) is used as the primary B3 beta. If we weight B3 as 50/50 Healthcare Products + Healthcare IT, the B3 unlevered beta rises to 0.91, which would push the base-case blended beta to ~0.86.

**FLAG:** The blended betas cluster tightly (0.81-0.85) regardless of scenario. This means bucket weighting has limited beta impact — the valuation spread comes primarily from the *multiple* differences across buckets, not from cost of capital differences. This is a useful finding: it means WACC is relatively stable across scenarios, and the football field width is driven by operating assumptions and multiples, not discount rate disagreements.

**Source:** [Damodaran — Betas by Sector](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)

---

## Size Premium (D4)

### CRSP Decile Classification for WHOOP ($10.1B)

| CRSP Decile | Market Cap Range (approx.) | Size Premium (over CAPM) |
|-------------|---------------------------|--------------------------|
| 1 (Mega-cap) | >$30B+ | -0.35% to 0% |
| 2 | ~$13.5B - $30B | ~0.50% |
| **3** | **~$7.3B - $13.5B** | **~0.81%** |
| 4 | ~$4.5B - $7.3B | ~0.85% |
| 5 | ~$2.5B - $4.5B | ~0.89% |
| 7 | ~$1.3B - $2.0B | ~1.58% |
| 8 | ~$730M - $1.3B | ~1.80% |
| 10 (Micro-cap) | <$250M | ~5-6% |

**WHOOP at $10.1B falls in CRSP Decile 3 (mid-cap, ~$7.3B-$13.5B).**

**Recommended size premium: 0.81%**

However, this is a *public company* size premium. For a private company like WHOOP, additional adjustments apply:

| Adjustment | Premium | Rationale |
|------------|---------|-----------|
| CRSP Decile 3 size premium | 0.81% | Market-cap-based |
| Private company / illiquidity discount | +1.0% to +3.0% | No public market; restricted transferability |
| **Total size + illiquidity premium** | **1.8% to 3.8%** | Range for private company adjustment |

**ESTIMATE — NOT DIRECTLY SOURCED.** The CRSP decile breakpoints and size premia are from 2024 Duff & Phelps / Kroll data (most recent publicly available). The private company premium is a standard practitioner range, not a Kroll-published figure. Kroll's detailed current data requires a paid subscription to the Cost of Capital Navigator.

**Sources:**
- [Kroll Cost of Capital Navigator](https://www.kroll.com/en/tools-and-platforms/cost-of-capital) (subscription required for current data)
- [CRSP Cap-Based Portfolio Breakpoints](https://www.crsp.org/indexes/breakpoints-chart/)
- Duff & Phelps / Kroll Valuation Handbook (2024 edition, [Scribd reference](https://www.scribd.com/document/512214235/Duffphelps))

---

## Country Risk Premium — International Reference

For potential international expansion modeling:

| Country | Moody's Rating | Country Risk Premium | Total ERP |
|---------|----------------|---------------------|-----------|
| United States | Aa1 | 0.23% | 4.46% |
| Germany | Aaa | 0.00% | 4.23% |
| United Kingdom | Aa3 | 0.78% | 5.01% |
| Japan | A1 | 0.91% | 5.14% |
| China | A1 | 0.91% | 5.14% |
| India | Baa3 | 2.85% | 7.08% |
| Brazil | Ba1 | 3.24% | 7.47% |

**Source:** [Damodaran — Country Default Spreads and Risk Premiums (January 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)

---

## Cost of Capital by Sector — Reference Table

| Sector | Cost of Equity | After-tax Cost of Debt | WACC | E/(D+E) | D/(D+E) | Bucket |
|--------|---------------|----------------------|------|---------|---------|--------|
| Electronics (Consumer & Office) | 7.81% | 4.51% | 7.63% | 94.51% | 5.49% | B1 |
| Recreation | 8.51% | 3.97% | 6.76% | 61.35% | 38.65% | B1 |
| Entertainment | 7.63% | 3.97% | 7.13% | 86.27% | 13.73% | B2 |
| Software (Entertainment) | 8.54% | 3.97% | 8.44% | 98.00% | 2.00% | B2 ref |
| Healthcare Products | 8.00% | 3.97% | 7.54% | 88.66% | 11.34% | B3 |
| Healthcare Info & Technology | 8.89% | 3.97% | 8.22% | 86.40% | 13.60% | B3 |
| Healthcare Support Services | 7.84% | 3.97% | 6.83% | 73.84% | 26.16% | B3 ref |
| Software (System & Application) | 9.64% | 3.97% | 9.34% | 94.72% | 5.28% | SaaS ref |
| Computers/Peripherals | 9.97% | 3.97% | 9.71% | 95.58% | 4.42% | HW ref |

**Source:** [Damodaran — Cost of Capital by Sector (January 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html)

---

## Recommended WHOOP WACC Range

### Build-Up Calculation

| Component | Bear | Base | Bull |
|-----------|------|------|------|
| Risk-free rate | 4.30% | 4.30% | 4.30% |
| ERP | 5.00% | 4.50% | 4.23% |
| Unlevered beta | 0.81 | 0.83 | 0.85 |
| Beta x ERP | 4.05% | 3.74% | 3.60% |
| Size premium (Decile 3) | 0.81% | 0.81% | 0.81% |
| Private company premium | 2.50% | 1.50% | 1.00% |
| **Cost of Equity / WACC** | **11.66%** | **10.35%** | **9.71%** |

WHOOP has no debt, so Cost of Equity = WACC.

### Summary

| Scenario | WACC |
|----------|------|
| Bear (higher risk, private discount) | ~11.5-12.0% |
| **Base** | **~10.0-10.5%** |
| Bull (near-IPO, lower private discount) | ~9.5-10.0% |

### Key Judgments Embedded

1. **Private company premium is the biggest swing factor.** At 1.0%-2.5%, it drives more WACC variation than beta or ERP differences. If WHOOP is 12-18 months from IPO (as the Series G signals), the lower end (1.0%) is defensible. If IPO risk is real, 2.0%+ is appropriate.

2. **Beta differences across scenarios are trivial.** The 0.81-0.85 range means bucket weighting barely moves WACC. This is analytically useful: it isolates the valuation debate to multiples and growth assumptions, not discount rates.

3. **Damodaran's sector WACCs (6.8%-9.7%) are for public companies with established capital structures.** WHOOP's all-equity, private, high-growth profile requires meaningful adjustments above these levels.

4. **Do NOT compute DCF math from these inputs in an LLM.** Transfer to Excel model per project conventions.

---

## Sources

- [Federal Reserve H.15 — Selected Interest Rates (April 15, 2026)](https://www.federalreserve.gov/releases/h15/)
- [FRED — 10-Year Treasury Constant Maturity (DGS10)](https://fred.stlouisfed.org/series/DGS10)
- [Damodaran — Historical Implied Equity Risk Premiums](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html)
- [Damodaran — Country Default Spreads and Risk Premiums (January 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)
- [Damodaran — Betas by Sector (January 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
- [Damodaran — Cost of Capital by Sector (January 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html)
- [Damodaran — Valuation Packet (Spring 2026)](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/valpacket1spr26.pdf)
- [Kroll — Recommended US ERP](https://www.kroll.com/en/reports/cost-of-capital/recommended-us-equity-risk-premium-and-corresponding-risk-free-rates)
- [Kroll — Cost of Capital Navigator](https://www.kroll.com/en/tools-and-platforms/cost-of-capital)
- [CRSP — Cap-Based Portfolio Breakpoints](https://www.crsp.org/indexes/breakpoints-chart/)
- [BVResources — Kroll Lowers ERP to 5.0%](https://www.bvresources.com/articles/bvwire/kroll-lowers-recommended-us-erp-to-50)

---

## Data Quality Flags

| Item | Status | Notes |
|------|--------|-------|
| Risk-free rate (D1) | DIRECTLY SOURCED | Fed H.15, April 14, 2026 |
| Damodaran implied ERP (D2) | DIRECTLY SOURCED | Damodaran website, January 2026 |
| Kroll ERP (D2) | DIRECTLY SOURCED | Public announcement, Feb 2025 |
| Unlevered betas (D3) | DIRECTLY SOURCED | Damodaran website, January 2026 |
| Sector WACCs | DIRECTLY SOURCED | Damodaran website, January 2026 |
| CRSP Decile 3 size premium (D4) | ESTIMATED | Based on 2024 Duff & Phelps data; current year may differ slightly |
| CRSP decile breakpoints | ESTIMATED | Approximate; shifts with market conditions |
| Private company premium | ESTIMATED | Practitioner convention, not Kroll-published for WHOOP specifically |
| Country risk premiums | DIRECTLY SOURCED | Damodaran website, January 2026 |
| WHOOP blended beta | DERIVED | Calculated from bucket weights x sector betas |
| WHOOP WACC range | DERIVED | Build-up method from sourced components |
