import streamlit as st
import requests

st.title("🤖 Hugging Face ML Sentiment Analyzer")

user_input = st.text_area("Enter text for sentiment analysis:")

if st.button("Analyze Sentiment"):
    if user_input:
        API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

        headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": user_input})
            response.raise_for_status()
            result = response.json()

            st.subheader("Analysis Result:")

            if isinstance(result, list) and result:
                st.write(f"**Sentiment:** {result[0]['label']}")
                st.write(f"**Confidence:** {result[0]['score']:.2f}")
            else:
                st.write(result)

        except Exception as e:
            st.error(f"Hata: {e}")
