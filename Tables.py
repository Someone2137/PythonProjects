import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

data = pd.read_csv(r"C:\Users\marty\PycharmProjects\data.csv", names=["Sex", "Length [mm]", "Diameter [mm]", "Height [mm]", "Whole weight [g]", "Shucked weight [g]", "Viscera weight [g]", "Shell weight [g]", "Rings"])

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

quantativeValues = ["Length [mm]", "Diameter [mm]", "Height [mm]", "Whole weight [g]", "Shucked weight [g]", "Viscera weight [g]", "Shell weight [g]", "Rings"]
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

print(summaryTable, "\n")


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

figure, axes = plt.subplots(4,2, figsize=(10,8))
axes = axes.flatten()

for index, column in enumerate(quantativeTable.columns):
    axes[index].hist(quantativeTable[column], bins=20, color="blue", edgecolor="black")
    axes[index].set_title(f"Histogram of {column}")
    axes[index].set_xlabel(column)
    axes[index].set_ylabel("Frequency")

plt.tight_layout()
plt.show()


correlation_matrix = quantativeTable.corr()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print("Correlation Matrix")
print(correlation_matrix)


plt.figure(figsize=(14,12))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt="2f", linewidths=0.5)
plt.title("Heatmap of Correlation Matrix")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


first_variable = "Diameter [mm]"
second_variable = "Length [mm]"
plt.figure(figsize=(10, 8))
sns.regplot(x=quantativeTable[first_variable], y=quantativeTable[second_variable], line_kws={"color": "red"})
plt.title(f"Linear Regression Plot: {first_variable} vs {second_variable}")
plt.xlabel(first_variable)
plt.ylabel(second_variable)
plt.show()