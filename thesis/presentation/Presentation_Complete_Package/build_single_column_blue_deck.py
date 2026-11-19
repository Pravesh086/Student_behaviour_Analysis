"""
build_single_column_blue_deck.py
================================
Generates the Single-Column Blue-Themed Pre-PhD Comprehensive Defense deck:
- Format: Single-Column wide layout (full-width cards, generous whitespace)
- Theme: Professional Academic Blue Theme (Navy, Royal Blue, Slate, White)
- Font Sizes: Extra large (24pt titles, 16pt card titles, 14.5-15pt bullets, 28pt stats)
- Publications: Updated to exactly 5 Published Papers + 1 in Queue (Under Review)
- Flow:
  1. Title & Credentials
  2. Publication Portfolio (5 Published + 1 in Queue)
  3. Base Problem: 12th Transition Shock to Engineering College
  4. The National Crisis: 18.4% Engineering Attrition
  5. The 4-Stage Behavioral Departure Trajectory
  6. Research Objectives: RQ1-5 -> RO1-5
  7. Proposed Solution: AcuLearn AI End-to-End Blueprint
  8. RO1: Complete Master Table of All 17 Non-Cognitive Constructs
  9. RO1: Scale Distillation & CFA Structural Fit Rigor
  10. RO1: Empirical Provenance & Split Quarantine (N=276 vs N=2,525)
  11. RO2: Soft Computing Fuzzy Perception Engine (DE-Tuned Mamdani FIS)
  12. RO3: BeNet Deep Architecture & Gated Linear Units (GLU)
  13. RO3: Bayesian Homoscedastic Multi-Task Loss Balancing
  14. RO3: Empirical Model Benchmarking (BeNet vs CatBoost, XGBoost, MLP)
  15. RO3: Acute Risk Recall & Component Ablation Waterfall
  16. RO4: Dual-Scope Explainable AI (DeepSHAP & LIME)
  17. RO4: 3-Tier Actionability Matrix & Ethical Boundaries
  18. RO4: CCRO Feasible Recourse Optimizer (PGD-AFT Algorithm)
  19. RO4: Clinical Case Walkthrough: Story of Student S-412
  20. RO4: The Student Psychological Kundali Dossier & 4 Archetypes
  21. RO5: Zero-Cloud In-Browser Edge AI (184 KB ONNX WASM Engine)
  22. RO5: Faculty Usability Trial & Time-Motion Study (SUS = 89.2)
  23. Algorithmic Fairness Audit & Subgroup Equity Evaluation
  24. Methodological Limitations & Empirical Boundaries
  25. Ph.D. Roadmap, NEP 2020 Implementation & Doctoral Conclusion
  26. Backup 1: 17 Constructs CFA Factor Loadings & Reliability
  27. Backup 2: BeNet Hyperparameters & Lipschitz Continuity
  28. Backup 3: CCRO Mathematical Formulation & Convergence Proofs
  29. Backup 4: Confusion Matrix on Real Test Split & Calibration
"""

import os
import sys
from PIL import Image
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# =============================================================================
# BLUE THEME PALETTE
# =============================================================================
COLOR_WHITE         = RGBColor(255, 255, 255)
COLOR_CANVAS_BG     = RGBColor(248, 250, 252) # Slate 50 (Soft off-white)
COLOR_CANVAS_BORDER = RGBColor(203, 213, 225) # Slate 300

COLOR_NAVY_DARK     = RGBColor(15, 23, 42)    # Slate 900 (Dominant Title)
COLOR_TEXT_BODY     = RGBColor(30, 41, 59)    # Slate 800 (Readable Body)
COLOR_TEXT_MUTED    = RGBColor(71, 85, 105)   # Slate 600

# Blue Theme Accents
COLOR_BLUE_PRIMARY  = RGBColor(29, 78, 216)   # Royal Blue 700
COLOR_BLUE_LIGHT    = RGBColor(239, 246, 255) # Blue 50
COLOR_BLUE_BORDER   = RGBColor(59, 130, 246)  # Blue 500
COLOR_BLUE_DEEP     = RGBColor(30, 58, 138)   # Blue 900
COLOR_BLUE_ACCENT   = RGBColor(2, 132, 199)   # Sky 600

COLOR_GOLD_BG       = RGBColor(255, 253, 235) # Gold 50
COLOR_GOLD_BORDER   = RGBColor(234, 179, 8)   # Gold 500
COLOR_GOLD_PILL     = RGBColor(202, 138, 4)   # Gold 600

ASSETS_DIR  = os.path.join(os.path.dirname(__file__), "assets")
OUTPUT_PPTX = os.path.join(os.path.dirname(__file__), "PrePhD_Defense_SingleColumn_Blue_Deck.pptx")
TOTAL_SLIDES = 29


# =============================================================================
# HELPER FUNCTIONS: SINGLE-COLUMN FORMAT WITH EXTRA LARGE FONTS
# =============================================================================

def add_slide_frame(slide, slide_num):
    """Draws background canvas, rounded border, and blue theme footer."""
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid(); bg.fill.fore_color.rgb = COLOR_CANVAS_BG; bg.line.fill.background()

    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.4), Inches(0.20), Inches(12.533), Inches(7.10))
    frame.fill.solid(); frame.fill.fore_color.rgb = COLOR_WHITE
    frame.line.color.rgb = COLOR_CANVAS_BORDER; frame.line.width = Pt(1.5)

    # Footer Left
    f_left = slide.shapes.add_textbox(Inches(0.6), Inches(7.04), Inches(4.8), Inches(0.22))
    p = f_left.text_frame.paragraphs[0]; p.text = ""
    r = p.add_run(); r.text = "MNIT Jaipur • Department of Computer Science & Engineering"
    r.font.size = Pt(9.5); r.font.color.rgb = COLOR_TEXT_MUTED

    # Footer Center
    f_mid = slide.shapes.add_textbox(Inches(5.0), Inches(7.04), Inches(3.5), Inches(0.22))
    p = f_mid.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.text = ""
    r = p.add_run(); r.text = "AcuLearn AI • Pre-PhD Comprehensive Defense"
    r.font.size = Pt(9.5); r.font.color.rgb = COLOR_TEXT_MUTED

    # Footer Right
    f_right = slide.shapes.add_textbox(Inches(10.2), Inches(7.04), Inches(2.5), Inches(0.22))
    p = f_right.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT; p.text = ""
    r = p.add_run(); r.text = f"Slide {slide_num} of {TOTAL_SLIDES}"
    r.font.size = Pt(9.5); r.font.bold = True; r.font.color.rgb = COLOR_NAVY_DARK

def add_header(slide, title_text, category_text, subtitle_text):
    """Adds the blue section pill, large 23pt title, and 12.5pt subtitle."""
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.34), Inches(4.5), Inches(0.30))
    pill.fill.solid(); pill.fill.fore_color.rgb = COLOR_BLUE_PRIMARY; pill.line.fill.background()
    p = pill.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.text = ""
    r = p.add_run(); r.text = category_text.upper()
    r.font.size = Pt(10.0); r.font.bold = True; r.font.color.rgb = COLOR_WHITE

    t_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.66), Inches(12.133), Inches(0.48))
    p = t_box.text_frame.paragraphs[0]; p.text = ""
    r = p.add_run(); r.text = title_text
    r.font.size = Pt(22.5); r.font.bold = True; r.font.color.rgb = COLOR_NAVY_DARK

    s_box = slide.shapes.add_textbox(Inches(0.6), Inches(1.12), Inches(12.133), Inches(0.30))
    p = s_box.text_frame.paragraphs[0]; p.text = ""
    r = p.add_run(); r.text = subtitle_text
    r.font.size = Pt(12.0); r.font.color.rgb = COLOR_TEXT_MUTED

def add_bottom_banner(slide, badge_text, takeaway_text):
    """Adds a full-width bottom highlight banner."""
    banner = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(6.46), Inches(12.133), Inches(0.50))
    banner.fill.solid(); banner.fill.fore_color.rgb = COLOR_GOLD_BG
    banner.line.color.rgb = COLOR_GOLD_BORDER; banner.line.width = Pt(1.5)

    tf = banner.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT; p.text = ""

    r1 = p.add_run(); r1.text = f"{badge_text}: "
    r1.font.bold = True; r1.font.size = Pt(12.0); r1.font.color.rgb = COLOR_GOLD_PILL

    r2 = p.add_run(); r2.text = takeaway_text
    r2.font.bold = False; r2.font.size = Pt(12.0); r2.font.color.rgb = COLOR_NAVY_DARK

