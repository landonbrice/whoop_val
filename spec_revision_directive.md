# Revision Directive: Spec v1 → v2

**Prepared:** April 16, 2026  
**Target document:** `2026-04-16-assumption-inventory-design.md`  
**Execution:** Hand this directive to Claude Code with the instruction below.

---

## Execution Instruction for Claude Code

Apply each change in this directive sequentially to the target spec file. Preserve the existing markdown structure, table formatting, and numbering conventions. For each change, follow the "Action," "Content," and "Insertion Point" specifications exactly. When a change requires modifying existing text, preserve surrounding context and only replace the specified content.

After all changes are applied:
1. Update the Summary Statistics table in the Overview to reflect new assumption counts
2. Update the Total row to reflect the new grand total
3. Run a consistency check: verify all cross-references still resolve (e.g., if C5 references Dexcom, ensure the reference is accurate)
4. Report any changes that could not be applied cleanly

Do not add commentary or meta-discussion to the spec. The spec is a specification, not a dialogue. Edit, don't interpret.

---

## Change 1: Add Take-Private Exclusion to Overview

**Action:** Insert new subsection in the Overview section, after the "Architecture" bullet list.

**Rationale:** The exclusion of take-private LBO as a valuation leg is an important methodological decision that should be explicit, not implicit through omission.

**Content to insert:**

```markdown
### Methodological Exclusion: Take-Private LBO

Take-private LBO is deliberately excluded from the football field. Three 
structural reasons:

1. **Capital structure is wrong for LBO.** WHOOP is all VC preferred with
   minimal debt capacity. Leverage cannot be applied to a cash-flow-positive
   growth business at the scale LBO economics require (5-7x EBITDA).
2. **IPO path is locked in.** Series G included sovereign wealth 
   (QIA, Mubadala) and crossover investors. These parties require public-
   market liquidity, not another private hold period.
3. **Strategic acquirers are partially foreclosed.** Abbott chose investor
   path rather than acquirer path. Apple/Google face antitrust friction in
   wearables M&A at this scale.

Strategic acquisition (distinct from LBO) IS captured via precedent 
transactions and remains a non-zero-probability tail scenario.
```

**Insertion point:** After the "Sourcing Stack" table (before the "Summary Statistics" table).

---

## Change 2: Add Section 6 — Precedent Transactions

**Action:** Insert new full section after Section 5 (DCF Mechanics), before "Priority Research Targets."

**Rationale:** Precedent Transactions is listed as one of five valuation methods in the Overview but has no dedicated assumption section. This gap leaves the football field with only four enumerable methods.

**Content to insert:**

```markdown
## Section 6: Precedent Transactions

**Feeds:** Football field (precedent transactions leg, 5-10% triangulation weight), 
Cross-check on trading comp regime, Strategic-acquirer scenario as tail option.

**Role:** Narrow-band reality check rather than primary triangulation input. 
Precedent transactions answer two questions trading comps cannot: 
(1) what do acquirers pay with control premium embedded, and 
(2) what through-cycle multiples look like across different macro regimes.

### Part A: Deal Set Assumptions

| # | Assumption | Base Case | Priority | Source | Status |
|---|---|---|---|---|---|
| P1 | Deal inclusion window | Last 5 years (2021-2026), with 3-year primary focus | High | Design decision | Locked |
| P2 | Deal inclusion criteria | Wearables, digital health, consumer subscription, medical device — matched to three-bucket framework | High | Design decision | Locked |
| P3 | Deal size threshold | $500M+ enterprise value (small deals have multiples distorted by synergy math) | Medium | Design decision | Locked |
| P4 | Initial deal set | See Part B | Critical | Pitchbook M&A module, press | **Unsourced** |
| P5 | Multiple extraction method | EV / LTM revenue at announcement date; EV / NTM revenue where available | High | Per-deal research | Needs pull |
| P6 | Control premium treatment | Embedded in precedent multiples; do NOT add additional premium on top | Structural | Design decision | Locked |
| P7 | Regime classification per deal | Tag each deal as ZIRP-peak / transition / current-regime | Medium | Judgment + macro data | Design decision |
| P8 | Outlier exclusion policy | Exclude deals where strategic synergies drove multiple 2x+ above peer median | Medium | Per-deal judgment | Design decision |

### Part B: Initial Deal Set

Organized by bucket to match comps framework:

**Bucket 1 analog (Consumer Hardware):**
- Fitbit / Google (2021) — ~$2.1B / ~1.3x revenue — distressed, failed subscription pivot
- Garmin / Firstbeat Analytics (2020) — small tuck-in, reference only

**Bucket 2 analog (Consumer Subscription):**
- Peloton / Precor (2020) — $420M / hardware manufacturing play
- Any Mirror/Tonal-era fitness M&A if applicable
- Strava acquisitions if available

**Bucket 3 analog (Health Data / Medical Device):**
- Masimo / Sound United (2022) — ~$1B / consumer audio + connected health
- Dexcom / Pops Diabetes Care (2022) — ~$900M / diabetes software
- Boston Scientific / BTG (2019) — reference for medical device multiples
- iRhythm / ZIO patent deals if any
- Beddit / Apple (2017) — small but relevant to sleep-tech acquisition patterns

### Part C: Analytical Outputs

| Output | Purpose |
|---|---|
| Median + IQR multiple by bucket | Direct application to WHOOP's bucket-weighted metrics |
| Through-cycle multiple range | Ground check on 2026 trading comp multiples |
| Strategic premium inference | Benchmark for tail scenario if Abbott/Apple/Google steps in |

### Research Budget

**2-3 hours total.** Lower than comps or DCF because the method is a 
reality check, not a core triangulation input. Pull deals, compute 
multiples, produce range. Move on.
```

