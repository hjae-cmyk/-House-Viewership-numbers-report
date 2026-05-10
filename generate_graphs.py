import pandas as pd
import matplotlib.pyplot as plt
import os

# Data preparation
data = {
    'Season': [1, 2, 3, 4, 5, 6, 7, 8],
    'Viewers_Millions': [13.34, 17.35, 19.95, 17.64, 13.62, 12.76, 10.32, 8.69]
}

df = pd.DataFrame(data)

# Calculate season-to-season changes
df['Change'] = df['Viewers_Millions'].diff()

# Set up the plot style
plt.style.use('seaborn-v0_8-whitegrid')

# 1. Graph of viewership over time
plt.figure(figsize=(10, 6))
plt.plot(df['Season'], df['Viewers_Millions'], marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
plt.title('House M.D. Average Viewership per Season', fontsize=16)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Viewers (Millions)', fontsize=14)
plt.xticks(df['Season'])
plt.grid(True, linestyle='--', alpha=0.7)
for i, v in enumerate(df['Viewers_Millions']):
    plt.text(df['Season'][i], v + 0.3, f"{v:.2f}", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('/home/ubuntu/House-Report/viewership_over_time.png', dpi=300)
plt.close()

# 2. Graph of season-to-season changes
plt.figure(figsize=(10, 6))
colors = ['g' if x > 0 else 'r' for x in df['Change']]
plt.bar(df['Season'][1:], df['Change'][1:], color=colors[1:], alpha=0.7)
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.title('House M.D. Season-to-Season Viewership Changes', fontsize=16)
plt.xlabel('Season Transition', fontsize=14)
plt.ylabel('Change in Viewers (Millions)', fontsize=14)
plt.xticks(df['Season'][1:], [f"S{i-1} to S{i}" for i in df['Season'][1:]])
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(df['Change'][1:]):
    plt.text(df['Season'][i+1], v + (0.2 if v > 0 else -0.5), f"{v:+.2f}", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('/home/ubuntu/House-Report/viewership_changes.png', dpi=300)
plt.close()

print("Graphs generated successfully.")
