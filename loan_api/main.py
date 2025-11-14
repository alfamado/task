# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from typing import Optional, Dict, Any
# import pandas as pd
# import numpy as np
# import joblib
# import os
# import uvicorn
# # from schemas import LoanRequest

# # -------- Configuration --------
# ARTIFACTS_PATH = r"C:\Users\NCC200\Desktop\TASK\EDA_Data_Processing\processed\preprocessing_artifacts.joblib"
# TRAIN_CLEANED_PATH = r"C:\Users\NCC200\Desktop\TASK\EDA_Data_Processing\processed\home_loan_train_cleaned.csv"
# MODEL_PATH = r"C:\Users\NCC200\Desktop\TASK\EDA_Data_Processing\loan_best_model.joblib"

# # -------- App --------
# app = FastAPI(title="Home Loan Approval - Prediction API",
#               description="Predict loan approval using a saved RandomForest model + preprocessing artifacts.",
#               version="1.0.0")

# # -------- Startup: load artifacts & model --------
# @app.on_event("startup")
# def load_artifacts():
#     global artifacts, model, expected_features, label_encoders, num_imputer, cat_imputer, scaler

#     # Load preprocessing artifacts
#     if not os.path.exists(ARTIFACTS_PATH):
#         raise RuntimeError(f"Preprocessing artifacts not found at: {ARTIFACTS_PATH}")
#     artifacts = joblib.load(ARTIFACTS_PATH)

#     # Expect these keys; be forgiving if some are absent
#     label_encoders = artifacts.get("label_encoders", {}) # dict: column -> LabelEncoder
#     num_imputer = artifacts.get("num_imputer", None)
#     cat_imputer = artifacts.get("cat_imputer", None)
#     scaler = artifacts.get("scaler", None)

#     # Load model
#     if not os.path.exists(MODEL_PATH):
#         raise RuntimeError(f"Model file not found at: {MODEL_PATH}")
#     model = joblib.load(MODEL_PATH)

#     # Load final features order from sample processed train CSV header
#     if not os.path.exists(TRAIN_CLEANED_PATH):
#         raise RuntimeError(f"Processed train CSV not found at: {TRAIN_CLEANED_PATH}")
#     expected_features = list(pd.read_csv(TRAIN_CLEANED_PATH, nrows=0).columns)
#     # Remove target if present
#     if "Loan_Status" in expected_features:
#         expected_features.remove("Loan_Status")

#     print("Loaded artifacts, model, and expected feature list.")
#     print(f"Number of features expected by model: {len(expected_features)}")


# # -------- Input schema (raw input) --------
# # We accept free-form JSON with raw fields (the original dataset fields).
# # If you prefer, pass the already-processed features matching expected_features.
# class LoanRequest(BaseModel):
#     # All original fields optional (we'll compute engineered fields as needed).
#     Gender: Optional[str] = None
#     Married: Optional[str] = None
#     Dependents: Optional[str] = None
#     Education: Optional[str] = None
#     Self_Employed: Optional[str] = None
#     ApplicantIncome: Optional[float] = None
#     CoapplicantIncome: Optional[float] = None
#     LoanAmount: Optional[float] = None
#     Loan_Amount_Term: Optional[float] = None
#     Credit_History: Optional[float] = None
#     Property_Area: Optional[str] = None
#     # Allow extra fields (client might send engineered fields directly)
#     class Config:
#         extra = "allow"

# # -------- Preprocessing Function --------
# def replicate_preprocessing(raw_payload: Dict[str, Any]) -> pd.DataFrame:
#     """
#     Input: raw_payload (dict) with original dataset fields.
#     Output: DataFrame with columns matching expected_features in the same order.
#     This function follows the same steps as the notebook's preprocessing:
#       - Dependents '3+' -> 3
#       - Create Total_Income, emi_estimate, income_to_loan_ratio, income_per_dependent
#       - Create missing flags if a field is missing in the incoming payload (best-effort)
#       - Impute using saved imputers
#       - Encode binary columns using saved label encoders
#       - One-hot encode nominal columns by comparing to expected_features and aligning
#       - Scale numeric features using saved scaler
#     NOTE: This function aims to be robust for typical inputs but please test thoroughly.
#     """

