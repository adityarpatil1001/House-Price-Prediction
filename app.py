import streamlit as st

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠"
)

st.title("🏠 House Price Prediction App")

st.write("Welcome to my first Machine Learning Web App!")

st.success("Streamlit is working successfully! 🎉")

import streamlit as st
import joblib

# Load trained model
model = joblib.load("models/xgb_model.pkl")

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠"
)

st.title("🏠 House Price Prediction")

st.success("Model loaded successfully! ✅")