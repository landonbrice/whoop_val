# 3-Year Weekly Beta Regression — Raw Output

**Date computed:** 2026-05-05
**Sampling window:** 2023-05-01 to 2026-05-05 (157 weekly observations)
**Benchmark:** S&P 500 (^GSPC)
**Method:** Simple weekly returns; OLS regression `r_stock = α + β × r_market + ε`
**Data source:** yfinance (Yahoo Finance historical daily-aggregated to weekly closes, auto-adjusted for splits/dividends)
**Bloomberg adjustment:** β_adj = (2/3) × β_raw + (1/3) × 1.0
**Script:** `scripts/compute_3y_weekly_betas.py`

## Output

| Ticker | n_obs | β_raw | β_adj | R² | Stock annualized vol | Market annualized vol |
|---|---|---|---|---|---|---|
| GRMN | 157 | 1.029 | 1.019 | 0.216 | 31.9% | 14.4% |
| PTON | 157 | 2.283 | 1.855 | 0.185 | 76.5% | 14.4% |
| SPOT | 157 | 1.014 | 1.010 | 0.134 | 39.9% | 14.4% |
| DXCM | 157 | 1.080 | 1.054 | 0.119 | 45.2% | 14.4% |
| RMD | 157 | 0.962 | 0.974 | 0.181 | 32.5% | 14.4% |
| MASI | 157 | 0.885 | 0.924 | 0.090 | 42.5% | 14.4% |
| IRTC | 157 | 0.816 | 0.877 | 0.057 | 49.1% | 14.4% |

## Quality Notes

- **R² generally low (5.7%-21.6%):** Confirms substantial idiosyncratic volatility unexplained by market for all 7 names. IRTC (5.7%) and MASI (9.0%) have especially weak market correlation — beta point estimates have wide standard errors
- **PTON raw 2.28 → adj 1.86:** Bloomberg adjustment pulls high-beta distressed names materially toward 1.0
- **IRTC raw 0.82 → adj 0.88:** Adjustment slightly elevates low-beta names. The drop from the 5Y monthly figure (1.33) is largely because the January 2021 CMS reimbursement crash (-83% over 7 months) is OUTSIDE the 3Y weekly window (window starts May 2023)
- **MASI raw 0.89 → adj 0.92:** Reflects deal-pending compression (stock has traded near $180 Danaher deal price since Feb 2026, dampening recent volatility) AND the operational period 2023-2025 was less volatile than the longer 5Y window suggested
- **SPOT raw 1.01:** Down from 5Y monthly 1.55. Spotify's profitability inflection in 2024 lowered realized volatility relative to the broader market vs. its pre-2024 unprofitable phase
- **DXCM raw 1.08:** Down from 5Y monthly 1.40. The July 2024 40% one-day drop is in window but diluted across 157 weekly obs

## Re-run Instructions

```bash
cd /Users/landonprojects/whoop_val
.venv-beta/bin/python scripts/compute_3y_weekly_betas.py
```

Update END date in `scripts/compute_3y_weekly_betas.py` to refresh as of a different valuation date.
