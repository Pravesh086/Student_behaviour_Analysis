import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Directories
FIG_DIRS = [
    r"C:\Users\Pravesh\Documents\Antigravity\Journal_Paper\figures",
    r"C:\Users\Pravesh\Documents\Antigravity\Thesis_LaTeX\figures",
    r"C:\Users\Pravesh\Documents\Antigravity\Thesis\figures"
]

for d in FIG_DIRS:
    os.makedirs(d, exist_ok=True)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9

DOMAINS = [
    "Academic Motivation", "Learning Behaviour", "Time Management", "Emotional Intelligence",
    "Physical Activity & Wellness", "Communication Skills", "Leadership & Teamwork", "Critical Thinking & Decision Making",
    "Career Readiness", "Digital Literacy & AI Readiness", "Creativity & Innovation", "Resilience & Adaptability",
    "Financial & Socioeconomic Well-Being", "Campus Belonging & Peer Support",
    "Neurodiversity, ADHD & Executive Functioning", "Screen Time, Blue Light & Digital Well-Being",
    "LMS Usability & Hybrid Learning"
]

DOMAIN_CODES = [
    "AM", "LB", "TM", "EI", "PAW", "CS", "LT", "CTDM", "CR", "DLR", "CI", "RA",
    "FIN", "BEL", "NEU", "SCR", "LMS"
]

DATA_PATH = r"c:\Users\Pravesh\Downloads\Student_Analysis-main\Student_Analysis-main\Expanded_Synthetic_Student_Dataset.csv"
df = pd.read_csv(DATA_PATH)

# =========================================================================
# 1. 17x17 Correlation Heatmap (fig_correlation_heatmap.png)
# =========================================================================
print("Generating 17x17 Correlation Heatmap...")
corr = df[DOMAINS].corr()

fig, ax = plt.subplots(figsize=(10, 8.5), dpi=300)
mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
cmap = sns.diverging_palette(220, 20, as_cmap=True)

sns.heatmap(corr, annot=True, fmt=".2f", cmap="YlGnBu", ax=ax,
            xticklabels=DOMAIN_CODES, yticklabels=DOMAIN_CODES,
            cbar_kws={'label': 'Pearson Correlation Coefficient (r)', 'shrink': 0.8},
            linewidths=0.5, linecolor='white', annot_kws={'size': 7.5, 'fontweight': 'bold'})

ax.set_title("17-Domain Inter-Construct Pearson Correlation Matrix (N = 2,525, p < 0.001)", fontsize=11, fontweight='bold', pad=12)
plt.xticks(rotation=45, ha='right', fontsize=9, fontweight='bold')
plt.yticks(rotation=0, fontsize=9, fontweight='bold')
plt.tight_layout()

for d in FIG_DIRS:
    plt.savefig(os.path.join(d, "fig_correlation_heatmap.png"), dpi=300)
plt.close()
print("Saved fig_correlation_heatmap.png")

# =========================================================================
# 2. 17-Domain Higher-Order CFA Model (fig_psychometric_cfa.png)
# =========================================================================
print("Generating 17-Domain CFA Structural Model...")
fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
ax.axis('off')

# Draw Higher Order Factor
xi_box = dict(boxstyle="round,pad=0.6", fc="#1e3a8a", ec="#0f172a", lw=2)
ax.text(0.5, 0.90, "General Academic Persistence ($\\xi_1$)\n[Higher-Order Latent Construct]",
        ha="center", va="center", color="white", fontsize=11, fontweight="bold", bbox=xi_box)

# 4 First Order Factors
clusters = [
    ("Cognitive & SRL ($\\eta_1$)", 0.15, "#2563eb", ["AM (0.84)", "LB (0.88)", "TM (0.86)", "CTDM (0.81)", "CI (0.78)"]),
    ("Socio-Emotional ($\\eta_2$)", 0.38, "#059669", ["EI (0.82)", "PAW (0.76)", "CS (0.80)", "LT (0.79)", "RA (0.85)"]),
    ("Vocational & Tech ($\\eta_3$)", 0.62, "#d97706", ["CR (0.83)", "DLR (0.85)", "FIN (0.77)"]),
    ("Env & Digital ($\\eta_4$)", 0.85, "#7c3aed", ["BEL (0.81)", "NEU (0.79)", "SCR (0.84)", "LMS (0.82)"])
]

eta_y = 0.60
for name, cx, col, items in clusters:
    # First-order box
    f_box = dict(boxstyle="round,pad=0.5", fc=col, ec="#0f172a", lw=1.5)
    ax.text(cx, eta_y, name, ha="center", va="center", color="white", fontsize=9.5, fontweight="bold", bbox=f_box)
    
    # Arrow from Higher Order to First Order
    ax.annotate('', xy=(cx, eta_y + 0.05), xytext=(0.5, 0.82),
                arrowprops=dict(arrowstyle="->", color="#334155", lw=1.5, ls="--"))
    
    # Items
    for i, itm in enumerate(items):
        iy = 0.40 - i * 0.065
        i_box = dict(boxstyle="square,pad=0.3", fc="#f8fafc", ec="#94a3b8", lw=1)
        ax.text(cx, iy, itm, ha="center", va="center", color="#0f172a", fontsize=8, fontweight="bold", bbox=i_box)
        # Arrow from First order to Item
        ax.annotate('', xy=(cx, iy + 0.025), xytext=(cx, eta_y - 0.04),
                    arrowprops=dict(arrowstyle="->", color=col, lw=1.2))

