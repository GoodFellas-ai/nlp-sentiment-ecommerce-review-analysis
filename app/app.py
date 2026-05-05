import streamlit as st
from transformers import pipeline

st.title("🤖 Sentiment Analyzer")

model = pipeline("sentiment-analysis")

text = st.text_area("Enter text")

if st.button("Analyze"):
    if text:
        result = model(text)[0]
        st.write("Sentiment:", result["label"])
        st.write("Score:", round(result["score"], 3))
