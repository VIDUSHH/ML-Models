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
        
    Age = st.text_input("Age of the Person")
    Sex = st.text_input("Sex of the person")
    Chest_Pain = st.text_input("chest pain type (4 values)")
    Resting_BP = st.text_input("resting blood pressure (in mm Hg on admission to the hospital)")
    Cholestoral = st.text_input("serum cholestoral in mg/dl")
    Fasting_Blood_Sugar = st.text_input("(fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)")
    Resting_ElectroCardiographic = st.text_input("resting electrocardiographic results")
    Max_Heart_Rate = st.text_input("maximum heart rate achieved")
    Exercise_included = st.text_input("exercise induced angina (1 = yes; 0 = no)")
    oldpeak = st.text_input("ST depression induced by exercise relative to rest")
    slope = st.text_input("the slope of the peak exercise ST segment")
    Vessels = st.text_input("number of major vessels (0-3) colored by flourosopy")
    Defect = st.text_input("1 = normal; 2 = fixed defect; 3 = reversable defect")
    
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
    