# WHOOP Valuation Master — PPT Gap Matrix

**Audit date:** 2026-05-10
**Live deck:** `/home/user/whoop_val/Whoop Valuation Master.pptx` (read-only)
**Canonical spec:** `/home/user/whoop_val/Whoop Master.html` Section IV
**Live model:** `/home/user/whoop_val/new-whoop-model .xlsx` (DCF, Scenarios, Football Field, Memo)

---

## Headline read

The deck is materially **out of sync with the spec**. The deck still tells a "DCF + Real Options additive layer, comps + back-solve verdict = modestly OVER" story (closing line: "headline overstates common-equivalent value by ~6%"). The spec mandates the opposite: scenario-weighted DCF as primary, real options retained as exhibit-only (NOT additive), Jensen Gap as the novel slide, and the central thesis "Series G mildly UNDERPRICED at +11%". Six of the 13 spec slides are missing or only partially present; the existing real-options slide and the back-solve slide both need to be rebuilt or repurposed. Numbers are also stale relative to the model.

---

## 1. Deck inventory

| Deck slide # | Page label | Title / headline (text on slide) | 1-line content summary |
|---|---|---|---|
| 1 | 01/12 | "Is WHOOP worth $10.1 billion?" | Title slide; investment question; two images. **Spec match.** |
| 2 | 02/12 — COMPANY | "A premium wearable with healthcare ambitions." | Company overview, 3 cards (What/How/Why hard to value), Series G mechanics box ($575M, $10.1B, 2.8x step-up). **Spec match.** |
| 3 | 02/12 — IDENTITY | "Business Model + Industry Outlook (TAM Expansion)" | Three-bucket comp identity (Hardware/Subscription/Health Data) with WHOOP at intersection. **Functions as the comps-disconnect intro; misnumbered page.** |
| 4 | 03/12 — METHOD | "Separating consumer subscription economics with healthcare optionality." | Methodology preview with 3-row table (Naive / Common practitioner / Ours). **Spec match (slide 3 in spec).** |
| 5 | 04/12 — DCF·BUILD | "Revenue = Members × ARPU" | DCF architecture: 3-phase chart (Y1-Y7 hypergrowth/inflection/terminal), Key Assumptions panel (2.5M→11.4M, ARPU $324→$396, churn 21%→14%, terminal 26% margin, WACC 10.5%, beta 1.32). |
| 6 | n/a — no header | "DCF logic:" | **DRAFT/NOTES SLIDE.** Raw planning text about Jensen, scenarios, comps anchor, healthcare upside. Not a built slide. |
| 7 | 05/12 — DCF·BUILD | "Three phases. Seven years." | Second DCF build slide. Same 3-phase structure, different numbers (2.5M→8.4M members at 18% CAGR, ARPU $305→$417 / $305→$348, exit 3.5x, WACC 10.79%, EBITDA 18%→37%, terminal $11.9B/$11.4B). **Duplicates slide 5 with conflicting numbers.** |
| 8 | 05/12 — DCF·OUTPUT | "Base case $8.4B — but identity matters more than precision." | EV→Equity waterfall (PV FCF +4.1, PV TV +5.2, EV 9.3, −Net Debt 0.6, +Cash 0.4, −SBC 0.7 = $8.4B base; range $5.8B-$12.1B). Tornado: WACC bucket / Terminal EBITDA / Subscriber growth Y3 / Terminal churn / Terminal g. |
| 9 | 06/12 — REAL OPTIONS·ARUNDEL | "DCF prices the business. It doesn't price the optionality." | Three real options stacked additive: Health-data $1.6B, Medical-device $0.9B, Enterprise/B2B $0.5B. Building bars 8.4 → 10.0 → 10.9 → 11.4. Black-Scholes inputs S=$3.4B, K=$1.8B, σ=52%, T=5y, r=4.2%, C=+$3.0B. **Conflicts with spec — spec says options are EXHIBIT-ONLY, not additive.** |
| 10 | 07/12 — COMPS | "The comp range is the analysis." | Three-bucket comp scatter (EV/Rev × NTM growth) + implied EV at bucket median: Hardware 2x = $2.2B, Subscription 3.5x = $3.9B, Health-data 8.5x = $9.4B. Post-IPO fates panel (Peloton −70%, Garmin +85%, Dexcom +400%). |
| 11 | 08/12 — ★ NOVELTY · BACK-SOLVE | "What does $10.1B actually mean?" | Series G $10.1B headline → −$0.9B (1× non-part liq pref) − $0.6B (ratchet) − $0.4B (participation) = **$8.2B common-equivalent**. Comparison table: implied @ $8.2B vs base case (subs 8.4M vs 7.1M, etc.). Gap ~$1.9B. |
| 12 | 09/12 — VERDICT | "The verdict — modestly over." | Football field with 5 methods (DCF, DCF+RO, Comps HW/Sub/HD, Series G common-equiv) plotted vs $10.1B reference. Central estimate **$9.6B, "verdict OVER ~6%"**. **Conflicts with spec — spec says +11% UNDER.** |
| 13 | 10/12 — HONEST SENSITIVITY | "Three triggers that flip the verdict." | Three downside triggers (churn +200bps, healthcare option fails by Y5, Peloton-style IPO re-rate) with EV impacts. **Functions as caveats slide.** |
| 14 | 11/12 — ONE SENTENCE | "WHOOP at $10.1B is priced as a health-data platform... overstates by ~6%." | Closing one-sentence verdict + "QUESTIONS?" Spec match (Q&A backup), but verdict is wrong direction. |

