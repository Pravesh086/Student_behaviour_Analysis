# AcuLearn AI Technical Manual: Survey Questionnaire, Domains, Conversion Scales & Soft Computing Fuzzy Rules

**Empirical Dataset Provenance:** `Master_Dataset_Clean.xlsx` ($N = 2,000$ Undergraduate Engineering Cohort)  
**Candidate:** Pravesh Kumar Bansal (Registration No.: 2019RCP9557, Student ID: 20804007)  
**Supervisor:** Dr. Mushtaq Ahmed, Associate Professor and Head, Department of CSE, MNIT Jaipur  
**Date:** November 2026  

---

## 1. Executive Overview & Theoretical Foundations

Contemporary Educational Data Mining (EDM) and Learning Analytics (LA) algorithms overwhelmingly rely on historical registrar metrics (Class 10th/12th marks, standardized entrance test ranks) and Virtual Learning Environment (VLE/LMS) clickstream logs. However, empirical investigations confirm that entrance exam ranks exhibit an extremely weak correlation with longitudinal college retention ($r = 0.12 - 0.18$). Entrance coaching trains students in single-timepoint analytical problem-solving under strict external surveillance; it is entirely blind to the latent non-cognitive behavioral traits—such as self-regulated time management, parental pressure resilience, nocturnal screen discipline, mess food adaptation, and peer help-seeking—that govern daily collegiate survival.

Furthermore, conventional early warning systems suffer from **post-mortem prediction latency**: they trigger flags only in Weeks 10 to 14 of the semester after mid-term examinations have already failed and grade point averages (CGPA) have collapsed. To provide a proactive, Day-1 intake assessment, this doctoral research engineered and administered the 125-feature diagnostic instrument embodied in `Master_Dataset_Clean.xlsx` across $N = 2,000$ undergraduate engineering students at Malaviya National Institute of Technology (MNIT) Jaipur and affiliated technical institutions.

## 2. Experimental Cohort Provenance & Survey Parameters

| Parameter | Specification | Institutional / Clinical Rationale |
| :--- | :--- | :--- |
| **Sample Size** | **$N = 2,000$ Students** | Full-time undergraduate engineering students across 125 clean variables. |
| **Gender Distribution** | **72.1% Male ($n = 1,442$)**, **27.9% Female ($n = 558$)** | Accurately reflects empirical gender distributions in Indian technical universities. |
| **Residential Status** | **56.9% Hostelers ($n = 1,138$)**, **43.1% Day Scholars ($n = 862$)** | Enables comparative modeling of residential transition shocks and mess food adaptation. |
| **Discipline Coverage** | CSE, AI/DS, ECE, EE, ME, Civil Engineering | Generalizes across theoretical, computational, and laboratory branches. |
| **Longitudinal Scope** | Semester 1 to Semester 8 | Deep tracking into junior and senior years (Semesters 5, 6, 7). |
| **Response Scale** | 5-Point Likert Scale ($1 = \text{Strongly Disagree}$ to $5 = \text{Strongly Agree}$) | Standardized psychometric measurement format. |
| **Intake Window** | Day 1 / Week 0 (Freshman Orientation Week) | Upstream intake before academic difficulties or probation manifest. |
| **Ethical Standards** | DPDP Act 2023 (India), IEEE P7000, ACM Code of Ethics | 100% voluntary consent, client-side SHA-256 de-identification, zero academic penalty. |

## 3. The 12-Domain Functional Taxonomy

