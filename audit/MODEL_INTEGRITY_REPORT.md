# WHOOP Model — Integrity Audit Report

**File audited:** `/home/user/whoop_val/new-whoop-model .xlsx` (read-only)
**Audit date:** 2026-05-10
**Active scenario in workbook:** Base (`Assumptions!B3 = "Base"`)
**Cached values present:** Yes — using `data_only=True`. No "uncached" cells encountered for the headline outputs below; static Bear/Bull EVs are stored as hard values in the DCF triangulation block (`DCF!B60:F65`) per the model's documented "snapshot refresh" pattern.

---

## 1. Headline Outputs (source-of-truth ledger)

### 1a. DCF Equity by Scenario — pulled from `DCF!C60:E63` triangulation snapshot

| Scenario | DCF EV ($M) | Equity ($M) | Equity + Real Opts ($M) | Real Opt Active ($M) | vs Series G | WACC | Source |
|---|---:|---:|---:|---:|---:|---:|---|
| Bear | 2,055.85 | 2,504.21 | 2,657.50 | 153.29 | -75.2% | 12.176% | `DCF!B60:F60`, `Assumptions!C74` |
| Base | 6,616.64 | 7,336.16 | 8,276.25 | 940.09 | -27.4% | 11.587% | `DCF!B61:F61`, `Assumptions!D74` |
| Bull | 18,877.82 | 19,882.00 | 22,596.33 | 2,714.32 | +123.7% | 11.004% | `DCF!B62:F62`, `Assumptions!E74` |
| ProbWeighted (input-level, 20/50/30) | 7,362.36 | 8,090.59 | 9,030.68 | 940.09 | -19.9% | 11.530% | `DCF!B63:F63`, `Assumptions!J74` |

> Live recompute (`DCF!C32` = 6,749.00, `C38` = 7,476.63) is slightly higher than the Base snapshot in `C61` (7,336.16). Snapshot is dated; live numbers should be re-snapped before final publication. **Δ = $140M (-1.9%) on Base equity.**

### 1b. Scenario-Weighted (P·DCF) — `Scenarios!E16:F18`

| Weight scheme | P_Bear / P_Base / P_Bull | Scenario-Wtd Equity ($M) | ProbWeighted Equity ($M) | Jensen Gap ($M) | vs Series G |
|---|---|---:|---:|---:|---:|
| Pessimistic | 35 / 50 / 15 | 7,526.85 | 6,730.53 | 796.32 | -25.5% |
| Neutral (Base) | 20 / 50 / 30 | 10,133.52 | 8,090.59 | 2,042.93 | +0.3% |
| Optimistic | 15 / 45 / 40 | 11,629.70 | 8,593.37 | 3,036.33 | +15.1% |

### 1c. Football Field Weighted Average — `Football Field!I6:J14`

Method weights (live, `Football Field!I6/I10/I13/I14`): DCF 40% / Comps 35% / Series G 10% / IPO Range 15%. Weighted base EV = **$7.107B** (`D18`); weighted base $/share = **$19.02** (`G18`). Premium/(discount) to Series G = **-29.6%** (`D20`).

### 1d. Real Options — `RealOptions!B31:D31` and `B36`

| | Bear | Base | Bull | Active (Base) | Scenario-wtd 20/50/30 |
|---|---:|---:|---:|---:|---:|
| Expected option value ($M) | 164.16 | 940.09 | 2,833.65 | 940.09 | 1,352.97 (`B38`) |

### 1e. 2025 / 2033 Revenue, Members, ARPU

