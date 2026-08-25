#!/usr/bin/env python3
"""
Dataset Expansion & Demographic Synthesizer
Expands Balanced_Synthetic_Student_Dataset.csv from 12 domains (180 questions) to 17 domains (255 questions)
Adds 13 demographic attributes per student with psychometrically consistent covariance.
Outputs: Expanded_Synthetic_Student_Dataset.csv
"""

import csv
import math
import random
import statistics

SOURCE_CSV = "Balanced_Synthetic_Student_Dataset.csv"
TARGET_CSV = "Expanded_Synthetic_Student_Dataset.csv"

# Set deterministic seed
random.seed(42)

NEW_DOMAINS = [
    "Financial & Socioeconomic Well-Being",
    "Campus Belonging & Peer Support",
    "Neurodiversity, ADHD & Executive Functioning",
    "Screen Time, Blue Light & Digital Well-Being",
    "LMS Usability & Hybrid Learning"
]

MAJORS = [
    "Computer Science & AI",
    "Data Science & Analytics",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Business & Finance",
    "Biomedical & Health Sciences",
    "Psychology & Behavioural Science",
    "Arts & Humanities"
]

def sample_likert(base_score, noise_std=0.65):
    """Generates an integer response between 1 and 5 correlated with base_score."""
    val = random.gauss(base_score, noise_std)
    return max(1, min(5, int(round(val))))