1. **Administrative & Audit Identifiers (Cols 1–7, 17–18):** Primary keys, timestamps, decoupled hashes.
2. **Socio-Demographics & Parental Capital (Cols 8–13, 19):** Gender, family income, paternal education/occupation, hometown.
3. **Prior Academic Ability & History (Cols 14–16, 21–22):** Branch, current semester, CGPA, 10th % and 12th % board marks.
4. **Residential Transition & Campus Adaptation (Cols 20, 71, 73–74, 94–103):** Hosteler status, homesickness, mess food adaptation, institutional rejection.
5. **Sports, Physical Health & Somatic Vitality (Cols 23–32, 63–70, 72):** Somatic exercise, physical energy, fatigue, burnout resistance.
6. **Academic Motivation & Career Commitment (Cols 33–42):** Forced enrollment, intrinsic passion, engineering identity.
7. **Study Habits, Metacognition & Procrastination (Cols 43–48, 91, 93):** Schedule formulation, imposter syndrome, semester delay.
8. **Self-Esteem & Social Confidence (Cols 49–52):** Social confidence, resilience against failure, challenge tolerance.
9. **Peer Dynamics & Social Influence (Cols 53–62, 92):** Peer study support vs toxic peer distraction, pressure, blame projection.
10. **Family Pressure & Parental Expectations (Cols 76–85):** Perfectionist demands, comparative criticism, emotional estrangement.
11. **Maladaptive Habits & Addiction Impact (Cols 86–90):** Late-night partying, harmful routines, response to counseling.
12. **Smartphone & Social Media Digital Addiction (Cols 104–116):** Compulsive screen scrolling, in-class phone use, withdrawal anxiety.
13. **Clinical Depressive Screening & Somatic Distress (Cols 75, 117–125):** DSM-5 sleep disruption, vegetative appetite shifts, disorientation, acute crisis.

## 4. Complete Itemized Master Table of All 125 Columns

