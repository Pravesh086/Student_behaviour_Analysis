# Pre-PhD Open Seminar & Progress Report: Complete Presentation Package

**Candidate:** Pravesh Kumar Bansal (2019RCP9557)  
**Supervisor:** Dr. Mushtaq Ahmed, Associate Professor and HOD  
**Department:** Computer Science & Engineering, Malaviya National Institute of Technology Jaipur  
**Date:** 19 November 2026  

---

## 📁 Package Contents Overview

This unified package contains all presentation documents (PowerPoint and Beamer PDFs), editable LaTeX source codes, Python generation scripts, and high-resolution figure images.

### 1. Presentation Documents

| File Name | Type | Description |
| :--- | :--- | :--- |
| `progress_report_presentation.pptx` | PowerPoint (PPTX) | Full 53-slide presentation with updated metadata and figures |
| `progress_report_beamer.pdf` | Beamer PDF | 53-page presentation matching reference Madrid theme |
| `progress_report_beamer.tex` | LaTeX Source | Editable Beamer LaTeX source for the 53-page deck |
| `presentation_blue.pdf` | Beamer PDF | 31-page executive presentation in Blue Theme |
| `presentation_blue.tex` | LaTeX Source | Editable LaTeX source for the 31-page deck |
| `PrePhD_Defense_SingleColumn_Blue_Deck.pptx` | PowerPoint (PPTX) | 29-slide executive PowerPoint deck |
| `all_17_features_complete_guide.pdf` | PDF Guide | Complete theoretical and empirical guide to the 17 non-cognitive features |

### 2. Python Build Scripts

- `generate_madrid_pptx.py`: Generates `progress_report_presentation.pptx` from scratch.
- `build_single_column_blue_deck.py`: Generates the executive single-column blue PowerPoint deck.
- `generate_17_features_pdf.py`: Generates the comprehensive 17-features reference document.

### 3. Image Assets (`assets/` Folder)

Contains **69 high-resolution images and diagrams** used throughout the presentation, including:

- `diagram_system_architecture.png`: Master system architecture flow
- `diagram_benet_architecture.png`: BE-Net deep neural network architecture
- `diagram_ccro_recourse.png`: Counterfactual Recourse (CCRO) actionable algorithm
- `fig18a_cfa_diagram.png`: Confirmatory Factor Analysis path model
- `fig4a_attrition_benchmark.png`: Attrition rate benchmarks across institutions
- `fig5a_trajectory_curve.png`: Longitudinal student GPA trajectory curves
- `fig10a_data_provenance_flow.png`: Survey data collection and provenance flow
- `fig24a_de_convergence.png`: Differential Evolution parameter convergence
- `fig31a_baseline_bars.png`: Benchmark baseline classifier comparison
- `fig32a_ablation_waterfall.png`: Component ablation waterfall analysis
- `fig35a_shap_beeswarm.png`: Global SHAP feature importance beeswarm plot
- `fig45a_kundali_radar.png`: Student Non-Cognitive Holistic Kundali radar chart
- `fig48a_fairness_bars.png`: Subgroup fairness evaluation across demographic groups
- `fig_confusion_matrices.png`: Confusion matrices across risk categories

## 🚀 Quick Usage Guide

1. **Present directly:** Open `progress_report_presentation.pptx` in Microsoft PowerPoint or `progress_report_beamer.pdf` in any PDF reader.
2. **Edit LaTeX:** Edit `progress_report_beamer.tex` or `presentation_blue.tex` and compile using:
   ```bash
   pdflatex progress_report_beamer.tex
   ```
3. **Regenerate PPTX:** Run:
   ```bash
   python generate_madrid_pptx.py
   ```