| Metric | Bear | Base | Bull | Source |
|---|---:|---:|---:|---|
| 2025 recognized revenue ($M) | 513 | 528.20 | 646 | `Assumptions!C12:E12` (live: `Revenue Build!D20` = 528.20) |
| 2033 ending members (M) | 7.500 | 10.924 | 18.107 | `Assumptions!C176:E176` |
| 2033 revenue ($M) | n/a (snapshot only) | 3,739.89 | n/a (snapshot only) | `Revenue Build!K20` (Base only — Bear/Bull aren't recomputed live) |
| 2033 ARPU ($/yr) | n/a | 352.16 | n/a | `ARPU!K10` (Base only) |
| WACC (active) | 12.176% | 11.587% | 11.004% | `Assumptions!C74:E74` |

> The model recomputes one scenario at a time (driven by `Assumptions!B3`). 2033 revenue/ARPU for Bear/Bull are not present as live cells; only the Bear/Bull DCF EV snapshots in `DCF!B60:F62` exist as static values.

---

## 2. Integrity Checks

| # | Check | Scenario | Expected | Actual | Pass/Fail | Severity | Suggested fix |
|---|---|---|---:|---:|---|---|---|
| 1 | Avg Members × ARPU = Revenue (2025) | Base | within ±5% | **0.00%** | PASS | — | Identity holds by construction (`Revenue Build!D20 = D13 × D17`) |
| 1 | Avg Members × ARPU = Revenue (2026-33) | Base | within ±5% | **0.00%** every year | PASS | — | — |
| 2 | TV / Total EV | Base | < 75% | **72.95%** (`DCF!C27`) | PASS | — | Just inside threshold; bull/lower-WACC versions could exceed. Header at `DCF!A3` already flags 78% under previous calibration |
| 3 | Exit-multiple TV vs Gordon Growth divergence | Base | < 25% | **33.65%** (`DCF!C24`) | **FAIL** | High | Exit-mult TV $13,090M vs Gordon $9,319M. Drop terminal multiple to ~2.7x for parity, or raise terminal `g` from 3% toward 4%, or accept as bull-bias (Checks!D9 already flags WARN). Calibration log `CalibrationLog!D5` recommends lowering exit mult to 3.0x |
| 4 | 5yr vs 8yr forecast PVs | Base | 7yr-over-5yr ≤ +30% on EV | model only computes 8yr horizon | INCONCLUSIVE | Med | Model lacks an explicit 5yr-DCF cell. PV of 2026-30 FCFs = $868M; PV of 2026-33 FCFs = $1,826M (110% larger), but TV is computed only at year-8. Without a 5yr-TV variant in the workbook, the methodology check can't be run. Add a parallel 5yr DCF block |
| 5 | S&M ≥ Gross adds × Variable CAC + Brand | Base | total ≥ var + brand | **Identity (Δ = 0)** every year (`Members!46 = 53 + 54`) | PASS | — | By construction — `P&L!23` reads `Members!46` directly |
| 6 | Cohort vintages reconcile to ending | Base | exact | **Y1surv + Y3+end + GA = Ending exactly** all years 2025-2033 (Δ ≤ 1e-6) | PASS | — | Model uses non-standard convention: Y2 survivors are absorbed into Y3+ end (`Members!E28 = E12 - E22 + E27`). Initial naive sum (Y1+Y2+Y3+GA) over-counts Y2 by ~0.9-1.5M/yr — flag for memo readers. 2024 historical row mis-sums by 0.13M because hardcoded |
| 7 | Cap-table waterfall = 100% at each exit scenario | n/a | 100% | **NOT BUILT** | **FAIL** | High | `Cap Table!A26:N35` are stub labels only — every value cell from "Total Exit Proceeds" through "Founder Equity Value" is empty. Build the waterfall before any deck claim about preferred-vs-common economics |
| 8 | Rule of 40 by Phase 3 (2031-2033) | Base | ≥ 20 | 2031 = 33.3, 2032 = 31.8, 2033 = 30.8 (`FCF!J22:L22`) | PASS | — | All three years comfortably above the Base ≥ 20 threshold; well below the methodology ceiling 50 |
| 8 | Rule of 40 by Phase 3 | Bull | ≥ 40 | not in workbook (Bull DCF is static snapshot) | INCONCLUSIVE | Low | Toggle `B3` to Bull and capture L22 once before final publication |
| 9 | Bucket weights sum = 100% | All | 100% | 100% (`Checks!B7`) | PASS | — | — |
| 10 | Real-options probability sums = 100% | All | 100% | 100% (`Checks!B10`) | PASS | — | Binary gate, by construction |
| 11 | WACC > Gordon `g` | Base | > 0pp (safer >3pp) | **7.84pp** (`Checks!B11`) | PASS | — | — |
| 12 | Gross-adds peak < 2× base year | Base | < 2.0× | **1.65×** (`Checks!B12`, peaks 2030 vs 2025) | PASS | — | — |
| 13 | Rule of 40 ≤ 50 sustained | Base | terminal ≤ 50 | max 44.10 (`Checks!B15`) | PASS | — | — |
| 14 | ProbWeighted weights sum = 100% | n/a | 100% | 100% (`Checks!B16`) | PASS | — | — |
| 15 | ARPU justification consistency | n/a | ✓ | **#REF!** (`Checks!B14`, `D14`) | **FAIL** | Low | Broken link, downstream of Member Thesis rebuild. Repair the cell formula or remove the row |

---

## 3. Known Issues from HTML §VI — Status

### F179 #DIV/0! at Assumptions (Member Thesis triangulation)
- **HTML claim:** F179 #DIV/0! is a known artifact of Member Thesis rebuild, doesn't affect downstream valuation but should be cleaned for cleanliness.
- **Current state:** F177 (the actual MG_triang formula, NOT F179 — `F179` is now empty/ documentation) reads `=(F176-'Member Thesis'!B20)/'Member Thesis'!B20` and resolves cleanly to **0.000636** (`Assumptions!F177`). Member Thesis B20 = 10.917, populated and not blank. **Issue is FIXED**, not preserved as the HTML and `Claude Log!F4` claim.
- **However**, three new errors have appeared in the same neighborhood:
  - `Assumptions!J174` = #REF! (Bull MG8 ProbWeighted column)
  - `Assumptions!E235`, `F235`, `I235`, `K235` = #REF! (MG8 — 2033 YoY tornado row)
  - `Checks!B14` = #REF!, `D14` = #REF! (ARPU justification consistency)
- **Recommended action:** Repair the broken ProbWeighted ref for MG8 in `J174` — likely the ProbWeighted formula was deleted and never replaced when J235 was wired. Cascade to E235/F235/I235/K235.

### ProbWeighted WACC bypass (J74/J75)
- **HTML claim:** "Earlier model state had WACC under ProbWeighted scenario silently falling through to Base. Fix was implemented (J74/J75 ProbWeighted formulas plus Active formula updates)."
- **Current state:** `Assumptions!F74` formula = `=IF($B$3="Bear",C74,IF($B$3="Bull",E74,IF($B$3="ProbWeighted",J74,D74)))`. J74 = 11.530%, distinct from Base's 11.587%. **Bypass is fixed and live.** When `B3` toggles to ProbWeighted, DCF picks up J74 not D74. Verified: ProbWeighted scenario in `DCF!C63` reflects the J74 WACC.
- **Subtle cousin issue still present:** `Assumptions!F73` (Implied CoE / "Damodaran sector approach", the legacy WACC) formula is `=IF($B$3="Bear",C73,IF($B$3="Bull",E73,D73))` — **NO ProbWeighted branch**. F73 falls through to Base under ProbWeighted. F73 isn't read by DCF (DCF reads F74), so this is cosmetic, but future maintainers may misread. Recommend adding `IF($B$3="ProbWeighted",J73,D73)` for consistency.

### Real-options exhibit member counts
- **HTML claim:** Should reflect 18M Bull endpoint, not older 16.7M.
- **Current state:** `RealOptions!D13` = 18.1067M, sourced live from `Assumptions!E176`. **Match confirmed; FIXED.**

### Bull terminal multiple recalibration (4.5x → 4.0x with 35/40/25 weighting)
- **HTML claim:** Current 4.5x with 60% bucket-3 weight; revenue mix (35/40/25) implies 4.0x; HTML estimates $1-2B reduction in Bull DCF.
- **Current state:** `Assumptions!E77` = **4.5x** (unchanged). `C84:E86` bucket weights still 40/40/20 / 20/40/40 / **10/30/60** — Bull at 60% bucket-3, not the 35/40/25 proposed in HTML §VI item 1.
- **Impact magnitude:** Bull TV uses 4.5× × 2033 revenue. At ~$5,500-6,000M Bull 2033 revenue (estimate, as Bull isn't computed live), dropping 4.5x → 4.0x would shave ~$2.5-3B off undiscounted TV. After ~5pp WACC discount factor (~0.45) over 8 years, PV impact ≈ **$1.1-1.4B reduction in Bull DCF**. Aligned with the HTML's $1-2B estimate.
- **Recommended action:** Decision pending — recalibrate to match revenue mix, or document the override (60% bucket-3 captures "healthcare success" composition under Bull thesis even when revenue mix is 35% payer-paid). Either way, memo should disclose the choice.

---

## 4. Surprises (not in the brief)

1. **Cap Table waterfall is a stub.** The "5. Cap Table" tab has no waterfall logic past row 25 — every "Common Value per Share / Preferred Value per Share / Founder Equity Value" cell is empty. Any deck or memo claim about preferred-stack economics (especially in the Bear $5B scenario where 1x non-participating preferences bite hardest) is currently unsupported by the model.

2. **2024 cohort row doesn't reconcile.** `Members!C9:C34` is hardcoded historical seed data; `Y1surv + Y3+end + GA = 1.289` vs `Ending = 1.1615` (Δ +0.13M). Doesn't affect forecast but a pedantic reviewer will spot it.

3. **Snapshot drift between live model and DCF triangulation block.** Live `DCF!C32` = $6,749M (Base EV). Snapshot at `DCF!B61` = $6,617M. Δ = $132M (+2%). The triangulation block (rows 60-65), Cover, Memo, Scenarios, and Football Field all read the SNAPSHOT, not the live model. Toggle `B3` and the snapshot does not refresh. Refresh protocol documented at `Assumptions!A205`. Before publication: snap once with current inputs.

4. **Bull/Bear DCFs aren't computed live anywhere.** They exist only as $-values in `DCF!B60:F62`. Any sensitivity that requires recomputing Bull (e.g., the recalibrated 4.0x terminal mult) requires manually toggling `B3 = Bull`, capturing the result, and pasting it back into the snapshot block. There is no formula that recomputes Bull in parallel with Base.

5. **Three of the 12 listed "Checks" are incomplete:** Check 5 (Exit/Gordon) is WARN, Check 10 (ARPU justification) is #REF!. Cover summary `B54:B57` reads 10 PASS / 1 WARN / 0 FAIL → "WARN" overall, but actually one check is a literal #REF! error and one is a stub from a Member Thesis rebuild that was never finished.

6. **F179 status differs from HTML.** HTML §VI item 2 and `Claude Log!F4` both describe F179 as a preserved-known-bug (#DIV/0!). It is NOT present in the workbook — F177 is the active formula, F179 contains documentation text. The audit trail in `Claude Log` is stale on this point.

7. **5-year DCF cross-check from methodology Sec 4 is not in the model.** The 7yr-vs-5yr divergence test is one of the methodology's stated integrity checks but the workbook only computes the 8yr horizon. Adding a parallel 5yr DCF block would close the gap.

8. **Methodology mismatch on cohort identity.** Reading `Members!E26-E28` literally, Y2 survivors are **double-counted** if a reader sums all three vintages — they're already absorbed into the Y3+ end-state row by formula `=E12-E22+E27`. The convention works mathematically but is non-obvious. Add a comment at `A28` or `A33`.

9. **CalibrationLog (`D5`, `D6`) shows historical TV/EV ratios at 85% and divergence at 55%.** The current 73% and 34% represent material progress (TV% now passes; divergence still fails but by half the prior gap). The header at `DCF!A3` reflects post-fix state. Calibration log should be updated to RESOLVED.

---

## 5. Recommended Pre-Publication Fixes (priority order)

| Pri | Item | Owner action |
|---|---|---|
| P0 | Build cap-table waterfall (`Cap Table!C28:H35`) | Required for any preferred-economics claim |
| P0 | Fix `Assumptions!J174` (#REF! in Bull MG8 ProbWeighted) and cascade to `E235/F235/I235/K235`, `Checks!B14/D14` | Removes #REF! from Cover/Checks |
| P1 | Decision: recalibrate Bull terminal multiple 4.5x → 4.0x (or document override) | $1-2B impact on Bull DCF; affects football field |
| P1 | Refresh DCF snapshot block (`B60:F65`) so live Base recompute matches | $132M drift currently |
| P1 | Resolve TV-method divergence (33.65% vs 25% threshold) | Either lower exit mult or raise `g`, or accept and document |
| P2 | Add 5yr-DCF parallel block for methodology Sec 4 cross-check | Close stated-but-missing integrity test |
| P2 | Add ProbWeighted branch to F73 formula for cosmetic consistency | One-line fix |
| P3 | Annotate `Members!A33` to flag Y2 absorption into Y3+ row | Prevent reviewer confusion |
| P3 | Update `Claude Log!F4` to reflect F179 fix and other state changes | Audit-trail hygiene |
