# Spec: Basic Charts

## Overview

This feature adds simple, explainable visualisations to InsightLite so that after a user uploads a CSV and reviews the existing profiling summary (shape, column types, missing values, duplicates), they can also see basic charts that surface distribution and structure at a glance. It builds directly on the CSV upload and profiling foundation already in place, extending the app from tabular profiling into lightweight visual insight — the next natural step in InsightLite's "load, review quality, explore insights" flow.

## Depends on

Depends on the CSV Upload and Basic Dataset Profiling feature (`.claude/specs/01-csv-profiling.md`), which provides the uploaded dataframe, column type detection, and the existing profiling section in `app.py` that this feature extends.

## User experience

After a user uploads a CSV and the existing profiling sections (preview, shape, column types, missing values, duplicates) are shown, a new "Charts" section appears below them.

- For numeric columns, the user can select a column (via a dropdown) and see a histogram of its values.
- For categorical/object columns, the user can select a column and see a bar chart of the top category value counts (e.g. top 10 categories).
- If a dataset has no numeric columns, the numeric chart option is hidden or shows a simple message instead of erroring.
- If a dataset has no categorical columns, the categorical chart option is hidden or shows a simple message instead of erroring.
- Charts render inline in the Streamlit app beneath the profiling sections, using simple, readable matplotlib charts (no custom styling complexity).

## Data science behaviour

- Missing values are excluded (dropped) before computing histograms or value counts — they must never crash a chart or silently appear as a phantom category.
- The original uploaded dataframe is never mutated; any filtering (e.g. dropping NaNs for a chart) happens on a copy or via non-mutating pandas operations.
- Numeric columns are identified using pandas dtype inspection (reusing/extending the existing column-type logic where sensible).
- Categorical/object columns are identified the same way.
- For bar charts of categorical data, only the top N (e.g. 10) most frequent categories are shown, with counts computed via `value_counts()`, to keep charts readable on high-cardinality columns.
- Chart-data preparation functions return plain pandas/numpy structures (e.g. a `Series` of counts) — no Streamlit or matplotlib calls inside `src/`, keeping data logic decoupled from rendering.

## Files to change

- `app.py` — add a "Charts" section that lets the user pick a numeric or categorical column and renders the corresponding chart.
- `requirements.txt` — add `matplotlib`.

## Files to create

- `src/charts.py` — reusable, non-UI functions for preparing chart data (e.g. `get_numeric_columns(df)`, `get_categorical_columns(df)`, `get_histogram_data(df, column)`, `get_top_category_counts(df, column, top_n=10)`).
- `tests/test_charts.py` — pytest tests for the functions in `src/charts.py`.

## New dependencies

- `matplotlib` — required for rendering histograms and bar charts.

## Out of scope

- Interactive/JS-based charting libraries (e.g. Plotly, Altair, Bokeh) — matplotlib only.
- Correlation matrices, scatter plots, or multi-column/multivariate charts.
- Chart export/download functionality.
- Custom chart styling, theming, or branding.
- Automatic "insight" generation or commentary about what a chart shows.
- Any changes to the existing profiling logic in `src/profiling.py`.
- Database integration, authentication, or persistence of chart selections.

## Rules for implementation

- Keep the implementation simple and readable.
- Keep `app.py` focused on Streamlit UI and orchestration.
- Put reusable data logic in `src/`.
- Do not add databases unless explicitly requested.
- Do not add authentication unless explicitly requested.
- Do not add complex frontend frameworks.
- Do not add heavy ML models unless explicitly requested.
- Use pandas for basic data manipulation.
- Use matplotlib for simple charts if charts are required.
- Handle missing values safely.
- Do not mutate the original dataframe unexpectedly.
- Make assumptions explicit.
- Follow `CLAUDE.md`.

## Definition of done

- [ ] `src/charts.py` exists with functions to identify numeric columns, identify categorical columns, prepare histogram data, and prepare top-N category counts.
- [ ] `app.py` renders a "Charts" section below the existing profiling output when a CSV is uploaded.
- [ ] User can select a numeric column and see a histogram rendered via matplotlib in the app.
- [ ] User can select a categorical column and see a bar chart of the top 10 category counts rendered via matplotlib in the app.
- [ ] Uploading a CSV with no numeric columns does not crash the app and shows a clear message instead.
- [ ] Uploading a CSV with no categorical columns does not crash the app and shows a clear message instead.
- [ ] Missing values are excluded from chart calculations without mutating the original dataframe.
- [ ] `matplotlib` is added to `requirements.txt`.
- [ ] `tests/test_charts.py` includes passing pytest tests covering: numeric column detection, categorical column detection, histogram data preparation, top-N category counts, and handling of missing values.
- [ ] `pytest` passes for the full test suite.
- [ ] `streamlit run app.py` runs without errors and charts render correctly for a sample CSV with both numeric and categorical columns.
