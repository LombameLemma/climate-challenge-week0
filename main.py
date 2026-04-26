import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🌍 Climate Dashboard")

df = pd.read_csv("data/ethiopia_clean.csv")

countries = st.multiselect("Select Country", df["country"].unique(), default=df["country"].unique())

filtered = df[df["country"].isin(countries)]

year_range = st.slider("Year Range", int(df["year"].min()), int(df["year"].max()), (2015, 2026))

filtered = filtered[(filtered["year"] >= year_range[0]) & (filtered["year"] <= year_range[1])]

st.subheader("Temperature Trend")
st.line_chart(filtered.groupby("month")["t2m"].mean())

st.subheader("Precipitation")
fig, ax = plt.subplots()
sns.boxplot(data=filtered, x="country", y="prectotcorr", ax=ax)
st.pyplot(fig)
