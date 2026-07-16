---
name: streamlit-design-polisher
description: Improve the UI/UX polish of lightweight Streamlit data apps (like InsightLite-style CSV upload, profiling, and charting tools) without over-engineering them. Use this skill whenever a user asks to make a Streamlit app "look better," "more professional," "more customer-facing," "less clunky," or asks for help with page layout, headings, empty states, metric cards, data-quality warnings, chart titles, sidebar guidance, or overall visual hierarchy in a Streamlit app. Also use it when reviewing or refactoring an existing app.py for a small internal or customer-facing Streamlit tool. Do NOT use this skill for building new data pipelines, adding authentication, adding databases, building custom React/JS frontends, or any request that goes beyond standard Streamlit components — flag those as out of scope instead.
---

# Streamlit Design Polisher

## Purpose

This skill helps Claude take a working but visually rough Streamlit data app and make it feel
polished, intentional, and easy for non-technical business users to navigate — using only
standard Streamlit components. It is a *polish* skill, not a *rebuild* skill: the app's
functionality, data logic, and structure should stay the same unless the user explicitly asks
for new features.

The target app shape is something like **InsightLite**: upload a CSV → preview data → view
profiling stats → check missing values/duplicates → view a few matplotlib charts. This skill
generalizes to any similarly small, single-page or few-page Streamlit data tool.

## When to use this skill

- The user asks to improve the look, feel, layout, or "professionalism" of a Streamlit app.
- The user asks for better headings, section descriptions, or help text.
- The user asks how to make an empty state, upload prompt, or onboarding flow nicer.
- The user asks for metric cards, data-quality warnings, or better chart presentation.
- The user asks for sidebar content, navigation, or general "make this customer-ready" polish.
- The user shares an `app.py` (or similar) and asks for a UI/UX review or light refactor.

## When NOT to use this skill

Politely note these are out of scope for this skill and confirm before doing them:

- Adding authentication/login, user accounts, or role-based access.
- Adding a database, persistent storage, or caching layers beyond `st.cache_data`.
- Building a custom frontend (React, custom JS components, complex injected CSS/HTML).
- Adding heavy ML features (auto-modeling, AI-generated insights, anomaly detection) that
  weren't already in the app.
- Multi-page app architecture, complex routing, or new business logic — unless the user
  explicitly asks for it.
- Large rewrites of working data logic. If the data logic looks buggy, mention it separately
  rather than silently rewriting it while doing UI polish.

If a request needs one of the above, do the UI polish that's in scope and call out the rest as
a separate, explicit ask.

## Core philosophy

A small customer-facing Streamlit app should feel **calm and obvious**, not impressive. Every
change should answer: "does this help a non-technical user understand what's happening and
what to do next?" If a change doesn't clearly do that, don't make it.

Favor:
- Standard Streamlit components over custom HTML/CSS.
- Plain language over jargon.
- Fewer, better-labeled things over more things.
- Consistency (same heading style, same caption style, same warning style throughout).

Avoid:
- Anything that makes `app.py` meaningfully longer or harder to follow.
- Cleverness that isn't needed. A working `st.metric` beats a fancy custom HTML card.

## UI improvement checklist

Work through this checklist when polishing an app. Not every item applies to every app — use
judgment about what the app actually needs.

1. **Page config** — Is `st.set_page_config()` set with a sensible `page_title`, `page_icon`,
   and `layout` (usually `"centered"` for simple tools, `"wide"` only if there are several
   charts/tables side by side)?
2. **Page title & intro** — Is there a clear `st.title()` or `st.header()` plus one to two
   sentences (`st.caption()` or `st.markdown()`) explaining what the app does, in plain language?
3. **Section structure** — Are major steps (upload → preview → quality checks → charts) broken
   into clearly labeled sections with `st.header()`/`st.subheader()`, ideally in the logical
   order a user would think through the task?
4. **Upload experience** — Does `st.file_uploader()` have a clear label and helpful `help=`
   text (accepted format, e.g. "CSV files only")? Is there a short instruction above it?
5. **Empty state** — Before a file is uploaded, does the user see something better than a blank
   page or raw error? E.g. an `st.info()` box explaining what to do, and ideally what they'll
   get once they upload.
6. **Metric cards** — Are key numbers (row count, column count, missing % , duplicate count)
   shown with `st.metric()` in `st.columns()` rather than buried in a text dump or raw table?
7. **Data-quality warnings** — Are missing values / duplicates / obvious issues called out
   with `st.warning()` or `st.success()` (when clean), using plain language and, where useful,
   a specific count?
8. **Chart presentation** — Does every chart have a clear title (via matplotlib `ax.set_title()`
   or an `st.subheader()` above it) and, where helpful, a one-line `st.caption()` explaining
   what to look for?
9. **Sidebar** — If the app has more than one step or setting, does the sidebar offer light
   orientation (what the app does, how to use it, links) rather than clutter? Don't add a
   sidebar just to have one.
10. **Help text for non-technical users** — Do technical terms (e.g. "null," "dtype," "duplicate
    rows") get a one-line plain-language explanation via `help=` params or captions?
11. **Visual hierarchy** — Is there a clear reading order (title → intro → upload → results)?
    Are `st.divider()` or spacing used sparingly to separate sections without creating clutter?
12. **Progressive disclosure** — Are advanced/rarely-needed details (e.g. raw dtypes, full
    profiling dump) tucked into `st.expander()` rather than always shown?
13. **No dead space or clutter** — Are there redundant headers, repeated explanations, or
    components that don't add information? Remove them.

## Implementation rules

- **Use only Streamlit's built-in components and standard layout primitives**: `st.title`,
  `st.header`, `st.subheader`, `st.caption`, `st.markdown`, `st.columns`, `st.metric`,
  `st.info`/`st.warning`/`st.success`/`st.error`, `st.expander`, `st.sidebar`, `st.divider`,
  `st.file_uploader`, `st.dataframe`/`st.table`. Do not reach for custom components,
  `st.components.v1.html`, or injected `<style>` blocks unless the user explicitly asks for
  custom styling.
- **Minimal CSS only if asked.** If the user explicitly wants custom colors/branding, keep any
  `st.markdown("<style>...</style>", unsafe_allow_html=True)` block short, isolated at the top
  of the file, and clearly commented. Never make this the default approach.
- **No new dependencies.** Don't add packages beyond what the app already uses (typically
  `streamlit`, `pandas`, `matplotlib`) unless the user asks for something that requires it.
