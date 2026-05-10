"""
Compute 3-year weekly regression betas for WHOOP comp set.

Methodology:
- 156 weekly returns (3 years x 52) ending May 5, 2026
- Friday-to-Friday weekly closes (yfinance interval='1wk')
- Simple returns: r_t = (P_t / P_{t-1}) - 1
- Regression: r_stock = alpha + beta * r_market + epsilon
- Benchmark: S&P 500 (^GSPC) for all comps (primary listings)
- Bloomberg-adjusted beta: beta_adj = (2/3) * beta_raw + (1/3) * 1.0
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

TICKERS = ["GRMN", "PTON", "SPOT", "DXCM", "RMD", "MASI", "IRTC"]
BENCHMARK = "^GSPC"
END = "2026-05-05"
START = "2023-05-01"  # ~3 years back; will trim to 156 weekly obs

def fetch_weekly(ticker, start, end):
    df = yf.download(
        ticker, start=start, end=end, interval="1wk",
        auto_adjust=True, progress=False, threads=False
    )
    if df.empty:
        return None
    # Use Adj Close (which is Close after auto_adjust=True)
    close = df["Close"].squeeze() if "Close" in df.columns else df.iloc[:, 0]
    return close.dropna()

def compute_beta(stock_ret, mkt_ret):
    # Align dates
    df = pd.concat([stock_ret, mkt_ret], axis=1).dropna()
    df.columns = ["stock", "mkt"]
    if len(df) < 50:
        return None
    cov = df["stock"].cov(df["mkt"])
    var = df["mkt"].var()
    beta_raw = cov / var
    # Adjusted
    beta_adj = (2/3) * beta_raw + (1/3) * 1.0
    # R-squared
    corr = df["stock"].corr(df["mkt"])
    r2 = corr ** 2
    return {
        "n_obs": len(df),
        "beta_raw": beta_raw,
        "beta_adj": beta_adj,
        "r2": r2,
        "stock_vol": df["stock"].std() * np.sqrt(52),
        "mkt_vol": df["mkt"].std() * np.sqrt(52),
    }

def main():
    print(f"Computing 3Y weekly betas as of {END}")
    print(f"Sampling window: {START} to {END}")
    print()

    # Pull benchmark
    mkt_close = fetch_weekly(BENCHMARK, START, END)
    if mkt_close is None:
        print("ERROR: Could not fetch benchmark")
        return
    mkt_ret = mkt_close.pct_change().dropna()
    print(f"S&P 500 benchmark: {len(mkt_ret)} weekly returns")
    print()

    results = []
    for ticker in TICKERS:
        close = fetch_weekly(ticker, START, END)
        if close is None or close.empty:
            print(f"{ticker}: NO DATA")
            results.append({"ticker": ticker, "error": "no data"})
            continue
        stock_ret = close.pct_change().dropna()
        out = compute_beta(stock_ret, mkt_ret)
        if out is None:
            print(f"{ticker}: insufficient data")
            results.append({"ticker": ticker, "error": "insufficient"})
            continue
        out["ticker"] = ticker
        results.append(out)
        print(
            f"{ticker:6s} | n={out['n_obs']:3d} | β_raw={out['beta_raw']:.3f} | "
            f"β_adj={out['beta_adj']:.3f} | R²={out['r2']:.3f} | "
            f"σ_stock={out['stock_vol']*100:.1f}% | σ_mkt={out['mkt_vol']*100:.1f}%"
        )

    print()
    print("=" * 80)
    print("SUMMARY TABLE (3Y weekly regression vs S&P 500)")
    print("=" * 80)
    df = pd.DataFrame(results)
    if "error" in df.columns:
        df = df[df["error"].isna() if "error" in df.columns else slice(None)]
    print(df[["ticker", "n_obs", "beta_raw", "beta_adj", "r2"]].to_string(index=False))

if __name__ == "__main__":
    main()
