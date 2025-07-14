import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    df = pd.read_excel("marks.csv.xlsx")  # Make sure the file exists
except FileNotFoundError:
    print("File not found")
    exit()

# Data cleaning
df = df[df["marks"] < 100]  # Filter invalid marks
df['marks'] = df['marks'].fillna(0)  # Fill NaN with 0
df['student'] = df['student'].fillna("NONE")  # Fill missing names

# Style settings
sns.set_style('whitegrid')
plt.rcParams.update({'font.size': 15, 'figure.autolayout': True})
title_font = {'family': 'arial', 'color': 'gray', 'size': 20, 'weight': 'bold'}
label_font = {'family': 'arial', 'color': 'gray', 'size': 13}

# Plot 1: Bar plot (All students)
plt.figure(figsize=(10, 6))
# Fixed palette warning by adding hue and legend=False
sns.barplot(x='student', y='marks', data=df, hue='student', palette='Set2', 
            edgecolor='blue', legend=False)
plt.title("Student Marks", fontdict=title_font)
plt.ylabel("Marks", fontdict=label_font)
plt.xlabel("Student", fontdict=label_font)
plt.xticks(rotation=45)
plt.tight_layout()  # Helps with margin warnings
plt.show()

# Plot 2: Line plot (Top students)
top = 5
top_stud = df.sort_values('marks', ascending=False).head(top)  # Get top 5 students

# Fixed figure size syntax - was plt.figure(12,6)
plt.figure(figsize=(12, 6))  
# Corrected to sns.lineplot (was plt.lineplot)
sns.lineplot(data=top_stud, x='student', y='marks', marker='o', 
             linewidth=3, color='purple')
plt.title("Top 5 Students", fontdict=title_font)
plt.xlabel("Student Name", fontdict=label_font)
plt.ylabel("Marks", fontdict=label_font)
plt.xticks(rotation=30, ha='right')
plt.grid(True, linestyle='--', alpha=1)

# Add value labels
for x, y in zip(top_stud['student'], top_stud['marks']):
    plt.text(x, y + 1, f"{y}", ha='center', fontsize=10)

plt.tight_layout()
plt.show()
#average students
class_avg=df['marks'].mean()
plt.figure(figsize=(12,7))
sns.barplot(x='student', y='marks', data=df, hue='student', palette='viridis',legend=False)
plt.axhline(y=class_avg, color='red', linestyle='--', linewidth=2)
plt.text(x=0.5, y=class_avg+2, 
        s=f'Class Average: {class_avg:.1f}', 
        color='red', fontweight='bold')
plt.title("Average marks", fontdict=title_font)
plt.xlabel("Student Name", fontdict=label_font)
plt.ylabel("Marks", fontdict=label_font)
plt.tight_layout()
plt.show()
avg=df['marks'].mean()
print(f"{avg} IS THE MEAN OF THE MARKS OF THE STUDENTS ")
med=df['marks'].median()
print(f"{med} IS THE MEDIAN OF THE MARKS OF THE STUDENTS ")
mod=df['marks'].mode()
print(f"{mod} IS THE MODE OF THE MARKS OF THE STUDENTS ")
standard=df['marks'].std()
print(f"{standard} IS THE STANDARD DEVIATION OF THE MARKS OF THE STUDENTS ")
deviation=df['marks'].var()
print(f"{deviation} IS THE VARIANCE OF THE MARKS OF THE STUDENTS ")