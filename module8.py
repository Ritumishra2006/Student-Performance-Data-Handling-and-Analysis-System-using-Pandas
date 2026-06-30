# Grouping 

#Using groupby(), Calculating :

import pandas as pd

# Read the dataset
df = pd.read_csv("student_performance.csv")

# Average Marks by Grade
avg_marks = df.groupby("Grade")["Marks"].mean()

# Number of Students in Each Grade
student_count = df.groupby("Grade")["Grade"].count()

# Average Attendance by Grade
avg_attendance = df.groupby("Grade")["Attendance"].mean()

# Display Results
print(" Average Marks by Grade ")
print(avg_marks)

print("\n Number of Students in Each Grade ")
print(student_count)

print("\n Average Attendance by Grade ")
print(avg_attendance)
