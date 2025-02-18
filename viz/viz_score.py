import matplotlib.pyplot as plt
import pandas as pd

def dashed_score_plot(df, score1, score2, img_path):
    plt.figure(figsize=(10, 6), dpi=150)

    # Plot Dashed Lines Connecting Theory and Application Scores
    for i in range(len(df)):
        plt.plot([df["University Abbreviation"].iloc[i], df["University Abbreviation"].iloc[i]], 
                [df[score1].iloc[i], df[score2].iloc[i]], 
                color="gray", linestyle="--", linewidth=1)

    # Scatter Plots for Theory and Application Scores
    plt.scatter(x=df["University Abbreviation"], y=df[score1], 
                marker='o', label=score1, s=100, c="#1f77b4", edgecolors="black")
    plt.scatter(x=df["University Abbreviation"], y=df[score2], 
                marker='o', label=score2, s=100, c="#d62728", edgecolors="black")

    # Formatting & Labels
    plt.legend(fontsize=12, loc="upper right", frameon=True, edgecolor="black")
    plt.title(f"{score1} vs. {score2} in Boston Universities", fontsize=14, fontweight="bold", pad=15)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel("University", fontsize=13, fontweight="bold")
    plt.ylabel("Score", fontsize=13, fontweight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.1)
    plt.tight_layout()
    plt.savefig(f"viz/imgs/{img_path}.png")

    # Display the Plot
    plt.show()
def main():
    scored_data = pd.read_csv("data/scored_colleges.csv")
    scored_data["University Abbreviation"] = [
        "BC", "BU", "Emmanuel", "Fisher", "Harvard", "MIT", "NEU", 
        "Simmons", "Suffolk", "UMB", "WIT"
    ]

    # Filter out zero values
    filtered_data = scored_data[(scored_data["Theory Score"] != 0) & (scored_data["Application Score"] != 0)]

    dashed_score_plot(filtered_data, "Theory Score", "Application Score", "theory_v_application")
    dashed_score_plot(filtered_data, "Ethics Score (Intro Course Description)", "Ethics Course Score", "ethics_intro_v_ethics_course")

if __name__ == "__main__":
    main()