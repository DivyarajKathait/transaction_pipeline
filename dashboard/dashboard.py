import streamlit as st
import pandas as pd
import psycopg2
from streamlit_autorefresh import st_autorefresh

#hello

st.set_page_config(layout="wide")
# 🔁 Auto-refresh every 2 seconds
st_autorefresh(interval=2000, key="refresh")

# 🛢️ Connect to DB
conn = psycopg2.connect(
    dbname="transaction_db",
    user="postgres",
    password="postgres",
    host="localhost"
)
# 📦 Query 100 recent transactions
recent_df = pd.read_sql("""
    SELECT * FROM transactions
    ORDER BY timestamp DESC
    LIMIT 100
""", conn)

# 📊 Query failure rate from ALL transactions
all_df = pd.read_sql("""
    SELECT status FROM transactions
""", conn)

# 📉 Calculate metrics
total = len(all_df)
failures = (all_df["status"] == "FAILED").sum()
failure_rate = (failures / total) * 100 if total > 0 else 0

# 🎯 Anomaly count
anomalies = (recent_df["is_anomaly"] == True).sum()

# 🖥️ Display
st.title("📊 Real-Time Transaction Monitoring Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("All Transactions", total)
col2.metric("Failure Rate (ALL)", f"{failure_rate:.2f}%")
col3.metric("Anomalies in last 100", anomalies)

st.bar_chart(recent_df["status"].value_counts())
st.line_chart(recent_df.groupby("timestamp")["amount"].sum())

st.subheader("🧾 Recent 100 Transactions")
st.dataframe(recent_df.sort_values(by="timestamp", ascending=False))
def highlight_anomalies(row):
    return ['background-color: red' if row['is_anomaly'] else '' for _ in row]

st.dataframe(recent_df.style.apply(highlight_anomalies, axis=1))


