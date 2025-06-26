import pandas as pd

df = pd.read_csv("custom.csv") 
print(df.head())
df = df.drop_duplicates()
df.columns = df.columns.str.strip().str.replace(' ', '_')
df['Subscription_Date'] = pd.to_datetime(df['Subscription_Date'], errors='coerce')
print("Missing values in each column:")
print(df.isnull().sum())


