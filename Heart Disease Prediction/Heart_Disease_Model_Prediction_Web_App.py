# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 21:42:41 2025

@author: Vidush
"""

import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('Heart Disease Prediction/models/heart_disease_model.sav', 'rb'))

def heart_disease_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype = float)

    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return "The Person does not have a Heart Disease"
    else:
      return "The Person has Heart Disease"
  
    
def main():
    #Giving a title
    st.title("Heart Disease Prediction Web App")
    
    #Getting the input data from the user
        
   import streamlit as st

st.title("Heart Disease Prediction Form")

Age = st.text_input(
    "Age of the Person (in years)",
    help="Enter your age as a number between 1 and 120 (e.g., 45)"
)

Sex = st.selectbox(
    "Sex of the Person",
    options=["0 = Female", "1 = Male"],
    help="Select 0 for Female, 1 for Male"
)

Chest_Pain = st.selectbox(
    "Chest Pain Type",
    options=[
        "0 = Typical Angina",
        "1 = Atypical Angina",
        "2 = Non-anginal Pain",
        "3 = Asymptomatic"
    ],
    help="Select a number from 0 to 3 based on your chest pain symptoms"
)

Resting_BP = st.text_input(
    "Resting Blood Pressure (in mm Hg)",
    help="Enter a number between 80 and 200 (e.g., 130)"
)

Cholestoral = st.text_input(
    "Serum Cholesterol (in mg/dl)",
    help="Enter a number typically between 100 and 600 (e.g., 250)"
)

Fasting_Blood_Sugar = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl?",
    options=["0 = No", "1 = Yes"],
    help="Select 1 if your fasting blood sugar is above 120 mg/dl, else 0"
)

Resting_ElectroCardiographic = st.selectbox(
    "Resting Electrocardiographic Results",
    options=[
        "0 = Normal",
        "1 = ST-T wave abnormality",
        "2 = Left ventricular hypertrophy"
    ],
    help="Select one of the 3 ECG result categories"
)

Max_Heart_Rate = st.text_input(
    "Maximum Heart Rate Achieved",
    help="Enter a number between 60 and 220 (e.g., 170)"
)

Exercise_included = st.selectbox(
    "Exercise Induced Angina",
    options=["0 = No", "1 = Yes"],
    help="Select 1 if you experienced angina during exercise, else 0"
)

oldpeak = st.text_input(
    "ST Depression (Oldpeak) Relative to Rest",
    help="Enter a decimal value (e.g., 1.4), typically ranges from 0 to 6"
)

slope = st.selectbox(
    "Slope of the Peak Exercise ST Segment",
    options=[
        "0 = Upsloping",
        "1 = Flat",
        "2 = Downsloping"
    ],
    help="Select the appropriate slope type"
)

Vessels = st.selectbox(
    "Number of Major Vessels Colored by Fluoroscopy (0-3)",
    options=["0", "1", "2", "3"],
    help="Enter the number of vessels (0-3)"
)

Defect = st.selectbox(
    "Thalassemia Defect Type",
    options=[
        "1 = Normal",
        "2 = Fixed Defect",
        "3 = Reversible Defect"
    ],
    help="Select the defect type based on diagnosis"
)

    #Code for Prediction
    target = ''
    
    #Creating a button for Prediction
    if st.button("Heart Condition: "):
       target = heart_disease_prediction([
    float(Age), float(Sex), float(Chest_Pain), float(Resting_BP), float(Cholestoral),
    float(Fasting_Blood_Sugar), float(Resting_ElectroCardiographic), float(Max_Heart_Rate),
    float(Exercise_included), float(oldpeak), float(slope), float(Vessels), float(Defect)])

    st.success(target)
    
    
if __name__ == '__main__':
    main()
    
