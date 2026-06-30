#Data Loading

import pandas as pd

# Read the CSV file
df = pd.read_csv("student_dataset_v2.csv")   

# Display the first five records
print("First Five Records:")
print(df.head())

# Display the last five records
print("\nLast Five Records:")
print(df.tail())

# Print the shape of the dataset
print("\nShape of Dataset:")
print(df.shape)

# Print column names
print("\nColumn Names:")
print(df.columns)

# Display data types of each column
print("\nData Types of Each Column:")
print(df.dtypes)