| Col # | Variable / Question Item Text | Domain | Polarity | Clinical & Retention Importance |
| :---: | :--- | :--- | :---: | :--- |
| 1 | Student_ID | Administrative | Neutral | Anonymized primary key ensuring research pseudonymization. |
| 2 | University | Administrative | Neutral | Institution name (MNIT Jaipur) establishing multi-campus provenance. |
| 3 | Timestamp | Administrative | Neutral | Time-tracking feature used to identify survey speed-traps (<8 min). |
| 4 | Username | Administrative | Neutral | Portal username, decoupled before model ingestion. |
| 5 | Total score | Administrative | Neutral | Raw platform intake verification score. |
| 6 | Name of the student | Administrative | Neutral | Student legal name, stripped via SHA-256 for DPDP Act 2023 compliance. |
| 7 | University Roll number | Administrative | Neutral | Institutional roll number, decoupled into cryptographic research ID. |
| 8 | Student Type | Demographics | Neutral | Programme tier verifying undergraduate engineering population. |
| 9 | Gender | Demographics | Immutable | Gender balance verification and multi-group fairness auditing. |
| 10 | Family Income | Demographics | Immutable | Family economic capital; indicates financial distress vulnerability. |
| 11 | Father Occupation | Demographics | Immutable | Paternal professional stability and parental occupation background. |
| 12 | Residential city and State | Demographics | Immutable | Hometown location; measures geographic displacement and relocation shock. |
| 13 | Fathers Highest Education | Demographics | Immutable | First-generation college status indicator (Bean & Metzner model). |
| 14 | Branch | Academic History | Immutable | Engineering branch; benchmarks discipline-specific workload pressures. |
| 15 | Current Semester | Academic History | Conditional | Longitudinal stage; distinguishes freshman transition from senior stress. |
| 16 | Current CGPA | Academic History | Output / Regress | Current CGPA ground truth for continuous trajectory prediction. |
| 17 | Emailid | Administrative | Neutral | Student contact channel for voluntary opt-in counseling alerts. |
| 18 | Contact Number | Administrative | Neutral | Emergency counselor escalation contact, strictly access-controlled. |
| 19 | Age | Demographics | Immutable | Chronological age; controls for gap years and coaching repetitions. |
| 20 | Are you Hosteler or not? | Transition | Actionable/Env | CRITICAL: Hosteler vs Day Scholar. Captures residential shock and mess diet. |
| 21 | Highschool (10th) percentage | Academic History | Immutable | Secondary school academic foundation and baseline aptitude. |
| 22 | 12th percentage | Academic History | Immutable | Senior secondary PCM board marks (shows weak r=0.14 correlation with retention). |
| 23 | Sports is equally important as academic subjects. | Sports & Vitality | Positive (+) | Somatic belief: measures valuation of physical balance alongside academics. |
| 24 | Sports should be a part of evaluation of grades in your academic result. | Sports & Vitality | Positive (+) | Institutional alignment: support for holistic grading vs pure rote tests. |
| 25 | You feel that if your favorite game is part of exam then you will top this exam? | Sports & Vitality | Positive (+) | Playfulness & passion: captures intrinsic energy and recreational drive. |
| 26 | You can play your favorite sports without any time bound? | Sports & Vitality | Positive (+) | Autonomous recreation: willingness to play without rigid schedule constraints. |
| 27 | You cannot assume your life without sports? | Sports & Vitality | Positive (+) | Recreational identity: sports as an essential non-negotiable life pillar. |
| 28 | Do you plan to continue participating in sports activities in the future? | Sports & Vitality | Positive (+) | Future somatic commitment: intent to sustain exercise throughout college. |
| 29 | Have you ever received encouragement or support from your peers or instructors to participate in sports activities? | Sports & Vitality | Positive (+) | Peer/faculty sports encouragement: social support for physical wellness. |
| 30 | How important do you think promoting sports culture is in educational institutions? | Sports & Vitality | Positive (+) | Institutional sports climate: perceived institutional focus on health. |
| 31 | rate your interest in participating in sports activities. | Sports & Vitality | Positive (+) | Self-rated sports enthusiasm: baseline recreational motivation level. |
| 32 | How often do you engage in sports activities? | Sports & Vitality | Positive (+) | Physical exercise frequency: concrete behavioral manifestation of fitness. |
| 33 | Your parents forcefully admitted you in the engineering? | Academic Motivation | Reverse (†) | CRITICAL: Parental coercion in engineering choice. Strongest early-dropout driver! |
| 34 | You don’t know why you are studying all these things and didn’t enjoy? | Academic Motivation | Reverse (†) | Academic anhedonia: lack of conceptual enjoyment and perceived study futility. |
| 35 | You want to get a job so that you can go in some another interest course? | Academic Motivation | Reverse (†) | Escapist career intent: viewing degree merely as a bridge to unrelated courses. |
| 36 | This course is your favorite. | Academic Motivation | Positive (+) | Intrinsic passion: genuine interest in the engineering curriculum. |
| 37 | You see your career in this field only? | Academic Motivation | Positive (+) | Long-term professional vision: commitment to engineering career trajectory. |
| 38 | The resources (labs, equipment, software) required for your engineering studies are easily accessible | Academic Motivation | Positive (+) | Perceived resource adequacy: lab equipment, computing, and software accessibility. |
| 39 | How often do you collaborate with peers on engineering projects or studies? | Academic Motivation | Positive (+) | Peer technical collaboration: active engagement in engineering project teams. |
| 40 | your instructors are supportive in guiding and encouraging your interest in engineering? | Academic Motivation | Positive (+) | Faculty mentorship support: accessibility of instructors for technical guidance. |
| 41 | You plan to pursue a career in engineering after graduation? | Academic Motivation | Positive (+) | Post-graduation engineering aspiration: persistence into technical industry. |
| 42 | You feel confident in identifying engineering problems and developing effective solutions? | Academic Motivation | Positive (+) | Engineering problem-solving self-efficacy: confidence in designing solutions. |
| 43 | You want to study but you don’t know where to start? | Study Habits | Reverse (†) | Executive dysfunction: cognitive paralysis on where to initiate study. |
| 44 | You don’t get interest in study because you think that whenever new semester will start then only you will study? | Study Habits | Reverse (†) | Chronic semester-delay rationalization: postponing study until next semester. |
| 45 | You feel that other students are very intelligent? | Study Habits | Reverse (†) | Imposter Syndrome: feeling peers are inherently superior/more intelligent. |
| 46 | In a semester so many times you make your schedule of study. | Study Habits | Positive (+) | Intention-action gap: repeated attempts to formulate study timetables. |
| 47 | After each semester you feel very guilty that you didn’t gave your 100%? | Study Habits | Reverse (†) | Post-semester guilt cycle: chronic regret over suboptimal effort investment. |
| 48 | You are confident in setting and achieving your personal and academic goals? | Study Habits | Positive (+) | Goal self-efficacy: confidence in setting and executing academic milestones. |
| 49 | You are   confident in social interactions with peers and instructors? | Self-Esteem | Positive (+) | Social self-efficacy: ease in interacting with professors and peer classmates. |
| 50 | rate your agreement with the statement: "I have high self-esteem." | Self-Esteem | Positive (+) | Global self-esteem: Rosenburg-style self-worth and intellectual confidence. |
| 51 | You have some past experiences (failures or successes) that influenced your current level of self-confidence? | Self-Esteem | Positive (+) | Attributional resilience: learning from past setbacks without ego collapse. |
| 52 | you are comfortable with trying new activities or taking on new challenges. | Self-Esteem | Positive (+) | Novelty challenge tolerance: comfort with new, open-ended technical tasks. |
| 53 | You believe in friendship very much? | Peer Dynamics | Positive (+) | Relational valuation: importance placed on collegiate peer friendships. |
| 54 | Your friends are same as you in each manner either in study or other things? | Peer Dynamics | Neutral | Peer homophily: perceived similarity with peer circle in study and values. |
| 55 | Your most of the time is spend with your friends? | Peer Dynamics | Neutral | Social immersion: volume of daily waking hours spent with friend group. |
| 56 | You want to spend your time with your friends only in vacations also? | Peer Dynamics | Neutral | Peer dependency: desire to remain with college friends during vacation. |
| 57 | Rate your agreement with the statement: "My friends have a positive influence on my academic and personal life." | Peer Dynamics | Positive (+) | Positive peer scaffolding: constructive influence on academic discipline. |
| 58 | How often do your friends distract you from your studies? | Peer Dynamics | Reverse (†) | Toxic peer distraction: friends actively pulling student away from study. |
| 59 | you feel pressured by your friends to engage in activities that you are uncomfortable with? | Peer Dynamics | Reverse (†) | Coercive peer pressure: feeling compelled to engage in uncomfortable acts. |
| 60 | the approval of your friends is important   in your decision-making process. | Peer Dynamics | Reverse (†) | External social approval dependency: inability to make independent choices. |
| 61 | do you participate in risky behaviors due to influence from friends? | Peer Dynamics | Reverse (†) | Peer-induced risk-taking: reckless behavior driven by social conformity. |
| 62 | you feel your friends impact your mental health? | Peer Dynamics | Reverse (†) | Relational mental strain: emotional distress and toxicity in peer group. |
| 63 | rate your agreement with the statement: "I am generally in good health." | Physical Health | Positive (+) | General physical health status: self-rated biological vitality baseline. |
| 64 | How does the quality and variety of food available to you impact your overall well-being in college? | Physical Health | Positive (+) | Campus nutritional adequacy: impact of mess food variety on well-being. |
| 65 | How often do you eat meals in the campus dining halls or other food facilities? | Physical Health | Positive (+) | Campus dining regularity: consistency of eating meals in hostel mess. |
| 66 | How often do you engage in physical activity or exercise? | Physical Health | Positive (+) | Routine physical exercise: frequency of cardiovascular workout/sports. |
| 67 | How would you rate your overall physical and mental health? | Physical Health | Positive (+) | Holistic health perception: combined physical and mental vitality score. |
| 68 | do you experience health-related issues that affect your daily activities? | Physical Health | Reverse (†) | Somatic disability: health ailments directly interfering with daily routine. |
| 69 | do health issues affect your academic performance? | Physical Health | Reverse (†) | Health-induced academic decline: medical issues causing low exam scores. |
| 70 | do you feel supported by friends, family, and instructors when dealing with health issues? | Physical Health | Positive (+) | Health support network: perceived care from family/friends during sickness. |
| 71 | You never like mess food? | Hostel Life | Reverse (†) | Mess food aversion: chronic dissatisfaction with campus residential dining. |
| 72 | All the time you feel very tired and lazy. | Hostel Life | Reverse (†) | Chronic fatigue syndrome: feeling lethargic, unrefreshed, and exhausted. |
| 73 | This environment doesn’t suit you. | Hostel Life | Reverse (†) | Environmental mismatch: feeling the collegiate institutional climate is toxic. |
| 74 | At home you are very energetic but not in college? | Hostel Life | Reverse (†) | Home-campus energy divergence: energetic at home but depleted at college. |
| 75 | You don’t get good sleep? | Hostel Life | Reverse (†) | Nocturnal sleep deficiency: inability to attain deep, restorative sleep. |
| 76 | Your parents always want you to improve more and never satisfies with your performance? | Family Pressure | Reverse (†) | Parental perfectionism: parents never satisfied with academic marks. |
| 77 | How satisfied are you with the resources available on campus for managing and coping with family pressure? | Family Pressure | Positive (+) | Campus coping resources: awareness of institutional counseling for stress. |
| 78 | How does Family stress or difficulty impact your academic performance and well-being? | Family Pressure | Reverse (†) | Family conflict spillover: domestic problems impairing concentration. |
| 79 | Your parents never motivate you like other parents? | Family Pressure | Reverse (†) | Comparative parental criticism: feeling parents compare student unfavorably. |
| 80 | Have you ever discussed this pressure with your family or anyone else for support? | Family Pressure | Positive (+) | Family emotional dialogue: willingness to discuss stress openly with parents. |
| 81 | You never achieve the expectations of your parents? | Family Pressure | Reverse (†) | Chronic failure feeling: perceived permanent inability to meet expectations. |
| 82 | You don’t want to talk your parents? | Family Pressure | Reverse (†) | CRITICAL: Parental emotional estrangement. Reluctance to speak to parents. |
| 83 | You think that your parents don’t support you like other parents do? | Family Pressure | Reverse (†) | Perceived lack of parental support: feeling isolated compared to peers. |
| 84 | do you feel your parents' aspirations influence your own life goals and ambitions? | Family Pressure | Neutral | Parental vicarious ambition: parental goals substituting personal drive. |
| 85 | rate your agreement with the statement: "I feel pressure from my family to meet certain expectations." | Family Pressure | Reverse (†) | Family expectation burden: acute pressure to attain high-paying placements. |
| 86 | rate your agreement with the statement: "I frequently engage in activities that I consider to be bad habits." | Maladaptive Habits | Reverse (†) | Self-acknowledged bad habits: engaging in addictive or harmful routines. |
| 87 | How effective have interventions (counseling, support groups, therapy) been in helping you manage or quit your bad habits? | Maladaptive Habits | Positive (+) | Therapeutic intervention efficacy: responsiveness to past counseling. |
| 88 | You enjoy the late-night parties with your friends? | Maladaptive Habits | Reverse (†) | Nocturnal partying: late-night escapism disrupting circadian rhythms. |
| 89 | How do you feel about the resources available on campus for addressing bad habits or addiction? | Maladaptive Habits | Positive (+) | Campus de-addiction awareness: perception of university counseling support. |
| 90 | How has your academic performance been impacted by any bad habits or addiction? | Maladaptive Habits | Reverse (†) | Habit-induced academic damage: performance collapse due to addictions. |
| 91 | Study is your first priority in exams. | Study Priorities | Positive (+) | Exam priority focus: placing academic study above social distractions. |
| 92 | If you get less score in exams, your friends are the main reason of your less score? | Study Priorities | Reverse (†) | External locus of control: blaming peer group for personal low marks. |
| 93 | Your daily routine is not fix? | Study Priorities | Reverse (†) | Circadian chaos: complete lack of structured daily study/sleep schedule. |
| 94 | rate your agreement with the statement: "I frequently feel homesick." | Homesickness | Reverse (†) | Acute homesickness frequency: persistent emotional pull toward home. |
| 95 | You visit home as often as you can? | Homesickness | Reverse (†) | Frequent home transit: fleeing campus on weekends, hurting study groups. |
| 96 | How satisfied are you with the resources available on campus for addressing homesickness? | Homesickness | Positive (+) | Campus transition support: satisfaction with institutional orientation. |
| 97 | How often do you stay in touch with family and friends from home? | Homesickness | Positive (+) | Home contact frequency: healthy communication with family support system. |
| 98 | You hardly ever think about home? | Homesickness | Positive (+) | Campus independence: emotional stability without compulsive home longing. |
| 99 | You call your family so many times during a day? | Homesickness | Reverse (†) | Compulsive parental calling: calling home multiple times daily due to anxiety. |
| 100 | You hate this place? | Homesickness | Reverse (†) | CRITICAL: Acute institutional rejection. Stating 'You hate this place'. |
| 101 | You are very excited when vocation is there? | Homesickness | Reverse (†) | Vacation fixation: mental disengagement from campus during semester. |
| 102 | How significantly does homesickness affect your mental health? | Homesickness | Reverse (†) | Homesickness psychological toll: homesickness inducing depressive affect. |
| 103 | How actively do you participate in campus activities to feel more connected? | Homesickness | Positive (+) | Campus activity engagement: participating in clubs to build belonging. |
| 104 | You spend so much time on your mobile? | Digital Addiction | Reverse (†) | Excessive screen time: compulsive hours spent on mobile devices. |
| 105 | your academic performance has been impacted by any Social media addiction? | Digital Addiction | Reverse (†) | Social media academic impairment: grades declining due to online apps. |
| 106 | Without any message also you scroll down the screen of your mobile for social media. | Digital Addiction | Reverse (†) | Phantom scrolling: mindlessly scrolling feeds even without notifications. |
| 107 | You cannot assume your life without social media sites or apps? | Digital Addiction | Reverse (†) | Digital dependency: expressing life is unimaginable without social apps. |
| 108 | Your friends comment on your photo or story matter for you a lot? | Digital Addiction | Reverse (†) | Social validation addiction: excessive anxiety over post likes/comments. |
| 109 | You share every happy and sad moment with your friends by posting? | Digital Addiction | Reverse (†) | Compulsive life broadcasting: sharing every emotional event online. |
| 110 | How significantly does your use of mobile phones or social media affect your physical health (e.g., eye strain, posture problems)? | Digital Addiction | Reverse (†) | Digital somatic toll: eye strain, neck posture, and physical discomfort. |
| 111 | rate your agreement with the statement: "My use of mobile phones or social media disrupts my daily life and activities." | Digital Addiction | Reverse (†) | Daily routine disruption: screen time delaying meals, study, and sleep. |
| 112 | How often does your use of mobile phones or social media negatively impact your academic performance? | Digital Addiction | Reverse (†) | Study distraction: social media interrupts homework and revision. |
| 113 | How significantly does your use of mobile phones or social media affect your productivity in academic or personal tasks? | Digital Addiction | Reverse (†) | Cognitive productivity decline: inability to sustain deep focused work. |
| 114 | Have you ever tried to reduce your use of mobile phones or social media? | Digital Addiction | Reverse (†) | Failed digital detox: attempted reduction of phone usage and failed. |
| 115 | How anxious do you feel when you are unable to access your mobile phone or social media? | Digital Addiction | Reverse (†) | Nomophobia & withdrawal: severe anxiety when mobile access is denied. |
| 116 | How often do you use your mobile phone or social media during classes or study sessions? | Digital Addiction | Reverse (†) | In-class digital distraction: using smartphone apps during live lectures. |
| 117 | Are you sleeping more or less then you normally sleep? | Clinical Screening | Reverse (†) | Sleep architecture disruption: insomnia or excessive vegetative hypersomnia. |
| 118 | Do you feel tired, no matter how much you sleep? | Clinical Screening | Reverse (†) | Unrefreshing sleep: persistent exhaustion regardless of sleep duration. |
| 119 | Are you enjoying the things right now happening in your life? | Clinical Screening | Positive (+) | Anhedonia marker: ability to experience joy in current daily events. |
| 120 | You don’t like interaction with anybody? | Clinical Screening | Reverse (†) | Social withdrawal & isolation: aversion to interacting with all humans. |
| 121 | Have you noticed any changes in your physical appearance, such as bloodshot eyes, unusual odors, or sudden weight loss or gain in the past month? | Clinical Screening | Reverse (†) | Somatic physical breakdown: bloodshot eyes, drastic weight fluctuations. |
| 122 | It is difficult for you to talk with your friends also. | Clinical Screening | Reverse (†) | Relational shutdown: inability to converse even with closest friends. |
| 123 | Have you noticed any changes in your sleeping patterns or appetite recently? | Clinical Screening | Reverse (†) | Vegetative somatic shifts: acute appetite loss or erratic circadian shifts. |
| 124 | Have you noticed any changes in your academic performance or behavior, such as missing classes or assignments, arriving late, or engaging in disruptive behavior in the past month? | Clinical Screening | Reverse (†) | Behavioral disinhibition: unexcused absenteeism, chronic late arrivals. |
| 125 | How often have you felt disoriented or confused in the past month? | Clinical Screening | Reverse (†) | CRITICAL: Cognitive disorientation, severe confusion, and acute crisis. |


