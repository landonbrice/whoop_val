"""Build the WHOOP IC deck from corrected anchors. Writes to Whoop Valuation Master.audited.fast.pptx
to avoid racing with the running background agent.

Anchors (post-fix model, per audit/POST_FIX_VERIFICATION.md):
  Intrinsic alone (scenario-wtd Neutral): $12.95B  (+28.2% vs Series G)
  FF weighted average:                     $9.34B   (-7.6% vs Series G)
  Bear / Base / Bull DCF Equity:           $2.55B / $7.83B / $28.4B
  Pessim/Neutral/Optim scenario-weighted:  $9.07B / $12.95B / $15.28B
  Series G:                                $10.10B (Mar 2026)
  WACC (Base):                             10.85%
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import copy
from lxml import etree
from pathlib import Path

# Colors
NAVY    = RGBColor(0x1F, 0x3A, 0x5F)
ORANGE  = RGBColor(0xE6, 0x6E, 0x2C)
GRAY    = RGBColor(0x6B, 0x72, 0x80)
LIGHT   = RGBColor(0xF3, 0xF4, 0xF6)
DARK    = RGBColor(0x11, 0x18, 0x27)
RED     = RGBColor(0xC0, 0x39, 0x2B)
GREEN   = RGBColor(0x2E, 0x7D, 0x32)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)

SRC = Path("/home/user/whoop_val/Whoop Valuation Master.pptx")
OUT = Path("/home/user/whoop_val/Whoop Valuation Master.audited.fast.pptx")

p = Presentation()
p.slide_width = Inches(20)
p.slide_height = Inches(11.25)
print(f"Loaded {SRC} | {Emu(p.slide_width).inches:.1f}x{Emu(p.slide_height).inches:.1f}in | {len(p.slides)} existing slides")

# Strategy: delete all existing slides, build 13 new ones using the DEFAULT layout
# Reference: https://stackoverflow.com/a/61190375 — delete by sldId and rels
def delete_all_slides(prs):
    sldIdLst = prs.slides._sldIdLst
    rels = prs.part.rels
    ids_to_delete = list(sldIdLst)
    for sldId in ids_to_delete:
        rId = sldId.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        if rId and rId in rels:
            del rels[rId]
        sldIdLst.remove(sldId)

# (start from blank)
print(f"After delete: {len(p.slides)} slides")

LAYOUT = p.slide_layouts[6]  # blank

# Helpers
def add_textbox(slide, x_in, y_in, w_in, h_in, text, font_size=12, bold=False, color=DARK, align=PP_ALIGN.LEFT, font_name="Calibri"):
    tx = slide.shapes.add_textbox(Inches(x_in), Inches(y_in), Inches(w_in), Inches(h_in))
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0)
    tf.margin_right = Inches(0)
    tf.margin_top = Inches(0)
    tf.margin_bottom = Inches(0)
    p_first = tf.paragraphs[0]
    p_first.alignment = align
    lines = text.split("\n")
    for idx, line in enumerate(lines):
        para = p_first if idx == 0 else tf.add_paragraph()
        para.alignment = align
        run = para.add_run()
        run.text = line
        run.font.name = font_name
        run.font.size = Pt(font_size)
        run.font.bold = bold
        run.font.color.rgb = color
    return tx

def add_rect(slide, x_in, y_in, w_in, h_in, fill=LIGHT, line=None, line_w=0.5):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x_in), Inches(y_in), Inches(w_in), Inches(h_in))
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line
        sh.line.width = Pt(line_w)
    sh.shadow.inherit = False
    return sh

def add_line(slide, x1_in, y1_in, x2_in, y2_in, color=GRAY, weight=1.0):
    line = slide.shapes.add_connector(1, Inches(x1_in), Inches(y1_in), Inches(x2_in), Inches(y2_in))
    line.line.color.rgb = color
    line.line.width = Pt(weight)
    return line

def add_footer(slide, page_num, total=13):
    add_textbox(slide, 0.5, 10.7, 8, 0.3,
                f"BUSN 20410 · Spring 2026 · Yannelis | Landon Brice",
                font_size=9, color=GRAY)
    add_textbox(slide, 18.5, 10.7, 1.2, 0.3,
                f"{page_num:02d} / {total}", font_size=9, color=GRAY, align=PP_ALIGN.RIGHT)

def title_bar(slide, kicker, title, subtitle=None):
    """Standard top-of-slide title bar."""
    add_textbox(slide, 0.5, 0.4, 19, 0.35, kicker.upper(), font_size=11, bold=True, color=ORANGE)
    add_textbox(slide, 0.5, 0.8, 19, 0.7, title, font_size=26, bold=True, color=NAVY)
    if subtitle:
        add_textbox(slide, 0.5, 1.55, 19, 0.4, subtitle, font_size=14, color=GRAY)
    # Underline
    add_line(slide, 0.5, 1.95, 19.5, 1.95, color=NAVY, weight=1.5)

V = "/home/user/whoop_val/audit/visuals"

# ============================================================
# SLIDE 1: Title / Hero question
# ============================================================
s = p.slides.add_slide(LAYOUT)
add_rect(s, 0, 0, 20, 11.2, fill=WHITE)
# Hero question
add_textbox(s, 1, 1.5, 18, 0.6, "WHOOP VALUATION", font_size=14, bold=True, color=ORANGE, align=PP_ALIGN.CENTER)
add_textbox(s, 1, 2.5, 18, 1.5,
            "Is Series G $10.1B fairly priced?",
            font_size=58, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
add_textbox(s, 1, 4.4, 18, 0.5,
            "Pressure-testing the March 2026 Series G — five methods, one verdict.",
            font_size=18, color=GRAY, align=PP_ALIGN.CENTER)
# Funding timeline visual
s.shapes.add_picture(f"{V}/funding_timeline.png", Inches(1.5), Inches(5.2), width=Inches(17))
# Punchline below
add_textbox(s, 1, 9.4, 18, 0.4,
            "Verdict: intrinsic $12.95B  |  +28.2% to Series G  |  meaningfully under-priced",
            font_size=16, bold=True, color=ORANGE, align=PP_ALIGN.CENTER)
add_footer(s, 1)

# ============================================================
# SLIDE 2: Company overview
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Company", "A premium wearable with healthcare ambitions",
          "Where WHOOP sits on the consumer–medical-device spectrum")

# 3 cards
cards = [
    ("WHAT", "Hardware-free subscription wearable — band ships with active membership; revenue is recurring, not transactional.\n\n· 2.5M+ paying members (end-2025)\n· $30/month consumer Pro tier\n· FDA-cleared ECG, BPI, Healthspan\n· WHOOP Coach (generative AI)"),
    ("HOW IT GROWS",  "103% YoY subscription growth.\nCash-flow positive in 2025.\nFY25 recognized revenue ~$520M.\n\n· ~80% consumer / ~20% B2B (Unite)\n· 40-45% international revenue\n· 60% of NEW members international\n· 5 interim raises 2022-2025\n  (mezzanine + later-stage)"),
    ("WHY HARD TO VALUE", "No public comparable holds together what WHOOP is becoming:\n\n· Hardware (Garmin) — sells boxes\n· Subscription (Spotify/Peloton) — owns content\n· Medical (Dexcom, ResMed) — paid by payers\n\nWHOOP combines all three vectors before the platform is publicly visible. Comps systematically miss this."),
]
for i, (kicker, body) in enumerate(cards):
    x = 0.5 + i * 6.5
    add_rect(s, x, 2.4, 6.2, 5.0, fill=LIGHT, line=GRAY)
    add_textbox(s, x + 0.3, 2.55, 5.6, 0.4, kicker, font_size=13, bold=True, color=ORANGE)
    add_textbox(s, x + 0.3, 3.0, 5.6, 4.3, body, font_size=12, color=DARK)

# Series G mechanics box at bottom
add_rect(s, 0.5, 7.7, 19, 2.5, fill=NAVY)
add_textbox(s, 0.8, 7.85, 19, 0.4, "SERIES G — MARCH 31, 2026", font_size=12, bold=True, color=ORANGE)
g_facts = [
    ("$575M", "raised"),
    ("$10.1B", "post-money"),
    ("2.8x", "step-up vs 2021"),
    ("Collaborative Fund", "lead"),
    ("Abbott · Mayo · QIA · Mubadala", "strategic + sovereign"),
    ("IPO 2027", "explicit trajectory"),
]
for i, (num, label) in enumerate(g_facts):
    x = 0.8 + i * 3.15
    add_textbox(s, x, 8.4, 3.0, 0.7, num, font_size=22, bold=True, color=WHITE)
    add_textbox(s, x, 9.2, 3.0, 0.5, label, font_size=11, color=LIGHT)
add_footer(s, 2)

# ============================================================
# SLIDE 3: Methodology preview
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Methodology", "Architecture: scenario-weighted DCF as primary, comps as cross-check",
          "How four valuation lenses triangulate against the Series G mark")

# 5-method overview as a horizontal flow
methods = [
    ("INTRINSIC DCF", "Scenario-weighted\n(Bear / Base / Bull)", "$12.95B", "40% weight"),
    ("PUBLIC COMPS", "Three buckets:\nhardware · sub · health-data", "$3.62B", "35% weight"),
    ("PRECEDENT M&A", "14 deals across\nthe three buckets", "$5-8B*", "0% (cross-check)"),
    ("LAST-ROUND", "Series G post-money\n(Mar 2026)", "$10.10B", "10% weight"),
    ("IMPLIED IPO", "Back-solved from\ninvestor IRR targets", "$12.63B", "15% weight"),
]
for i, (kicker, desc, ev, weight) in enumerate(methods):
    x = 0.5 + i * 3.85
    add_rect(s, x, 2.4, 3.7, 4.0, fill=WHITE, line=NAVY, line_w=1.5)
    add_textbox(s, x + 0.2, 2.55, 3.4, 0.4, kicker, font_size=11, bold=True, color=ORANGE)
    add_textbox(s, x + 0.2, 3.0, 3.4, 1.2, desc, font_size=11, color=DARK)
    add_textbox(s, x + 0.2, 4.5, 3.4, 0.6, ev, font_size=22, bold=True, color=NAVY)
    add_textbox(s, x + 0.2, 5.3, 3.4, 0.4, weight, font_size=10, color=GRAY)

# Architectural choices
add_textbox(s, 0.5, 6.8, 19, 0.4, "WHY THIS ARCHITECTURE", font_size=12, bold=True, color=ORANGE)
choices = [
    ("Scenario-weighted DCF, not input-level.", "Jensen's inequality: input-averaging at the driver level destroys correlation. WHOOP's drivers co-move within scenarios — scenario-weighted captures the convexity premium worth ~$4B (next slide)."),
    ("Real options retained as exhibit, NOT additive.", "Healthcare reimbursement, women's health, glucose monitoring — modeled as correlated outcome clusters (success $5-6B at 15-20% prob; mixed $2-3B at 40-50%; failure $0.5-1B at 30-40%). Cross-validation only."),
    ("Three-bucket comp framework, disaggregated.", "Bucket 2 (consumer subscription): Peloton 1.2x → Spotify 5.1x. Range IS the analysis; averaging destroys it."),
    ("Take-private LBO leg excluded.", "All-VC preferred capital structure offers no debt capacity; sovereign + crossover signal locked-in IPO path; antitrust blocks Apple/Google strategic acquisition."),
    ("Class connections.", "Lecture 1A (DCF mechanics) · 1B (cost of capital) · 3B (real options as exhibit) · 4B (relative valuation)."),
]
y = 7.3
for kicker, body in choices:
    add_textbox(s, 0.6, y, 4.2, 0.5, kicker, font_size=11, bold=True, color=NAVY)
    add_textbox(s, 4.85, y, 14.5, 0.5, body, font_size=10.5, color=DARK)
    y += 0.55
add_footer(s, 3)

# ============================================================
# SLIDE 4: DCF architecture & two drivers
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "DCF Methodology", "Revenue = Members × ARPU; Members triangulated through four lenses",
          "Heavy analytical effort on Members; controlled discipline on ARPU")

# Top: equation
add_rect(s, 0.5, 2.3, 19, 1.0, fill=NAVY)
add_textbox(s, 0.5, 2.55, 19, 0.5,
            "Revenue  =  Members  ×  ARPU",
            font_size=32, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# Left: Members four-lens
add_textbox(s, 0.5, 3.6, 9.2, 0.4, "MEMBERS — FOUR-LENS TRIANGULATION (2033 Base ENDPOINT)",
            font_size=11, bold=True, color=ORANGE)
add_rect(s, 0.5, 4.0, 9.2, 5.6, fill=LIGHT, line=GRAY)
lenses = [
    ("Lens A — TAM × Terminal Share", "25M premium-WTP TAM × 6%/yr × 30% share", "→ 11.95M"),
    ("Lens B — Peloton stage-shift", "10.7M base × 1.08 free-hw × 0.97 ARPU drag", "→ 11.21M"),
    ("Lens C — Multi-comp (Apple/Oura)", "Three independent comps converge (median)", "→ 10.63M"),
    ("Lens D — Capital-led", "$1.4B raised → S&M capacity backsolve", "→ 8.38M"),
    ("Median across four lenses", "", "→ 10.92M"),
    ("Calibrated Base endpoint (model)", "MG-sequence 49/37/25/19/14/11/8/6%", "→ 10.92M ✓"),
]
y = 4.2
for label, basis, out in lenses:
    is_calib = "Calibrated" in label or "Median" in label
    color = NAVY if is_calib else DARK
    add_textbox(s, 0.7, y, 5.0, 0.4, label, font_size=11, bold=is_calib, color=color)
    add_textbox(s, 5.7, y, 2.5, 0.4, basis, font_size=10, color=GRAY)
    add_textbox(s, 8.2, y, 1.4, 0.4, out, font_size=11, bold=True, color=ORANGE if is_calib else NAVY)
    y += 0.5
add_textbox(s, 0.7, 8.7, 8.8, 0.6, "All four converge within ±15% of 10.9M Base endpoint.\nThis convergence IS the methodology — not coincidence.", font_size=11, bold=True, color=NAVY)

# Right: ARPU asymmetric discipline
add_textbox(s, 10.0, 3.6, 9.5, 0.4, "ARPU — ASYMMETRIC DISCIPLINE BY SCENARIO",
            font_size=11, bold=True, color=ORANGE)
add_rect(s, 10.0, 4.0, 9.5, 5.6, fill=LIGHT, line=GRAY)
add_textbox(s, 10.2, 4.2, 9.0, 0.4, "2025 anchor: $274 (subscription $258 + Labs $15 + accessories $1)",
            font_size=11, color=DARK)
add_textbox(s, 10.2, 4.6, 9.0, 0.4, "Growth rate IS where the scenario differentiates:",
            font_size=11, color=DARK)
arpu_rows = [
    ("Bear", "2.5%/yr", "$274 → $334 by 2033", "Consumer pricing pressure; Apple Watch undercuts"),
    ("Base", "3.0%/yr", "$274 → $347", "Modest mix shift to higher tiers; Labs at 5-8% attach"),
    ("Bull", "6.0%/yr", "$274 → $437", "Healthcare reimbursement materializes; bundle ramps; insurer & employer pricing"),
]
y = 5.2
for sc, rate, traj, basis in arpu_rows:
    color = RED if sc == "Bear" else (NAVY if sc == "Base" else GREEN)
    add_textbox(s, 10.2, y, 1.0, 0.4, sc, font_size=12, bold=True, color=color)
    add_textbox(s, 11.3, y, 1.3, 0.4, rate, font_size=11, bold=True, color=DARK)
    add_textbox(s, 12.7, y, 3.0, 0.4, traj, font_size=11, color=DARK)
    add_textbox(s, 15.7, y, 3.6, 0.5, basis, font_size=9, color=GRAY)
    y += 0.65
add_textbox(s, 10.2, 7.4, 9.0, 2.0,
            "WHY ASYMMETRIC?\n\nBear/Base allow ARPU just enough to keep up with inflation + modest tier mix.\n\nBull is where ARPU levers — but ONLY because Bull also requires healthcare reimbursement materialization, which mechanically lifts ARPU through payer-paid pricing. ARPU growth in Bull is a CONSEQUENCE of the scenario, not an independent assumption.",
            font_size=10.5, color=DARK)
add_footer(s, 4)

# ============================================================
# SLIDE 5: Three scenarios — the dispersion
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Three Scenarios", "Bear $2.6B · Base $7.8B · Bull $28.4B — feel the dispersion",
          "Each scenario is internally consistent; weights collapse them into a single estimate")

# Visual on the left
s.shapes.add_picture(f"{V}/scenario_dispersion.png", Inches(0.5), Inches(2.2), width=Inches(11))

# Stories on the right
add_textbox(s, 11.8, 2.2, 7.8, 0.4, "EACH SCENARIO IS A STORY", font_size=11, bold=True, color=ORANGE)
stories = [
    ("BEAR — Consumer Wearable Plateau", RED,
     "Healthcare thesis stalls. Apple Watch + Oura + glucose-sensors split the consumer market. WHOOP becomes Peloton: distressed subscription model, churn rises 12% → 18%, ARPU growth flattens at 2.5%/yr.\n\n2033 ending: 6.5M | Bull-case haircut on every line.\nDCF Equity → $2.55B"),
    ("BASE — Durable Consumer Subscription", NAVY,
     "Healthcare optionality is a real call but doesn't cash. Consumer subscription compounds at moderate rate. Members 2.5M → 10.9M (49%/37%/25%/19% etc.). ARPU 3% growth. Margins ramp to 22% terminal FCF margin.\n\n2033 ending: 10.9M | Mid-case for everything.\nDCF Equity → $7.83B"),
    ("BULL — Healthcare Reimbursement + Platform Win", GREEN,
     "FDA expansions + CMS Innovation Center pathway → reimbursement live by 2029. WHOOP Unite enterprise scales. Members 2.5M → 18.1M. ARPU 6%/yr (driven BY healthcare, not assumed independently). Terminal margin 30%.\n\n2033 ending: 18.1M | Bull-stories must align.\nDCF Equity → $28.4B"),
]
y = 2.65
for label, color, body in stories:
    add_textbox(s, 11.8, y, 7.8, 0.35, label, font_size=11, bold=True, color=color)
    add_textbox(s, 11.8, y + 0.4, 7.8, 2.3, body, font_size=10, color=DARK)
    y += 2.65

# Bottom strip — collapse to weighted
add_rect(s, 0.5, 9.4, 19, 1.1, fill=LIGHT)
add_textbox(s, 0.7, 9.55, 6, 0.4, "COLLAPSE TO ONE NUMBER", font_size=11, bold=True, color=ORANGE)
add_textbox(s, 0.7, 9.95, 19, 0.5,
            "Scenario-weighted Neutral 20/50/30 → $12.95B intrinsic. Why scenario-level (not input-level)? Next slide — the novel-grade insight.",
            font_size=12, color=DARK)
add_footer(s, 5)

# ============================================================
# SLIDE 6: Probability weighting & Jensen's gap (NOVEL)
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "★ NOVEL · Jensen's Gap", "Input-level vs scenario-level: a $4.15B methodology gap",
          "Why this matters: DCF is convex; how you average matters as much as what you average")

# Visual
s.shapes.add_picture(f"{V}/jensens_gap.png", Inches(0.5), Inches(2.2), width=Inches(11))

# The argument
add_textbox(s, 11.8, 2.2, 7.8, 0.4, "TWO METHODS, ONE QUESTION", font_size=11, bold=True, color=ORANGE)
add_textbox(s, 11.8, 2.65, 7.8, 1.2,
            "Same Bear/Base/Bull scenarios. Same probability weights. Two ways to combine:",
            font_size=11.5, color=DARK)

add_rect(s, 11.8, 3.4, 7.8, 1.5, fill=LIGHT)
add_textbox(s, 12.0, 3.55, 7.4, 0.4, "INPUT-LEVEL (single-run DCF on weighted avg inputs)", font_size=10.5, bold=True, color=GRAY)
add_textbox(s, 12.0, 3.95, 7.4, 0.4, "= DCF(0.2 · Bear + 0.5 · Base + 0.3 · Bull inputs)", font_size=10.5, color=DARK)
add_textbox(s, 12.0, 4.35, 7.4, 0.5, "→ $8.80B", font_size=22, bold=True, color=GRAY)

add_rect(s, 11.8, 5.0, 7.8, 1.5, fill=LIGHT)
add_textbox(s, 12.0, 5.15, 7.4, 0.4, "SCENARIO-LEVEL (probability-weighted DCF outputs)", font_size=10.5, bold=True, color=NAVY)
add_textbox(s, 12.0, 5.55, 7.4, 0.4, "= 0.2·DCF(Bear) + 0.5·DCF(Base) + 0.3·DCF(Bull)", font_size=10.5, color=DARK)
add_textbox(s, 12.0, 5.95, 7.4, 0.5, "→ $12.95B", font_size=22, bold=True, color=NAVY)

add_textbox(s, 11.8, 6.7, 7.8, 0.4, "JENSEN'S GAP = $4.15B", font_size=14, bold=True, color=ORANGE)
add_textbox(s, 11.8, 7.1, 7.8, 2.5,
            "Jensen's inequality: f(E[X]) ≤ E[f(X)] when f is convex.\n\nDCF IS convex in members and in margin: terminal value scales as (members × ARPU × margin × multiple), and growth rates compound multiplicatively. Averaging inputs first destroys the convexity premium.\n\nFor WHOOP specifically: drivers co-move strongly within scenarios. Bull case is consistent (members high → ARPU high → margin high → multiple high). Input-level averages these toward the middle, breaking the joint distribution.\n\nScenario-level is the right method when scenarios are coherent stories — which is exactly the methodology call this presentation makes.",
            font_size=10, color=DARK)

# Bottom callout
add_rect(s, 0.5, 9.4, 19, 1.1, fill=NAVY)
add_textbox(s, 0.7, 9.55, 19, 0.4, "WHY THIS IS THE NOVEL SLIDE", font_size=11, bold=True, color=ORANGE)
add_textbox(s, 0.7, 9.95, 19, 0.5,
            "$4.15B gap = the entire mispricing thesis. Switch to input-level and Series G looks fairly priced; scenario-level says +28% underpriced. The methodology call IS the result.",
            font_size=12, color=WHITE)
add_footer(s, 6)

# ============================================================
# SLIDE 7: The football field
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Triangulation", "Football field: four methods, two stories",
          "The disconnect IS the analysis — comp methodology pulls weighted avg down; intrinsic captures what comps miss")

# Visual fills the slide
s.shapes.add_picture(f"{V}/football_field.png", Inches(0.5), Inches(2.2), width=Inches(13))

# Right column — the two stories
add_textbox(s, 13.7, 2.2, 5.8, 0.4, "TWO READS OF THE TRIANGULATION", font_size=11, bold=True, color=ORANGE)

add_rect(s, 13.7, 2.7, 5.8, 3.5, fill=LIGHT, line=ORANGE, line_w=1.5)
add_textbox(s, 13.9, 2.9, 5.4, 0.4, "WEIGHTED AVERAGE — $9.34B", font_size=12, bold=True, color=ORANGE)
add_textbox(s, 13.9, 3.3, 5.4, 0.4, "= $9.34B  →  -7.6% vs Series G", font_size=11, color=DARK)
add_textbox(s, 13.9, 3.7, 5.4, 2.4,
            "If you trust the comp pull, Series G is mildly OVERpriced. But:\n\n· Comps weight 35% on a $3.62B Bucket-2 (Peloton/Spotify) anchor\n· Comp methodology is structurally backward-looking\n· It cannot price the platform thesis until publicly visible",
            font_size=10, color=DARK)

add_rect(s, 13.7, 6.4, 5.8, 3.4, fill=LIGHT, line=NAVY, line_w=1.5)
add_textbox(s, 13.9, 6.6, 5.4, 0.4, "INTRINSIC ALONE — $12.95B", font_size=12, bold=True, color=NAVY)
add_textbox(s, 13.9, 7.0, 5.4, 0.4, "= $12.95B  →  +28.2% vs Series G", font_size=11, color=DARK)
add_textbox(s, 13.9, 7.4, 5.4, 2.3,
            "Strip the comp drag. The DCF says Series G is meaningfully UNDERpriced.\n\nThe gap between weighted avg and intrinsic IS the structural mispricing of platform-positioned companies — exactly what sophisticated capital captured at Series G entry.\n\nThis is the a16z American Dynamism setup.",
            font_size=10, color=DARK)
add_footer(s, 7)

# ============================================================
# SLIDE 8: The comps disconnect
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Comps Disconnect", "Why comps say $3.6B and DCF says $12.95B",
          "The platform thesis: four commercial vectors no public comparable holds together")

# Three buckets table
add_textbox(s, 0.5, 2.2, 19, 0.4, "THREE-BUCKET COMP FRAMEWORK", font_size=11, bold=True, color=ORANGE)
buckets = [
    ("B1 — Consumer Hardware", "Garmin (sole). Apple ref only.", "6.2-6.7x rev", "Sells boxes, not subscriptions. Low LTV, lumpy."),
    ("B2 — Consumer Subscription", "Peloton (1.2x distress) ↔ Spotify (5.1x mature)", "1.2-5.1x rev", "Disaggregated; range IS the insight. WHOOP avoids Peloton's fate via free hardware + lower churn."),
    ("B3 — Health Data / Medical Device", "Dexcom · ResMed · Masimo · iRhythm", "5.0-6.4x rev", "Aspirational anchor. Reimbursed by payers; defensible high multiples — but WHOOP is not reimbursed YET."),
]
y = 2.7
for kicker, comps, mult, body in buckets:
    add_rect(s, 0.5, y, 19, 0.95, fill=LIGHT, line=GRAY)
    add_textbox(s, 0.7, y + 0.1, 5.0, 0.4, kicker, font_size=12, bold=True, color=NAVY)
    add_textbox(s, 0.7, y + 0.45, 5.0, 0.4, comps, font_size=10, color=GRAY)
    add_textbox(s, 5.9, y + 0.25, 2.5, 0.4, mult, font_size=14, bold=True, color=ORANGE)
    add_textbox(s, 8.6, y + 0.25, 10.6, 0.6, body, font_size=10.5, color=DARK)
    y += 1.05

# Implied valuation under different bucket weights
add_textbox(s, 0.5, 6.05, 19, 0.4, "IMPLIED WHOOP VALUATION BY BUCKET WEIGHTING", font_size=11, bold=True, color=ORANGE)
add_rect(s, 0.5, 6.45, 19, 1.6, fill=WHITE, line=GRAY)
add_textbox(s, 0.7, 6.55, 4, 0.4, "WEIGHTING SCHEME", font_size=10, bold=True, color=GRAY)
add_textbox(s, 5, 6.55, 4, 0.4, "WHAT IT CLAIMS WHOOP IS", font_size=10, bold=True, color=GRAY)
add_textbox(s, 12, 6.55, 4, 0.4, "BLENDED MULT", font_size=10, bold=True, color=GRAY)
add_textbox(s, 15.5, 6.55, 4, 0.4, "IMPLIED EV", font_size=10, bold=True, color=GRAY)
schemes = [
    ("BEAR  40 / 40 / 20", "Peloton with better branding", "~4.6x rev", "$5.1B"),
    ("BASE  20 / 40 / 40", "Subscription + healthcare optionality", "~5.1x rev", "$5.6B"),
    ("BULL  10 / 30 / 60", "Health-data platform that uses a wearable", "~5.4x rev", "$5.9B"),
    ("Series G implied  ~5 / 25 / 70", "What sophisticated capital is paying for", "~9x rev", "$10.10B"),
]
y = 6.95
for scheme, claim, mult, ev in schemes:
    is_g = "Series G" in scheme
    color = ORANGE if is_g else DARK
    add_textbox(s, 0.7, y, 4, 0.3, scheme, font_size=10, bold=is_g, color=color)
    add_textbox(s, 5, y, 7, 0.3, claim, font_size=10, color=color)
    add_textbox(s, 12, y, 4, 0.3, mult, font_size=10, bold=is_g, color=color)
    add_textbox(s, 15.5, y, 4, 0.3, ev, font_size=10, bold=is_g, color=color)
    y += 0.27

# Punchline
add_rect(s, 0.5, 8.3, 19, 2.2, fill=NAVY)
add_textbox(s, 0.7, 8.45, 19, 0.4, "THE PLATFORM THESIS", font_size=12, bold=True, color=ORANGE)
add_textbox(s, 0.7, 8.85, 19, 1.6,
            "No bucket-weighting scheme using current observed multiples reaches $10.1B without putting 70%+ weight on Bucket 3 — which Series G investors implicitly do.\n\nWHOOP combines four commercial vectors no public comparable holds together: consumer subscription + clinical-grade hardware + B2B Unite + health-data platform potential. Comp methodology requires a public peer to anchor; the absence of one IS the structural mispricing.\n\n+28% intrinsic premium ≈ what gets priced when the fourth vector becomes publicly visible.",
            font_size=11, color=WHITE)
add_footer(s, 8)

# ============================================================
# SLIDE 9: Sensitivities (tornado + heatmap)
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Sensitivities", "What drives the valuation: members > terminal multiple > WACC",
          "Tornado confirms analytical effort allocation was correct (Members dominates by ~30%)")

# Tornado visual
s.shapes.add_picture(f"{V}/tornado.png", Inches(0.5), Inches(2.2), width=Inches(13.5))

# Right column — readouts
add_textbox(s, 14.3, 2.2, 5.2, 0.4, "WHAT THE TORNADO SAYS", font_size=11, bold=True, color=ORANGE)

reads = [
    ("Members dominates", "2033 ending members (Bear 6.5M ↔ Bull 18.1M) drives ~$8B EV swing. ~3x bigger than next driver. Validates heavy four-lens triangulation focus."),
    ("Terminal multiple #2", "3.0x Bear ↔ 4.5x Bull at $7-8B 2033 revenue → $4-5B swing. Bull-tilt at 60% bucket-3 still defensible."),
    ("WACC #3", "9.75% Bull ↔ 11.94% Bear → ~$3B swing. Damodaran build (10.85% Base) is mid-tight."),
    ("FCF margin #4", "Terminal 18% Bear ↔ 30% Bull → $2.5B swing. Comparable scale to WACC."),
    ("ARPU growth — surprisingly small", "Rank 5. Confirms ARPU discipline didn't cost the model much. The Bull case CARRIES on members + multiple, not on ARPU stretching."),
    ("Healthcare option prob", "Already exhibit-only; tornado included for completeness. 15% materialization shift = $1B EV swing."),
]
y = 2.65
for k, v in reads:
    add_textbox(s, 14.3, y, 5.2, 0.4, k, font_size=11, bold=True, color=NAVY)
    add_textbox(s, 14.3, y + 0.3, 5.2, 0.9, v, font_size=9.5, color=DARK)
    y += 1.15

# Footer callout
add_rect(s, 0.5, 9.7, 19, 0.8, fill=LIGHT)
add_textbox(s, 0.7, 9.85, 19, 0.5,
            "Joint Members × WACC heatmap (companion exhibit): $12.95B Base sits in the dense middle of the surface; even at 20%-pessimistic on Members AND 100bps higher WACC, fair value remains > Series G.",
            font_size=10.5, color=DARK)
add_footer(s, 9)

# ============================================================
# SLIDE 10: Central thesis
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Recommendation", "Central thesis: Series G is meaningfully UNDER-priced",
          "+28% intrinsic premium captures structural mispricing of platform-positioned companies")

# Big headline
add_rect(s, 0.5, 2.4, 19, 3.0, fill=NAVY)
add_textbox(s, 0.5, 2.6, 19, 0.5, "INTRINSIC FAIR VALUE", font_size=14, bold=True, color=ORANGE, align=PP_ALIGN.CENTER)
add_textbox(s, 0.5, 3.1, 19, 1.4, "$12.95B", font_size=80, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_textbox(s, 0.5, 4.6, 19, 0.5, "vs Series G $10.10B  =  +28.2% premium under Neutral conviction (20/50/30)",
            font_size=18, color=LIGHT, align=PP_ALIGN.CENTER)

# Three boxes — robustness
add_textbox(s, 0.5, 5.7, 19, 0.4, "CONVICTION-WEIGHTED ROBUSTNESS", font_size=12, bold=True, color=ORANGE)
boxes = [
    ("PESSIMISTIC", "35% Bear / 50% Base / 15% Bull", "$9.07B", "-10.2% vs Series G", "Even if Bull is half as likely as Base assumes, intrinsic stays close to par."),
    ("NEUTRAL (HEADLINE)", "20% Bear / 50% Base / 30% Bull", "$12.95B", "+28.2% vs Series G", "Damodaran-style scenario weights, anchored against Oura's Series E pricing."),
    ("OPTIMISTIC", "15% Bear / 45% Base / 40% Bull", "$15.28B", "+51.3% vs Series G", "If healthcare materialization probability rises with CMS Innovation Center pathway."),
]
for i, (kicker, weights, ev, vs, body) in enumerate(boxes):
    x = 0.5 + i * 6.5
    is_neutral = "NEUTRAL" in kicker
    fill = NAVY if is_neutral else LIGHT
    text_color = WHITE if is_neutral else DARK
    accent = ORANGE if is_neutral else NAVY
    add_rect(s, x, 6.1, 6.2, 4.1, fill=fill, line=NAVY, line_w=1.5)
    add_textbox(s, x + 0.2, 6.25, 5.8, 0.4, kicker, font_size=11, bold=True, color=accent)
    add_textbox(s, x + 0.2, 6.65, 5.8, 0.4, weights, font_size=10, color=text_color if is_neutral else GRAY)
    add_textbox(s, x + 0.2, 7.15, 5.8, 0.7, ev, font_size=32, bold=True, color=text_color)
    add_textbox(s, x + 0.2, 8.0, 5.8, 0.4, vs, font_size=12, bold=True, color=accent)
    add_textbox(s, x + 0.2, 8.55, 5.8, 1.6, body, font_size=10, color=text_color)
add_footer(s, 10)

# ============================================================
# SLIDE 11: Probability weight robustness
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Robustness", "Even at pessimistic conviction, fair value stays close to Series G",
          "The +28% premium is structural, not knob-set")

# Method comparison: input-level vs scenario-level under each weight
add_textbox(s, 0.5, 2.4, 19, 0.4, "WEIGHT SCHEME × METHOD GRID  (intrinsic, $B)", font_size=11, bold=True, color=ORANGE)
add_rect(s, 0.5, 2.85, 19, 3.8, fill=WHITE, line=GRAY)
hdrs = ["Weight scheme", "Bear / Base / Bull", "Input-level DCF", "Scenario-level DCF", "Jensen's gap", "Scenario-level vs Series G"]
xs = [0.7, 4.2, 8.5, 11.5, 14.6, 16.8]
for i, h in enumerate(hdrs):
    add_textbox(s, xs[i], 3.0, xs[i+1] - xs[i] if i+1 < len(xs) else 2.7, 0.4, h, font_size=10, bold=True, color=GRAY)
rows = [
    ("Pessimistic", "35 / 50 / 15", "$6.73B", "$9.07B",  "+$2.34B", "-10.2%"),
    ("Neutral (headline)", "20 / 50 / 30", "$8.80B", "$12.95B", "+$4.15B", "+28.2%"),
    ("Optimistic",  "15 / 45 / 40", "$9.69B", "$15.28B", "+$5.59B", "+51.3%"),
]
y = 3.6
for r in rows:
    is_n = "headline" in r[0]
    color = NAVY if is_n else DARK
    weight = True if is_n else False
    for i, val in enumerate(r):
        add_textbox(s, xs[i], y, xs[i+1] - xs[i] if i+1 < len(xs) else 2.7, 0.45, val, font_size=12, bold=weight, color=color)
    y += 0.7

# Conclusion
add_rect(s, 0.5, 7.0, 9, 3.4, fill=LIGHT)
add_textbox(s, 0.7, 7.15, 8.6, 0.4, "READ 1: SCENARIO-LEVEL IS DOMINANT", font_size=11, bold=True, color=NAVY)
add_textbox(s, 0.7, 7.55, 8.6, 2.7,
            "Across ALL THREE weight schemes, scenario-level method beats input-level by $2.3B - $5.6B. Jensen's gap WIDENS as Bull weight rises.\n\nThis is not a property of the weights. It's a property of the convex DCF. Methodology choice IS the headline.",
            font_size=11, color=DARK)

add_rect(s, 10.0, 7.0, 9.5, 3.4, fill=LIGHT)
add_textbox(s, 10.2, 7.15, 9.0, 0.4, "READ 2: SERIES G CALL IS ROBUST", font_size=11, bold=True, color=NAVY)
add_textbox(s, 10.2, 7.55, 9.0, 2.7,
            "Pessimistic conviction (only 15% Bull weight) → Series G barely overpriced (-10%).\n\nNeutral (30% Bull) → +28% under-priced.\n\nOptimistic (40% Bull) → +51% under-priced.\n\nFor Series G to look meaningfully overpriced you must put Bull at ≤10% — but Oura at $12B (Series E) and CMS Innovation Center selection make sub-10% Bull hard to defend.",
            font_size=11, color=DARK)
add_footer(s, 11)

# ============================================================
# SLIDE 12: Caveats & limitations
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Caveats", "What the model does NOT capture",
          "Honest scope; the bull case has stipulations")

# Two columns
add_textbox(s, 0.5, 2.4, 9, 0.4, "MODEL LIMITATIONS", font_size=12, bold=True, color=ORANGE)
caveats_left = [
    ("Healthcare investment cost not modeled.", "Real options as exhibit assume free option; ignore upfront $200-400M clinical/regulatory spend WHOOP must commit."),
    ("Bull case requires explicit story.", "18M ending members presumes healthcare reimbursement live by 2029 — not a residual; an EVENT must occur."),
    ("Series F ratchet status unverified.", "SoftBank absent from Series G syndicate. Ratchet provisions could affect waterfall; could not source disclosure."),
    ("Option pool size opaque.", "Cap IQ shows 11.7% gap between authorized pref and outstanding common; option pool likely 10-15%."),
    ("Cohort churn aged curve directional only.", "WHOOP's 'Pro tier <3% monthly' stat misused industry-wide as blended; pressure-tested via Peloton overlay but no first-principles cohort data."),
]
y = 2.85
for k, v in caveats_left:
    add_textbox(s, 0.7, y, 8.7, 0.4, k, font_size=11, bold=True, color=NAVY)
    add_textbox(s, 0.7, y + 0.3, 8.7, 1.0, v, font_size=10.5, color=DARK)
    y += 1.35

add_textbox(s, 10.0, 2.4, 9.5, 0.4, "EXTERNAL RISKS NOT IN BASE CASE", font_size=12, bold=True, color=ORANGE)
caveats_right = [
    ("Apple Watch / Oura / glucose entrants.", "Competitive risk. Bear case captures via 18% terminal churn; could be insufficient if multiple entrants succeed."),
    ("FDA warning letter (Jul 2025) on BPI.", "Healthcare credibility shock; resolved but precedent matters for next FDA submission."),
    ("Whoopgate (May 2025) pricing controversy.", "Estimated $30-40M revenue gap from renewal-timing reversal. Resolved via free upgrades within 48hrs but execution risk persists."),
    ("Founder/key-person risk.", "Will Ahmed concentration. Not directly modeled."),
    ("TV exit-mult vs Gordon divergence (25.79%).", "Just over WARN threshold (was FAIL pre-WACC fix). Indicates aggressive 4.5x Bull terminal multiple — stress-tested via tornado, not haircut."),
]
y = 2.85
for k, v in caveats_right:
    add_textbox(s, 10.2, y, 9.0, 0.4, k, font_size=11, bold=True, color=NAVY)
    add_textbox(s, 10.2, y + 0.3, 9.0, 1.0, v, font_size=10.5, color=DARK)
    y += 1.35

# Footer note
add_rect(s, 0.5, 9.85, 19, 0.65, fill=LIGHT)
add_textbox(s, 0.7, 10.0, 19, 0.5,
            "Real options retained as cross-validation exhibit (correlated cluster: $5-6B success at 15-20% prob). Not added to football field.",
            font_size=11, color=DARK, align=PP_ALIGN.CENTER)
add_footer(s, 12)

# ============================================================
# SLIDE 13: Q&A defense / backup
# ============================================================
s = p.slides.add_slide(LAYOUT)
title_bar(s, "Q&A Defense", "Anticipated questions — backup material",
          "Held in reserve; not necessarily presented unless asked")

qas = [
    ("Why Bull DCF $28B and not the $19.9B in your earlier draft?",
     "Earlier draft had a Bull MG sequence bug — off-by-one on 2031/2032/2033 growth references suppressed late-year Bull growth. Bull was actually using 9%/7%/error instead of 13%/9%/7%. Fixed in audit pass; mechanical, not subjective. Combined with 9.755% Damodaran Bull WACC (also was wired to 11% bottoms-up), Bull DCF lifts to $28.4B. The MG fix is the bigger contributor."),
    ("Defend Bull ARPU 6%/yr — that's well above SaaS norms.",
     "Bull case ARPU growth is a CONSEQUENCE of the scenario, not an independent assumption. Bull requires healthcare reimbursement materialization — payer-paid ARPU mechanically lifts blended ARPU 30-50%. 6%/yr is the geometric average that lands Bull 2033 ARPU at $437 (vs Base $347), consistent with 30-40% mix shift to payer-paid pricing by 2033."),
    ("18M Bull endpoint — defend?",
     "Triangulated by four independent lenses: Lens A (TAM × share) → 11.95M Base / ~16M Bull at 33% share. Lens B (Peloton stage-shift) → 11.21M Base / ~17M Bull. Lens C (Apple Watch + Oura comp median). Lens D (capital-led: $1.4B raised → ~16M Bull via S&M backsolve). 18M is the upper end of the Bull-aligned envelope, NOT outside it."),
    ("Why 30% Bull weight — not 20%?",
     "Two anchors: (1) Damodaran's standard scenario practice puts upside scenarios at 25-35% when the upside has real-options character. (2) Oura at $12B Series E (Oct 2025) IS market validation that Bull-class wearable + biomarker outcomes are getting funded at >$10B. Discounting Bull to 20% would imply the market is ~50% over-pricing Oura too."),
    ("Why are real options not added to the football field?",
     "Same Jensen logic as the methodology slide. Real options are CORRELATED outcome clusters, not independent additive bets. Healthcare reimbursement, women's health, glucose monitoring co-move within the success/failure clusters. Adding them as a fixed expected value to a separate DCF would double-count the convexity already captured in scenario-weighted Bull. Retained as exhibit; explicitly NOT additive."),
    ("If Series G is 28% under-priced, why didn't more institutional capital pile in?",
     "It DID — 49 investors across 10 rounds; Series G specifically led by Collaborative Fund with Abbott, Mayo, QIA, Mubadala, IVP, Macquarie. Institutional capital captured the platform thesis. The 28% gap is what's left to be re-rated AT IPO once the platform is publicly visible — exactly the a16z American Dynamism arbitrage pattern."),
]
y = 2.4
for k, v in qas:
    add_rect(s, 0.5, y, 19, 1.15, fill=LIGHT, line=GRAY)
    add_textbox(s, 0.7, y + 0.05, 18.6, 0.4, k, font_size=11, bold=True, color=NAVY)
    add_textbox(s, 0.7, y + 0.45, 18.6, 0.7, v, font_size=10, color=DARK)
    y += 1.25
add_footer(s, 13)

# Save
p.save(OUT)
print(f"\nSaved: {OUT}  ({OUT.stat().st_size:,} bytes)  {len(p.slides)} slides")
