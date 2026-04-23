import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# ==========================================
# GRAPH 3: NLP Intent Confusion Matrix
# ==========================================
# Assuming 20 prompts (5 of each category) with 95% routing accuracy
categories = ['Sorting', 'Math_Op', 'UI_Comp', 'String_Manip']
# Confusion matrix data: [True Label vs Predicted Label]
conf_matrix = np.array([
    [5, 0, 0, 0],  # 5 Sorting correctly predicted
    [0, 4, 0, 1],  # 4 Math correctly predicted, 1 misclassified as String
    [0, 0, 5, 0],  # 5 UI correctly predicted
    [0, 0, 0, 5]   # 5 String correctly predicted
])

plt.figure(figsize=(7, 5))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=categories, yticklabels=categories,
            annot_kws={"size": 14, "weight": "bold"})

plt.title('Confusion Matrix: NLP Intent Classification', fontweight='bold', pad=15)
plt.xlabel('Predicted Intent (Naive Bayes)', fontweight='bold')
plt.ylabel('Actual User Intent', fontweight='bold')
plt.tight_layout()
plt.savefig('Confusion_Matrix_NLP.png', dpi=300)
print("✅ Graph saved: Confusion_Matrix_NLP.png")

# ==========================================
# GRAPH 4: AST Retry Success Distribution
# ==========================================
# Breakdown of the 8 successful generations
attempts = ['Attempt 1\n(Raw Base)', 'Attempt 2\n(AST + Temp 0.2)', 'Attempt 3\n(AST + Temp 0.3)', 'Failed\n(Discarded)']
counts = [5, 2, 1, 12]  # Total 20

plt.figure(figsize=(8, 5))
colors = ['#2ecc71', '#3498db', '#9b59b6', '#e74c3c']
bars = plt.bar(attempts, counts, color=colors, width=0.5)

# Add numeric labels on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, str(yval), 
             ha='center', va='bottom', fontweight='bold', fontsize=12)

# Draw a line showing cumulative success
cumulative_success = [5, 7, 8, 8] # 5 -> 5+2 -> 5+2+1
plt.plot(attempts[:3], cumulative_success[:3], color='#f39c12', marker='o', 
         linestyle='dashed', linewidth=2, markersize=8, label='Cumulative Success')

plt.title('Code Rescue Breakdown via AST Self-Healing Loop', fontweight='bold')
plt.ylabel('Number of Prompts', fontweight='bold')
plt.ylim(0, 14)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('AST_Retry_Breakdown.png', dpi=300)
print("✅ Graph saved: AST_Retry_Breakdown.png")