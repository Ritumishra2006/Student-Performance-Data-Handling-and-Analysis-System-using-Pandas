import pandas as pd

# 1. Ingest (Load Data)

df = pd.read_csv("student_dataset_v2.csv")   

print("First 10 Rows:")
print(df.head(10))

print("\nLast 5 Rows:")
print(df.tail(5))

# 2. Understand Data

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# 3. Data Cleaning

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values in Marks column with mean

marks_mean = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(marks_mean)

print("\nMissing Values After Filling:")
print(df.isnull().sum())

# 4. Basic Analysis

print("\nHighest Attendance:")
print(df["Attendance"].max())

print("\nAverage Study Hours:")
print(df["StudyHours"].mean())