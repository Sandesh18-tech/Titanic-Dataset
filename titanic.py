import pandas as pd
import os

file_path = r"C:\Users\YourName\Downloads\titanic.csv"

if os.path.exists(file_path):
    titanic = pd.read_csv(file_path)

    print("Titanic Dataset:")
    print(titanic)

    print("\nFirst 5 Rows:")
    print(titanic.head())

    print("\nDataset Information:")
    print(titanic.info())
else:
    print("Titanic dataset not found!")
