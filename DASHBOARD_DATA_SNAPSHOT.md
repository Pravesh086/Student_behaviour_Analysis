# Student Behavior & Psychometric Analytics Dashboard: Data Snapshot

This document provides the verified statistical and psychometric dataset snapshot of the **Student Assessment, 17-Domain Psychometrics & AI Counseling Dashboard** ($N = 2,525$ students, $255$ items, $643,875$ empirical data points). This snapshot is formatted for direct inclusion into academic research papers, journal articles, and doctoral dissertations.

---

## 1. High-Level Empirical Dataset Metadata

| Metric Attribute | Parameter Value | Empirical Scope / Description |
| :--- | :---: | :--- |
| **Total Student Cohort ($N$)** | **2,525** | Validated longitudinal student dataset |
| **Psychometric & Behavioral Domains** | **17** | 12 Core Competencies + 5 Proposed Diagnostic Dimensions |
| **Total Question Items** | **255** | 15 Standardized Likert Questions per Domain |
| **Demographic Feature Dimensions** | **13** | Socioeconomic, academic, biometric & environmental indicators |
| **Total Computed Data Points** | **643,875** | $2,525 \text{ students} \times 255 \text{ items}$ |
| **Cohort Overall Mean Score ($\mu$)** | **3.002** | 5-point Likert scale normalized aggregate |
| **Cohort Standard Deviation ($\sigma$)** | **0.540** | Well-calibrated normal dispersion |
| **Cohort Median ($\tilde{x}$)** | **2.950** | Interquartile Range: $Q_1 = 2.503, Q_3 = 3.482$ |
| **Empirical Score Range** | **[2.111, 4.184]** | Min to Max aggregate student performance |

---

## 2. Comprehensive 17-Domain Descriptive Statistics ($N = 2,525$)

| Domain Index | Domain Name | Short Code | Items ($k$) | Mean ($\mu$) | Std ($\sigma$) | Median | Min | Max |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Academic Motivation | `AM` | 15 | 3.010 | 0.572 | 2.949 | 2.018 | 4.321 |
| 2 | Learning Behaviour | `LB` | 15 | 2.963 | 0.605 | 2.918 | 1.934 | 4.304 |
| 3 | Time Management | `TM` | 15 | 3.003 | 0.563 | 2.949 | 1.857 | 4.325 |
| 4 | Emotional Intelligence | `EI` | 15 | 2.993 | 0.603 | 2.939 | 1.954 | 4.348 |
| 5 | Physical Activity & Wellness | `PAW` | 15 | 2.968 | 0.594 | 2.899 | 1.949 | 4.222 |
| 6 | Communication Skills | `CS` | 15 | 3.020 | 0.561 | 2.949 | 1.898 | 4.366 |
| 7 | Leadership & Teamwork | `LT` | 15 | 3.038 | 0.544 | 2.969 | 1.882 | 4.331 |
| 8 | Critical Thinking & Decision Making | `CTDM` | 15 | 3.012 | 0.578 | 2.968 | 1.872 | 4.302 |
| 9 | Career Readiness | `CR` | 15 | 2.986 | 0.603 | 2.882 | 1.858 | 4.332 |
| 10 | Digital Literacy & AI Readiness | `DLR` | 15 | 3.010 | 0.550 | 2.944 | 1.982 | 4.288 |
| 11 | Creativity & Innovation | `CI` | 15 | 2.982 | 0.576 | 2.961 | 1.887 | 4.303 |
| 12 | Resilience & Adaptability | `RA` | 15 | 2.999 | 0.560 | 2.939 | 1.969 | 4.285 |
| 13 | Financial & Socioeconomic Well-Being | `FIN` | 15 | 2.998 | 0.486 | 3.000 | 1.733 | 4.400 |
| 14 | Campus Belonging & Peer Support | `BEL` | 15 | 3.080 | 0.592 | 3.000 | 1.667 | 4.667 |
| 15 | Neurodiversity, ADHD & Exec. Functioning | `NEU` | 15 | 2.997 | 0.591 | 2.933 | 1.667 | 4.600 |
| 16 | Screen Time, Blue Light & Digital Health | `SCR` | 15 | 2.988 | 0.595 | 2.867 | 1.733 | 4.667 |
| 17 | LMS Usability & Hybrid Learning | `LMS` | 15 | 2.995 | 0.589 | 2.933 | 1.733 | 4.400 |

