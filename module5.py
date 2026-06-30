# Data Filtering

# Generating saparate Datasets for:

import pandas as pd

# Read the dataset
df = pd.read_csv("student_performance.csv")

# 1. Top-Performing Students
# (Marks >= 90 or Grade = A)
top_students = df[df["Marks"] >= 90]

# 2. Failed Students
failed_students = df[df["Result"] == "Fail"]

# 3. Students with Attendance Below 75%
low_attendance = df[df["Attendance"] < 75]

# 4. Students Studying More Than 8 Hours
high_study_hours = df[df["StudyHours"] > 8]

# Save Each Dataset as CSV
top_students.to_csv("top_performing_students.csv", index=False)
failed_students.to_csv("failed_students.csv", index=False)
low_attendance.to_csv("low_attendance_students.csv", index=False)
high_study_hours.to_csv("high_study_hours_students.csv", index=False)


# Display Number of Records
print("Top-Performing Students:", len(top_students))
print("Failed Students:", len(failed_students))
print("Students with Attendance Below 75%:", len(low_attendance))
print("Students Studying More Than 8 Hours:", len(high_study_hours))

print("\nAll filtered datasets have been saved successfully.")