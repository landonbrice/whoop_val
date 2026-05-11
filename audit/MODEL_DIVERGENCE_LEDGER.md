# WHOOP Master Model — Divergence Ledger vs. Whoop Master.html

Audit date: 2026-05-10. Workbook: `/home/user/whoop_val/new-whoop-model .xlsx`. Read-only.
HTML truth document: `/home/user/whoop_val/Whoop Master.html`.

---

## Tab Inventory

| Tab | Purpose (1-line) |
|---|---|
| `Claude Log` | Session changelog of architectural moves (real-options redesign, ProbWeighted rebalance, etc.) |
| `Cover` | Title page; live snapshot of headline EV/equity numbers from DCF |
| `Memo` | Memo-ready visuals: scenario table, waterfall, tornado, football field, heatmap, Jensen triangulation |
| `Assumptions` | Master input registry; all Bear/Base/Bull/Active/ProbWeighted columns; 14 numbered sections |
| `Member Thesis` | Four-lens triangulation (TAM, Peloton stage-shift, Comps Apple/Oura/Garmin, SAM/SOM) → calibrated Oura-shape trajectory |
| `Members` | Cohort-aged member engine (gross adds, churn by tenure, ending/avg members) |
| `ARPU` | Single-line blended ARPU driver; bottoms-up justification table (consumer + Unite mix); Bull 6.0% decomposition |
| `Revenue Build` | Members × ARPU = Revenue, by year |
| `P&L` | Revenue → COGS → OpEx → EBIT → Tax → NI; SBC and NOL schedules wired |
| `FCF` | NOPAT → +D&A → −CapEx → −ΔNWC → UFCF; ΔNWC sourced from WC & Cash |
| `WC & Cash` | Bottoms-up working capital (DSO/DIH/DPO + deferred rev) + cash roll-forward |
| `WACC Bottom-Up` | Justification (Build B): per-comp Hamada beta regressions → bucket medians; cross-checks Damodaran sector |
| `DCF` | Discounting + terminal value + equity bridge + scenario triangulation block (rows 56-74) |
| `RealOptions` | Healthcare binary-gate decision tree; scenario × probability; macro-weight grid; pushback memo |
| `Comps` | Three-thesis comp library (Failed Pivot / Subscription Executed / Healthcare Platform); Oura ref |
| `Precedents` | Precedent transactions table (data only; not wired into Football Field) |
| `Cap Table` | Round-by-round funding history; partial — waterfall formulas not built |
| `Football Field` | Multi-method synthesis with weights, weighted average, chart helper table |
| `Scenarios` | Scenario × method matrix; probability-weight sensitivity; Jensen gap output |
| `Sensitivity` | WACC × Exit Multiple grid + four other 2-D grids and tornado |
| `Checks` | 10 automated integrity checks (Members×ARPU=Rev, TV%EV, Gordon validity, etc.) |
| `Sources` | Index of research files |
| `CalibrationLog` | Open items with priority and suggested fix |

---

## TL;DR — Top Five Divergences and Posture