## 5. Mathematical Conversion & Preprocessing Pipeline (How We Convert)

### Stage 1: Text-to-Integer Nominal Mapping
Raw textual responses from the web survey are mapped to ordinal integers:
- $\text{Strongly Disagree} \to 1$
- $\text{Disagree} \to 2$
- $\text{Neutral} / \text{Moderately True} \to 3$
- $\text{Agree} \to 4$
- $\text{Strongly Agree} \to 5$

### Stage 2: Reverse-Coding Inversion for Acquiescence Defense
To eliminate yea-saying acquiescence bias, approximately 22% of survey questions are negatively keyed ($†$). All negatively phrased items are mathematically inverted prior to parcel aggregation:

$$x_{\text{recoded}} = (k + 1) - x_{\text{raw}} = 6 - x_{\text{raw}}$$

*Example:* If a student responds **Strongly Agree** ($5$) to Col 33 (*"Your parents forcefully admitted you in engineering?"*), the recoded intrinsic motivation score becomes $6 - 5 = 1$ (Critically Depleted). Conversely, **Strongly Disagree** ($1$) recodes to $6 - 1 = 5$ (High Autonomous Motivation).

### Stage 3: Full Information Maximum Likelihood (FIML) Missing-Value Imputation
Rather than employing destructive listwise deletion, missing values are handled under Missing At Random (MAR) assumptions using FIML, preserving asymptotic covariance structure.