def main():
    print(f"Reading {SOURCE_CSV}...")
    with open(SOURCE_CSV, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        original_rows = list(reader)

    total_students = len(original_rows)
    print(f"Processing {total_students} students...")

    expanded_rows = []

    for idx, r in enumerate(original_rows):
        student_id = f"STU-{idx+1:04d}"
        success = r["Student_Success"]
        overall_mean_12 = float(r["Overall_Mean"])

        # Domain anchors
        am = float(r["Academic Motivation"])
        lb = float(r["Learning Behaviour"])
        tm = float(r["Time Management"])
        ei = float(r["Emotional Intelligence"])
        paw = float(r["Physical Activity & Wellness"])
        cs = float(r["Communication Skills"])
        lt = float(r["Leadership & Teamwork"])
        dl = float(r["Digital Literacy & AI Readiness"])
        ra = float(r["Resilience & Adaptability"])

        # Demographic synthesis with realistic covariate relationships
        # 1. Socioeconomic Tier
        se_rand = random.random()
        if se_rand < 0.18:
            income_tier = "Low Income"
            fin_anchor = 2.3 + (overall_mean_12 - 3.0) * 0.4
        elif se_rand < 0.40:
            income_tier = "Lower Middle"
            fin_anchor = 2.7 + (overall_mean_12 - 3.0) * 0.4
        elif se_rand < 0.72:
            income_tier = "Middle Class"
            fin_anchor = 3.1 + (overall_mean_12 - 3.0) * 0.4
        elif se_rand < 0.92:
            income_tier = "Upper Middle"
            fin_anchor = 3.5 + (overall_mean_12 - 3.0) * 0.3
        else:
            income_tier = "High Income"
            fin_anchor = 3.9 + (overall_mean_12 - 3.0) * 0.3

        # 2. Part-Time Job Hours
        if income_tier in ["Low Income", "Lower Middle"]:
            job_hours = random.choices(["0 hrs/week", "1-10 hrs/week", "11-20 hrs/week", "20+ hrs/week"], weights=[0.15, 0.25, 0.40, 0.20])[0]
        else:
            job_hours = random.choices(["0 hrs/week", "1-10 hrs/week", "11-20 hrs/week", "20+ hrs/week"], weights=[0.55, 0.25, 0.15, 0.05])[0]

        # 3. First Gen Student
        first_gen = "Yes" if (income_tier in ["Low Income", "Lower Middle"] and random.random() < 0.48) or (random.random() < 0.15) else "No"

        # 4. International Student
        intl_student = "Yes" if random.random() < 0.14 else "No"

        # 5. Gender
        g_rand = random.random()
        gender = "Female" if g_rand < 0.49 else ("Male" if g_rand < 0.95 else "Non-Binary")

        # 6. Academic Year & Age
        year = random.choices(["Freshman", "Sophomore", "Junior", "Senior", "Graduate"], weights=[0.28, 0.26, 0.24, 0.18, 0.04])[0]
        if year == "Freshman": age = random.choices([18, 19], weights=[0.8, 0.2])[0]
        elif year == "Sophomore": age = random.choices([19, 20], weights=[0.75, 0.25])[0]
        elif year == "Junior": age = random.choices([20, 21], weights=[0.75, 0.25])[0]
        elif year == "Senior": age = random.choices([21, 22, 23], weights=[0.7, 0.2, 0.1])[0]
        else: age = random.randint(23, 27)

        # 7. Department / Major
        major = random.choice(MAJORS)

        # 8. Enrollment Status
        enrollment = "Part-Time" if job_hours == "20+ hrs/week" and random.random() < 0.45 else "Full-Time"

        # 9. Housing Type
        if year == "Freshman":
            housing = random.choices(["On-Campus Dormitory", "Off-Campus Apartment", "Commuter / Family Home"], weights=[0.72, 0.10, 0.18])[0]
        elif year in ["Sophomore", "Junior"]:
            housing = random.choices(["On-Campus Dormitory", "Off-Campus Apartment", "Commuter / Family Home"], weights=[0.35, 0.45, 0.20])[0]
        else:
            housing = random.choices(["On-Campus Dormitory", "Off-Campus Apartment", "Commuter / Family Home"], weights=[0.15, 0.65, 0.20])[0]

        # 10. Prior GPA & Attendance Rate
        base_gpa = 2.0 + (overall_mean_12 / 5.0) * 1.95 + random.gauss(0, 0.1)
        prior_gpa = round(max(2.10, min(4.00, base_gpa)), 2)

        base_att = 68.0 + (overall_mean_12 / 5.0) * 30.0 + random.gauss(0, 2.5)
        attendance_pct = round(max(60.0, min(99.5, base_att)), 1)

        # --- Generate 75 New Questions for the 5 Proposed Domains (15 items each) ---
        new_q_dict = {}

        # Domain 13: Financial Well-Being (Q181 - Q195)
        # Driven by fin_anchor + resilience
        d13_base = max(1.8, min(4.5, 0.7 * fin_anchor + 0.3 * ra))
        d13_items = [sample_likert(d13_base) for _ in range(15)]
        for i, val in enumerate(d13_items):
            new_q_dict[f"Q{181+i:03d}"] = str(val)
        d13_score = round(statistics.mean(d13_items), 3)

        # Domain 14: Campus Belonging & Peer Support (Q196 - Q210)
        # Driven by Leadership, Communication, Housing
        housing_bonus = 0.25 if housing == "On-Campus Dormitory" else (-0.15 if housing == "Commuter / Family Home" else 0.0)
        first_gen_penalty = -0.15 if first_gen == "Yes" else 0.05
        d14_base = max(1.8, min(4.5, 0.45 * lt + 0.35 * cs + 0.2 * ei + housing_bonus + first_gen_penalty))
        d14_items = [sample_likert(d14_base) for _ in range(15)]
        for i, val in enumerate(d14_items):
            new_q_dict[f"Q{196+i:03d}"] = str(val)
        d14_score = round(statistics.mean(d14_items), 3)

        # Domain 15: Neurodiversity, ADHD & Executive Functioning (Q211 - Q225)
        # Driven by Time Management, Learning Behaviour, Emotional Regulation
        d15_base = max(1.8, min(4.5, 0.5 * tm + 0.3 * lb + 0.2 * am))
        d15_items = [sample_likert(d15_base) for _ in range(15)]
        for i, val in enumerate(d15_items):
            new_q_dict[f"Q{211+i:03d}"] = str(val)
        d15_score = round(statistics.mean(d15_items), 3)

        # Domain 16: Screen Time, Blue Light & Digital Well-Being (Q226 - Q240)
        # Driven by Physical Wellness, Digital Literacy
        d16_base = max(1.8, min(4.5, 0.55 * paw + 0.30 * dl + 0.15 * ra))
        d16_items = [sample_likert(d16_base) for _ in range(15)]
        for i, val in enumerate(d16_items):
            new_q_dict[f"Q{226+i:03d}"] = str(val)
        d16_score = round(statistics.mean(d16_items), 3)

        # Domain 17: LMS Usability & Hybrid Learning (Q241 - Q255)
        # Driven by Learning Behaviour, Digital Literacy, Academic Motivation
        d17_base = max(1.8, min(4.5, 0.45 * dl + 0.35 * lb + 0.20 * am))
        d17_items = [sample_likert(d17_base) for _ in range(15)]
        for i, val in enumerate(d17_items):
            new_q_dict[f"Q{241+i:03d}"] = str(val)
        d17_score = round(statistics.mean(d17_items), 3)

        # Compute 17-Domain Combined Mean
        all_17_domain_scores = [
            float(r["Academic Motivation"]), float(r["Learning Behaviour"]), float(r["Time Management"]),
            float(r["Emotional Intelligence"]), float(r["Physical Activity & Wellness"]), float(r["Communication Skills"]),
            float(r["Leadership & Teamwork"]), float(r["Critical Thinking & Decision Making"]), float(r["Career Readiness"]),
            float(r["Digital Literacy & AI Readiness"]), float(r["Creativity & Innovation"]), float(r["Resilience & Adaptability"]),
            d13_score, d14_score, d15_score, d16_score, d17_score
        ]
        overall_mean_17 = round(statistics.mean(all_17_domain_scores), 3)

        # Construct new row
        new_row = {}
        # Demographics first
        new_row["Student_ID"] = student_id
        new_row["Gender"] = gender
        new_row["Age"] = str(age)
        new_row["Academic_Year"] = year
        new_row["Department_Major"] = major
        new_row["Enrollment_Status"] = enrollment
        new_row["Housing_Type"] = housing
        new_row["First_Gen_Student"] = first_gen
        new_row["International_Student"] = intl_student
        new_row["Socioeconomic_Tier"] = income_tier
        new_row["Part_Time_Job_Hours"] = job_hours
        new_row["Attendance_Rate_Pct"] = str(attendance_pct)
        new_row["Prior_GPA"] = str(prior_gpa)

        # Copy original Q001 - Q180
        for q_num in range(1, 181):
            q_code = f"Q{q_num:03d}"
            new_row[q_code] = r[q_code]

        # Add new Q181 - Q255
        for q_num in range(181, 256):
            q_code = f"Q{q_num:03d}"
            new_row[q_code] = new_q_dict[q_code]

        # Copy original 12 domains
        for d in [
            "Academic Motivation", "Learning Behaviour", "Time Management", "Emotional Intelligence",
            "Physical Activity & Wellness", "Communication Skills", "Leadership & Teamwork",
            "Critical Thinking & Decision Making", "Career Readiness", "Digital Literacy & AI Readiness",
            "Creativity & Innovation", "Resilience & Adaptability"
        ]:
            new_row[d] = r[d]

        # Add 5 new domains
        new_row["Financial & Socioeconomic Well-Being"] = str(d13_score)
        new_row["Campus Belonging & Peer Support"] = str(d14_score)
        new_row["Neurodiversity, ADHD & Executive Functioning"] = str(d15_score)
        new_row["Screen Time, Blue Light & Digital Well-Being"] = str(d16_score)
        new_row["LMS Usability & Hybrid Learning"] = str(d17_score)

        # Overall Means & Classifications
        new_row["Overall_Mean_12"] = str(overall_mean_12)
        new_row["Overall_Mean_17"] = str(overall_mean_17)
        new_row["Overall_Mean"] = str(overall_mean_17)
        new_row["Dropout_Risk_Low"] = r["Dropout_Risk_Low"]
        new_row["Dropout_Risk_Medium"] = r["Dropout_Risk_Medium"]
        new_row["Career_Readiness_Highly Ready"] = r["Career_Readiness_Highly Ready"]
        new_row["Career_Readiness_Not Ready"] = r["Career_Readiness_Not Ready"]
        new_row["Career_Readiness_Ready"] = r["Career_Readiness_Ready"]
        new_row["Student_Success"] = success

        expanded_rows.append(new_row)

    # Save to Expanded_Synthetic_Student_Dataset.csv
    print(f"Writing {TARGET_CSV}...")
    headers = list(expanded_rows[0].keys())
    with open(TARGET_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(expanded_rows)

    print(f"Successfully generated {TARGET_CSV} with {len(headers)} columns across {len(expanded_rows)} students!")

if __name__ == "__main__":
    main()
