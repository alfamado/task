# import joblib

# # Load your pipeline
# pipeline = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_pipeline.joblib")

# # Check structure
# print("Pipeline Steps:\n", pipeline.named_steps)

# # If it contains a preprocessor, print the feature names it expects
# try:
#     preprocessor = pipeline.named_steps["preprocessor"]
#     print("\nFeature Names Seen at Fit Time:\n", preprocessor.get_feature_names_out())
# except Exception as e:
#     print("Could not extract feature names:", e)

import joblib
import pandas as pd

# Loading train data
train = pd.read_csv(r"C:\Users\NCC200\Desktop\TASK\EDA_Data_Processing\home_loan_train.csv")

# Separating features and target
X = train.drop("Loan_Status", axis=1)
y = train["Loan_Status"]

# Loading pipeline
pipeline = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_pipeline.joblib")

# Fit the pipeline on training data
pipeline.fit(X, y)

# Save the fitted pipeline
joblib.dump(pipeline, r"C:\Users\NCC200\Desktop\TASK\loan_api\model\loan_pipeline_fitted.joblib")

print("Fitted pipeline saved as loan_pipeline_fitted.joblib")