import streamlit as st
import pandas as pd
from transformers import pipeline

st.set_page_config(page_title="Sentiment Dashboard", layout="wide")

df = pd.read_csv("Womens Clothing E-Commerce Reviews.csv")
model = pipeline("sentiment-analysis")

# SIDEBAR NAV
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Analyze Text"])

# ================= DASHBOARD =================
if page == "Dashboard":

    st.title("📊 E-Commerce Sentiment Dashboard")

    # METRICS ROW (FEELING LIKE APPLE DASHBOARD)
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Reviews", len(df))
    c2.metric("Avg Rating", round(df["Rating"].mean(), 2))
    c3.metric("Unique Ratings", df["Rating"].nunique())

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Rating Distribution")
        st.bar_chart(df["Rating"].value_counts().sort_index())

    with col2:
        st.subheader("Sample Reviews")
        st.dataframe(df[["Review Text", "Rating"]].head(10))

# ================= ANALYZE PAGE =================
elif page == "Analyze Text":

    st.title("🧠 Sentiment Analyzer")

    text = st.text_area("Enter review text")

    if st.button("Analyze"):
        result = model(text)[0]

        st.markdown("### Result")
        st.success(f"Sentiment: {result['label']}")
        st.info(f"Confidence: {round(result['score'], 3)}")

    st.divider()

    if st.button("Random Review Test"):
        sample = df["Review Text"].dropna().sample(1).iloc[0]
        st.write(sample)

        result = model(sample)[0]
        st.write(result)