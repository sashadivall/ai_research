#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:57:43 2025

@author: mollyvarrenti
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the CSV file with error handling
file_path = Path('data/scored_colleges.csv')
df = pd.read_csv(file_path)

# Select the relevant columns
columns = ['University Name', 'Theory Score', 'Application Score', 'Ethics Score (Intro Course Description)', 'Ethics Course Score']
df = df[columns]

# Filter out rows where all scores are 0.0
df = df[(df[columns[1:]] != 0.0).any(axis=1)]

# Set the 'University Name' column as the index
df.set_index('University Name', inplace=True)

# Define custom colors for each column (dark to light hues of red)
colors = ['#8B0000', '#B22222', '#CD5C5C', '#F08080']

# Plot the clustered bar chart with custom colors
ax = df.plot(kind='bar', edgecolor='black', figsize=(15, 8), color=colors)

# Set the labels and title
ax.set_xlabel('University Name')
ax.set_ylabel('Scores')
ax.set_title('Scores by University')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.tight_layout()

plt.savefig("viz/imgs/clustered_bar_chart.png")
plt.show()