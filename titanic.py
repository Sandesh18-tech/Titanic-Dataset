import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic-Dataset.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nShape of Dataset:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nSurvival Count:")
print(df['Survived'].value_counts())

print("\nGender Count:")
print(df['Sex'].value_counts())

print("\nPassenger Class:")
print(df['Pclass'].value_counts())

print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

plt.hist(df['Age'].dropna(), bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.hist(df['Fare'], bins=20)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

plt.boxplot(df['Age'].dropna())
plt.title("Age Boxplot")
plt.show()

print(pd.crosstab(df['Sex'], df['Survived']))
