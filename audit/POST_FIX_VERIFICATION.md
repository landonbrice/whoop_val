# WHOOP Model — Post-Fix Verification Report

**Audit date:** 2026-05-10
**Live model:** `new-whoop-model .xlsx`
**Edit method:** Direct XML manipulation (chart files preserved; openpyxl drops them on round-trip)
**Snapshot block:** Refreshed for all four scenarios (Bear/Base/Bull/ProbWeighted)

---

## 1. Headline outputs — pre-fix vs post-fix vs HTML target

| Output | Pre-fix | Post-fix | Δ | HTML target | Notes |
|---|---:|---:|---:|---:|---|
| Bear DCF Equity | $2,504M | **$2,547M** | +$43M | $2,500M | Match |
| Base DCF Equity | $7,336M | **$7,827M** | +$491M | $7,300M | WACC fix lifted |
| Bull DCF Equity | $19,882M | **$28,428M** | **+$8,546M** | $19,880M | **HTML target was based on buggy Bull MG** |
| ProbWeighted Equity | $8,091M | $8,798M | +$707M | n/a | |
| Scenario-Wtd Pessimistic 35/50/15 | $7,527M | $9,069M | +$1,542M | $7,500M | |
| **Scenario-Wtd Neutral 20/50/30** | $10,134M | **$12,951M** | +$2,817M | $11,200M | **+15.6% above HTML target** |
| Scenario-Wtd Optimistic 15/45/40 | $11,630M | $15,275M | +$3,645M | $13,000M | |
| **Football Field weighted avg** | $7,107M | **$9,335M** | +$2,228M | $8,630M | **+8.2% above HTML target** |
| **Intrinsic alone (= Scenario-Wtd Neutral)** | $10,134M | **$12,951M** | +$2,817M | $11,200M | |
| **Premium to Series G — intrinsic alone** | +0.3% | **+28.2%** | +27.9pp | +11% | **Underpricing thesis stronger than HTML** |
| **Premium to Series G — FF weighted avg** | -29.6% | **-7.6%** | +22.0pp | -14.5% | |

---

## 2. WACC verification

| Cell | Pre-fix | Post-fix | HTML target |
|---|---:|---:|---:|
| Assumptions!F73 (Damodaran Base) | 10.85% | 10.85% | 10.85% |
| Assumptions!F74 (bottoms-up Base) | 11.59% | 11.59% | n/a |
| Assumptions!J73 (ProbWeighted, NEW) | n/a | 10.74% | n/a |
| **DCF!D12 (live WACC used by DCF)** | **11.59%** | **10.85%** | **10.85%** |

Bull WACC dropped from 11.00% → 9.755% (Damodaran Bull) — this contributed roughly half of the Bull DCF jump. The other half is the Bull MG fix unblocking late-year growth (2031/2032/2033 now use 13%/9%/7% instead of 9%/7%/error).

---

## 3. Football Field row contributions (post-fix)

| Row | Method | Base ($B) | Weight | Contribution ($B) |
|---|---|---:|---:|---:|
| 6 | 1. Intrinsic DCF (base case, no options) | 7.827 | 0% | 0.000 |
| 9 | **1d. Scenario-Weighted DCF (P·DCF)** | **12.951** | **40%** | **5.180** |
| 10 | 2. Public Comps (three-thesis) | 3.573 | 35% | 1.250 |
| 13 | 4. Last-Round Implied (Series G) | 10.100 | 10% | 1.010 |
| 14 | 5. Implied IPO Trading Range | 12.625 | 15% | 1.894 |
| 18 | **Weighted Average EV** | | | **9.335** |
| 20 | Premium / (Discount) to Series G | | | **-7.58%** |

Weight migrated from row 6 (base-case-only DCF) to row 9 (scenario-weighted DCF) per HTML §III.

---

## 4. Integrity checks (post-fix)

| # | Check | Pre-fix | Post-fix | Threshold | Status |
|---|---|---:|---:|---|---|
| 4 | TV / Total EV (Base) | 72.95% | 74.28% | <75% PASS | **PASS** |
| 5 | TV exit-mult vs Gordon divergence (Base) | 33.65% | **25.79%** | <25% PASS, <35% WARN | **WARN** (was FAIL) |
| 10 | ARPU justification (Checks!B14) | #REF! | '✓' → 'PASS' | ✓ → PASS | **PASS** |
| Stray #REF! (E235/F235/I235/K235/J174) | #REF! | clean | n/a | **resolved** |

The TV divergence improved from 33.65% → 25.79% — just barely WARN. This is because the lower WACC lifted Gordon TV more than exit-mult TV. With user's "accept and document" decision, this is logged as a known WARN with the explanation that exit-multiple TV reflects bucket-weighted comp medians (justified by business mix) while Gordon TV anchors on perpetuity growth (3% terminal); the gap narrowed but is structurally inherent to the bull-tilt of bucket-3 weighting at terminal.

---

## 5. Key revenue / member / ARPU values (post-fix, Base scenario)

| Metric | Pre-fix | Post-fix | HTML target |
|---|---:|---:|---:|
| FY25 revenue ($M) | 528 | **520.6** | 520 |
| FY33 revenue ($M, Base) | 3,740 | 3,686 | n/a |
| 2025 ARPU ($) | 278 | **274** | 274 |
| 2033 ARPU ($, Base) | 352 | 347 | 347 |
| 2033 ending members (M, Base) | 10.92 | 10.92 | 10.9 |
| **Bull 2033 ending members (M)** | 18.107 | 18.107 | 18.0 |

