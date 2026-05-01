# WHOOP Churn Dynamics — Deep Dive

**Date:** May 1, 2026
**Purpose:** Replace the model's flat-annual churn assumption with a defensible cohort-aged framework specific to WHOOP. Identify what we know, what we're inferring, and what would resolve the remaining uncertainty.
**Status:** First pass; feeds R10/R11 architecture for model rebuild.

---

## 1. Why churn is the single most consequential assumption

Churn cascades into every other valuation lever:

| Downstream | Sensitivity to churn |
|---|---|
| **LTV** | At $300 ARPU and 70% sub GM: 1.5%/mo monthly churn → $1,176 LTV; 3.0%/mo → $583 LTV. **2x swing** for a 100bp monthly delta. |
| **LTV/CAC** | Below 3x = bear case territory; above 5x = healthcare-platform territory. The whole 22-bp range above sits inside the same plausible bracket. |
| **Comp bucket weighting** | High churn → Bucket 2 distressed end (Peloton). Low churn → Bucket 3 health-data justification holds. Single biggest input into "what is WHOOP." |
| **Terminal multiple** | High-churn business deserves perpetuity multiple compression. Low-churn business holds Dexcom-adjacent multiples even at slowing growth. |
| **Real options probability** | Healthcare reimbursement option requires demonstrated retention — HCPs won't prescribe a wearable if patients drop off in 6 months. Churn directly gates the highest-value real option. |

**Bottom line:** This isn't a model line item. It's the central thesis variable. Getting churn wrong by 50bp/mo (a defensible margin given our data) swings DCF EV by $2-3B.

---

## 2. What WHOOP has actually disclosed

The total evidence base is thin. Here's everything publicly available, ranked by quality:

| Source | Metric | Value | Quality | Subset? |
|---|---|---|---|---|
| Series G press release (Mar 2026) | Monthly churn — **Pro tier only** | "<3%" | High on the point | **YES — premium tier, not blended** |
| Sacra equity research (paywalled summary visible) | "Retention rate" (undefined) | ">80-85%" | Medium | Likely 12-mo annual retention; unclear if cohort-based or trailing |
| WHOOP marketing | Daily app opens / member | 8x competitor avg | High on engagement, ZERO on churn | Engagement ≠ retention |
| WHOOP CEO Will Ahmed (TechCrunch) | "Members are highly engaged and stay with us" | Qualitative | Low | Promotional language |
| Pitchbook tearsheet | Cohort retention | **NOT DISCLOSED** | — | — |
| WHOOP S-1 (when filed) | Net retention, cohort tables | Will be disclosed in 2027 | — | — |

**Critical observation:** WHOOP has been raising money for 14+ years and has *never* disclosed a cohort retention table. Compare to Peloton's 2019 S-1 (full cohort tables for first 5 years) and Spotify's pre-IPO disclosures. WHOOP's choice to keep this opaque is itself informative — companies disclose retention data when it tells a flattering story.

**The "<3% Pro tier" data point is being misused.** Pro is the premium tier (Peak/Life equivalent). Premium tiers structurally retain better than base tiers across every subscription business with public cohort data:
- Spotify: Premium 12-mo retention >95% vs. Free → Premium conversion <20%
- Peloton: Connected Fitness churn 1.5-1.9%/mo vs. App-only churn 7-8.4%/mo
- Netflix: Premium tier retention historically 4-5pp higher than basic

Applying the "<3%" Pro number as a *blended* retention rate is the analytical equivalent of taking Peloton Connected Fitness churn and citing it for the App business.

**Most likely blended monthly churn (point estimate): 3-4%.** This is consistent with:
- Pro tier <3% as the floor (premium customers, smaller share of base)
- Base tier (WHOOP One @ $199/yr) likely 4-5% monthly given price-sensitivity selection
- Mid tier (Peak @ $239/yr) somewhere between

That's **35-50% annual churn**, much higher than the ">80% retention" framing suggests.

---

## 3. Engagement signals as churn proxies (Pitchbook data)

WHOOP doesn't disclose churn, but Pitchbook captures behavioral signals that *correlate* with retention:

