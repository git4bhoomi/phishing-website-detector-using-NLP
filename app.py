#app.py
import streamlit as st
import re
import joblib

# Load saved model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Clean URL function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'https?://', '', text)
    return text

# Page title
st.title("🔐 Phishing Website Detector")

st.write("Enter a URL and the model will predict whether it is phishing or legitimate.")

# Input box
url = st.text_input("Enter Website URL")

# Predict button
if st.button("Analyze"):

    if url.strip() == "":
        st.warning("Please enter a URL.")

    else:
        cleaned_url = clean_text(url)
        vector = vectorizer.transform([cleaned_url])
        prediction = model.predict(vector)

        if prediction[0] == "bad":
            st.error("⚠️ Phishing Website Detected")
        else:
            st.success("✅ Legitimate Website")
