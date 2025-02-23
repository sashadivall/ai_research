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
    filtered_data2 = filtered_data[(filtered_data["Ethics Course Breadth Score"] != 0) & (filtered_data["Ethics Course Depth Score"] != 0)]
    # print(len(filtered_data["Undergrad Enrollement"]))

    # dashed_score_plot(filtered_data, "Theory Score", "Application Score", "theory_v_application")
    # dashed_score_plot(filtered_data, "Ethics Score (Intro Course Description)", "Ethics Course Score", "ethics_intro_v_ethics_course")

    scatter = plt.scatter(x="Theory Score", y="Application Score", data=filtered_data, 
                          s=filtered_data["Undergrad Enrollement"] / filtered_data["Undergrad Enrollement"].max() * 100, 
                          label="Undergrad Enrollment", color="firebrick")
    plt.xlim(0, 5)
    plt.ylim(0, 5)

    # Add labels for each point
    for i, row in filtered_data.iterrows():
        plt.text(row["Theory Score"], row["Application Score"] + 0.1, row["University Abbreviation"], fontsize=9, ha='center')

    # Create a legend for the sizes
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=5, func=lambda s: s * filtered_data["Undergrad Enrollement"].max() / 100)
    size_legend = plt.legend(handles, labels, loc="lower left", title="Enrollment Size")
    plt.grid(axis="x", linestyle="--", alpha=0.1)
    plt.grid(axis="y", linestyle="--", alpha=0.1)
    plt.title("Theory Score vs. Application Score, Intro To AI Course", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Theory Score")
    plt.ylabel("Application Score")
    plt.gca().add_artist(size_legend)
    plt.savefig("viz/imgs/theory_v_application_2.png")
    plt.show()

    scatter2 = plt.scatter(x="Ethics Course Breadth Score", y="Ethics Course Depth Score", data=filtered_data2, 
                          s=filtered_data2["Undergrad Enrollement"] / filtered_data2["Undergrad Enrollement"].max() * 100, 
                          label="Undergrad Enrollment", color="firebrick")
    plt.xlim(0, 6)
    plt.ylim(0, 6)

    # Add labels for each point
    # for i, row in filtered_data.iterrows():
    #     plt.text(row["Ethics Course Breadth Score"], row["Ethics Course Depth Score"] - 0.2, row["University Abbreviation"], fontsize=9, ha='center')

    # Create a legend for the sizes
    handles, labels = scatter2.legend_elements(prop="sizes", alpha=0.6, num=5, func=lambda s: s * filtered_data2["Undergrad Enrollement"].max() / 100)
    size_legend = plt.legend(handles, labels, loc="upper left", title="Enrollment Size")
    plt.grid(axis="x", linestyle="--", alpha=0.1)
    plt.grid(axis="y", linestyle="--", alpha=0.1)
    plt.title("Breadth Score vs. Depth Score, AI Ethics Course", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Breadth Score")
    plt.ylabel("Depth Score")
    plt.gca().add_artist(size_legend)
    plt.savefig("viz/imgs/depth_vs_breadth.png")
    plt.show()

if __name__ == "__main__":
    main()