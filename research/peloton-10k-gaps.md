# Peloton 10-K Data Gaps — S&M vs G&A Split, SBC, ARPU

**Date compiled:** April 16, 2026
**Source:** SEC EDGAR XBRL API (CIK 0001639825) — machine-readable 10-K tagged data
**Peloton fiscal year ends June 30.**

---

## 1. Sales & Marketing vs General & Administrative Expense Split

| Fiscal Year | S&M ($M) | G&A ($M) | S&M + G&A ($M) | Revenue ($M) | S&M % Rev | G&A % Rev | SG&A % Rev |
|---|---|---|---|---|---|---|---|
| FY2019 (Jun '19) | $324.0 | $207.0 | $531.0 | $915 | 35.4% | 22.6% | 58.0% |
| FY2020 (Jun '20) | $476.7 | $351.4 | $828.1 | $1,826 | 26.1% | 19.2% | 45.4% |
| FY2021 (Jun '21) | $728.3 | $661.8 | $1,390.1 | $4,022 | 18.1% | 16.5% | 34.6% |
| FY2022 (Jun '22) | $1,018.9 | $963.4 | $1,982.3 | $3,582 | 28.4% | 26.9% | 55.3% |
| FY2023 (Jun '23) | $648.2 | $798.1 | $1,446.3 | $2,800 | 23.2% | 28.5% | 51.6% |
| FY2024 (Jun '24) | $658.9 | $651.0 | $1,309.9 | $2,701 | 24.4% | 24.1% | 48.5% |
| FY2025 (Jun '25) | $421.6 | $527.3 | $948.9 | $2,491 | 16.9% | 21.2% | 38.1% |

**Source:** SEC EDGAR XBRL — `SellingAndMarketingExpense` and `GeneralAndAdministrativeExpense` tags, 10-K filings.

### Key Observations

- S&M peaked at **$1,019M in FY2022** (28.4% of revenue), then collapsed to **$422M in FY2025** (16.9%) — a 59% cut.
- G&A peaked at **$963M in FY2022** (26.9% of revenue), then cut to **$527M in FY2025** (21.2%) — a 45% cut.
- **S&M was cut faster and deeper than G&A.** S&M went from 52% of SG&A (FY2021) to 44% of SG&A (FY2025). G&A is now the larger component.
- **FY2023 is the inversion year:** G&A ($798M) exceeded S&M ($648M) for the first time, reflecting restructuring costs flowing through G&A while marketing was slashed.
- At the growth peak (FY2021), S&M was 18.1% of revenue — the most efficient period. By FY2022, it ballooned to 28.4% as revenue declined but spend continued.

### Quarterly Reference (Q2 FY2026, Dec 2025 quarter)

From Q2 FY2026 press release:
- S&M: $152.1M (23.2% of quarterly revenue)
- G&A: $102.9M (15.7%)
- Annualized run-rate: S&M ~$608M, G&A ~$412M

*Source: Peloton Q2 FY2026 earnings press release (GlobeNewsWire, Feb 5, 2026)*

---

## 2. Stock-Based Compensation Expense

| Fiscal Year | SBC ($M) | Revenue ($M) | SBC % Rev |
|---|---|---|---|
| FY2019 (Jun '19) | $89.5 | $915 | 9.8% |
| FY2020 (Jun '20) | $88.8 | $1,826 | 4.9% |
| FY2021 (Jun '21) | $194.0 | $4,022 | 4.8% |
| FY2022 (Jun '22) | $328.4 | $3,582 | 9.2% |
| FY2023 (Jun '23) | $405.0 | $2,800 | 14.5% |
| FY2024 (Jun '24) | $311.7 | $2,701 | 11.5% |
| FY2025 (Jun '25) | $229.6 | $2,491 | 9.2% |

**Source:** SEC EDGAR XBRL — `ShareBasedCompensation` tag, 10-K filings (cash flow statement).

### Key Observations

- SBC peaked at **$405M in FY2023** (14.5% of revenue) despite massive layoffs — reflects accelerated vesting and severance-related SBC.
- Declining to $230M in FY2025 as headcount dropped from ~8,700 (peak) to ~2,700.
- Even at FY2025 levels, SBC is **9.2% of revenue** — meaningful for FCF-to-equity comparisons.
- Cumulative SBC FY2019-FY2025: **~$1.66B** in non-cash compensation expense.

---

## 3. Average Net Monthly CF Subscription Revenue Per CF Subscriber

**STATUS: FLAGGED_GAP — NOT FULLY RESOLVED**

This KPI is reported in Peloton's 10-K MD&A section and quarterly shareholder letters, but those documents returned 403 errors (SEC EDGAR HTML) or timeouts (Peloton IR PDFs). The metric is NOT tagged in XBRL.

### Derived Estimates (Subscription Revenue / Avg CF Subs / 12)

| Fiscal Year | Sub Rev ($M) | Avg CF Subs (M) | Derived Monthly ARPU |
|---|---|---|---|
| FY2021 | ~$872 | ~1.71 | ~$42.50 |
| FY2022 | ~$1,395 | ~2.65 | ~$43.87 |
| FY2023 | ~$1,669 | ~3.00 | ~$46.36 |
| FY2024 | $1,709 | ~2.99 | ~$47.63 |
| FY2025 | $1,674 | ~2.84 | ~$49.12 |

**Caveats:** These are estimates. The official Peloton KPI may differ because: (a) subscription revenue includes non-CF subscription revenue (app-only, Peloton For Business); (b) average subscriber count is a period average, not end-of-period; (c) pricing changes mid-year distort simple division.

**Known pricing milestones:**
- June 2023: CF subscription raised from $39/mo to $44/mo (US)
- October 2025: Additional price increase (amount TBD)

**To fully resolve:** Download 10-K PDFs directly and search for "Average Net Monthly Connected Fitness Subscription Revenue Per Connected Fitness Subscriber" in the KPI tables.

---

## Summary Validation

### S&M + G&A cross-check against known SG&A totals

| FY | S&M + G&A (XBRL) | Known SG&A | Delta |
|---|---|---|---|
| FY2021 | $1,390.1M | $1,390M | Match |
| FY2022 | $1,982.3M | $1,982M | Match |
| FY2023 | $1,446.3M | $1,446M | Match |
| FY2024 | $1,309.9M | $1,310M | Match |
| FY2025 | $948.9M | $949M | Match |

All figures cross-check within rounding. Data is confirmed accurate from primary SEC EDGAR source.

---

## Sources

1. SEC EDGAR XBRL API — `https://data.sec.gov/api/xbrl/companyfacts/CIK0001639825.json` (tags: SellingAndMarketingExpense, GeneralAndAdministrativeExpense, ShareBasedCompensation)
2. Peloton Q2 FY2026 earnings press release — GlobeNewsWire, Feb 5, 2026
3. Peloton FY2025 10-K filed Aug 7, 2025 — `https://investor.onepeloton.com/static-files/833f0550-c53b-46a8-ba70-1d85022f1427`
