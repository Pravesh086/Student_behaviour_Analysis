#!/usr/bin/env python3
"""
Comprehensive 17-Domain & 255-Question Psychometrics, Demographic Analytics & AI Counseling Engine
Analyzes Expanded_Synthetic_Student_Dataset.csv (2,525 students x 255 questions x 17 domains + 13 Demographics)
Outputs structured JSON and JS for the web dashboard and REST API.
"""

import csv
import json
import math
import os
import statistics
from collections import Counter, defaultdict

# Auto-detect expanded dataset or generate if not present
CSV_FILE = "Expanded_Synthetic_Student_Dataset.csv"
if not os.path.exists(CSV_FILE):
    import expand_dataset
    expand_dataset.main()

OUTPUT_JSON = "dashboard_data.json"
OUTPUT_JS = "dashboard_data.js"

DOMAINS_17 = [
    "Academic Motivation",
    "Learning Behaviour",
    "Time Management",
    "Emotional Intelligence",
    "Physical Activity & Wellness",
    "Communication Skills",
    "Leadership & Teamwork",
    "Critical Thinking & Decision Making",
    "Career Readiness",
    "Digital Literacy & AI Readiness",
    "Creativity & Innovation",
    "Resilience & Adaptability",
    # 5 Newly Integrated Proposed Domains
    "Financial & Socioeconomic Well-Being",
    "Campus Belonging & Peer Support",
    "Neurodiversity, ADHD & Executive Functioning",
    "Screen Time, Blue Light & Digital Well-Being",
    "LMS Usability & Hybrid Learning"
]

DOMAIN_SHORT_CODES = {
    "Academic Motivation": "AM",
    "Learning Behaviour": "LB",
    "Time Management": "TM",
    "Emotional Intelligence": "EI",
    "Physical Activity & Wellness": "PAW",
    "Communication Skills": "CS",
    "Leadership & Teamwork": "LT",
    "Critical Thinking & Decision Making": "CTDM",
    "Career Readiness": "CR",
    "Digital Literacy & AI Readiness": "DLR",
    "Creativity & Innovation": "CI",
    "Resilience & Adaptability": "RA",
    # 5 New Codes
    "Financial & Socioeconomic Well-Being": "FIN",
    "Campus Belonging & Peer Support": "BEL",
    "Neurodiversity, ADHD & Executive Functioning": "NEU",
    "Screen Time, Blue Light & Digital Well-Being": "SCR",
    "LMS Usability & Hybrid Learning": "LMS"
}

