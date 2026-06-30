# Statistical Analysis

#Computing :

import pandas as pd

# Read the dataset
df = pd.read_csv("student_performance.csv")

# Select only numerical columns
numeric_df = df.select_dtypes(include=['number'])

# Mean
print(" Mean ")
print(numeric_df.mean())

# Median
print("\n Median ")
print(numeric_df.median())

# Mode
print("\n Mode ")
print(numeric_df.mode())

# Standard Deviation
print("\n Standard Deviation ")
print(numeric_df.std())

# Variance
print("\n Variance ")
print(numeric_df.var())

# Correlation Matrix
print("\n Correlation Matrix ")
print(numeric_df.corr())