#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:09:34 2025

@author: mollyvarrenti
"""

import pandas as pd
import plotly.graph_objects as go
import os

# Load the Excel file
file_path = 'data/colleges_data.csv'
df = pd.read_csv(file_path)

# Ensure all descriptions are strings
df['Intro to AI Course Description'] = df['Intro to AI Course Description'].astype(str)

# Extract keywords from 'Intro to AI Course Description'
keywords_to_filter = ["learning", "machine", "artificial", "intelligence", "neural",
    "processing", "supervised", "unsupervised", "language", "deep",
    "reinforcement", "natural", "vision", "decision", "bias",
    "classification", "probability", "inference", "optimization", "network",
    "theory", "application", "mathematical", "statistical", "computational",
    "analysis", "modeling", "systems", "principles", "methods", "data",
    "training", "development", "evaluation", "implementation", "technology",
    "automation", "reasoning", "cognitive", "performance", "framework"]

df['Keywords'] = df['Intro to AI Course Description'].apply(
    lambda x: [word.lower() for word in x.split() if word.lower() in keywords_to_filter]
)

# Flatten the list of keywords and create a unique list of keywords
all_keywords = [keyword for sublist in df['Keywords'].tolist() for keyword in sublist]
unique_keywords = list(set(all_keywords))

# Create the Sankey diagram
university_names = df['University Name'].tolist()
labels = university_names + unique_keywords

source_indices = []
target_indices = []

for i, keywords in enumerate(df['Keywords']):
    for keyword in keywords:
        source_indices.append(labels.index(university_names[i]))
        target_indices.append(labels.index(keyword))

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=[1]*len(source_indices)
    )
)])

fig.update_layout(title_text="Sankey Diagram of Universities and AI Course Keywords", font_size=10)

# Ensure the directory exists
output_dir = 'sankey_code/imgs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the Sankey diagram to the specified file path
output_file_path = os.path.join(output_dir, 'sankey_diagram.html')
fig.write_html(output_file_path)

print(f"Sankey diagram saved to {output_file_path}")