# Full 255 Questions Descriptive Topic Mapping (15 questions per domain)
QUESTION_TOPICS = {
    "Academic Motivation": [
        "Goal Clarity & Ambition", "Intrinsic Curiosity", "Drive for Academic Mastery",
        "Engagement with Coursework", "Perseverance in Difficult Subjects", "Value Placed on Education",
        "Proactive Academic Planning", "Desire for Academic Excellence", "Interest in Deep Learning",
        "Self-Driven Study Habits", "Positive Attitude to Challenges", "Commitment to Academic Milestones",
        "Active Classroom Participation", "Motivation to Overcome Setbacks", "Long-Term Academic Vision"
    ],
    "Learning Behaviour": [
        "Active Listening & Note-Taking", "Regular Revision Routine", "Resourcefulness in Research",
        "Conceptual Understanding Focus", "Self-Regulated Learning Strategies", "Effective Homework Completion",
        "Questioning & Clarification Seeking", "Application of Feedback", "Structured Study Schedules",
        "Meta-Cognitive Self-Monitoring", "Independent Problem Solving", "Utilization of Study Aids",
        "Peer Collaborative Study", "Paced Exam Preparation", "Continuous Skill Improvement"
    ],
    "Time Management": [
        "Daily Task Prioritization", "Adherence to Study Deadlines", "Minimizing Procrastination",
        "Balanced Study-Life Routine", "Efficient Allocation of Study Hours", "Calendar & Planner Usage",
        "Managing Academic Distractions", "Prompt Submission of Assignments", "Long-Range Project Pacing",
        "Effective Exam Prep Scheduling", "Consistent Sleep & Study Rhythm", "Task Breakdown & Chunking",
        "Handling Competing Demands", "Timely Attendance & Punctuality", "Stress-Free Deadline Management"
    ],
    "Emotional Intelligence": [
        "Self-Awareness of Emotions", "Emotional Regulation Under Pressure", "Empathy Toward Peers",
        "Handling Constructive Criticism", "Stress Tolerance in Exams", "Recognizing Triggers of Anxiety",
        "Maintaining Optimism During Difficulty", "Social Awareness in Group Settings", "Conflict De-escalation",
        "Mindful Emotional Expression", "Compassion and Peer Support", "Adapting to Emotional Atmosphere",
        "Self-Calming Techniques", "Understanding Non-Verbal Cues", "Resilience Against Frustration"
    ],
    "Physical Activity & Wellness": [
        "Regular Physical Exercise", "Nutritious Eating Habits", "Consistent Sleep Schedule",
        "Hydration & Energy Maintenance", "Active Breaks During Study", "Mind-Body Health Balance",
        "Outdoor Movement & Fresh Air", "Posture & Ergonomics at Desk", "Avoidance of Substance Burnout",
        "Stress Release Through Sports", "Physical Stamina for Long Tasks", "Preventative Health Awareness",
        "Relaxation & Deep Breathing", "Engagement in Recreational Play", "Overall Energy & Vitality Level"
    ],
    "Communication Skills": [
        "Clear Verbal Articulation", "Active & Attentive Listening", "Effective Written Expression",
        "Confidence in Public Speaking", "Constructive Question Formulations", "Persuasive Presentation Ability",
        "Non-Verbal Body Language & Eye Contact", "Clarity in Group Discussions", "Structuring Logical Arguments",
        "Digital Communication Etiquette", "Synthesizing Complex Ideas Simply", "Openness to Diverse Viewpoints",
        "Providing Clear Peer Feedback", "Diplomatic Conflict Articulation", "Concise & Meaningful Summaries"
    ],
    "Leadership & Teamwork": [
        "Collaborative Team Mindset", "Inspiring & Motivating Others", "Fair Delegation of Shared Tasks",
        "Taking Initiative on Group Work", "Fostering Inclusive Team Norms", "Accountability for Team Outcomes",
        "Mediating Group Disagreements", "Encouraging Quiet Contributors", "Shared Vision Alignment",
        "Reliability as a Team Contributor", "Constructive Consensus Building", "Adaptability in Team Roles",
        "Celebrating Group Achievements", "Transparent Decision Making", "Mentoring & Uplifting Teammates"
    ],
    "Critical Thinking & Decision Making": [
        "Evaluating Evidence Objectively", "Logical Fallacy Identification", "Root Cause Problem Analysis",
        "Synthesizing Multiple Perspectives", "Sound Judgement Under Uncertainty", "Challenging Biased Assumptions",
        "Systematic Option Weighing", "Data-Driven Decision Making", "Strategic Long-Term Reasoning",
        "Distinguishing Fact from Opinion", "Foreseeing Unintended Consequences", "Structured Decision Frameworks",
        "Intellectual Rigor & Questioning", "Iterative Solution Optimization", "Ethical Decision Frameworks"
    ],
    "Career Readiness": [
        "Clarity of Career Direction", "Resume & Portfolio Preparation", "Professional Networking Ability",
        "Industry Trends Knowledge", "Interview & Presentation Skills", "Understanding Job Market Demands",
        "Professional Etiquette & Demeanor", "Proactive Internship/Job Search", "Continuous Professional Upskilling",
        "Workplace Problem Solving Agility", "Alignment with Career Mentors", "Commercial & Industry Awareness",
        "Strategic Career Goal Setting", "Readiness for Work Culture", "Translating Academic Skills to Industry"
    ],
    "Digital Literacy & AI Readiness": [
        "Proficiency with Digital Productivity Tools", "Understanding AI Concepts & Tools", "Ethical Use of AI in Learning",
        "Effective AI Prompt Engineering", "Critical Assessment of AI Outputs", "Cybersecurity & Data Privacy Habits",
        "Online Research & Source Verification", "Digital File & Workflow Management", "Agility with New Software Platforms",
        "Algorithmic Thinking & Automation", "Collaborative Cloud Tools Mastery", "Digital Troubleshooting Capability",
        "Understanding AI Impact on Careers", "Data Interpretation & Literacy", "Responsible Digital Citizenship"
    ],
    "Creativity & Innovation": [
        "Generating Novel Ideas", "Thinking Outside the Box", "Connecting Unrelated Concepts",
        "Willingness to Experiment & Iterate", "Creative Problem Reframing", "Artistic or Technical Ingenuity",
        "Comfort with Ambiguity & Novelty", "Brainstorming Fluent Solutions", "Challenging Conventional Wisdom",
        "Transforming Ideas into Prototypes", "Embracing Constructive Failure", "Originality in Project Execution",
        "Cross-Disciplinary Exploration", "Curiosity for Unexplored Fields", "Adaptive Resourcefulness"
    ],
    "Resilience & Adaptability": [
        "Bouncing Back from Low Grades", "Thriving Amidst Unplanned Changes", "Viewing Failures as Growth Lessons",
        "Patience Under High Pressure", "Flexibility with New Teaching Styles", "Grit in Long-Term Pursuits",
        "Maintaining Focus During Disruptions", "Positive Cognitive Reframing", "Proactive Seeking of Help",
        "Emotional Steadiness Under Stress", "Openness to Shifting Priorities", "Overcoming Imposter Syndrome",
        "Tenacity Against Academic Hurdles", "Adaptability to Diverse Environments", "Sustained Long-Term Determination"
    ],
    # 5 New Domains (Q181 - Q255)
    "Financial & Socioeconomic Well-Being": [
        "Absence of Tuition Anxiety", "Work-Study Hours Balance", "Textbook & Courseware Access",
        "Awareness of Emergency Financial Aid", "Minimal Domestic Financial Demands", "High-Speed Hardware Equity",
        "Emergency Financial Resilience", "Confidence in Graduation Affordability", "Food & Housing Security",
        "Budgeting & Living Cost Management", "Absence of Debt Burden Panic", "Family Educational Financial Support",
        "Access to Commuter Transit Subsidies", "Healthcare & Insurance Peace of Mind", "Financial Planning Self-Efficacy"
    ],
    "Campus Belonging & Peer Support": [
        "Sense of Departmental Community", "Reliable Peer Study Network", "Faculty Office Hours Comfort",
        "Extracurricular & Club Participation", "Inclusivity in Class Discussions", "Absence of Social Isolation",
        "Access to Senior Student Mentors", "Institutional Pride & Affinity", "Positive Roommate/Housing Harmony",
        "Campus Mental Health Center Trust", "Welcoming Atmosphere in Laboratories", "Comfort Seeking Academic Advice",
        "Cross-Cultural Peer Friendships", "Participation in Campus Traditions", "Active Voice in Student Governance"
    ],
    "Neurodiversity, ADHD & Executive Functioning": [
        "Low Friction Task Initiation", "Sustained Attention During Lectures", "Assignment Material Organization",
        "Comfort in Multi-Sensory Classrooms", "Cognitive Flexibility Across Subjects", "Working Memory for Multi-Step Tasks",
        "Awareness of Disability Accommodations", "Effective Personal Focus Rituals", "Restlessness Regulation Strategies",
        "Navigating Hyperfocus Balance", "Effective Time Estimation Ability", "Management of Exam Sensory Distractions",
        "Verbal Processing Comprehension", "Emotional Regulation for Frustration", "Adaptive Note-Taking Systems"
    ],
    "Screen Time, Blue Light & Digital Well-Being": [
        "Recreational Screen Time Moderation", "Pre-Sleep Blue Light Hygiene", "Absence of Digital Eye Strain",
        "Focus Without Social Media Distraction", "Ergonomic Desk & Chair Setup", "Consistent 20-20-20 Eye Breaks",
        "Weekend Digital Detox Practices", "Resistance to Notification Overwhelm", "Post-Screen Physical Stretching",
        "Optimal Screen Brightness Settings", "Healthy Asynchronous Study Limits", "Outdoor Eye Relief Habits",
        "Minimal Doomscrolling at Night", "Audio-Only Study Variation", "Mindful Digital Consumption"
    ],
    "LMS Usability & Hybrid Learning": [
        "LMS Portal Navigability", "Effective Use of Recorded Lectures", "Hybrid Classroom Engagement",
        "Rubric & Grading Transparency", "Timeliness of Instructor Feedback", "Breakout Room Collaboration Ease",
        "Technical Submission Self-Sufficiency", "Alignment with Hybrid Pedagogy", "Clear Digital Notification Feeds",
        "Mobile LMS Accessibility", "Synchronous Chat Participation", "Discussion Board Value & Quality",
        "Digital Exam Proctoring Ease", "Integrated Calendar Synchronization", "Cloud Submission Reliability"
    ]
}