def add_single_column_card(slide, pill_text, headline_text, bullets, stat_number=None, stat_label=None, top=Inches(1.52), height=Inches(4.78)):
    """Full-width single-column card with large fonts (14.5pt bullets)."""
    left = Inches(0.6); width = Inches(12.133)
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid(); card.fill.fore_color.rgb = COLOR_WHITE
    card.line.color.rgb = COLOR_BLUE_BORDER; card.line.width = Pt(1.8)

    # Top Pill
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.3), top + Inches(0.20), Inches(3.6), Inches(0.30))
    pill.fill.solid(); pill.fill.fore_color.rgb = COLOR_BLUE_LIGHT
    pill.line.color.rgb = COLOR_BLUE_BORDER; pill.line.width = Pt(1.0)
    p = pill.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.text = ""
    r = p.add_run(); r.text = pill_text.upper()
    r.font.size = Pt(10.5); r.font.bold = True; r.font.color.rgb = COLOR_BLUE_PRIMARY

    curr_top = top + Inches(0.56)

    # Headline
    if headline_text:
        h_box = slide.shapes.add_textbox(left + Inches(0.3), curr_top, width - Inches(0.6), Inches(0.40))
        p = h_box.text_frame.paragraphs[0]; p.text = ""
        r = p.add_run(); r.text = headline_text
        r.font.size = Pt(16.0); r.font.bold = True; r.font.color.rgb = COLOR_NAVY_DARK
        curr_top += Inches(0.42)

    # Optional Big Stat Callout
    if stat_number and stat_label:
        s_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.3), curr_top, width - Inches(0.6), Inches(0.76))
        s_box.fill.solid(); s_box.fill.fore_color.rgb = COLOR_BLUE_LIGHT
        s_box.line.color.rgb = COLOR_BLUE_BORDER; s_box.line.width = Pt(1.0)

        tf = s_box.text_frame
        p1 = tf.paragraphs[0]; p1.alignment = PP_ALIGN.CENTER; p1.text = ""
        r1 = p1.add_run(); r1.text = stat_number
        r1.font.size = Pt(28.0); r1.font.bold = True; r1.font.color.rgb = COLOR_BLUE_PRIMARY

        p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER; p2.text = ""
        r2 = p2.add_run(); r2.text = stat_label
        r2.font.size = Pt(11.0); r2.font.color.rgb = COLOR_TEXT_MUTED
        curr_top += Inches(0.82)

    # Large Bullets (14.5pt lead-in, 14pt body text)
    b_h = max(Inches(1.0), height - (curr_top - top) - Inches(0.18))
    b_box = slide.shapes.add_textbox(left + Inches(0.3), curr_top, width - Inches(0.6), b_h)
    tf = b_box.text_frame; tf.word_wrap = True

    for i, (lead, body) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(10); p.space_before = Pt(3); p.text = ""

        r_dot = p.add_run(); r_dot.text = "• "
        r_dot.font.bold = True; r_dot.font.size = Pt(15.0); r_dot.font.color.rgb = COLOR_BLUE_PRIMARY

        r_lead = p.add_run(); r_lead.text = f"{lead}: "
        r_lead.font.bold = True; r_lead.font.size = Pt(14.5); r_lead.font.color.rgb = COLOR_NAVY_DARK

        r_body = p.add_run(); r_body.text = body
        r_body.font.bold = False; r_body.font.size = Pt(14.0); r_body.font.color.rgb = COLOR_TEXT_BODY

def add_single_column_visual_card(slide, pill_text, headline_text, bullets, image_filename, stat_number=None, stat_label=None):
    """Clean single-column split card: text bullets on top/side with visual figure in dedicated blue frame."""
    top = Inches(1.52); height = Inches(4.78)
    card_w = Inches(5.95); img_w = Inches(5.95)

    # Left text card
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), top, card_w, height)
    card.fill.solid(); card.fill.fore_color.rgb = COLOR_WHITE
    card.line.color.rgb = COLOR_BLUE_BORDER; card.line.width = Pt(1.8)

    # Pill
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top + Inches(0.18), Inches(3.2), Inches(0.28))
    pill.fill.solid(); pill.fill.fore_color.rgb = COLOR_BLUE_LIGHT
    pill.line.color.rgb = COLOR_BLUE_BORDER; pill.line.width = Pt(1.0)
    p = pill.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.text = ""
    r = p.add_run(); r.text = pill_text.upper()
    r.font.size = Pt(10.0); r.font.bold = True; r.font.color.rgb = COLOR_BLUE_PRIMARY

    curr_top = top + Inches(0.52)

    # Headline
    if headline_text:
        h_box = slide.shapes.add_textbox(Inches(0.8), curr_top, card_w - Inches(0.4), Inches(0.36))
        p = h_box.text_frame.paragraphs[0]; p.text = ""
        r = p.add_run(); r.text = headline_text
        r.font.size = Pt(15.0); r.font.bold = True; r.font.color.rgb = COLOR_NAVY_DARK
        curr_top += Inches(0.38)

    # Stat box
    if stat_number and stat_label:
        s_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), curr_top, card_w - Inches(0.4), Inches(0.70))
        s_box.fill.solid(); s_box.fill.fore_color.rgb = COLOR_BLUE_LIGHT
        s_box.line.color.rgb = COLOR_BLUE_BORDER; s_box.line.width = Pt(1.0)

        tf = s_box.text_frame
        p1 = tf.paragraphs[0]; p1.alignment = PP_ALIGN.CENTER; p1.text = ""
        r1 = p1.add_run(); r1.text = stat_number
        r1.font.size = Pt(26.0); r1.font.bold = True; r1.font.color.rgb = COLOR_BLUE_PRIMARY

        p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER; p2.text = ""
        r2 = p2.add_run(); r2.text = stat_label
        r2.font.size = Pt(10.5); r2.font.color.rgb = COLOR_TEXT_MUTED
        curr_top += Inches(0.76)

    # Bullets
    b_h = max(Inches(0.8), height - (curr_top - top) - Inches(0.12))
    b_box = slide.shapes.add_textbox(Inches(0.8), curr_top, card_w - Inches(0.4), b_h)
    tf = b_box.text_frame; tf.word_wrap = True

    for i, (lead, body) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8); p.space_before = Pt(2); p.text = ""

        r_dot = p.add_run(); r_dot.text = "• "
        r_dot.font.bold = True; r_dot.font.size = Pt(14.0); r_dot.font.color.rgb = COLOR_BLUE_PRIMARY

        r_lead = p.add_run(); r_lead.text = f"{lead}: "
        r_lead.font.bold = True; r_lead.font.size = Pt(14.0); r_lead.font.color.rgb = COLOR_NAVY_DARK

        r_body = p.add_run(); r_body.text = body
        r_body.font.bold = False; r_body.font.size = Pt(13.5); r_body.font.color.rgb = COLOR_TEXT_BODY

    # Right Image container
    img_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.78), top, img_w, height)
    img_card.fill.solid(); img_card.fill.fore_color.rgb = COLOR_WHITE
    img_card.line.color.rgb = COLOR_BLUE_BORDER; img_card.line.width = Pt(1.5)

    img_path = os.path.join(ASSETS_DIR, image_filename)
    if os.path.exists(img_path):
        try:
            with Image.open(img_path) as im:
                orig_w, orig_h = im.size
            avail_w = img_w - Inches(0.36)
            avail_h = height - Inches(0.24)
            scale = min(avail_w / Inches(orig_w / 96.0), avail_h / Inches(orig_h / 96.0))
            new_w = Inches((orig_w / 96.0) * scale)
            new_h = Inches((orig_h / 96.0) * scale)
            img_left = Inches(6.78) + (img_w - new_w) / 2.0
            img_top = top + Inches(0.12) + (avail_h - new_h) / 2.0
            slide.shapes.add_picture(img_path, img_left, img_top, width=new_w, height=new_h)
        except Exception as e:
            print(f"Error loading {image_filename}: {e}")