| Signal | Apr 2026 value | Trend | Interpretation |
|---|---|---|---|
| Mobile app rating | 4.5 stars (stable) | Stable | Healthy — would expect deterioration if mass churning users were leaving angry reviews |
| Mobile app reviews count | 12,216 | +5% over 6 months (~110/month new) | **Surprisingly low for 2.5M members.** Either (a) members don't engage app store, or (b) active member count is materially lower than 2.5M |
| Daily app opens / member | 8x competitor average | Per WHOOP claim | Strong engagement signal IF accurate; consistent with passive-wearing thesis |
| Employee count growth (LinkedIn signal) | **-2.98%** | 3rd percentile (i.e., bottom decile) | Hiring slowdown or contraction — *could* signal cost cuts in anticipation of slower revenue or churn-driven reset |
| WHOOPgate (May 2025) | Significant Reddit/Twitter backlash | Spike, then resolved within 48 hrs | Acute negative event; the speed and generosity of WHOOP's response (free upgrades) probably *prevented* a churn spike |

**The two amber flags:**

1. **Review velocity** — 110 net new reviews/month against 2.5M members (and ~800K new members in 2025) implies <0.014% monthly review rate. For comparison, Peloton's app at peak 3M subscribers was generating 500+ reviews/month. Possible explanations:
   - WHOOP members rate the *device* not the *app* (rates on D2C site, not Play/App Store)
   - Active member count is lower than reported (e.g., 1.5-1.8M actually using the app vs. 2.5M billed members)
   - Member behavior is "set and forget" — open app daily but don't engage with store

2. **Employee growth contraction** — WHOOP's Pitchbook signal of -2.98% headcount growth puts it in the bottom decile of comparable companies. CLAUDE.md notes 600+ planned hires in 2026, but the late-2025 dip (742 → 700 per LinkedIn) suggests a hiring freeze pre-Series G. Could be unrelated to churn, but in context of a "cash flow positive in 2025" claim, the cost-control posture pre-fundraise is consistent with managing burn against unproven retention.

Neither is dispositive. Both are worth noting in the IC memo as "signals to monitor."

---

## 4. Structural drivers that should reduce WHOOP churn vs. peer baseline

These are the bull-case mechanics. Each is real, but each has a counter:

| Driver | Why it should help WHOOP | Counter-argument |
|---|---|---|
| **Passive 24/7 wearing** | No motivation gate, unlike Peloton's "did I work out today?" decision | Wear rate likely declines after novelty period (similar to Apple Watch); passive abandonment risk |
| **Physiological data lock-in** | Years of biometric history doesn't transfer to Oura or Apple Watch | Most users don't reference historical data; they care about today's recovery score |
| **Lower price point** | $199-359/yr vs. Peloton $528/yr → less "is this worth it?" pressure | Lower price = lower switching cost too; easier to abandon a $20/mo charge than a $44/mo one |
| **Premium customer segment** | Athletes, biohackers, executives — less price-sensitive | Adverse selection on the way down too; if performance/health goals shift, defection is fast |
| **Subscription IS the product** | No bike-obsolescence dynamic that drove Peloton churn | Hardware obsolescence still exists (4.0 → 5.0 → 6.0); legacy hardware degrades user experience |
| **WHOOP Coach (AI engagement layer)** | New utility per member as model improves | Newer/competing AI coaches (Apple Intelligence, Google Fitbit AI) may erode this advantage |
| **Annual plan dominance** | ~88% on annual plans → 12-month commitment baked in | Annual renewal cliff at month 12 is the highest-churn moment; current data masks this |

**Net assessment:** The structural drivers are real but probably push blended monthly churn 50-100bp below Peloton's current 1.8%, not 200-300bp below. **Plausible WHOOP-specific blended monthly: 1.0-1.5% in steady state, NOT 0.5-1.0% the bull case implies.**

---

## 5. Structural drivers that should INCREASE WHOOP churn vs. peer optimism

These are the bear-case mechanics — the ones that could push WHOOP to Peloton's current 1.8%/mo:

1. **Apple Watch + Oura competitive bracket.** Apple Watch is "free" (already owned) for 200M+ Apple users; Oura Ring is more discreet form factor and now offers Cellular. Both are taking share from the "I want a health wearable" customer segment. WHOOP's pricing and form factor (band-only) may not have a defensive moat as strong as the bull case assumes.