1. **Football Field is executing a different thesis from the HTML.** HTML commits to weights `40/35/10/15` (DCF / Comps / Series G / IPO) and a primary DCF method = **scenario-weighted** (`Scenarios tab` = ~$10.13B). The model wires the football field DCF row to the **base-case-only equity** (`DCF!C61` = $7.34B) at 40% weight. The scenario-weighted P·DCF (which the HTML calls the headline) is shown only as ancillary row 1d, given **zero weight**. Weighted average prints **$7.11B** vs. HTML's stated $8.63B. This is the single biggest divergence.
2. **WACC is wrong relative to the HTML.** HTML targets Bull ~9.5% / Base ~10.85% / Bear ~12% via the Damodaran-style top-down build. The DCF reads `Assumptions!F74` = the **bottom-up build** at **11.59% Base / 11.00% Bull / 12.18% Bear** — a ~75bps Base-case overstatement that drags every DCF number down. The Damodaran build (10.85% Base, 9.75% Bull, 11.94% Bear) sits in C73:E73, computed but not referenced.
3. **Bull MG sequence is broken.** HTML targets `70/55/38/27/19/13/9/7` → 18.0M. Model has `70/55/38/27/19/13/9/#REF!` → 18.11M. `E174` (MG8 Bull 2033) is a `#REF!` error; `D174` (MG8 Base) formula references that #REF! in its Bull branch. The known Assumptions F179 issue is *fixed* (F177 prints 0.06%), but the Bull tail breaks differently — MG6/MG7/MG8 Bull formulas at F172/F173/F174 reference `E173`/`E174`/`#REF!` not `E172`/`E173`/`E174`. **Critical formula regression.**
4. **ARPU 2025 anchor is $278, not $274.** HTML commits to $274. Model has Base = $278 (ARPU!D20 sum: $258 sub + $15 Labs + $5 accessories). Bear hardcoded at $270, Bull at $340. The HTML's 2033 outcomes ($334 / $347 / $437) are not produced — model 2033 prints ~$352 Base only (Bear/Bull ARPU paths are not separately modeled because R4 Bull/Bear are hardcoded $ levels with the same `R4g` 3% growth, not scenario-specific growth rates).
5. **Probability-weighted scenario DCF outputs match the HTML closely** — input-level $8.09B vs. HTML $8.0B; scenario-level $10.13B vs. HTML $10.13B; both anchored at neutral 20/50/30. **This is the strongest part of the model — the Jensen Gap architecture is executed cleanly.** Posture: the model nails the central methodological insight but undercuts it by failing to wire the headline through to the Football Field.

**Overall posture:** the model executes maybe 70% of the HTML thesis. The Member Thesis four-lens triangulation, the Jensen Gap diagnostic in `DCF!A56:F74`, the bucket-weighted real options exhibit, and the three-thesis Comps tab are all built and consistent with the HTML. But the **headline number flowing into the football field is $7.1B, not $11.2B**, and the WACC is ~75bps too high. A reader of just the Cover/Football Field would conclude WHOOP is meaningfully discounted to Series G — the **opposite** of the HTML's "+11% premium" thesis.

---

## Open Questions

1. **WACC source of truth.** HTML's 10.85% Base maps to `Assumptions!C73:E73` (Damodaran-style component sum). DCF reads `F74` (bottoms-up median, 11.59% Base). Was the model deliberately migrated to the bottoms-up justification, with the HTML not yet updated? Or was the DCF link supposed to stay on F73 and got accidentally redirected? The `WACC Bottom-Up` sheet itself says "DCF tab continues to reference Assumptions!F74 (Build A)" — but Build A is the *Damodaran* build, and F74 is *Build B*. The labeling in cell A115 and the wiring contradict each other.
2. **Real options member counts** — HTML §VI item 7 calls for reconciling RealOptions to the post-restructure Bull endpoint (18M). Model uses `Assumptions!E176` = 18.11M (geometric compound from broken MG sequence). If MG8 Bull is fixed to 0.07 the endpoint becomes ~18.0M as intended; the chain works but is downstream of the `#REF!`.
3. **Football Field weights.** HTML stipulates 40/35/10/15 with DCF = scenario-weighted. Model gives 40% to base-case-only DCF (row 6) and 35% to Comps (row 10) and 10%/15% to Series G/IPO. Were rows 1c/1d (ProbWeighted, Scenario-Weighted) intended to *replace* row 1's weight, or to coexist as exhibits? The K6 note says "Bear/Base/Bull DCF Equity sourced from DCF triangulation rows 60-62" — i.e., uses base case for the headline by design. This is inconsistent with the HTML headline.
4. **Comps base used in Scenarios row 7 Base column.** `Scenarios!C7 = 83.5977` (hardcoded numeric) — appears to be an erroneous overwrite of a formula. Football Field correctly uses `Comps!D55 = $3,624.77M`. Likely a manual edit accident.
5. **Bull MG #REF! origin.** Was a row inserted/deleted in Section 12 that broke `E174` and the chained Bull references at F172:F174 / J172:J174 / K172:K174 / E235 / F235? The Member Thesis tab still produces the 18.0M endpoint via a separate (correct) trajectory build, masking the breakage.

