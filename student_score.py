import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
try:
    df=pd.read_excel("student_score.xlsx")
except FileNotFoundError:
    print("File not found")
#data cleaning

df['english']=df['english'].fillna(0)
df['sst']=df['sst'].fillna(0)
df['maths']=df['maths'].fillna(0)
df['science']=df['science'].fillna(0)
df['student']=df['student'].fillna("none")

# Style settings     bar graph     line     box plt       histogram
sns.set_style('whitegrid')
plt.rcParams.update({'font.size': 15, 'figure.autolayout': True})
title_font = {'family': 'arial', 'color': 'gray', 'size': 20, 'weight': 'bold'}
label_font = {'family': 'arial', 'color': 'gray', 'size': 13}


max_math=sum(df['maths'])
max_eng=sum(df['english'])
max_sst=sum(df['sst'])
max_science=sum(df['science'])
lis=[max_sst,max_eng,max_math,max_science]
all=list(lis)
print(f"{min(all)} is the minimum of all subjects and maximum for all subjects is {max(all)}")
avg=df['maths'].mean()
print(f"{avg} IS THE MEAN OF THE Maths OF THE STUDENTS ")
med=df['maths'].median()
print(f"{med} IS THE MEDIAN OF THE MARKS OF THE STUDENTS ")
mod=df['maths'].mode()
print(f"{mod} IS THE MODE OF THE MARKS OF THE STUDENTS ")
standard=df['maths'].std()
print(f"{standard} IS THE STANDARD DEVIATION OF THE MARKS OF THE STUDENTS ")
deviation=df['maths'].var()
print(f"{deviation} IS THE VARIANCE OF THE MARKS OF THE STUDENTS ")
#sceince
avg1=df['science'].mean()
print(f"{avg1} IS THE MEAN OF THE Maths OF THE STUDENTS ")
med1=df['science'].median()
print(f"{med1} IS THE MEDIAN OF THE MARKS OF THE STUDENTS ")
mod1=df['science'].mode()
print(f"{mod1} IS THE MODE OF THE MARKS OF THE STUDENTS ")
standard1=df['science'].std()
print(f"{standard1} IS THE STANDARD DEVIATION OF THE MARKS OF THE STUDENTS ")
deviation1=df['science'].var()
print(f"{deviation1} IS THE VARIANCE OF THE MARKS OF THE STUDENTS ")
#sst
avg2=df['sst'].mean()
print(f"{avg2} IS THE MEAN OF THE sst OF THE STUDENTS ")
med2=df['sst'].median()
print(f"{med2} IS THE MEDIAN OF THE sst OF THE STUDENTS ")
mod2=df['sst'].mode()
print(f"{mod2} IS THE MODE OF THE sst OF THE STUDENTS ")
standard2=df['sst'].std()
print(f"{standard2} IS THE STANDARD DEVIATION OF THE sst OF THE STUDENTS ")
deviation2=df['sst'].var()
print(f"{deviation2} IS THE VARIANCE OF THE sst OF THE STUDENTS ")
#english
avg3=df['english'].mean()
print(f"{avg3} IS THE MEAN OF THE english OF THE STUDENTS ")
med3=df['english'].median()
print(f"{med3} IS THE MEDIAN OF THE english OF THE STUDENTS ")
mod3=df['english'].mode()
print(f"{mod3} IS THE MODE OF THE english OF THE STUDENTS ")
standard3=df['english'].std()
print(f"{standard3} IS THE STANDARD DEVIATION OF THE english OF THE STUDENTS ")
deviation3=df['english'].var()
print(f"{deviation3} IS THE VARIANCE OF THE english OF THE STUDENTS ")



df['total_marks'] = df['english'] + df['sst'] + df['maths'] + df['science']
print("\nAll Students' Total Marks:")
print(df[['student', 'total_marks']])
df['avg_marks'] = (df['english'] + df['sst'] + df['maths'] + df['science'])/4
print("\nAll Students' Average Marks:")
print(df[['student', 'avg_marks']])
subjects = ['english', 'sst', 'maths', 'science']
for subject in subjects:
    top_student = df.loc[df[subject].idxmax()]
    print(f"\nHighest in {subject.upper()}:")
    print(f"Student: {top_student['student']}")
    print(f"Marks: {top_student[subject]}")
#Bar chart: Total marks of each student
plt.figure(figsize=(12,6))
sns.barplot(x='student',y='total_marks',data=df,hue='student',palette='viridis',legend=False)
plt.title('Total Marks of Each Student',fontdict=title_font)
plt.ylabel('total_marks',fontdict=label_font)
plt.xlabel('student',fontdict=label_font)
plt.tight_layout()
plt.show()
#Line chart: Subject-wise average marks
averages = df[['english', 'sst', 'maths', 'science']].mean()

# Create line graph
plt.figure(figsize=(10, 6))
averages.plot(kind='line', marker='o', markersize=8, 
             color=['blue', 'green', 'red', 'purple'], 
             linewidth=2)
plt.title("Subject-Wise Average Marks", fontdict=title_font)
plt.xlabel("Subjects", fontdict=label_font)
plt.ylabel("Average Marks", fontdict=label_font)
plt.ylim(0, 100)  # Assuming max marks are 100
plt.grid(True, linestyle='--', alpha=0.5)
for x, y in enumerate(averages):
    plt.text(x, y+2, f'{y:.1f}', ha='center', fontsize=12)
plt.tight_layout()
plt.show()
#Boxplot: Spread of marks per subject
# Melt the dataframe for better plotting
melted_df = pd.melt(df, id_vars=['student'], 
                    value_vars=['english', 'sst', 'maths', 'science'],
                    var_name='Subject', value_name='Marks')

# Create boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Subject', y='Marks', data=melted_df, palette='pastel')

plt.ylabel('marks',fontdict=label_font)
plt.xlabel('student',fontdict=label_font)
plt.tight_layout()
plt.show()
#Histogram: Frequency distribution of marks
plt.figure(figsize=(10, 6))
sns.histplot(data=df[['english', 'sst', 'maths', 'science']], 
             bins=20, 
             kde=True,  # Adds a smoothed line
             palette='viridis', 
             alpha=0.6)  # Makes slightly transparent

# Add titles and labels
plt.title('Frequency Distribution of Marks Across Subjects', fontsize=15, pad=20)
plt.xlabel('Marks', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.legend(title='Subject', labels=['English', 'SST', 'Maths', 'Science'])

# Show plot
plt.tight_layout()
plt.show()