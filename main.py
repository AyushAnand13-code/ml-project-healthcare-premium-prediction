import streamlit as st
from prediction_helper import predict

st.title("Health Insurance Cost Predictor")

# Row 1
col1, col2, col3 = st.columns(3)
age = col1.number_input("Age", min_value=0, max_value=100, step=1)
gender = col2.selectbox("Gender", ["Male", "Female"])
region = col3.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

# Row 2
col4, col5, col6 = st.columns(3)
number_of_dependants = col4.number_input("Number of Dependants", min_value=0, max_value=10, step=1)
marital_status = col5.selectbox("Marital Status", ["Unmarried", "Married"])
bmi_category = col6.selectbox("BMI Category", ["Overweight", "Underweight", "Normal", "Obesity"])

# Row 3
col7, col8, col9 = st.columns(3)
smoking_status = col7.selectbox("Smoking Status", ["Regular", "No Smoking", "Occasional", "Smoking=0", "Does Not Smoke", "Not Smoking"])
employment_status = col8.selectbox("Employment Status", ["Self-Employed", "Freelancer", "Salaried"])
income_level = col9.selectbox("Income Level", ["> 40L", "<10L", "10L - 25L", "25L - 40L"])

# Row 4
col10, col11, col12 = st.columns(3)
income_lakhs = col10.number_input("Income (in Lakhs)", min_value=0, max_value=100, step=1)
medical_history = col11.selectbox("Medical History", [
    "High blood pressure", "No Disease", "Diabetes & High blood pressure",
    "Diabetes & Heart disease", "Diabetes", "Diabetes & Thyroid",
    "Heart disease", "Thyroid", "High blood pressure & Heart disease"
])
insurance_plan = col12.selectbox("Insurance Plan", ["Silver", "Bronze", "Gold"])

# Store inputs in a dictionary
input_dict = {
    "age": age,
    "gender": gender,
    "region": region,
    "number_of_dependants": number_of_dependants,
    "marital_status": marital_status,
    "bmi_category": bmi_category,
    "smoking_status": smoking_status,
    "employment_status": employment_status,
    "income_level": income_level,
    "income_lakhs": income_lakhs,
    "medical_history": medical_history,
    "insurance_plan": insurance_plan
}

# Predict button
if st.button("Predict"):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium: {prediction}")