#     # Create single-row DataFrame from payload
#     df = pd.DataFrame([raw_payload])

#     # Normalizing column names
#     # Droping any Loan_ID if present
#     if "Loan_ID" in df.columns:
#         df = df.drop(columns=["Loan_ID"])

#     # Dependents handling: '3+' -> 3 and cast to numeric
#     if "Dependents" in df.columns:
#         df["Dependents"] = df["Dependents"].replace({"3+": "3"})
#         try:
#             df["Dependents"] = pd.to_numeric(df["Dependents"], errors="coerce")
#         except Exception:
#             pass

#     # Creating engineering features
#     if "Total_Income" not in df.columns:
#         app_inc = df.get("ApplicantIncome", pd.Series([0])).fillna(0).astype(float)
#         co_inc = df.get("CoapplicantIncome", pd.Series([0])).fillna(0).astype(float)
#         df["Total_Income"] = app_inc + co_inc

#     if "emi_estimate" not in df.columns:
#         # protecting division by zero or NaN
#         try:
#             df["emi_estimate"] = df["LoanAmount"].astype(float) / df["Loan_Amount_Term"].astype(float)
#         except Exception:
#             df["emi_estimate"] = np.nan

#     if "income_to_loan_ratio" not in df.columns:
#         # adding 1 to denominator to avoid divide-by-zero
#         df["income_to_loan_ratio"] = df["Total_Income"].astype(float) / (df["LoanAmount"].fillna(0).astype(float) + 1)

#     if "income_per_dependent" not in df.columns:
#         df["income_per_dependent"] = df["Total_Income"].astype(float) / (1 + df["Dependents"].fillna(0).astype(float))

#     # Creating missing flags for fields that are missing in payload and were flagged in training
#     # Setting flag = 1 if value is null/NaN in incoming payload
#     for col in expected_features:
#         if col.endswith("_missing_flag"):
#             raw_col = col.replace("_missing_flag", "")
#             df[col] = df.get(raw_col).isna().astype(int)

#     # Ensuring all original categorical columns exist (so imputer can run)
#     # Inferring categorical columns from label_encoders keys and columns found in expected_features that are string (dummies)
#     # For simplicity, adding any missing columns with NaN to be imputed/encoded later
#     for col in expected_features:
#         if col not in df.columns:
#             df[col] = np.nan

#     # Reorder columns to a deterministic order for imputation (but imputer expects numeric arrays)
#     # To perform imputation needed to separate numeric and categorical columns
#     # Following the logic used earlier: numeric dtype for numerical transformations
#     # Numeric columns are those currently parseable as float (except missing flags)
#     numeric_mask = []
#     for col in df.columns:
#         if col.endswith("_missing_flag"):
#             numeric_mask.append(False) # treat flags as non-numeric for imputer step (they are already 0/1)
#         else:
#             # Attempting to coerce to numeric
#             try:
#                 pd.to_numeric(df[col], errors="raise")
#                 numeric_mask.append(True)
#             except Exception:
#                 numeric_mask.append(False)

#     # Relying on the saved imputers: first apply cat_imputer on object columns then num_imputer
#     # Identifying categorical cols (objects, or those not numeric_mask)
#     cat_cols = [c for c, isnum in zip(df.columns, numeric_mask) if not isnum and not c.endswith("_missing_flag")]
#     num_cols = [c for c, isnum in zip(df.columns, numeric_mask) if isnum]

#     # Applying categorical imputer (if exists)
#     if cat_imputer is not None and len(cat_cols) > 0:
#         try:
#             df_cat = pd.DataFrame(cat_imputer.transform(df[cat_cols]), columns=cat_cols)
#             df[cat_cols] = df_cat
#         except Exception:
#             # cat_imputer might be fitted to a subset; fall back to fillna with 'Missing'
#             df[cat_cols] = df[cat_cols].fillna("Missing")

