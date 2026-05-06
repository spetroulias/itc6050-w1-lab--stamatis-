import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
st.set_page_config(page_title="ITC6050 — GitHub Issue Health",
layout="wide")
st.title("📊 GitHub Issue Health Dashboard")
st.caption("ITC 6050 — Week 1 Lab — Mini End-to-End Pipeline")
engine = create_engine(
"postgresql+psycopg2://itc6050:itc6050@localhost:5432/lab"
)
df = pd.read_sql(
"SELECT * FROM analytics.issues_summary ORDER BY month",
engine,
)
# --- Top-line KPIs -------------------------------------------------------
total = int(df["issue_count"].sum())
open_now = int(df.loc[df["state"] == "open", "issue_count"].sum())
avg_days = round(df["avg_days_open"].mean(), 1)
col1, col2, col3 = st.columns(3)
col1.metric("Total issues", f"{total:,}")
col2.metric("Currently open", f"{open_now:,}")
col3.metric("Avg days open", f"{avg_days}")
# --- Chart ---------------------------------------------------------------
st.subheader("Issues by month")
chart = df.pivot(index="month", columns="state",
values="issue_count").fillna(0)
st.bar_chart(chart)
# --- Table ---------------------------------------------------------------
st.subheader("Raw summary")
st.dataframe(df, use_container_width=True)
