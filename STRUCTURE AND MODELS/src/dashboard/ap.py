import streamlit as st
import pandas as pd
import joblib

st.title("Traffic Accident Risk Predictor")

model = joblib.load('../models/model.pkl')
user_input = st.text_input("Enter location coordinates (lat,long):")

if user_input:
    # Mock processing
    result = model.predict([[some_features]])
    st.write("Accident Risk Level:", result)