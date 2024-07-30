import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:\Users\marty\OneDrive\Pulpit\Programowanie\dogVsCat.xlsx")
Country = data["Country"]
Cat = data["cat"]

plt.figure(figsize=(10, 5))
plt.bar(Country, Cat, color="lightblue")
plt.xlabel("Country", labelpad=15)
plt.ylabel("Percentage", labelpad=15)
plt.title("Pet owners that said they have a cat in 2022")
plt.tight_layout()

plt.show()