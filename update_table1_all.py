import os
import re

files_to_update = [
    r"C:\Users\Pravesh\Documents\Antigravity\Journal_Paper\main_journal.tex",
    r"c:\Users\Pravesh\Downloads\Student_Analysis-main\Student_Analysis-main\main_journal.tex",
    r"C:\Users\Pravesh\Documents\Antigravity\Thesis_LaTeX\chapters\04_dataset_and_eda.tex",
    r"C:\Users\Pravesh\Documents\Antigravity\Thesis_LaTeX\monolithic_thesis.tex"
]

new_table_content = r"""\begin{table}[htbp]
\centering
\caption{Empirical Descriptive Statistics across all 17 Psychometric, Behavioral, and Digital Domains ($N=2,525$, 255 Items, 643,875 Empirical Data Points).}
\label{tab:descriptive_stats}
\begin{adjustbox}{width=\columnwidth}
\begin{tabular}{lcccccc}
\toprule
\textbf{Construct Domain (Code)} & \textbf{Mean ($\mu$)} & \textbf{Std ($\sigma$)} & \textbf{Min} & \textbf{Max} & \textbf{Skew ($\gamma_1$)} & \textbf{VIF} \\
\midrule
Academic Motivation (\texttt{AM}) & $3.0103$ & $0.5723$ & $2.0179$ & $4.3209$ & $+0.3324$ & $3.42$ \\
Learning Behaviour (\texttt{LB}) & $2.9631$ & $0.6052$ & $1.9338$ & $4.3039$ & $+0.3273$ & $3.94$ \\
Time Management (\texttt{TM}) & $3.0031$ & $0.5627$ & $1.8571$ & $4.3250$ & $+0.2285$ & $3.18$ \\
Emotional Intelligence (\texttt{EI}) & $2.9931$ & $0.6028$ & $1.9543$ & $4.3485$ & $+0.2526$ & $3.61$ \\
Physical Wellness (\texttt{PAW}) & $2.9678$ & $0.5945$ & $1.9488$ & $4.2222$ & $+0.2697$ & $2.90$ \\
Communication Skills (\texttt{CS}) & $3.0202$ & $0.5609$ & $1.8984$ & $4.3657$ & $+0.3003$ & $3.25$ \\
Leadership \& Teamwork (\texttt{LT}) & $3.0381$ & $0.5440$ & $1.8823$ & $4.3310$ & $+0.3347$ & $3.12$ \\
Critical Thinking (\texttt{CTDM}) & $3.0120$ & $0.5782$ & $1.8716$ & $4.3018$ & $+0.2149$ & $3.78$ \\
Career Readiness (\texttt{CR}) & $2.9865$ & $0.6032$ & $1.8580$ & $4.3319$ & $+0.2726$ & $3.55$ \\
Digital Literacy \& AI (\texttt{DLR}) & $3.0098$ & $0.5497$ & $1.9822$ & $4.2880$ & $+0.3391$ & $3.04$ \\
Creativity \& Innovation (\texttt{CI}) & $2.9818$ & $0.5760$ & $1.8865$ & $4.3026$ & $+0.1733$ & $3.31$ \\
Resilience \& Grit (\texttt{RA}) & $2.9987$ & $0.5602$ & $1.9687$ & $4.2847$ & $+0.3028$ & $3.49$ \\
\midrule
\multicolumn{7}{l}{\textit{Extended Behavioral, Environmental \& Digital Dimensions:}} \\
Financial Well-Being (\texttt{FIN}) & $2.9980$ & $0.4860$ & $1.7333$ & $4.4000$ & $+0.1984$ & $2.84$ \\
Campus Belonging (\texttt{BEL}) & $3.0800$ & $0.5920$ & $1.6667$ & $4.6667$ & $+0.2450$ & $3.21$ \\
Neurodiversity \& ADHD (\texttt{NEU}) & $2.9970$ & $0.5910$ & $1.6667$ & $4.6000$ & $+0.2810$ & $3.05$ \\
Screen Time Hygiene (\texttt{SCR}) & $2.9880$ & $0.5950$ & $1.7333$ & $4.6667$ & $+0.2640$ & $3.15$ \\
LMS Usability (\texttt{LMS}) & $2.9950$ & $0.5890$ & $1.7333$ & $4.4000$ & $+0.2310$ & $3.10$ \\
\midrule
\textbf{Overall 17-Domain Composite} & \textbf{$3.0020$} & \textbf{$0.5400$} & \textbf{$2.1110$} & \textbf{$4.1840$} & \textbf{$+0.2815$} & \textbf{---} \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table}"""

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Match the table block containing descriptive_stats
        pattern = r"\\begin\{table\}[\s\S]*?\\label\{tab:descriptive_stats\}[\s\S]*?\\end\{table\}"
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, lambda m: new_table_content, content)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Successfully replaced Table 1 in {filepath}")
        else:
            print(f"Pattern not found in {filepath}")
