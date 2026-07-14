# Spec 01: CSV Upload and Basic Dataset Profiling

## Problem Statement
Data scientists often need a fast, no-setup way to sanity-check a CSV file before diving into deeper analysis. Today there's no quick way in InsightLite to upload a dataset and immediately see its shape, structure, and basic data-quality signals.

## User Story
As a data scientist, I want to upload a CSV file and instantly see a preview of the data along with basic profiling information (row/column counts, column types, missing values, duplicates), so I can quickly assess the dataset's shape and quality before doing further analysis.

## Scope
- File upload widget in Streamlit for CSV files.
- Preview of the first 5 rows of the uploaded dataset.
- Display of total row count and column count.
- Display of column names and their inferred data types.
- Display of missing value count per column.
- Display of total duplicate row count.
- Reusable profiling logic implemented in `src/profiling.py`.
- `app.py` limited to UI rendering and orchestration (calling into `src/profiling.py`).

## Out of Scope
- Charts or visualizations of any kind.
- Database integration or persistence.
- Authentication or user accounts.
- ML model training.
- Advanced data cleaning or transformation (e.g., imputation, outlier removal).

## Acceptance Criteria
- User can upload a `.csv` file via a Streamlit file uploader.
- After upload, the app displays a table with the first 5 rows of the dataset.
- The app displays the total number of rows and total number of columns.
- The app displays a table listing each column name alongside its data type.
- The app displays the count of missing values for each column.
- The app displays the total number of duplicate rows in the dataset.
- All profiling calculations are performed by functions in `src/profiling.py`, not inline in `app.py`.
- The original uploaded dataframe is not mutated by profiling functions.
- If no file is uploaded, the app shows a simple prompt/message instead of erroring.

## Implementation Notes
- Use `pandas.read_csv` to load the uploaded file into a dataframe.
- Add functions to `src/profiling.py`, e.g.:
  - `get_shape(df)` → returns (row_count, column_count)
  - `get_column_types(df)` → returns column name/dtype pairs
  - `get_missing_counts(df)` → returns missing value count per column
  - `get_duplicate_count(df)` → returns count of duplicate rows
- Each function should accept a dataframe and return plain Python/pandas data structures (no Streamlit calls inside `src/profiling.py`), keeping profiling logic decoupled from the UI.
- `app.py` should call these functions and render results using `st.dataframe`, `st.write`, or similar simple Streamlit components.
- Handle empty CSVs or CSVs with zero rows gracefully (no crashes).
- Keep functions small and focused, per project conventions.

## Testing Notes
- Add pytest tests in `tests/` for each function in `src/profiling.py`.
- Test cases should cover:
  - A simple dataframe with no missing values or duplicates.
  - A dataframe with missing values in one or more columns.
  - A dataframe with duplicate rows.
  - An empty dataframe (zero rows).
- Tests should assert on return values directly (no Streamlit involved).
- Keep tests lightweight and readable, following existing conventions in the project.
