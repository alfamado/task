# import joblib
# from pathlib import Path

# # Loading the preprocessing artifacts
# proc_artifacts = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\preprocessing_artifacts.joblib")

# # Creating output directory (same as model folder)
# model_dir = Path(r"C:\Users\NCC200\Desktop\TASK\loan_api\model")

# # Extracting and saving each component individually
# joblib.dump(proc_artifacts['scaler'], model_dir / "scaler.joblib")
# joblib.dump(proc_artifacts['num_imputer'], model_dir / "num_imputer.joblib")
# joblib.dump(proc_artifacts['cat_imputer'], model_dir / "cat_imputer.joblib")
# joblib.dump(proc_artifacts['label_encoders'], model_dir / "label_encoders.joblib")

# print("Individual preprocessing artifacts saved successfully.")

import joblib
from sklearn.pipeline import Pipeline

# loading components
preprocessors = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\preprocessing_artifacts.joblib")
model = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_best_model.joblib")

# building pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# (assuming num/cat columns are known from training)
numeric_features = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
categorical_features = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

full_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                ('model', model)])

# save combined pipeline
joblib.dump(full_pipeline, r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_pipeline.joblib")