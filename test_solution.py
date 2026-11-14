
import pandas as pd
from solution import add_virtual_column


def test_sum_of_two_columns():
    df = pd.DataFrame([[2, 3], [4, 5]], columns=["first", "second"])
    df_expected = pd.DataFrame([[2, 3, 5], [4, 5, 9]], columns=["first", "second", "total"])
    df_result = add_virtual_column(df, "first + second", "total")
    assert df_result.equals(df_expected)


def test_multiplication_of_two_columns():
    df = pd.DataFrame([[2, 3], [4, 5]], columns=["first", "second"])
    df_expected = pd.DataFrame([[2, 3, 6], [4, 5, 20]], columns=["first", "second", "total"])
    df_result = add_virtual_column(df, "first * second", "total")
    assert df_result.equals(df_expected)


def test_subtraction_of_two_columns():
    df = pd.DataFrame([[5, 3], [8, 2]], columns=["first", "second"])
    df_expected = pd.DataFrame([[5, 3, 2], [8, 2, 6]], columns=["first", "second", "difference"])
    df_result = add_virtual_column(df, "first - second", "difference")
    assert df_result.equals(df_expected)


def test_combined_operations():
    df = pd.DataFrame([[2, 3, 1], [4, 5, 2]], columns=["quantity", "price", "discount"])
    df_expected = pd.DataFrame([[2, 3, 1, 5], [4, 5, 2, 18]], columns=["quantity", "price", "discount", "revenue"])
    df_result = add_virtual_column(df, "quantity * price - discount", "revenue")
    assert df_result.equals(df_expected)


def test_empty_result_when_invalid_column():
    df = pd.DataFrame([[1, 2]], columns=["first", "second"])
    df_result = add_virtual_column(df, "first + second", "total1")
    assert df_result.empty


def test_empty_result_when_invalid_role():
    df = pd.DataFrame([[1, 2]], columns=["first", "second"])
    df_result = add_virtual_column(df, "first / second", "total")
    assert df_result.empty

    df_result = add_virtual_column(df, "first + missing", "total")
    assert df_result.empty


def test_when_extra_spaces_in_role():
    df = pd.DataFrame([[1, 2]], columns=["first", "second"])
    df_expected = pd.DataFrame([[1, 2, 3]], columns=["first", "second", "total"])
    df_result = add_virtual_column(df, "  first + second  ", "total")
    assert df_result.equals(df_expected)
