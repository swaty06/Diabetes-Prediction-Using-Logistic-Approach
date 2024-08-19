# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:22:51 2024

@author: rampr
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

# Load the trained model
with open('classifier_model.pkl', 'rb') as file:
    model = pickle.load(file)
    # Load the dataset for EDA
diabetes = load_diabetes(as_frame=True)
df = pd.concat([diabetes.data, pd.Series(diabetes.target, name="target")], axis=1)

# Function to get user input
def get_user_input():
    st.sidebar.header('User Input Parameters')

    # Input fields for user data
    pregnancies = st.sidebar.slider('Pregnancies', 0, 20, 1)
    glucose = st.sidebar.slider('Glucose', 0, 200, 120)
    blood_pressure = st.sidebar.slider('Blood Pressure', 0, 122, 70)
    skin_thickness = st.sidebar.slider('Skin Thickness', 0, 99, 20)
    insulin = st.sidebar.slider('Insulin', 0.0, 846.0, 79.0)
    bmi = st.sidebar.slider('BMI', 0.0, 67.1, 32.0)
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0, 2.42, 0.47)
    age = st.sidebar.slider('Age', 21, 100, 33)

    # Collecting input data into an array
    user_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    
    return user_data

# Function to create EDA visualizations
def eda():
    st.subheader('Exploratory Data Analysis (EDA)')

    st.write("### Distribution of Features")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.hist(ax=ax)
    st.pyplot(fig)

    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Main function to display the app
def main():
    st.title('Diabetes Prediction App')
    st.markdown("""
    This app predicts the likelihood of diabetes based on user input.
    Use the sidebar to adjust the input parameters and explore the data in the EDA section below.
    """)

    # Display EDA section
    eda_expander = st.expander("Explore Data (EDA)")
    with eda_expander:
        eda()

    # Get user input
    user_input = get_user_input()

    # Add a button for prediction
    if st.button('Predict Diabetes'):
        prediction = model.predict(user_input)
        st.subheader('Prediction Result:')
        if prediction[0] == 1:
            st.error('The model predicts that the patient **has diabetes**.')
        else:
            st.success('The model predicts that the patient **does not have diabetes**.')

if __name__ == '__main__':
    main()
