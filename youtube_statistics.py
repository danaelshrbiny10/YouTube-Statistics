"""Global YouTube Statistics."""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("dataset\Global YouTube Statistics.csv", encoding="unicode_escape")

df = pd.DataFrame(
    data,
    columns=[
        "Youtuber",
        "rank",
        "video views",
        "subscribers",
        "Population",
    ],
)

df.set_index("Youtuber")

numeric_columns = df.select_dtypes(include=["number"])

if not numeric_columns.empty:
    ax = numeric_columns.plot(
        figsize=(10, 6),
        title="YouTube Statistics for Top YouTubers",
        marker="o",
        rot=45,
    )

    plt.xlabel("YouTuber")
    plt.ylabel("Counts")
    plt.legend(title="Statistics")

    N = 100
    for column in numeric_columns.columns:
        top_N_values = numeric_columns.nlargest(N, column)
        for index, row in top_N_values.iterrows():
            x = index
            y = row[column]
            label = "{:.0f}".format(y)
            ax.annotate(
                label,
                (x, y),
                textcoords="offset points",
                xytext=(0, 995),
                ha="center",
            )

    plt.tight_layout()
    plt.show()
else:
    print("No numeric data available for plotting.")
