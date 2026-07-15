import pandas as pd


def get_numeric_columns(df: pd.DataFrame) -> list[str]:
    """Return the names of columns with numeric dtypes."""
    return df.select_dtypes(include="number").columns.tolist()


def get_histogram_data(df: pd.DataFrame, column: str) -> pd.Series:
    """Return the non-missing values of a numeric column, ready for histogram plotting."""
    return df[column].dropna()
