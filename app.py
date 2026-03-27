import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.getcwd())

from src.ingestion.csv_loader import load_csv
from src.processing.cleaner import clean_text
from src.processing.sentiment import analyze_sentiment
from src.processing.categorizer import categorize

st.title("Feedback Intelligence Dashboard")

df = load_csv("data/sample.csv")

# Process data
df["clean_text"] = df["text"].apply(clean_text)

sentiments = df["clean_text"].apply(analyze_sentiment)
df["sentiment"] = sentiments.apply(lambda x: x[0])
df["score"] = sentiments.apply(lambda x: x[1])

df["category"] = df["clean_text"].apply(categorize)

# Show data
st.write(df.head())

# Charts
st.subheader("Sentiment Distribution")
st.bar_chart(df["sentiment"].value_counts())

st.subheader("Category Distribution")
st.bar_chart(df["category"].value_counts())
