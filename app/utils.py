
import pandas as pd

# ==============================
# LOAD DATA
# ==============================
def load_data():
    ethiopia = pd.read_csv("data/ethiopia_clean.csv")
    kenya = pd.read_csv("data/kenya_clean.csv")
    nigeria = pd.read_csv("data/nigeria_clean.csv")

    ethiopia["country"] = "Ethiopia"
    kenya["country"] = "Kenya"
    nigeria["country"] = "Nigeria"

    df = pd.concat([ethiopia, kenya, nigeria], ignore_index=True)
    df.columns = df.columns.str.lower().str.strip()

    return df


# ==============================
# FILTER BY COUNTRY
# ==============================
def filter_by_country(df, countries):
    return df[df["country"].isin(countries)]


# ==============================
# MONTHLY AGGREGATION
# ==============================
def monthly_avg(df, value_col="t2m"):
    df["date"] = pd.to_datetime(df[["year", "month"]].assign(day=1))
    return df.groupby(["date", "country"])[value_col].mean().reset_index()


# ==============================
# VULNERABILITY FEATURES
# ==============================
def add_features(df):
    df["t2m_range"] = df["t2m_max"] - df["t2m_min"]
    return df