**Total slides: 14.** Page labels go up to "11/12" — deck is internally inconsistent on numbering and is missing a slide of its own count.

---

## 2. Model headline numbers (for cross-check)

Pulled live from `new-whoop-model .xlsx` with `data_only=True`:

| Metric | Model value | Source cell |
|---|---|---|
| Bear DCF Equity | **$2,504M** | `DCF!C60` |
| Base DCF Equity | **$7,336M** | `DCF!C61` |
| Bull DCF Equity | **$19,882M** | `DCF!C62` |
| ProbWeighted (input-level) Equity | **$8,091M** | `DCF!C63` |
| Scenario-Weighted Equity (Neutral 20/50/30) | **$10,134M** | `Scenarios!E17` |
| Pessimistic (35/50/15) Scenario-Wtd | $7,527M | `Scenarios!E16` |
| Optimistic (15/45/40) Scenario-Wtd | $11,630M | `Scenarios!E18` |
| **Jensen Gap (Neutral)** | **$2,043M (25.3%)** | `DCF!C68:C69` |
| Real Options — Bear / Base / Bull | $164M / $940M / $2,834M | `DCF!C43:C45` |
| WACC (Base) | **11.59%** | `DCF!D12` |
| Exit multiple (Base) | **3.5x** | `DCF!C21` |
| Terminal Value (selected, blended) | $11,204M | `DCF!C25` |
| EV (DCF Base) | $6,749M | `DCF!C32` |
| Football Field Weighted Avg | **$7,107M** ($7.1B) | `Football Field!D18` |
| Series G mark | $10,100M | constant |
| FY25 Revenue | **$528M** | `DCF!C8` |
| Comp B2 Median (Subscription, Recognized GP × EV/GP) | $3,625M | `Comps!D55` |
| Comp B3 Healthcare bookings GP × EV/GP median | $6,600M | `Comps!D67` |

**Note:** Model Base FY25 revenue = **$528M** (not the "$520M" the spec slide-2 prose says, and not the $725M base from CLAUDE.md research). Spec uses $520M; deck uses $528M only on a buried sheet — slide 2 says "78% gross margin closer to software" but no FY25 revenue number is stated on slide 2.

**Note on "intrinsic $11.2B":** The spec says intrinsic alone = $11.2B (= scenario-weighted Neutral $10.1B + healthcare option). Model returns scenario-weighted Neutral = **$10,134M with options included = $11,449M** (`DCF!D65`). So the spec's $11.2B is consistent with model `Equity + Options` at scenario-weighted neutral, not the bare scenario-weighted DCF. The deck never surfaces this number anywhere.

---

## 3. Gap matrix (spec → deck)

Severity legend: **Critical** = thesis-breaking; **High** = required content missing or wrong; **Medium** = misaligned but salvageable; **Low** = cosmetic.

