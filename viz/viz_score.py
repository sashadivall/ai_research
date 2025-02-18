import matplotlib.pyplot as plt
import pandas as pd
import os
# Load Data
scored_data = pd.read_csv("data/scored_colleges.csv")
scored_data["University Abbreviation"] = [
    "BC", "BU", "Emmanuel", "Fisher", "Harvard", "MIT", "NEU", 
    "Simmons", "Suffolk", "UMB", "WIT"
]

# Filter out zero values
filtered_data = scored_data[(scored_data["Theory Score"] != 0) & (scored_data["Application Score"] != 0)]

# Create Figure
plt.figure(figsize=(10, 6), dpi=150)

# Plot Dashed Lines Connecting Theory and Application Scores
for i in range(len(filtered_data)):
    plt.plot([filtered_data["University Abbreviation"].iloc[i], filtered_data["University Abbreviation"].iloc[i]], 
             [filtered_data["Theory Score"].iloc[i], filtered_data["Application Score"].iloc[i]], 
             color="gray", linestyle="--", linewidth=1)

# Scatter Plots for Theory and Application Scores
plt.scatter(x=filtered_data["University Abbreviation"], y=filtered_data["Theory Score"], 
            marker='o', label='Theory Score', s=100, c="#1f77b4", edgecolors="black")
plt.scatter(x=filtered_data["University Abbreviation"], y=filtered_data["Application Score"], 
            marker='o', label='Application Score', s=100, c="#d62728", edgecolors="black")

# Formatting & Labels
plt.legend(fontsize=12, loc="upper right", frameon=True, edgecolor="black")
plt.title("Theory vs. Application Scores in Boston Universities", fontsize=14, fontweight="bold", pad=15)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel("University", fontsize=13, fontweight="bold")
plt.ylabel("Score", fontsize=13, fontweight="bold")
plt.grid(axis="y", linestyle="--", alpha=0.1)
plt.tight_layout()
plt.savefig("viz/imgs/theory_v_application.png")

# Display the Plot
plt.show()
