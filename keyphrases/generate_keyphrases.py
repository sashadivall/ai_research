import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from myopenai.myopenai import MyOpenAI

def extract_keyphrases(data: pd.DataFrame) -> None:
    instructions = """
    You are an expert in AI ethics and curriculum evaluation. 
    You will be given a list of course descriptions for introductory AI and machine learning classes offered at the 
    undergraduate level. For each description, you must extract a list of keywords and phrases, specifically those words and phrases in the 
    course description that are related to computer science, machine learning, and artificial intelligence.  \n\n
    Example\n
    **Course Description**: DS 340 covers the most important concepts and algorithms in AI and machine learning, ranging from search to deep neural networks, 
    with an eye toward conceptual understanding and building a final project. Important topics include varieties of search (for lookahead), probabilistic 
    reasoning, gradient descent applied to neural networks, applying regularization, reinforcement learning, the role of embeddings in natural language processing, 
    and the role of attention in transformer architectures (eg, BERT and GPT4). Applications include image classification, sentiment analysis, game playing, 
    and recommender systems, as well as a cursory introduction to generative AI. A background in Python programming is necessary, while multivariable calculus, 
    linear algebra, and probability allow a deeper understanding of the material. 
    **Resulting Topics List**: [
    "algorithms",
    "machine learning",
    "neural networks",
    "search",
    "probabilistic reasoning",
    "gradient descent",
    "regularization",
    "reinforcement learning",
    "embeddings",
    "natural language processing",
    "transformer architectures",
    "image classification",
    "sentiment analysis",
    "game playing",
    "recommender systems",
    "generative AI",
    ]
    Each word or phrase you return **MUST BE** in the course description.
    Return a string dictionary with a key `values` and a list of each course's keywords and phrases (also formatted as a list). 
    For example, you return {"values": [[keywordsforcourse1], [keywordsforcourse2]...]}.
    **DO NOT FORMAT THE STRING AS JSON**. Return the dictionary as a string
    """
    my_chat = MyOpenAI(instructions=instructions)
    intro_description = list(data["Intro to AI Course Description"])
    results = my_chat.generate_keyphrases(intro_description)
    print(results)

    keyphrases = pd.DataFrame({
        "University Name": data["University Name"],
        "Topic List": results,
    })
    keyphrases.to_csv("keyphrases/data/college_topics.csv")
    print(f"Topic List Dataframe successfully written.")

def main():
    colleges_data = pd.read_csv('data/new_colleges_data.csv')
    colleges_data = colleges_data.dropna(subset=["Intro to AI Course Description"])
    extract_keyphrases(colleges_data)

if __name__ == "__main__":
    main()
