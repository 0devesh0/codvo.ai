import pandas as pd

df = pd.read_csv("C:\\Users\\deves\\Desktop\\uv\\data\\sales_data.csv")

print(df.head())

print("\nColumn Data Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic info
print("\nBasic Info:")
print(df.info())