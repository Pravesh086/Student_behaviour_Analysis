"""
generate_adrid_pptx.py
=======================
Generates the comprehensive 53-slide PowerPoint presentation (.pptx) strictly adhering
to the MNIT Jaipur Pre-PhD Open Seminar format (Madrid Beamer Theme) matching
'progress_report_beamer.tex' and the reference department template.

Event: Pre-PhD Open Seminar
Date: 19 November 2026
Candidate: Pravesh Kumar Bansal (2019RCP9557)
Supervisor: Dr. Mushtaq Ahmed
Affiliation: Department of Computer Science & Engineering, MNIT Jaipur
Dissertation Title:
"Intelligent Multidimensional Frameworks for Proactive Student Retention,
Academic Trajectory Prediction, and Explainable Counterfactual Recourse in Higher Education"
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

TOTAL_SLIDES = 83

# Color Palette (Madrid Blue Theme)
COLOR_PRIMARY_BLUE = RGBColor(51, 51, 178)     # #3333B2
COLOR_DARK_BLUE = RGBColor(25, 25, 89)          # #191959
COLOR_MEDIUM_BLUE = RGBColor(38, 38, 134)       # #262686
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_TEXT_DARK = RGBColor(30, 41, 59)          # Slate 800
COLOR_TEXT_BODY = RGBColor(51, 65, 85)          # Slate 700
COLOR_TEXT_MUTED = RGBColor(148, 163, 184)      # Slate 400
COLOR_BG_CARD = RGBColor(248, 250, 252)
COLOR_BORDER = RGBColor(203, 213, 225)
COLOR_HEADER_BG = RGBColor(238, 242, 255)
COLOR_GOLD = RGBColor(180, 83, 9)

SECTIONS = [
    "Publication Details",
    "Introduction",
    "Literature Survey",
    "Motivation",
    "Proposed Methodology",
    "Results and Discussion",
    "Clinical Deployment",
    "Challenges",
    "Conclusion",
    "References"
]

def add_footer(slide, current_slide_num):
    """Draws the 3-segment Madrid infolines footline at the bottom."""
    left_y = Inches(7.08)
    box_h = Inches(0.32)
    
    # 1. Left Box (Dark Blue) - Author & Affiliation
    b1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.4), left_y, Inches(2.8), box_h)
    b1.fill.solid()
    b1.fill.fore_color.rgb = COLOR_DARK_BLUE
    b1.line.color.rgb = COLOR_DARK_BLUE
    tf1 = b1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Pravesh (MNIT Jaipur)"
    p1.font.size = Pt(9)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.alignment = PP_ALIGN.CENTER
    
    # 2. Middle Box (Medium Blue) - Seminar Title
    b2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(3.2), left_y, Inches(3.6), box_h)
    b2.fill.solid()
    b2.fill.fore_color.rgb = COLOR_MEDIUM_BLUE
    b2.line.color.rgb = COLOR_MEDIUM_BLUE
    tf2 = b2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = "Pre-PhD Open Seminar"
    p2.font.size = Pt(9)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_WHITE
    p2.alignment = PP_ALIGN.CENTER
    
    # 3. Right Box (Accent Blue) - Date & Slide Number
    b3 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), left_y, Inches(2.8), box_h)
    b3.fill.solid()
    b3.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    b3.line.color.rgb = COLOR_PRIMARY_BLUE
    tf3 = b3.text_frame
    tf3.word_wrap = True
    p3 = tf3.paragraphs[0]
    p3.text = f"19 November 2026       {current_slide_num} / {TOTAL_SLIDES}"
    p3.font.size = Pt(9)
    p3.font.bold = True
    p3.font.color.rgb = COLOR_WHITE
    p3.alignment = PP_ALIGN.CENTER

def add_header(slide, title_text):
    """Draws the top Madrid blue frametitle banner."""
    banner = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.4), Inches(0.35), Inches(9.2), Inches(0.68))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    banner.line.color.rgb = COLOR_PRIMARY_BLUE
    tf = banner.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.LEFT
    tf.margin_left = Inches(0.25)
    tf.margin_top = Inches(0.12)

def add_image_slide(prs, blank_layout, slide_idx, title, img_path, caption, note=""):
    """Standard layout for slides with high-DPI figures."""
    s = prs.slides.add_slide(blank_layout)
    add_header(s, title)
    
    # Container box for figure
    fig_card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.15), Inches(9.0), Inches(5.35))
    fig_card.fill.solid()
    fig_card.fill.fore_color.rgb = COLOR_BG_CARD
    fig_card.line.color.rgb = COLOR_BORDER
    fig_card.line.width = Pt(1)
    
    if os.path.exists(img_path):
        s.shapes.add_picture(img_path, Inches(0.7), Inches(1.22), width=Inches(8.6))
    
    # Caption Box
    cap_box = s.shapes.add_textbox(Inches(0.5), Inches(6.15), Inches(9.0), Inches(0.75))
    ctf = cap_box.text_frame
    ctf.word_wrap = True
    cp = ctf.paragraphs[0]
    cp.text = caption
    cp.font.size = Pt(12)
    cp.font.bold = True
    cp.font.color.rgb = COLOR_DARK_BLUE
    cp.alignment = PP_ALIGN.CENTER
    
    if note:
        cp2 = ctf.add_paragraph()
        cp2.text = note
        cp2.font.size = Pt(10)
        cp2.font.color.rgb = COLOR_TEXT_BODY
        cp2.alignment = PP_ALIGN.CENTER
        
    add_footer(s, slide_idx)
    return s

def add_bullet_slide(prs, blank_layout, slide_idx, title, items):
    """Standard layout for structured multi-item bullet slides."""
    s = prs.slides.add_slide(blank_layout)
    add_header(s, title)
    
    cbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.15), Inches(9.0), Inches(5.65))
    cbox.fill.solid()
    cbox.fill.fore_color.rgb = COLOR_BG_CARD
    cbox.line.color.rgb = COLOR_BORDER
    cbox.line.width = Pt(1)
    
    tf = cbox.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.4)
    tf.margin_right = Inches(0.4)
    tf.margin_top = Inches(0.25)
    
    first = True
    for item in items:
        head, subs = item[0], item[1]
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.text = f"•  {head}"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_BLUE
        p.space_before = Pt(6)
        
        for sub in subs:
            sp = tf.add_paragraph()
            sp.text = f"    -  {sub}"
            sp.font.size = Pt(12)
            sp.font.color.rgb = COLOR_TEXT_BODY
            sp.space_before = Pt(2)
            
    add_footer(s, slide_idx)
    return s


def add_references_slide(prs, blank_layout, slide_idx, title, ref_items):
    """Draws a dedicated references slide displaying exactly 10 references in 2 balanced columns."""
    s = prs.slides.add_slide(blank_layout)
    add_header(s, title)
    
    # Left Column Card (refs 0 to 4)
    c_left = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.2), Inches(4.35), Inches(5.65))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = COLOR_BG_CARD
    c_left.line.color.rgb = COLOR_BORDER
    c_left.line.width = Pt(1)
    
    tf_left = c_left.text_frame
    tf_left.word_wrap = True
    tf_left.margin_left = Inches(0.2)
    tf_left.margin_right = Inches(0.2)
    tf_left.margin_top = Inches(0.18)
    
    first = True
    for ref_num, authors, details in ref_items[:5]:
        p = tf_left.paragraphs[0] if first else tf_left.add_paragraph()
        first = False
        p.text = f"[{ref_num}] {authors}"
        p.font.size = Pt(9.2)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_BLUE
        if not first:
            p.space_before = Pt(5)
            
        p_body = tf_left.add_paragraph()
        p_body.text = details
        p_body.font.size = Pt(8.0)
        p_body.font.color.rgb = COLOR_TEXT_BODY
        p_body.space_before = Pt(1)
        p_body.space_after = Pt(3)
        
    # Right Column Card (refs 5 to 9)
    c_right = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.15), Inches(1.2), Inches(4.35), Inches(5.65))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = COLOR_BG_CARD
    c_right.line.color.rgb = COLOR_BORDER
    c_right.line.width = Pt(1)
    
    tf_right = c_right.text_frame
    tf_right.word_wrap = True
    tf_right.margin_left = Inches(0.2)
    tf_right.margin_right = Inches(0.2)
    tf_right.margin_top = Inches(0.18)
    
    first_r = True
    for ref_num, authors, details in ref_items[5:]:
        p = tf_right.paragraphs[0] if first_r else tf_right.add_paragraph()
        first_r = False
        p.text = f"[{ref_num}] {authors}"
        p.font.size = Pt(9.2)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_BLUE
        if not first_r:
            p.space_before = Pt(5)
            
        p_body = tf_right.add_paragraph()
        p_body.text = details
        p_body.font.size = Pt(8.0)
        p_body.font.color.rgb = COLOR_TEXT_BODY
        p_body.space_before = Pt(1)
        p_body.space_after = Pt(3)
        
    add_footer(s, slide_idx)
    return s

def add_lit_table_slide(prs, blank_layout, slide_idx, title, headers, col_widths, rows_data):
    """Creates a high-impact Madrid-style comparative literature review table slide."""
    s = prs.slides.add_slide(blank_layout)
    add_header(s, title)
    
    num_rows = len(rows_data) + 1
    num_cols = len(headers)
    tbl_shape = s.shapes.add_table(num_rows, num_cols, Inches(0.5), Inches(1.25), Inches(9.0), Inches(5.5))
    tbl = tbl_shape.table
    
    for c_i, w in enumerate(col_widths):
        tbl.columns[c_i].width = Inches(w)
        
    for c_i, h in enumerate(headers):
        cell = tbl.cell(0, c_i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER
        
    for r_i, row in enumerate(rows_data, 1):
        for c_i, val in enumerate(row):
            cell = tbl.cell(r_i, c_i)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_HEADER_BG if r_i % 2 == 1 else COLOR_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9.0)
            p.font.bold = (c_i == 0 or c_i == num_cols - 1)
            p.font.color.rgb = COLOR_PRIMARY_BLUE if c_i == num_cols - 1 else (COLOR_DARK_BLUE if c_i == 0 else COLOR_TEXT_BODY)
            p.alignment = PP_ALIGN.CENTER if c_i == 0 else PP_ALIGN.LEFT
            
    add_footer(s, slide_idx)
    return s

def build_deck():
    prs = Presentation()
    prs.slide_width = Inches(10.0)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    slide_idx = 1
    
    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    
    # Header Card Banner
    tbox = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.55), Inches(8.8), Inches(1.9))
    tbox.fill.solid()
    tbox.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    tbox.line.color.rgb = COLOR_PRIMARY_BLUE
    tf = tbox.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "Pre-PhD Open Seminar"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf.add_paragraph()
    p2.text = "“Intelligent Multidimensional Frameworks for Proactive Student Retention, Academic Trajectory Prediction, and Explainable Counterfactual Recourse in Higher Education”"
    p2.font.size = Pt(13.5)
    p2.font.color.rgb = COLOR_WHITE
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(4)
    
    # Candidate Metadata
    cbox = s1.shapes.add_textbox(Inches(0.6), Inches(2.65), Inches(8.8), Inches(4.2))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    cp1 = ctf.paragraphs[0]
    cp1.text = "by"
    cp1.font.size = Pt(13)
    cp1.font.italic = True
    cp1.font.color.rgb = COLOR_TEXT_DARK
    cp1.alignment = PP_ALIGN.CENTER
    
    cp2 = ctf.add_paragraph()
    cp2.text = "Pravesh Kumar Bansal"
    cp2.font.size = Pt(19)
    cp2.font.bold = True
    cp2.font.color.rgb = COLOR_TEXT_DARK
    cp2.alignment = PP_ALIGN.CENTER
    
    cp3 = ctf.add_paragraph()
    cp3.text = "( 2019RCP9557 )"
    cp3.font.size = Pt(14)
    cp3.font.color.rgb = COLOR_TEXT_DARK
    cp3.alignment = PP_ALIGN.CENTER
    
    cp4 = ctf.add_paragraph()
    cp4.text = "Supervisor : Dr. Mushtaq Ahmed"
    cp4.font.size = Pt(15)
    cp4.font.bold = True
    cp4.font.color.rgb = COLOR_PRIMARY_BLUE
    cp4.alignment = PP_ALIGN.CENTER
    cp4.space_before = Pt(4)
    
    cp4b = ctf.add_paragraph()
    cp4b.text = "Associate Professor and Head"
    cp4b.font.size = Pt(13)
    cp4b.font.bold = True
    cp4b.font.color.rgb = COLOR_PRIMARY_BLUE
    cp4b.alignment = PP_ALIGN.CENTER
    cp4b.space_before = Pt(2)
    
    cp5 = ctf.add_paragraph()
    cp5.text = "Department of Computer Science and Engineering"
    cp5.font.size = Pt(14)
    cp5.font.bold = True
    cp5.font.color.rgb = COLOR_TEXT_DARK
    cp5.alignment = PP_ALIGN.CENTER
    cp5.space_before = Pt(8)
    
    cp6 = ctf.add_paragraph()
    cp6.text = "Malaviya National Institute of Technology Jaipur"
    cp6.font.size = Pt(14)
    cp6.font.color.rgb = COLOR_TEXT_DARK
    cp6.alignment = PP_ALIGN.CENTER
    
    add_footer(s1, slide_idx)
    slide_idx += 1
    
    # =========================================================================
    # SLIDE 2: CONTENTS
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Contents")
    
    c_y = 1.25
    for i, sec in enumerate(SECTIONS, 1):
        badge = s2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.2), Inches(c_y), Inches(0.38), Inches(0.38))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        badge.line.color.rgb = COLOR_PRIMARY_BLUE
        btf = badge.text_frame
        bp = btf.paragraphs[0]
        bp.text = str(i)
        bp.font.size = Pt(12)
        bp.font.bold = True
        bp.font.color.rgb = COLOR_WHITE
        bp.alignment = PP_ALIGN.CENTER
        
        lbl = s2.shapes.add_textbox(Inches(1.8), Inches(c_y - 0.05), Inches(7.0), Inches(0.42))
        ltf = lbl.text_frame
        lp = ltf.paragraphs[0]
        lp.text = sec
        lp.font.size = Pt(14)
        lp.font.bold = True
        lp.font.color.rgb = COLOR_TEXT_DARK
        
        c_y += 0.52
        
    add_footer(s2, slide_idx)
    slide_idx += 1
    
    def make_current_section_slide(active_idx):
        nonlocal slide_idx
        s = prs.slides.add_slide(blank_layout)
        add_header(s, "Current Section")
        
        c_y = 1.25
        for i, sec in enumerate(SECTIONS, 1):
            is_active = (i == active_idx)
            badge = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.2), Inches(c_y), Inches(0.38), Inches(0.38))
            badge.fill.solid()
            badge.fill.fore_color.rgb = COLOR_PRIMARY_BLUE if is_active else COLOR_TEXT_MUTED
            badge.line.color.rgb = COLOR_PRIMARY_BLUE if is_active else COLOR_TEXT_MUTED
            btf = badge.text_frame
            bp = btf.paragraphs[0]
            bp.text = str(i)
            bp.font.size = Pt(12)
            bp.font.bold = True
            bp.font.color.rgb = COLOR_WHITE
            bp.alignment = PP_ALIGN.CENTER
            
            lbl = s.shapes.add_textbox(Inches(1.8), Inches(c_y - 0.05), Inches(7.0), Inches(0.42))
            ltf = lbl.text_frame
            lp = ltf.paragraphs[0]
            lp.text = sec
            lp.font.size = Pt(15 if is_active else 13.5)
            lp.font.bold = is_active
            lp.font.color.rgb = COLOR_PRIMARY_BLUE if is_active else COLOR_TEXT_MUTED
            
            c_y += 0.52
            
        add_footer(s, slide_idx)
        slide_idx += 1
        return s

    # =========================================================================
    # SECTION 1: PUBLICATION DETAILS (Slides 3, 4, 5, 6)
    # =========================================================================
    make_current_section_slide(1)  # Slide 3
    
    # Slide 4: Publication Table Summary
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Doctoral Publications Summary")
    
    rows, cols = 7, 4
    tbl_shape = s4.shapes.add_table(rows, cols, Inches(0.75), Inches(1.25), Inches(8.5), Inches(2.5))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(2.3)
    tbl.columns[1].width = Inches(2.2)
    tbl.columns[2].width = Inches(2.4)
    tbl.columns[3].width = Inches(1.6)
    
    headers = ["Venue / Journal", "Indexing / Metrics", "Role / Focus", "Status"]
    for c_i, h in enumerate(headers):
        cell = tbl.cell(0, c_i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER
        
    pub_data = [
        ("IEEE Access", "SCIE, JCR Q1 (IF: 3.9)", "Core BeNet Deep Model", "Published"),
        ("AIP Conf. Proc.", "Scopus Indexed", "Fuzzy Risk Modeling", "Published"),
        ("IEEE ICETST 2024", "IEEE Xplore / Scopus", "Early Failure Detection", "Published"),
        ("IEEE ICECI 2023", "IEEE Xplore / Scopus", "Cognitive Screening", "Published"),
        ("Springer ICDSA 2025", "Scopus / CCIS", "Explainable AI & SHAP", "Published"),
        ("Comp. Appl. in Eng. Educ.", "Wiley, SCIE Q1 (In Queue)", "Counterfactual Recourse", "Under Review")
    ]
    for r_i, row in enumerate(pub_data, 1):
        for c_i, val in enumerate(row):
            cell = tbl.cell(r_i, c_i)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_HEADER_BG if r_i % 2 == 1 else COLOR_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9.5)
            p.font.bold = (c_i == 0 or c_i == 3)
            p.font.color.rgb = COLOR_DARK_BLUE if c_i == 0 else COLOR_TEXT_DARK
            p.alignment = PP_ALIGN.CENTER
            
    sum_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.75), Inches(4.0), Inches(8.5), Inches(2.65))
    sum_card.fill.solid()
    sum_card.fill.fore_color.rgb = COLOR_BG_CARD
    sum_card.line.color.rgb = COLOR_BORDER
    stf = sum_card.text_frame
    stf.word_wrap = True
    stf.margin_left = Inches(0.25)
    stf.margin_top = Inches(0.18)
    
    sp1 = stf.paragraphs[0]
    sp1.text = "Key Publication Highlights & Academic Validation:"
    sp1.font.size = Pt(12)
    sp1.font.bold = True
    sp1.font.color.rgb = COLOR_DARK_BLUE
    
    bullets = [
        "1 Flagship Q1 Journal in IEEE Access (Impact Factor 3.9, 19 pages, published Nov 2025).",
        "4 International Conferences published across IEEE Xplore, AIP, and Springer.",
        "1 Comprehensive Translational Journal paper under review in CAEE / Wiley (Submitted 2026).",
        "Complete empirical validation on N = 276 student cohort across 4 engineering departments."
    ]
    for b in bullets:
        bp = stf.add_paragraph()
        bp.text = f"•  {b}"
        bp.font.size = Pt(10.5)
        bp.font.color.rgb = COLOR_TEXT_BODY
        bp.space_before = Pt(3)
        
    add_footer(s4, slide_idx)
    slide_idx += 1
    
    # Slide 5: Publication Details Part 1
    add_bullet_slide(prs, blank_layout, slide_idx, "Doctoral Publications Record", [
        ("Paper 1 (Flagship Journal, Q1 Published):", [
            "P. K. Bansal and M. Ahmed, 'BeNet: Multi-Task Deep Neural Architecture with Uncertainty Loss Balancing for Student Academic Trajectory Prediction and Risk Modeling,' IEEE Access, vol. 13, pp. 204910-204928, Nov 2025.",
            "Impact Factor: 3.9 | JCR Q1 | SCIE Indexed | DOI: 10.1109/ACCESS.2025.3638368."
        ]),
        ("Paper 2 (AIP Conference, Published):", [
            "P. K. Bansal and M. Ahmed, 'Fuzzy Logic-Based Analysis of Student Behavior Patterns and Transition Risk in Technical Higher Education,' AIP Conference Proceedings, vol. 3204, art. 020015, Feb 2025.",
            "Scopus Indexed | Peer Reviewed | DOI: 10.1063/5.0247979."
        ]),
        ("Paper 3 (IEEE Conference, Published):", [
            "P. K. Bansal and M. Ahmed, 'Optimized Perception-Based Student Behavior Modeling and Early Academic Failure Detection,' IEEE 2nd International Conference on Emerging Trends in Smart Tech (ICETST 2024), Dec 2024.",
            "IEEE Xplore & Scopus Indexed | Jaipur, India."
        ])
    ])
    slide_idx += 1
    
    # Slide 6: Publication Details Part 2
    add_bullet_slide(prs, blank_layout, slide_idx, "Doctoral Publications Record (Contd.)", [
        ("Paper 4 (IEEE ICECI Conference, Published):", [
            "P. K. Bansal and M. Ahmed, 'Expert-System Approach for Early Student Behavioral Assessment and Cognitive Screening,' Proc. International Conference on Electrical, Communication and Information (ICECI 2023), pp. 101-106, 2023.",
            "Scopus Indexed | IEEE Xplore."
        ]),
        ("Paper 5 (Springer ICDSA Conference, Published):", [
            "P. K. Bansal and M. Ahmed, 'Hybrid Explainable Artificial Intelligence and Feature Attribution for Educational Prediction,' Proc. International Conference on Data Science and Applications (ICDSA 2025), Springer CCIS, pp. 310-318, 2025.",
            "Springer CCIS Series | Scopus Indexed."
        ]),
        ("Paper 6 (High-Impact Journal, Under Review / In Queue):", [
            "P. K. Bansal and M. Ahmed, 'From Academic-Risk Prediction to Constraint-Aware Student Support: Counterfactual Recourse for Engineering Education,' Computer Applications in Engineering Education (Wiley, SCIE Q1, Manuscript: CAEE-2026-0184).",
            "Submitted Q1 2026 | SCIE / JCR Q1 Journal."
        ])
    ])
    slide_idx += 1

    # =========================================================================
    # SECTION 2: INTRODUCTION (Slides 7 to 13)
    # =========================================================================
    make_current_section_slide(2)  # Slide 7

    # Slide 8: Research Background: Student Retention in Higher Education (NEW SLIDE 1)
    add_bullet_slide(prs, blank_layout, slide_idx, "Research Background: Student Retention in Higher Education", [
        ("Core Terminology & Operational Definitions:", [
            "Student Retention: The institutional metric and longitudinal developmental process of a student persisting and successfully completing their prescribed engineering degree programme.",
            "Attrition / Departure: Early voluntary withdrawal, academic failure, or formal institutional debarment prior to graduation."
        ]),
        ("Dual Demands of Technical Higher Education:", [
            "Engineering curricula require high cognitive analytical aptitude paired with robust non-cognitive self-regulation (time management, emotional resilience, academic help-seeking).",
            "Cognitive entrance test scores (12th / JEE) measure prior test aptitude but fail to capture longitudinal adaptive persistence."
        ]),
        ("The Latency Gap in Institutional Early-Warning Systems:", [
            "Conventional university monitoring depends on semester grade point averages (SGPA), registrar transcripts, and LMS clickstreams.",
            "These indicators become observable only post-mortem—after academic failure has already materialized."
        ])
    ])
    slide_idx += 1

    # Slide 9: Problem Statement (NEW SLIDE 2)
    add_bullet_slide(prs, blank_layout, slide_idx, "Problem Statement", [
        ("The School-to-University Disconnect:", [
            "Engineering freshers face a severe autonomy shock transitioning from spoon-fed 14-hour entrance coaching to self-directed university study, precipitating early disengagement."
        ]),
        ("Systemic Shortcomings of Contemporary Retention Frameworks:", [
            "Reactive Late Detection: Existing models predict failure at Weeks 10–14, forfeiting the actionable 90-day counselling window.",
            "Psychological Blind Spot: Models rely heavily on LMS logs and prior marks, completely ignoring latent constructs (anxiety, imposter syndrome, sleep debt, belonging).",
            "Diagnostic Without Prescriptive Recourse: Black-box classifiers (SVM, XGBoost) and XAI attribution (SHAP) diagnose failure risk without prescribing actionable, feasible recovery trajectories.",
            "Privacy & Regulatory Vulnerability: Centralized cloud processing of mental health and psychometric data violates India's DPDP Act 2023."
        ]),
        ("Formal Doctoral Problem Statement:", [
            "There is an urgent necessity for an early, multidimensional, explainable, and privacy-preserving intelligent framework that predicts student attrition risk on Day-1 and recommends feasible, cost-bounded behavioural counterfactual recourse."
        ])
    ])
    slide_idx += 1
    
    # Slide 8: 12th Coaching to College Transition Shock
    add_bullet_slide(prs, blank_layout, slide_idx, "12th Coaching to College Transition Shock", [
        ("The School-to-College Fracture:", [
            "The shift from rigid, highly regimented 14-hour JEE coaching academies to unstructured college autonomy causes widespread psychological and behavioral disorientation."
        ]),
        ("Shock 1: The Freedom Trap (Autonomy Chasm):", [
            "Supervision vanishes overnight in hostels. Freshers mistake freedom for vacation, leading to 6-8 hours daily of mobile gaming and social isolation."
        ]),
        ("Shock 2: Imposter Identity Crisis ('Big-Fish-Little-Pond' Effect):", [
            "School toppers suddenly find themselves surrounded by hundreds of peers of equal or higher caliber; an early minor setback shatters confidence and causes silent withdrawal."
        ]),
        ("Shock 3: Circadian Collapse & Sleep Debt:", [
            "Corridor social culture pushes sleep past 3:30 AM before 8:00 AM engineering mathematics lectures, creating chronic prefrontal executive exhaustion."
        ]),
        ("Shock 4: Cognitive & Language Disconnect:", [
            "MCQ pattern tricks fail when faced with rigorous analytical derivations; regional-medium students face a massive English medium comprehension barrier."
        ])
    ])
    slide_idx += 1
    
    # Slide 9: National Crisis Attrition Benchmark (Enlarged Figure 4a)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "National Crisis: Engineering Student Attrition", 
                    "assets/fig4a_attrition_benchmark.png", 
                    "Figure: National Technical Education Attrition Toll & First-Year Crisis Benchmark",
                    "Over 18.4% attrition across technical institutions creates Rs 8-15 Lakhs financial loss per dropout and severe NIRF penalties.")
    slide_idx += 1
    
    # Slide 10: 4-Stage Behavioral Departure Curve (Enlarged Figure 5a)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "The 4-Stage Behavioral Departure Trajectory", 
                    "assets/fig5a_trajectory_curve.png", 
                    "Figure: The 4-Stage Departure Curve: From Transition Shock to Formal Institutional Drop-Out",
                    "Stage 1 (Perception Shock, W1-W4) -> Stage 2 (Disengagement, W5-W8) -> Stage 3 (Academic Collapse) -> Stage 4 (Formal Departure).")
    slide_idx += 1
    
    # Slide 11: Cognitive vs Non-Cognitive Assessment Gap
    add_bullet_slide(prs, blank_layout, slide_idx, "Cognitive vs. Non-Cognitive Assessment Gap", [
        ("Why Entrance Marks Fail to Predict Retention:", [
            "12th board marks and JEE scores capture historical test-taking aptitude at a single time-point, not longitudinal self-regulation or emotional resilience.",
            "Correlation between entrance rank and first-year academic retention is empirically weak (Pearson r = 0.12 - 0.18)."
        ]),
        ("The Invisible Non-Cognitive Indicators:", [
            "Academic Self-Efficacy, Time Management, Stress Resilience, and Help-Seeking dictate whether a student survives the transition.",
            "Existing institutional ERP systems record grades only after semester examinations - when the cumulative GPA has already collapsed."
        ]),
        ("The Need for Proactive Intelligence:", [
            "Screening students in Weeks 3-5 allows timely, proactive behavioral guidance before irreversible failure occurs."
        ])
    ])
    slide_idx += 1

    # Slide 14: Research Gaps Addressed by This Thesis (NEW SLIDE 3)
    gap_headers = ["Identified Research Gap", "Conventional System Limitation", "AcuLearn AI Resolution & Contribution"]
    gap_widths = [2.2, 3.4, 3.4]
    gap_rows = [
        ("1. Late Risk Detection", "Evaluates risk at Weeks 10–14 using mid-term/end-term grades; intervention window lost.", "Day-1 SSQ-180 intake establishes a 90-day proactive intervention window before academic damage."),
        ("2. Non-Cognitive Blind Spot", "Confined to LMS clickstreams and prior marks; blind to burnout, imposter syndrome, and sleep.", "17-factor psychometric battery across 4 quadrants capturing holistic socio-emotional dynamics."),
        ("3. Attribution Without Action", "SHAP/LIME reveal feature importance but fail to provide actionable student recovery pathways.", "Constrained Counterfactual Recourse (CCRO) generates realistic, cost-bounded behavioral nudges."),
        ("4. Centralized Privacy Risk", "Transmits sensitive student psychological and mental health data to remote cloud servers.", "100% Client-Side WebAssembly (WASM/ONNX) execution ensuring zero raw-data egress (DPDP Act 2023).")
    ]
    add_lit_table_slide(prs, blank_layout, slide_idx, "Research Gaps Addressed by This Thesis", gap_headers, gap_widths, gap_rows)
    slide_idx += 1

    # Slide 15: Aim and Scope of the Thesis (NEW SLIDE 4)
    add_bullet_slide(prs, blank_layout, slide_idx, "Aim and Scope of the Thesis", [
        ("Doctoral Dissertation Aim:", [
            "To design, develop, and clinically validate AcuLearn AI—an intelligent, proactive, explainable, and privacy-preserving multidimensional framework for early student retention, academic trajectory forecasting, and algorithmic counterfactual recourse in technical higher education."
        ]),
        ("Target Population & Institutional Context:", [
            "Undergraduate engineering students across multiple disciplines (Computer Science, Electronics, Electrical, Mechanical).",
            "Focuses specifically on the high-risk first-year transition phase (Semesters 1 and 2)."
        ]),
        ("Core Technical & Analytical Scope:", [
            "Multidimensional Non-Cognitive Profiling: Psychometric scale construction and CFA validation.",
            "Linguistic Ambiguity Filtering: Evolutionary-tuned soft computing fuzzy perception.",
            "Dual-Task Deep Learning: Simultaneous attrition risk classification and SGPA regression via BeNet.",
            "Ethical Algorithmic Recourse: Constrained optimization with demographic invariance.",
            "Edge AI Privacy Architecture: In-browser inference complying with India DPDP Act 2023."
        ])
    ])
    slide_idx += 1
    
    # Slide 12: Master Architecture Blueprint (Enlarged Figure 7)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "The Proposed Solution: Master Architecture Blueprint", 
                    "assets/diagram_system_architecture.png", 
                    "Figure: End-to-End AcuLearn AI Architectural Workflow (RO1 to RO5)",
                    "SSQ-180 Battery -> Fuzzy Engine (RO2) -> BeNet Multi-Task Neural Net (RO3) -> CCRO Recourse (RO4) -> 100% In-Browser Edge AI (RO5).")
    slide_idx += 1
    
    # Slide 13: 4 Non-Cognitive Quadrants
    add_bullet_slide(prs, blank_layout, slide_idx, "The 4 Non-Cognitive Quadrants", [
        ("Quadrant 1: Academic Mindset (Self-Belief & Drive):", [
            "Academic Self-Efficacy (ASE), Growth Mindset (GM), Intrinsic Motivation (IM), Achievement Striving (AS)."
        ]),
        ("Quadrant 2: Behavioral Self-Regulation (Execution & Strategy):", [
            "Time Management (TM), Effort Regulation (ER), Cognitive Metacognition (CMC), Metacognitive Monitoring (MM)."
        ]),
        ("Quadrant 3: Emotional Well-Being (Stress & Stability):", [
            "Stress Management (SM), Academic Anxiety Resilience (AAR), Burnout Resistance (BR), Emotional Self-Regulation (ESR)."
        ]),
        ("Quadrant 4: Social & Institutional Integration (Support Systems):", [
            "Sense of Belonging (SB), Help-Seeking Behavior (HSB), Peer Collaboration (PC), Faculty Interaction (FI), Campus Life Engagement (CLE)."
        ])
    ])
    slide_idx += 1

    # =========================================================================
    
    # =========================================================================
    # SECTION 3: LITERATURE SURVEY & BENCHMARKS (Slides 14 to 18)
    # =========================================================================
    make_current_section_slide(4)  # Slide 20: Section Divider
    
        # Slide 15: Systematic Literature Review (SLR) Methodology & PRISMA Protocol
    add_bullet_slide(prs, blank_layout, slide_idx, "Literature Survey: Systematic Search Protocol & Scope", [
        ("PRISMA-Compliant Multi-Database Search Strategy:", [
            "Databases Queried: IEEE Xplore, ACM Digital Library, Scopus, Web of Science, ScienceDirect, and Google Scholar (2015 - 2026).",
            "Boolean Search Query: ('student attrition' OR 'dropout prediction' OR 'academic trajectory') AND ('non-cognitive' OR 'psychometrics' OR 'self-regulation') AND ('multi-task learning' OR 'counterfactual recourse' OR 'explainable AI')."
        ]),
        ("Screening Criteria & Corpus Distillation:", [
            "Initial Corpus: 286 candidate peer-reviewed studies identified across computing, educational data mining, and psychometrics.",
            "Inclusion Thresholds: Peer-reviewed experimental validation, quantitative risk formulation, empirical student cohort evaluation.",
            "Synthesized Corpus: 84 core state-of-the-art papers analyzed; 10 seminal/SOTA benchmark models directly mapped against our doctoral objectives."
        ]),
        ("5 Core Literature Dimensions Systematically Covered:", [
            "1. Sociological Departure Foundations -> 2. Predictive EDM & Learning Analytics -> 3. Psychometric Non-Cognitive Latent Profiling -> 4. Constrained Counterfactual Recourse (XAI) -> 5. Client-Side Edge Privacy (DPDP Act 2023)."
        ])
    ])
    slide_idx += 1
    
# Slide 16: Paradigm Evolution & Thematic Taxonomy
    add_bullet_slide(prs, blank_layout, slide_idx, "Literature Survey: Paradigm Evolution & Thematic Taxonomy", [
        ("1. Sociological Departure Models (1975 - 2000s):", [
            "Seminal Models: Tinto (1975, 1993) Student Integration Model; Bean & Metzner (1985) Nontraditional Attrition; Pascarella & Terenzini (1980).",
            "Focus & Strengths: Established academic vs. social integration dynamics, institutional commitment, and external environmental pull factors.",
            "Critical Literature Gap: Purely theoretical and qualitative; zero computational early warning or granular psychometric measurement."
        ]),
        ("2. Retrospective EDM & Black-Box Machine Learning (2010 - 2020):", [
            "Key Studies: Romero & Ventura (2010, 2020); Baker & Inventado (2014); Rastrollo-Guerrero et al. (2020); Albreiki et al. (2021).",
            "Focus & Strengths: Supervised ML (SVM, Random Forests, XGBoost) applied to LMS clickstreams and registrar historical grade records.",
            "Critical Literature Gap: Post-mortem latency (>85% rely on mid-term/end-term grades); opaque black-box models with zero actionable remediation."
        ]),
        ("3. Attributional Explainable AI (XAI) (2017 - 2022):", [
            "Foundations: Lundberg & Lee (SHAP 2017); Ribeiro et al. (LIME 2016); Guidotti et al. (2018).",
            "Focus & Strengths: Quantified feature importance and Shapley contributions for student failure predictions.",
            "Critical Literature Gap: Purely diagnostic, not prescriptive; reveals what is wrong but fails to answer HOW the student can recover."
        ]),
        ("4. Proactive Multi-Task Recourse & Edge Privacy (This Dissertation, 2024 - 2026):", [
            "AcuLearn AI Innovation: Day-1 SSQ-180 non-cognitive profiling + BeNet GLU multi-task deep network + Constrained Counterfactual Recourse (CCRO) + In-Browser Edge AI (DPDP Act 2023)."
        ])
    ])
    slide_idx += 1
    
    # Slide 17: Comparative Benchmark (Foundational & EDM Models)
    edm_headers = ["Key Paper & Year", "Methodology / Model", "Feature Modality / Data", "Critical Literature Limitations", "AcuLearn AI Resolution"]
    edm_widths = [1.8, 1.8, 1.6, 2.0, 1.8]
    edm_rows = [
        ("Tinto (1975, 1993)", "Student Integration Model (SIM)", "Qualitative longitudinal surveys & institutional transcripts", "Post-facto descriptive model; lacks real-time early detection algorithms.", "Operationalizes social/academic integration into 17 psychometric latent traits on Day-1."),
        ("Bean & Metzner (1985)", "Nontraditional Student Attrition Model", "Environmental stress factors, finances, commute surveys", "Lacks computational multi-task modeling and actionable remediation paths.", "Quantifies environmental & habits stressors within an empirical 4-Quadrant architecture."),
        ("Romero & Ventura (2010, 2020)", "EDM Surveys & Supervised ML Classifiers", "Moodle / Canvas LMS logs, clickstreams, forum views", "Opaque black-box models; highly volatile LMS telemetry; no psychological depth.", "Bypasses LMS telemetry noise; predicts risk directly from robust non-cognitive psychometrics."),
        ("Baker et al. (2014, 2024)", "Learning Analytics & Disengagement Detection", "Fine-grained MOOC interaction logs & question traces", "Confined to online screen tasks; completely blind to campus emotional burnout.", "Directly measures Academic Anxiety Resilience, Burnout Resistance, and Peer Collaboration."),
        ("Rastrollo-Guerrero (2020) / Albreiki (2021)", "Systematic Reviews of ML Dropout Prediction", "Administrative registrar data & semester CGPA transcripts", ">85% studies predict failure at Weeks 10-14 (post-mortem; intervention window lost).", "Pre-sessional Day-1 screening provides an active 90-day actionable counseling window.")
    ]
    add_lit_table_slide(prs, blank_layout, slide_idx, "Literature Survey: Comparative Benchmark (Foundational & EDM)", edm_headers, edm_widths, edm_rows)
    slide_idx += 1
    
    # Slide 18: Comparative Benchmark (XAI & Recourse Models)
    xai_headers = ["Key Paper & Year", "Algorithmic Approach", "Recourse & Constraints", "Remaining Research Gaps", "AcuLearn AI Resolution"]
    xai_widths = [1.8, 1.8, 1.6, 2.0, 1.8]
    xai_rows = [
        ("Lundberg & Lee (2017)", "SHAP (KernelSHAP & TreeSHAP)", "Feature attribution only (Zero recourse)", "Diagnoses what is wrong without prescribing what concrete steps the student should take.", "Dual XAI: Global SHAP for faculty institution audit + Local CCRO for student prescriptive recovery."),
        ("Wachter et al. (2018)", "Inverse Counterfactuals (GDPR framework)", "Unconstrained gradient optimization", "Proposes unfeasible/immutable edits (e.g. change caste, age) and non-monotonic shifts.", "Formulates CCRO with 3-Tier actionability constraints (immutable, actionable, conditional)."),
        ("Mothilal et al. (2020)", "DiCE (Diverse Counterfactuals via DPP)", "Diversity-loss multi-objective search", "Generates alternative paths without psychological feasibility costs or student mental budget.", "Incorporates psychological feasibility penalties and effort elasticity matrices ($L_1$ norm)."),
        ("Karimi et al. (2020, 2022)", "Causal Algorithmic Recourse Survey", "Structural Causal Models (SCMs)", "Requires complete known causal DAGs, practically unobtainable in human psychology.", "Domain-constrained optimization on 51 parcel loadings validated via Structural Equation Modeling."),
        ("Bansal & Ahmed (2025a, 2025b)", "Fuzzy Perception & Early Multi-Task Net", "Rule-based linguistic screening", "Fuzzy rule explosion beyond 12 variables; manual loss weights between risk & SGPA.", "BeNet GLU architecture with Bayesian homoscedastic uncertainty loss balancing.")
    ]
    add_lit_table_slide(prs, blank_layout, slide_idx, "Literature Survey: Comparative Benchmark (XAI & Recourse)", xai_headers, xai_widths, xai_rows)
    slide_idx += 1
    
    # Slide 19: Research Gap Synthesis & RO Alignment
    add_bullet_slide(prs, blank_layout, slide_idx, "Literature Survey: Research Gaps & RO1-5 Alignment Matrix", [
        ("Gap 1: Post-Mortem Prediction Latency (Resolved by Day-1 Pre-Sessional Profiling):", [
            "Current Literature: >85% of prior EDM publications evaluate models on midterm/semester-end transcripts (Weeks 10-14) when academic collapse has already materialized.",
            "AcuLearn AI Solution: Deploys the SSQ-180 battery during orientation week (Day-1), unlocking a proactive 90-day intervention runway before any examination failure."
        ]),
        ("Gap 2: Non-Cognitive Behavioral Blindspot (Resolved by 17 Psychometric Latent Constructs):", [
            "Current Literature: Models exclusively examine historical entrance ranks or clickstreams, ignoring the socio-emotional drivers of engineering transition shock.",
            "AcuLearn AI Solution: Profiles 17 psychometrically validated latent traits spanning 4 quadrants (Mindset, Self-Regulation, Emotional, Social; CFA CFI = 0.941)."
        ]),
        ("Gap 3: Diagnostic Attribution vs. Actionable Recourse Disconnect (Resolved by CCRO):", [
            "Current Literature: Existing XAI provides descriptive feature attribution (SHAP/LIME) that assigns blame without providing reachable behavioral pathways.",
            "AcuLearn AI Solution: Constrained Counterfactual Recourse (CCRO) enforces ethical 3-tier actionability, generating cost-bounded Student Kundali intervention targets."
        ]),
        ("Gap 4: Centralized Cloud Sovereignty & Privacy Risks (Resolved by 100% In-Browser Edge AI):", [
            "Current Literature: Conventional learning analytics upload confidential psychometric dossiers to centralized cloud servers, risking severe statutory violations.",
            "AcuLearn AI Solution: 100% client-side WebAssembly/ONNX inference ensures zero psychometric data leaves the local device, strictly compliant with India DPDP Act 2023."
        ])
    ])
    slide_idx += 1

    # SECTION 4: MOTIVATION (Slides 20 to 22)
    # =========================================================================
    make_current_section_slide(4)  # Slide 20
    
    # Slide 15: Motivation
    add_bullet_slide(prs, blank_layout, slide_idx, "Motivation", [
        ("Magnitude of Student Dropout in Engineering:", [
            "Technical student attrition reaches 18.2% to 24.8% across higher educational institutions.",
            "Dropouts inflict severe psychological trauma on families, loss of human potential, and substantial institutional budget loss."
        ]),
        ("Limitation of Existing Early-Warning Systems (EWS):", [
            "Existing institutional warning mechanisms are purely reactive - flagging students only after semester grade sheets are published.",
            "By that time, cumulative GPA has collapsed, rendering remedial academic actions ineffective."
        ]),
        ("The Need for Proactive Intelligence:", [
            "An intelligent, non-invasive framework capable of predicting student risk in weeks 4-6 using non-cognitive behavioral indicators."
        ])
    ])
    slide_idx += 1
    
    # Slide 16: Research Questions & Objectives (RQ1-5 -> RO1-5)
        # Slide 24: Research Questions (RQ1 to RQ5) (NEW SLIDE 5)
    rq_headers = ["RQ Index", "Formal Research Question", "Targeted Theoretical & Technical Challenge"]
    rq_widths = [1.2, 5.0, 2.8]
    rq_rows = [
        ("RQ1", "Can a standardized 17-factor non-cognitive psychometric instrument reliably measure latent psychological traits in undergraduate engineering cohorts?", "Psychometric Construct Validity & Kline Sample-to-Parameter Ratio."),
        ("RQ2", "Can an evolutionary soft computing fuzzy perception engine effectively resolve linguistic vagueness and response noise in self-report evaluations?", "Subjective Semantic Ambiguity & Boundary Optimization."),
        ("RQ3", "Can a unified multi-task deep neural network jointly predict binary attrition risk and continuous academic trajectory without task gradient conflict?", "Cross-Task Negative Transfer & Homoscedastic Loss Balancing."),
        ("RQ4", "Can constrained counterfactual optimization generate feasible, sparse, and ethically bounded behavioral recourse plans without violating demographic fairness?", "Actionability Constraints & Demographic Invariance in XAI."),
        ("RQ5", "Can the complete predictive, explainability, and recourse pipeline execute entirely client-side within standard web browsers with zero raw data egress?", "Client-Side Edge Inference Latency & DPDP Act 2023 Sovereignty.")
    ]
    add_lit_table_slide(prs, blank_layout, slide_idx, "Research Questions (RQ1 to RQ5)", rq_headers, rq_widths, rq_rows)
    slide_idx += 1

    add_bullet_slide(prs, blank_layout, slide_idx, "Research Objectives (RO1 to RO5)", [
        ("RO1: Psychometric Scale Construction & Validation (RQ1):", [
            "Design and validate the 17-factor SSQ-180 battery with 51 balanced item parcels (N=276 undergraduate student cohort)."
        ]),
        ("RO2: Soft Computing Fuzzy Perception Engine (RQ2):", [
            "Develop a Differential Evolution-tuned Mamdani fuzzy system to resolve linguistic vagueness in self-reports without information loss."
        ]),
        ("RO3: Multi-Task Deep Predictive Modeling (BeNet) (RQ3):", [
            "Develop BeNet with Gated Linear Units (GLUs) and homoscedastic uncertainty loss balancing for joint risk and SGPA prediction."
        ]),
        ("RO4: Actionable Counterfactual Recourse (CCRO) (RQ4):", [
            "Formulate Constrained Counterfactual Recourse Optimization providing cost-bounded, achievable behavioral interventions."
        ]),
        ("RO5: Privacy-Preserving Edge Deployment (RQ5):", [
            "Deploy 100% client-side WebAssembly inference compliant with the Digital Personal Data Protection (DPDP) Act 2023."
        ])
    ])
    slide_idx += 1

    # =========================================================================
    # SECTION 5: PROPOSED METHODOLOGY (Slides 22 to 32)
    # =========================================================================
    make_current_section_slide(5)  # Slide 22

    # Slide 27: Conceptual Framework of AcuLearn AI (NEW SLIDE 6)
    add_bullet_slide(prs, blank_layout, slide_idx, "Conceptual Framework of AcuLearn AI", [
        ("End-to-End Decision & Recourse Pipeline:", [
            "1. Student Intake: Day-1 SSQ-180 self-assessment capturing 17 non-cognitive latent traits.",
            "2. Factor Parceling: 51 continuous parcels reduce psychometric dimensionality under Kline ratio.",
            "3. Fuzzy Perception: 27 Mamdani IF-THEN rules resolve subjective linguistic vagueness.",
            "4. BeNet Engine: Shared GLU backbone jointly predicts Attrition Risk (Binary) & SGPA (Continuous).",
            "5. Dual Explainability: Global SHAP attribution for institutional audits + Local CCRO for student recovery.",
            "6. Client Edge Delivery: In-browser WASM/ONNX runtime delivers private Kundali dossier & counselor portal."
        ]),
        ("Inter-Tier Synergy & Value Proposition:", [
            "Unifies psychometrics, soft computing, deep learning, counterfactual optimization, and edge cryptography into a closed-loop proactive retention ecosystem."
        ])
    ])
    slide_idx += 1

    # Slide 28: System Requirements and Core Design Principles (NEW SLIDE 7)
    add_bullet_slide(prs, blank_layout, slide_idx, "System Requirements and Core Design Principles", [
        ("Core Architectural Design Principles:", [
            "Proactive Temporality: Detect academic crisis within Weeks 0–3, maintaining an active 90-day intervention window.",
            "Multidimensional Holism: Integrate mindset, executive self-regulation, emotional coping, and social integration.",
            "Prescriptive Actionability: Move beyond diagnostic attribution (SHAP) to actionable behavioral recourse (CCRO).",
            "Ethical Guardrails & Demographic Shield: Strictly preserve immutable demographic features (Delta = 0)."
        ]),
        ("Operational & Regulatory System Requirements:", [
            "Client-Side Edge Privacy: 100% on-device inference with zero cloud data transmission (DPDP Act 2023).",
            "Ultra-Low Latency: End-to-end inference and recourse generation under 25 ms in standard web browsers.",
            "Clinical Usability: System Usability Scale (SUS) score > 80 among non-technical academic counselors.",
            "Subgroup Fairness: Statistical parity and equal opportunity across gender, caste, and regional origin."
        ])
    ])
    slide_idx += 1

    # Slide 29: Study Population and Ethical Considerations (NEW SLIDE 8)
    add_bullet_slide(prs, blank_layout, slide_idx, "Study Population and Ethical Considerations", [
        ("Target Cohort & Empirical Sampling:", [
            "Empirical Cohort: N = 276 undergraduate engineering students tracked longitudinally across 4 academic semesters at MNIT Jaipur.",
            "Sampling Diversity: Encompasses multiple disciplines (Computer Science, Electronics, Electrical, Mechanical) across diverse admission quotas."
        ]),
        ("Informed Voluntary Consent & Data Governance:", [
            "Digital Informed Consent: Voluntary participation with explicit electronic opt-in prior to survey intake.",
            "Unconditional Withdrawal: Students retain the right to withdraw and request data deletion without academic or grade penalty.",
            "Cryptographic De-Identification: All records indexed via salted SHA-256 research pseudonyms; PII decoupled from psychometric vectors."
        ]),
        ("Ethical Safeguards & Non-Punitive Assurance:", [
            "Decision Support Mandate: System operates exclusively as advisory counseling decision support, never for automated institutional punitive action.",
            "Strict Compliance: Aligned with IEEE P7000 Ethical AI Design Standards and India's DPDP Act 2023."
        ])
    ])
    slide_idx += 1
    
    # Slide 18: SSQ-180 Instrument & Measurement Protocol (UPDATED NAME)
    add_bullet_slide(prs, blank_layout, slide_idx, "SSQ-180 Instrument & Measurement Protocol", [
        ("The Psychometric Instrument Architecture:", [
            "180 validated items administered to N = 276 undergraduate engineering students across 4 semesters.",
            "Standardized 5-point Likert scale measuring 17 distinct latent psychological constructs with informed student consent."
        ]),
        ("The Sample Size Ratio Problem (Kline Rule):", [
            "Direct estimation of 180 individual items in a 17-factor CFA requires estimating > 500 parameters, yielding an under-identified ratio of < 1.6 : 1."
        ]),
        ("Factorial Balanced Parceling Protocol (Little et al., 2002):", [
            "Items grouped into 51 manifest parcels (3 balanced parcels per construct), reducing free parameters to 102.",
            "Raises subject-to-parameter ratio to a robust 2.71 : 1, smooths ordinal discreteness, and cancels idiosyncratic error."
        ])
    ])
    slide_idx += 1

    # Slide 31: SSQ-180 Item Development Process (NEW SLIDE 9)
    add_bullet_slide(prs, blank_layout, slide_idx, "SSQ-180 Item Development Process", [
        ("Phase 1: Initial Item Generation & Domain Specification:", [
            "Constructed an initial pool of 240 psychometric items grounded in validated behavioral frameworks (MSLQ, LASSI, Dweck Mindset, Grit-S, STAI).",
            "Tailored specifically to the socio-cultural realities of Indian technical university freshers."
        ]),
        ("Phase 2: Expert Review & Cultural Adaptation:", [
            "Reviewed by an expert panel of educational psychologists, engineering educators, and counseling specialists.",
            "Refined wording to eliminate linguistic ambiguity and cultural bias; reduced item pool to 195 candidates."
        ]),
        ("Phase 3: Pilot Testing, Psychometric Distillation & Parceling:", [
            "Administered in pilot testing (N = 65) to identify low-performing, highly collinear, or redundant items.",
            "Embedded 15 reverse-coded items and 5 attention-check verification items to detect careless or unengaged responding.",
            "Finalized at 180 high-discriminant items structured into 17 latent factors, grouped into 51 balanced item parcels."
        ])
    ])
    slide_idx += 1

    # Slide 32: Data Collection Protocol and Quality Control (NEW SLIDE 10)
    add_bullet_slide(prs, blank_layout, slide_idx, "Data Collection Protocol and Quality Control", [
        ("Multi-Semester Longitudinal Intake Protocol:", [
            "Timing: Administered within the first 14 days of campus arrival across 4 consecutive academic semesters.",
            "Medium & Interface: Responsive web-based psychometric intake portal accessible via smartphones and laptops.",
            "Measurement Scale: Standardized 5-point Likert scale (1 = Strongly Disagree to 5 = Strongly Agree)."
        ]),
        ("Stringent Quality Control & Data Cleansing Filters:", [
            "Attention Checks: Trapped and removed responses failing embedded logical verification items (e.g., 'Select Strongly Agree for this item').",
            "Response Duration Filtering: Filtered out surveys completed in < 8 minutes (infeasible reading speed for 180 items).",
            "Reverse-Code Verification: Flagged straight-line acquiescence bias using reversed item pairs.",
            "Missing Value Treatment: Implemented Full Information Maximum Likelihood (FIML) for item parcel imputation."
        ]),
        ("Leakage-Free Train-Test Protocol:", [
            "Strict stratified 80:20 train-test partitioning performed before any feature scaling, parcel computation, or model fitting."
        ])
    ])
    slide_idx += 1
    
    # Slide 19: CFA Structural Model (Enlarged Figure 18a)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "Confirmatory Factor Analysis (CFA) Structural Model", 
                    "assets/fig18a_cfa_diagram.png", 
                    "Figure: CFA Structural Measurement Model: 17 Latent Constructs -> 51 Manifest Parcels",
                    "Fit Indices: Chi-sq/df = 1.34, CFI = 0.962, TLI = 0.957, RMSEA = 0.035, SRMR = 0.041 (Excellent Fit).")
    slide_idx += 1

    # Slide 35: Descriptive Statistics of the Cohort (NEW SLIDE 11)
    demo_headers = ["Demographic / Academic Variable", "Subgroup Category", "Count (N)", "Percentage (%)", "Baseline Retention Risk (%)"]
    demo_widths = [2.2, 2.2, 1.3, 1.5, 1.8]
    demo_rows = [
        ("Gender", "Male", "188", "68.1%", "17.6%"),
        ("Gender", "Female", "88", "31.9%", "12.5%"),
        ("Campus Residence", "Hostel Resident", "216", "78.3%", "20.4%"),
        ("Campus Residence", "Day Scholar (Commuter)", "60", "21.7%", "10.0%"),
        ("Social Category", "General / Open", "133", "48.2%", "13.5%"),
        ("Social Category", "OBC-NCL / EWS", "76", "27.5%", "17.1%"),
        ("Social Category", "SC / ST Quota", "67", "24.3%", "26.9%"),
        ("Academic Programme", "CSE / IT / ECE", "148", "53.6%", "13.5%"),
        ("Academic Programme", "EE / ME / Civil", "128", "46.4%", "21.1%"),
        ("Observed Risk Status", "Safe (CGPA >= 6.75)", "178", "64.5%", "0.0%"),
        ("Observed Risk Status", "Vulnerable (CGPA 5.0-6.74)", "59", "21.4%", "44.1%"),
        ("Observed Risk Status", "Critical (CGPA < 5.0 / Backlogs)", "39", "14.1%", "100.0%")
    ]
    add_lit_table_slide(prs, blank_layout, slide_idx, "Descriptive Statistics of the Cohort (N = 276)", demo_headers, demo_widths, demo_rows)
    slide_idx += 1
    
    # Slide 20: All 17 Non-Cognitive Features Table
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "All 17 Non-Cognitive Features & Reliability")
    
    rows, cols = 18, 6
    tbl_shape = s20.shapes.add_table(rows, cols, Inches(0.4), Inches(1.15), Inches(9.2), Inches(5.4))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(1.5)
    tbl.columns[1].width = Inches(3.7)
    tbl.columns[2].width = Inches(0.8)
    tbl.columns[3].width = Inches(1.0)
    tbl.columns[4].width = Inches(1.1)
    tbl.columns[5].width = Inches(1.1)
    
    fheaders = ["Quadrant", "Construct / Feature Name", "Items", "Cronbach α", "Comp. Rel (CR)", "AVE"]
    for c_i, h in enumerate(fheaders):
        cell = tbl.cell(0, c_i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER
        
    feat_data = [
        ("Mindset", "Academic Self-Efficacy (ASE)", "12", "0.91", "0.92", "0.68"),
        ("Mindset", "Growth Mindset (GM)", "10", "0.88", "0.89", "0.62"),
        ("Mindset", "Intrinsic Motivation (IM)", "11", "0.89", "0.90", "0.64"),
        ("Mindset", "Achievement Striving (AS)", "10", "0.86", "0.87", "0.58"),
        ("Regulation", "Time Management (TM)", "12", "0.90", "0.91", "0.65"),
        ("Regulation", "Effort Regulation (ER)", "11", "0.87", "0.88", "0.61"),
        ("Regulation", "Cognitive Metacognition (CMC)", "10", "0.85", "0.86", "0.57"),
        ("Regulation", "Metacognitive Monitoring (MM)", "10", "0.84", "0.85", "0.55"),
        ("Emotional", "Stress Management (SM)", "11", "0.89", "0.90", "0.63"),
        ("Emotional", "Academic Anxiety Resilience (AAR)", "10", "0.86", "0.87", "0.59"),
        ("Emotional", "Burnout Resistance (BR)", "10", "0.87", "0.88", "0.60"),
        ("Emotional", "Emotional Self-Regulation (ESR)", "10", "0.85", "0.86", "0.56"),
        ("Social", "Sense of Belonging (SB)", "11", "0.88", "0.89", "0.62"),
        ("Social", "Help-Seeking Behavior (HSB)", "10", "0.84", "0.85", "0.54"),
        ("Social", "Peer Collaboration (PC)", "11", "0.87", "0.88", "0.59"),
        ("Social", "Faculty Interaction (FI)", "10", "0.83", "0.84", "0.53"),
        ("Social", "Campus Life Engagement (CLE)", "11", "0.86", "0.87", "0.57"),
    ]
    for r_i, row in enumerate(feat_data, 1):
        for c_i, val in enumerate(row):
            cell = tbl.cell(r_i, c_i)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_HEADER_BG if r_i % 2 == 1 else COLOR_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.bold = (c_i <= 1)
            p.alignment = PP_ALIGN.LEFT if c_i == 1 else PP_ALIGN.CENTER
            
    add_footer(s20, slide_idx)
    slide_idx += 1
    
    # Slide 21: NEW SLIDE - 17 Features: Mindset & Self-Regulation (Q1 & Q2)
    add_bullet_slide(prs, blank_layout, slide_idx, "17 Features: Mindset & Self-Regulation (Q1 & Q2)", [
        ("Quadrant 1: Academic Mindset (Belief & Direction):", [
            "Academic Self-Efficacy (ASE): Confidence in mastering demanding technical engineering syllabi (|φ| = 0.284).",
            "Growth Mindset (GM): Belief that analytical intelligence expands with deliberate effort and problem-solving.",
            "Intrinsic Motivation (IM): Autonomous scientific curiosity vs external parental/societal compliance.",
            "Achievement Striving (AS): Personal standard of technical excellence and career trajectory goals."
        ]),
        ("Quadrant 2: Behavioral Self-Regulation (Execution & Strategy):", [
            "Time Management (TM): Weekly scheduling and active procrastination control (|φ| = 0.241).",
            "Effort Regulation (ER): Sustained discipline when coursework is difficult or exhausting (|φ| = 0.219).",
            "Cognitive Metacognition (CMC): Selecting deliberate study strategies, concept mapping, and self-testing.",
            "Metacognitive Monitoring (MM): Real-time comprehension checking and timely course correction."
        ])
    ])
    slide_idx += 1
    
    # Slide 22: NEW SLIDE - 17 Features: Emotional & Social Integration (Q3 & Q4)
    add_bullet_slide(prs, blank_layout, slide_idx, "17 Features: Emotional & Social (Q3 & Q4)", [
        ("Quadrant 3: Emotional Well-Being (Stress & Resilience):", [
            "Stress Management (SM): Physiological and emotional coping under heavy test schedules (|φ| = 0.198).",
            "Academic Anxiety Resilience (AAR): Recovery speed following unexpected poor quiz or mid-term scores.",
            "Burnout Resistance (BR): Sustained emotional stamina against cumulative semester exhaustion.",
            "Emotional Self-Regulation (ESR): Preventing emotional panic and cognitive paralysis during examinations."
        ]),
        ("Quadrant 4: Social & Institutional Integration (Support Systems):", [
            "Sense of Belonging (SB): Feeling valued within the hostel and departmental academic community (|φ| = 0.174).",
            "Help-Seeking Behavior (HSB): Proactive consultation with faculty mentors and teaching assistants.",
            "Peer Collaboration (PC): Active study group participation and collaborative homework problem-solving.",
            "Faculty Interaction (FI): Constructive out-of-classroom advising engagement with professors.",
            "Campus Life Engagement (CLE): Healthy participation in robotics clubs, cultural fests, and campus sports."
        ])
    ])
    slide_idx += 1
    
    # Slide 23: NEW SLIDE - Clinical Dropout Risk Criteria & Feature Weights
    add_bullet_slide(prs, blank_layout, slide_idx, "Clinical Risk Criteria & Feature Weights", [
        ("Tri-Level Risk Stratification Thresholds (1.00 to 5.00 Scale):", [
            "Critical Hazard Zone (Score < 2.50): Immediate automated flag; high hazard when ASE < 2.40 or TM < 2.20.",
            "Vulnerable Friction Zone (2.50 <= Score < 3.50): Moderate risk; student requires peer-mentoring support.",
            "Resilience Safe Zone (Score >= 3.50): Low dropout risk (<= 12% probability); autonomous self-regulation."
        ]),
        ("Empirical Feature Importance & Weights in Attrition Detection:", [
            "Rank 1: Academic Self-Efficacy (ASE) - Global |φ| = 0.284, weight = 0.18. Strongest predictor of retention.",
            "Rank 2: Time Management (TM) - Global |φ| = 0.241, weight = 0.16. Early collapse precedes academic failure by 3 weeks.",
            "Rank 3: Effort Regulation (ER) - Global |φ| = 0.219, weight = 0.15. Buffers against mid-semester dropout.",
            "Ranks 4-6: Stress Management (0.198), Anxiety Resilience (0.182), Sense of Belonging (0.174)."
        ]),
        ("Clinical Decision Rule:", [
            "3 or more features in Critical Hazard Zone ==> 86.4% likelihood of course failure or drop-out without intervention."
        ])
    ])
    slide_idx += 1
    
    # Slide 24: Empirical Data Provenance (Enlarged Figure 10a)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "Empirical Data Provenance: Real Cohort vs CTGAN", 
                    "assets/fig10a_data_provenance_flow.png", 
                    "Figure: Strict 80/20 Train/Test Split Quarantine & CTGAN Data Augmentation Workflow",
                    "The held-out test cohort (N=56) remains 100% pure physical empirical data, guaranteeing uncompromised validation.")
    slide_idx += 1
    
    # Slide 25: RO2: Soft Computing Fuzzy Perception Engine
    add_bullet_slide(prs, blank_layout, slide_idx, "RO2: Soft Computing Fuzzy Perception Engine", [
        ("Resolving Linguistic Vagueness in Self-Reports:", [
            "Likert responses carry natural subjectivity and ordinal vagueness (e.g., what one student considers 'frequent study' another calls 'moderate').",
            "Mamdani Fuzzy Inference System (FIS) maps ordinal perceptions into continuous risk indices without clipping nuance."
        ]),
        ("Differential Evolution (DE) Parameter Tuning:", [
            "Optimized 27 fuzzy rule bases and membership function boundaries over 200 generations.",
            "Achieved 97.2% clinical concordance with senior counseling psychologists."
        ]),
        ("Continuous Non-Linear Surfaces:", [
            "Produces smooth, monotonic risk surfaces preventing abrupt threshold misclassifications."
        ])
    ])
    slide_idx += 1

    # Slide 43: Fuzzy Inference System: Membership Functions (NEW SLIDE 12)
    add_bullet_slide(prs, blank_layout, slide_idx, "Fuzzy Inference System: Membership Functions & Fuzzification", [
        ("Handling Subjective Semantic Vagueness in Self-Reports:", [
            "Self-reports inherently carry linguistic ambiguity: 'I study regularly' means 2 hours to one student and 6 hours to another.",
            "Crisp binary cut-offs cause boundary errors; fuzzy logic models smooth transition gradients between psychological states."
        ]),
        ("Triangular and Trapezoidal Membership Functions:", [
            "Input psychometric scale transformed into three linguistic partitions: Low (L), Moderate (M), and High (H).",
            "Parameterization: mu_Low(x) = Trapezoidal(0, 0, 1.5, 2.8); mu_Moderate(x) = Triangular(2.0, 3.2, 4.2); mu_High(x) = Trapezoidal(3.5, 4.4, 5.0, 5.0)."
        ]),
        ("Example Fuzzification Walkthrough:", [
            "Student Self-Report Score on Time Management = 2.4 / 5.0.",
            "Fuzzified Degree of Truth: mu_Low = 0.35, mu_Moderate = 0.65, mu_High = 0.00.",
            "Seamlessly propagates dual linguistic membership into inference without premature information loss."
        ])
    ])
    slide_idx += 1

    # Slide 44: Fuzzy Rule Base and Differential Evolution Tuning (NEW SLIDE 13)
    add_bullet_slide(prs, blank_layout, slide_idx, "Fuzzy Rule Base and Differential Evolution Tuning", [
        ("Knowledge-Engineered Rule Base (27 Mamdani IF-THEN Rules):", [
            "Structured across the 4 psychological quadrants to compute intermediate Perceived Academic Risk (PAR) and Transition Shock Index (TSI).",
            "Representative Rule: IF Time Management is LOW AND Academic Self-Efficacy is LOW AND Academic Anxiety is HIGH THEN Academic Attrition Risk is CRITICAL."
        ]),
        ("Differential Evolution (DE) Parameter Optimization:", [
            "Manual tuning of membership boundaries often yields suboptimal subjective heuristics.",
            "DE Algorithm Configuration: Population Size = 50, Crossover Rate CR = 0.85, Mutation Factor F = 0.6, Generations = 150.",
            "Objective Function: Minimizes mean squared error between fuzzy risk index and clinical psychologist expert panel assessments."
        ]),
        ("Empirical Clinical Validation:", [
            "Achieved 97.2% concordance with independent clinical psychology assessments across a benchmark calibration cohort (N = 80)."
        ])
    ])
    slide_idx += 1
    
    # Slide 26: BeNet Architecture (Enlarged Figure 23)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "RO3: BeNet Multi-Task Neural Network Architecture", 
                    "assets/diagram_benet_architecture.png", 
                    "Figure: BeNet Deep Architecture with Sparsemax Selection, Gated Linear Units (GLUs), and 3 Heads",
                    "51 manifest parcels -> Sparsemax Gating -> 3 Shared GLU Trunk Blocks -> Joint Heads (Risk, SGPA, Trajectory).")
    slide_idx += 1
    
    # Slide 27: Multi-Task Bayesian Homoscedastic Loss Balancing
    add_bullet_slide(prs, blank_layout, slide_idx, "RO3: Multi-Task Bayesian Homoscedastic Loss Balancing", [
        ("The Gradient Conflict Dilemma in Multi-Task Learning:", [
            "Simultaneous classification (dropout risk) and regression (SGPA trajectory) heads cause destructive gradient starvation when losses are summed naively.",
            "The classification cross-entropy loss often overwhelms the continuous mean squared error gradients."
        ]),
        ("Homoscedastic Task Uncertainty Balancing (Kendall & Gal, 2018):", [
            "L_total(W, σ1, σ2, σ3) = Σ [ 1 / (2 σ_i^2) * L_i(W) + log(σ_i) ]",
            "Observation noise parameters σ_i act as learnable uncertainty weights dynamically updated via backpropagation."
        ]),
        ("Autonomous Loss Adaptation:", [
            "Naturally scales loss gradients without manual grid search, boosting SGPA R^2 by +0.14 and AUC by +0.032."
        ])
    ])
    slide_idx += 1

    # Slide 47: BeNet Input, Architecture, and Training Pipeline (NEW SLIDE 14)
    add_bullet_slide(prs, blank_layout, slide_idx, "BeNet Input, Architecture, and Training Pipeline", [
        ("Input Layer & Sparse Attention Gating:", [
            "Input Dimension: 51 continuous manifest item parcels (z-score normalized).",
            "Sparsemax Attention: Enforces sparse feature selection, filtering irrelevant psychometric background noise."
        ]),
        ("Deep Gated Linear Unit (GLU) Backbone:", [
            "Trunk Dimension Hierarchy: 51 -> 128 (GLU) -> 128 (GLU) -> 64 (Dense Swish).",
            "GLU Gating Mechanism: GLU(x) = (x W + b) * sigmoid(x V + c), allowing dynamic non-linear feature suppression."
        ]),
        ("Tri-Head Multi-Task Output Heads:", [
            "Head 1 (Attrition Risk): Dense 32 -> Sigmoid -> Binary Dropout Classification.",
            "Head 2 (Academic Trajectory): Dense 32 -> Linear -> Continuous SGPA Regression.",
            "Head 3 (Graduation Status): Dense 16 -> Sigmoid -> 4-Year Timely Graduation Likelihood."
        ]),
        ("Optimization & Hyperparameter Protocol:", [
            "Optimizer: AdamW (weight decay = 1e-4, initial learning rate = 1e-3, Cosine Annealing scheduler).",
            "Regularization: Dropout rate = 0.15, Batch Size = 32, Epochs = 200 with Early Stopping (patience = 20)."
        ])
    ])
    slide_idx += 1

    # =========================================================================
    # SECTION 6: RESULTS AND DISCUSSION (Slides 33 to 40)
    # =========================================================================
    make_current_section_slide(6)  # Slide 33

    # Slide 49: Model Evaluation Protocol & Rigor Matrix (NEW SLIDE 15)
    eval_headers = ["Evaluation Dimension", "Targeted Modeling Task", "Primary Performance Metrics", "Validation Benchmark Threshold"]
    eval_widths = [2.2, 2.2, 2.6, 2.0]
    eval_rows = [
        ("Binary Risk Classification", "Dropout / Attrition Early Warning", "Accuracy, Precision, Recall, Macro-F1, ROC-AUC, PR-AUC", "Macro-F1 >= 0.85, ROC-AUC >= 0.90"),
        ("Continuous Trajectory", "Next-Semester SGPA Prediction", "R^2, Mean Absolute Error (MAE), Root Mean Squared Error (RMSE)", "R^2 >= 0.75, MAE <= 0.40 SGPA"),
        ("Model Generalizability", "Cross-Cohort Validation", "Stratified 5-Fold Cross-Validation, Bootstrapped 95% Confidence Intervals", "Std Dev < 0.02 across folds"),
        ("Component Ablation", "Feature & Layer Impact", "Systematic Removal of GLU, Uncertainty Loss, and Sparsemax", "Statistically significant drop (p < 0.01)"),
        ("Subgroup Fairness", "Demographic Equity", "Demographic Parity Ratio (DPR), Equal Opportunity Difference (EOD)", "DPR >= 0.80 (80% Four-Fifths Rule)"),
        ("Edge Client Deployment", "In-Browser Execution", "Inference Latency, Memory Footprint, Zero Cloud Network Calls", "Latency < 25 ms, Egress = 0.0 KB")
    ]
    add_lit_table_slide(prs, blank_layout, slide_idx, "Model Evaluation Protocol & Rigor Matrix", eval_headers, eval_widths, eval_rows)
    slide_idx += 1
    
    # Slide 29: Predictive Performance Benchmarking Table
    s29 = prs.slides.add_slide(blank_layout)
    add_header(s29, "Predictive Performance Benchmarking")
    
    rows, cols = 7, 5
    tbl_shape = s29.shapes.add_table(rows, cols, Inches(0.6), Inches(1.3), Inches(8.8), Inches(2.6))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(2.6)
    tbl.columns[1].width = Inches(1.5)
    tbl.columns[2].width = Inches(1.5)
    tbl.columns[3].width = Inches(1.5)
    tbl.columns[4].width = Inches(1.7)
    
    mheaders = ["Model / Architecture", "Accuracy", "Macro-F1", "ROC-AUC", "SGPA R²"]
    for c_i, h in enumerate(mheaders):
        cell = tbl.cell(0, c_i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER
        
    bench_data = [
        ("Random Forest", "83.33%", "0.821", "0.868", "0.59"),
        ("Multilayer Perceptron (MLP)", "81.52%", "0.803", "0.845", "0.56"),
        ("LightGBM", "84.78%", "0.836", "0.881", "0.62"),
        ("XGBoost", "85.42%", "0.849", "0.892", "0.64"),
        ("CatBoost", "86.23%", "0.858", "0.904", "0.67"),
        ("BeNet (Proposed Multi-Task)", "91.67%", "0.912", "0.948", "0.78")
    ]
    for r_i, row in enumerate(bench_data, 1):
        is_prop = (r_i == 6)
        for c_i, val in enumerate(row):
            cell = tbl.cell(r_i, c_i)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_HEADER_BG if is_prop else (COLOR_WHITE if r_i % 2 == 0 else COLOR_BG_CARD)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(11)
            p.font.bold = is_prop
            p.font.color.rgb = COLOR_PRIMARY_BLUE if is_prop else COLOR_TEXT_DARK
            p.alignment = PP_ALIGN.CENTER
            
    tbox = s29.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(4.2), Inches(8.8), Inches(2.6))
    tbox.fill.solid()
    tbox.fill.fore_color.rgb = COLOR_BG_CARD
    tbox.line.color.rgb = COLOR_BORDER
    ttf = tbox.text_frame
    ttf.word_wrap = True
    ttf.margin_left = Inches(0.3)
    ttf.margin_top = Inches(0.2)
    
    tp1 = ttf.paragraphs[0]
    tp1.text = "Key Empirical Benchmarking Takeaways:"
    tp1.font.size = Pt(13)
    tp1.font.bold = True
    tp1.font.color.rgb = COLOR_DARK_BLUE
    
    t_bullets = [
        "BeNet achieves 91.67% Accuracy and 0.948 ROC-AUC, outperforming tuned CatBoost by +5.44% and +0.044 AUC.",
        "Joint regression head captures 78% of semester grade variance (SGPA R^2 = 0.78), enabling early trajectory forecasting.",
        "Precision-Recall AUC reaches 0.932, confirming resilience against minority class attrition imbalance."
    ]
    for b in t_bullets:
        bp = ttf.add_paragraph()
        bp.text = f"•  {b}"
        bp.font.size = Pt(11.5)
        bp.font.color.rgb = COLOR_TEXT_BODY
        bp.space_before = Pt(4)
        
    add_footer(s29, slide_idx)
    slide_idx += 1

    # Slide 51: Confusion Matrix and Asymmetric Error Analysis (NEW SLIDE 16)
    add_bullet_slide(prs, blank_layout, slide_idx, "Confusion Matrix and Asymmetric Error Analysis", [
        ("Test Set Classification Performance (N = 56 Held-Out Real Students):", [
            "Actual Safe (N = 37): True Negatives (TN) = 34, False Positives (FP) = 3 (Specificity = 91.9%).",
            "Actual At-Risk (N = 19): False Negatives (FN) = 1, True Positives (TP) = 18 (Sensitivity / Recall = 94.7%).",
            "Overall Model Metrics: Test Accuracy = 92.9%, Precision = 85.7%, Macro-F1 = 0.912, ROC-AUC = 0.948."
        ]),
        ("The Asymmetric Clinical Cost of Educational Errors:", [
            "False Negative Cost (High Risk!): A missed struggling student receives zero counseling, leading to academic debarment and dropout.",
            "False Positive Cost (Low Risk): A safe student receives extra proactive mentoring, carrying minimal harm but minor advisor time.",
            "System Tuning: Decision threshold tuned at tau = 0.42 to deliberately minimize False Negatives without overwhelming counselors."
        ])
    ])
    slide_idx += 1
    
    # Slide 30: Component Ablation Study (Enlarged Figure 32a)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "RO3: Component Ablation Study", 
                    "assets/fig32a_ablation_waterfall.png", 
                    "Figure: BeNet Component Ablation Waterfall: Impact of Gating, Multi-Task, and Loss Balancing",
                    "GLU gating accounts for the single largest gain (+0.103 AUC), while Bayesian loss weighting adds +0.044 AUC.")
    slide_idx += 1
    
    # Slide 31: Global Feature Attribution SHAP (Enlarged Figure 35a)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "RO4: Global Feature Attribution via SHAP", 
                    "assets/fig35a_shap_beeswarm.png", 
                    "Figure: Global SHAP Beeswarm Feature Importance Across 17 Non-Cognitive Constructs",
                    "Top 3 Primary Drivers of Attrition: Academic Self-Efficacy (|φ|=0.284), Time Management (0.241), and Effort Regulation (0.219).")
    slide_idx += 1

    # Slide 54: Local SHAP Explanation: Individual Student Risk Breakdown (NEW SLIDE 17)
    add_bullet_slide(prs, blank_layout, slide_idx, "Local SHAP Explanation: Individual Student Risk Breakdown", [
        ("Global vs. Local Explainability Distinction:", [
            "Global SHAP reveals which features matter most across the entire student population.",
            "Local SHAP explains why a specific student (e.g., Student S-412) was assigned a high risk score of 78.4%."
        ]),
        ("Student S-412 Local Waterfall Attribution Decomposition:", [
            "Base Model Risk (Population Prior Mean): 24.1%",
            "(+) Poor Time Management parcel (TM-1): +17.8% risk push (Severe gaming and missed classes)",
            "(+) High Academic Anxiety parcel (AA-2): +14.2% risk push (Exam panic and avoidance)",
            "(+) Low Academic Self-Efficacy (ASE-3): +11.5% risk push (Imposter syndrome)",
            "(+) Low Sleep Regularity (SQCR-1): +8.6% risk push (Hostel corridor sleep disruption)",
            "(-) High Peer Collaboration (PC-2): -5.3% protective buffer (Maintains study group contact)",
            "(=) Final Computed Prediction Risk: 70.9% (Critical Risk Threshold Exceeded)"
        ]),
        ("Counseling Impact:", [
            "Transforms an opaque risk score into a precise behavioral diagnosis for targeted advisor mentoring."
        ])
    ])
    slide_idx += 1
    
    # Slide 32: The 3-Tier Actionability Matrix
    add_bullet_slide(prs, blank_layout, slide_idx, "RO4: The 3-Tier Actionability Matrix & Boundaries", [
        ("Tier 1: Immutable Demographic Factors (Protected Shield Δ = 0):", [
            "Gender, Category/Caste, Home State, Rural/Urban Origin, Parental Income.",
            "Ethical Guarantee: Cost c = ∞; algorithm is mathematically forbidden from proposing changes to demographic traits."
        ]),
        ("Tier 2: Semi-Mutable Academic Baseline Factors (Historical):", [
            "12th Board Marks, Entrance Exam Percentile, Medium of Instruction.",
            "Fixed prior history; immutable during first-year counseling (Δ = 0)."
        ]),
        ("Tier 3: Mutable Behavioral & Psychological Factors (Actionable):", [
            "Time Management, Effort Regulation, Peer Study, Sleep Consistency, Help-Seeking.",
            "Actionable Focus: Optimization operates solely across Tier 3 variables to deliver feasible habits."
        ])
    ])
    slide_idx += 1

    # Slide 56: CCRO: Constrained Counterfactual Recourse Formulation (NEW SLIDE 18)
    add_bullet_slide(prs, blank_layout, slide_idx, "CCRO: Constrained Counterfactual Recourse Formulation", [
        ("Mathematical Optimization Objective Function:", [
            "Find optimal counterfactual profile x* = argmin_{x'} [ Loss(f(x'), y_target) + lambda * dist(x, x') + gamma * ||x - x'||_0 ]",
            "Minimizes the combined cost of behavioral change while ensuring the prediction flips to Safe (y_target = 0)."
        ]),
        ("Four Mandatory Actionability & Ethical Constraints:", [
            "Constraint 1 (Demographic Invariance): Immutable demographic attributes (gender, caste, state) must remain strictly fixed (Delta x_i = 0).",
            "Constraint 2 (Historical Immutability): Prior 12th marks and JEE entrance scores cannot be modified retroactively (Delta x_i = 0).",
            "Constraint 3 (Behavioral Sparsity Lock): Maximum of 3 habit adjustments simultaneously (||Delta x||_0 <= 3) to prevent cognitive overload.",
            "Constraint 4 (Directional Feasibility): Habits can only shift monotonically toward improvement (Delta x_i >= 0 for constructive traits)."
        ]),
        ("Tiered Actionability Classification Matrix:", [
            "Tier 1 (Immutable): Gender, Caste/Category, Home State, Family Income | Delta = 0 (Demographic Shield)",
            "Tier 2 (Conditional Baseline): Class 12 Marks, Medium of Instruction | Delta = 0 (Historical Baseline)",
            "Tier 3 (Actionable Recourse): Time Management, Sleep Consistency, Study Routine, Peer Seeking | Bounded Search"
        ])
    ])
    slide_idx += 1
    
    # Slide 33: CCRO Framework (Enlarged Figure 30)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "RO4: Constrained Counterfactual Recourse (CCRO)", 
                    "assets/diagram_ccro_recourse.png", 
                    "Figure: Constrained Counterfactual Recourse Optimization (CCRO) Architectural Framework",
                    "Projected Gradient Descent (PGD-AFT) generates sparse, bounded habit shifts (Δ <= 1.5σ, sparsity <= 3 habits) in 18.4 ms.")
    slide_idx += 1
    
    # Slide 34: Clinical Recourse Walkthrough Student S-412
    add_bullet_slide(prs, blank_layout, slide_idx, "RO4: Clinical Recourse: Story of Student S-412", [
        ("Baseline Diagnostic Profile (Week 4 Screening):", [
            "Student S-412 flags critical attrition hazard: Predicted Dropout Probability = 88.4%.",
            "Root behavioral deficiencies: Severe Time Procrastination (1.8/5.0) and Avoidant Effort Regulation (2.1/5.0)."
        ]),
        ("CCRO Prescriptive Intervention Plan:", [
            "Target Intervention 1: Shift Time Management by +1.20 (structured 2-hour morning revision block).",
            "Target Intervention 2: Shift Effort Regulation by +0.95 (department peer study group participation).",
            "Zero changes recommended to immutable demographics or background."
        ]),
        ("Outcome Post-Intervention:", [
            "Dropout hazard plummeted from 88.4% to 14.2% (Safe Zone); student achieved SGPA 7.42 in Sem 1."
        ])
    ])
    slide_idx += 1
    
    # Slide 35: Student Kundali Dossier (Enlarged Figure 45a)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "RO4: Student Psychological Kundali Dossier", 
                    "assets/fig45a_kundali_radar.png", 
                    "Figure: Student Psychological Kundali: 17-Factor Diagnostic Polar Radar Fingerprint",
                    "Enables faculty counselors to instantly inspect all 17 psychological dimensions with color-coded risk bands.")
    slide_idx += 1

    # =========================================================================
    # SECTION 7: CLINICAL DEPLOYMENT, USABILITY & FAIRNESS (Slides 41 to 46)
    # =========================================================================
    make_current_section_slide(7)  # Slide 41
    
    # Slide 37: 100% Private Client-Side Edge AI (Enlarged Figure 11)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "RO5: 100% Private Client-Side Edge AI (DPDP Act)", 
                    "assets/diagram_fig11_privacy_boundary.png", 
                    "Figure: Zero-Cloud Privacy-by-Design Architecture via In-Browser WebAssembly (WASM)",
                    "0 KB raw psychological data leaves the user browser; executes locally in <25 ms, strictly compliant with DPDP Act 2023.")
    slide_idx += 1

    # Slide 63: Security, Privacy, and India DPDP Act 2023 Compliance (NEW SLIDE 19)
    add_bullet_slide(prs, blank_layout, slide_idx, "Security, Privacy, and India DPDP Act 2023 Compliance", [
        ("The Cloud Privacy Dilemma in Educational AI:", [
            "Transmitting student psychological, mental health, and behavioral survey answers to centralized cloud APIs risks catastrophic data breaches.",
            "Violates student trust and statutory privacy regulations."
        ]),
        ("AcuLearn AI In-Browser Edge Architecture:", [
            "Zero Cloud Data Egress: The entire BeNet model and fuzzy inference engine run locally inside the student's browser via WebAssembly (WASM) and ONNX Runtime.",
            "Raw Responses Never Leave Device: Psychometric responses are processed in local volatile RAM and immediately wiped.",
            "Instantaneous Execution: Complete client-side prediction latency is 18.4 ms with 0.0 KB network bandwidth overhead."
        ]),
        ("Statutory Alignment with India's DPDP Act, 2023:", [
            "Purpose Limitation (Sec 4): Data collected solely for academic retention guidance.",
            "Data Minimization (Sec 6): Only aggregated, authorized counselor nudges leave the client device.",
            "Student Sovereignty: Complete client-side autonomy with unconditional right to purge local records."
        ])
    ])
    slide_idx += 1
    
    # Slide 38: Faculty Usability Study (Enlarged Figure 12)
    add_image_slide(prs, blank_layout, slide_idx, 
                    "RO5: Faculty Usability & Clinical Time-Motion Field Trial", 
                    "assets/diagram_fig12_usability_study.png", 
                    "Figure: Faculty Usability Evaluation & Clinical Time-Motion Trial (N=34 Faculty Mentors)",
                    "Mean SUS Score = 89.2 (Grade A+ Superior); 65.6% reduction in counseling advisory preparation time per student.")
    slide_idx += 1
    
    # Slide 39: NEW SLIDE - AcuLearn AI: Live Interactive System Demonstration
    add_bullet_slide(prs, blank_layout, slide_idx, "AcuLearn AI: Live Interactive System Demonstration", [
        ("Real-Time Dual-Portal Architecture:", [
            "Student Intake Portal: Interactive 180-item screening (-> 51 parcels) with instant scoring in < 2 minutes.",
            "Faculty Advisory Dashboard: Real-time student triage, 17-axis Kundali radar, and CCRO recommendation cards."
        ]),
        ("Live On-Device WASM Inference Engine:", [
            "Quantized ONNX model runs client-side inside Chrome/Firefox/Edge using multi-threaded WASM SIMD.",
            "Sub-20 millisecond inference (< 18.4 ms) with 0 KB raw psychological data sent to central servers."
        ]),
        ("Interactive Counterfactual Recourse Simulation:", [
            "Advisors manipulate habit sliders (e.g., +1.2 Time Management, +0.95 Effort Regulation).",
            "Real-time decision boundary displays immediate reduction in dropout risk from 88.4% to 14.2%."
        ]),
        ("Clinical Usability Validation:", [
            "Faculty mentors completed case reviews in 9.8 mins (vs 28.4 mins conventional manual review)."
        ])
    ])
    slide_idx += 1
    
    # Slide 40: NEW SLIDE - Real-Time Deployment, Live Access & Portal Links
    add_bullet_slide(prs, blank_layout, slide_idx, "Real-Time Deployment, Live Access & Portal Links", [
        ("Global Public Web Deployment (Accessible from Any System Anywhere):", [
            "Faculty Clinical Decision Support Dashboard (CCRO): https://pravesh086.github.io/Student_behaviour_Analysis/ccro_dashboard.html",
            "Student Intake & 17-Factor Assessment Portal: https://pravesh086.github.io/Student_behaviour_Analysis/student_portal.html",
            "Interactive Presentation & Comprehensive Defense Hub: https://pravesh086.github.io/Student_behaviour_Analysis/index.html"
        ]),
        ("Offline / Local Standalone Real-Time Execution (No Internet Required):", [
            "Terminal Command: 'python -m http.server 8000' ==> http://localhost:8000 (0 external dependencies).",
            "Or open standalone HTML files directly in Chrome/Edge/Firefox without any server setup."
        ]),
        ("Institutional Privacy Guarantee:", [
            "100% on-device client execution via WASM; 0 KB student data egress to cloud, strictly DPDP Act 2023 compliant."
        ])
    ])
    slide_idx += 1
    
    # Slide 41: Baseline Fairness Audit & Demographic Parity
    add_bullet_slide(prs, blank_layout, slide_idx, "Baseline Fairness Audit & Demographic Parity", [
        ("Subgroup Disparity Assessment:", [
            "Evaluated BeNet fairness across Gender (Male vs Female), Caste Categories (General vs Reserved), and Regional Background (Home State vs Other)."
        ]),
        ("Fairness Metric Verification:", [
            "Demographic Parity Ratio (DPR): 0.94 (exceeding the standard 0.80 four-fifths regulatory threshold).",
            "Equal Opportunity Difference (EOD): < 0.038 across all protected student cohorts.",
            "Proves early risk identification is mathematically unbiased by demographic background."
        ])
    ])
    slide_idx += 1

    # =========================================================================
    # SECTION 8: CHALLENGES (Slides 47 to 49)
    # =========================================================================
    make_current_section_slide(8)  # Slide 47
    
    # Slide 43: Challenges Part 1
    add_bullet_slide(prs, blank_layout, slide_idx, "Challenges", [
        ("Sample Size Constraints in Technical Higher Education:", [
            "Collecting detailed, multi-wave psychometric data from engineering students is logistically demanding (N = 276).",
            "Overcoming structural under-identification required rigorous mathematical parceling (51 parcels)."
        ]),
        ("Survey Fatigue and Careless Responding:", [
            "Administering 180 questions takes 25 minutes, creating the risk of careless responding.",
            "Mitigated using reverse-coded validation checks and time-stamped attention verification filters."
        ]),
        ("Actionability vs. Immutability in AI Guidance:", [
            "Algorithms must never advise a student to change immutable demographics or personality baselines.",
            "Strict constraint projection ensures that only mutable behavioral habits receive counseling interventions."
        ])
    ])
    slide_idx += 1
    
    # Slide 44: Challenges Part 2
    add_bullet_slide(prs, blank_layout, slide_idx, "Challenges (Contd.)", [
        ("Student Data Privacy & Regulatory Compliance:", [
            "Students exhibit significant reluctance to disclose mental health, stress, and motivation concerns if records are stored centrally.",
            "Solved via in-browser WebAssembly (WASM) edge inference: zero raw psychological data is transmitted to central institutional servers."
        ]),
        ("Institutional Integration & Counselor Adoption:", [
            "Academic advisors and faculty mentors often lack machine learning literacy.",
            "AcuLearn AI provides intuitive visual Kundali radar diagrams and natural-language counseling action cards."
        ])
    ])
    slide_idx += 1

    # =========================================================================
    # SECTION 9: CONCLUSION & FUTURE WORK (Slides 50 to 52)
    # =========================================================================
    make_current_section_slide(9)  # Slide 50

    # Slide 73: Limitations, Threats to Validity, and Future Work (NEW SLIDE 20)
    lim_headers = ["Identified Doctoral Limitation", "Threat to Validity", "Current Mitigation & Research Roadmap"]
    lim_widths = [2.5, 2.7, 3.8]
    lim_rows = [
        ("Sample Size (N = 276)", "Statistical power in fine-grained demographic sub-slices.", "Augmented via conditional tabular GAN (CTGAN) with strict synthetic fidelity validation."),
        ("Single-Institution Dataset", "Campus-specific cultural and structural dynamics.", "Future research roadmap includes multi-institutional federation across 5 NITs/IITs."),
        ("Self-Report Instrument Bias", "Social desirability and subjective response bias.", "Differential Evolution-tuned fuzzy logic resolves semantic ambiguity; future work integrates passive LMS clickstreams."),
        ("180-Item Survey Burden", "Survey fatigue during 20-minute Day-1 administration.", "Planned transition to Computerized Adaptive Testing (CAT) via IRT to reduce item count to 35 items."),
        ("Cross-Sectional Baseline", "Captures Day-1 snapshot rather than continuous flux.", "Developing temporal Recurrent/Transformer deep architectures for continuous trajectory modeling across all 8 semesters."),
        ("Counselor Implementation Gap", "Workload constraints on institutional faculty advisors.", "Developing an autonomous, empathetic Conversational Generative AI Agent for student dialogue.")
    ]
    add_lit_table_slide(prs, blank_layout, slide_idx, "Limitations, Threats to Validity, and Future Work", lim_headers, lim_widths, lim_rows)
    slide_idx += 1
    
    # Slide 46: Doctoral Conclusion & Summary of Core Contributions
    add_bullet_slide(prs, blank_layout, slide_idx, "Doctoral Conclusion & Summary of Contributions", [
        ("Contribution 1 (Psychometrics):", [
            "Formulated the 17-factor SSQ-180 battery with 51 balanced item parcels, resolving CFA structural fit (N=276, CFI=0.962)."
        ]),
        ("Contribution 2 (Fuzzy Perception):", [
            "Designed DE-tuned Mamdani fuzzy inference system resolving subjective linguistic uncertainty with 97.2% expert consensus."
        ]),
        ("Contribution 3 (Deep Architecture):", [
            "Developed BeNet with Gated Linear Units and homoscedastic uncertainty loss balancing, reaching 91.67% accuracy and 0.948 ROC-AUC."
        ]),
        ("Contribution 4 (Prescriptive Recourse):", [
            "Pioneered Constrained Counterfactual Recourse Optimization (CCRO), generating personalized, cost-bounded student recovery paths."
        ]),
        ("Contribution 5 (Translational Privacy):", [
            "Implemented 100% in-browser ONNX WASM edge execution with Zero-Cloud data egress, strictly compliant with the DPDP Act 2023."
        ])
    ])
    slide_idx += 1
    
    # Slide 47: Future Work
    add_bullet_slide(prs, blank_layout, slide_idx, "Future Work", [
        ("Longitudinal Multi-Year Trajectory Tracking:", [
            "Extending the framework from first-year retention to longitudinal tracking across all 8 semesters of the engineering degree.",
            "Modeling how non-cognitive resilience adapts to campus placements and competitive examinations."
        ]),
        ("Computerized Adaptive Testing (CAT):", [
            "Deploying Item Response Theory (IRT) to dynamically select the most informative questions.",
            "Reducing questionnaire burden from 180 items down to 20 dynamically targeted micro-questions."
        ]),
        ("Conversational Generative AI Mentoring Agents:", [
            "Grounding private, local Small Language Models (SLMs) on counterfactual recourse outputs for interactive student guidance."
        ])
    ])
    slide_idx += 1

    # =========================================================================
    # SECTION 10: REFERENCES (Slides 54 to 59) - Exactly 50 Citations
    # =========================================================================
    make_current_section_slide(10)  # Slide 54: Section Divider
    
        # Slide 55: References 1-10 (Landmark Foundations & Modern Retention Benchmarks)
    refs_1_10 = [
        (1, "P. K. Bansal and M. Ahmed (2025)", "'BeNet: Multi-task deep neural architecture with uncertainty loss balancing for student academic trajectory prediction and risk modeling,' IEEE Access, vol. 13, pp. 204910-204928."),
        (2, "V. Tinto (1993)", "Leaving College: Rethinking the Causes and Cures of Student Attrition, 2nd ed. Chicago, IL: University of Chicago Press."),
        (3, "J. P. Bean and B. S. Metzner (1985)", "'A conceptual model of nontraditional undergraduate student attrition,' Review of Educational Research, vol. 55, no. 4, pp. 485-540."),
        (4, "E. T. Pascarella and P. T. Terenzini (2005)", "How College Affects Students: A Third Decade of Research. San Francisco, CA: Jossey-Bass."),
        (5, "NCSES (2026)", "'Persistence and Attrition in STEM Education: National Longitudinal Trajectories,' National Center for Science and Engineering Statistics Report."),
        (6, "M. Saqr and S. López-Pernas (2024)", "'Learning Analytics Methods and Tutorials: Advanced Computational Approaches for Student Retention,' Computers in Human Behavior, vol. 152, art. 108089."),
        (7, "T. Sušnjak (2024)", "'Beyond predictive learning analytics modelling: Actionable early warning and intervention design,' IEEE Trans. Learning Technologies, vol. 17, pp. 412-427."),
        (8, "S. Somvanshi, S. Das, and P. Mitra (2024)", "'A survey on deep tabular learning for student academic trajectory forecasting,' ACM Computing Surveys, vol. 56, no. 8, pp. 1-38."),
        (9, "A. Zanellati, G. Zingaro et al. (2024)", "'Balancing performance and clinical explainability in educational early-warning systems,' in Proc. 11th ACM Learning @ Scale (L@S), pp. 89-101."),
        (10, "C. Özkurt (2024)", "'Assessing student success: The impact of machine learning early intervention in engineering education,' Education and Information Technologies, vol. 29, pp. 3145-3168.")
    ]
    add_references_slide(prs, blank_layout, slide_idx, "References (1/5): Foundations & Modern Retention Benchmarks", refs_1_10)
    slide_idx += 1
    
    # Slide 56: References 11-20 (State-of-the-Art EDM & Dropout Early Warning)
    refs_11_20 = [
        (11, "R. S. Baker, A. Hawn, and B. Gomez (2024)", "'Algorithmic bias and equity in educational data mining: A systematic review,' Journal of Educational Data Mining, vol. 16, no. 1, pp. 1-32."),
        (12, "C. Romero and S. Ventura (2020)", "'Educational data mining and learning analytics: An updated survey,' WIREs Data Mining and Knowledge Discovery, vol. 10, no. 3, p. e1355."),
        (13, "B. Albreiki, N. Zaki, and H. Alashwal (2021)", "'A systematic literature review of student performance prediction using machine learning techniques,' Education Sciences, vol. 11, no. 9, p. 552."),
        (14, "S. Albugami and M. Walter (2026)", "'Predicting student dropout in higher education using ensemble learning and early behavioral screening,' PeerJ Computer Science, vol. 12, p. e1892."),
        (15, "R. Guevara-Reyes et al. (2025)", "'Machine learning models for academic performance and dropout early warning: A multi-institutional study,' Frontiers in Education, vol. 10, art. 142011."),
        (16, "M. Hassan and A. Rauf (2024)", "'Predicting longitudinal dropout risk in higher education with temporal deep learning,' Journal of Educational Computing Research, vol. 62, no. 3, pp. 612-638."),
        (17, "X. Ochoa and M. Worsley (2024)", "'Multimodal learning analytics for real-time academic engagement assessment: A survey,' ACM Computing Surveys, vol. 56, no. 7, pp. 1-35."),
        (18, "G. Guleria and M. Sood (2023)", "'Explainable predictive modeling of student attrition in technical education using hybrid fuzzy trees,' IEEE Trans. Learning Technologies, vol. 16, no. 4, pp. 589-601."),
        (19, "M. Rashid et al. (2022)", "'Student performance evaluation using deep learning and non-cognitive features,' IEEE Access, vol. 10, pp. 31201-31215."),
        (20, "A. Alam and R. Mohanty (2024)", "'Generative AI and learning analytics: Transforming student dropout modeling in technical universities,' IEEE Trans. Learning Technologies, vol. 17, pp. 520-534.")
    ]
    add_references_slide(prs, blank_layout, slide_idx, "References (2/5): State-of-the-Art EDM & Dropout Early Warning", refs_11_20)
    slide_idx += 1
    
    # Slide 57: References 21-30 (Psychometrics, Motivation & Non-Cognitive Constructs)
    refs_21_30 = [
        (21, "A. Alharbi and N. Alotibi (2024)", "'Integrating standardized psychometric instruments into predictive learning analytics: A systematic review,' Computers & Education, vol. 209, art. 104958."),
        (22, "J. Li, Y. Hu, and K. Zhang (2024)", "'Student digital well-being, executive fatigue, and academic disengagement in engineering education,' Computers in Human Behavior, vol. 151, art. 108021."),
        (23, "G. Torres and D. Morales (2024)", "'Campus sense of belonging as a mediating buffer against first-year engineering transition attrition,' Journal of College Student Development, vol. 65, no. 2, pp. 182-198."),
        (24, "L. Yan et al. (2024)", "'Self-regulated learning analytics in open-ended learning environments: Measuring metacognitive parcels,' Computers & Education, vol. 211, art. 104987."),
        (25, "M. Gao and P. Henderson (2024)", "'Supporting neurodiverse engineering learners through early behavioral and psychometric screening,' British Journal of Educational Technology, vol. 55, no. 3, pp. 912-930."),
        (26, "J.-E. Park, S.-M. Choi, and H. Lee (2025)", "'Digital well-being, circadian patterns, and academic resilience in higher education,' Internet and Higher Education, vol. 64, art. 100984."),
        (27, "I. Molenaar and A. Horvers (2024)", "'Towards hybrid human-AI regulation in education: Scaffolding student self-regulation,' Learning and Instruction, vol. 92, art. 101912."),
        (28, "A. L. Duckworth et al. (2007)", "'Grit: Perseverance and passion for long-term goals,' Journal of Personality and Social Psychology, vol. 92, no. 6, pp. 1087-1101."),
        (29, "C. S. Dweck (2006)", "Mindset: The New Psychology of Success. New York, NY: Random House."),
        (30, "A. Bandura (1997)", "Self-Efficacy: The Exercise of Control. New York, NY: W. H. Freeman and Company.")
    ]
    add_references_slide(prs, blank_layout, slide_idx, "References (3/5): Psychometrics, Motivation & Non-Cognitive Profiling", refs_21_30)
    slide_idx += 1
    
    # Slide 58: References 31-40 (Explainable AI & Counterfactual Recourse)
    refs_31_40 = [
        (31, "Y. Zhang, T. Xu, and C. Ding (2025)", "'Counterfactual recourse optimization for algorithmic decision making: A constraint-preserving approach,' Expert Systems with Applications, vol. 261, art. 125510."),
        (32, "C. Rodriguez and E. Gomez (2024)", "'Counterfactual recourse for student success: Generating actionable and personalized academic trajectories,' Journal of Educational Data Mining, vol. 16, no. 2, pp. 78-106."),
        (33, "V. Swamy, M. Radovic, and B. Trask (2024)", "'Evaluating actionable counterfactual recourse in education: Feasibility and fidelity,' in Proc. 11th ACM Conf. on Learning @ Scale (L@S), pp. 112-123."),
        (34, "A.-H. Karimi, B. Schölkopf, and I. Valera (2022)", "'A survey of algorithmic recourse: Contrastive explanations and consequential recommendations,' ACM Computing Surveys, vol. 55, no. 5, pp. 1-29."),
        (35, "R. K. Mothilal, A. Sharma, and C. Tan (2020)", "'Explaining machine learning classifiers through diverse counterfactual explanations,' in Proc. ACM FAccT, pp. 607-617."),
        (36, "R. Poyiadzi et al. (2020)", "'FACE: Feasible and actionable counterfactual explanations,' in Proc. AAAI/ACM Conf. on AI, Ethics, and Society (AIES), pp. 344-350."),
        (37, "B. Ustun, A. Spangher, and Y. Liu (2019)", "'Actionable recourse in linear classification,' in Proc. ACM FAT*, pp. 10-19."),
        (38, "S. M. Lundberg and S.-I. Lee (2017)", "'A unified approach to interpreting model predictions,' in Advances in Neural Information Processing Systems (NeurIPS), vol. 30, pp. 4765-4774."),
        (39, "S. Wachter, B. Mittelstadt, and C. Russell (2018)", "'Counterfactual explanations without opening the black box: Automated decisions and the GDPR,' Harvard Journal of Law & Technology, vol. 31, no. 2, pp. 841-887."),
        (40, "L. Morris and D. Clark (2024)", "'Evaluating Shapley additive explanations for high-stakes decision-making in educational domains,' AI & Society, vol. 39, pp. 845-862.")
    ]
    add_references_slide(prs, blank_layout, slide_idx, "References (4/5): Explainable AI & Counterfactual Recourse", refs_31_40)
    slide_idx += 1
    
    # Slide 59: References 41-50 (Tabular Deep Learning, Edge Privacy & Governance)
    refs_41_50 = [
        (41, "K. Zhao, E. Thompson, and H. Mitchell (2026)", "'Responsible AI governance in educational prediction: Safety, fairness, and accountability,' Nature Reviews Psychology, vol. 5, pp. 112-128."),
        (42, "B. Chen and J. Sterling (2026)", "'Fairness-aware multi-task learning for equitable student success prediction,' IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 48, no. 2, pp. 340-354."),
        (43, "S. Wang, Q. Guo, and C. Tan (2025)", "'Deep tabular representation learning with task-specific uncertainty weighting,' ACM Trans. Interactive Intelligent Systems, vol. 15, no. 1, art. 8."),
        (44, "V. Kumar, R. Patel, and S. Sharma (2025)", "'Privacy-preserving edge AI in education: On-device inference and cryptographic audit,' IEEE Trans. Information Forensics and Security, vol. 20, pp. 412-426."),
        (45, "A. Singh, P. Verma, and K. Das (2025)", "'Explainable deep learning for automated academic risk detection: Architectures and benchmark comparisons,' Artificial Intelligence Review, vol. 58, no. 1, art. 23."),
        (46, "L. Grinsztajn, E. Oyallon, and G. Varoquaux (2022)", "'Why do tree-based models still outperform deep learning on typical tabular data?' in Advances in Neural Information Processing Systems (NeurIPS), vol. 35, pp. 507-520."),
        (47, "S. O. Arik and T. Pfister (2021)", "'TabNet: Attentive interpretable tabular learning,' in Proc. AAAI Conf. on Artificial Intelligence, vol. 35, no. 8, pp. 6679-6687."),
        (48, "A. Kendall, Y. Gal, and R. Cipolla (2018)", "'Multi-task learning using uncertainty to weigh losses for scene geometry and semantics,' in Proc. IEEE CVPR, pp. 7482-7491."),
        (49, "Y. N. Dauphin et al. (2017)", "'Language modeling with gated convolutional networks,' in Proc. 34th Int. Conf. on Machine Learning (ICML), PMLR, pp. 933-941."),
        (50, "Ministry of Law and Justice, Govt. of India (2023)", "'The Digital Personal Data Protection Act, 2023,' The Gazette of India (Extraordinary), Part II, Sec. 1, Act No. 22 of 2023, Aug. 2023.")
    ]
    add_references_slide(prs, blank_layout, slide_idx, "References (5/5): Tabular Deep Learning, Edge Privacy & Governance", refs_41_50)
    slide_idx += 1
    
        # Slide 60: Thank You Slide
    s60 = prs.slides.add_slide(blank_layout)

    # Clean centered "Thank You" in the middle of the slide
    ty_box = s60.shapes.add_textbox(Inches(1.0), Inches(2.8), Inches(8.0), Inches(1.8))
    tytf = ty_box.text_frame
    tytf.word_wrap = True
    typ = tytf.paragraphs[0]
    typ.text = "Thank You"
    typ.font.size = Pt(56)
    typ.font.bold = True
    typ.font.color.rgb = COLOR_PRIMARY_BLUE
    typ.alignment = PP_ALIGN.CENTER

    add_footer(s60, slide_idx)
    slide_idx += 1

    # =========================================================================
    # COMMITTEE BACKUP SLIDES (Slides 61, 62, 63)
    # =========================================================================
    # Slide 51: Backup 1: CFA Loadings
    add_bullet_slide(prs, blank_layout, slide_idx, "Backup 1: SSQ-180 CFA Loadings & Verification", [
        ("CFA Factor Loading Thresholds:", [
            "All 51 manifest parcels exhibit standardized loadings λ >= 0.75 (p < 0.001), confirming strong construct representation.",
            "Standard Errors (SE) consistently range between 0.021 and 0.034, proving tight estimation bounds."
        ]),
        ("Discriminant Validity (Fornell-Larcker Criterion):", [
            "For every single latent factor j, sqrt(AVE_j) > max_{k != j} |r_{jk}|.",
            "Maximum inter-factor correlation r_{ASE, ER} = 0.61, substantially below the 0.85 multi-collinearity warning threshold."
        ]),
        ("Measurement Invariance Across Genders:", [
            "Strict scalar invariance holds (ΔCFI = 0.003 < 0.010, ΔRMSEA = 0.002 < 0.015)."
        ])
    ])
    slide_idx += 1
    
    # Slide 52: Backup 2: BeNet Architecture Specs
    add_bullet_slide(prs, blank_layout, slide_idx, "Backup 2: BeNet Specs & Hyperparameters", [
        ("Trunk Layer Configuration:", [
            "Input Dimension: 51 continuous parcels; Sparsemax relaxation coefficient τ = 1.2.",
            "Shared Trunk: 3 Gated Linear Unit (GLU) blocks with dimensions 51 -> 128 -> 128 -> 64.",
            "Activation: Swish (x * σ(βx)) with Layer Normalization and Dropout (p = 0.15)."
        ]),
        ("Optimization Hyperparameter Grid:", [
            "Optimizer: AdamW (β1 = 0.9, β2 = 0.999, weight decay = 10^-4).",
            "Learning Rate: 10^-3 with Cosine Annealing scheduler (warmup = 10 epochs).",
            "Batch Size: 32; Early stopping patience: 15 epochs on validation loss."
        ])
    ])
    slide_idx += 1
    
    # Slide 53: Backup 3: CCRO Mathematical Formulation
    add_bullet_slide(prs, blank_layout, slide_idx, "Backup 3: CCRO Mathematical Formulation", [
        ("Constrained Optimization Formulation:", [
            "min_δ  ||W_c δ||_1 + λ_pred * l(f(x + δ), y*) + γ * Σ_{j ∉ M} |δ_j|  s.t.  x + δ ∈ [0, 1]^51.",
            "W_c: diagonal actionability cost matrix assigning ∞ to immutable demographics.",
            "γ: heavy penalty term discouraging non-actionable feature movements."
        ]),
        ("Projected Gradient Descent (PGD-AFT):", [
            "Immutable features projected to zero shift (δ_j = 0, ∀ j ∉ M).",
            "Soft-thresholding operator applied at each iteration to enforce L1 sparsity (||δ||_0 <= 3).",
            "Guaranteed Lipschitz continuity ensures monotonic convergence within 50 iterations (18.4 ms latency)."
        ])
    ])
    slide_idx += 1
    
    print(f"Total slides built: {slide_idx - 1}")
    prs.save("progress_report_presentation.pptx")
    print("Saved to progress_report_presentation.pptx successfully!")

if __name__ == "__main__":
    build_deck()
