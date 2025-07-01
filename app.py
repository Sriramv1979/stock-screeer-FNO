import streamlit as st
import requests

st.title("F&O Screener")
MODE = st.sidebar.radio("Mode", ["Manual", "Auto (2 min)"])
if st.sidebar.button("Refresh") or MODE.startswith("Auto"):
    data = requests.get("http://localhost:8000/screener").json()
    st.write(data)