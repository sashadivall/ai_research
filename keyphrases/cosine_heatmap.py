import numpy as np
import pandas as pd
import ast
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

def vectorize(topics, vocabulary):
    return np.array([1 if term in topics else 0 for term in vocabulary])

def compute_cosine_similarities(data: pd.DataFrame) -> None:
   # data["Topic List Revised"] = data["Topic List Revised"].apply(ast.literal_eval)
    
    vocabulary = list(set(topic for topics in data["Topic List Revised"] for topic in topics))

    vectors = data["Topic List Revised"].apply(lambda topics: vectorize(topics, vocabulary))

    # Compute cosine similarity matrix
    vectors = np.stack(vectors.values)  # Convert list of vectors to a matrix
    cosine_sim_matrix = cosine_similarity(vectors)

    plt.figure(figsize=(10, 8))
    sns.heatmap(cosine_sim_matrix, annot=True, cmap="viridis", xticklabels=data["University Abbreviation"], yticklabels=data["University Abbreviation"])

    plt.title("Intro to AI Course Cosine Similarity Based on Topic Vectors​")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.savefig("keyphrases/imgs/cosine_similarity.png")
    plt.show()


def main():
    data = pd.read_csv('keyphrases/data/college_topics_revised.csv')
    data["University Abbreviation"] = [
        "BC", "BU", "Emmanuel", "Harvard", "MIT", "NEU", 
        "Simmons", "Suffolk", "UMB", "WIT"
    ]
    compute_cosine_similarities(data)


if __name__ == "__main__":
    main()