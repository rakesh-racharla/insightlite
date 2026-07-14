import pandas as pd

from src.profiling import (
    get_column_types,
    get_duplicate_count,
    get_missing_counts,
    get_shape,
)


def test_get_shape():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert get_shape(df) == (3, 2)


def test_get_column_types():
    df = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})
    types = get_column_types(df)
    assert types["a"] == "int64"
    assert types["b"] == "object"


def test_get_missing_counts_no_missing():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    counts = get_missing_counts(df)
    assert counts["a"] == 0
    assert counts["b"] == 0


def test_get_missing_counts_with_missing():
    df = pd.DataFrame({"a": [1, None, 3], "b": [None, None, 6]})
    counts = get_missing_counts(df)
    assert counts["a"] == 1
    assert counts["b"] == 2


def test_get_duplicate_count_no_duplicates():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert get_duplicate_count(df) == 0


def test_get_duplicate_count_with_duplicates():
    df = pd.DataFrame({"a": [1, 2, 1], "b": [4, 5, 4]})
    assert get_duplicate_count(df) == 1


def test_empty_dataframe():
    df = pd.DataFrame({"a": [], "b": []})
    assert get_shape(df) == (0, 2)
    assert get_duplicate_count(df) == 0
    counts = get_missing_counts(df)
    assert counts["a"] == 0
    assert counts["b"] == 0