#     else:
#         df[cat_cols] = df[cat_cols].fillna("Missing")

#     # Applying numeric imputer
#     if num_imputer is not None and len(num_cols) > 0:
#         try:
#             df_num = pd.DataFrame(num_imputer.transform(df[num_cols]), columns=num_cols)
#             df[num_cols] = df_num
#         except Exception:
#             df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce").fillna(0)

#     else:
#         df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce").fillna(0)

#     # Applying label encoders for binary columns
#     for col, le in label_encoders.items():
#         if col in df.columns:
#             # Converting to str to match training encoders
#             df[col] = df[col].astype(str)
#             try:
#                 df[col] = le.transform(df[col])
#             except Exception:
#                 # If unseen label, mapping to most frequent class (0/1 fallback)
#                 # Attempting to inverse_transform first unique, else fill 0
#                 try:
#                     df[col] = df[col].map(lambda x: le.transform([x])[0])
#                 except Exception:
#                     df[col] = 0

#     # One-hot encoding: assuming model expects dummy columns found in expected_features that are not yet present
#     # Creating dummies for any categorical columns present in df
#     dummies = pd.get_dummies(df.drop(columns=[c for c in df.columns if c.endswith("_missing_flag") or c in num_cols]), drop_first=False)
#     # Combine numeric, flags, and dummies
#     final_df = pd.concat([df[num_cols + [c for c in df.columns if c.endswith("_missing_flag")]], dummies], axis=1)

#     # Aligning with expected_features: adding any missing columns with 0, and drop extras
#     for col in expected_features:
#         if col not in final_df.columns:
#             final_df[col] = 0.0

#     # Dropping any columns not in expected_features
#     final_df = final_df[expected_features]

#     # Applying scaling if scaler available
#     if scaler is not None:
#         try:
#             final_df[expected_features] = scaler.transform(final_df[expected_features])
#         except Exception:
#             # If scaler expects fewer/more columns, attempting to transform numerical columns only
#             try:
#                 final_df = final_df.astype(float)
#                 final_df[expected_features] = scaler.transform(final_df[expected_features])
#             except Exception:
#                 pass

#     return final_df

# # -------- Prediction endpoint --------
# @app.post("/predict")
# def predict(payload: LoanRequest):
#     """
#     Receives raw JSON representing one applicant (original fields like ApplicantIncome, LoanAmount, etc.).
#     Returns predicted probability and class label (0 = not approved, 1 = approved).
#     """
#     try:
#         raw = payload.dict()
#         # Preprocess input to final feature vector
#         X = replicate_preprocessing(raw)
#         # Predict
#         proba = model.predict_proba(X)[:, 1][0]
#         pred = int(model.predict(X)[0])
#         return {
#             "prediction": pred,
#             "probability": float(proba),
#             "model": os.path.basename(MODEL_PATH)
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

# # -------- Health endpoint --------
# @app.get("/health")
# def health():
#     return {"status": "ok", "model_loaded": bool(model is not None)}

# # -------- Run server (optional) --------
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

# from fastapi import FastAPI
# import joblib
# import pandas as pd
# import numpy as np
# from schemas import LoanRequest

# # Loading model and scaler from the 'model' folder
# model = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_best_model.joblib")
# scaler = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\scaler.joblib")
# num_imputer = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\num_imputer.joblib")
# cat_imputer = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\cat_imputer.joblib")
# label_encoders = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\label_encoders.joblib")

# app = FastAPI(title="Loan Prediction API")

# @app.post("/predict")
# def predict_loan(data: LoanRequest):
#     # Converting input to DataFrame
#     input_df = pd.DataFrame([data.dict()])

#     # Identifying categorical and numerical columns
#     cat_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
#     num_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']

#     # Imputing missing values
#     input_df[num_cols] = num_imputer.transform(input_df[num_cols])
#     input_df[cat_cols] = cat_imputer.transform(input_df[cat_cols])

