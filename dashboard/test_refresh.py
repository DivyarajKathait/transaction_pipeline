# test_refresh.py
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import datetime

st_autorefresh(interval=1000, key="test")

st.write("⏱️ Current time:", datetime.datetime.now())