**Insertion point:** After line 444 (end of Section 5 Part F), before the "Priority Research Targets" section at line 469.

**Update needed:** Priority Research Targets section should add one entry:

```markdown
| 11 | **Precedent M&A deals (Fitbit, Masimo, Dexcom-Pops, etc.)** | Precedent transactions leg of football field | Pitchbook M&A, SEC filings of acquirers |
```

---

## Change 3: Add IPO Trading Range Assumptions

**Action:** Expand Section 4's "Three-Stage Discount Framework" subsection with enumerated assumptions. The framework is currently descriptive; it needs assumption numbers.

**Rationale:** The Implied IPO Trading Range is one of five valuation methods but its underlying assumptions are implicit in the three-stage calculation, not enumerated. Enumeration makes them auditable and sensitivity-testable.

**Content to replace:**

Current Section 4 has a "Three-Stage Discount Framework" subsection with narrative text and a conceptual table. Replace with the same narrative PLUS the following assumption table inserted after the "Series G investors' implicit belief" paragraph:

```markdown
### IPO Trading Range Assumptions (Numbered)

| # | Assumption | Base Case | Priority | Source | Status |
|---|---|---|---|---|---|
| I1 | IPO timing window | 12-18 months from Series G (Q2 2027 - Q1 2028) | High | Press, Series G investor commentary | Tier 2 |
| I2 | IPO pricing discount (to Stage 1 fair value) | 15-25% | Critical | IPO pricing studies (Loughran/Ritter), recent tech IPO performance | Tier 2 |
| I3 | Illiquidity/timing discount (current private vs. IPO price) | 5-15% | High | Academic literature on pre-IPO DLOM shrinkage near IPO window | Tier 3 |
| I4 | Series G required investor IRR | 20-30% over 3-5 year hold | Medium | Late-stage growth equity return expectations | Tier 3 |
| I5 | Implied Stage 1 public fair value | $13-15B (from back-solve) | Derived | Calculated from $10.1B / (1 - I3) / (1 - I2) | Derived |
| I6 | Sensitivity on Stage 1 | Report range across I2 and I3 bounds | High | Derived | Needs build |

**Interpretation:** The $10.1B Series G mark, backed out through I2 and I3, 
implies Series G investors are underwriting a public-market fair value of 
$13-15B. This is the number the intrinsic DCF and comps analysis need to 
support or contest — not the $10.1B private mark.
```

**Insertion point:** In Section 4, replace the existing "Three-Stage Discount Framework" subsection content (currently at approximately lines 286-300) with expanded content including this table. Preserve the existing stage explanations and back-solve logic; add the enumerated table beneath them.

---

