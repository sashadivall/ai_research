#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:05:52 2025

@author: mollyvarrenti
"""

import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
file_path = 'keyphrases/data/college_topics_revised.csv'
df = pd.read_csv(file_path)

# Ensure the column headers are correctly read
df.columns = df.columns.str.strip()

# Extract the relevant columns by their names
university_names = df['University Name']
topics_revised = df['Topic List Revised']

# Split the topics into individual topics
topics_revised_split = topics_revised.str.split(', ').apply(lambda x: [topic for topic in x if topic and topic != "other"])
print(topics_revised_split)

# Create a list of unique labels
labels = list(pd.concat([university_names, pd.Series([item for sublist in topics_revised_split for item in sublist])]).unique())

# Create a mapping from labels to indices
label_indices = {label: i for i, label in enumerate(labels)}

# Create the source and target indices for the Sankey diagram
sources = []
targets = []
values = []

for i, university in enumerate(university_names):
    for topic in topics_revised_split[i]:
        sources.append(label_indices[university])
        targets.append(label_indices[topic])
        values.append(1)  # Assign a value of 1 for each link

# Assign colors to nodes
colors = ['#636EFA'] * len(university_names.unique()) + ['#EF553B'] * (len(labels) - len(university_names.unique()))
# Identify the index of Northeastern University
northeastern_index = label_indices.get('Northeastern University')

# Assign colors to links
link_colors = ['indianred' if source == northeastern_index else 'lightblue' for source in sources]
# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        hoverlabel=dict(bgcolor='white', font_size=12, font_family='Arial'),
        color=link_colors,
        line=dict(color='darkgrey', width=0.5)
    )
)])

# Update layout and save the figure
fig.update_layout(title_text="Enhanced Sankey Diagram of University Names and Topics", font_size=10, font_color="black")
output_path = 'keyphrases/imgs/sankey_diagram.html'
fig.write_html(output_path)

print(f"Sankey diagram saved to {output_path}")