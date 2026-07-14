import pandas as pd


def get_shape(df: pd.DataFrame) -> tuple[int, int]:
    """Return (row_count, column_count)."""
    return df.shape


def get_column_types(df: pd.DataFrame) -> pd.Series:
    """Return column name -> dtype name (as string)."""
    return df.dtypes.astype(str)


def get_missing_counts(df: pd.DataFrame) -> pd.Series:
    """Return column name -> count of missing values."""
    return df.isna().sum()


def get_duplicate_count(df: pd.DataFrame) -> int:
    """Return the total number of duplicate rows."""
    return int(df.duplicated().sum())