## Change 4: Add R19 — Non-Subscription ARPU Decomposition

**Action:** Add new assumption R19 to Section 1's assumption table.

**Rationale:** The spec flags that effective ARPU (~$440) vs. subscription-only math (~$265) creates a $175 gap as a "future session" item. But this gap is load-bearing for bucket-3 weighting (determines whether non-sub revenue is Labs, accessories, or plan mix) and should be an explicit assumption with candidate decompositions.

**Content to insert:**

Add row R19 to Section 1's main assumption table:

```markdown
| R19 | Non-subscription ARPU decomposition | $175/member gap between R4 ($440) and subscription-only math (~$265). Three candidate decompositions modeled (see below) | **Critical for bucket-3** | DCF (revenue mix), Comps (bucket weighting), Real Options (D19, D21) | Pitchbook, Labs pricing, press on Labs uptake | **Unsourced — load-bearing** |
```

Then add this subsection after the "Key Dependencies" bullet list at the end of Section 1:

```markdown
### R19 Decomposition Candidates

| Candidate | Accessories | Labs | Plan Mix | Bucket-3 Implication |
|---|---|---|---|---|
| R19a — Accessories-heavy | $100 | $40 | $35 | Bucket 2 bias; WHOOP is a subscription-merch business |
| R19b — Labs-heavy | $40 | $110 | $25 | Strong bucket 3 bias; healthcare platform thesis validated |
| R19c — Plan-mix heavy | $50 | $50 | $75 | Neutral; tier upgrades driving ARPU, mixed thesis |

**The correct decomposition is a research target.** Until sourced, model 
all three as sensitivity scenarios. The choice directly affects bucket-3 
weighting (V11) and therefore the football field multiple range.
```

**Insertion point:** Add R19 row to the Section 1 assumption table. Add decomposition subsection after the existing "Key Dependencies" section.

---

## Change 5: Add Rationale Note to C5

**Action:** Modify the C5 row in Section 2's assumption table.

**Rationale:** C5 asserts WHOOP subscription GM of 75-85% at steady state, which exceeds Dexcom's 64%. This structural difference needs rationale or a reviewer will question the assumption.

**Content to modify:**

Current C5 row:
```markdown
| C5 | Subscription gross margin (standalone) | 75-85% at steady state | Critical | DCF | Peer: pure SaaS ~80%, Dexcom ~64% | Tier 3 |
```

Replace with:
```markdown
| C5 | Subscription gross margin (standalone) | 75-85% at steady state | Critical | DCF | Peer: pure SaaS ~80%, Dexcom ~64% | Tier 3 |

**C5 rationale:** WHOOP subscription margin is structurally higher than 
Dexcom's because Dexcom's "subscription" revenue includes consumable 
sensor replacements (recurring hardware COGS), while WHOOP's subscription 
is pure software/data delivery with hardware treated as a separate 
one-time cost at acquisition. This is also why WHOOP's trading multiple 
is not directly comparable to Dexcom's at face value — WHOOP's recurring 
revenue is arguably higher quality (pure software margins), which 
supports a premium within the growth-adjusted framework.
```

**Insertion point:** In Section 2 assumption table, after the C5 row, insert the rationale note as a paragraph before the C6 row.

---

## Change 6: Add Section 7 — Research Execution Policy

**Action:** Insert new full section after Section 6 (Precedent Transactions) and before "Priority Research Targets."

**Rationale:** The spec currently has 28 unsourced critical assumptions and a 10-item priority research list, but no exit criteria, fallback policies, or response protocols for when things go wrong. For an overnight autonomous run on Mac Mini with Playwright, these protocols are not optional — they're what prevents the agent from hanging, rabbit-holing, or producing garbage.

**Content to insert:**