2. **Hardware obsolescence cycle.** Every 2 years, WHOOP launches a new hardware generation. Members on old hardware face worsening relative experience. Two outcomes:
   - **Upgrade and stay:** OK retention but device CAC shows up as a recurring cost (no longer one-time)
   - **Don't upgrade and degrade:** churn risk rises in year 2-3 as features lag
   
   This dynamic doesn't exist for pure-software subscriptions like Spotify. It DOES exist for Peloton (bike obsolescence drove FY2023-24 churn).

3. **Auto-renewal abandonment.** Annual plans renew silently. Members who stopped wearing 6 months ago still get billed for 12 months. The "active member" count masks real engagement decay. When members notice (credit card statement audit, calendar reminder), they cancel — and the cancellation wave can be lumpy and severe. **This is the silent churn risk.**

4. **Price compression pressure.** If Apple/Samsung/Google bundle similar features into their existing watch ecosystems (already happening with Apple Watch Series 10 cardiac features), WHOOP's premium price loses the "best-in-class" justification. The customer realizes they're paying $30/mo for what their existing device does for free.

5. **WHOOP 5.0 transition risk realized in WHOOPgate.** May 2025 backlash showed the member base is sensitive to perceived fairness on hardware upgrades. Even though WHOOP responded well, the episode revealed:
   - Members track the value-for-money equation closely
   - Reddit/social mobilizes fast against perceived nickel-and-diming
   - Future hardware cycles will be scrutinized similarly

6. **"Whoop fatigue" — the recovery score paradox.** WHOOP's core value prop is the daily recovery score. After 18-24 months, many users find their score variability narrows (they've optimized) and the daily check-in becomes routine rather than insightful. This is a known dynamic in fitness wearables (Fitbit, Garmin) and may be the single biggest driver of long-tail churn.

**Net assessment:** These drivers are also real and probably push blended monthly churn 50-150bp ABOVE the bull case. Combined with #4, the realistic blended monthly is **probably 1.5-2.5% in steady state**, not the 1.0-1.5% the base case implies.

---

## 6. The cohort curve hypothesis with WHOOP-specific deltas

The research file proposed a generic cohort curve. Here's the WHOOP-specific version with rationale:

| Tenure | Generic estimate | WHOOP-specific estimate | Rationale for delta |
|---|---|---|---|
| **Months 1-3** | 4.0-5.0%/mo | **3.5-4.5%/mo** | Slightly lower than generic because WHOOP's 30-day free trial filters out worst-fit customers before they show up in paying cohort |
| **Months 4-12** | 2.0-2.5%/mo | **2.5-3.0%/mo** | Slightly HIGHER than generic. The annual-plan-cliff at month 12 will pull churn forward into months 10-12 (members hit "do I renew?" decision). Base tier especially. |
| **Year 2** | 1.5-2.0%/mo | **1.8-2.3%/mo** | Higher than generic. Post-renewal cliff drop-off + hardware obsolescence beginning to matter (year-2 customers are on aging WHOOP 4.0 vs. new 5.0 launches). |
| **Year 3+** | 1.0-1.5%/mo | **1.3-1.8%/mo** | Higher than generic. The "WHOOP fatigue" dynamic + competitive pressure from Apple Watch ecosystem expansion. Pure software subscriptions can hit 1.0%/mo (Spotify Premium); hardware-coupled subscriptions cannot. |

**Implied 12-month retention:** Cumulative survival of 3-month × 9-month early churn = (1-0.04)³ × (1-0.0275)⁹ = 0.885 × 0.778 = **68.9%**.

This is materially worse than the marketed ">80-85%" — by ~12 percentage points. Possible reconciliations:
- WHOOP's ">80%" figure is for *a specific cohort* (e.g., athletes who bought the device, not subscribers who took the free trial)
- WHOOP's ">80%" figure excludes month 1-3 attrition (i.e., it's "of those still active at month 4, 80% are still active at month 12")
- Our cohort estimates are too pessimistic

**The first two interpretations are common.** Companies often quote retention figures that exclude early-stage drop-off because it makes the number look better. Peloton's pre-IPO marketing did this; the S-1 disclosure revealed the true full-cohort number was ~10pp lower.

---

## 7. Peer overlay scenarios for stress-testing

### Bull case: Spotify Premium overlay
Spotify Premium subscribers (the closest pure-software comparison): blended monthly churn 0.6-0.8%, 12-month retention >90%.

