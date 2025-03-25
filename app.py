import streamlit as st
import joblib
import numpy as np
import pickle
with open("survival_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the trained model
model = joblib.load("survival_model.pkl")

# Streamlit app UI
st.title("Survival Prediction App")

# Input fields
age = st.number_input("Enter Age:", min_value=0, max_value=120, value=30)
sex = st.selectbox("Select Sex:", ["Male", "Female"])
smoker = st.selectbox("Are you a Smoker?", ["Yes", "No"])

# Convert categorical data
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0

# Predict button
if st.button("Predict"):
    features = np.array([[age, sex, smoker]])
    prediction = model.predict(features)[0]
    
    st.write(f"Predicted Survival Probability: {prediction:.2f}")
