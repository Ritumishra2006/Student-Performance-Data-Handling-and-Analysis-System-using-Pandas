import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Read dataset
df = pd.read_csv("student_performance.csv")

# Top 10 Students by Performance Score
top10 = df.sort_values(by="Performance_Score", ascending=False).head(10)

print("Top 10 Students Based on Performance Score")
print(top10[["Name", "Performance_Score"]])

# Bar Chart - Top 10 Students
plt.figure(figsize=(10,6))
plt.bar(top10["Name"], top10["Performance_Score"])
plt.title("Top 10 Students by Performance Score")
plt.xlabel("Student Name")
plt.ylabel("Performance Score")
plt.xticks(rotation=45)
plt.tight_layout()

# Save graph
plt.savefig("output/top10_performance.png")
plt.show()

# Grade Distribution Pie Chart
grade_count = df["Grade"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(grade_count,
        labels=grade_count.index,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Grade Distribution")
plt.savefig("output/grade_distribution.png")
plt.show()

# Marks Distribution Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Marks"], bins=10)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("output/marks_distribution.png")
plt.show()

print("\nGraphs saved successfully in the 'output' folder.")