def pearson_corr(x, y):
    n = len(x)
    if n == 0: return 0
    mx = sum(x) / n
    my = sum(y) / n
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    sx = math.sqrt(sum((x[i] - mx) ** 2 for i in range(n)))
    sy = math.sqrt(sum((y[i] - my) ** 2 for i in range(n)))
    if sx * sy == 0: return 0
    return cov / (sx * sy)

def generate_ai_counseling_dossier(student):
    diagnostics = student["diagnostics"]
    active_flags = []
    if diagnostics["interest"]["isFlagged"]: active_flags.append("Lack of Academic Interest & Drive")
    if diagnostics["collaboration"]["isFlagged"]: active_flags.append("Peer Collaboration Deficit")
    if diagnostics["procrastination"]["isFlagged"]: active_flags.append("Chronic Procrastination")
    if diagnostics["screenFatigue"]["isFlagged"]: active_flags.append("Screen Fatigue & Ergonomic Strain")
    if diagnostics["chronicSkipping"]["isFlagged"]: active_flags.append("Chronic Skipping / Attendance Risk")
    if diagnostics["mentalBurnout"]["isFlagged"]: active_flags.append("Mental Burnout & Emotional Overload")
    if diagnostics["courseFailure"]["isFlagged"]: active_flags.append("Imminent Course Failure Threat")

    flag_count = len(active_flags)
    ov_mean = student.get("overallMean", 3.0)
    if flag_count >= 4 or ov_mean < 2.5:
        priority = "Critical Intervention Required"
        priority_color = "#ef4444"
    elif flag_count >= 2 or ov_mean < 3.0:
        priority = "High Priority Mentoring"
        priority_color = "#f59e0b"
    elif flag_count == 1:
        priority = "Targeted Coaching"
        priority_color = "#06b6d4"
    else:
        priority = "Positive Reinforcement & Growth"
        priority_color = "#10b981"

    root_causes = []
    if diagnostics["mentalBurnout"]["isFlagged"] and diagnostics["procrastination"]["isFlagged"]:
        root_causes.append("Burnout-Avoidance Cycle: High stress spikes trigger procrastination avoidance, compounding deadline pressure.")
    if diagnostics["screenFatigue"]["isFlagged"]:
        root_causes.append("Digital & Physical Strain: Excessive uninterrupted screen hours degrade energy, focus, and sleep hygiene.")
    if diagnostics["interest"]["isFlagged"]:
        root_causes.append("Goal Disconnect: Disconnection from course relevance lowers intrinsic motivation and participation.")
    if diagnostics["collaboration"]["isFlagged"]:
        root_causes.append("Social & Academic Isolation: Low peer engagement deprives student of shared study support.")
    if diagnostics["chronicSkipping"]["isFlagged"]:
        root_causes.append("Attendance Decay: Irregular circadian rhythms lead to missed lectures and content gaps.")
    if not root_causes:
        root_causes.append("Balanced Baseline: Strong foundation with opportunities for honors enrichment and leadership.")

    action_plan = [
        {
            "week": "Week 1: Stabilization & Biological Rhythm",
            "objective": "Reset sleep schedule, implement 20-20-20 screen rule, and schedule advisor intake.",
            "actions": [
                "Establish consistent wake-up time and 7.5 hour sleep window.",
                "Take 5-minute movement/eye breaks after every 45 minutes of screen work.",
                "Conduct initial 20-minute counseling review with departmental advisor."
            ]
        },
        {
            "week": "Week 2: Micro-Chunking & Pacing",
            "objective": "Deconstruct large intimidating assignments into 25-minute Pomodoro intervals.",
            "actions": [
                "Apply the '5-Minute Rule' to begin delayed assignments.",
                "Set daily top-3 priorities before opening digital devices.",
                "Submit first assignment draft 48 hours before official deadline."
            ]
        },
        {
            "week": "Week 3: Collaborative Re-Engagement & Tutoring",
            "objective": "Engage in peer study groups and attend professor office hours.",
            "actions": [
                "Pair with a designated study buddy for two 1-hour co-working blocks.",
                "Attend one faculty office hour to clarify challenging concepts.",
                "Participate actively with at least one question in seminar discussions."
            ]
        },
        {
            "week": "Week 4: Long-Term Habit Formation",
            "objective": "Evaluate milestone progress, review completed work, and formalize sustainable habits.",
            "actions": [
                "Review completed deliverables vs baseline with counselor.",
                "Establish weekly Sunday planning ritual for upcoming assignments.",
                "Transition from crisis triage to proactive career skill advancement."
            ]
        }
    ]

    counselor_questions = [
        f"\"When you begin studying for your courses, what is the primary emotional or mental hurdle you experience?\"",
        "\"What is one specific source of daily friction (screen fatigue, workload, sleep) that we can adjust immediately?\"",
        "\"Which topics or projects have sparked your curiosity or felt most rewarding over the past month?\"",
        "\"What is one micro-goal for this week (under 15 min/day) that you feel 100% confident you can accomplish?\""
    ]

    daily_habits = [
        "Morning 3-Priority Card: Write top 3 academic tasks before checking phone notifications.",
        "20-Minute Screen-Free Walk: Afternoon daylight exposure to counteract digital strain.",
        "5-Minute Nightly Workspace Reset: Clear desk to lower cognitive resistance the next morning."
    ]

    return {
        "priority": priority,
        "priorityColor": priority_color,
        "activeFlags": active_flags,
        "flagCount": flag_count,
        "rootCauses": root_causes,
        "actionPlan": action_plan,
        "counselorQuestions": counselor_questions,
        "dailyHabits": daily_habits
    }