**Implied for WHOOP (bull):**
- Months 1-3: 2.0-3.0%/mo (early churn lower because committed buyers)
- Year 1+: 1.0%/mo
- 12-mo retention: ~80%

This is the marketing-claim case. Achievable only if WHOOP looks more like a media subscription than a hardware-coupled service. **Probability: low (~20%).**

### Base case: Strava / Garmin Connect overlay
Strava (premium subs) and Garmin (Connect+) — wearable-adjacent, fitness-coupled subscriptions: blended monthly 1.2-1.8%, 12-month retention 75-82%.

**Implied for WHOOP (base):**
- Months 1-3: 3.5-4.5%/mo
- Year 1+: 1.5%/mo
- 12-mo retention: ~70%

This is the realistic best-case. **Probability: ~50%.**

### Bear case: Peloton overlay
Peloton Connected Fitness today: 1.5-1.9%/mo, ~80% annual retention but trending down.

**Implied for WHOOP (bear):**
- Months 1-3: 4.5-5.5%/mo
- Year 1+: 1.8-2.2%/mo (rising)
- 12-mo retention: ~60-65%

This is the "novelty fades, competitors win" case. Subscription LTV craters; bucket-2 distressed multiples become defensible. **Probability: ~30%.**

---

## 8. The hardware-cycle interaction (an under-modeled risk)

Every 2 years, WHOOP launches new hardware. Members face a forced choice:

| Cohort | Hardware | Choice in 2026 | Likely outcome |
|---|---|---|---|
| 2022-2023 acquired | WHOOP 4.0 | Upgrade to 5.0 (free during WHOOPgate response) | Mostly stay, but 10-15% churn at decision point |
| 2024 acquired | WHOOP 4.0 (late) | Same upgrade decision | Mostly upgrade |
| 2025 H1 acquired | WHOOP 4.0 (just before 5.0 launch) | "I just bought this and it's already obsolete?" — high churn risk | This was the WHOOPgate cohort; ~15-20% likely churned |
| 2025 H2 acquired | WHOOP 5.0 | No immediate decision needed | Baseline churn applies |

**The model implication:** Every 2 years, the *blended* monthly churn spikes by 50-100bp for 1-2 quarters around new hardware launch. This is invisible in a flat-annual churn assumption but matters for forecast year 2028 (next hardware cycle, WHOOP 6.0).

The rebuild should include a "hardware launch churn step" — a one-time 50-100bp monthly churn add in launch quarters, reverting to baseline.

---

## 9. The auto-renewal silent churn problem

WHOOP charges annual plans up front and renews silently. This creates a known/unknown gap:

- **Reported active members** = paid-and-billed subscribers (denominator includes inactive billed users)
- **Engaged active members** = subscribers who wear the device daily (the actual revenue durability base)

If 2.5M members are billed but only 1.8M are engaged (a plausible 28% silent-attrition rate based on Peloton App-only data), then:
- Year 12 renewal cliff: ~700K members realize they don't use it, cancel at renewal
- Reported member count drops abruptly when annual renewals don't happen
- This shows up as a quarterly churn spike, not steady decay

**The model should track engaged vs. billed members separately.** Bear case: assume 60% engaged ratio steady-state. Base: 75%. Bull: 90%. The "engaged" number drives renewal probability; the "billed" number drives current revenue.

---

## 10. Synthesis — recommended R10 / R11 architecture

| Element | Bear | Base | Bull |
|---|---|---|---|
| Months 1-3 monthly churn | 5.0% | 4.0% | 3.0% |
| Months 4-12 monthly churn | 3.0% | 2.5% | 2.0% |
| Year 2 monthly churn | 2.3% | 1.8% | 1.3% |
| Year 3+ monthly churn | 1.8% | 1.5% | 1.0% |
| Hardware-launch churn step (every 2 yrs) | +100bp/mo for 2 quarters | +75bp/mo for 2 quarters | +50bp/mo for 2 quarters |
| Engaged-to-billed ratio (steady state) | 60% | 75% | 90% |
| **Implied 12-mo retention** | ~62% | ~70% | ~80% |
| **Implied LTV (at $338 ARPU, 70% sub GM)** | ~$650 | ~$1,050 | ~$1,800 |

**Critical model directives:**