| Spec # | Spec slide name | Present? | Deck slide # | Title match? | Content alignment | Numbers correct vs model? | Visuals present? | Severity | Build path |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Title + investment question | Yes | 1 | Yes | full | Series G $10.1B correct | 2 stock images | Low | Keep. Polish images. |
| 2 | Company overview (2.5M, $520M, $30/mo, no-comp framing) | Yes | 2 | Yes | partial | $520M FY25 revenue NOT on slide; pricing tiers $199/$239/$359 unclear vs spec "$30/month"; 78% GM stated | Cards + product image + Series G mechanics | Medium | Add explicit $520M FY25 + 2.5M members callouts; reconcile $30/mo vs tier prices. |
| 3 | Methodology preview (scenario-weighted DCF primary; RO considered; comps cross-check; Series G validation; class-content links 1A/1B/3B/4B) | Partial | 4 | No — slide says "Separating consumer sub economics with healthcare optionality" | partial | n/a (qualitative) | 3-row table | High | Re-anchor to spec language: scenario-weighted DCF = primary, RO = considered, comps = cross-check, Series G = validation. Add Lecture 1A/1B/3B/4B labels. Slide 3 (identity-bucket) currently sits in spec-3 position but is really comps content — relocate to spec-8 position. |
| 4 | DCF architecture: Revenue = Members × ARPU; four-lens triangulation; ARPU 2.5/3.0/6.0% with Bull decomposition | Partial | 5 (and duplicated on 7) | "Revenue = Members × ARPU" yes | partial | Slide 5 says ARPU $324→$396 (≠ spec $274 anchor, $334/$347/$437 endpoints). Members 2.5M→11.4M (spec says 10.9M Base). Slide 7 says 2.5M→8.4M @ 18% CAGR (≠ spec 10.9M / Lens-D capital-led). WACC 10.5% (slide 5) vs 10.79% (slide 7) vs **model 11.59% Base** — all wrong. | Phase chart + assumptions panel | **Critical** | Single, clean DCF arch slide. Pull Members 2.5M → 10.9M (Base); show four-lens triangulation visual (TAM/Peloton-shifted/Multi-comp/Capital-led converging on ~10.5M median). ARPU 2.5/3.0/6.0% with Bull decomposition (3% inf + 1% mix + 1% Labs + 0.3% Unite + 0.7% payer). WACC 11.59% from model. Drop the duplicate slide 7. |
| 5 | Three scenarios — dispersion ($2.5B → ~$23B post-restructure) | No (only oblique) | — | — | none | Bear $2.5B and Bull $19.9B (or $22.6B with options) live in Scenarios sheet but no slide visualizes the dispersion | None | **Critical** | New slide. Three-bar dispersion chart: Bear $2.5B, Base $7.3B (or $8.3B w/options), Bull $19.9B (or $22.6B w/options). Bear "Plateau"/Base "Durable Subscription"/Bull "Healthcare + Platform" labels with thesis line each. Series G gold reference line. |
| 6 | Probability weighting + Jensen's Gap (input-level $8.0B vs scenario-level $11.2B). **Novel slide.** | No (only as draft notes) | 6 (notes-only) | n/a | none | Slide 6 contains raw draft text that mentions Jensen, but no built visual. Model has both numbers: ProbWeighted $8.09B, Scenario-Weighted Neutral $10.13B (+ options $11.45B). | None | **Critical** | New slide — highest leverage. Two-anchor diagram: input-level $8.0B (left) vs scenario-level $11.2B (right). Jensen convexity sketch (DCF f(X) plotted against X with E[f(X)] vs f(E[X]) annotated). For-WHOOP correlation list (members/margins, members/multiple, members/WACC, ARPU/multiple). This earns the novelty grade. |
| 7 | Football field — 4 methods, weighted avg $8.6B (below SeriesG), intrinsic alone $11.2B (above) | Partial | 12 | "modestly over" verdict directly contradicts spec | partial | Slide says central $9.6B, verdict "OVER ~6%". Spec & model say $8.6B weighted avg / $11.2B intrinsic = "+11% UNDER". Football Field tab actually computes weighted avg $7.1B (because slide method weights diverge from spec 40/35/10/15). Method bars list 03A Hardware $1.2-2.8B, 03B Sub $3.0-4.6B, 03C HD $7.4-13.0B, M01 DCF $5.8-12.1B, M02 DCF+RO $7.4-14.9B, Series G common-equiv $8.0-9.0B. | Football field bars + Series G ref line | **Critical** | Rebuild verdict and arithmetic. Spec methods: Intrinsic DCF (40%) $11.2B, Public Comps (35%) $3.6B, Series G (10%) $10.1B, IPO Range (15%) $12.6B → weighted $8.63B. Show **dual** result: weighted avg $8.6B *and* intrinsic alone $11.2B. Verdict: +11% UNDER, not −6% over. Drop the (split) DCF + DCF+RO twin bars; spec is RO-not-additive. |
| 8 | Comps disconnect — three-bucket; B2 puts WHOOP at $3.6B; comp methodology systematically misses platform; a16z American Dynamism setup | Partial | 3 + 10 | n/a | partial | Slide 3 establishes three-bucket identity but with wrong comp lists (Peloton·Sonos·Roku for sub vs spec's Peloton·Spotify; GoPro·Fitbit·Garmin for hardware vs spec's Garmin only). Slide 10 has the scatter plot and bucket-median EVs ($2.2B / $3.9B / $9.4B). Subscription bucket implied $3.9B ≈ spec's $3.6B. No a16z American Dynamism framing anywhere. | Scatter + bucket EVs + post-IPO fates panel | High | Consolidate to one slide: three-bucket scatter + implied EVs + a16z American Dynamism setup ("comp methodology systematically misses platform-positioned companies before platform thesis is publicly visible"). Use spec's bucket comp lists: B1 Garmin (Apple ref), B2 Peloton+Spotify, B3 Dexcom/ResMed/Masimo/iRhythm. |
| 9 | Sensitivities — tornado (Members > Terminal > WACC > FCF margin > ARPU growth > healthcare option) + 2-way heatmap (Members × WACC) | Partial | 8 | n/a | partial | Slide 8 has tornado but ranking is WACC-by-bucket / Terminal EBITDA / Subscriber growth Y3 / Terminal churn / Terminal g — does **not** match spec ranking. Model `Memo!A35:A47` ranking = Member Growth > Terminal EV/Rev > WACC > R&D > SBC > G&A > Terminal COGS > CapEx > Y3+ churn > Tax. No 2-way heatmap on slide; model has one (`Memo!A66:H73`, WACC × Exit Multiple — but spec wants Members × WACC). | Tornado bars only | High | Rebuild tornado with model's actual ranking (Members dominates by ~30%). Add Members × WACC heatmap (need to construct; currently model has WACC × Exit Multiple). Spec says ARPU rank 5 confirms ARPU discipline didn't cost much — surface that as a callout. |
| 10 | Central thesis: $11.2B vs $10.10B = +11% → "Series G mildly underpriced" | No | — | n/a | none | Deck's closing thesis (slide 12 + 14) is **opposite direction**: "modestly over ~6%" / "headline overstates by ~6%" | None | **Critical** | New slide (or repurpose slide 14). Headline number $11.2B intrinsic vs $10.10B Series G = +11%. "Series G mildly underpriced." a16z American Dynamism: sophisticated capital captures structural mispricing. |
| 11 | Probability weight sensitivity — three schemes producing $7.5B / $11.2B / $13.0B | No | — | n/a | none | Model `Scenarios!E16:E18` = $7.53B / $10.13B / $11.63B (+options $8.84B / $11.45B / $12.94B — close to spec's quoted 7.5/11.2/13.0) | None | High | New slide. Three-scheme bar chart with Pessimistic 35/50/15, Neutral 20/50/30, Optimistic 15/45/40. Use Equity+Options scenario-weighted: $8.8B / $11.4B / $12.9B (matches spec's quoted ranges within rounding). Robust-conclusion note: even pessimistic exceeds bear-only DCF. |
| 12 | Caveats and limitations (founder risk, competitive risk, healthcare timing, RO not additive) | Partial | 13 | n/a | partial | Slide 13 lists 3 trigger-flips (churn, healthcare option failure, IPO re-rate). Doesn't explicitly call out founder risk, competitive risk (Apple/Oura/glucose), Series F ratchet status, RO-not-additive rationale. | 3 trigger cards | Medium | Expand to spec's 4 caveat groups: investment cost at decision node; founder execution risk; competitive risk (Apple Watch / Oura / glucose); healthcare timing 2033 horizon. Explicit "real options retained as cross-validation, NOT additive" note. |
| 13 | Q&A backup — anticipated Qs and prepared As | Partial | 14 | "QUESTIONS?" yes | partial | One closing sentence; no anticipated Q&A backup material | "QUESTIONS?" + 1 sentence | Medium | Build proper backup slide(s) with the seven anticipated Q&As from spec Section V (Bull ARPU 6% defense, members 18M decomposition, RO not-additive, 30% Bull weight anchoring, comps disconnect, why DCF+RO earlier vs now, why not APV). Hold as appendix flip-to material. |
| — | **Extra in deck not in spec: Slide 6 (draft notes)** | — | 6 | — | n/a | — | none | High | **Delete or rebuild as Jensen Gap slide.** Currently a planning-text dump. |
| — | **Extra in deck not in spec: Slide 7 (duplicate DCF build)** | — | 7 | — | n/a | Numbers conflict with slide 5: 8.4M vs 11.4M members; ARPU $305→$417 vs $324→$396; WACC 10.79% vs 10.5%; exit 3.5x | Same template as slide 5 with denser numbers panel | High | **Delete.** Consolidate any salvageable detail (WACC bottom-up CAPM build) into spec slide 4 single DCF-arch slide. |
| — | **Extra in deck not in spec: Slide 11 (Series G back-solve)** | — | 11 | "★ NOVELTY · BACK-SOLVE" | n/a | Liquidation pref math: $10.1B − $0.9B − $0.6B − $0.4B = $8.2B common-equivalent. Spec NEVER does this — spec treats Series G headline as the market price, not a value to be discounted to common-equivalent. CLAUDE.md confirms 1× non-participating pari passu (no ratchet of $0.6B has source). | Bridge bars + comparison table | High | **Delete or relocate to backup.** Preference-bridge logic conflicts with spec methodology. If kept, must be reframed as a side-check, not a "novelty" centerpiece — the spec's novelty is Jensen Gap, not pref math. |