- **Don't touch data logic.** Keep parsing, profiling, and chart-generation logic as-is. Only
  change *how results are presented*, not *how they're computed*, unless asked.
- **Keep app.py manageable.** If polish additions would make a single-file app sprawling,
  prefer tightening prose and consolidating repeated patterns (e.g. a small helper function for
  a warning banner used three times) over leaving duplicated blocks. Don't split into multiple
  files/modules unless the user asks — that's a structural change, not polish.
- **Preserve existing functionality.** Every current feature (upload, preview, profiling,
  missing-value/duplicate checks, charts) must still work identically after polish. Polish is
  additive/cosmetic, not a functional rewrite.
- **Don't invent new features.** Stick to what's in the app or in the user's request. No
  auto-generated AI insights, no login, no export-to-PDF, no themes system — unless asked.
- **Respect layout choice.** Default to `layout="centered"` for a simple single-flow app; only
  switch to `"wide"` if there's a real need (e.g. several charts/tables side-by-side) and say
  why.
- **Be consistent.** Pick one tone and pattern for captions, warnings, and section headers, and
  use it throughout, rather than varying style section to section.

## Output format

When polishing an app, structure the response like this:

1. **Short summary** (2-4 sentences) of what you changed and why, framed around user
   experience (e.g. "Added an empty state before upload, grouped stats into metric cards, and
   gave charts titles/captions so results are easier to scan").
2. **The updated code** — either a full updated `app.py` (for a small file) or a diff/patch-style
   set of edits if the file is large and only parts changed. Prefer showing the complete file
   when it's under roughly 150-200 lines, since that's the norm for this class of app.
3. **A short "what to check" list** — 2-4 bullets telling the user what to look at when they run
   it (e.g. "Confirm the empty-state message matches your brand voice," "Check that the metric
   cards render correctly with your column names").

Don't pad the response with a long lecture about design principles — the checklist above is for
Claude's own reasoning, not something to restate at length to the user unless they ask why a
change was made.

## Examples of good Streamlit improvements

**Empty state before upload:**
```python
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"],
    help="We accept standard CSV files up to 200MB.",
)

if uploaded_file is None:
    st.info(
        "👆 Upload a CSV to get started. Once uploaded, you'll see a preview, "
        "quick data-quality checks, and a few summary charts."
    )
    st.stop()
```

**Metric cards instead of a raw text dump:**
```python
st.subheader("At a glance")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Rows", f"{len(df):,}")
col2.metric("Columns", len(df.columns))
col3.metric("Missing values", f"{df.isna().sum().sum():,}")
col4.metric("Duplicate rows", f"{df.duplicated().sum():,}")
```

**Clear, plain-language data-quality warning:**
```python
missing_total = df.isna().sum().sum()
if missing_total > 0:
    st.warning(
        f"⚠️ Found {missing_total:,} missing values across "
        f"{df.isna().any().sum()} column(s). Consider reviewing these before analysis."
    )
else:
    st.success("✅ No missing values found.")
```

**Chart with title and caption:**
```python
st.subheader("Distribution of values")
fig, ax = plt.subplots()
df[selected_col].hist(ax=ax, bins=20)
ax.set_title(f"Histogram of {selected_col}")
ax.set_xlabel(selected_col)
ax.set_ylabel("Count")
st.pyplot(fig)
st.caption("Shows how values in this column are spread out. Tall bars mean common values.")
```

**Lightweight sidebar guidance:**
```python
with st.sidebar:
    st.header("About InsightLite")
    st.markdown(
        "Upload a CSV to quickly preview your data, spot quality issues, "
        "and see a few simple charts — no setup required."
    )
    st.caption("Tip: works best with CSVs under 50,000 rows.")
```

**Tucking detail away with an expander:**
```python
with st.expander("See full column details"):
    st.dataframe(df.dtypes.astype(str).rename("dtype"))
```

## Examples of over-engineered changes to avoid

- ❌ Injecting a large custom `<style>` block to recreate a "card" component with shadows and
  gradients, instead of using `st.metric()` / `st.container(border=True)`.
- ❌ Adding a login screen ("so it feels more like a real product") when the user only asked
  for visual polish.
- ❌ Introducing a SQLite/Postgres layer to "save past uploads" when the app is meant to be
  stateless.
- ❌ Splitting a 120-line `app.py` into six modules and a `components/` package for a simple
  single-page tool.
- ❌ Adding an AI-generated "insights summary" feature using an LLM call when the user only
  asked to improve layout and headings.
- ❌ Replacing `st.file_uploader` with a custom drag-and-drop JS component via
  `st.components.v1.html`.
- ❌ Adding a full theming system (light/dark toggle, multiple color palettes, a settings page)
  for an app that just needed clearer section headers.
- ❌ Rewriting the profiling/statistics logic "while I'm in there" instead of leaving it
  untouched and only changing presentation.
- ❌ Adding dependencies like `streamlit-extras`, `plotly`, or `pandas-profiling` when
  matplotlib and standard components already do the job.
