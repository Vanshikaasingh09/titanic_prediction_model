import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model/titanic_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎯 Titanic Survival Predictor")

# User inputs
sex = st.selectbox("Sex", ["male", "female"])
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.slider("Fare", 0.0, 500.0, 50.0)
embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

# Map categorical inputs
sex = 0 if sex == "male" else 1
embarked_map = {"S": 0, "C": 1, "Q": 2}
embarked = embarked_map[embarked]

# Predict
if st.button("Predict"):
    features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
    prediction = model.predict(features)[0]
    st.success("🎉 Survived!" if prediction == 1 else "❌ Did not survive.")
