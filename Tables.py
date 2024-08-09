import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\marty\PycharmProjects\data.csv", names=["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"])

sexCount = data["Sex"].value_counts()
sexPercentage = data["Sex"].value_counts(normalize=True) * 100
sexPercentage = sexPercentage.round(2)

result = pd.DataFrame(
    {
        "count": sexCount,
        "%": sexPercentage
    }
)

result.index = ["Male", "Female", "Infant"]

print(result, "\n")

quantativeValues = ["Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"]
quantativeTable = data[quantativeValues]

summaryTable = pd.DataFrame(
    {
        "mean": quantativeTable.mean().round(2),
        "std": quantativeTable.std().round(2),
        "min": quantativeTable.min().round(2),
        "25%": quantativeTable.quantile(0.25).round(2),
        "50%": quantativeTable.median().round(2),
        "75%": quantativeTable.quantile(0.75).round(2),
        "max": quantativeTable.max().round(2)
    }
)

print(summaryTable)

plt.figure(figsize=[10,7])
bars = sexCount.plot(kind="bar", color=["blue", "green", "yellow"])
plt.title("Counts of ocurrances of each sex")
plt.xlabel("Sex", labelpad=15)
plt.ylabel("Count", labelpad=15)
bars.set_xticklabels(["Male", "Female", "Infant"], rotation=1)

for bar in bars.patches:
    yValue = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/ 2, yValue, f"{yValue}", ha="center", va="bottom")

plt.show()