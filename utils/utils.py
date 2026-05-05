import pandas as pd
import re

# Define clean_text function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Define map_sentiment function
def map_sentiment(rating):
    if rating <= 2:
        return "negative"
    elif rating == 3:
        return "neutral"
    else:
        return "positive"

# Reload the DataFrame to ensure all original columns are present
df = pd.read_csv("Womens_Clothing_E-Commerce_Reviews.csv")

# Drop rows where 'Review Text' or 'Rating' are missing
df = df.dropna(subset=["Review Text", "Rating"])

# Sample the DataFrame (if it has more than 8000 rows, for consistency with previous steps)
df = df.sample(min(len(df), 8000), random_state=42)

# Apply text cleaning and sentiment mapping
df["cleaned"] = df["Review Text"].apply(clean_text)
df["sentiment"] = df["Rating"].apply(map_sentiment)

# Display first few rows and columns to verify
print("DataFrame columns after preparation:")
print(df.columns)
df.head()
