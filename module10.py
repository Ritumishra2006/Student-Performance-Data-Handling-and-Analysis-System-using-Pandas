# Report Generation

#Generating a final report containing :

import pandas as pd

# Read the dataset
df = pd.read_csv("student_performance.csv")


# Calculate Report Values
total_students = len(df)
passed_students = (df["Result"] == "Pass").sum()
failed_students = (df["Result"] == "Fail").sum()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()
average_marks = df["Marks"].mean()
average_attendance = df["Attendance"].mean()

# Grade-wise Distribution
grade_distribution = df["Grade"].value_counts()

# Create Report DataFrame
report = pd.DataFrame({
    "Metric": [
        "Total Students",
        "Passed Students",
        "Failed Students",
        "Highest Marks",
        "Lowest Marks",
        "Average Marks",
        "Average Attendance"
    ],
    "Value": [
        total_students,
        passed_students,
        failed_students,
        highest_marks,
        lowest_marks,
        round(average_marks, 2),
        round(average_attendance, 2)
    ]
})
# Save report
report.to_csv("report.csv", index=False)

# Display report
print(" Student Report ")
print(report)

# Display Grade-wise Distribution
print("\n Grade-wise Distribution ")
print(grade_distribution)

# (Optional) Save Grade Distribution separately
grade_distribution.to_csv("grade_distribution.csv", header=["Number_of_Students"])

print("\nReport saved as 'report.csv'")