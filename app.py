import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from src.charts import get_histogram_data, get_numeric_columns
from src.profiling import (
    get_column_types,
    get_duplicate_count,
    get_missing_counts,
    get_shape,
)


def render_quality_banner(count: int, issue_text: str, clean_text: str) -> None:
    if count > 0:
        st.warning(f"⚠️ Found {issue_text}.")
    else:
        st.success(f"✅ {clean_text}")


st.set_page_config(page_title="InsightLite", page_icon="📊", layout="centered")

with st.sidebar:
    st.header("About InsightLite")
    st.markdown(
        "InsightLite helps you quickly understand a new dataset before diving into "
        "analysis — load your data, review its quality, and explore key insights."
    )
    st.markdown(
        "**How it works**\n"
        "1. Load data\n"
        "2. Review quality\n"
        "3. Explore insights"
    )

st.title("📊 InsightLite")
st.caption("A lightweight data profiling assistant for data scientists.")

st.divider()

st.subheader("Upload your dataset")
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type="csv",
    help="Upload a CSV (comma-separated values) file to preview and profile it.",
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except pd.errors.EmptyDataError:
        st.error("This file appears to be empty or not a valid CSV.")
    else:
        st.subheader("Preview")
        st.caption("Showing the first 5 rows of your uploaded file.")
        st.dataframe(df.head())

        st.subheader("Data quality snapshot")
        rows, columns = get_shape(df)
        missing_counts = get_missing_counts(df)
        missing_total = int(missing_counts.sum())
        duplicate_count = get_duplicate_count(df)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Rows", f"{rows:,}")
        col2.metric("Columns", f"{columns:,}")
        col3.metric(
            "Missing values",
            f"{missing_total:,}",
            help="Total number of empty/null cells across all columns.",
        )
        col4.metric(
            "Duplicate rows",
            f"{duplicate_count:,}",
            help="Rows that are exact copies of another row.",
        )

        render_quality_banner(
            missing_total,
            issue_text=(
                f"{missing_total:,} missing value(s) across "
                f"{int((missing_counts > 0).sum())} column(s)"
            ),
            clean_text="No missing values found.",
        )
        render_quality_banner(
            duplicate_count,
            issue_text=f"{duplicate_count:,} duplicate row(s)",
            clean_text="No duplicate rows found.",
        )

        with st.expander("See full column details (dtypes & missing counts)"):
            column_details = (
                get_column_types(df)
                .rename("dtype")
                .to_frame()
                .join(missing_counts.rename("missing_count"))
                .rename_axis("column")
                .reset_index()
            )
            st.dataframe(column_details, hide_index=True)

        st.divider()

        st.subheader("Distribution chart")
        numeric_columns = get_numeric_columns(df)

        if not numeric_columns:
            st.info("No numeric columns available to chart.")
        else:
            selected_column = st.selectbox(
                "Choose a numeric column",
                numeric_columns,
                help="Pick a numeric column to see how its values are distributed.",
            )
            values = get_histogram_data(df, selected_column)

            if values.empty:
                st.info(f"No non-missing numeric values in '{selected_column}' to chart.")
            else:
                fig, ax = plt.subplots()
                ax.hist(values)
                ax.set_title(f"Distribution of {selected_column}")
                ax.set_xlabel(selected_column)
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
                plt.close(fig)
                st.caption(
                    "This histogram shows how values in the selected column are "
                    "spread out. Taller bars mean more rows fall in that range."
                )
else:
    st.info(
        "👆 Upload a CSV file to get started. Once uploaded, you'll see a preview, "
        "data-quality checks, and a chart of a numeric column."
    )
