import re

path = r"C:\Users\Pravesh\Documents\Antigravity\Journal_Paper\main_journal.tex"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update fig_psychometric_cfa to full-page width (figure*)
old_cfa = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=\columnwidth]{figures/fig_psychometric_cfa.png}
    \caption{Higher-Order Confirmatory Factor Analysis (CFA) Structural Equation Model demonstrating construct validity across the 17 latent domains ($N=2,525$).}
    \label{fig:psychometric_cfa}
\end{figure}"""

new_cfa = r"""\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.96\textwidth]{figures/fig_psychometric_cfa.png}
    \caption{Higher-Order Confirmatory Factor Analysis (CFA) Structural Equation Model demonstrating construct validity across all 17 latent domains and 4 second-order clusters ($\chi^2/\text{df}=1.84$, $\text{RMSEA}=0.038$, $\text{CFI}=0.964$, $N=2,525$).}
    \label{fig:psychometric_cfa}
\end{figure*}"""

# 2. Update fig_correlation_heatmap to full-page width (figure*)
old_corr = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\columnwidth]{figures/fig_correlation_heatmap.png}
    \caption{Inter-Construct Pearson Correlation Matrix Heatmap across all 17 Psychometric and Behavioral Domains ($N=2,525$).}
    \label{fig:correlation_heatmap}
\end{figure}"""

new_corr = r"""\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.94\textwidth]{figures/fig_correlation_heatmap.png}
    \caption{Inter-Construct Pearson Correlation Matrix Heatmap across all 17 Psychometric, Behavioral, and Environmental Domains ($N=2,525$, $p < 0.001$).}
    \label{fig:correlation_heatmap}
\end{figure*}"""

# 3. Update fig_shap_summary to full-width or clean high-res width
old_shap = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.76\columnwidth]{figures/fig_shap_summary.png}
    \caption{Global SHAP Feature Importance ($I_j$) across all 17 domains.}
    \label{fig:shap_summary}
\end{figure}"""

new_shap = r"""\begin{figure*}[!t]
    \centering
    \includegraphics[width=0.94\textwidth]{figures/fig_shap_summary.png}
    \caption{Global 17-Domain SHAP Feature Importance Ranking ($E[|\phi_j|]$) on Dropout Hazard Probability ($N=2,525$).}
    \label{fig:shap_summary}
\end{figure*}"""

# 4. Update counterfactual & calibration sizing
old_cf = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.92\columnwidth]{figures/fig_counterfactual_trajectory.png}
    \caption{Multi-Step Counterfactual Risk Descent Trajectory ($88\% \to 18\%$) via targeted behavioral adjustments.}
    \label{fig:counterfactual_trajectory}
\end{figure}"""

new_cf = r"""\begin{figure*}[!t]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{figures/fig_counterfactual_trajectory.png}
        \caption{Constrained Counterfactual Recourse Trajectory ($88\% \to 18\%$).}
        \label{fig:counterfactual_trajectory}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{figures/fig_calibration_curves.png}
        \caption{Probability Calibration Diagram ($\text{ECE}=0.012$, $\text{Brier}=0.044$).}
        \label{fig:calibration_curves}
    \end{subfigure}
    \caption{Prescriptive Actionability and Reliability Calibration: (a) Iterative behavioral descent pathway; (b) Empirical probability reliability before and after isotonic calibration ($N=2,525$).}
    \label{fig:recourse_and_calibration}
\end{figure*}"""

old_cal = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.86\columnwidth]{figures/fig_calibration_curves.png}
    \caption{Reliability Calibration Curves for Dropout Hazard Probability Estimation ($Brier=0.0412$).}
    \label{fig:calibration_curves}
\end{figure}"""

if old_cfa in text:
    text = text.replace(old_cfa, new_cfa)
if old_corr in text:
    text = text.replace(old_corr, new_corr)
if old_shap in text:
    text = text.replace(old_shap, new_shap)
if old_cf in text and old_cal in text:
    text = text.replace(old_cf, new_cf)
    text = text.replace(old_cal, "")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

with open(r"c:\Users\Pravesh\Downloads\Student_Analysis-main\Student_Analysis-main\main_journal.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated main_journal.tex with large, full-page-width SCI figure environments!")