1. **Track cohort vintages.** Each year's new members get their own age bucket; blended churn is the weighted average of all live cohorts.
2. **Apply hardware-launch step in 2028, 2030, 2032 (every other year).**
3. **Track engaged vs. billed ratio separately.** Engaged members drive renewal probability; billed members drive current revenue.
4. **Output blended annual churn as a derived line for sensitivity grids** — but never let users overwrite it as input.
5. **Sanity-check against ">80% retention" claim:** if base case produces 12-mo retention <70%, flag in the model output rather than rationalize the disagreement.

---

## 11. What would resolve the remaining uncertainty

| Source | What it would tell us | Likelihood / timeline |
|---|---|---|
| **WHOOP S-1 filing** | Full cohort tables, net retention, MRR/ARR disclosures (required by SEC) | **Definitive — but ~12 months out (likely Q1 2027)** |
| **Sacra equity research PDF** ($50/mo) | Detailed retention analysis, possibly tier-level | Moderate — purchase-gate is low-cost, high-value |
| **Pitchbook tearsheet refresh** with retention prompt | Sometimes includes "12-month retention" line if recently updated | Low — already attempted, didn't yield cohort data |
| **Oura Pitchbook deep dive** | Closest comp; if Oura discloses retention, sets a band | Medium — worth re-checking |
| **Peloton's own ARPU KPI from FY2025 10-K MD&A** | Provides the most current blended-churn-implied LTV for the bear overlay | Available — should pull |
| **App Store Connect / Sensor Tower data** | Mobile app DAU/MAU trends as engagement proxy | Paid services; budget-dependent |
| **Reddit r/whoop / Glassdoor sentiment monitoring** | Soft signals on member sentiment trend, employee perspective on churn | Free; moderate value |

**Recommendation:** Buy the Sacra report ($50/mo, 1-month subscription = $50 one-time). It's the highest-value paywall in the entire research workflow. Even partial disclosure of WHOOP-specific cohort data resolves R10/R11 from "Tier 3 unsourced" to "Tier 2 validated."

---

## 12. The IC memo paragraph

The synthesis lands here:

> *Churn is the single largest unsourced lever in the WHOOP valuation. WHOOP has never disclosed a cohort retention table — a notable choice for a company 14 years into its life that has raised $1B+ across 10 rounds. The publicly available data points (Sacra ">80-85% retention", Series G "<3% Pro tier monthly churn") describe a select subset of the member base, not blended economics.*
>
> *Our base case applies a cohort-aged churn curve consistent with Strava/Garmin Connect+ peer subscriptions, implying ~70% 12-month retention and ~$1,050 blended LTV. This sits between the marketed ">80%" claim (bull case, Spotify-like, ~80% retention, $1,800 LTV) and the Peloton overlay (bear case, ~62% retention, $650 LTV). At our base-case LTV, LTV/CAC is ~5x at $200 CAC — healthy but not extraordinary.*
>
> *The Series G mark of $10.1B requires the bull case to hold. If churn dynamics ultimately resolve closer to Peloton's current trajectory (1.8%/mo, declining to bear-case territory), Series G investors are paying for healthcare optionality and growth premium, not subscription economics. The healthcare reimbursement option (CMS Innovation Center pathway) becomes the sole bridge to the mark — and that option's probability depends on demonstrated retention WHOOP has yet to disclose.*

---

## Appendix: Key formulas used

- Annual retention from monthly churn: R_annual = (1 - r_monthly)^12
- Expected lifetime: L = 1 / r_monthly (months)
- LTV: LTV = ARPU × Sub GM × L_years
- Cumulative cohort survival to month T: S(T) = ∏ (1 - r_t) where r_t is monthly churn at age t

## Sources

- WHOOP Series G press release (Mar 2026, via TechCrunch)
- Sacra equity research (summary, pre-paywall) — `research/web-research-sweep.md`
- Pitchbook WHOOP tearsheet (Apr 2026 scrape) — `research/whoop-pitchbook-data.md`
- Peloton 10-K analysis — `research/peloton-10k-analysis.md`
- Revenue/bookings reconciliation — `research/revenue-bookings-reconciliation.md`
- Reddit r/whoop WHOOPgate discussion (May 2025) — referenced in `research/web-research-sweep.md`

*Last updated: May 1, 2026*
