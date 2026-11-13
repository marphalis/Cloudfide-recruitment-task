import pandas as pd
from solution import add_virtual_column

data = pd.read_csv("sales.csv").drop_duplicates()

data.columns = data.columns.str.strip()
data.columns = data.columns.str.replace(" ", "_", regex=False)
data.columns = data.columns.str.lower()

data = data[data["order_id"].str.startswith("SO-", na=False)]
data = data[data["quantity"] != "Quantity"]

data["unit_price"] = data["unit_price"].str.replace(",", ".", regex=False)

for col in data.columns:
    converted = pd.to_numeric(data[col].str.replace(" ", "", regex=False), errors="coerce")

    if converted.notna().sum() == data[col].notna().sum():
        data[col] = converted.fillna(0)

data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce")

data = data.map(lambda x: x.strip().lower() if isinstance(x, str) else x)

data = add_virtual_column(data, "quantity * unit_price" , "revenue")

by_region = data.groupby("region").agg({"revenue": "sum"})

by_region.to_csv("revenue_by_region.csv", index=True, header=True)