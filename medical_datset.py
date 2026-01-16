import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("medical_data.csv")

print("Initial Shape:", df.shape)

# Check missing values
missing = df.isnull().sum()
print("\nMissing Values:\n", missing)

# Visualize missing values
missing[missing > 0].plot(kind='bar')
plt.title("Missing Values Count")
plt.show()

# Numerical columns
num_cols = df.select_dtypes(include=np.number).columns

# Categorical columns
cat_cols = df.select_dtypes(include='object').columns

# Fill numerical columns with median
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with mode
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Drop columns with more than 50% missing values
threshold = len(df) * 0.5
df = df.dropna(axis=1, thresh=threshold)

print("\nFinal Shape:", df.shape)

# Save cleaned dataset
df.to_csv("cleaned_medical_data.csv", index=False)

print("Data cleaning completed. Cleaned file saved.")
