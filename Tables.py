import pandas as pd

data = pd.read_csv(r"C:\Users\marty\PycharmProjects\data.csv", header=None, names=["Sex", "Variable1", "Variable2", "Variable3", "Variable4", "Variable5", "Variable6", "Variable7", "Variable8"])

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

quantativeValues = ["Variable1", "Variable2", "Variable3", "Variable4", "Variable5", "Variable6", "Variable7", "Variable8"]
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