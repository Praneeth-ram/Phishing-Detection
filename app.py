import streamlit as st
import requests

st.title("Phishing URL Detector")
url = st.text_input("Enter URL:")

if st.button("Check"):
    response = requests.post("http://127.0.0.1:8000/predict/", json={"url": url})
    
    try:
        result = response.json()
        st.write("Response:", result)  # Debugging output

        if isinstance(result, dict) and "phishing" in result:
            if result["phishing"]:
                st.error("🚨 Phishing URL")
            else:
                st.success("✅ Legitimate URL")
        else:
            st.error("Unexpected response format")
    except Exception as e:
        st.error(f"Error processing response: {e}")
