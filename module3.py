# Data Cleaning

import pandas as pd

df = pd.read_csv("student_dataset_v2.csv")

# 1. Remove Duplicate Records
df = df.drop_duplicates()

# 2. Handle Missing Values
df = df.dropna()

# 3. Remove Invalid Entries
# Remove rows where Name or Branch is empty
df = df[df["Name"].str.strip() != ""]


# 4. Validate Attendance
df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]


# 5. Validate Study Hours
df = df[(df["StudyHours"] >= 0) & (df["StudyHours"] <= 24)]

# 6. Validate Marks
f = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]


# Save Cleaned Dataset
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned successfully!")
print("Cleaned dataset saved as 'cleaned_data.csv'.")
