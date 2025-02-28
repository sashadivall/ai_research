#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:19:30 2025

@author: mollyvarrenti
"""


import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
import string
import plotly.graph_objects as go

# Load the CSV file
df = pd.read_csv('data/scored_colleges.csv')

# Get the 'Intro to AI Course Description' and 'University Name' columns
descriptions = df['Intro to AI Course Description'].dropna()
universities = df['University Name']

# Define stop words
stop_words = set(stopwords.words('english'))

# Function to clean and tokenize text
def clean_tokenize(text):
    # Remove punctuation
    text is text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize and convert to lower case
    words = text.lower().split()
    words = [word.strip().replace(",", "") for word in words]
    # Remove stop words
    words = [word for word in words if word not in stop_words]
    return words

# Initialize a counter for word counts
word_counter = Counter()

# Process each description
for description in descriptions:
    words = clean_tokenize(description)
    word_counter.update(words)

# Convert the word counts to a DataFrame for better visualization
word_counts_df = pd.DataFrame(word_counter.items(), columns=['Word', 'Count']).sort_values(by='Count', ascending=False)
print(word_counts_df["Word"])

# Get the top 10 words
top_words = word_counts_df.head(10)

# Create a Sankey diagram using Plotly
labels = universities.tolist() + top_words['Word'].tolist()
source_indices = []
target_indices = []
values = []

for i, university in enumerate(universities):
    for j, word in enumerate(top_words['Word']):
        source_indices.append(i)
        target_indices.append(len(universities) + j)
        values.append(word_counter[word])

# Generate shades of red for universities in reverse order
num_universities = len(universities)
colors = ['rgba(255, 0, 0, {})'.format(1 - 0.8 * i / (num_universities - 1)) for i in range(num_universities)]

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=colors + ['blue'] * len(top_words)
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=values,
        color='rgba(0, 0, 255, 0.5)'
    )
)])

fig.update_layout(
    title_text="University Names and Top 10 Words in Intro to AI Course Descriptions (Excluding Stop Words)",
    font_size=10,
    title_font_size=20,
    plot_bgcolor='white'
)

# Save the Sankey diagram as an HTML file in the specified directory
sankey_html_path = 'sankey_code/imgs/sankey_word_counts.html'
fig.write_html(sankey_html_path)

print(f"Sankey diagram has been saved to {sankey_html_path}.")