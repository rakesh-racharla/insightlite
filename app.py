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

st.set_page_config(page_title="InsightLite", page_icon="📊", layout="centered")

st.title("📊 InsightLite")
st.write("A lightweight data profiling assistant for data scientists.")

st.divider()

st.subheader("Upload your dataset")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except pd.errors.EmptyDataError:
        st.error("This file appears to be empty or not a valid CSV.")
    else:
        st.subheader("Preview")
        st.dataframe(df.head())

        rows, columns = get_shape(df)
        st.write(f"**Rows:** {rows} &nbsp;&nbsp; **Columns:** {columns}")

        st.subheader("Column types")
        st.dataframe(
            get_column_types(df).rename("dtype").rename_axis("column").reset_index()
        )

        st.subheader("Missing values")
        st.dataframe(
            get_missing_counts(df)
            .rename("missing_count")
            .rename_axis("column")
            .reset_index()
        )

        st.subheader("Duplicate rows")
        st.write(get_duplicate_count(df))

        st.subheader("Chart")
        numeric_columns = get_numeric_columns(df)

        if not numeric_columns:
            st.info("No numeric columns available to chart.")
        else:
            selected_column = st.selectbox("Choose a numeric column", numeric_columns)
            values = get_histogram_data(df, selected_column)

            if values.empty:
                st.info(f"No non-missing numeric values in '{selected_column}' to chart.")
            else:
                fig, ax = plt.subplots()
                ax.hist(values)
                ax.set_xlabel(selected_column)
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
                plt.close(fig)
else:
    st.info("👆 Upload a CSV file to see a preview and profiling summary.")

    st.subheader("What is InsightLite?")
    st.write(
        "InsightLite helps you quickly understand a new dataset before diving into "
        "analysis. Load your data, review its quality, and explore key insights — "
        "all in one place."
    )

    st.subheader("How it works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 1. Load data")
        st.write("Bring in a dataset to get started.")

    with col2:
        st.markdown("### 2. Review quality")
        st.write("Check for missing values, types, and anomalies.")

    with col3:
        st.markdown("### 3. Explore insights")
        st.write("Summarize trends and patterns at a glance.")
