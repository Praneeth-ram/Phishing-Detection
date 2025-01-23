import streamlit as st
import requests

st.title("Phishing URL Detector")
url = st.text_input("Enter URL:")

if st.button("Check"):
    response = requests.post("http://127.0.0.1:8000/predict/", json={"url": url})
    result = response.json()
    if result["phishing"]:
        st.error("🚨 Phishing URL")
    else:
        st.success("✅ Legitimate URL")