Note: model produces 18.107M Bull endpoint with the canonical 70/55/38/27/19/13/9/7 sequence; HTML rounded to 18.0M.

---

## 6. Charts preserved

16 chart support files preserved through the XML-level fix (openpyxl drops them on round-trip; direct XML editing does not). Pre-fix and post-fix file structures match for all chart-related XMLs.

---

## 7. Critical Finding — Bull DCF Re-Anchor

**The HTML's stated headlines ($11.2B intrinsic, +11% premium, $8.63B weighted avg) were calibrated to a model state with two latent bugs:**
1. Bull MG sequence used off-by-one growth-rate references for 2031/2032/2033 — Bull was actually growing at 9%/7%/error in those years instead of intended 13%/9%/7%
2. DCF was reading the bottoms-up WACC (11.59% Base) instead of the Damodaran build (10.85% Base)

With both bugs fixed, the model produces:
- **Intrinsic alone $12.95B vs Series G $10.10B = +28% premium** (HTML claimed +11%)
- **Football Field weighted avg $9.34B vs Series G = -7.6%** (HTML claimed -14.5%)
- **Bull DCF $28.4B vs HTML's $19.9B target**

**Implication:** The "Series G mildly underpriced" thesis is *stronger*, not weaker, with the bugs fixed. Premium goes from +11% → +28%. The deck and memo should be re-anchored to the post-fix numbers.

---

## 8. Editorial decisions captured

Per user's batch decisions (2026-05-10):
- **Bull terminal multiple:** Kept at 4.5x with 60% bucket-3 weighting (HTML §VI item 1 flagged this as defensible-either-way; user chose to document the override rather than recalibrate to 4.0x at 35/40/25). $1-2B Bull-DCF impact accepted.
- **Cap Table waterfall:** Skipping. Will strip preferred-economics from the deck (slide 11's $0.6B ratchet + $0.4B participation — fabricated, no source in CLAUDE.md research).
- **TV exit-mult vs Gordon divergence:** Accept and document (now WARN at 25.79%, was FAIL at 33.65%).

# WHOOP Model — Phase 3b Addendum: WACC reverted to bottoms-up

**Date:** 2026-05-10 (later same session)
**Decision:** User chose to use the comp-derived bottoms-up WACC (11.59% Base) as the model's live WACC, not Damodaran top-down (10.85% Base). Editorial call — bottoms-up is the more conservative anchor and uses our own per-comp regression work.

## Headlines under bottoms-up WACC

| Output | Pre-WACC-fix (orig) | Phase 3a (Damodaran 10.85%) | Phase 3b (bottoms-up 11.59%) — CURRENT |
|---|---:|---:|---:|
| Bear DCF Equity | $2.50B | $2.55B | **$2.50B** |
| Base DCF Equity | $7.34B | $7.83B | **$7.32B** |
| Bull DCF Equity | $19.88B | $28.43B | **$24.66B** |
| Scenario-Wtd Neutral 20/50/30 | $10.13B | $12.95B | **$11.56B** |
| Scenario-Wtd Pessimistic | $7.53B | $9.07B | **$8.23B** |
| Scenario-Wtd Optimistic | $11.63B | $15.28B | **$13.53B** |
| Input-level Neutral | $8.09B | $8.80B | **$8.19B** |
| Jensen's gap (Neutral) | $2.04B | $4.15B | **$3.37B** |
| FF Weighted Avg | $7.11B | $9.34B | **$8.78B** |
| Premium (intrinsic alone) | +0.3% | +28.2% | **+14.4%** |
| Premium (FF weighted) | -29.6% | -7.6% | **-13.1%** |
| WACC Base | 11.59% | 10.85% | **11.59%** |

## Cell changes from Phase 3a → 3b

- **`DCF!D12:K12`** repointed from `=Assumptions!$F$73` (Damodaran) back to `=Assumptions!$F$74` (bottoms-up).
- **`DCF!B60:F63`** snapshot block refreshed via toggle through 4 scenarios + capture of live recompute via `formulas` library.
- **`Assumptions!B3`** restored to "Base" (canonical default).

The Bull MG fix (off-by-one Bull arms at F172/F173/F174 referencing E173/E174/#REF! instead of E172/E173/E174) is RETAINED from Phase 3a — that fix is mechanical, not subjective, and the user has not reversed it.

## Thesis under bottoms-up

Series G $10.10B is **modestly under-priced at +14.4%** under Neutral conviction (down from +28.2% with Damodaran WACC). The "Series G mildly under-priced" thesis remains; the magnitude is now more conservative and Q&A-defendable. FF weighted average is below Series G by 13.1%, which the deck reframes as the structural mispricing of platform-positioned companies under comp-based methodology.

## Deck status

`Whoop Valuation Master.audited.fast.pptx` rebuilt with 15 slides (was 13):
- Added Slide 5 — DCF Mechanics Build (year-by-year P&L + PV table + EV→Equity bridge)
- Added Slide 6 — WACC Mechanics (per-comp regressed betas, bucket medians, blended β, CAPM build, Damodaran cross-check banner)
- All other slides have headline numbers re-anchored to bottoms-up via JSON-driven build_deck.py

5 visuals regenerated for new numbers: football_field.png, scenario_dispersion.png, jensens_gap.png (tornado.png and funding_timeline.png unchanged).