def main():
    print(f"Loading {CSV_FILE} for 17-domain & 255-question psychometric analysis...")
    with open(CSV_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        raw_rows = list(reader)

    total_students = len(raw_rows)
    print(f"Total students: {total_students}")

    students = []
    
    diag_summary = {
        "disinterested": {"count": 0, "title": "Lack of Academic Interest", "icon": "compass", "color": "#f97316"},
        "collab_deficit": {"count": 0, "title": "Collaboration Deficit", "icon": "users-x", "color": "#a855f7"},
        "procrastinating": {"count": 0, "title": "Chronic Procrastination", "icon": "clock", "color": "#f59e0b"},
        "screen_fatigue": {"count": 0, "title": "Screen Fatigue & Strain", "icon": "monitor", "color": "#06b6d4"},
        "chronic_skipping": {"count": 0, "title": "Chronic Skipping Risk", "icon": "user-minus", "color": "#ec4899"},
        "mental_burnout": {"count": 0, "title": "Mental Burnout Risk", "icon": "flame", "color": "#ef4444"},
        "course_failure": {"count": 0, "title": "Imminent Course Failure", "icon": "alert-octagon", "color": "#dc2626"}
    }

    for idx, r in enumerate(raw_rows):
        student_id = r.get("Student_ID", f"STU-{idx+1:04d}")
        
        # Categorize Dropout Risk
        if r["Dropout_Risk_Low"] == "True": dropout_risk = "Low"
        elif r["Dropout_Risk_Medium"] == "True": dropout_risk = "Medium"
        else: dropout_risk = "High"

        # Categorize Career Readiness
        if r["Career_Readiness_Highly Ready"] == "True": career_readiness = "Highly Ready"
        elif r["Career_Readiness_Ready"] == "True": career_readiness = "Ready"
        elif r["Career_Readiness_Not Ready"] == "True": career_readiness = "Not Ready"
        else: career_readiness = "Moderately Ready"

        success_tier = r["Student_Success"]
        overall_mean = round(float(r.get("Overall_Mean", r.get("Overall_Mean_17", r.get("Overall_Mean_12", 3.0)))), 3)

        # 17 Domain Scores
        domain_scores = {}
        for d in DOMAINS_17:
            domain_scores[d] = round(float(r[d]), 3)

        # 255 Question responses (1 to 255)
        q_responses = {}
        for q_num in range(1, 256):
            q_code = f"Q{q_num:03d}"
            if q_code in r:
                q_responses[q_code] = int(r[q_code])

        # Demographics
        demographics = {
            "gender": r.get("Gender", "Female"),
            "age": int(r.get("Age", 20)),
            "academicYear": r.get("Academic_Year", "Sophomore"),
            "major": r.get("Department_Major", "Computer Science & AI"),
            "enrollment": r.get("Enrollment_Status", "Full-Time"),
            "housing": r.get("Housing_Type", "On-Campus Dormitory"),
            "firstGen": r.get("First_Gen_Student", "No"),
            "international": r.get("International_Student", "No"),
            "incomeTier": r.get("Socioeconomic_Tier", "Middle Class"),
            "jobHours": r.get("Part_Time_Job_Hours", "0 hrs/week"),
            "attendancePct": float(r.get("Attendance_Rate_Pct", 85.0)),
            "priorGPA": float(r.get("Prior_GPA", 3.2))
        }

        # 7 Diagnostics
        q_interest_avg = (q_responses.get("Q001", 3) + q_responses.get("Q002", 3) + q_responses.get("Q004", 3)) / 3.0
        interest_score = round(0.6 * domain_scores["Academic Motivation"] + 0.4 * q_interest_avg, 2)
        is_disinterested = interest_score < 2.80
        if is_disinterested: diag_summary["disinterested"]["count"] += 1

        q_collab_avg = (q_responses.get("Q028", 3) + q_responses.get("Q091", 3) + q_responses.get("Q100", 3)) / 3.0
        collab_score = round(0.4 * domain_scores["Leadership & Teamwork"] + 0.3 * domain_scores["Communication Skills"] + 0.3 * q_collab_avg, 2)
        is_collab_deficit = collab_score < 2.80
        if is_collab_deficit: diag_summary["collab_deficit"]["count"] += 1

        q_procrast_avg = (q_responses.get("Q032", 3) + q_responses.get("Q033", 3) + q_responses.get("Q038", 3)) / 3.0
        procrast_score = round(0.5 * domain_scores["Time Management"] + 0.5 * q_procrast_avg, 2)
        is_procrastinating = procrast_score < 2.80
        if is_procrastinating: diag_summary["procrastinating"]["count"] += 1

        q_strain_avg = (q_responses.get("Q065", 3) + q_responses.get("Q068", 3) + q_responses.get("Q069", 3)) / 3.0
        screen_fatigue_score = round(0.5 * domain_scores["Physical Activity & Wellness"] + 0.5 * q_strain_avg, 2)
        is_screen_fatigue = screen_fatigue_score < 2.80
        if is_screen_fatigue: diag_summary["screen_fatigue"]["count"] += 1

        skipping_score = round((q_responses.get("Q044", 3) + q_responses.get("Q013", 3) + q_responses.get("Q021", 3) + q_responses.get("Q041", 3)) / 4.0, 2)
        is_chronic_skipping = skipping_score < 2.70 and domain_scores["Time Management"] < 2.80
        if is_chronic_skipping: diag_summary["chronic_skipping"]["count"] += 1

        q_burnout_avg = (q_responses.get("Q050", 3) + q_responses.get("Q051", 3) + q_responses.get("Q166", 3) + q_responses.get("Q069", 3)) / 4.0
        burnout_score = round(0.35 * domain_scores["Emotional Intelligence"] + 0.35 * domain_scores["Resilience & Adaptability"] + 0.30 * q_burnout_avg, 2)
        is_mental_burnout = burnout_score < 2.80
        if is_mental_burnout: diag_summary["mental_burnout"]["count"] += 1

        is_course_failure = overall_mean < 2.60 and dropout_risk == "High" and success_tier in ["Bad", "Poor"]
        if is_course_failure: diag_summary["course_failure"]["count"] += 1

        student_diagnostics = {
            "interest": {"score": interest_score, "status": "High Drive" if interest_score >= 3.5 else ("Moderate" if interest_score >= 2.8 else "Disinterested"), "isFlagged": is_disinterested},
            "collaboration": {"score": collab_score, "status": "Strong Team Member" if collab_score >= 3.5 else ("Cooperative" if collab_score >= 2.8 else "Collaboration Deficit"), "isFlagged": is_collab_deficit},
            "procrastination": {"score": procrast_score, "status": "Proactive" if procrast_score >= 3.5 else ("Manageable" if procrast_score >= 2.8 else "Chronic Delay"), "isFlagged": is_procrastinating},
            "screenFatigue": {"score": screen_fatigue_score, "status": "Healthy Balance" if screen_fatigue_score >= 3.5 else ("Mild Strain" if screen_fatigue_score >= 2.8 else "Severe Fatigue"), "isFlagged": is_screen_fatigue},
            "chronicSkipping": {"score": skipping_score, "status": "Consistent Attendance" if not is_chronic_skipping else "High Skipping Risk", "isFlagged": is_chronic_skipping},
            "mentalBurnout": {"score": burnout_score, "status": "Resilient & Calm" if burnout_score >= 3.5 else ("Moderate Stress" if burnout_score >= 2.8 else "High Burnout Risk"), "isFlagged": is_mental_burnout},
            "courseFailure": {"score": overall_mean, "status": "Academic Good Standing" if not is_course_failure else "Imminent Course Failure", "isFlagged": is_course_failure}
        }

        student_record = {
            "id": student_id,
            "success": success_tier,
            "dropoutRisk": dropout_risk,
            "careerReadiness": career_readiness,
            "overallMean": overall_mean,
            "domainScores": domain_scores,
            "responses": q_responses,
            "demographics": demographics,
            "diagnostics": student_diagnostics
        }

        student_record["counseling"] = generate_ai_counseling_dossier(student_record)
        students.append(student_record)

    # 1. Summary KPIs
    success_counts = Counter(s["success"] for s in students)
    dropout_counts = Counter(s["dropoutRisk"] for s in students)
    career_counts = Counter(s["careerReadiness"] for s in students)

    overall_scores = [s["overallMean"] for s in students]
    overall_mean = statistics.mean(overall_scores)
    overall_median = statistics.median(overall_scores)
    overall_std = statistics.stdev(overall_scores)
    overall_min = min(overall_scores)
    overall_max = max(overall_scores)
    overall_q1 = statistics.quantiles(overall_scores, n=4)[0]
    overall_q3 = statistics.quantiles(overall_scores, n=4)[2]

    hist_bins = 10
    bin_width = (overall_max - overall_min) / hist_bins
    hist_counts = [0] * hist_bins
    hist_labels = []
    for b in range(hist_bins):
        b_start = overall_min + b * bin_width
        b_end = b_start + bin_width
        hist_labels.append(f"{b_start:.2f}-{b_end:.2f}")
    for val in overall_scores:
        bin_idx = min(int((val - overall_min) / bin_width), hist_bins - 1)
        hist_counts[bin_idx] += 1

    # 2. 17 Domains Analytics
    domain_analytics = []
    for d_idx, d_name in enumerate(DOMAINS_17):
        q_start = d_idx * 15 + 1
        q_end = (d_idx + 1) * 15
        q_keys = [f"Q{i:03d}" for i in range(q_start, q_end + 1)]
        
        scores = [s["domainScores"][d_name] for s in students]
        d_mean = statistics.mean(scores)
        d_std = statistics.stdev(scores)
        d_median = statistics.median(scores)
        d_min = min(scores)
        d_max = max(scores)
        d_q1 = statistics.quantiles(scores, n=4)[0]
        d_q3 = statistics.quantiles(scores, n=4)[2]

        # Cronbach Alpha
        k = len(q_keys) # 15
        item_vars = []
        for q in q_keys:
            q_vals = [s["responses"].get(q, 3) for s in students]
            item_vars.append(statistics.variance(q_vals))
        sum_item_var = sum(item_vars)

        domain_total_scores = [sum(s["responses"].get(q, 3) for q in q_keys) for s in students]
        total_var = statistics.variance(domain_total_scores)
        cronbach_alpha = (k / (k - 1)) * (1 - sum_item_var / total_var) if total_var > 0 else 0

        tier_means = {}
        for tier in ["Excellent", "Good", "Average", "Poor", "Bad"]:
            sub_scores = [s["domainScores"][d_name] for s in students if s["success"] == tier]
            tier_means[tier] = round(statistics.mean(sub_scores), 3) if sub_scores else 0

        risk_means = {}
        for risk in ["Low", "Medium", "High"]:
            sub_scores = [s["domainScores"][d_name] for s in students if s["dropoutRisk"] == risk]
            risk_means[risk] = round(statistics.mean(sub_scores), 3) if sub_scores else 0

        career_means = {}
        for cr in ["Highly Ready", "Ready", "Moderately Ready", "Not Ready"]:
            sub_scores = [s["domainScores"][d_name] for s in students if s["careerReadiness"] == cr]
            career_means[cr] = round(statistics.mean(sub_scores), 3) if sub_scores else 0

        domain_analytics.append({
            "name": d_name,
            "code": DOMAIN_SHORT_CODES[d_name],
            "questionRange": f"Q{q_start:03d} - Q{q_end:03d}",
            "mean": round(d_mean, 3),
            "std": round(d_std, 3),
            "median": round(d_median, 3),
            "min": round(d_min, 3),
            "max": round(d_max, 3),
            "q1": round(d_q1, 3),
            "q3": round(d_q3, 3),
            "cronbachAlpha": round(cronbach_alpha, 4),
            "tierMeans": tier_means,
            "riskMeans": risk_means,
            "careerMeans": career_means,
            "isNew": d_idx >= 12
        })

    # 3. 17x17 Correlation Matrix
    corr_matrix = []
    for d1 in DOMAINS_17:
        row = []
        v1 = [s["domainScores"][d1] for s in students]
        for d2 in DOMAINS_17:
            v2 = [s["domainScores"][d2] for s in students]
            r_val = pearson_corr(v1, v2)
            row.append(round(r_val, 3))
        corr_matrix.append(row)

    domain_overall_corr = {}
    for d in DOMAINS_17:
        vd = [s["domainScores"][d] for s in students]
        domain_overall_corr[d] = round(pearson_corr(vd, overall_scores), 4)

    # 4. 255 Questions Psychometrics
    question_analytics = []
    for d_idx, d_name in enumerate(DOMAINS_17):
        q_start = d_idx * 15 + 1
        q_end = (d_idx + 1) * 15
        q_keys = [f"Q{i:03d}" for i in range(q_start, q_end + 1)]
        domain_totals = [sum(s["responses"].get(q, 3) for q in q_keys) for s in students]

        for item_idx, q_code in enumerate(q_keys):
            q_num = int(q_code[1:])
            q_title = QUESTION_TOPICS[d_name][item_idx]
            vals = [s["responses"].get(q_code, 3) for s in students]
            
            q_mean = statistics.mean(vals)
            q_std = statistics.stdev(vals)
            q_var = statistics.variance(vals)

            freq = Counter(vals)
            freq_dist = {str(k): freq.get(k, 0) for k in range(1, 6)}
            freq_pct = {str(k): round(freq.get(k, 0) / total_students * 100, 1) for k in range(1, 6)}

            difficulty_index = round((q_mean - 1) / 4.0, 3)
            item_disc_domain = round(pearson_corr(vals, domain_totals), 3)
            item_disc_overall = round(pearson_corr(vals, overall_scores), 3)

            tier_q_means = {}
            for tier in ["Excellent", "Good", "Average", "Poor", "Bad"]:
                sub_vals = [s["responses"].get(q_code, 3) for s in students if s["success"] == tier]
                tier_q_means[tier] = round(statistics.mean(sub_vals), 2) if sub_vals else 0

            question_analytics.append({
                "code": q_code,
                "number": q_num,
                "title": q_title,
                "domain": d_name,
                "domainCode": DOMAIN_SHORT_CODES[d_name],
                "mean": round(q_mean, 3),
                "std": round(q_std, 3),
                "variance": round(q_var, 3),
                "difficulty": difficulty_index,
                "discriminationDomain": item_disc_domain,
                "discriminationOverall": item_disc_overall,
                "frequency": freq_dist,
                "frequencyPct": freq_pct,
                "tierMeans": tier_q_means,
                "isNew": d_idx >= 12
            })

    # 5. Demographic Cohort Breakdowns
    demographic_analytics = {
        "byMajor": defaultdict(lambda: {"count": 0, "mean": [], "dropoutRisk": Counter(), "success": Counter()}),
        "byYear": defaultdict(lambda: {"count": 0, "mean": [], "dropoutRisk": Counter(), "success": Counter()}),
        "byGender": defaultdict(lambda: {"count": 0, "mean": [], "dropoutRisk": Counter(), "success": Counter()}),
        "byHousing": defaultdict(lambda: {"count": 0, "mean": [], "dropoutRisk": Counter(), "success": Counter()}),
        "byFirstGen": defaultdict(lambda: {"count": 0, "mean": [], "dropoutRisk": Counter(), "success": Counter()}),
        "byIncome": defaultdict(lambda: {"count": 0, "mean": [], "dropoutRisk": Counter(), "success": Counter()}),
        "byJobHours": defaultdict(lambda: {"count": 0, "mean": [], "dropoutRisk": Counter(), "success": Counter()})
    }

    for s in students:
        dm = s["demographics"]
        # Major
        m = dm["major"]
        demographic_analytics["byMajor"][m]["count"] += 1
        demographic_analytics["byMajor"][m]["mean"].append(s["overallMean"])
        demographic_analytics["byMajor"][m]["dropoutRisk"][s["dropoutRisk"]] += 1
        demographic_analytics["byMajor"][m]["success"][s["success"]] += 1

        # Year
        y = dm["academicYear"]
        demographic_analytics["byYear"][y]["count"] += 1
        demographic_analytics["byYear"][y]["mean"].append(s["overallMean"])
        demographic_analytics["byYear"][y]["dropoutRisk"][s["dropoutRisk"]] += 1
        demographic_analytics["byYear"][y]["success"][s["success"]] += 1

        # Gender
        g = dm["gender"]
        demographic_analytics["byGender"][g]["count"] += 1
        demographic_analytics["byGender"][g]["mean"].append(s["overallMean"])
        demographic_analytics["byGender"][g]["dropoutRisk"][s["dropoutRisk"]] += 1
        demographic_analytics["byGender"][g]["success"][s["success"]] += 1

        # Housing
        h = dm["housing"]
        demographic_analytics["byHousing"][h]["count"] += 1
        demographic_analytics["byHousing"][h]["mean"].append(s["overallMean"])
        demographic_analytics["byHousing"][h]["dropoutRisk"][s["dropoutRisk"]] += 1

        # FirstGen
        fg = dm["firstGen"]
        demographic_analytics["byFirstGen"][fg]["count"] += 1
        demographic_analytics["byFirstGen"][fg]["mean"].append(s["overallMean"])
        demographic_analytics["byFirstGen"][fg]["dropoutRisk"][s["dropoutRisk"]] += 1

        # Income
        inc = dm["incomeTier"]
        demographic_analytics["byIncome"][inc]["count"] += 1
        demographic_analytics["byIncome"][inc]["mean"].append(s["overallMean"])
        demographic_analytics["byIncome"][inc]["dropoutRisk"][s["dropoutRisk"]] += 1

        # Job Hours
        jh = dm["jobHours"]
        demographic_analytics["byJobHours"][jh]["count"] += 1
        demographic_analytics["byJobHours"][jh]["mean"].append(s["overallMean"])
        demographic_analytics["byJobHours"][jh]["dropoutRisk"][s["dropoutRisk"]] += 1

    # Format demographic aggregates for JSON
    formatted_demographics = {}
    for key, group in demographic_analytics.items():
        formatted_demographics[key] = []
        for cat, stats in group.items():
            formatted_demographics[key].append({
                "category": cat,
                "count": stats["count"],
                "mean": round(statistics.mean(stats["mean"]), 2),
                "dropoutLow": stats["dropoutRisk"]["Low"],
                "dropoutMed": stats["dropoutRisk"]["Medium"],
                "dropoutHigh": stats["dropoutRisk"]["High"],
                "successDistribution": dict(stats.get("success", {}))
            })

    # Compact student directory
    compact_students = []
    for s in students:
        compact_students.append({
            "id": s["id"],
            "success": s["success"],
            "risk": s["dropoutRisk"],
            "career": s["careerReadiness"],
            "mean": s["overallMean"],
            "scores": s["domainScores"],
            "demographics": s["demographics"],
            "diagnostics": s["diagnostics"],
            "counseling": s["counseling"]
        })

    payload = {
        "metadata": {
            "title": "Expanded Student Assessment, 17-Domain Psychometrics & Demographic Analytics",
            "totalStudents": total_students,
            "totalDomains": len(DOMAINS_17),
            "totalQuestions": 255,
            "totalDataPoints": total_students * 255,
            "generatedAt": "2026-08-22"
        },
        "kpis": {
            "totalStudents": total_students,
            "overallMean": round(overall_mean, 3),
            "overallMedian": round(overall_median, 3),
            "overallStd": round(overall_std, 3),
            "overallMin": round(overall_min, 3),
            "overallMax": round(overall_max, 3),
            "overallQ1": round(overall_q1, 3),
            "overallQ3": round(overall_q3, 3),
            "successCounts": dict(success_counts),
            "dropoutCounts": dict(dropout_counts),
            "careerCounts": dict(career_counts),
            "overallHist": {
                "labels": hist_labels,
                "counts": hist_counts
            }
        },
        "diagnosticsSummary": diag_summary,
        "domains": domain_analytics,
        "domainNames": DOMAINS_17,
        "domainCodes": [DOMAIN_SHORT_CODES[d] for d in DOMAINS_17],
        "correlationMatrix": corr_matrix,
        "domainOverallCorr": domain_overall_corr,
        "questions": question_analytics,
        "demographics": formatted_demographics,
        "students": compact_students,
        "sampleFullStudents": students[:250]
    }

    print(f"Writing {OUTPUT_JSON}...")
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"Writing {OUTPUT_JS}...")
    with open(OUTPUT_JS, "w", encoding="utf-8") as f:
        f.write("window.DASHBOARD_DATA = ")
        json.dump(payload, f)
        f.write(";\n")

    print("17-Domain & 255-Question Psychometrics & Demographic analysis complete!")

if __name__ == "__main__":
    main()