### Stage 4: Manifest Item Parceling & Standardization
To satisfy Kline's $5:1 - 10:1$ SEM sample-to-parameter ratio and prevent neural network overfitting, items are grouped into 51 balanced manifest parcels (3 balanced parcels per latent factor):

$$P_k = \frac{1}{|S_k|} \sum_{i \in S_k} x_{\text{recoded}, i}$$

Parcels are then standardized via z-score scaling: $z = (P_k - \mu_k)/\sigma_k$ and normalized to $[0, 1]$.

## 6. Soft Computing Fuzzy Perception Engine & Complete Rule Base

### Parameterized Membership Functions
Continuous parcel scores $x \in [1.0, 5.0]$ are mapped into three linguistic partitions: Low ($L$), Moderate ($M$), and High ($H$):

- $\mu_{\text{Low}}(x) = \text{Trap}(x; 0.0, 0.0, 1.5, 2.8)$
- $\mu_{\text{Mod}}(x) = \text{Tri}(x; 2.0, 3.2, 4.2)$
- $\mu_{\text{High}}(x) = \text{Trap}(x; 3.5, 4.4, 5.0, 5.0)$

This guarantees dual membership (e.g., $x = 2.4$ yields $\mu_{\text{Low}} = 0.35$ and $\mu_{\text{Mod}} = 0.65$), preserving graded truth values without crisp boundary error.

