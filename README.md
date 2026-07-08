# Disease Prediction Using Machine Learning

## Project Overview

This project predicts whether a breast cancer tumor is benign or malignant using Machine Learning. A Random Forest Classifier is trained on the Breast Cancer Dataset from Scikit-Learn and deployed using Streamlit.

## Objective

The objective of this project is to develop a machine learning model that can assist in disease prediction based on medical features.

## Technologies Used

* Python
* Scikit-Learn
* Pandas
* NumPy
* Streamlit
* Google Colab
* VS Code

## Dataset

The project uses the Breast Cancer Wisconsin Dataset available in Scikit-Learn.

Features include:

* Radius
* Texture
* Perimeter
* Area
* Smoothness
* And other medical measurements

## Machine Learning Algorithm

Random Forest Classifier

## Project Workflow

1. Load the dataset
2. Preprocess the data
3. Split into training and testing sets
4. Train the Random Forest model
5. Evaluate model performance
6. Save the trained model
7. Build a Streamlit application
8. Predict disease status

## Model Performance

* Accuracy: Approximately 95%–98%

## Project Files

* Disease_Prediction.ipynb
* app.py
* disease_model.pkl
* README.md

## How to Run

### Install Required Libraries

pip install streamlit scikit-learn pandas numpy

### Run the Application

streamlit run app.py

## Sample Output

The application predicts:

* Benign (No Cancer)
* Malignant (Cancer Detected)

## Future Improvements

* Improve UI design
* Deploy the application online
* Use additional datasets for better accuracy

## Author

Anushka Shamkant Bhamare

Data Science Engineering Student
