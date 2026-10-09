import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("data/raw/materials.csv")

# clean column names
df.columns = df.columns.str.strip()

out_dir = Path("data/processed")
out_dir.mkdir(parents=True, exist_ok=True)

# 1. Deliveries per site
if "Site" in df.columns:
    site_counts = df["Site"].value_counts()
    plt.figure()
    site_counts.plot(kind="bar")
    plt.title("Deliveries per Site")
    plt.xlabel("Site")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_dir / "deliveries_per_site.png")
    plt.close()
    print("Saved: deliveries_per_site.png")

# 2. Quantity per site
qty_col = None
for c in df.columns:
    if "qty" in c.lower() or "quantity" in c.lower():
        qty_col = c
        break

if qty_col and "Site" in df.columns:
    qty_per_site = df.groupby("Site")[qty_col].sum()
    plt.figure()
    qty_per_site.plot(kind="bar")
    plt.title("Quantity per Site")
    plt.xlabel("Site")
    plt.ylabel(qty_col)
    plt.tight_layout()
    plt.savefig(out_dir / "quantity_per_site.png")
    plt.close()
    print("Saved: quantity_per_site.png")
else:
    print(f"Could not find Quantity column. Columns are: {list(df.columns)}")