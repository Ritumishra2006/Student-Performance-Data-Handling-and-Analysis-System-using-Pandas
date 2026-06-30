 #Data Transformation


 #Creating following new columns :

import pandas as pd

# Read the cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# Assign Grades

def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(assign_grade)

# Assign Result

def assign_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

df["Result"] = df["Marks"].apply(assign_result)


# Create Performance Score
# Formula:
# 70% Marks + 20% Attendance + 10% Study Hours
# (Study Hours assumed out of 10)

df["Performance_Score"] = (
    (df["Marks"] * 0.7) +
    (df["Attendance"] * 0.2) +
    (df["StudyHours"] * 10 * 0.1)
)

# Round to 2 decimal places
df["Performance_Score"] = df["Performance_Score"].round(2)

# Display the updated dataset
print(df)

# Save the updated dataset
df.to_csv("student_performance.csv", index=False)

print("\nStudent performance file saved as 'student_performance.csv'")