```markdown
## Section 7: Research Execution Policy

This section defines how research is executed, when to stop, what to do 
when data is unavailable, and how to handle mid-project surprises. Designed 
for both manual work sessions and autonomous overnight runs on 
Mac Mini with Playwright.

### Part A: Time-Boxing

| Rule | Specification |
|---|---|
| Per-target time box | **3 hours maximum per priority research target** |
| Total research budget | **~30-40 hours across all priority targets** |
| Per-target minimum | Must produce at least a Tier 3 estimate before moving to next target |
| Overnight run limits | Each overnight session: max 4 targets; auto-checkpoint every 30 min |

**Rationale for 3-hour box:** tight enough to enforce discipline, loose 
enough to accommodate research dead-ends and retries. 2 hours is too 
aggressive for Pitchbook scraping + triangulation; 4+ hours enables 
rabbit-holing.

### Part B: Data Sourcing Fallback Logic

For each unsourced assumption, follow this cascade:

```
Tier 1 (Primary):     Pitchbook / Capital IQ / official filings
          ↓ (if unavailable after 90 min)
Tier 2 (Triangulated): Credible press (Bloomberg, TechCrunch, Sacra) + analyst estimates
          ↓ (if still unavailable)
Tier 3 (Reasoned):    Peer data + first-principles estimate, with explicit logic trail
          ↓ (if even this is unreliable)
FLAGGED_GAP:          Mark as "sensitivity only" — model range, do not commit to point
```

Every assumption must land at Tier 3 or better, OR be explicitly marked 
as FLAGGED_GAP. Do not fabricate. Do not leave blank.

### Part C: Research Failure Protocol

When a priority target cannot be sourced within its 3-hour box:

1. **Log what was found** (even if partial) in a dated research note
2. **Commit to Tier 3 estimate** using the fallback logic above
3. **Flag as "low confidence"** in the model with a comment
4. **Continue to next target** — do not block on unresolvable data
5. **Revisit only if modeling surfaces the assumption as load-bearing**

For the Mac Mini overnight run specifically: if Playwright hits 
authentication failure on Pitchbook, skip to SEC filing targets and log 
the Pitchbook failure. Do not spend overnight cycles retrying failed 
authentications.

### Part D: Model Diagnostic Protocol

When the DCF, comps, and precedent methods produce divergent valuations 
(>50% spread between highest and lowest method), triage as follows:

1. **First, check terminal value dominance.** If DCF terminal value is 
   >75% of enterprise value, the explicit forecast is doing too little 
   work. Revisit growth deceleration curves.
2. **Second, check multiple compression.** If terminal multiples are 
   close to current comp multiples, you forgot compression. Apply the 
   40-60% compression factor per D28.
3. **Third, check growth-adjusted multiples.** If comp set has widely 
   varying growth rates (Dexcom 20%, Garmin 10%), raw multiples are 
   misleading. Normalize per V8.
4. **Fourth, check WACC consistency.** If WACC is held constant across 
   scenarios but business risk differs materially, bear case is 
   under-discounted.
5. **If divergence persists**, the assumption inconsistency is itself 
   the finding. Document which methods disagree, what assumption bridges 
   them, and what would have to be true for reconciliation. This is 
   publishable analytical content.

### Part E: Unknowable Assumption Protocol

Some assumptions cannot be sourced at any tier (R11 churn, R14 attach 
rates, S3 preferences without S-1 access). These are genuinely unknowable 
from public data.

Policy:
1. **Do not pretend** to have sourced them. Mark as "Tier 3: estimated, 
   genuinely unknown"
2. **Model as sensitivity ranges**, not point estimates
3. **Report the sensitivity in the memo** — show how the valuation moves 
   across the plausible range of the unknown assumption
4. **Use peer data as ceiling/floor**, not as point estimate (e.g., 
   Peloton churn ~45% as upper bound, Dexcom ~10% as lower bound, 
   WHOOP somewhere in between with honest uncertainty)
5. **For the memo**: the existence of unknowable assumptions is itself 
   a finding. State explicitly: "the central range of $X-Y billion 
   contains $Z billion of sensitivity to unknowable assumptions, which 
   is why the Series G syndicate demanded participation rights / FDA 
   milestones / etc."

### Part F: Framework Revision Protocol

If research surfaces something that challenges the spec itself (e.g., 
WHOOP has a major product line not in the framework; or a regulatory 
event materially changes the bucket-3 weighting):

1. **Stop research.** Do not continue pulling data based on a framework 
   that no longer fits reality.
2. **Document the discovery** in a dated research note with specific 
   citation.
3. **Propose a spec revision** — which assumptions change, which 
   remain, what new assumptions are needed.
4. **Request approval before proceeding** if working collaboratively; 
   log and continue with flagged change if solo.
5. **Update CLAUDE.md** to reflect the new framework state.

**Do not silently adapt** the framework based on new information. The 
spec's value comes from being a commitment device; changing it silently 
undermines the commitment.

### Part G: Definition of Done (Research Phase)

Research phase is complete when ALL of the following are true:

- [ ] All 10-11 priority research targets have been attempted (not 
      necessarily sourced, but attempted)
- [ ] Every CRITICAL assumption has either a Tier 1-2 source OR an 
      explicit FLAGGED_GAP marker with sensitivity range
- [ ] Total research hours ≤ 40
- [ ] Research log is complete, dated, and linkable from spec
- [ ] A "research findings summary" document exists, one paragraph per 
      priority target, with source attribution

When all boxes are checked, move to model construction. Do not keep 
researching to close the last 10% of gaps; remaining gaps become 
sensitivity ranges in the model.
```

