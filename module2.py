# Data Inspection

import pandas as pd

# Read the CSV file
df = pd.read_csv("student_dataset_v2.csv")

# 1. Find missing values
print("Missing Values:")
print(df.isnull().sum())

# 2. Find duplicate records
print("\nDuplicate Records:")
print(df.duplicated())

# Number of duplicate records
print("\nTotal Duplicate Records:")
print(df.duplicated().sum())

# Display duplicate rows (if any)
print("\nDuplicate Rows:")
print(df[df.duplicated()])

# 3. Display descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 4. Check memory usage
print("\nMemory Usage:")
print(df.memory_usage())

# Total memory used
print("\nTotal Memory Used:")
print(df.memory_usage(deep=True).sum(), "bytes")

# 5. Display summary information
print("\nSummary Information:")
df.info()