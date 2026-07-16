# Spec: Polish App Design

## Overview

This feature applies a UI/UX polish pass to InsightLite's existing Streamlit app now that CSV upload, profiling, and basic charting are all in place. It does not add new data functionality — it improves how the existing upload flow, profiling results, and charts are presented so the app feels calm, clear, and customer-ready for a non-technical user, following the guidance already captured in the `streamlit-design-polisher` skill.

## Depends on

Depends on both prior features being complete:
- CSV Upload and Basic Dataset Profiling (`.claude/specs/01-csv-profiling.md`)
- Basic Charts (`.claude/specs/basic-charts.md`)

## User experience

- Before uploading a file, the user sees a clear, friendly empty state (via `st.info()`) explaining what to do and what they'll get, instead of just a bare uploader.
- The file uploader has a clear label and `help=` text describing accepted format.
- Key summary numbers (rows, columns, missing values, duplicate rows) are shown as `st.metric()` cards in `st.columns()` instead of plain text/tables.
- Missing values and duplicate rows are called out with `st.warning()` (if present) or `st.success()` (if clean), in plain language with specific counts.
- Each chart has a clear title and a short `st.caption()` explaining what to look for.
- Detailed/raw information (e.g. full column dtype table) is tucked into an `st.expander()` rather than always shown.
- A lightweight sidebar gives orientation (what the app does, how to use it) without adding clutter.
- Section order and headings follow the natural flow: title/intro → upload → preview → data quality → charts.
- All existing functionality (upload, preview, profiling stats, missing values, duplicates, numeric chart) continues to work identically — this is a presentation-only change.

## Data science behaviour

No specific data science behaviour. Profiling and charting logic in `src/profiling.py` and `src/charts.py` are not modified — only how their results are displayed in `app.py` changes.

## Files to change

- `app.py` — restructure presentation using `st.metric`, `st.columns`, `st.warning`/`st.success`, `st.expander`, `st.caption`, sidebar content, and improved empty state, per the `streamlit-design-polisher` skill checklist.

## Files to create

No new files expected.

## New dependencies

No new dependencies.

## Out of scope

- Any changes to profiling or charting calculation logic in `src/`.
- Authentication, databases, or persistence.
- Custom CSS/HTML components or JS-based frontends.
- New chart types or new profiling metrics.
- Multi-page app structure or routing.
- Categorical/bar charts (not yet implemented in the current app — out of scope here).

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
- Follow the `streamlit-design-polisher` skill's checklist and implementation rules (standard Streamlit components only, no new dependencies, preserve existing functionality).

## Definition of done

- [ ] Empty state before upload uses `st.info()` with clear guidance on what to do and what the user will get.
- [ ] `st.file_uploader()` has a descriptive label and `help=` text.
- [ ] Row count, column count, missing value count, and duplicate row count are shown via `st.metric()` in `st.columns()`.
- [ ] Missing values and duplicates are surfaced via `st.warning()`/`st.success()` with plain-language, specific-count messaging.
- [ ] The chart section has a clear title and a `st.caption()` explaining what the chart shows.
- [ ] Full column dtype details are shown inside an `st.expander()` rather than always visible.
- [ ] A sidebar with brief app orientation is present.
- [ ] `streamlit run app.py` runs without errors and all existing functionality (upload, preview, profiling, charts) still works for a sample CSV.
- [ ] `pytest` passes for the full existing test suite (no test behaviour should change since data logic is untouched).
- [ ] No new pip dependencies were added to `requirements.txt`.
