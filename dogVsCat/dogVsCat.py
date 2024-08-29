import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:\Users\marty\OneDrive\Pulpit\Programowanie\PythonProjects\dogVsCat.xlsx")
Country = data["Country"]
Cat = data["cat"]

plt.figure(figsize=(10, 7))
bars = plt.bar(Country, Cat, color="lightblue")

for bar in bars:
    yValue = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yValue, f'{yValue}%', ha='center', va='bottom')

plt.xlabel("Country", labelpad=15)
plt.ylabel("Percentage", labelpad=15)
plt.title("Pet owners that said they have a cat in 2022")
plt.tight_layout()

plt.show()