---

## 4. Numbers ledger

Cross-check of every numeric claim found in the deck against spec/model. **Match** = within ~5%. **Mismatch** = ≥5% off or directionally wrong.

| Slide | Claim on slide | Source on slide | Spec / model says | Flag |
|---|---|---|---|---|
| 1 | Series G $10.1B | "Is WHOOP worth $10.1B?" | $10.10B (constant) | Match |
| 2 | $575M Series G raise | round mechanics box | $575M (CLAUDE.md) | Match |
| 2 | $10.1B post-money | round mechanics box | $10.10B | Match |
| 2 | $3.6B Series F (2021) | round mechanics box | $3.6B (CLAUDE.md) | Match |
| 2 | F→G step-up 2.8× | round mechanics box | $10.1B / $3.6B = 2.8x | Match |
| 2 | 2.5M members (implied via card text) | card 1 | 2.5M | Match |
| 2 | Tier prices $199/$239/$359 | card 2 | spec slide-2 says "$30/month" — pricing tiers consistent w/ Core/Peak/Life from CLAUDE.md | Match (presentation differs from spec language) |
| 2 | 78% gross margin | card 2 | Model slide cells: GM 75% (`Comps!B8`), terminal GM 78% (slide 7) | Match (terminal) |
| 2 | ~80% recurring sub / ~20% B2B Unite | card 2 | CLAUDE.md confirms ~80/20 | Match |
| 4 | "Bear/Base/Bull DCF, no real options; healthcare baked into Bull case" rejected | table row 2 | Spec **adopts this** as final architecture (RO not additive, healthcare flows through Bull fundamentals) | **MISMATCH — reverse polarity vs spec** |
| 4 | "Disciplined two-driver DCF + separate real option layer + probability weighting" = "Ours" | table row 3 | Spec **rejected this** — RO is exhibit-only after iteration 4-5 | **MISMATCH — directly contradicts spec** |
| 5 | Members 2.5M → 11.4M | top-line panel | Spec Base = **10.9M** (calibrated above 10.5M median) | Mismatch (~5% high) |
| 5 | Subscriber CAGR +24% | top-line panel | Implied 11.4/2.5 over 7y = 24%; spec doesn't state CAGR but is consistent | Match |
| 5 | ARPU $324 → $396 | top-line panel | Spec ARPU = $274 (2025), Base 2033 = $347. Slide 5 starts ARPU 18% above spec, ends 14% above. | **Mismatch** |
| 5 | Entering churn 21% / Terminal churn 14% | retention panel | Model `Memo!E14` etc. ProbWeighted churn baseline; flat-annual not cohort-aged. CLAUDE.md mandates cohort-aged framework. | Flag — methodology mismatch |
| 5 | Terminal EBITDA margin 26% | margin panel | Slide 7 says 37% terminal. Model `P&L` not pulled but DCF FCF margin 2033 = 20.8% (`DCF!K10`). | **Conflicting w/in deck**; slide 5 number lower than reasonable DCF terminal |
| 5 | Terminal g 3.0% | margin panel | Spec confirms 3.0% | Match |
| 5 | WACC base 10.5% | margin panel | Model **WACC = 11.59% Base** (`DCF!D12`); spec says 10.85% | **Mismatch (1pp low)** |
| 5 | Comp-set beta 1.32 (relevered) | margin panel | Spec says β unlevered 0.81-0.85 (CLAUDE.md WACC research) | **Mismatch (significantly high)** |
| 7 | Members 2.5M → 8.4M | unit econ chain | Slide 5 says 11.4M for same 7-year horizon. Model uses 10.9M Base spec target. | **Internal contradiction** |
| 7 | Member CAGR 18% (chain) vs 20.2% (panel) | unit econ + top-line | Slides internally inconsistent | Flag |
| 7 | ARPU $305 → $417 (chain) vs $305 → $348 (panel) | unit econ chain vs top-line | Internally inconsistent on the same slide; spec Base $347 by 2033 matches the $348 number | Flag |
| 7 | Revenue $0.87B → $3.27B | unit econ chain | Model `DCF!D8:K8` = $0.89B (2026) → $3.74B (2033). Closer to model. | Match (rough) |
| 7 | EBITDA margin 18% → 37% terminal | unit econ chain | Slide 5 says 26% terminal. Model FCF margin 2033 = 20.8%. EBITDA margin would be higher; not directly verifiable from extracts but the **18→37 jump is much more aggressive than slide 5's 26%**. | **Internal contradiction** |
| 7 | WACC 10.79% (with βU 0.97 × ERP 4.61%, +Cost of equity 8.79%, +Private co premium 2.00%) | WACC build panel | Model **WACC Base 11.59%**. Spec methodology says ERP 4.5%, β unlevered 0.81-0.85 (≠ 0.97), no separate "private co premium 2%" in spec. | **Mismatch** |
| 7 | Exit multiple 3.5× | terminal panel | Model `DCF!C21 = 3.5x` Base | Match |
| 7 | Perpetual growth g 3.0% | terminal panel | Match | Match |
| 7 | Terminal Value $11.9B / $11.4B | terminal panel | Model `DCF!C22 = 13.09B` (exit multiple), `DCF!C23 = 9.32B` (Gordon), `DCF!C25 = 11.20B` (selected blend) | Close on selected ($11.2B); slide presents two figures unclearly |
| 8 | EV → Equity waterfall: PV FCF +4.1, PV TV +5.2, EV 9.3, −0.6, +0.4, −0.7 = $8.4B | waterfall | Model: PV FCF 1.83, PV TV 4.92, **EV 6.75**, −0.01 debt, +0.74 cash, **Equity 7.48** (`DCF!C30:C38`). **Slide values are ~38% higher than model.** | **Major mismatch** |
| 8 | Sensitivity range $5.8B — $12.1B | sensitivity range | Model 2D heatmap (`Memo!B66:H73`) range $4.68B-$11.04B at extremes; close to slide range | Roughly match |
| 8 | Tornado bars: WACC ±2.8 / Term EBITDA ±2.0 / Sub growth Y3 ±1.6 / Term churn ±1.1 / Term g ±0.7 | tornado | Model `Memo!A35:A47` ranking: Members > Term EV/Rev > WACC > R&D > SBC > G&A > etc. **Spec & model both put MEMBERS first** — slide doesn't include Members at all. | **Critical mismatch — Members missing from tornado** |
| 9 | Real Options 01 Health-data +$1.6B / 02 Med-device +$0.9B / 03 Enterprise +$0.5B → +$3.0B aggregate | RO build | Model `DCF!C45 = $940M` Base, `C44 = $2,834M` Bull. Spec says total RO at neutral conviction = $1.29B and **NOT additive**. | **Conceptual mismatch (additivity) + ~$3B slide vs $0.94B model base** |
| 9 | Stylized Black-Scholes inputs (S=$3.4B, K=$1.8B, σ=52%, T=5y, r=4.2%, C=$3.0B) | input panel | Spec uses decision-tree (Lecture 3B Arundel-style, real-world probabilities, no replicating portfolio because underlying isn't tradable). Black-Scholes framing is **methodologically wrong per spec**. | **Methodology mismatch** |
| 10 | Garmin 2.4× / GoPro 0.9× / Fitbit 1.6× / Sonos 3.2× / Peloton 2.6× / Roku 4.1× / Dexcom 9.4× / Masimo 7.8× / iRhythm 10.2× / Inspire 8.6× | comp scatter | Model `Comps!E19:E27`: PTON 1.22 / SONO 1.07 / GPRO 0.40 / SPOT 3.66 / ROKU 3.02 / DXCM 4.24 / IRTC 4.65 / RMD 5.23 / MASI 5.96 / GRMN 5.25 | **Mismatch** — slide multiples are 2-2.5x higher than model across the board (looks like slide is using older / different comp pull, possibly 2023 data) |
| 10 | Hardware bucket $2.2B (2× rev × ~$1.1B rev) | implied EV | Model uses recognized rev $528M; bookings $1.1B. Spec uses recognized basis. 2× $1.1B = $2.2B uses bookings. Spec base methodology says use recognized. | Methodology mismatch — uses bookings not recognized |
| 10 | Subscription bucket $3.9B (3.5× rev) | implied EV | Model `Comps!D54 = $3.67B` (bookings × EV/Rev median 3.34); `D55 = $3.62B` (recognized GP × EV/GP). 3.9 is in range. | Match (rough) |
| 10 | Health-data bucket $9.4B (8.5× rev) | implied EV | Model `Comps!D64 = $2.61B` recognized × EV/Rev (median 4.94); `D67 = $6.60B` bookings GP × EV/GP. 8.5x is **above max model multiple**. | **Mismatch — spec & model multiples 4.2-5.96x; slide 8.5x looks like 2023 peak data** |
| 10 | Post-IPO fates: Peloton −70%, Garmin +85%, Dexcom +400% | post-IPO panel | Directional anchors; not in model | Anecdotal (no model cross-check) |
| 11 | Common-equivalent bridge: $10.1B − $0.9B liq pref − $0.6B ratchet − $0.4B participation = $8.2B | bridge | CLAUDE.md says all prefs 1× non-participating pari passu — **there is no ratchet** documented (Series F ratchet "not found", SoftBank absent). Liq pref bridge is speculative. | **Source-unsupported — flag as fabricated** |
| 11 | Implied @$8.2B vs base case: subs 8.4M vs 7.1M, term margin 29% vs 26%, rev CAGR 26% vs 22%, churn 12% vs 14%, WACC 9.5% vs 10.5% | comparison table | Same WACC / margin numbers as slide 5 (which itself disagrees w/ model) | Compounding mismatches |
| 11 | Common-equiv gap ~$1.9B | bottom-right callout | $10.1B − $8.2B = $1.9B | Internal-arithmetic match (but premise wrong) |
| 12 | Method 01 DCF range 5.8-12.1 / Method 02 DCF+RO 7.4-14.9 / 03A HW 1.2-2.8 / 03B Sub 3.0-4.6 / 03C HD 7.4-13.0 / 04 Series G common-equiv $8.0-9.0 | football field bars | Model Football Field: DCF 2.5-19.9 / DCF+RO 2.66-22.6 / Comps 1.18-7.55 / Series G 10.1 / IPO 11.88-13.47. **Slide ranges don't reflect model.** | **Major mismatch — slide football field doesn't agree with model Football Field tab** |
| 12 | Central estimate $9.6B | central callout | Model weighted avg = $7.11B (`Football Field!D18`); spec weighted avg = $8.63B; spec intrinsic alone = $11.2B | **Mismatch — slide $9.6B doesn't match any model output** |
| 12 | Verdict OVER ~6% | verdict callout | Spec verdict: +11% UNDER | **CRITICAL — verdict reversed** |
| 13 | Churn +200bps → DCF base drops ~14%; verdict flips OVER ~25% | trigger 1 | Sensitivity directionally reasonable; not directly cross-checkable | Flag |
| 13 | Healthcare option fails → central falls to ~$8.4B | trigger 2 | Removing $940M base option from $9.0B-ish central leaves ~$8.0B; close | Match (rough) |
| 13 | IPO Peloton trajectory → multiple compresses 60-70%, Series G overstates by ~50% | trigger 3 | Directional, not cross-checkable | Flag |
| 14 | "headline overstates common-equivalent value by ~6%" | closing line | Spec: +11% UNDER | **CRITICAL — verdict reversed** |

---

## 5. Top-5 highest-leverage gaps to fix first

### Gap 1 — Verdict polarity is reversed (Critical)
**What:** Slides 12 and 14 close with "modestly OVER ~6%" / "headline overstates by ~6%". Spec closes with "Series G is mildly UNDERPRICED, +11% premium." Slides 9 & 11 reinforce wrong direction (RO additive bridge to $11.4B; Series G "discounted" to $8.2B common-equiv).
**Why it matters:** This is the project's central thesis. Reversing it kills the a16z American Dynamism framing, the Jensen Gap motivation, and the "novelty" grade component.
**Build path:** Rewrite slides 12 and 14. Replace pref-discount logic with intrinsic-value-vs-Series-G framing. Headline: $11.2B intrinsic vs $10.1B Series G = +11% UNDER. Drop the pref bridge entirely (or move to caveats).

### Gap 2 — Jensen Gap slide does not exist (Critical)
**What:** Slide 6 contains raw planning text that *mentions* Jensen but is not a built slide. The spec's most-novel slide (input-level $8.0B vs scenario-level $11.2B; convexity diagram) is missing.
**Why it matters:** Jensen Gap is the single 12.5% novelty/interest grade lever. Without it the deck has no methodological centerpiece.
**Build path:** New slide 6. Two-anchor diagram with $8.09B (model `DCF!C63`) and $11.45B (model `DCF!D65`, scenario-weighted Equity+Options Neutral). Convexity sketch. WHOOP-specific correlation list (members×margins, members×multiple, members×WACC, ARPU×multiple).

### Gap 3 — Members visualization uses wrong target and is missing four-lens triangulation (Critical)
**What:** Slides 5 and 7 have conflicting Members targets (11.4M vs 8.4M); neither matches spec Base 10.9M. The four-lens triangulation visual (TAM, Peloton-shifted, Multi-comp, Capital-led) — flagged in spec as a top-3 visual to polish — is absent.
**Why it matters:** Members is the #1 sensitivity driver per the model tornado (Memo!A35); the deck currently misrepresents it AND fails to present the most credibility-earning visual in the project.
**Build path:** Single DCF-architecture slide (delete the duplicate). Members 2.5M → 10.9M. Build the four-lens converging chart (TAM 8.55M / Peloton-shifted 11.42M / Multi-comp 10.5M / Capital-led 8.4M, median ~10.5M, calibrated 10.9M). Pull WACC 11.59% from model.

### Gap 4 — Real Options slide directly contradicts spec methodology (Critical)
**What:** Slide 9 stacks three real options additively ($1.6B + $0.9B + $0.5B = $3.0B premium on top of DCF), uses Black-Scholes framing. Spec mandates exactly the opposite: RO is exhibit-only (not additive), uses decision-tree (Arundel/Lecture 3B), and double-counts with Bull bucket-3 multiple. Spec architecture iteration #5 specifically rejected the additive approach.
**Why it matters:** Anyone who reads the spec and then the deck will see directly contradictory analytical claims. Q&A defense impossible — the team would have to pick one.
**Build path:** Rebuild slide as exhibit/cross-validation: show RO computed value $940M Base / $164M Bear / $2.83B Bull (model `DCF!C43:C45`), label as "computed but NOT additive — healthcare flows through Bull fundamentals." Frame as Lecture 3B engagement, not as primary valuation.

### Gap 5 — Tornado is missing the dominant driver (High)
**What:** Slide 8 tornado bars cover WACC, Terminal EBITDA, Subscriber growth Y3, Terminal churn, Terminal g — but **does NOT include Members**. Model `Memo!A35` ranks Member Growth (MG1-MG8) #1 with $2,347M Bear-side delta — by far the largest sensitivity. Spec calls out Members > Terminal > WACC > FCF margin > ARPU > healthcare-option as the canonical ranking.
**Why it matters:** Sensitivity slide is what the audience uses to pressure-test the answer. Omitting the largest driver makes the analysis look incomplete and shifts attention to secondary inputs.
**Build path:** Rebuild tornado from `Memo!A35:G47` ranking. Add Members × WACC heatmap (currently model has WACC × Exit Multiple — needs new grid). Surface the spec callout that ARPU rank-5 confirms ARPU discipline didn't cost much.

---

## Notes for caller

- Multiple comp multiples on slide 10 look like 2023 peak values (Dexcom 9.4×, iRhythm 10.2×, Masimo 7.8×) vs current model values 4.2-5.96×. Suggest verifying source date.
- Slide 11 liquidation-pref bridge ($0.6B "ratchet" + $0.4B "participation") has no source in CLAUDE.md research; CLAUDE.md explicitly says "all prefs 1× non-participating pari passu." This appears fabricated.
- Page-number labels in deck headers go 01, 02, 02, 03, 04, (none), 05, 05, 06, 07, 08, 09, 10, 11 — duplicate "02" and "05", labeled "/12" but only 14 slides. Renumbering pass needed regardless of content fixes.
- Slide 5 is the only slide that contains the WHOOP-style "Phase 1/2/3 over Y1-Y7" chart structure and Slide 7 is its near-duplicate; recommend keeping slide 7's denser data panels and dropping slide 5's redundant chart.
- Numbers ledger flagged 4 internal contradictions on slide 5 vs slide 7 (Members, ARPU, EBITDA margin, WACC) — these are inside the deck itself, not just deck-vs-spec.
