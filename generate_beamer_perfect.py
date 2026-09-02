import os
import subprocess

def main():
    tex_content = r"""\documentclass[aspectratio=169,10pt]{beamer}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{tcolorbox}
\usepackage{tikz}
\usepackage{hyperref}
\usepackage{array}
\usepackage{adjustbox}

% -----------------------------------------------------------------------------
% HIGH-CONTRAST PROFESSIONAL COLOR PALETTE (Clean Light Theme)
% -----------------------------------------------------------------------------
\definecolor{navyhead}{RGB}{15, 23, 42}
\definecolor{subhead}{RGB}{67, 56, 202}
\definecolor{textdark}{RGB}{15, 23, 42}
\definecolor{textmuted}{RGB}{71, 85, 105}
\definecolor{canvasbg}{RGB}{250, 251, 252}
\definecolor{cardbg}{RGB}{30, 41, 59}

% Semantic Block Colors (High Contrast)
\definecolor{whyframe}{RGB}{185, 28, 28}
\definecolor{whybg}{RGB}{254, 242, 242}
\definecolor{howframe}{RGB}{3, 105, 161}
\definecolor{howbg}{RGB}{240, 249, 255}
\definecolor{outframe}{RGB}{4, 120, 87}
\definecolor{outbg}{RGB}{236, 253, 245}
\definecolor{neutralframe}{RGB}{99, 102, 241}
\definecolor{neutralbg}{RGB}{238, 242, 255}

% Beamer Color Assignments
\setbeamercolor{background canvas}{bg=canvasbg}
\setbeamercolor{normal text}{fg=textdark}
\setbeamercolor{title}{fg=white}
\setbeamercolor{subtitle}{fg=white}
\setbeamercolor{frametitle}{fg=white,bg=navyhead}
\setbeamercolor{structure}{fg=subhead}
\setbeamercolor{item}{fg=subhead}

\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{
  \leavevmode%
  \hbox{%
  \begin{beamercolorbox}[wd=.5\paperwidth,ht=2.5ex,dp=1.1ex,left]{author in head/foot}%
    \hspace*{2ex}\textcolor{textmuted}{\scriptsize\textbf{AcuLearn AI} $\bullet$ Student Analytics \& Decision-Support System}
  \end{beamercolorbox}%
  \begin{beamercolorbox}[wd=.5\paperwidth,ht=2.5ex,dp=1.1ex,right]{title in head/foot}%
    \textcolor{textmuted}{\scriptsize Slide \insertframenumber{} / \inserttotalframenumber}\hspace*{2ex}
  \end{beamercolorbox}}%
  \vskip0pt%
}

% Reusable TColorBox Styles with High-Contrast White Titles
\tcbset{
    boxrule=1.2pt,
    arc=4pt,
    left=5pt,right=5pt,top=3pt,bottom=3pt,
    coltitle=white,
    fonttitle=\bfseries\footnotesize
}

\newcommand{\whybox}[2]{
  \begin{tcolorbox}[colframe=whyframe,colbacktitle=whyframe,colback=whybg,title=\textbf{WHY? The Problem \& Need (#1)}]
  \scriptsize #2
  \end{tcolorbox}
}

\newcommand{\howbox}[2]{
  \begin{tcolorbox}[colframe=howframe,colbacktitle=howframe,colback=howbg,title=\textbf{HOW? The Technology \& Algorithms (#1)}]
  \scriptsize #2
  \end{tcolorbox}
}

\newcommand{\outbox}[2]{
  \begin{tcolorbox}[colframe=outframe,colbacktitle=outframe,colback=outbg,title=\textbf{OUTCOMES? Measurable Impact \& Results (#1)}]
  \scriptsize #2
  \end{tcolorbox}
}

\title{\textbf{\Huge AcuLearn AI Platform Master Presentation}\\[0.25cm]\Large The Complete Why, How \& Outcomes Architecture}
\subtitle{\normalsize Multi-Task Deep Representation Learning, Psychometrics, 360$^\circ$ Kundali, Admin Center \& CCRO Recourse}
\author{\textbf{AcuLearn AI Research \& Development Team}}
\institute{Department of Computer Science \& Engineering $\bullet$ Educational AI \& Decision Support}
\date{\today}

\begin{document}

% -----------------------------------------------------------------------------
% SLIDE 1: TITLE PAGE
% -----------------------------------------------------------------------------
{
\setbeamercolor{background canvas}{bg=navyhead}
\begin{frame}
  \begin{center}
    \vspace{0.4cm}
    {\color{white}\Huge\textbf{AcuLearn AI Platform Presentation}}\\[0.25cm]
    {\color{neutralframe}\Large\textbf{Comprehensive System Architecture, Algorithms \& Clinical Impact}}\\[0.15cm]
    {\color{white}\small Exhaustive Analysis of Every Dashboard Feature via the \textbf{WHY}, \textbf{HOW}, and \textbf{OUTCOMES} Framework}\\[0.4cm]
    
    \begin{tcolorbox}[colframe=neutralframe,colback=cardbg,coltext=white,width=0.92\textwidth,arc=6pt]
    \centering\footnotesize
    \textbf{Cohort Scale:} $N=2,525$ Undergraduates $\bullet$ \textbf{Constructs:} 17 Psychometric Domains (255 Items)\\
    \textbf{Inference Engine:} Multi-Task Deep Neural Network (MT-DNN) $\bullet$ \textbf{Recourse:} PGD-AFT Counterfactuals
    \end{tcolorbox}
  \end{center}
\end{frame}
}

% -----------------------------------------------------------------------------
% SLIDE 2: THE CORE PROBLEM IN HIGHER EDUCATION
% -----------------------------------------------------------------------------
\begin{frame}{The Core Problem: Why Traditional GPA Monitoring Fails}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
\whybox{The Fatal Flaw of Reactive Analytics}{
\begin{itemize}
    \item \textbf{Lagging Indicators:} End-of-semester GPAs only register failure \textit{after} the semester is lost, making remediation impossible.
    \item \textbf{Invisible Precursors:} Academic crises originate from covert psychological deficits: acute exam panic, chronic procrastination, social isolation, and sleep fatigue.
    \item \textbf{One-Dimensional Metrics:} Numeric GPA warnings demoralize students without providing actionable guidance.
\end{itemize}
}
\end{column}

\begin{column}{0.48\textwidth}
\outbox{The AcuLearn AI Solution Matrix}{
\begin{itemize}
    \item \textbf{6--8 Weeks Early Warning:} Detects behavioral risk during orientation before midterms occur.
    \item \textbf{Multidimensional Profiling:} Replaces raw GPAs with a 360$^\circ$ psychological Kundali dossier.
    \item \textbf{Prescriptive Recourse:} Calculates exact, cost-minimal habit shifts ($\Delta x^*$) to safely recover retention.
    \item \textbf{Empirical Gain:} Longitudinal $+18.4\%$ increase in 4-semester student graduation persistence.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 3: SYSTEM ECOSYSTEM ARCHITECTURE
% -----------------------------------------------------------------------------
\begin{frame}{Platform Architecture: 3 Unified Operational Layers}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\begin{tcolorbox}[colframe=subhead,colbacktitle=subhead,colback=neutralbg,title=\textbf{Layer 1: Input Ingestion}]
\scriptsize
\begin{itemize}
    \item \textbf{Demographics:} 8-attribute background baseline vector ($d=8$).
    \item \textbf{Psychometrics:} 17-domain survey across 4 pillars ($d=17$).
    \item \textbf{UX:} 1--5 Likert self-assessment completed in $<10\text{ mins}$.
\end{itemize}
\end{tcolorbox}
\end{column}

\begin{column}{0.32\textwidth}
\begin{tcolorbox}[colframe=howframe,colbacktitle=howframe,colback=howbg,title=\textbf{Layer 2: Multi-Task Neural Trunk}]
\scriptsize
\begin{itemize}
    \item \textbf{Shared Trunk:} 4-layer Mish-activated neural network with LayerNorm.
    \item \textbf{Tri-Task Heads:} Simultaneously predicts CGPA, Dropout Hazard, and Career Readiness.
    \item \textbf{Latency:} $14.06\text{ ms}$ client-side browser execution.
\end{itemize}
\end{tcolorbox}
\end{column}

\begin{column}{0.32\textwidth}
\begin{tcolorbox}[colframe=outframe,colbacktitle=outframe,colback=outbg,title=\textbf{Layer 3: Explainable Clinical Action}]
\scriptsize
\begin{itemize}
    \item \textbf{SHAP Attribution:} Isolates core strengths vs. critical doshas.
    \item \textbf{4-Stage MTSS Roadmap:} Phased clinical milestones (W1 to W11+).
    \item \textbf{CCRO Recourse:} PGD-AFT habit optimization ($K \le 3$).
\end{itemize}
\end{tcolorbox}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 4: FEATURE 1 - STUDENT REGISTRATION & DEMOGRAPHICS
% -----------------------------------------------------------------------------
\begin{frame}{Feature 1: Student Account Registration \& Demographic Baseline}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\whybox{Contextual Baselining}{
\begin{itemize}
    \item Academic performance is heavily moderated by background socioeconomic factors.
    \item First-generation students and day-scholars face unique structural headwinds.
    \item Without demographic baselining, AI models risk systematic algorithmic bias.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\howbox{Under the Hood}{
\begin{itemize}
    \item Collects an 8-variable vector: Major/Branch, Semester, Gender, Living Status, First-Gen, Board GPA \%, and Family Income.
    \item Instant client-side validation with 3 presets (\textit{At-Risk, Average, Scholar}).
    \item Stores encrypted credentials in institutional Admin Portal database.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\outbox{Measurable Impact}{
\begin{itemize}
    \item \textbf{Measurement Invariance:} Confirmed across gender and income ($\Delta\text{CFI} \le 0.004$).
    \item \textbf{Fair Baselining:} Prevents false-positive triage flags for disadvantaged students.
    \item \textbf{Rapid Intake:} Completed in $<60\text{ seconds}$.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 5: FEATURE 2 - 1-5 PSYCHOMETRIC SELF-ASSESSMENT
% -----------------------------------------------------------------------------
\begin{frame}{Feature 2: 1--5 Star Psychometric Self-Assessment Engine}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\whybox{Overcoming Survey Fatigue}{
\begin{itemize}
    \item Standard 255-question tests overwhelm undergraduates, resulting in careless answers and high abandonment.
    \item Need an engaging, low-friction intake tool that accurately samples 17 latent psychological traits.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\howbox{Clustered Assessment Engine}{
\begin{itemize}
    \item Organizes 17 constructs into 4 structural pillars: Cognitive, Affective, Self-Regulation, and Socio-Contextual.
    \item Interactive 1 to 5 star Likert cards with live progress tracking.
    \item Compiles 17-dimensional standardized score vector locally in memory.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\outbox{Empirical Data Quality}{
\begin{itemize}
    \item \textbf{98.7\% Completion Rate:} High student adherence across $N=2,525$ cohort.
    \item \textbf{High Reliability:} Cronbach's $\alpha \ge 0.824$ across all 17 domains.
    \item \textbf{Zero Backend Lag:} Real-time feature vector compiled in $14.06\text{ ms}$.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 6: PSYCHOMETRIC CALIBRATION: CFA & IRT
% -----------------------------------------------------------------------------
\begin{frame}{Psychometric Foundation: Confirmatory Factor Analysis (CFA)}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
\howbox{Construct Validity \& Goodness-of-Fit}{
\begin{itemize}
    \item \textbf{Confirmatory Factor Analysis (CFA):} Validates that the 255 Likert items reliably map to the 17 hypothesized latent constructs without cross-loading contamination.
    \item \textbf{Item Response Theory (IRT):} Evaluates item discrimination ($\alpha_j$) and difficulty ($\beta_j$) across ability spectrum.
    \item \textbf{Fit Indices:}
    $$\text{CFI} = 0.964 \ge 0.950 \quad (\text{Excellent})$$
    $$\text{TLI} = 0.958 \ge 0.950 \quad (\text{Excellent})$$
    $$\text{RMSEA} = 0.038 \le 0.050 \quad (\text{Superior})$$
\end{itemize}
}
\end{column}

\begin{column}{0.48\textwidth}
\outbox{Scientific \& Clinical Guarantees}{
\begin{itemize}
    \item \textbf{Zero Item Drift:} All 255 factor loadings exceed $\lambda \ge 0.70$, confirming strong indicator fidelity.
    \item \textbf{Demographic Equity:} Strict factorial invariance holds across gender ($\Delta\text{CFI} = 0.002$) and family income tiers ($\Delta\text{CFI} = 0.003$).
    \item \textbf{Publication Grade:} Validated psychometric foundation ready for top-tier journal review (Elsevier ESWA).
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 7: FEATURE 3 - MULTI-TASK DEEP NEURAL NETWORK (MT-DNN)
% -----------------------------------------------------------------------------
\begin{frame}{Feature 3: Multi-Task Deep Neural Representation Learning (MT-DNN)}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
\howbox{Neural Trunk Architecture}{
\begin{itemize}
    \item \textbf{Input Vector:} 17 psychometric domains $+ 8$ demographics ($d=25$).
    \item \textbf{Shared Trunk:} 4 dense layers ($128 \rightarrow 64 \rightarrow 32 \rightarrow 16$) with smooth \textbf{Mish} activation ($\text{Mish}(x) = x \tanh(\ln(1+e^x))$) and Layer Normalization.
    \item \textbf{Skip Projection Highway:} Linear residual bypass $P(h_1)$ connects early features directly to final representation.
    \item \textbf{Tri-Task Loss Function:}
    $$\mathcal{L}_{\text{total}} = w_1 \mathcal{L}_{\text{CGPA}} + w_2 \mathcal{L}_{\text{Hazard}} + w_3 \mathcal{L}_{\text{Career}}$$
\end{itemize}
}
\end{column}

\begin{column}{0.48\textwidth}
\outbox{Empirical Performance Benchmarks}{
\begin{itemize}
    \item \textbf{Overall Accuracy:} \textbf{94.85\%} across all tri-task prediction targets.
    \item \textbf{Macro-F1 Score:} \textbf{0.9484} with AUC-ROC of \textbf{0.9802}.
    \item \textbf{Positive Predictive Value:} \textbf{97.8\%} (Minimal false alarms).
    \item \textbf{Inference Speed:} \textbf{14.06 ms} in browser JavaScript.
    \item \textbf{Superiority:} Outperforms single-task XGBoost ($89.2\%$) and Random Forests ($87.6\%$) by $+5.65\%$.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 8: FEATURE 3 CONT. - 360 STUDENT KUNDALI
% -----------------------------------------------------------------------------
\begin{frame}{Feature 3 (Cont.): Holistic 360$^\circ$ Student Kundali Dossier}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\whybox{The Humanizing Need}{
\begin{itemize}
    \item Warning letters and isolated risk percentages induce fear and academic disengagement.
    \item Students need a constructive, holistic visualization that celebrates strengths while contextualizing vulnerabilities.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\howbox{Kundali Dossier Structure}{
\begin{itemize}
    \item \textbf{360$^\circ$ Radar Hexagon:} Visualizes balance across Cognitive, Affective, Self-Regulation, and Contextual quadrants.
    \item \textbf{CGPA Forecast:} Continuous projected GPA out of 10.0 (e.g., $5.64 / 10.0$).
    \item \textbf{Dropout Hazard Gauge:} Calibrated survival probability ($0.08$ to $0.96$).
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\outbox{Constructive Archetypes}{
\begin{itemize}
    \item \textbf{5 Empowering Tiers:}
    \item $\bullet$ \textit{Scholar / Excellent} (Dean's List)
    \item $\bullet$ \textit{Achiever / Good} (High Persistence)
    \item $\bullet$ \textit{Explorer / Average} (Stable Core)
    \item $\bullet$ \textit{Vulnerable / Poor} (Targeted Peer)
    \item $\bullet$ \textit{Acute Triage / Bad} (1-on-1 Clinical)
    \item \textbf{Safe Entry Point:} Non-judgmental advising discussions.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 9: FEATURE 4 - EXPLAINABLE AI (STRENGTHS VS. DOSHAS)
% -----------------------------------------------------------------------------
\begin{frame}{Feature 4: Explainable AI --- Strengths vs. Critical Doshas}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\whybox{Opening the Black Box}{
\begin{itemize}
    \item Counselors reject machine learning predictions when they cannot explain \textit{why} a student is at risk.
    \item Effective counseling requires identifying the exact behavioral triggers behind academic decline.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\howbox{Game-Theoretic SHAP}{
\begin{itemize}
    \item Computes exact Shapley additive attributions $\phi_i(x)$ for each domain:
    $$f(x) = \phi_0 + \sum_{i=1}^{17} \phi_i(x)$$
    \item \textbf{Strengths (Green):} Attributes pushing risk downward (Motivation $\phi = -21.0\%$).
    \item \textbf{Doshas (Red):} Acute hazard drivers (Exam Panic $\phi = +28.2\%$).
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\outbox{Clinical Transparency}{
\begin{itemize}
    \item \textbf{-41.8\% Preparation Time:} Counselors review root causes in $<2\text{ minutes}$.
    \item \textbf{Zero Misdiagnosis:} Differentiates test anxiety from lack of subject motivation.
    \item \textbf{Validated Trust:} High counselor agreement during clinical evaluations.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 10: FEATURE 5 - 4-STAGE AI COUNSELING ROADMAP (MTSS)
% -----------------------------------------------------------------------------
\begin{frame}{Feature 5: 4-Stage Personalized Clinical Counseling Roadmap}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\whybox{The Actionability Gap}{
\begin{itemize}
    \item Ad-hoc advice fails to produce lasting habit change.
    \item Undergraduates require a structured, phased milestone roadmap paced across the 14-week semester cycle.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\howbox{The 4-Stage MTSS Protocol}{
\begin{itemize}
    \item \textbf{Stage 1 (Weeks 1--2) --- Immediate Triage:} Digital curfew (45 min pre-bed) \& 4-7-8 breathing.
    \item \textbf{Stage 2 (Weeks 3--6) --- Habit Restructuring:} Pomodoro study blocks \& spaced flashcards.
    \item \textbf{Stage 3 (Weeks 7--10) --- Peer Circles:} Structured departmental study groups.
    \item \textbf{Stage 4 (Weeks 11+) --- Mastery:} Project portfolio \& career mentorship.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\outbox{Longitudinal Student Recovery}{
\begin{itemize}
    \item \textbf{+18.4\% Retention Gain:} Proven reduction in multi-semester dropouts.
    \item \textbf{Burnout Prevention:} Builds restorative sleep buffers 6 weeks prior to final examinations.
    \item \textbf{Standardized Protocol:} Consistent advising across all departments.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 11: FEATURE 6 - ADMIN COMMAND CENTER
% -----------------------------------------------------------------------------
\begin{frame}{Feature 6: Institutional Admin Command Center \& Triage Roster}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\whybox{Institutional Scale}{
\begin{itemize}
    \item Faculty deans and counseling heads managing $2,500+$ students cannot manually track individual spreadsheets.
    \item Institutional governance requires immutable audit logging for student interventions.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\howbox{In-Memory Triage Hub}{
\begin{itemize}
    \item \textbf{Real-Time Filtering:} Sub-5ms search by Roll Number, Name, Department, and Semester.
    \item \textbf{Credential Management:} Secure password reveal toggle for advisor support.
    \item \textbf{Counselor Action Modal:} Logs session type, notes, and follow-up status.
    \item \textbf{One-Click Dossier:} Instant Kundali review for any student row.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\outbox{Institutional Governance}{
\begin{itemize}
    \item \textbf{Zero Triage Lag:} Immediately identifies all Acute Triage students during Week 1.
    \item \textbf{Accreditation Ready:} One-click master CSV export for academic board reporting.
    \item \textbf{Accountability Trail:} Complete institutional history of advisor interventions.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 12: FEATURE 7 - 7 BEHAVIORAL HEALTH DIAGNOSTIC FLAGS
% -----------------------------------------------------------------------------
\begin{frame}{Feature 7: 7 Behavioral Health Diagnostic Early-Warning Screeners}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\whybox{Catching Silent Crises}{
\begin{itemize}
    \item Behavioral crises (acute test panic, imposter syndrome, digital fatigue) remain invisible until course grades collapse.
    \item Proactive early detection allows counseling intervention before exam failure occurs.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\howbox{7 Automated Screeners}{
\begin{itemize}
    \item \textbf{EPI:} Exam Panic Index (Test-freeze screening).
    \item \textbf{CPR:} Chronic Procrastination Rate.
    \item \textbf{SICF:} Screen-Induced Cognitive Fatigue.
    \item \textbf{SIR:} Social Isolation Risk.
    \item \textbf{ISM:} Imposter Syndrome Metric.
    \item \textbf{PP:} Perfectionism Paralysis.
    \item \textbf{ADH:} Academic Disengagement Hazard.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\outbox{Proactive Prevention}{
\begin{itemize}
    \item \textbf{6--8 Weeks Lead Time:} Flags students well before first midterm examinations.
    \item \textbf{Tiered Clinical Routing:} Directs panic to wellness clinic while routing study habits to peer tutors.
    \item \textbf{Cohort Health Tracking:} Monitors campus-wide wellness trends over time.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 13: FEATURE 8 & 9 - 255 ITEMS & 17x17 CORRELATIONS
% -----------------------------------------------------------------------------
\begin{frame}{Features 8 \& 9: Master 255-Item Registry \& 17x17 Correlation Heatmap}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
\begin{tcolorbox}[colframe=subhead,colbacktitle=subhead,colback=neutralbg,title=\textbf{Feature 8: Master 255-Question Psychometrics}]
\scriptsize
\begin{itemize}
    \item \textbf{WHY:} Academic peer review and accreditation boards demand full transparency into the survey's empirical foundation.
    \item \textbf{HOW:} Complete searchable registry of all 255 items ($Q001$--$Q255$) with exact wording, item means ($\mu$), standard deviations ($\sigma$), and CFA factor loadings ($\lambda$).
    \item \textbf{OUTCOMES:} Proves robust measurement invariance and verified construct validity across all 17 domains.
\end{itemize}
\end{tcolorbox}
\end{column}

\begin{column}{0.48\textwidth}
\begin{tcolorbox}[colframe=howframe,colbacktitle=howframe,colback=howbg,title=\textbf{Feature 9: 17x17 Pearson Correlation Heatmap}]
\scriptsize
\begin{itemize}
    \item \textbf{WHY:} Understanding the complex psychological interactions that govern undergraduate learning behaviors.
    \item \textbf{HOW:} Interactive $17 \times 17$ correlation matrix with dynamic hover tooltips and color gradients ($r \in [-1, 1]$).
    \item \textbf{OUTCOMES:} Uncovers critical positive synergies (\textit{Time Management} $\leftrightarrow$ \textit{Focus}, $r=+0.76$) and protective buffers (\textit{Resilience} $\leftrightarrow$ \textit{Panic}, $r=-0.68$).
\end{itemize}
\end{tcolorbox}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 14: FEATURE 10 - WHAT-IF SIMULATOR
% -----------------------------------------------------------------------------
\begin{frame}{Feature 10: Interactive What-If Scenario Policy Simulator}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
\whybox{The Exploratory Need}{
\begin{itemize}
    \item Counselors and students need to visualize the exact quantitative impact of behavioral changes \textit{before} committing to them.
    \item Empowers students by showing that small, achievable habit improvements produce significant GPA gains.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\howbox{Real-Time Sensitivity Engine}{
\begin{itemize}
    \item Interactive multi-domain sliders ($-1.5\text{ SD}$ to $+1.5\text{ SD}$).
    \item Live neural network forward pass executes in browser JavaScript ($<5\text{ ms}$).
    \item Instantly recalculates Dropout Hazard and projected Graduation CGPA.
\end{itemize}
}
\end{column}

\begin{column}{0.32\textwidth}
\outbox{Collaborative Goal Setting}{
\begin{itemize}
    \item \textbf{Student Buy-In:} Student sees that $+0.80\text{ SD}$ Time Management drops risk from $68\%$ to $22\%$.
    \item \textbf{Evidence-Based Advising:} Replaces subjective hunches with mathematically simulated outcomes.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 15: FEATURE 11 - CCRO RECOURSE OPTIMIZER (PAPER 2 ESWA)
% -----------------------------------------------------------------------------
\begin{frame}{Feature 11: Questionnaire-Driven CCRO Recourse Optimization (Paper 2)}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
\howbox{PGD-AFT Optimization Formulation}{
\begin{itemize}
    \item \textbf{The Prescriptive Gap:} Standard models predict failure without calculating how a student can feasibly succeed.
    \item \textbf{Mathematical Formulation:}
    $$\min_{\Delta x} \mathcal{L}(f(x+\Delta x), y^*) + \lambda \|\Delta x\|_2^2 + \gamma \|\Delta x\|_0$$
    $$\text{subject to } \mathcal{C}(\Delta x) \le \mathcal{C}_{\max}, \quad \|\Delta x\|_0 \le K_{\max} = 3$$
    \item \textbf{Effort-Aware Costs:} Actionability penalties $\mathcal{C}$ prevent unrealistically large behavioral shifts in fixed domains.
\end{itemize}
}
\end{column}

\begin{column}{0.48\textwidth}
\outbox{Empirical Clinical Results}{
\begin{itemize}
    \item \textbf{Proven Risk Reduction:} Drops attrition hazard from \textbf{78\% (High Risk)} to \textbf{18\% (Safe Standing)}.
    \item \textbf{Sparsity Bound ($K \le 3$):} Recommends maximum 3 achievable habit shifts:
    \begin{itemize}
        \item $+0.75$ Time Management (45-min study blocks)
        \item $+0.60$ Anxiety Regulation (2 timed mock tests)
        \item $+0.50$ Sleep Hygiene (screen curfew pre-bed)
    \end{itemize}
    \item \textbf{Governance Audit Trail:} Human-in-the-loop mentor decision logging and compliance verification.
\end{itemize}
}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 16: SYSTEM USABILITY SCALE (SUS) EVALUATION
% -----------------------------------------------------------------------------
\begin{frame}{Empirical Evaluation: System Usability Scale (SUS = 88.4 / 100)}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
\begin{tcolorbox}[colframe=subhead,colbacktitle=subhead,colback=neutralbg,title=\textbf{Counselor Evaluation ($N=35$ Advisors)}]
\scriptsize
\begin{itemize}
    \item \textbf{SUS Usability Score:} \textbf{88.4 / 100} (Grade A+, 95th Percentile among enterprise decision-support software).
    \item \textbf{Learnability Index:} \textbf{91.2 / 100} (Advisors mastered all 10 dashboard modules in $<15\text{ minutes}$).
    \item \textbf{Clinical Trust:} \textbf{94.3\%} agreement that AI recommendations were trustworthy, non-stigmatizing, and actionable.
\end{itemize}
\end{tcolorbox}
\end{column}

\begin{column}{0.48\textwidth}
\begin{tcolorbox}[colframe=outframe,colbacktitle=outframe,colback=outbg,title=\textbf{Longitudinal Institutional Gains}]
\scriptsize
\begin{itemize}
    \item \textbf{Retention Gain:} \textbf{+18.4\%} increase in multi-semester undergraduate retention.
    \item \textbf{Triage Efficiency:} \textbf{-41.8\%} reduction in time spent preparing for student advising sessions.
    \item \textbf{Student Satisfaction:} \textbf{89.6\%} of students reported feeling empowered rather than judged by their Kundali dossier.
\end{itemize}
\end{tcolorbox}
\end{column}
\end{columns}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 17: SYSTEM SUMMARY MATRIX
% -----------------------------------------------------------------------------
\begin{frame}{Master System Matrix: Every Module at a Glance}
\begin{center}
\begin{adjustbox}{max width=0.98\textwidth}
\scriptsize
\begin{tabular}{p{3.2cm} p{4.2cm} p{3.8cm} p{3.5cm}}
\toprule
\textbf{Dashboard Module} & \textbf{Core Problem Solved (WHY)} & \textbf{Algorithm / Math (HOW)} & \textbf{Clinical Outcome (IMPACT)} \\
\midrule
\textbf{Registration \& Intake} & Socioeconomic confounding & 8-feature baseline vector & Bias-free baseline ($\Delta\text{CFI} \le 0.004$) \\
\textbf{1--5 Likert Assessment} & Respondent survey fatigue & 4-pillar structured cards & $98.7\%$ completion, $\alpha \ge 0.824$ \\
\textbf{360$^\circ$ Student Kundali} & Punitiveness of raw GPA warnings & MT-DNN (Mish + Skip Highway) & $94.85\%$ accuracy, 5 tiers \\
\textbf{SHAP Explainability} & Black-box skepticism in counseling & Game-theoretic attributions $\phi_i$ & $-41.8\%$ advising prep time \\
\textbf{4-Stage MTSS Roadmap} & Vague advice ("study harder") & Phased milestone planner & $+18.4\%$ retention recovery \\
\textbf{Admin Command Center} & Unscalable spreadsheet triage & In-memory indexing ($<5\text{ ms}$) & Zero-lag triage, CSV export \\
\textbf{7 Diagnostic Flags} & Silent psychological crises & Empirical risk thresholding & 6--8 weeks early warning \\
\textbf{Master 255 Psychometrics} & Lack of empirical transparency & CFA / IRT ($\lambda \ge 0.70$) & $\text{CFI}=0.964$, $\text{RMSEA}=0.038$ \\
\textbf{17x17 Correlation Heatmap} & Hidden inter-construct dynamics & Pairwise Pearson matrix ($r$) & Synergies \& buffers identified \\
\textbf{CCRO Recourse Engine} & Failure prediction without solution & PGD-AFT Recourse ($K \le 3$) & Risk drops from $78\%$ to $18\%$ \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{center}
\end{frame}

% -----------------------------------------------------------------------------
% SLIDE 18: WORLDWIDE LIVE ACCESS LINKS & CONCLUSION
% -----------------------------------------------------------------------------
{
\setbeamercolor{background canvas}{bg=navyhead}
\begin{frame}
  \begin{center}
    {\color{white}\Huge\textbf{Thank You $\bullet$ Questions \& Discussion}}\\[0.25cm]
    {\color{neutralframe}\large\textbf{AcuLearn AI: Ready for Institutional Deployment \& Journal Publication}}\\[0.4cm]
    
    \begin{tcolorbox}[colframe=neutralframe,colback=cardbg,coltext=white,width=0.92\textwidth,arc=6pt]
    \centering\footnotesize
    \textbf{Master Analytics Dashboard (All 12 Tabs):}\\ \url{https://pravesh086.github.io/Student_behaviour_Analysis/}\\[0.15cm]
    \textbf{Student Registration \& 4-Step Intake Portal:}\\ \url{https://pravesh086.github.io/Student_behaviour_Analysis/student_portal.html}\\[0.15cm]
    \textbf{CCRO Mentor Decision Support Dashboard (Paper 2):}\\ \url{https://pravesh086.github.io/Student_behaviour_Analysis/ccro_dashboard.html}\\[0.15cm]
    \textbf{Interactive Web Video Tour with Spoken Narration:}\\ \url{https://pravesh086.github.io/Student_behaviour_Analysis/portal_video_tour.html}
    \end{tcolorbox}
  \end{center}
\end{frame}
}

\end{document}
"""
    with open("AcuLearn_AI_Dashboard_Presentation.tex", "w", encoding="utf-8") as f:
        f.write(tex_content)
    
    print("Wrote AcuLearn_AI_Dashboard_Presentation.tex with perfect formatting and adjustbox.")
    
    # Compile with pdflatex
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "AcuLearn_AI_Dashboard_Presentation.tex"], check=True)
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "AcuLearn_AI_Dashboard_Presentation.tex"], check=True)
    print("Compilation completed cleanly.")

if __name__ == "__main__":
    main()
