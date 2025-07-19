{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "97a4f067-4fe9-42c3-afe0-98b8701d3f84",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app.py\n",
    "import streamlit as st\n",
    "import numpy as np\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "913da103-a9e0-4e86-8edc-44fe8a790c00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load the trained model\n",
    "model = joblib.load(\"random_forest_model.pkl\")\n",
    "\n",
    "st.set_page_config(page_title=\"Boston Housing Price Predictor\")\n",
    "st.title(\"🏠 Boston Housing Price Predictor\")\n",
    "st.markdown(\"Enter house details below to predict its price using a trained Random Forest model.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0d0924f7-2bfc-4a5b-ad96-a2359542ed25",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Input fields\n",
    "rm = st.slider(\"Average number of rooms per dwelling (RM)\", 3.0, 9.0, 6.0)\n",
    "lstat = st.slider(\"% lower status of the population (LSTAT)\", 1.0, 40.0, 12.0)\n",
    "ptratio = st.slider(\"Pupil-teacher ratio by town (PTRATIO)\", 12.0, 22.0, 18.0)\n",
    "tax = st.slider(\"Property tax rate (TAX)\", 180, 720, 300)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "475e8045-5e8a-4096-95f0-9b4b3818e7d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Prediction\n",
    "if st.button(\"Predict Price\"):\n",
    "    input_data = np.array([[rm, lstat, ptratio, tax]])\n",
    "    predicted_price = model.predict(input_data)[0]\n",
    "    st.success(f\"Predicted house price: ${predicted_price * 1000:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c6a1243-b0d5-4fa8-857c-4ec4a22775a2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
