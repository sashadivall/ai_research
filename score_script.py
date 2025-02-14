import argparse
from pathlib import Path
import pandas as pd
from scoring.score import score_application, score_ethics, score_theory

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
    # score_application(data)
    # score_ethics(data)
    # print(data.info())

if __name__ == "__main__":
    args = parse_args()
    dataset_path = args.dataset_path
    main(dataset_path)