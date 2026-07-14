import streamlit as st

st.set_page_config(page_title="InsightLite", page_icon="📊", layout="centered")

st.title("📊 InsightLite")
st.write("A lightweight data profiling assistant for data scientists.")

st.divider()

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