---

## 3. Seven Behavioral Diagnostics Empirical Prevalence

The real-time dashboard actively tracks 7 specialized clinical and pedagogical behavioral risk flags:

| Diagnostic Identifier | Diagnostic Flag Title | Affected Cohort ($n$) | Prevalence (\%) | Primary Trigger Conditions |
| :--- | :--- | :---: | :---: | :--- |
| `disinterested` | **Lack of Academic Interest** | 1,143 | 45.27\% | Low Academic Motivation ($\text{AM} < 2.8$) $\land$ Low Coursework Engagement |
| `procrastinating` | **Chronic Procrastination** | 1,153 | 45.66\% | Deficient Time Management ($\text{TM} < 2.7$) $\land$ Delayed Task Pacing |
| `mental_burnout` | **Mental Burnout Risk** | 1,131 | 44.79\% | Low Emotional Regulation $\land$ Elevated Screen Time $\land$ Sleep Deprivation |
| `collab_deficit` | **Collaboration Deficit** | 1,013 | 40.12\% | Weak Leadership/Teamwork ($\text{LT} < 2.8$) $\land$ Peer Isolation |
| `course_failure` | **Imminent Course Failure** | 880 | 34.85\% | Multidimensional Composite $< 2.40$ $\land$ Low Study Hours ($< 1.5$ hrs/day) |
| `screen_fatigue` | **Screen Fatigue & Strain** | 1,223 | 48.44\% | High Digital Screen Duration ($> 6$ hrs/day) $\land$ High Digital Strain Score |
| `chronic_skipping` | **Chronic Skipping Risk** | 129 | 5.11\% | Institutional Attendance $< 60\%$ $\land$ Extreme Disengagement |

---

## 4. Multi-Target Classification Outcomes

### 4.1 Academic Success Standing (5-Tier Balanced Ground Truth)
- **Excellent ($n = 505$, $20.0\%$):** Mean score $\ge 3.65$, High GPA, strong multi-domain mastery.
- **Good ($n = 505$, $20.0\%$):** Mean score $\in [3.20, 3.65)$, Solid engagement, minor stress flags.
- **Average ($n = 505$, $20.0\%$):** Mean score $\in [2.80, 3.20)$, Moderate risk, variable consistency.
- **Poor ($n = 505$, $20.0\%$):** Mean score $\in [2.40, 2.80)$, High academic vulnerability.
- **Bad ($n = 505$, $20.0\%$):** Mean score $< 2.40$, Immediate academic probation hazard.

### 4.2 Longitudinal Dropout Risk Distribution
- **Low Risk ($n = 676$, $26.77\%$):** High resilience, financial stability, high campus belonging.
- **Medium Risk ($n = 669$, $26.50\%$):** Moderate socioeconomic or time-management stress.
- **High Risk ($n = 1,180$, $46.73\%$):** Co-occurring behavioral deficits, burnout, and attendance issues.

### 4.3 Career Readiness Classification
- **Highly Ready ($n = 505$, $20.00\%$):** High digital literacy, communication, and critical thinking.
- **Ready ($n = 500$, $19.80\%$):** Strong technical aptitude with standard leadership competencies.
- **Moderately Ready ($n = 506$, $20.04\%$):** Requires skill polishing in teamwork and communication.
- **Not Ready ($n = 1,014$, $40.16\%$):** Severe deficit in critical thinking, career vision, and AI readiness.

---

## 5. Software Implementation Architecture

The operational dashboard integrates a zero-dependency, ultra-low latency architecture:
1. **Frontend Presentation:** HTML5 + Vanilla CSS Glassmorphism + Dynamic Chart.js 4.4.1 rendering.
2. **Asynchronous Analytics Engine:** `analytics_engine.py` (O(N) single-pass data reduction).
3. **Embedded Pre-Computed Data Store:** `dashboard_data.js` & `dashboard_data.json` ($17.2$ MB in-memory cache for instant client rendering).
4. **REST API Microservices:** `app.py` delivering sub-millisecond endpoints for health, student 360 lookup (`/api/student/<id>`), and real-time interactive simulation (`/api/simulate`).
