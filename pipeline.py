import pandas as pd

from solution import add_virtual_column
def clean_data (data: pd.DataFrame)  -> pd.DataFrame:
    data.columns = data.columns.str.strip()
    data.columns = data.columns.str.replace(" ", "_", regex=False)
    data.columns = data.columns.str.lower()

    if "order_id" in data.columns:
        data = data[data["order_id"].astype("string").str.startswith("SO-", na=False)]

    if "unit_price" in data.columns:
        data["unit_price"] = data["unit_price"].astype("string").str.replace(",", ".", regex=False)

    for col in data.columns:
        converted = pd.to_numeric(data[col].astype("string").str.replace(" ", "", regex=False), errors="coerce")

        if converted.notna().sum() == data[col].notna().sum():
            data[col] = converted.fillna(0)

    if "order_date" in data.columns:
        data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce")

    return data.map(lambda x: x.strip().lower().replace(" ", "_") if isinstance(x, str) else x)


def add_revenue (data: pd.DataFrame)  -> pd.DataFrame:
    return add_virtual_column(data, "quantity * unit_price" , "revenue")


def main():
    data = pd.read_csv("sales.csv").drop_duplicates()

    data = clean_data(data)
    data = add_revenue(data)

    by_region = data.groupby("region").agg({"revenue": "sum"})

    by_region.to_csv("revenue_by_region.csv", index=True, header=True)


if __name__ == "__main__":
    main()