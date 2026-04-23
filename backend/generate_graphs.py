import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the CSV Data
try:
    df = pd.read_csv('research_results.csv')
except FileNotFoundError:
    print("Error: 'research_results.csv' nahi mila. Pehle benchmark script run karein.")
    exit()

# Set visual style
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# GRAPH 1: Overall Success Rate & The Impact of AST
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))

# Calculate categories
total = len(df)
success_first_try = len(df[(df['Success Status'] == 'Pass') & (df['Attempts Needed'] == 1)])
success_auto_corrected = len(df[(df['Success Status'] == 'Pass') & (df['Attempts Needed'] > 1)])
failed = len(df[df['Success Status'] == 'Fail'])

labels = ['Success (1st Try)', 'Auto-Corrected (By AST)', 'Failed']
sizes = [success_first_try, success_auto_corrected, failed]
colors = ['#4ade80', '#facc15', '#f87171']
explode = (0, 0.1, 0)  # Highlight the auto-corrected slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140, textprops={'fontsize': 12, 'weight': 'bold'})
plt.title('Impact of AST Self-Healing on CodeGen-350M', fontsize=16, fontweight='bold', pad=20)

# Save Graph 1
plt.savefig('AST_Impact_Chart.png', bbox_inches='tight')
print("✅ Created: AST_Impact_Chart.png")

# ---------------------------------------------------------
# GRAPH 2: Intent Accuracy (Kaunsa topic AI ko easy laga?)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))

# Group by Intent and calculate success
intent_success = df.groupby('Expected Intent')['Success Status'].apply(lambda x: (x == 'Pass').sum()).reset_index()
intent_success.rename(columns={'Success Status': 'Successful Generations'}, inplace=True)

# Create Bar Chart
ax = sns.barplot(x='Expected Intent', y='Successful Generations', data=intent_success, palette='viridis')
plt.title('Generation Success Rate by Intent Category', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('NLP Intent Category', fontsize=12)
plt.ylabel('Number of Successful Outputs', fontsize=12)
plt.ylim(0, 5) # Since we tested 5 per category

# Save Graph 2
plt.savefig('Intent_Success_Bar.png', bbox_inches='tight')
print("✅ Created: Intent_Success_Bar.png")

