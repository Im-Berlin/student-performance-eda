import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("student-por.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nStatistical Summary:")
print(df.describe())

# ---------------------------------
# Grade Distribution
# ---------------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["G3"], bins=20)

plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade")
plt.ylabel("Frequency")

plt.savefig("Grade_Distribution.png")
plt.show()

# ---------------------------------
# Study Time vs Grade
# ---------------------------------

plt.figure(figsize=(8,5))
sns.boxplot(x="studytime", y="G3", data=df)

plt.title("Study Time vs Final Grade")

plt.savefig("Studytime_vs_Grade.png")
plt.show()

# ---------------------------------
# Absences vs Grade
# ---------------------------------

plt.figure(figsize=(8,5))
sns.scatterplot(
    x="absences",
    y="G3",
    data=df
)

plt.title("Absences vs Final Grade")

plt.savefig("Absences_vs_Grade.png")
plt.show()

# ---------------------------------
# Gender vs Grade
# ---------------------------------

plt.figure(figsize=(8,5))
sns.barplot(
    x="sex",
    y="G3",
    data=df
)

plt.title("Gender vs Final Grade")

plt.savefig("Gender_vs_Grade.png")
plt.show()

# ---------------------------------
# Correlation Heatmap
# ---------------------------------

numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(12,8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig("Correlation_Heatmap.png")
plt.show()

print("\nEDA Completed Successfully")