import streamlit as st
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("Microfinance Loan Prediction")

st.write("Enter applicant details to predict loan approval:")

# Input fields for all 12 features
Dependents = st.number_input("Dependents", min_value=0, max_value=10, value=0)
ApplicantIncome = st.number_input("Applicant Income", min_value=0, value=5000)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0, value=0)
LoanAmount = st.number_input("Loan Amount", min_value=0, value=150)
Loan_Amount_Term = st.number_input("Loan Amount Term (months)", min_value=0, value=360)
Credit_History = st.selectbox("Credit History", options=[0, 1], index=1)
Gender_Male = st.selectbox("Gender Male", options=[0, 1], index=1)
Married_Yes = st.selectbox("Married Yes", options=[0, 1], index=1)
Education_Not_Graduate = st.selectbox("Education Not Graduate", options=[0, 1], index=0)
Self_Employed_Yes = st.selectbox("Self Employed Yes", options=[0, 1], index=0)
Property_Area_Semiurban = st.selectbox("Property Area Semiurban", options=[0, 1], index=1)
Property_Area_Urban = st.selectbox("Property Area Urban", options=[0, 1], index=0)

# Predict button
if st.button("Predict Loan Status"):
    features = [Dependents, ApplicantIncome, CoapplicantIncome, LoanAmount,
                Loan_Amount_Term, Credit_History, Gender_Male, Married_Yes,
                Education_Not_Graduate, Self_Employed_Yes, Property_Area_Semiurban,
                Property_Area_Urban]
    prediction = model.predict([features])[0]
    
    if prediction == 1:
        st.success("✅ Loan likely to be approved")
    else:
        st.error("❌ Loan likely to be rejected")