### Complete 27 Mamdani Fuzzy IF-THEN Rules Matrix

| Rule # | Study Habits (SH) | Affective Stability (AS) | Transition Factor (ET) | Inferred Risk (PAR) | Clinical Triage Action |
| :---: | :---: | :---: | :---: | :---: | :--- |
| R01 | Low | Low | Low | **Critical At-Risk** | Immediate Crisis Counseling |
| R02 | Low | Low | Moderate | **Critical At-Risk** | Immediate Crisis Counseling |
| R03 | Low | Low | High | **Elevated Hazard** | Faculty Mentor Intervention |
| R04 | Low | Moderate | Low | **Critical At-Risk** | Immediate Crisis Counseling |
| R05 | Low | Moderate | Moderate | **Elevated Hazard** | Faculty Mentor Intervention |
| R06 | Low | Moderate | High | **Elevated Hazard** | Faculty Mentor Intervention |
| R07 | Low | High | Low | **Elevated Hazard** | Faculty Mentor Intervention |
| R08 | Low | High | Moderate | **Elevated Hazard** | Faculty Mentor Intervention |
| R09 | Low | High | High | **Moderate Vulnerability** | Peer Study Group Scaffolding |
| R10 | Moderate | Low | Low | **Critical At-Risk** | Immediate Crisis Counseling |
| R11 | Moderate | Low | Moderate | **Elevated Hazard** | Faculty Mentor Intervention |
| R12 | Moderate | Low | High | **Elevated Hazard** | Faculty Mentor Intervention |
| R13 | Moderate | Moderate | Low | **Elevated Hazard** | Faculty Mentor Intervention |
| R14 | Moderate | Moderate | Moderate | **Elevated Hazard** | Faculty Mentor Intervention |
| R15 | Moderate | Moderate | High | **Moderate Vulnerability** | Peer Study Group Scaffolding |
| R16 | Moderate | High | Low | **Elevated Hazard** | Faculty Mentor Intervention |
| R17 | Moderate | High | Moderate | **Moderate Vulnerability** | Peer Study Group Scaffolding |
| R18 | Moderate | High | High | **Safe Retention Zone** | Routine Developmental Advising |
| R19 | High | Low | Low | **Elevated Hazard** | Faculty Mentor Intervention |
| R20 | High | Low | Moderate | **Elevated Hazard** | Faculty Mentor Intervention |
| R21 | High | Low | High | **Moderate Vulnerability** | Peer Study Group Scaffolding |
| R22 | High | Moderate | Low | **Elevated Hazard** | Faculty Mentor Intervention |
| R23 | High | Moderate | Moderate | **Moderate Vulnerability** | Peer Study Group Scaffolding |
| R24 | High | Moderate | High | **Safe Retention Zone** | Routine Developmental Advising |
| R25 | High | High | Low | **Moderate Vulnerability** | Peer Study Group Scaffolding |
| R26 | High | High | Moderate | **Safe Retention Zone** | Routine Developmental Advising |
| R27 | High | High | High | **Safe Retention Zone** | Routine Developmental Advising |


