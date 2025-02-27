#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:51:55 2025

@author: mollyvarrenti
"""

import os
import pandas as pd
import re

# Path to your original file
file_path = "keyphrases/data/college_topics.csv"
df = pd.read_csv(file_path)

# Clean and split the 'Topic List' column into individual topics
def clean_topic_list(topic_str):
    topics = re.sub(r"[\[\]']", '', str(topic_str)).split(', ')
    return [topic.strip().lower() for topic in topics]

df['Cleaned Topics'] = df['Topic List'].apply(clean_topic_list)

# Define broad topic categories with expanded topics
topic_mapping = {
    "machine learning": [
        "supervised learning", "unsupervised learning", "reinforcement learning", 
        "deep learning", "computational learning theory", "meta-learning",
        "instance-based learning", "inductive bias", "overfitting", "regularization",
        "gradient-based methods", "gradient descent", "boosting",  
        "transformer architectures"
    ],
    "ml techniques": [
        "support vector machines", "decision trees", "classification", "clustering", 
        "ensemble methods", "feature space representations", "kernel methods", 
        "deterministic tasks", "stochastic tasks"
    ],
    "artificial intelligence": [
        "artificial intelligence", "AI techniques", "automation", "generative AI",
        "multiagent systems", "automated deduction", "heuristic search", "state-space search methods", "knowledge representation", 
        "search"
    ],
    "game playing": [
        "game playing", "robotics", "planning"
    ],
    "problem solving and decision making": [
        "problem-solving", "decision-making", 
    ],
    "natural language processing": [
        "natural language processing", "sentiment analysis", "embeddings"
    ],
    "computer vision": [
        "computer vision", "image classification"
    ],
    "probabilistic methods": [
        "probabilistic reasoning", "Bayesian approaches", 
        "hidden Markov models", "maximum likelihood", "uncertain reasoning", "reasoning under uncertainty", "reasoning"
    ],
    "logic and theorem proving": [
        "logic", "predicate calculus", "theorem-proving", "graphical models", 
    ],
    "neural networks": [
        "neural networks", "neural-network architectures"
    ],
    "bias and ethics": [
        "bias", "human-computer interaction"
    ],
    "systems": [
        "expert systems", "recommender systems", "personalized information filtering", "association",
        "production rule systems", 
    ],
    "analytics and optimization": [
        "business analytics", "evaluation", "optimization"
    ]
}


# Reverse mapping for quick lookup
reverse_mapping = {}
for broad_topic, specific_topics in topic_mapping.items():
    for specific_topic in specific_topics:
        reverse_mapping[specific_topic] = broad_topic

# Map detailed topics to broader categories
def map_topics(topics):
    mapped_topics = {}
    for topic in topics:
        mapped_topics[topic] = reverse_mapping.get(topic, "other")
    return mapped_topics

df['Mapped Topics'] = df['Cleaned Topics'].apply(map_topics)

# Create 'Topic List Revised'
def create_revised_topic_list(mapped_topics):
    revised_topics = list(dict.fromkeys(mapped_topics.values()))
    return ', '.join(revised_topics)

df['Topic List Revised'] = df['Mapped Topics'].apply(create_revised_topic_list)

# Add the 'Unique Topic Count' column to count the number of unique topics in the 'Topic List Revised'
def count_unique_topics(topic_list):
    topics = topic_list.split(', ')
    return len(set(topics))

df['Unique Topic Count'] = df['Topic List Revised'].apply(count_unique_topics)
print(df)
# Save new CSV to the same directory as the original file
output_file = os.path.join(os.path.dirname(file_path), 'college_topics_revised.csv')
df[['University Name', 'Topic List', 'Topic List Revised', 'Unique Topic Count']].to_csv(output_file, index=False)

print(f"CSV file saved at: {output_file}")
