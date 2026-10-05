import pandas as pd

# 1. Load - file is inside data/ folder
df = pd.read_csv("data/materials.csv")
print("Raw Data:")
print(df)

# 2. Transform: total quantity by site, material and unit
summary = df.groupby(["site", "material", "unit"], as_index=False)["quantity"].sum()
summary.rename(columns={"quantity": "total_quantity"}, inplace=True)

print("\nSummary by Site:")
print(summary)

# 3. Count deliveries per site
site_total = df.groupby("site", as_index=False)["delivery_id"].count()
site_total.rename(columns={"delivery_id": "total_deliveries"}, inplace=True)

print("\nDeliveries per Site:")
print(site_total)

# 4. Save processed files inside data/ folder
summary.to_csv("data/processed_materials_by_site.csv", index=False)
site_total.to_csv("data/processed_deliveries_by_site.csv", index=False)

print("\nDone! 2 processed files saved in data/ folder.")