### Inference & Centroid Defuzzification
Conjunctive firing strength:

$$\alpha_r = \min\left( \mu_{\text{SH}, r}(x_{\text{SH}}), \mu_{\text{AS}, r}(x_{\text{AS}}), \mu_{\text{ET}, r}(x_{\text{ET}}) \right)$$

Aggregated fuzzy output hazard:

$$\mu_{\text{agg}}(y) = \max_{r=1..27} \left( \min( \alpha_r, \mu_{\text{Risk}, r}(y) ) \right)$$

Defuzzification to crisp risk probability $\text{PAR} \in [0.0, 1.0]$ via Center of Gravity (Centroid):

$$y^* = \frac{\int y \cdot \mu_{\text{agg}}(y) \, dy}{\int \mu_{\text{agg}}(y) \, dy}$$

### Differential Evolution (DE) Parameter Tuning
The objective function minimized the mean squared error against expert clinical psychologist evaluations across a calibration subset ($N = 80$):

$$\min_{\mathbf{\theta}} J(\mathbf{\theta}) = \frac{1}{N} \sum_{i=1}^N \left( y_i^{\text{expert}} - f_{\text{FIS}}(x_i; \mathbf{\theta}) \right)^2 + \gamma \|\mathbf{\theta} - \mathbf{\theta}_{\text{init}}\|_2^2$$

DE hyperparameters: Population $NP = 50$, Crossover rate $CR = 0.85$, Mutation factor $F = 0.6$, 150 generations. Converged to **97.2% clinical concordance** (published in *AIP Conf. Proc.*, 2025).

## 7. Multi-Layer Bias Elimination & Quality Control

1. **Acquiescence Bias:** Eliminated via 22.2% negatively keyed items ($†$) inverted via $x_{\text{recoded}} = 6 - x_{\text{raw}}$.
2. **Inattention & Speed Traps:** Five bogus attention-verification checks; submissions $< 8$ minutes quarantined ($n = 14$ pruned).
3. **Social Desirability Bias:** Client-side SHA-256 pseudonymization and non-punitive safe-harbor consent (zero grade penalty).
4. **Common Method Variance (CMV):** Harman's single-factor test reveals first factor explains only **22.1% variance** ($< 50\%$ threshold).
5. **Subjective Linguistic Noise:** Soft fuzzy membership partitions absorb semantic fuzziness.
6. **Demographic Fairness:** Multi-group CFA establishes configural, metric, and scalar invariance across gender and social categories ($\Delta\text{CFI} < 0.010, \Delta\text{RMSEA} < 0.015$).