**Insertion point:** After Change 2's new Section 6, before the "Priority Research Targets" section.

---

## Change 7: Update Summary Statistics Table

**Action:** Modify the Summary Statistics table in the Overview to reflect new assumptions added by changes above.

**Content to modify:**

Current summary:
```markdown
| Category | Assumptions | Critical | Unsourced | Locked |
|---|---|---|---|---|
| Section 1: Revenue & Growth | 18 | 6 | 5 | 2 |
| Section 2: Cost Structure & Margins | 17 | 7 | 6 | 1 |
| Section 3: Capital Structure & Cap Table | 17 | 5 | 10 | 0 |
| Section 4: Comparable Companies | 19 | 8 | 4 | 0 |
| Section 5: DCF Mechanics | 29 | 12 | 3 | 0 |
| **Total** | **100** | **38 Critical** | **28 Unsourced** | **3 Locked** |
```

Replace with:
```markdown
| Category | Assumptions | Critical | Unsourced | Locked |
|---|---|---|---|---|
| Section 1: Revenue & Growth | 19 | 7 | 6 | 2 |
| Section 2: Cost Structure & Margins | 17 | 7 | 6 | 1 |
| Section 3: Capital Structure & Cap Table | 17 | 5 | 10 | 0 |
| Section 4: Comparable Companies | 19 | 8 | 4 | 0 |
| Section 4B: IPO Trading Range | 6 | 2 | 2 | 0 |
| Section 5: DCF Mechanics | 29 | 12 | 3 | 0 |
| Section 6: Precedent Transactions | 8 | 1 | 1 | 4 |
| **Total** | **115** | **42 Critical** | **32 Unsourced** | **7 Locked** |
```

---

## Change 8: Update Priority Research Targets

**Action:** Modify the Priority Research Targets table to reflect new Section 6 additions and to integrate with Section 7's time-boxing policy.

**Content to modify:**

Current table lists 10 priorities. Add entry 11 (precedent transactions) and add a time-box column:

```markdown
| Priority | Target | Time Box | What It Unlocks | Source |
|---|---|---|---|---|
| 1 | Peloton 10-Ks (2019-2025) | 3 hrs | S&M trajectory, GM decomposition, churn disclosures | SEC EDGAR |
| 2 | Pitchbook: WHOOP tearsheet | 3 hrs | Churn, retention, unit economics, gap financing | Playwright → Pitchbook |
| 3 | Pitchbook: Oura profile | 3 hrs | Closest private comp — valuation, revenue, implied multiple | Playwright → Pitchbook |
| 4 | Dexcom 10-K | 2 hrs | R&D intensity, GM structure, regulatory pathway | SEC EDGAR |
| 5 | Comp multiples pull (7 public comps) | 3 hrs | Current + historical EV/Rev at 4 time points | Public data |
| 6 | Pitchbook: WHOOP cap table | 3 hrs | Shares, preferences, option pool, secondary activity | Playwright → Pitchbook |
| 7 | Forge/EquityZen: WHOOP secondary | 2 hrs | Common share price signal | Web search |
| 8 | Damodaran ERP + beta data | 1 hr | WACC inputs | Damodaran website |
| 9 | WHOOP pricing history | 1 hr | Historical pricing changes | Web Archive |
| 10 | Remaining 10-Ks (GRMN, RMD, MASI, IRTC) | 3 hrs | Complete comp profiles | SEC EDGAR |
| 11 | Precedent M&A deals | 2 hrs | Precedent transactions leg + regime check | Pitchbook M&A, press |

**Total time budget:** 26 hours. Remaining 4-14 hours available for 
retries, triangulation, and gap closure per Section 7 policy.
```

