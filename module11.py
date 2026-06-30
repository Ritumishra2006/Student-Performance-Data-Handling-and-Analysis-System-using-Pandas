# Export Data
#Project should generate the following output files:

import pandas as pd
import os

# Create Output Folder
os.makedirs("output", exist_ok=True)

# Read dataset
df = pd.read_csv("student_performance.csv")

# Clean Data
cleaned_data = df.drop_duplicates().dropna()
cleaned_data.to_csv("output/cleaned_data.csv", index=False)

# Top Performing Students (Toppers)
toppers = cleaned_data[cleaned_data["Marks"] >= 90]
toppers.to_csv("output/toppers.csv", index=False)

# Failed Students
failed_students = cleaned_data[cleaned_data["Result"] == "Fail"]
failed_students.to_csv("output/failed_students.csv", index=False)

# Generate Report
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
        len(cleaned_data),
        (cleaned_data["Result"] == "Pass").sum(),
        (cleaned_data["Result"] == "Fail").sum(),
        cleaned_data["Marks"].max(),
        cleaned_data["Marks"].min(),
        round(cleaned_data["Marks"].mean(), 2),
        round(cleaned_data["Attendance"].mean(), 2)
    ]
})

# Add Grade-wise Distribution
grade_distribution = cleaned_data["Grade"].value_counts()

for grade, count in grade_distribution.items():
    report.loc[len(report)] = [f"Grade {grade}", count]

# Save Report
report.to_csv("output/report.csv", index=False)

print("All files generated successfully!")
print("Files are saved inside the 'output' folder.")