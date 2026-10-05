import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_deliveries_by_site.csv")
plt.figure()
plt.bar(df['site'], df['total_deliveries'])
plt.title("Deliveries per Construction Site - Day 2")
plt.xlabel("Site")
plt.ylabel("Number of Deliveries")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("data/deliveries_per_site.png")
print("Saved: deliveries_per_site.png")

df2 = pd.read_csv("data/processed_materials_by_site.csv")
plt.figure()
plt.bar(df2['site'], df2['total_quantity'], color='orange')
plt.title("Total Quantity per Site")
plt.xlabel("Site")
plt.ylabel("Total Quantity")
plt.savefig("data/quantity_per_site.png")
print("Saved: quantity_per_site.png")
