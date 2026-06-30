# Data Analysis

#performing the analysis :

import pandas as pd

# Read the dataset
df = pd.read_csv("student_performance.csv")

# Average Marks
average_marks = df["Marks"].mean()

# Highest Marks
highest_marks = df["Marks"].max()

# Lowest Marks
lowest_marks = df["Marks"].min()

# Average Attendance
average_attendance = df["Attendance"].mean()

# Average Study Hours
average_study_hours = df["StudyHours"].mean()

# Pass Percentage
pass_percentage = (df["Result"] == "Pass").mean() * 100

# Fail Percentage
fail_percentage = (df["Result"] == "Fail").mean() * 100

# Grade Distribution
grade_distribution = df["Grade"].value_counts()

# Display Results
print(" Student Performance Analysis ")

print(f"\nAverage Marks: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")

print(f"\nAverage Attendance: {average_attendance:.2f}%")
print(f"Average Study Hours: {average_study_hours:.2f} hours")

print(f"\nPass Percentage: {pass_percentage:.2f}%")
print(f"Fail Percentage: {fail_percentage:.2f}%")

print("\nGrade Distribution:")
print(grade_distribution)