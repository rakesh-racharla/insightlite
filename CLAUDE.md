# InsightLite Claude Instructions

## Project overview
InsightLite is a lightweight Streamlit app for data scientists.

The app helps users quickly inspect a CSV dataset, review simple data-quality issues, and generate basic visual insights.

This project is intentionally simple. The main goal is to demonstrate Claude Code workflows, not to build a complex production application.

## Tech stack
- Python
- Streamlit
- pandas
- matplotlib
- pytest

## Project structure
- `app.py`: Streamlit UI and app orchestration
- `requirements.txt`: Python dependencies
- `README.md`: setup and usage instructions
- `src/`: reusable data logic if the app grows
- `tests/`: simple pytest tests when reusable logic is added

## Coding conventions
- Keep code simple and readable.
- Prefer small functions over large blocks of logic.
- Do not add databases unless explicitly requested.
- Do not add authentication unless explicitly requested.
- Do not add complex frontend frameworks.
- Do not add heavy ML models unless explicitly requested.
- Keep `app.py` focused on UI and orchestration.
- Put reusable data logic in `src/`.

## Data science guidance
- Handle missing values safely.
- Do not mutate the original dataframe unexpectedly.
- Make assumptions explicit.
- Avoid data leakage in any modelling-related logic.
- Prefer explainable summaries over complex automation.
- Use simple visualisations that are easy to interpret.

## Testing guidance
- Add simple pytest tests for reusable functions.
- Prioritise tests for data profiling, cleaning, and validation logic.
- Keep tests lightweight and easy to understand.

## Prompting guidance for Claude
- Before making large changes, explain the plan.
- For feature work, prefer small incremental changes.
- Do not over-engineer.
- Ask for clarification only when necessary.