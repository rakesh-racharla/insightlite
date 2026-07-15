import pandas as pd

from src.charts import get_histogram_data, get_numeric_columns


def test_get_numeric_columns_mixed_types():
    df = pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"], "c": [1.5, 2.5, 3.5]})
    assert get_numeric_columns(df) == ["a", "c"]


def test_get_numeric_columns_no_numeric():
    df = pd.DataFrame({"a": ["x", "y"], "b": ["z", "w"]})
    assert get_numeric_columns(df) == []


def test_get_numeric_columns_all_numeric():
    df = pd.DataFrame({"a": [1, 2], "b": [3.0, 4.0]})
    assert get_numeric_columns(df) == ["a", "b"]


def test_get_histogram_data_no_missing():
    df = pd.DataFrame({"a": [1, 2, 3]})
    result = get_histogram_data(df, "a")
    assert list(result) == [1, 2, 3]


def test_get_histogram_data_drops_missing():
    df = pd.DataFrame({"a": [1, None, 3, None]})
    result = get_histogram_data(df, "a")
    assert list(result) == [1, 3]


def test_get_histogram_data_all_missing():
    df = pd.DataFrame({"a": [None, None, None]})
    result = get_histogram_data(df, "a")
    assert result.empty


def test_get_histogram_data_does_not_mutate_original():
    df = pd.DataFrame({"a": [1, None, 3]})
    get_histogram_data(df, "a")
    assert df["a"].isna().sum() == 1


def test_empty_dataframe():
    df = pd.DataFrame({"a": []})
    assert get_numeric_columns(df) == ["a"]
    result = get_histogram_data(df, "a")
    assert result.empty
