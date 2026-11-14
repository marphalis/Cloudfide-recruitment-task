
import pandas as pd
from pipeline import clean_data, add_revenue


def test_cleaning_decimal_commas():
    df = pd.DataFrame({
        "Unit_Price": ["10,50", "5,00"]
    })
    df_result = clean_data(df)

    assert df_result["unit_price"].tolist() == [10.50, 5.00]


def test_missing_discount():
    df = pd.DataFrame({
        "Quantity": [2],
        "Unit_Price": [10],
        "Discount": [None]
    })
    df_result = clean_data(df)

    assert df_result["discount"].iloc[0] == 0


def test_revenue_calculation():
    df = pd.DataFrame({
        "quantity": [2, 3],
        "unit_price": [10, 5],
        "discount": [2, 0]
    })
    df_result = add_revenue(df)

    assert df_result["revenue"].tolist() == [20, 15]


def test_revenue_by_region():
    df = pd.DataFrame({
        "Region": ["North", "South", "North"],
        "revenue": [100, 50, 25]
    })
    df_result = df.groupby("Region")["revenue"].sum()

    assert df_result.to_dict() == {"North": 125, "South": 50}
