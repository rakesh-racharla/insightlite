---
description: Create a spec file and feature branch for the next InsightLite feature
argument-hint: "Feature name e.g. csv profiling"
allowed-tools: Read, Write, Glob, Bash(git:*)
---

You are a senior data science engineer spinning up a new feature for
InsightLite, a lightweight Streamlit data profiling app. Always follow
the rules in CLAUDE.md.

User input: $ARGUMENTS

## Step 1 — Check working directory is clean

Run `git status` and check for uncommitted, unstaged, or untracked files.

If any exist, stop immediately and tell the user to commit or stash changes
before proceeding.

DO NOT CONTINUE until the working directory is clean.

## Step 2 — Parse the arguments

From $ARGUMENTS extract:

1. `feature_title` — human readable title in Title Case
   - Example: "CSV Profiling"
   - Example: "Basic Charts"
   - Example: "Export Cleaned Data"

2. `feature_slug` — git and file safe slug
   - Lowercase
   - Kebab-case
   - Only a-z, 0-9 and -
   - Maximum 40 characters
   - Example: csv-profiling
   - Example: basic-charts
   - Example: export-cleaned-data

3. `branch_name` — format: `feature/<feature_slug>`
   - Example: `feature/csv-profiling`

If you cannot infer these from $ARGUMENTS, ask the user to clarify before proceeding.

## Step 3 — Check branch name is not taken

Run `git branch` to list existing branches.

If `branch_name` is already taken, append a number:

- `feature/csv-profiling-01`
- `feature/csv-profiling-02`

## Step 4 — Switch to main and pull latest

Run:

```bash
git checkout main
git pull origin main
```

If the project does not have a remote GitHub repository configured, skip the pull and explain that no remote is configured.

## Step 5 — Create and switch to the feature branch

Run:

```bash
git checkout -b <branch_name>
```

## Step 6 — Research the codebase

Read these files before writing the spec:

- `CLAUDE.md` — project rules, conventions, and constraints
- `app.py` — current Streamlit app structure
- `requirements.txt` — current dependencies
- `README.md` — current project usage instructions
- All files in `src/` if the folder exists
- All files in `.claude/specs/` if the folder exists

Check existing specs to avoid duplicating previous feature work.

If the requested feature already appears to be complete, warn the user and stop.

## Step 7 — Write the spec

Generate a spec document with this exact structure:

---

# Spec: <feature_title>

## Overview

One paragraph describing what this feature does and why it exists at this stage of the InsightLite project.

## Depends on

Which previous features this requires to be complete.

If there are no dependencies, state "No feature dependencies".

## User experience

Describe what the user should see or do in the Streamlit app.

Keep this practical and simple.

## Data science behaviour

Describe what data logic, profiling, validation, cleaning, or visualisation behaviour is needed.

If not applicable, state "No specific data science behaviour".

## Files to change

Every existing file that will likely be modified.

## Files to create

Every new file that will likely be created.

## New dependencies

Any new pip packages.

If none, state "No new dependencies".

## Out of scope

List what should not be built as part of this feature.

Always avoid unnecessary complexity.

## Rules for implementation

Specific constraints Claude must follow.

Always include:

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

A specific testable checklist.

Each item must be something that can be verified by running the app, running tests, or inspecting the code.

Use checkboxes.

---

## Step 8 — Save the spec

Save to:

`.claude/specs/<feature_slug>.md`

Create `.claude/specs/` if it does not already exist.

## Step 9 — Report to the user

Print a short summary in this exact format:

```text
Branch:    <branch_name>
Spec file: .claude/specs/<feature_slug>.md
Title:     <feature_title>
```

Then tell the user:

"Review the spec at `.claude/specs/<feature_slug>.md`
then enter Plan Mode with Shift+Tab twice to begin implementation."

Do not print the full spec in chat unless explicitly asked.
