import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("random_forest_model.pkl")

st.set_page_config(page_title="California Housing Price Predictor")
st.title("🏠 California Housing Price Predictor")
st.markdown("Enter house details below to predict its price using a trained Random Forest model.")

# Input fields
rm = st.slider("Average number of rooms per dwelling (RM)", 3.0, 9.0, 6.0)
lstat = st.slider("% lower status of the population (LSTAT)", 1.0, 40.0, 12.0)
ptratio = st.slider("Pupil-teacher ratio by town (PTRATIO)", 12.0, 22.0, 18.0)
tax = st.slider("Property tax rate (TAX)", 180, 720, 300)

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[rm, lstat, ptratio, tax]])
    predicted_price = model.predict(input_data)[0]
    st.success(f"Predicted house price: ${predicted_price * 1000:.2f}")
