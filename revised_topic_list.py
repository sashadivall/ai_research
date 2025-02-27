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
file_path = "/Users/mollyvarrenti/Desktop/Desktop - Molly’s MacBook Pro/RISE Materials/college_topics.csv"
df = pd.read_csv(file_path)

# Clean and split the 'Topic List' column into individual topics
def clean_topic_list(topic_str):
    topics = re.sub(r"[\[\]']", '', str(topic_str)).split(', ')
    return [topic.strip().lower() for topic in topics]

df['Cleaned Topics'] = df['Topic List'].apply(clean_topic_list)

# Define broad topic categories with expanded topics
topic_mapping = {
    'neural networks': ['deep learning', 'neural network architectures', 'artificial neural networks', 'backpropagation', 'convolutional neural networks', 'recurrent neural networks'],
    'machine learning': ['machine learning', 'supervised learning', 'unsupervised learning', 'reinforcement learning', 'transfer learning', 'semi-supervised learning'],
    'artificial intelligence': ['artificial intelligence', 'ai', 'intelligent systems', 'knowledge representation', 'planning', 'expert systems'],
    'data science': ['data analysis', 'data mining', 'big data', 'data visualization', 'data cleaning', 'feature engineering', 'data wrangling'],
    'algorithms': ['algorithms', 'graph algorithms', 'sorting algorithms', 'search algorithms', 'divide and conquer', 'greedy algorithms'],
    'optimization': ['optimization', 'convex optimization', 'linear programming', 'integer programming', 'dynamic programming', 'stochastic optimization'],
    'probability and statistics': ['probabilistic view', 'statistics', 'bayesian methods', 'hypothesis testing', 'regression analysis', 'sampling methods'],
    'natural language processing': ['nlp', 'natural language processing', 'text mining', 'sentiment analysis', 'named entity recognition', 'text summarization'],
    'computer vision': ['computer vision', 'image processing', 'object detection', 'image classification', 'image segmentation', 'face recognition'],
    'robotics': ['robotics', 'autonomous systems', 'control theory', 'robot motion planning', 'robot perception', 'robotic manipulation'],
    'bioinformatics': ['bioinformatics', 'computational biology', 'genomics', 'proteomics', 'bioinformatics algorithms', 'drug discovery'],
    'theoretical computer science': ['theoretical computer science', 'complexity theory', 'computational theory', 'automata theory', 'computational models'],
    'software engineering': ['software engineering', 'programming languages', 'software design', 'software testing', 'version control', 'agile methodologies'],
    'cybersecurity': ['cybersecurity', 'cryptography', 'network security', 'cyberattack detection', 'firewalls', 'vulnerability management'],
    'databases': ['databases', 'sql', 'database management', 'noSQL', 'data normalization', 'query optimization'],
    'human-computer interaction': ['human-computer interaction', 'hci', 'usability', 'user experience', 'interface design', 'user-centered design'],
    'cloud computing': ['cloud computing', 'distributed systems', 'cloud infrastructure', 'cloud storage', 'cloud security', 'cloud computing services'],
    'quantum computing': ['quantum computing', 'quantum algorithms', 'quantum cryptography', 'quantum machine learning', 'quantum information theory'],
    'computational neuroscience': ['computational neuroscience', 'brain modeling', 'neuron modeling', 'cognitive neuroscience', 'neural networks', 'neural signal processing'],
    'computer graphics': ['computer graphics', '3d modeling', 'rendering', 'graphics programming', 'ray tracing', 'computer animation'],
    'blockchain technology': ['blockchain', 'cryptocurrency', 'decentralized finance', 'smart contracts', 'blockchain security'],
    'internet of things': ['internet of things', 'smart devices', 'IoT security', 'IoT networks', 'sensor networks'],
    'augmented reality': ['augmented reality', 'virtual reality', 'mixed reality', 'immersive technologies', 'AR development'],
    'edge computing': ['edge computing', 'fog computing', 'distributed computing', 'low latency processing', 'real-time data processing'],
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