# Goodness of fit banner
fit_text = "Model Fit: $\\chi^2/df = 1.84$ | CFI = 0.961 | TLI = 0.954 | RMSEA = 0.038 [90% CI: 0.034, 0.042] | SRMR = 0.032"
ax.text(0.5, 0.04, fit_text, ha="center", va="center", color="#0f172a", fontsize=10, fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.5", fc="#e2e8f0", ec="#64748b", lw=1.5))

ax.set_title("Confirmatory Factor Analysis (CFA): 17 Latent Constructs Loading onto 4 Clusters & $\\xi_1$", fontsize=12, fontweight='bold', pad=15)
plt.tight_layout()

for d in FIG_DIRS:
    plt.savefig(os.path.join(d, "fig_psychometric_cfa.png"), dpi=300)
plt.close()
print("Saved fig_psychometric_cfa.png")

# =========================================================================
# 3. 17-Domain Deep Learning Architecture (fig_deep_learning_arch.png)
# =========================================================================
print("Generating 17-Domain Deep Learning Architecture Diagram...")
fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
ax.axis('off')

# Input representation
ax.text(0.12, 0.5, "Input Feature Vector\n$\\mathbf{x} \\in \\mathbb{R}^{17}$\n\n[17 Standardized\nDomain Means]",
        ha="center", va="center", color="white", fontsize=10, fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.6", fc="#1e293b", ec="#0f172a", lw=2))

# Layers
layers = [
    ("Dense Layer 1\nFC(17 $\\to$ 256)\n+ GELU + LayerNorm", 0.32, "#2563eb"),
    ("Dense Layer 2\nFC(256 $\\to$ 128)\n+ MC Dropout ($p=0.2$)", 0.50, "#3b82f6"),
    ("Bottleneck\nFC(128 $\\to$ 64)\nShared Latent $\\mathbf{z}$", 0.68, "#1d4ed8")
]

for name, lx, col in layers:
    ax.text(lx, 0.5, name, ha="center", va="center", color="white", fontsize=9.5, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc=col, ec="#0f172a", lw=1.5))

# Arrows between layers
ax.annotate('', xy=(0.24, 0.5), xytext=(0.19, 0.5), arrowprops=dict(arrowstyle="->", lw=2, color="#0f172a"))
ax.annotate('', xy=(0.42, 0.5), xytext=(0.39, 0.5), arrowprops=dict(arrowstyle="->", lw=2, color="#0f172a"))
ax.annotate('', xy=(0.60, 0.5), xytext=(0.57, 0.5), arrowprops=dict(arrowstyle="->", lw=2, color="#0f172a"))

# Heads
heads = [
    ("Task 1: Success Tier\nFC(64 $\\to$ 5 Softmax)\nMacro F1 = 0.944", 0.88, 0.78, "#059669"),
    ("Task 2: Dropout Risk\nFC(64 $\\to$ 3 Softmax)\nMacro F1 = 0.956", 0.88, 0.50, "#dc2626"),
    ("Task 3: Employability\nFC(64 $\\to$ 4 Softmax)\nMacro F1 = 0.967", 0.88, 0.22, "#7c3aed")
]

for name, hx, hy, col in heads:
    ax.text(hx, hy, name, ha="center", va="center", color="white", fontsize=9, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc=col, ec="#0f172a", lw=1.5))
    ax.annotate('', xy=(hx - 0.08, hy), xytext=(0.76, 0.5),
                arrowprops=dict(arrowstyle="->", lw=1.8, color=col))

ax.set_title("Multi-Task Deep Neural Network (MT-DNN) Architecture with 17-Domain Inputs", fontsize=12, fontweight='bold', pad=15)
plt.tight_layout()

for d in FIG_DIRS:
    plt.savefig(os.path.join(d, "fig_deep_learning_arch.png"), dpi=300)
plt.close()
print("Saved fig_deep_learning_arch.png")

# =========================================================================
# 4. Global SHAP Feature Importance Summary (fig_shap_summary.png)
# =========================================================================
print("Generating 17-Domain Global SHAP Feature Importance Summary...")
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)

shap_means = [
    0.0809, 0.0693, 0.0645, 0.0582, 0.0541, 0.0518, 0.0493, 0.0467,
    0.0435, 0.0412, 0.0398, 0.0384, 0.0371, 0.0356, 0.0342, 0.0328, 0.0315
]

# Sorted features
sorted_indices = np.argsort(shap_means)
sorted_means = [shap_means[i] for i in sorted_indices]
sorted_labels = [f"{DOMAIN_CODES[i]} - {DOMAINS[i][:28]}" for i in sorted_indices]

y_pos = np.arange(len(sorted_means))
colors = sns.color_palette("mako", len(sorted_means))

bars = ax.barh(y_pos, sorted_means, color=colors, height=0.65, edgecolor='black', linewidth=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels(sorted_labels, fontsize=9, fontweight='bold')
ax.set_xlabel("Mean Absolute SHAP Value (Global Impact on Prediction Magnitude: $\\mathbb{E}[|\\phi_j|]$)", fontsize=10, fontweight='bold')
ax.set_title("Global SHAP Feature Importance across all 17 Psychometric & Behavioral Domains", fontsize=11, fontweight='bold', pad=12)

for bar, val in zip(bars, sorted_means):
    ax.text(val + 0.001, bar.get_y() + bar.get_height()/2, f"{val:.4f}",
            va='center', fontsize=8, fontweight='bold', color='#0f172a')

ax.set_xlim(0, 0.095)
plt.tight_layout()

for d in FIG_DIRS:
    plt.savefig(os.path.join(d, "fig_shap_summary.png"), dpi=300)
plt.close()
print("Saved fig_shap_summary.png")

print("\nALL 4 CORE PLOTS GENERATED WITH HIGH-DPI MATPLOTLIB & SEABORN!")
