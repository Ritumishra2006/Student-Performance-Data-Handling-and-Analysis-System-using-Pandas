# Sorting

#Display

import pandas as pd

# Read the dataset
df = pd.read_csv("student_performance.csv")

# Sort Students by Marks (Highest to Lowest)
marks_sorted = df.sort_values(by="Marks", ascending=False)

# Sort Students by Attendance (Highest to Lowest)
attendance_sorted = df.sort_values(by="Attendance", ascending=False)

# Sort Students by Study Hours (Highest to Lowest)
study_hours_sorted = df.sort_values(by="StudyHours", ascending=False)


# Display Sorted Data
print("Students Sorted by Marks")
print(marks_sorted)

print("\nStudents Sorted by Attendance")
print(attendance_sorted)

print("\nStudents Sorted by StudyHours")
print(study_hours_sorted)

# Save Sorted Datasets as CSV Files
marks_sorted.to_csv("students_sorted_by_marks.csv", index=False)
attendance_sorted.to_csv("students_sorted_by_attendance.csv", index=False)
study_hours_sorted.to_csv("students_sorted_by_studyhours.csv", index=False)

print("\nSorted datasets saved successfully.")