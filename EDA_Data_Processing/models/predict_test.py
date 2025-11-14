# from fastapi import FastAPI
# import pickle
# import numpy as np
# from schemas import LoanRequest

# app = FastAPI()

# # Load model and scaler
# model = pickle.load(open("model/loan_best_model.pkl", "rb"))
# scaler = pickle.load(open("model/loan_scaler.pkl", "rb"))

# @app.post("/predict")
# def predict_loan_status(data: LoanRequest):
#     input_data = np.array([[ 
#         data.ApplicantIncome, data.CoapplicantIncome, data.LoanAmount,
#         data.Loan_Amount_Term, data.Credit_History,
#         data.Gender, data.Married, data.Dependents,
#         data.Education, data.Self_Employed, data.Property_Area
#     ]])

#     # Perform scaling if necessary
#     scaled_input = scaler.transform(input_data)

#     prediction = model.predict(scaled_input)[0]
#     probability = model.predict_proba(scaled_input)[0][1]

#     return {
#         "prediction": int(prediction),
#         "probability": float(probability)
#     }


import requests
import pandas as pd

url = "http://127.0.0.1:8000/predict"

# === testing applicants ===
samples = {
    "High Approval": {
        "Gender": "Male",
        "Married": "Yes",
        "Dependents": "0",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 7000,
        "CoapplicantIncome": 2000,
        "LoanAmount": 100,
        "Loan_Amount_Term": 360,
        "Credit_History": 1.0,
        "Property_Area": "Urban"
    },
    "Borderline": {
        "Gender": "Male",
        "Married": "Yes",
        "Dependents": "1",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 4500,
        "CoapplicantIncome": 1200,
        "LoanAmount": 150,
        "Loan_Amount_Term": 360,
        "Credit_History": 0.0,
        "Property_Area": "Semiurban"
    },
    "Low Approval": {
        "Gender": "Female",
        "Married": "No",
        "Dependents": "2",
        "Education": "Not Graduate",
        "Self_Employed": "Yes",
        "ApplicantIncome": 2500,
        "CoapplicantIncome": 0,
        "LoanAmount": 200,
        "Loan_Amount_Term": 360,
        "Credit_History": 0.0,
        "Property_Area": "Rural"
    }
}

# === Collecting predictions ===
results = []
for label, data in samples.items():
    r = requests.post(url, json=data).json()
    results.append({
        "Case": label,
        "Prediction": "Approved" if r["prediction"] == 1 else "Rejected",
        "Probability": round(r["probability"], 3)
    })

# === Displaying ===
df = pd.DataFrame(results)
print(df.to_string(index=False))