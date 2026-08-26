import re

path = r"C:\Users\Pravesh\Documents\Antigravity\Journal_Paper\main_journal.tex"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Enrich citations
replacements = [
    (r"\\cite\{tinto1975dropout, tinto1993leaving\}", r"\\cite{tinto1975dropout, tinto1993leaving, hassan2024predicting, alam2024generative}"),
    (r"\\cite\{romero2020educational, baker2009state, conijn2017predicting\}", r"\\cite{romero2020educational, baker2009state, conijn2017predicting, martinez2023human, yan2024self, ochoa2024multimodal}"),
    (r"\\cite\{chen2016xgboost, arik2021tabnet, ke2017lightgbm\}", r"\\cite{chen2016xgboost, arik2021tabnet, ke2017lightgbm, singh2025explainable, hassan2024predicting}"),
    (r"\\cite\{sugai2006school\}", r"\\cite{sugai2006school, fernandez2023multi, molenaar2024towards}"),
    (r"\\cite\{lundberg2017unified,ribeiro2016why,swamy2024evaluating,morris2024evaluating\}", r"\\cite{lundberg2017unified, ribeiro2016why, khosravi2023explainable, swamy2024evaluating, morris2024evaluating, singh2025explainable}"),
    (r"\\cite\{wachter2017counterfactual,mothilal2020explaining,zhang2025counterfactual\}", r"\\cite{wachter2017counterfactual, mothilal2020explaining, swamy2024evaluating, zhang2025counterfactual, rodriguez2024counterfactual}"),
    (r"\\cite\{caruana1997multitask,chen2025multimodal,wang2025deep\}", r"\\cite{caruana1997multitask, chen2025multimodal, wang2025deep, singh2025explainable}"),
    (r"\\cite\{dwork2012fairness,hardt2016equality,baker2024algorithmic,zhao2026responsible\}", r"\\cite{dwork2012fairness, hardt2016equality, baker2024algorithmic, zhao2026responsible, chen2026fairness}"),
    (r"\\cite\{zimmerman2000attaining,deci2000self,molenaar2024towards,alharbi2024psychometric\}", r"\\cite{zimmerman2000attaining, deci2000self, molenaar2024towards, alharbi2024psychometric, yan2024self, torres2024belonging, park2025digital, gao2024neurodiversity, li2024student}"),
    (r"\\cite\{fernandez2023multi,dwivedi2023artificial,li2024student,gao2024neurodiversity\}", r"\\cite{fernandez2023multi, dwivedi2023artificial, li2024student, gao2024neurodiversity, kumar2025privacy, zhao2026responsible, chen2026fairness}"),
    (r"\\cite\{gal2016dropout\}", r"\\cite{gal2016dropout, chen2025multimodal, wang2025deep}")
]

for pat, repl in replacements:
    text = re.sub(pat, repl, text)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

with open(r"c:\Users\Pravesh\Downloads\Student_Analysis-main\Student_Analysis-main\main_journal.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Enriched citations in main_journal.tex across all major theoretical and empirical sections!")
