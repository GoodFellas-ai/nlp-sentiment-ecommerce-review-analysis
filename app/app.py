# To run this Streamlit app in Colab, you need to install Streamlit first.
# This line should ideally be run once, or handled in a requirements.txt for actual deployment.
pip install streamlit

import streamlit as st
import requests

st.title("🤖 Hugging Face ML Sentiment Analyzer")

user_input = st.text_area("Enter text for sentiment analysis:")

if st.button("Analyze Sentiment"):
    if user_input:
        # Using a specific Hugging Face sentiment analysis model's inference API.
        # Example: distilbert-base-uncased-finetuned-sst-2-english
        API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
        
        # IMPORTANT: Replace "YOUR_HF_TOKEN" with your actual Hugging Face API token.
        # You can get one from your Hugging Face settings (https://huggingface.co/settings/tokens).
        # For secure deployment, consider using Streamlit secrets (st.secrets["HF_TOKEN"]).
        headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": user_input})
            response.raise_for_status() # Raise an exception for HTTP errors (e.g., 401, 404, 500)
            result = response.json()

            st.subheader("Analysis Result:")
            # Hugging Face API response for sentiment analysis is typically a list of dictionaries
            # e.g., [{'label': 'POSITIVE', 'score': 0.999...}]
            if isinstance(result, list) and result:
                sentiment_label = result[0].get('label')
                sentiment_score = result[0].get('score')
                st.write(f"**Sentiment:** {sentiment_label}")
                st.write(f"**Confidence:** {sentiment_score:.2f}")
            else:
                st.write("Could not parse sentiment from API response.")
                st.write(result) # Display raw result for debugging
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to Hugging Face API: {e}")
            st.info("Please ensure your Hugging Face token is correct and the model URL is valid.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