#     # Encoding categorical columns using label encoders
#     for col in cat_cols:
#         input_df[col] = label_encoders[col].transform(input_df[col])

#     # Applying scaling to numerical columns
#     input_df[num_cols] = scaler.transform(input_df[num_cols])

#     # Predicting
#     prediction = model.predict(input_df)[0]
#     probability = model.predict_proba(input_df)[0][1]

#     return {
#         "prediction": int(prediction),
#         "probability": round(float(probability), 3)
#     }


# import joblib
# from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas as pd
# from schemas import LoanRequest

# app = FastAPI(title="Loan Prediction API")

# # loading full pipeline
# pipeline = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_pipeline.joblib")
# model = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_best_model.joblib")

# @app.post("/predict")
# def predict(request: LoanRequest):
#     df = pd.DataFrame([request.dict()])
#     pred = pipeline.predict(df)[0]
#     prob = pipeline.predict_proba(df)[0][1]
#     return {"prediction": int(pred), "probability": round(float(prob), 3)}

# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
# import pandas as pd
# from .schemas import LoanRequest

# # Load the full pipeline (preprocessor + model)
# pipeline = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_pipeline.joblib")

# # Define the API app
# app = FastAPI(title="Loan Approval Prediction API")

# @app.post("/predict")
# def predict_loan(data: LoanRequest):
#     # Convert to DataFrame
#     df = pd.DataFrame([data.dict()])

#     # Use the pipeline directly for prediction
#     prediction = pipeline.predict(df)[0]
#     probability = pipeline.predict_proba(df)[0][1]

#     result = "Approved" if prediction == 1 else "Rejected"
#     return {
#         "Loan_Status": result,
#         "Approval_Probability": round(float(probability), 4)
#     }

# from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas as pd
# import joblib
# from .schemas import LoanRequest

# app = FastAPI(title="Loan Approval Prediction API")

# # Loading saved artifacts
# artifacts = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\preprocessing_artifacts.joblib")
# model = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_best_model.joblib")

# num_imputer = artifacts["num_imputer"]
# cat_imputer = artifacts["cat_imputer"]
# scaler = artifacts["scaler"]
# label_encoders = artifacts["label_encoders"]


# # Preprocessing Function
# def preprocess_input(input_data: pd.DataFrame):
#     df = input_data.copy()

#     # Label encoding
#     for col, le in label_encoders.items():
#         if col in df.columns:
#             df[col] = le.transform(df[col])

#     # Numeric and categorical column separation
#     num_cols = df.select_dtypes(include=["int64", "float64"]).columns
#     cat_cols = df.select_dtypes(include=["object"]).columns

#     # Impute and scale
#     if len(num_cols) > 0:
#         df[num_cols] = num_imputer.transform(df[num_cols])
#         df[num_cols] = scaler.transform(df[num_cols])
#     if len(cat_cols) > 0:
#         df[cat_cols] = cat_imputer.transform(df[cat_cols])

#     return df

# # Predict Function
# def predict_from_input(df: pd.DataFrame):
#     X_processed = preprocess_input(df)
#     pred = model.predict(X_processed)[0]
#     prob = model.predict_proba(X_processed)[0, 1]
#     return int(pred), float(prob)

# # API Endpoint
# @app.post("/predict")
# def predict_loan(data: LoanRequest):
#     input_df = pd.DataFrame([data.dict()])
#     pred, prob = predict_from_input(input_df)
#     return {"prediction": pred, "probability": prob}

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from schemas import LoanRequest

app = FastAPI(title="Loan Approval Prediction API")

# Load the trained pipeline (already includes preprocessing + model)
pipeline = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_pipeline_fitted.joblib")

@app.post("/predict")
def predict_loan(data: LoanRequest):
    # Convert input to DataFrame
    df = pd.DataFrame([data.dict()])
    
    # Predict using the pipeline (no manual preprocessing needed)
    prediction = pipeline.predict(df)[0]
    probability = pipeline.predict_proba(df)[0, 1]
    
    return {"prediction": prediction, "probability": float(probability)}