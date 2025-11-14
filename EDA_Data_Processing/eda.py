# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Set a style for plots
sns.set_style("whitegrid")

# 1. Load the dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
try:
    df = pd.read_csv('your_dataset.csv')
except FileNotFoundError:
    print("Error: Dataset file not found. Please check the path.")
    exit()

# 2. Initial Data Inspection
print("--- Initial Data Inspection ---")
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset information:")
df.info()
print("\nDescriptive statistics:")
print(df.describe())
print("\nShape of the dataset (rows, columns):", df.shape)
print("\nColumn names:", df.columns)

# 3. Handling Missing Values
print("\n--- Missing Values Analysis ---")
print("Missing values per column:")
print(df.isnull().sum())

# Example: Impute missing values in a numeric column with the mean
# df['numeric_column'].fillna(df['numeric_column'].mean(), inplace=True)
# Example: Drop rows with any missing values
# df.dropna(inplace=True)

# 4. Explore Data Characteristics (Data Types, Unique Values)
print("\n--- Data Characteristics ---")
print("Data types of columns:")
print(df.dtypes)
print("\nUnique values and their counts for a categorical column (example 'category_column'):")
# Replace 'category_column' with an actual categorical column in your dataset
# if 'category_column' in df.columns:
#     print(df['category_column'].value_counts())
# else:
#     print("Categorical column 'category_column' not found.")

# 5. Data Visualization
print("\n--- Data Visualization ---")
# Example: Histogram for a numeric column
# if 'numeric_column' in df.columns:
#     plt.figure(figsize=(8, 6))
#     sns.histplot(df['numeric_column'], kde=True)
#     plt.title('Distribution of Numeric Column')
#     plt.xlabel('Numeric Column')
#     plt.ylabel('Frequency')
#     plt.show()
# else:
#     print("Numeric column 'numeric_column' not found for histogram.")

# Example: Box plot for a numeric column to visualize outliers
# if 'numeric_column' in df.columns:
#     plt.figure(figsize=(8, 6))
#     sns.boxplot(y=df['numeric_column'])
#     plt.title('Box Plot of Numeric Column')
#     plt.ylabel('Numeric Column')
#     plt.show()
# else:
#     print("Numeric column 'numeric_column' not found for box plot.")

# Example: Correlation heatmap for numerical features
numeric_df = df.select_dtypes(include=np.number)
if not numeric_df.empty:
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Numeric Features')
    plt.show()
else:
    print("No numeric columns found for correlation heatmap.")

# 6. Outlier Detection (Example using Z-score for a numeric column)
# from scipy import stats
# if 'numeric_column' in df.columns:
#     z_scores = np.abs(stats.zscore(df['numeric_column'].dropna()))
#     outliers = df[z_scores > 3]
#     print("\nOutliers in 'numeric_column' (Z-score > 3):")
#     print(outliers)
# else:
#     print("Numeric column 'numeric_column' not found for outlier detection.")