import streamlit as st
import pandas as pd

st.title("🌍 Climate Dashboard")

df = pd.read_csv("data/ethiopia_clean.csv")

country = st.selectbox("Select Country", df['country'].unique())

filtered = df[df['country'] == country]

st.line_chart(filtered.groupby('month')['t2m'].mean())
st.bar_chart(filtered.groupby('month')['prectotcorr'].mean())