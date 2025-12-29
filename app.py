import streamlit as st
import pickle
import numpy as np

with open("house_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")

size = st.number_input("House Size (sqft)", min_value=200)
bedrooms = st.number_input("Bedrooms", min_value=1)
bathrooms = st.number_input("Bathrooms", min_value=1)
age = st.number_input("House Age", min_value=0)

if st.button("Predict Price"):
    data = np.array([[size, bedrooms, bathrooms, age]])
    prediction = model.predict(data)
    st.success(f"Predicted House Price: ₦{prediction[0]:,.2f}")