---

## Divergence Ledger

| # | Commitment (HTML) | Where in model | Found value | Matches? | Severity | Fix path |
|---|---|---|---|---|---|---|
| 1 | **Two-driver revenue: Members × ARPU only** | `Revenue Build`, `ARPU!D10`, `Members!*35`. `Revenue Build!C20` = Avg Members × Blended ARPU. No add-on revenue lines. | Two-driver discipline holds. ARPU bottoms-up justification ($258 sub + $15 Labs + $5 accessories) sits on ARPU sheet row 17-20 as a *memo only* table; does not layer separate revenue. | YES | — | None needed |
| 2 | **Four-lens triangulation → ~10.9M Base 2033 (lenses ~8.55 / ~11.42 / ~10.5 / ~8.4M)** | `Member Thesis!B16:B20`. Lens A=11.95, Lens B=11.21, Lens C=10.63, Lens D=8.38, Median=10.92. | Lenses match the HTML *shape* but values diverge: Lens A 11.95 vs HTML 8.55 (HTML used 25% terminal share; model uses 30%); Lens B 11.21 vs HTML 11.42 (free-hw multiplier 1.08 vs HTML 1.10); Lens C 10.63 vs HTML 10.5 (close); Lens D 8.38 vs HTML 8.4 (close). Median 10.92 = HTML 10.9 essentially exact. | PARTIAL | Medium | Lens A: change `Member Thesis!B29` from 0.3 → 0.25 to match HTML. Lens B: change `B41` from 1.08 → 1.10. (One-cell edits each.) Median is already on target so the live-model output is fine; cosmetic only for memo defense. |
| 3a | **ARPU 2025 anchor = $274** | `Assumptions!D11` → `ARPU!D10` = `=D8` = `=D20` = SUM($258 sub + $15 Labs + $5 accessories) = **$278** | $278 vs HTML $274 (+$4, +1.4%) | NO | Low | One-cell: change ARPU!D17, D18, or D19 to sum to 274 (e.g. accessories from $5 → $1). |
| 3b | **ARPU growth: Bear 2.5% / Base 3.0% / Bull 6.0%** | `Assumptions!C149:E149` = 2.5% / 3.0% / 6.0%. Active = `F149` = 3.0% (Base scenario active). | Values **MATCH** Bear/Base/Bull. | YES | — | None |
| 3c | **Bull 6% decomposes 3.0/1.0/1.0/0.3/0.7 (inflation/tier-mix/Labs-BP/B2B/payer)** | `ARPU!B31:B35` = 0.03 / 0.01 / 0.01 / 0.003 / 0.007, sum B36 = 0.06. | **MATCHES exactly.** Justification table is memo-only (does not drive). | YES | — | None |
| 3d | **2033 ARPU outcomes Bear $334 / Base $347 / Bull $437** | `ARPU!D10:L10` produces a single Base path: 2033 = $352. Bear path uses $270 × growth-rate-not-defined; Bull uses $340 hardcoded but `R4g` (F149) Active reads only Base 3%. There is no Bear/Bull ARPU trajectory. | NO. Model shows **only one ARPU path** (Base $278 → $352). Bear and Bull 2025 anchors exist (C11=$270, E11=$340) but no scenario-specific growth path is traced through ARPU sheet. The ARPU tab's `D10` formula reads `D8` (anchor) only via Base; growth rate `D9` reads `F149` which is scenario-active but yields $352 Base 2033, not the $334/$347/$437 trio. | NO | High | Multi-cell rebuild on ARPU tab: parallel Bear/Bull rows growing each at C149/E149 from C11/E11. Currently only Base path is traced. |
| 4 | **Bull MG1-MG8 = 70 / 55 / 38 / 27 / 19 / 13 / 9 / 7 → 18.0M** | `Assumptions!E167:E174` = 70 / 55 / 38 / 27 / 19 / 13 / 9 / **7** (correct numeric values). BUT `E174 = #REF!` per the printout in row 174 (`IF(...,"Bull",#REF!,...)`). Computed `MG_chk!E176` = 18.11M (geometrically compounds 1.07 from a `#REF!` source resolved to 0.07 historically). Bull values for MG6/MG7/MG8 Active formulas (F172/F173/F174) reference `E173/E174/#REF!` not `E172/E173/E174`. ProbWeighted (J) row similarly broken. | Numbers print ~correct (E176 → 18.11M, very close to 18.0M target) but **formula chain is broken**. F172 Bull arm references E173, F173 Bull arm references E174, F174 Bull arm references `#REF!`. Bull-scenario member endpoint is wrong-by-construction. The Active (F176) Base scenario doesn't notice. | PARTIAL | Critical | Multi-cell edit: rewrite `F172`, `F173`, `F174`, `J172`, `J173`, `J174`, `E235`, `F235`, `K235` to reference `E172/E173/E174` (and fix E174's broken `#REF!` if it needs to be 0.07 hardcoded). When user toggles `B3 → Bull`, member endpoint will jump because of the off-by-one row reference. |
| 5a | **Bucket weights: Bear 40/40/20, Base 20/40/40, Bull 10/30/60** | `Assumptions!C83:E85` = (0.4,0.2,0.1) / (0.4,0.4,0.3) / (0.2,0.4,0.6). | **MATCHES exactly.** Bucket weights for B1/B2/B3 across Bear/Base/Bull. | YES | — | None |
| 5b | **WACC: Bull ~9.5% / Base ~10.85% / Bear ~12%** | `Assumptions!C73:E73` (Damodaran sector build) = **11.94% / 10.85% / 9.75%** — matches HTML exactly. BUT the DCF reads `F74` (bottoms-up build) = **12.18% / 11.59% / 11.00%** for Bear/Base/Bull. | Damodaran build (C73:E73) matches HTML; **DCF is reading the wrong row**. Live Base WACC in DCF is 11.59%, not 10.85%. Material drag on EV. | NO | Critical | One-cell: change `DCF!D12` (and copies E12:K12) from `=Assumptions!$F$74` to `=Assumptions!$F$73`. Or repoint `Assumptions!F74` to F73's source. Either is single-edit. Affects all DCF outputs. |
| 5c | **CSRP varies 1-3% by scenario** | `Assumptions!C72:E72` = 0.03 / 0.02 / 0.01. | **MATCHES** Bear 3% / Base 2% / Bull 1%. | YES | — | None |
| 5d | **Components Rf ~4.3%, ERP ~4.5%, size premium ~0.8%** | C68:E68=4.3%; C69:E69=4.5%; C71:E71=0.81%. | All three match. | YES | — | None |
| 6 | **Terminal multiples Bear 3.0x / Base 3.5x / Bull 4.5x** | `Assumptions!C77:E77` = 3.0 / 3.5 / 4.5. ProbWeighted J77 = 3.7. | **MATCHES exactly.** | YES | — | None |
| 7a | **Input-level (ProbWeighted) at 20/50/30 ≈ $8.0B** | `DCF!C63 = 8090.59`; reproduced at `Football Field!D8`, `Scenarios!E5`, `Memo!E11`. | **$8.09B, matches HTML $8.0B (within rounding).** | YES | — | None |
| 7b | **Scenario-level at 20/50/30 ≈ $10.13B (~$10.1B)** | `DCF!C65 = 10133.52` formula `=0.2*C60+0.5*C61+0.3*C62` (using static snapshot). `Scenarios!E17 = 10133.52`. | **$10.13B, matches HTML exactly.** | YES | — | None |
| 7c | **Both implementations live in the model with Jensen Gap exposed** | `DCF!A56:F74` triangulation block; `Scenarios!A12:H18` weight-scheme grid; `Memo!*` headline. Jensen gap = $2.04B at neutral. | Architecture present and correct. Static snapshot caveat documented. | YES | — | None |
| 8a | **Pessimistic 35/50/15 → $7.5B** | `Scenarios!E16 = 7526.85` formula uses live C60/C61/C62. | **$7.53B, matches.** | YES | — | None |
| 8b | **Neutral 20/50/30 → $11.2B** | `Scenarios!E17 = 10133.52`. HTML claim: "$11.2B intrinsic". | **$10.13B in model vs. $11.2B in HTML.** ~$1.07B (~10%) gap. Very likely caused by WACC issue (#5b above): if WACC were corrected from 11.59% Base → 10.85% Base, scenario-weighted EV rises ~$1B+ as TV PV expands. | NO | High | Cascades from #5b. Fix WACC pointer; will likely resolve to ~$11.0-11.4B. |
| 8c | **Optimistic 15/45/40 → $13.0B** | `Scenarios!E18 = 11629.70`. HTML claim: $13.0B. | **$11.63B in model vs. $13.0B in HTML.** ~$1.37B (~11%) gap. Same WACC root cause. | NO | High | Cascades from #5b. |
| 9a | **Football field weights DCF 40 / Comps 35 / Series G 10 / IPO 15** | `Football Field!I6=0.4, I10=0.35, I13=0.1, I14=0.15`. Sum check I16=1.00. | **Weights match exactly.** | YES | — | None |
| 9b | **DCF 40% weight applies to scenario-weighted intrinsic ~$11.2B** | `Football Field!D6 = DCF!C61/1000 = 7.336` (Base case, no scenario weighting, no real options). | **NO.** Model uses Base-only DCF Equity ($7.34B), giving Football Field weighted average $7.11B, vs. HTML's claimed $8.63B based on scenario-weighted $11.2B at 40%. | NO | Critical | One-cell: change `Football Field!D6` from `=DCF!C61/1000` to `=Scenarios!E17/1000` (scenario-weighted neutral). Also low/high to E16/E18. **Or** reweight: move 40% to row 1d (Scenario-Weighted DCF) and zero out row 1. Either is single-area edit, but must be made consciously. |
| 9c | **Comps 3-bucket** | Comps tab built around Three-Thesis: Failed Pivot / Subscription Executed / Healthcare Platform (rows 36-67). Composite span feeds Football Field. | **MATCHES the HTML's three-thesis framing.** "Bucket 1 / Bucket 2 / Bucket 3" labeling in WACC sheet maps to same three theses. | YES | — | None |
| 10a | **Real options $164M Bear / $940M Base / $2,609M Bull** | `RealOptions!B31:D31` = 164.16 / 940.09 / **2833.65**. | Bear & Base match. **Bull = $2,834M vs. HTML $2,609M (+$224M, +8.6%).** Diff likely from member-endpoint feeding `Assumptions!E176` = 18.11M (broken MG sequence) vs intended 18.0M, plus eligibility/ARPU/multiple differences. | PARTIAL | Low | If MG sequence is fixed (#4) and intended Bull endpoint is 18.0M, gap closes to ~$50M cosmetic. |
| 10b | **Real options scenario-weighted at neutral ~$1.29B** | `RealOptions!B38 = 1352.97` and `RealOptions!D97 (yellow center) = 1352.97`. | $1.35B vs HTML $1.29B. Within rounding given the Bull overstatement above. | PARTIAL | Cosmetic | Cascades from #10a; same fix path. |
| 10c | **Real options EXHIBIT-ONLY, not in football field as primary** | `Football Field!A7 = "1b. DCF + Real Options"` — listed as a row but with **no I-column weight** (column I empty for rows 7, 8, 9). Weighted average uses only rows 6/10/13/14. | **Correctly exhibit-only**: real options listed for transparency but excluded from weighted average. Matches HTML methodological intent. | YES | — | None |
| 11a | **F179 #DIV/0! cleanup** (HTML §VI item 2) | `Assumptions!F177 = (F176 - 'Member Thesis'!B20)/'Member Thesis'!B20 = 0.000636` (PASS). `Member Thesis!B20 = 10.92`. The F179 listed in instructions is empty / not a #DIV/0!. | **Resolved.** Triangulation distance prints 0.06%, no error. F179 itself is empty. | YES (FIXED) | — | None |
| 11b | **ProbWeighted WACC bypass fix at J74/J75** | `Assumptions!J74 = $C$2*C74 + $E$2*D74 + $G$2*E74 = 0.1153`; `F74 = IF(...,$ProbWeighted",J74,...))`. ProbWeighted scenario correctly weights bottoms-up WACC. (HTML refers to J74/J75 fix; J74 is wired, J75 doesn't exist as separate cell — likely the intended F73 read is also wired through `IF($B$3="ProbWeighted",J73,...)`. Inspection: F73 has NO ProbWeighted branch; only F74 does.) | F74 fix present. **F73 (Damodaran build, the row HTML actually uses) has no ProbWeighted branch** — if DCF were repointed back to F73 per #5b, ProbWeighted scenario would silently fall through to Base. | PARTIAL | High | If #5b is actioned (DCF → F73), also add ProbWeighted branch to F73 with companion J73. Multi-cell edit. |
| 11c | **Real options member counts updated to 18M Bull endpoint** | `RealOptions!D13 = Assumptions!E176 = 18.11M`. | Live-linked to MG sequence (which is broken; resolved value is correct ~18M). | PARTIAL | Cosmetic | Resolves with #4. |

---

## Other Notable Findings (not on the original checklist)

- **Scenarios!C7 = 83.5977** is a hardcoded numeric in the "Trading Comps Base" cell, almost certainly an accidental overwrite of `=Comps!D55`. Football Field correctly reads from Comps, but Scenarios tab Base column for Comps is broken.
- **Cap Table waterfall** is unbuilt (only round-by-round funding history). HTML doesn't require waterfall, but the assumption `Assumptions!F54` (FD shares = 410M) is used as the per-share denominator everywhere — no consistency check between cap table and FD shares.
- **DCF!A45 "active scenario" real options** uses Base ($940M) regardless of scenario toggle — `RealOptions!B36` only switches Bear/Base/Bull, doesn't have a ProbWeighted branch. ProbWeighted scenario gets Base real options.
- **Sensitivity tab Grid 1** WACC range starts at 10.09%, anchored on the Base 10.85% target — confirming the *intent* of the HTML. So the sensitivity grids were built against the Damodaran (F73) WACC even though DCF live-reads F74. This is direct internal evidence that **#5b is a bug, not a deliberate migration.**
- **Checks tab item 4** flags `TV % EV = 73%` (PASS, near WARN threshold 75%); **item 5** flags TV divergence 33.6% (FAIL, threshold 25%). DCF tab itself notes the integrity flags in A3. Consistent with HTML §VI item 1 ("Bull terminal multiple may need recalibration").

---

## Severity Summary (counts)

- **Critical:** 3 (Football Field DCF wiring #9b, WACC pointer #5b, Bull MG `#REF!` chain #4)
- **High:** 4 (ARPU 2033 trajectory missing scenarios #3d, Neutral $11.2B target #8b, Optimistic $13B target #8c, ProbWeighted F73 branch #11b)
- **Medium:** 1 (Lens A/B inputs slightly off HTML #2)
- **Low:** 2 (ARPU $4 anchor diff #3a, Bull RO $224M overstatement #10a)
- **Cosmetic:** 2 (RO weighted #10b, RO member-endpoint cosmetic #11c)

If the three Critical items are fixed, the model would print: scenario-weighted DCF Base ~$11.2B, Football Field weighted average ~$8.5-8.7B, in line with the HTML's stated $11.2B / $8.63B headlines. The Jensen Gap architecture, Real Options exhibit, and Comps three-thesis framework are already production-ready.