# =============================================================================
# BUILD DECK (EXACT 29 SLIDES)
# =============================================================================

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    print("Building Single-Column Blue-Themed Defense Presentation...")

    # =========================================================================
    # SLIDE 1: TITLE & CREDENTIALS
    # =========================================================================
    s = prs.slides.add_slide(blank_layout)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid(); bg.fill.fore_color.rgb = COLOR_CANVAS_BG; bg.line.fill.background()

    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(0.35), Inches(12.333), Inches(6.8))
    card.fill.solid(); card.fill.fore_color.rgb = COLOR_WHITE
    card.line.color.rgb = COLOR_BLUE_BORDER; card.line.width = Pt(2.0)

    # Institution Pill
    pill = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.70), Inches(11.333), Inches(0.42))
    pill.fill.solid(); pill.fill.fore_color.rgb = COLOR_BLUE_LIGHT
    pill.line.color.rgb = COLOR_BLUE_BORDER; pill.line.width = Pt(1.2)
    p = pill.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.text = ""
    r = p.add_run(); r.text = "MALAVIYA NATIONAL INSTITUTE OF TECHNOLOGY JAIPUR • DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING"
    r.font.size = Pt(11.0); r.font.bold = True; r.font.color.rgb = COLOR_BLUE_PRIMARY

    # Title
    t_box = s.shapes.add_textbox(Inches(0.8), Inches(1.30), Inches(11.733), Inches(1.4))
    p = t_box.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.text = ""
    r = p.add_run(); r.text = "AcuLearn AI: Intelligent Multidimensional Frameworks for Proactive Student Retention, Academic Trajectory Prediction, and Explainable Counterfactual Recourse"
    r.font.size = Pt(24.0); r.font.bold = True; r.font.color.rgb = COLOR_NAVY_DARK

    sub_box = s.shapes.add_textbox(Inches(1.0), Inches(2.85), Inches(11.333), Inches(0.4))
    p = sub_box.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.text = ""
    r = p.add_run(); r.text = "Pre-PhD Comprehensive Examination & Doctoral Defense"
    r.font.size = Pt(15.0); r.font.bold = True; r.font.color.rgb = COLOR_BLUE_PRIMARY

    # 3 Summary Cards
    col_w = Inches(3.6)
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(3.45), col_w, Inches(2.4))
    c1.fill.solid(); c1.fill.fore_color.rgb = COLOR_BLUE_LIGHT; c1.line.color.rgb = COLOR_BLUE_BORDER
    tf = c1.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = ""; r = p.add_run(); r.text = "DOCTORAL CANDIDATE"; r.font.bold = True; r.font.size = Pt(12); r.font.color.rgb = COLOR_BLUE_PRIMARY
    p2 = tf.add_paragraph(); p2.text = ""; r = p2.add_run(); r.text = "Pravesh Kumar Bansal"; r.font.bold = True; r.font.size = Pt(16); r.font.color.rgb = COLOR_NAVY_DARK
    p3 = tf.add_paragraph(); p3.text = ""; r = p3.add_run(); r.text = "Reg. No: 2019rcp9557\nDept. of Computer Science & Engineering\nMNIT Jaipur, Rajasthan, India"; r.font.size = Pt(12); r.font.color.rgb = COLOR_TEXT_BODY

    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.866), Inches(3.45), col_w, Inches(2.4))
    c2.fill.solid(); c2.fill.fore_color.rgb = COLOR_BLUE_LIGHT; c2.line.color.rgb = COLOR_BLUE_BORDER
    tf = c2.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = ""; r = p.add_run(); r.text = "RESEARCH SUPERVISOR"; r.font.bold = True; r.font.size = Pt(12); r.font.color.rgb = COLOR_BLUE_PRIMARY
    p2 = tf.add_paragraph(); p2.text = ""; r = p2.add_run(); r.text = "Dr. Mushtaq Ahmed"; r.font.bold = True; r.font.size = Pt(16); r.font.color.rgb = COLOR_NAVY_DARK
    p3 = tf.add_paragraph(); p3.text = ""; r = p3.add_run(); r.text = "Associate Professor and HOD\nDept. of Computer Science & Engineering\nMNIT Jaipur, Rajasthan, India"; r.font.size = Pt(12); r.font.color.rgb = COLOR_TEXT_BODY

    c3 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.733), Inches(3.45), col_w, Inches(2.4))
    c3.fill.solid(); c3.fill.fore_color.rgb = COLOR_GOLD_BG; c3.line.color.rgb = COLOR_GOLD_BORDER
    tf = c3.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = ""; r = p.add_run(); r.text = "SCHOLARLY OUTPUT"; r.font.bold = True; r.font.size = Pt(12); r.font.color.rgb = COLOR_GOLD_PILL
    p2 = tf.add_paragraph(); p2.text = ""; r = p2.add_run(); r.text = "5 Published • 1 in Queue"; r.font.bold = True; r.font.size = Pt(15); r.font.color.rgb = COLOR_NAVY_DARK
    p3 = tf.add_paragraph(); p3.text = ""; r = p3.add_run(); r.text = "• Core Paper in IEEE Access (Q1, IF 3.9)\n• IERB Protocol Approved (Jan 12, 2025)\n• 100% In-Browser Edge AI (DPDP Act 2023)"; r.font.size = Pt(11.5); r.font.color.rgb = COLOR_TEXT_BODY

    b_pill = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(6.05), Inches(11.333), Inches(0.44))
    b_pill.fill.solid(); b_pill.fill.fore_color.rgb = COLOR_CANVAS_BG; b_pill.line.color.rgb = COLOR_CANVAS_BORDER
    p = b_pill.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.text = ""
    r = p.add_run(); r.text = "★ Central Thesis: First-year college attrition is preventable on Day 1 using non-cognitive behavioral intelligence and explainable counterfactual recourse."
    r.font.size = Pt(12.0); r.font.bold = True; r.font.color.rgb = COLOR_NAVY_DARK

    # =========================================================================
    # SLIDE 2: PUBLICATION DETAILS (5 PUBLISHED + 1 IN QUEUE)
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 2)
    add_header(s, "Doctoral Publications Record: 5 Published & 1 in Queue", "RESEARCH RECOGNITION • PEER-REVIEWED PORTFOLIO", "Comprehensive scholarly portfolio establishing peer-reviewed validation across all chapters")

    # Single-column structured publication list
    add_single_column_card(s, "Peer-Reviewed Publication Portfolio", "5 Accepted & Published International Papers + 1 Journal Manuscript Under Review",
                           [("Paper 1 (Flagship Journal, Q1 Published)", "IEEE Access (Impact Factor: 3.9, SCIE, JCR Q1, Scopus). 'BeNet: Multi-Task Deep Neural Architecture with Uncertainty Loss Balancing for Student Academic Trajectory Prediction and Risk Modeling', Vol. 13, pp. 204910-204928, Nov 2025. DOI: 10.1109/ACCESS.2025.3638368."),
                            ("Paper 2 (AIP Conference, Published)", "AIP Conference Proceedings (Scopus Indexed). 'Fuzzy Logic-Based Analysis of Student Behavior Patterns and Transition Risk in Technical Higher Education', Vol. 3204, Art. 020015, Feb 2025. DOI: 10.1063/5.0247979."),
                            ("Paper 3 (IEEE Conference, Published)", "IEEE 2nd International Conference on Emerging Trends in Smart Tech (ICETST 2024, IEEE Xplore / Scopus). 'Optimized Perception-Based Student Behavior Modeling and Early Academic Failure Detection', Dec 2024."),
                            ("Paper 4 (IEEE ICECI Conference, Published)", "Proc. International Conference on Electrical, Communication and Information (ICECI 2023, Scopus). 'Expert-System Approach for Early Student Behavioral Assessment and Cognitive Screening', pp. 101–106, 2023."),
                            ("Paper 5 (ICDSA Conference, Published)", "Proc. International Conference on Data Science and Applications (ICDSA 2025, Springer / Scopus). 'Hybrid Explainable Artificial Intelligence and Feature Attribution for Educational Prediction', pp. 310–318, 2025."),
                            ("Paper 6 (High-Impact Journal, In Queue / Under Review)", "Journal of Educational Technology & Society (Manuscript: CAEE-2026-0184). 'An Explainable Hybrid ML Framework with Actionable Counterfactual Recourse and In-Browser WASM Deployment for Higher Education', Submitted Q1 2026.")],
                           stat_number="5 Published + 1 in Queue", stat_label="All Doctoral Objectives (RO1 to RO5) are Fully Anchored in Peer-Reviewed Literature")
    add_bottom_banner(s, "★ SCHOLARLY TRACK RECORD", "5 peer-reviewed publications (including IEEE Access Q1, IF 3.9) and 1 journal in queue comprehensively validate this dissertation.")

    # =========================================================================
    # SLIDE 3: PROBLEM MOTIVATION: 12TH TO COLLEGE TRANSITION
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 3)
    add_header(s, "The Problem at the Base: 12th Coaching to Engineering Transition", "PROBLEM MOTIVATION • THE SCHOOL-TO-COLLEGE FRACTURE", "Why bright students who scored 95% in board exams face acute academic failure in engineering colleges")
    add_single_column_card(s, "The School-to-University Fracture", "The Four Interlocking Transition Shocks Faced by First-Year Freshers",
                           [("Shock 1: The Freedom Trap (Autonomy Chasm)", "For 2 years, rigid 14-hour JEE coaching strictly regulated every waking hour. In college hostels, supervision vanishes overnight; students mistake total lack of surveillance for leisure, leading to 6–8 hours daily on mobile gaming and streaming."),
                            ("Shock 2: Imposter Identity Crisis", "School toppers collide with hundreds of other toppers ('Big-Fish-Little-Pond' effect). A low pop-quiz score shatters self-worth, leading to deep imposter syndrome, silent distress, and complete withdrawal from office hours and doubt-clearing."),
                            ("Shock 3: Circadian Collapse & Sleep Debt", "Late-night corridor culture pushes bedtimes past 3:30 AM before 8:00 AM mathematics lectures. Chronic sleep deprivation downregulates prefrontal executive functions, rendering freshers physically present but cognitively unable to follow proofs."),
                            ("Shock 4: Cognitive & Language Disconnect", "Entrance coaching trained students in MCQ shortcut tricks; university engineering demands first-principles derivations. Concurrently, regional/Hindi-medium freshers face an overwhelming technical English translation burden.")])
    add_bottom_banner(s, "★ BASE PROBLEM", "Academic failure is driven by an unmanaged four-dimensional transition shock, not a lack of raw intelligence.")

    # =========================================================================
    # SLIDE 4: THE NATIONAL RETENTION CRISIS
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 4)
    add_header(s, "National Crisis: First-Year Technical College Attrition", "THE NATIONAL REALITY • CONTEXT & EMPIRICAL BENCHMARK", "Quantifying the human, economic, and institutional toll of freshman engineering departure in India")
    add_single_column_visual_card(s, "The Crisis in Numbers", "High Attrition Across Technical Higher Education",
                                 [("18.4% National Attrition Rate", "Across Indian technical institutions, nearly 1 out of 5 first-year students drops out or receives a year-back."),
                                  ("Middle-Class Financial Trauma", "Families lose ₹8–15 Lakhs in coaching fees, tuition, and bank loans, triggering acute social stigma and loan defaults."),
                                  ("Institutional Penalties", "NIRF rankings penalize colleges under Graduation Outcome (GO); NAAC accreditation scores drop severely."),
                                  ("Faculty Mentoring Gap", "With 1 faculty mentor per 40 students, professors cannot manually detect silent psychological distress.")],
                                 "fig4a_attrition_benchmark.png",
                                 stat_number="18.4%", stat_label="National Average First-Year Engineering Attrition Benchmark in India")
    add_bottom_banner(s, "★ THE NATIONAL CRISIS", "Student departure is an unaddressed national emergency requiring automated Day-1 early screening.")

    # =========================================================================
    # SLIDE 5: 4-STAGE BEHAVIORAL DEPARTURE TRAJECTORY
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 5)
    add_header(s, "The 4-Stage Behavioral Departure Trajectory", "STUDENT PSYCHOLOGY • THE PROGRESSIVE FAILURE FUNNEL", "Mapping the 14-week chronological progression from Day-1 subtle friction to institutional debarment")
    add_single_column_visual_card(s, "The Failure Spiral", "Chronological Progression from Week 1 to Week 14",
                                 [("Stage 1 (Days 1–15, Latent Friction)", "Subtle micro-attendance slips and bedtimes past 3:30 AM. This is AcuLearn's primary Day-1 intervention window."),
                                  ("Stage 2 (Days 16–35, Active Avoidance)", "Hostel room isolation, tutorial skipping, gaming binges, and false reassurances during weekly parental phone calls."),
                                  ("Stage 3 (Days 36–55, Exam Panic)", "Desperate 48-hour pre-midterm cramming, panic in examination halls, failing grades, and acute emotional distress."),
                                  ("Stage 4 (Days 56–75, Debarment & Dropout)", "Attendance falls below the mandatory 75% threshold; institutional debarment notices, year-back, and permanent dropout occur.")],
                                 "fig5a_trajectory_curve.png")
    add_bottom_banner(s, "★ EARLY ARREST", "Traditional ERPs act at Stage 4 when debarment is irreversible; AcuLearn intervenes on Day 1 at Stage 1.")

    # =========================================================================
    # SLIDE 6: RESEARCH OBJECTIVES: RQ1-5 -> RO1-5
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 6)
    add_header(s, "Doctoral Research Questions & Objectives (RQ1–5 -> RO1–5)", "RESEARCH FRAMEWORK • FORMAL RESEARCH OBJECTIVES", "Systematic mapping of doctoral theoretical inquiries to empirical engineering deliverables")
    add_single_column_card(s, "Formal Research Framework", "Mapping Doctoral Research Questions to Concrete Research Objectives",
                           [("Mathematical Problem Formulation", "Student s_i is formalized as state vector s_i = <x_nc, x_acad, x_dem>, where x_nc in R^51 non-cognitive parcels. The objective is to learn f(s_i) -> <y_risk, y_sgpa, y_grad> while computing minimal feasible recourse delta_x* reaching safety zone (p <= 0.20)."),
                            ("RO1: Psychometric Scale Design (RQ1)", "Develop, purify, and validate the 17-construct SSQ-180 battery with 51 manifest parcels, achieving strict structural fit (CFA CFI > 0.95, alpha > 0.90)."),
                            ("RO2: Soft Computing Fuzzy Perception (RQ2)", "Design a Differential Evolution-tuned Mamdani fuzzy inference system to resolve linguistic vagueness in self-reports without information loss (97.2% consensus agreement)."),
                            ("RO3: Deep Multi-Task Predictive Engine (RQ3)", "Engineer the BeNet deep network using Gated Linear Units (GLU) and Bayesian homoscedastic uncertainty loss balancing to outperform gradient-boosted trees."),
                            ("RO4: Explainable AI & Constrained Recourse (RQ4)", "Develop dual XAI (DeepSHAP/LIME) and Constrained Counterfactual Recourse Optimization (CCRO) to generate sparse, actionable habit adjustments under immutable demographic locks."),
                            ("RO5: Zero-Cloud Edge AI & Usability (RQ5)", "Deploy an in-browser WebAssembly (ONNX WASM) client executing in 13.8 ms with zero cloud data egress, delivering verified faculty adoption (SUS = 89.2).")])
    add_bottom_banner(s, "★ FORMAL MAPPING", "Every research objective directly translates educational theory into an empirical, deployable software component.")

    # =========================================================================
    # SLIDE 7: PROPOSED SOLUTION: ACULEARN AI BLUEPRINT
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 7)
    add_header(s, "The Proposed Solution: AcuLearn AI End-to-End Blueprint", "SYSTEM BLUEPRINT • THE ACULEARN AI ARCHITECTURE", "A 5-tier architecture connecting Day-1 on-device intake to multi-task neural inference and clinical recourse")
    add_single_column_visual_card(s, "The 5-Tier Data Pipeline", "Architectural Flow from Survey to Recourse",
                                 [("Tier 1 & 2: Client Intake & Fuzzy Perception", "Responsive on-device survey intake computes 51 parcels; DE-tuned Mamdani fuzzy logic resolves linguistic vagueness into crisp behavioral indices."),
                                  ("Tier 3: BeNet Neural Multi-Task Core", "GLU feature gating and 128-d shared latent backbone with Bayesian homoscedastic loss balancing simultaneously predicting Risk, SGPA, and Graduation."),
                                  ("Tier 4: Dual-Scope XAI & Recourse Engine", "DeepSHAP/LIME feature attribution + CCRO optimizer computing sparse 3-point habit modifications in 18.4 ms."),
                                  ("Tier 5: Presentation Dashboards", "Student Kundali portal for self-reflection and Faculty Advisory triage command center.")],
                                 "fig9a_master_system_blueprint.png")
    add_bottom_banner(s, "★ THE PROPOSED SOLUTION", "A completely unified pipeline where 100% of raw student psychometrics remain strictly inside the local browser session.")

    # =========================================================================
    # SLIDE 8: ALL 17 FEATURES TABLE (SSQ-180 BATTERY)
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 8)
    add_header(s, "RO1: Complete Specification of All 17 Non-Cognitive Constructs", "RO1 / PSYCHOMETRICS • COMPLETE 17 CONSTRUCT TAXONOMY", "The 180-item SSQ-180 inventory organized across 4 cardinal life quadrants (51 Manifest Parcels)")

    t_w = Inches(5.95); t_h = Inches(4.75)
    t1_shape = s.shapes.add_table(10, 4, Inches(0.6), Inches(1.52), t_w, t_h)
    table1 = t1_shape.table
    table1.columns[0].width = Inches(0.7); table1.columns[1].width = Inches(2.9)
    table1.columns[2].width = Inches(0.8); table1.columns[3].width = Inches(1.55)

    t2_shape = s.shapes.add_table(11, 4, Inches(6.78), Inches(1.52), t_w, t_h)
    table2 = t2_shape.table
    table2.columns[0].width = Inches(0.7); table2.columns[1].width = Inches(2.9)
    table2.columns[2].width = Inches(0.8); table2.columns[3].width = Inches(1.55)

    def style_cell(cell, text, bold=False, size=Pt(10.5), color=COLOR_TEXT_BODY, bg=COLOR_WHITE, align=PP_ALIGN.LEFT):
        cell.fill.solid(); cell.fill.fore_color.rgb = bg
        p = cell.text_frame.paragraphs[0]; p.alignment = align; p.text = ""
        r = p.add_run(); r.text = text
        r.font.bold = bold; r.font.size = size; r.font.color.rgb = color

    style_cell(table1.cell(0, 0), "Quad", bold=True, size=Pt(10.5), color=COLOR_WHITE, bg=COLOR_BLUE_DEEP, align=PP_ALIGN.CENTER)
    style_cell(table1.cell(0, 1), "Construct Domain (Q1 & Q2)", bold=True, size=Pt(10.5), color=COLOR_WHITE, bg=COLOR_BLUE_DEEP)
    style_cell(table1.cell(0, 2), "Items", bold=True, size=Pt(10.5), color=COLOR_WHITE, bg=COLOR_BLUE_DEEP, align=PP_ALIGN.CENTER)
    style_cell(table1.cell(0, 3), "alpha / CR", bold=True, size=Pt(10.5), color=COLOR_WHITE, bg=COLOR_BLUE_DEEP, align=PP_ALIGN.CENTER)

    q1_q2_data = [
        ("Q1", "1. Academic Self-Efficacy", "12", "alpha=0.89 / CR=0.94"),
        ("Q1", "2. Metacognitive Regulation", "11", "alpha=0.87 / CR=0.93"),
        ("Q1", "3. Time Management Discipline", "10", "alpha=0.85 / CR=0.92"),
        ("Q1", "4. Deep vs Surface Approach", "10", "alpha=0.84 / CR=0.91"),
        ("Q2", "5. Test & Evaluative Anxiety", "12", "alpha=0.91 / CR=0.95"),
        ("Q2", "6. Imposter Phenomenon", "10", "alpha=0.88 / CR=0.93"),
        ("Q2", "7. Stress Resilience & Coping", "11", "alpha=0.86 / CR=0.92"),
        ("Q2", "8. Academic Burnout Vulnerability", "12", "alpha=0.93 / CR=0.96"),
        ("Q1-2", "Subtotal: 8 Constructs", "88 Items", "All CFA Loadings > 0.80")
    ]
    for row_idx, (q, name, items, stats) in enumerate(q1_q2_data, start=1):
        bg = COLOR_BLUE_LIGHT if q == "Q1" else (RGBColor(241, 245, 249) if q == "Q2" else COLOR_CANVAS_BG)
        bld = (row_idx == 9)
        style_cell(table1.cell(row_idx, 0), q, bold=True, size=Pt(10), color=COLOR_NAVY_DARK, bg=bg, align=PP_ALIGN.CENTER)
        style_cell(table1.cell(row_idx, 1), name, bold=bld, size=Pt(10.5), color=COLOR_NAVY_DARK, bg=bg)
        style_cell(table1.cell(row_idx, 2), items, bold=bld, size=Pt(10), color=COLOR_TEXT_BODY, bg=bg, align=PP_ALIGN.CENTER)
        style_cell(table1.cell(row_idx, 3), stats, bold=bld, size=Pt(10), color=COLOR_BLUE_PRIMARY if not bld else COLOR_NAVY_DARK, bg=bg, align=PP_ALIGN.CENTER)

    style_cell(table2.cell(0, 0), "Quad", bold=True, size=Pt(10.5), color=COLOR_WHITE, bg=COLOR_BLUE_PRIMARY, align=PP_ALIGN.CENTER)
    style_cell(table2.cell(0, 1), "Construct Domain (Q3 & Q4)", bold=True, size=Pt(10.5), color=COLOR_WHITE, bg=COLOR_BLUE_PRIMARY)
    style_cell(table2.cell(0, 2), "Items", bold=True, size=Pt(10.5), color=COLOR_WHITE, bg=COLOR_BLUE_PRIMARY, align=PP_ALIGN.CENTER)
    style_cell(table2.cell(0, 3), "alpha / CR", bold=True, size=Pt(10.5), color=COLOR_WHITE, bg=COLOR_BLUE_PRIMARY, align=PP_ALIGN.CENTER)

    q3_q4_data = [
        ("Q3", "9. Institutional Belonging", "11", "alpha=0.90 / CR=0.94"),
        ("Q3", "10. Peer Study Group Integration", "10", "alpha=0.85 / CR=0.92"),
        ("Q3", "11. Faculty Mentorship Seeking", "10", "alpha=0.83 / CR=0.91"),
        ("Q3", "12. Help-Seeking Stigma", "10", "alpha=0.87 / CR=0.93"),
        ("Q4", "13. Sleep Hygiene & Regularity", "11", "alpha=0.88 / CR=0.94"),
        ("Q4", "14. Digital Escapism & Gaming", "10", "alpha=0.86 / CR=0.92"),
        ("Q4", "15. Grit & Perseverance", "10", "alpha=0.84 / CR=0.91"),
        ("Q4", "16. Career Clarity & Purpose", "10", "alpha=0.86 / CR=0.92"),
        ("Q4", "17. Growth Mindset Orientation", "10", "alpha=0.82 / CR=0.91"),
        ("Q3-4", "Total: 17 Constructs", "180 Items", "CR: 0.91-0.96 | Passed HTMT")
    ]
    for row_idx, (q, name, items, stats) in enumerate(q3_q4_data, start=1):
        bg = COLOR_BLUE_LIGHT if q == "Q3" else (RGBColor(241, 245, 249) if q == "Q4" else COLOR_CANVAS_BG)
        bld = (row_idx == 10)
        style_cell(table2.cell(row_idx, 0), q, bold=True, size=Pt(10), color=COLOR_NAVY_DARK, bg=bg, align=PP_ALIGN.CENTER)
        style_cell(table2.cell(row_idx, 1), name, bold=bld, size=Pt(10.5), color=COLOR_NAVY_DARK, bg=bg)
        style_cell(table2.cell(row_idx, 2), items, bold=bld, size=Pt(10), color=COLOR_TEXT_BODY, bg=bg, align=PP_ALIGN.CENTER)
        style_cell(table2.cell(row_idx, 3), stats, bold=bld, size=Pt(10), color=COLOR_BLUE_PRIMARY if not bld else COLOR_NAVY_DARK, bg=bg, align=PP_ALIGN.CENTER)

    add_bottom_banner(s, "★ 17 NON-COGNITIVE CONSTRUCTS", "Exactly 180 purified items across 17 domains grouped into 51 manifest parcels, achieving composite reliability CR >= 0.91.")

    # =========================================================================
    # SLIDE 9: RO1: SCALE DISTILLATION & CFA STRUCTURAL FIT
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 9)
    add_header(s, "RO1: Scale Distillation Pipeline & CFA Structural Fit", "RO1 / METHODOLOGY • PSYCHOMETRIC SCALE RIGOR", "From 285 candidate questions to 180 validated items grouped into 51 manifest parcels")
    add_single_column_visual_card(s, "Scale Distillation Rigor", "Item Purification & Dimensionality Reduction",
                                 [("5-Stage Purification Funnel", "285 candidate items evaluated via Lawshe's CVI (12 experts), exploratory factor analysis, and item pruning to 180 items."),
                                  ("Manifest Parceling Advantage", "Averages 3 to 4 items into 51 continuous parcels, reducing input dimensionality by 71.7% and stabilizing normality."),
                                  ("Confirmatory Factor Analysis", "chi^2/df = 1.42, CFI = 0.958, TLI = 0.952, RMSEA = 0.038 [0.031, 0.044], SRMR = 0.041 (surpassing Hu & Bentler criteria)."),
                                  ("Measurement Invariance", "Metric and scalar invariance confirmed across gender (p=0.412) and engineering disciplines (p=0.384).")],
                                 "fig18a_cfa_diagram.png",
                                 stat_number="CFI = 0.958", stat_label="Comparative Fit Index (Exceeding Hu & Bentler 0.95 Strict Threshold)")
    add_bottom_banner(s, "★ STRUCTURAL RIGOR", "Confirmatory factor analysis confirms SSQ-180 measures genuine psychological traits rather than measurement noise.")

    # =========================================================================
    # SLIDE 10: RO1: EMPIRICAL PROVENANCE & SPLIT QUARANTINE
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 10)
    add_header(s, "Empirical Provenance: Real MNIT Cohort vs CTGAN Benchmark", "DATASET PROVENANCE • SPLIT QUARANTINE & PROTOCOL", "Strict scientific separation between real physical students and computational stress-test augmentation")
    add_single_column_visual_card(s, "Strict Experimental Protocol", "Quarantined Splits & Benchmark Expansion",
                                 [("Quarantined Train/Test Split", "Real cohort (N=276) was partitioned 80/20 into Train (N=220) and Test (N=56) BEFORE any synthetic modeling."),
                                  ("CTGAN Stress Augmentation", "CTGAN was trained exclusively on the 80% train split to expand to 2,525 benchmark records."),
                                  ("Preserved Hazard Ratio", "Maintained the exact 16.4% acute-risk minority class ratio without artificial label distortion."),
                                  ("Real Held-Out Evaluation", "All reported BeNet performance metrics were evaluated on the held-out REAL student test split.")],
                                 "fig10a_data_provenance_flow.png",
                                 stat_number="N = 276 Real", stat_label="Surveyed Engineering Students at MNIT Jaipur across Branches")
    add_bottom_banner(s, "★ SCIENTIFIC INTEGRITY", "Synthetic data was strictly an architecture stress-test; all final reported accuracy reflects genuine generalization to real students.")

    # =========================================================================
    # SLIDE 11: RO2: SOFT COMPUTING FUZZY PERCEPTION ENGINE
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 11)
    add_header(s, "RO2: Soft Computing Fuzzy Perception Engine", "RESEARCH OBJECTIVE 2 • SOFT COMPUTING PERCEPTION ENGINE", "Resolving linguistic survey ambiguity via Differential Evolution-tuned Mamdani fuzzy inference")
    add_single_column_visual_card(s, "Fuzzy Behavioral Mapping", "Differential Evolution Parameter Optimization",
                                 [("Linguistic Vagueness Resolution", "Human self-reports ('sometimes overwhelmed') lack crisp boundaries; fuzzy logic models continuous truth [0.0, 1.0]."),
                                  ("Differential Evolution Tuning", "27 Mamdani IF-THEN rules tuned via DE (F=0.8, CR=0.9, 150 generations) optimizing trapezoidal crossover points."),
                                  ("Expert Clinical Alignment", "Achieves 97.2% consensus agreement with human counseling psychologists across 50 benchmark cases (kappa = 0.91)."),
                                  ("Bridge to Deep Learning", "Translates subjective Likert responses into continuous, calibrated behavioral indices for BeNet.")],
                                 "fig24a_de_convergence.png",
                                 stat_number="97.2% Agreement", stat_label="Consensus Alignment with Expert Counseling Board (Cohen's kappa = 0.91)")
    add_bottom_banner(s, "★ FUZZY ML RIGOR", "Differential Evolution automates fuzzy membership calibration, bridging human linguistic self-reports with deep neural inputs.")

    # =========================================================================
    # SLIDE 12: RO3: BENET DEEP ARCHITECTURE & GATED LINEAR UNITS
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 12)
    add_header(s, "RO3: BeNet Deep Architecture & Gated Linear Units (GLU)", "RESEARCH OBJECTIVE 3 • MULTI-TASK DEEP NEURAL NETWORK CORE", "Feature gating and shared representations for simultaneous retention, GPA, and graduation prediction")
    add_single_column_visual_card(s, "The Three Neural Stages", "Architectural Mechanics of BeNet",
                                 [("Stage 1: Gated Linear Units (GLU)", "GLU(x) = (xW + b) * sigmoid(xV + c) dynamically suppresses irrelevant non-cognitive noise and amplifies crisis signals."),
                                  ("Stage 2: Shared 128-d Backbone", "Dense representation with Swish activation and dropout (0.25) balancing shared cross-task psychological representations."),
                                  ("Stage 3: Tri-Head Multi-Task Predictors", "Parallel specialized heads output Attrition Hazard (Sigmoid), Continuous SGPA (Linear), and Graduation (Sigmoid)."),
                                  ("Lipschitz Continuity", "Spectral normalization guarantees bounded gradients (L <= 1.0) for stable recourse optimization.")],
                                 "fig28a_benet_architecture.png")
    add_bottom_banner(s, "★ DEEP ARCHITECTURE", "Gated linear units dynamically isolate salient transition shocks while shared representations transfer inductive bias across tasks.")

    # =========================================================================
    # SLIDE 13: RO3: BAYESIAN HOMOSCEDASTIC LOSS BALANCING
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 13)
    add_header(s, "RO3: Multi-Task Bayesian Homoscedastic Loss Balancing", "RO3 / OPTIMIZATION • BAYESIAN MULTI-TASK UNCERTAINTY", "Eliminating gradient starvation across classification and regression output heads")
    add_single_column_visual_card(s, "Multi-Task Loss Balancing", "Kendall & Gal Uncertainty Formulation",
                                 [("Gradient Conflict Problem", "Continuous SGPA MSE loss operates on a much larger scale than binary cross-entropy, starving classification heads."),
                                  ("Bayesian Loss Formulation", "Loss weighted by 1 / (2*sigma_t^2) * L_t + ln(sigma_t), dynamically learning task-dependent homoscedastic observation noise."),
                                  ("Accelerated Convergence", "Speeds training plateau by 40% (stabilizing at epoch 38) and eliminates manual hyperparameter tuning."),
                                  ("Empirical Gains", "Delivers +3.7% boost in classification ROC-AUC and 18.2% reduction in continuous SGPA RMSE.")],
                                 "fig29a_bayesian_loss.png",
                                 stat_number="+3.7% AUC", stat_label="Classification Performance Gain via Bayesian Homoscedastic Weighting")
    add_bottom_banner(s, "★ BAYESIAN RIGOR", "Homoscedastic uncertainty weighting prevents continuous regression gradients from dominating binary classification recall.")

    # =========================================================================
    # SLIDE 14: RO3: COMPREHENSIVE EMPIRICAL BENCHMARKING
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 14)
    add_header(s, "RO3: Comprehensive Empirical Model Benchmarking", "RO3 / BENCHMARKING • MULTI-MODEL COMPARATIVE EVALUATION", "BeNet outperforming gradient boosted decision trees and classical neural baselines on held-out test students")
    add_single_column_visual_card(s, "Benchmark Superiority", "Evaluated on Held-Out Test Students",
                                 [("Classification Supremacy", "BeNet achieves ROC-AUC of 0.948 and PR-AUC of 0.912, outperforming CatBoost (0.892), XGBoost (0.884), and MLP (0.832)."),
                                  ("Regression Precision", "Continuous SGPA prediction achieves RMSE = 0.412 and R^2 = 0.784 (a 16.8% error reduction over CatBoost's 0.495)."),
                                  ("Statistical Significance", "Paired Wilcoxon signed-rank test (p < 0.001) and 1,000 bootstrap resamples [0.938, 0.957] confirm non-overlapping gains."),
                                  ("Low Calibration Error", "Expected Calibration Error of ECE = 0.028 confirms dependable probability outputs for clinical advising.")],
                                 "fig31a_baseline_bars.png",
                                 stat_number="ROC-AUC 0.948", stat_label="BeNet Multi-Task Attrition Prediction (PR-AUC = 0.912)")
    add_bottom_banner(s, "★ BENCHMARK SUPREMACY", "BeNet achieves state-of-the-art predictive performance, validating the deep multi-task inductive bias over shallow trees.")

    # =========================================================================
    # SLIDE 15: RO3: ACUTE ATTRITION RECALL & ABLATION WATERFALL
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 15)
    add_header(s, "RO3: Acute Attrition Risk Recall & Ablation Waterfall", "RO3 / ROBUSTNESS • MINORITY RISK CAPTURE & COMPONENT WATERFALL", "Maximizing detection of failing students while maintaining low false-alarm rates")
    add_single_column_visual_card(s, "High-Risk Minority Recall", "Component-Wise Architectural Ablation",
                                 [("Acute Attrition Recall", "Captures 81.2% of failing students at 0.5 threshold and 88.9% at 0.35 screening threshold (CatBoost misses 31.6%)."),
                                  ("Ablation Waterfall", "Base MLP (0.832) -> +GLU Gating (0.894, +6.2%) -> +Bayesian Loss (0.931, +3.7%) -> +DE-Fuzzy (0.948, +1.7%)."),
                                  ("Low False Alarm Burden", "False Positive Rate is bounded at 5.8%, preventing faculty alert fatigue and unnecessary panic."),
                                  ("Decision Curve Analysis", "Clinical net benefit curves confirm superior counseling intervention yield across all decision thresholds.")],
                                 "fig32a_ablation_waterfall.png",
                                 stat_number="88.9% Recall", stat_label="Acute Failing Student Capture at Early Screening Threshold (tau = 0.35)")
    add_bottom_banner(s, "★ CLINICAL RECALL", "Every architectural choice contributes statistically validated gains toward catching failing freshers before midterms.")

    # =========================================================================
    # SLIDE 16: RO4: DUAL-SCOPE EXPLAINABLE AI (SHAP & LIME)
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 16)
    add_header(s, "RO4: Dual-Scope Explainable AI (DeepSHAP & LIME)", "RESEARCH OBJECTIVE 4 • DUAL-SCOPE INTERPRETABILITY", "Transforming black-box predictions into transparent institutional and student-level insights")
    add_single_column_visual_card(s, "Macro & Micro Interpretability", "Transparent Decision Logic for Mentors",
                                 [("Macro-Level Global SHAP", "Unmasks national retention drivers: Bedtime Inconsistency (P17), Self-Efficacy (P04), and Study Structure (P14) emerge as top 3 factors."),
                                  ("Micro-Level Local LIME", "Explains individual student risk: reveals exact risk push factors (+0.28 from 4.2h sleep debt) and protective buffers (-0.14 from peer pods)."),
                                  ("Actionable Diagnostic Dossier", "Replaces raw percentages with plain-language diagnostic talking points for faculty mentors."),
                                  ("Demographic Fairness Confirmation", "Confirms that caste, gender, and family income contribute < 5% to prediction, preventing bias reinforcement.")],
                                 "fig35a_shap_beeswarm.png")
    add_bottom_banner(s, "★ DUAL-SCOPE XAI", "Bridges global institutional policy insights with granular, empathetic mentor-student counseling talking points.")

    # =========================================================================
    # SLIDE 17: RO4: THE 3-TIER ACTIONABILITY MATRIX
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 17)
    add_header(s, "RO4: The 3-Tier Actionability Matrix & Ethical Boundaries", "RO4 / ETHICAL RECOURSE • ACTIONABILITY CONSTRAINTS", "Preventing absurd counterfactuals by mathematically locking immutable demographic identities")
    add_single_column_card(s, "Ethical Feasibility Manifold", "Structured 3-Tier Feature Classification",
                           [("Tier 1: Immutable Demographic Shield (delta_j = 0)", "Gender, Caste, Native State, School Board, and Family Socioeconomic Tier are hard-locked mathematically. The optimization algorithm is strictly prohibited from altering immutable human identities, eliminating discriminatory advice."),
                            ("Tier 2: Semi-Actionable & Inertial Attributes (delta_j >= 0)", "Cumulative GPA and prior course attendance records are bounded by temporal inertia and monotonicity constraints. The optimizer cannot recommend past time travel or advising students to 'attend fewer lectures'."),
                            ("Tier 3: Actionable Habit Levers (Subject to Cost Matrix c)", "Targeted behavioral shifts: nightly sleep consistency, self-study hours, nocturnal phone screen exposure, and peer group study participation. The 17-Domain cost matrix c penalizes high-difficulty psychological effort, ensuring realistic habit targets.")],
                           stat_number="delta = 0", stat_label="Strict Mathematical Lock Enforced on All Demographic Coordinates")
    add_bottom_banner(s, "★ ETHICAL RECOURSE", "Projects recommendations strictly onto actionable daily habits, eliminating discriminatory advice and cognitive overload.")

    # =========================================================================
    # SLIDE 18: RO4: CCRO FEASIBLE RECOURSE OPTIMIZER (PGD-AFT)
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 18)
    add_header(s, "RO4: CCRO Feasible Recourse Optimizer (PGD-AFT)", "RO4 / COUNTERFACTUAL RECOURSE • OPTIMIZATION ALGORITHM", "Finding the minimum-effort, clinically feasible path from acute failure risk to academic safety")
    add_single_column_visual_card(s, "PGD-AFT Optimization Engine", "Formulation & Real-Time Convergence",
                                 [("Constrained Formulation", "Minimizes prediction loss to safety (p <= 0.20), regularized by L1 effort, L0 sparsity, and Mahalanobis plausibility."),
                                  ("PGD-AFT Solver", "Projected Gradient Descent with Adaptive Feature Thresholding prunes trivial adjustments and forces demographic projection."),
                                  ("Cognitive Sparsity (||delta||_0 <= 3)", "Concentrates student willpower on at most 2–3 habit modifications, preventing despair and abandonment."),
                                  ("Fast Convergence (18.4 ms)", "Averages 14 iterations (< 20 ms), enabling real-time interactive recourse generation in web browsers.")],
                                 "fig37a_ccro_2d_boundary.png",
                                 stat_number="18.4 ms", stat_label="Average Recourse Optimization Latency (97.8% Validity, 0.0% Feasibility Violation)")
    add_bottom_banner(s, "★ ALGORITHMIC ELEGANCE", "CCRO formulates academic recovery as a constrained optimization problem, delivering sparse, achievable habit changes in 18.4 ms.")

    # =========================================================================
    # SLIDE 19: RO4: CLINICAL RECOURSE WALKTHROUGH — STUDENT S-412
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 19)
    add_header(s, "RO4: Clinical Recourse Walkthrough: Story of Student S-412", "RO4 / CLINICAL CASE STUDY • PRESCRIPTIVE RECOURSE IN ACTION", "Real-world validation: from 86.4% Day-1 attrition risk to verified second-semester academic safety")
    add_single_column_visual_card(s, "From Risk to Academic Safety", "Clinical Prescriptive Intervention Flow",
                                 [("Day-1 Crisis Flag", "Student S-412 flagged with 86.4% Attrition Risk (predicted SGPA 5.20) due to 4:15 AM bedtime, 4.5h nocturnal screen, and imposter panic."),
                                  ("CCRO 3-Point Prescription", "1. Sleep Reset: Shift bedtime to 1:00 AM (+1.75h sleep); 2. Study Scaffolding: Increase study to 2.5h/day; 3. Peer Coding Pod."),
                                  ("Projected Trajectory Shift", "Model projected risk collapsing from 86.4% -> 28.1% with predicted SGPA rising to 6.85."),
                                  ("Actual Follow-Up Reality", "In actual Semester 2 follow-up, S-412 achieved an SGPA of 7.12, remained safely enrolled, and passed all credits.")],
                                 "fig41a_s412_recourse.png",
                                 stat_number="86.4% -> 28.1%", stat_label="Projected Risk Reduction via 3 Sparse Daily Habit Shifts (Actual SGPA = 7.12)")
    add_bottom_banner(s, "★ CLINICAL VALIDATION", "Proves that small, structured habit modifications convert acute Day-1 failure risk into verified second-semester success.")

    # =========================================================================
    # SLIDE 20: RO4: STUDENT KUNDALI RADAR & ARCHETYPES
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 20)
    add_header(s, "RO4: The Student Psychological Kundali Dossier & Archetypes", "RO4 / CLINICAL PROFILING • CULTURALLY EMPATHETIC DOSSIER", "Translating 51 high-dimensional parcels into intuitive 4-quadrant strengths and vulnerabilities")
    add_single_column_visual_card(s, "The 4 Student Archetypes", "Personalized Mentoring Interventions",
                                 [("The Student Kundali Radar", "Modernizes the traditional Kundali into a 4-quadrant polar chart mapping protective strengths and hazard vulnerabilities."),
                                  ("Archetype A (Burnout Striver)", "High study hours (6+h) but chronic sleep debt (< 4h) and imposter anxiety. Requires sleep reset and cognitive reframing."),
                                  ("Archetype B (Disconnected Commuter)", "Day-scholar with 2-hour transit and zero campus social belonging. Requires dedicated day-scholar peer pods."),
                                  ("Archetypes C & D (Overwhelmed / Gamer)", "Facing technical English shock (bilingual buddy pairing) or late-night gaming (digital curfews and morning routines).")],
                                 "fig45a_kundali_radar.png")
    add_bottom_banner(s, "★ CULTURAL EMPATHY", "Replaces cold administrative warnings with a culturally resonant diagnostic dossier that guides empathetic faculty advising.")

    # =========================================================================
    # SLIDE 21: RO5: ZERO-CLOUD CLIENT EDGE AI (ONNX WASM)
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 21)
    add_header(s, "RO5: 100% Private Client-Side Edge AI (ONNX WASM Engine)", "RESEARCH OBJECTIVE 5 • PRIVACY-PRESERVING EDGE AI", "Eliminating cloud data leaks by executing deep neural inference locally inside the web browser")
    add_single_column_visual_card(s, "In-Browser WASM Execution", "Zero-Cloud Edge AI Deployment",
                                 [("184 KB Client Payload", "Quantized BeNet exported to ONNX; gzipped client payload is only 184 KB, loading in < 150 ms over standard 4G connections."),
                                  ("13.8 ms Latency", "Multi-threaded WebAssembly (WASM SIMD) executes neural forward propagation in 13.8 ms on any student laptop or phone."),
                                  ("Zero Cloud Data Egress", "100% of survey responses and prediction vectors remain inside the user's browser session, satisfying India's DPDP Act 2023."),
                                  ("Offline Execution", "Students complete screening and receive recourse plans without requiring active server connectivity.")],
                                 "fig42a_edge_latency.png",
                                 stat_number="184 KB • 13.8 ms", stat_label="Quantized ONNX Model Footprint & In-Browser Multi-Threaded WASM Latency")
    add_bottom_banner(s, "★ RADICAL PRIVACY", "Eliminates institutional data breach risks by running deep neural inference and counterfactual optimization entirely on the client edge.")

    # =========================================================================
    # SLIDE 22: RO5: FACULTY USABILITY TRIAL & TIME-MOTION STUDY
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 22)
    add_header(s, "RO5: Faculty Usability Evaluation & Time-Motion Study", "RESEARCH OBJECTIVE 5 • CLINICAL USABILITY & FIELD TRIAL", "Empirical field trial across 32 faculty mentors demonstrating high operational adoption")
    add_single_column_visual_card(s, "Advisory Field Trial", "65.6% Mentoring Prep Time Reduction",
                                 [("Exceptional System Usability", "Achieved System Usability Scale (SUS) score of 89.2 +- 4.1 across 32 MNIT faculty mentors, placing in the top 5% (Grade A+)."),
                                  ("65.6% Time-Motion Reduction", "Advisory preparation time collapsed from 45.0 minutes to just 15.5 minutes per student during triage periods."),
                                  ("Eliminating Awkward Interrogation", "Pre-computed Kundali radar profiles eliminated awkward exploratory questioning, fostering empathetic trust."),
                                  ("High Clinical Endorsement", "94% of participating professors confirmed they would mandate AcuLearn AI for future fresher cohorts.")],
                                 "fig47a_sus_distribution.png",
                                 stat_number="SUS = 89.2", stat_label="System Usability Scale Score (Grade A+, Top 5% Enterprise Software Usability)")
    add_bottom_banner(s, "★ FIELD ADOPTION", "High usability scores and massive time savings confirm operational feasibility in real university counseling workflows.")

    # =========================================================================
    # SLIDE 23: BASELINE FAIRNESS AUDIT & DEMOGRAPHIC PARITY
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 23)
    add_header(s, "Baseline Fairness Audit & Demographic Parity Evaluation", "ETHICAL AI & FAIRNESS • SUBGROUP DISPARITY AUDIT", "Verifying equitable student protection across gender, caste, and socioeconomic categories")
    add_single_column_visual_card(s, "Fairness Benchmark Audit", "Compliance with Regulatory Equity Standards",
                                 [("Demographic Parity Ratio (0.941)", "BeNet easily surpasses the EEOC 80% Four-Fifths regulatory threshold, whereas Logistic Regression (0.742) fails it."),
                                  ("Equalized Odds Difference (0.024)", "Equalized odds difference is significantly lower than CatBoost (0.052) and XGBoost (0.071)."),
                                  ("Negligible Gender Gap", "ROC-AUC difference between female (0.946) and male (0.949) student cohorts is bounded at just 0.003."),
                                  ("Caste & Category Equity", "High-risk recall disparity between General and Reserved categories (SC/ST/OBC) is strictly bounded under 0.6%.")],
                                 "fig48a_fairness_bars.png",
                                 stat_number="DPR = 0.941", stat_label="Demographic Parity Ratio (Exceeding EEOC 80% Four-Fifths Regulatory Ceiling)")
    add_bottom_banner(s, "★ CERTIFIED EQUITY", "Non-cognitive parceling strips historical bias, ensuring certified fairness across all student demographic subgroups.")

    # =========================================================================
    # SLIDE 24: METHODOLOGICAL LIMITATIONS & BOUNDARIES
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 24)
    add_header(s, "Limitations of the Study & Empirical Boundaries", "SCIENTIFIC TRANSPARENCY • METHODOLOGICAL SCOPE", "Explicit doctoral acknowledgment of primary cohort scope, synthetic data role, and self-reports")
    add_single_column_card(s, "Doctoral Scientific Transparency", "Explicit Acknowledgment of Empirical Boundaries",
                           [("1. Single-Institute Primary Cohort Scope", "Primary real empirical data was sourced from N=276 students at MNIT Jaipur (an Institute of National Importance). Generalizability to non-residential state technical colleges requires ongoing multi-site consortium trials."),
                            ("2. Controlled Synthetic Augmentation Scope", "CTGAN expansion to 2,525 benchmark records served strictly as an architectural stress test. Synthetic data is an experimental computational probe, not an empirical substitute for physical human cohorts."),
                            ("3. Self-Report Recall & Desirability Bias", "Day-1 habit estimates rely on student self-reporting, subject to recall error and social desirability. Mitigated via psychometric manifest parceling, reverse-coded attention checks, and completion speed verification."),
                            ("4. Longitudinal Horizon & Recourse Causality", "Empirical validation currently tracks Semesters 1 and 2; full 8-semester tracking is ongoing through 2027. CCRO recourse represents projected mathematical optimization rather than randomized controlled trial (RCT) causal proofs.")])
    add_bottom_banner(s, "★ SCIENTIFIC INTEGRITY", "Transparently articulating empirical boundaries demonstrates doctoral rigor and frames continuing post-doctoral research.")

    # =========================================================================
    # SLIDE 25: ROADMAP (NEP 2020) & DOCTORAL CONCLUSION
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 25)
    add_header(s, "Implementation Roadmap (NEP 2020) & Doctoral Conclusion", "SYNTHESIS • IMPLEMENTATION ROADMAP & DOCTORAL CONCLUSION", "Scaling from MNIT Jaipur to a national retention platform under National Education Policy 2020")
    add_single_column_visual_card(s, "3-Phase Scaling Roadmap", "Doctoral Impact & Core Conclusion",
                                 [("Phase 1: Single-Site Pilot (Completed)", "MNIT Jaipur validation across N=276 freshers, 32 faculty mentors, open-source WASM engine, and 5 publications."),
                                  ("Phase 2: State Consortium (2026–2027)", "Expanding to 15 technical engineering colleges across Rajasthan technical university network."),
                                  ("Phase 3: National Platform (NEP 2020)", "Public open-access deployment supporting National Education Policy student retention and mental wellness mandates."),
                                  ("Doctoral Conclusion", "College failure is preventable on Day 1 through non-cognitive behavioral intelligence, shifting analytics from autopsy to care.")],
                                 "fig53a_doctoral_gantt.png")
    add_bottom_banner(s, "★ ENDURING CONTRIBUTION", "AcuLearn AI proves that first-year failure is preventable on Day 1, transforming educational data mining into empathetic student care.")

    # =========================================================================
    # SLIDE 26: BACKUP 1: 17 CONSTRUCTS CFA LOADINGS & RELIABILITY TABLE
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 26)
    add_header(s, "Backup Slide 1: SSQ-180 CFA Loadings & Construct Reliability", "COMMITTEE BACKUP KIT • PSYCHOMETRIC MEASUREMENT MODEL", "Standardized factor loadings, composite reliability, and average variance extracted across constructs")
    add_single_column_card(s, "Convergent & Discriminant Validity", "Psychometric Measurement Verification Across All 17 Domains",
                           [("Standardized Factor Loadings (lambda >= 0.80)", "All 51 manifest parcels exhibit standardized factor loadings exceeding 0.80 on their designated latent constructs (p < 0.001), demonstrating robust indicator reliability."),
                            ("Composite Reliability (CR >= 0.85)", "Composite reliability exceeds 0.85 across all 17 domains, easily surpassing the recommended 0.70 benchmark and establishing high internal consistency."),
                            ("Average Variance Extracted (AVE >= 0.58)", "AVE exceeds 0.58 across all constructs, confirming that latent constructs capture substantially more variance than measurement error."),
                            ("Fornell-Larcker & HTMT.85 Criteria", "Square root of AVE exceeds all inter-construct correlations, and all pairwise HTMT ratios are < 0.64 (well below 0.85 ceiling), confirming absolute discriminant validity.")])
    add_bottom_banner(s, "★ BACKUP EVIDENCE", "Factor loadings (lambda > 0.80, p < 0.001) and AVE (> 0.58) strictly confirm convergent and discriminant psychometric validity.")

    # =========================================================================
    # SLIDE 27: BACKUP 2: BENET HYPERPARAMETERS & LIPSCHITZ CONTINUITY
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 27)
    add_header(s, "Backup Slide 2: BeNet Hyperparameter Grid & Architecture Specs", "COMMITTEE BACKUP KIT • DEEP LEARNING ARCHITECTURAL SPECS", "Complete specifications for GLU trunk, loss weighting, and Lipschitz continuity constraints")
    add_single_column_card(s, "Deep Learning Specifications", "Hyperparameter Selection Grid & Spectral Normalization Mechanics",
                           [("Network Hyperparameters", "Gated Linear Units: 51 input parcels -> 128 hidden features -> Swish activation -> Dropout (0.25). Optimizer: AdamW (weight decay 1e-4, initial lr 1e-3, Cosine Annealing). Batch size = 64 with early stopping (epoch 38)."),
                            ("Spectral Normalization Mechanics", "Weight matrices are divided by their spectral norm sigma(W): W_sn = W / sigma(W), mathematically guaranteeing ||W_sn||_2 <= 1.0."),
                            ("Global Lipschitz Constant (L <= 1.0)", "Because activation functions (Swish, Sigmoid) are 1-Lipschitz, the global network Lipschitz constant satisfies L <= 1.0, ensuring gradient stability."),
                            ("Adversarial & Recourse Stability", "Bounded gradients prevent explosive oscillations during projected gradient descent counterfactual search, ensuring smooth recourse manifolds.")])
    add_bottom_banner(s, "★ BACKUP EVIDENCE", "Spectral normalization guarantees Lipschitz continuity (L <= 1.0), ensuring smooth, stable counterfactual recourse convergence.")

    # =========================================================================
    # SLIDE 28: BACKUP 3: CCRO MATHEMATICAL FORMULATION & CONVERGENCE
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 28)
    add_header(s, "Backup Slide 3: CCRO Mathematical Formulation & Convergence", "COMMITTEE BACKUP KIT • COUNTERFACTUAL OPTIMIZATION RIGOR", "Formal loss optimization, non-expansive projection, and step-size convergence guarantees")
    add_single_column_card(s, "Mathematical Optimization Rigor", "Objective Function Formulation & Convergence Proofs",
                           [("Objective Function Formulation", "arg min { max(0, f1(x+delta) - tau)^2 + lambda1*||c * delta||_1 + lambda2*||delta||_0 + lambda3*D_plaus } subject to delta in C. Demographic hard constraint locks delta_j = 0 for all immutable coordinates."),
                            ("Lipschitz Bounded Gradient", "Since ||grad f1||_2 <= L via spectral normalization, the objective gradient grad J is L-Lipschitz continuous."),
                            ("Step-Size Convergence Guarantee", "Using learning rate eta < 2/L, PGD-AFT is mathematically proven to converge monotonically to a stationary local minimum."),
                            ("Non-Expansive Projection (Pi_C)", "Orthogonal projection Pi_C onto the convex feasibility box is strictly non-expansive: ||Pi_C(u) - Pi_C(v)|| <= ||u - v||, enforcing exactly 0.0% feasibility violation.")])
    add_bottom_banner(s, "★ BACKUP EVIDENCE", "Proven Lipschitz continuity and non-expansive orthogonal projection guarantee stable convergence in 14 iterations (< 20 ms).")

    # =========================================================================
    # SLIDE 29: BACKUP 4: CONFUSION MATRIX ON REAL TEST SPLIT & CALIBRATION
    # =========================================================================
    s = prs.slides.add_slide(blank_layout); add_slide_frame(s, 29)
    add_header(s, "Backup Slide 4: Confusion Matrices, PR Curves & Calibration", "COMMITTEE BACKUP KIT • EMPIRICAL CLASSIFICATION DIAGNOSTICS", "Evaluation across default (0.50) and early-warning screening (0.35) decision thresholds")
    add_single_column_visual_card(s, "Held-Out Real Test Set (N=56)", "Threshold Diagnostic Comparison",
                                 [("Default Threshold (0.50)", "Sensitivity = 77.8%, Specificity = 93.6%, Precision = 70.0%, Negative Predictive Value = 95.7%."),
                                  ("Screening Threshold (0.35)", "Sensitivity = 88.9%, Specificity = 87.2%, Negative Predictive Value = 97.6% (catches nearly 9 out of 10 failing students)."),
                                  ("Low Brier Score (0.068)", "Mean squared error of probabilistic predictions confirms highly accurate, reliable risk estimates."),
                                  ("Expected Calibration Error", "ECE = 0.028 confirms predicted probabilities reflect true empirical failure frequencies.")],
                                 "fig_confusion_matrices.png",
                                 stat_number="NPV = 97.6%", stat_label="Negative Predictive Value at Early Screening Threshold (tau = 0.35)")
    add_bottom_banner(s, "★ BACKUP EVIDENCE", "At the screening threshold (0.35), BeNet achieves 88.9% recall and 97.6% NPV, minimizing catastrophic false negatives.")

    # Save presentation
    prs.save(OUTPUT_PPTX)
    print(f"\n=======================================================")
    print(f"Single-Column Blue Defense Deck generated successfully!")
    print(f"Total Slides: {len(prs.slides)}")
    print(f"Saved to: {OUTPUT_PPTX}")
    print(f"=======================================================")

if __name__ == "__main__":
    build_presentation()
