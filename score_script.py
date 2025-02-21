import argparse
from pathlib import Path
import pandas as pd
from scoring.score import score_theory, score_application, score_ethics_intro, score_ethics_breadth, score_ethics_depth

def parse_args():
    parser = argparse.ArgumentParser(description='argument parser for gpt scoring')
    parser.add_argument(
        "--dataset_path",
        '-d',
        type=Path,
        default="data/colleges_data.csv",
        help="Path to the dataset."
    )
    return parser.parse_args()


def read_in_data(dataset_path: Path) -> pd.DataFrame:
    data = pd.read_csv(dataset_path)
    return data

def main(dataset_path: Path):
    data = read_in_data(dataset_path)
    score_theory(data)
    score_application(data)
    score_ethics_intro(data)
    score_ethics_breadth(data)
    score_ethics_depth(data)
    data.to_csv("data/scored_colleges.csv")

if __name__ == "__main__":
    args = parse_args()
    dataset_path = args.dataset_path
    main(dataset_path)