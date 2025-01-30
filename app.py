import streamlit as st
import pickle
import numpy as np



# Load the saved model
with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)

# Sidebar for navigation
st.sidebar.title("Heart Disease Prediction App")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Prediction"])

# Home Page
if app_mode == "Home":
    st.title("Heart Disease Prediction Using Machine Learning")
    st.write("Welcome to the Heart Disease Prediction app!")
    
    # Display an image
    st.image("Heart.jpg", caption="Predicting Heart Disease", use_container_width=True)  
    
    st.markdown("""
    ## Global Statistics
    - Heart disease is the leading cause of death worldwide.
    - Over **17 million** people die each year due to cardiovascular diseases.
    - Early detection can reduce the risk of complications.
""")

# About Page
elif app_mode == "About":
    st.title("About Heart Disease Prediction App")
    
    st.write("""
    This app leverages machine learning to predict the likelihood of heart disease based on various health factors.
    Heart disease is one of the leading causes of death worldwide, and early detection is crucial for effective intervention.
    
    The model used in this app was trained on a dataset of heart disease indicators, including features such as:
    - Age
    - Sex
    - Chest pain type
    - Resting blood pressure
    - Cholesterol levels
    - Fasting blood sugar levels
    - ECG results
    - Maximum heart rate
    - Exercise-induced angina
    - ST depression induced by exercise
    - Slope of the peak exercise ST segment
    - Number of major vessels colored by fluoroscopy
    - Thalassemia

    ## How It Works:
    1. You will be prompted to input various health factors into the app.
    2. Based on these inputs, the app uses a pre-trained machine learning model to predict whether you are at risk for heart disease.
    3. The prediction is provided in real-time, helping you understand your potential risk and take the necessary actions.

    ## Disclaimer:
    This app is for informational purposes only and should not be used as a substitute for professional medical advice. 
    Please consult with a healthcare provider for proper diagnosis and treatment.
    
    ## About the Model:
    The machine learning model used in this app is trained on historical health data and uses classification algorithms to predict the likelihood of heart disease.
    The model was trained using a dataset containing a variety of cardiovascular risk factors and outcomes.
    
    ### Author:
    This app was created by [Nikhil H and team] for educational purposes. 
    """)

    st.markdown("""
    ### References:
    - UCI Machine Learning Repository - Heart Disease Dataset: [Link](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
    """)
    
# Disease Prediction Page
elif app_mode == "Disease Prediction":
    st.title("Heart Disease Prediction")

    st.write("""
    Welcome to the heart disease prediction page. 
    Please enter your health details in the following fields, and the model will predict the likelihood of heart disease.
    """)

    # Input fields
    age = st.number_input("Age", min_value=1, max_value=200, value=50)
    sex = st.selectbox("Sex", options=["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=300, value=120)
    chol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", options=["Yes", "No"])
    restecg = st.selectbox("Resting ECG Results", options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150)
    exang = st.selectbox("Exercise-Induced Angina", options=["Yes", "No"])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=["Upsloping", "Flat", "Downsloping"])
    ca = st.number_input("Number of Major Vessels (0-3) Colored by Fluoroscopy", min_value=0, max_value=3, value=0)
    thal = st.selectbox("Thalassemia", options=["Normal", "Fixed Defect", "Reversible Defect"])

    # Map categorical inputs to numerical values
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "Yes" else 0
    exang = 1 if exang == "Yes" else 0
    restecg_mapping = {"Normal": 0, "ST-T Wave Abnormality": 1, "Left Ventricular Hypertrophy": 2}
    restecg = restecg_mapping[restecg]
    slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    slope = slope_mapping[slope]
    thal_mapping = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}
    thal = thal_mapping[thal]
    cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
    cp = cp_mapping[cp]

    # Predict button
    if st.button("Predict"):
        # Create the input features array
        input_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        prediction = model.predict(input_features)
        prediction_proba = model.predict_proba(input_features)  # Get the probability
        
        # Display the result
        if prediction[0] == 1:
            st.error("Prediction: **The model predicted that you have heart disease Please consult a healthcare professional for further evaluation")
            st.write(f"Confidence: {prediction_proba[0][1]*100:.2f}%")
            
        else:
            st.success("Prediction: **The model predicted that you don't have heart disease Keep maintaining a healthy lifestyle!.**")
            st.write(f"Confidence: {prediction_proba[0][0]*100:.2f}%")
            