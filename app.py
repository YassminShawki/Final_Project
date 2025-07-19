import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("random_forest_model.pkl")

st.set_page_config(page_title="California Housing Price Predictor")
st.title("🏠 California Housing Price Predictor")
st.markdown("Enter house details below to predict its price using a trained Random Forest model.")

# Input fields
crim = st.number_input("Per capita crime rate by town (CRIM)", min_value=0.0, value=0.1)
zn = st.number_input("Proportion of residential land zoned for large lots (ZN)", min_value=0.0, value=0.0)
indus = st.number_input("Proportion of non-retail business acres (INDUS)", min_value=0.0, value=7.0)
chas = st.selectbox("Tract bounds Charles River? (CHAS)", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
nox = st.number_input("Nitric oxide concentration (NOX)", min_value=0.0, max_value=1.0, value=0.5)
rm = st.slider("Average number of rooms (RM)", 3.0, 9.0, 6.0)
age = st.slider("Proportion of units built before 1940 (AGE)", 0.0, 100.0, 60.0)
dis = st.number_input("Weighted distances to employment centers (DIS)", min_value=1.0, value=4.0)
rad = st.selectbox("Accessibility to radial highways (RAD)", options=list(range(1, 25)))
tax = st.slider("Full-value property-tax rate (TAX)", 180, 720, 300)
ptratio = st.slider("Pupil-teacher ratio (PTRATIO)", 12.0, 22.0, 18.0)
b = st.number_input("1000(Bk - 0.63)^2 (B)", min_value=0.0, value=300.0)
lstat = st.slider("% lower status of the population (LSTAT)", 1.0, 40.0, 12.0)


# Prediction
if st.button("Predict Price"):
    input_data = np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
    predicted_price = model.predict(input_data)[0]
    st.success(f"Predicted house price: ${predicted_price * 1000:.2f}")
