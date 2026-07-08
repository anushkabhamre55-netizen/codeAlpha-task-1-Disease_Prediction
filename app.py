import streamlit as st
import pickle
from sklearn.datasets import load_breast_cancer

# Load trained model
model = pickle.load(open("disease_model.pkl", "rb"))

# Load dataset for feature names
data = load_breast_cancer()

st.title("Disease Prediction System")
st.write("Breast Cancer Prediction using Machine Learning")

# Input fields
features = []

for feature in data.feature_names[:5]:
    value = st.number_input(feature, value=1.0)
    features.append(value)

# Fill remaining features with 0
while len(features) < 30:
    features.append(0)

# Prediction button
if st.button("Predict"):

    prediction = model.predict([features])

    if prediction[0] == 1:
        st.success("Prediction: Benign (No Cancer)")
    else:
        st.error("Prediction: Malignant (Cancer Detected)")