---

## Change 9: Minor — Tighten Meta-Commentary

**Action:** Remove duplicate emphasis where the same analytical framing appears multiple times.

**Rationale:** Spec should read like specification, not dialogue. Some framings are emphasized two or three times.

**Specific removals:**

1. In Section 2, the "Peloton 10-Ks as priority" point appears in both the assumption table (C9c) and in a separate "Key Research Priority" subsection at the end. Retain in C9c, remove or compress the end-of-section subsection.

2. In Section 4, "both are defensible, report both" appears in multiple framings. Retain the single clearest statement under the Dual Back-Solve section; remove restatements elsewhere.

3. Move any process-level commentary ("this is the central question of the paper") to an appendix or footnote if kept; don't repeat inline.

**Action for each:** identify and delete duplicative paragraphs. Do not remove the underlying assumptions or table rows.

---

## Change 10: Update Next Steps Section

**Action:** Replace the existing "Next Steps" section at the end of the spec.

**Rationale:** The existing Next Steps list is short and implementation-light. With Section 7 now defining research execution policy, Next Steps should be operational.

**Content to replace:**

Current:
```markdown
## Next Steps

1. **Research execution plan** — sequence the 10 priority research targets into work sessions
2. **Pitchbook scraping session** — Playwright-driven pull of WHOOP, Oura, and cap table data (targets 2, 3, 6)
3. **SEC filing pulls** — Peloton and Dexcom 10-K analysis (targets 1, 4)
4. **Comp multiples build** — Pull and compute current + historical multiples for all 7 public comps (target 5)
5. **Excel model scaffolding** — Set up the workbook structure with assumption cells linked to this spec
```

Replace with:
```markdown
## Next Steps

### Immediate (before first research session)

1. Confirm Playwright + Pitchbook authentication works end-to-end on a 
   throwaway query (e.g., pull Peloton's Pitchbook page as test)
2. Create research log template in /research/ directory
3. Set up Excel model scaffold skeleton with assumption cells linked to 
   this spec by assumption number

### Research Phase (per Section 7 policy)

1. **Session 1 (overnight):** Targets 1, 2, 3 — Peloton 10-Ks, WHOOP 
   Pitchbook, Oura Pitchbook. ~9 hours wall time; Playwright for 
   Pitchbook, SEC for Peloton.
2. **Session 2 (overnight):** Targets 4, 5, 6 — Dexcom 10-K, comp 
   multiples, WHOOP cap table. ~9 hours wall time.
3. **Session 3 (manual or overnight):** Targets 7-11. ~9 hours wall time.
4. **Gap closure (manual):** Review all FLAGGED_GAP assumptions, 
   triangulate Tier 3 estimates, finalize research findings summary.

### Model Construction (after research phase)

1. Excel DCF build — populate scaffold from research outputs
2. Cap table + waterfall model
3. Comps + precedent transactions workbook
4. Football field synthesis
5. Sensitivity tables per D27 specifications

### Synthesis

1. IC memo draft
2. Football field slide
3. Peer review cycle
```

---

## Post-Application Checklist

After applying all changes, Claude Code should verify:

- [ ] Summary Statistics table reflects new assumption counts (115 total, 42 critical)
- [ ] New sections (6, 7) are properly integrated with consistent markdown formatting
- [ ] Take-private exclusion is explicit in Overview
- [ ] R19 is in Section 1 with decomposition subsection
- [ ] C5 has rationale note
- [ ] IPO Trading Range has enumerated assumptions (I1-I6)
- [ ] Precedent Transactions has full section with deal set and budget
- [ ] Research Execution Policy is a complete new Section 7
- [ ] Priority Research Targets has time-box column and Target 11
- [ ] Next Steps is updated with session-level plan
- [ ] No duplicate meta-commentary remains

Report any changes that could not be applied cleanly. Do not interpret ambiguity; ask.
