import pandas as pd

data = {
    'date': ['2024-06-01', '2023-12-15', '2025-01-10']
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_name'] = df['date'].dt.day_name()
df['month_name'] = df['date'].dt.month_name()
df['is_future'] = df['date'] > pd.Timestamp.today()
df['plus_7_days'] = df['date'] + pd.Timedelta(days=7)

print(df)
