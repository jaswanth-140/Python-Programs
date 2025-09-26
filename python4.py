import pandas as pd

df = pd.read_csv('C:/Users/jashw/Desktop/PYTHON PROGRAMS/temperature.csv')
print("Original Data:")
print(df.head())

df['date'] = pd.to_datetime(df['date'])
df['temperature_celsius'] = df['temperature_celsius'].fillna(df['temperature_celsius'].mean())
df['temperature_fahrenheit'] = df['temperature_celsius'] * 9 / 5 + 32
df['temp_7day_avg'] = df['temperature_celsius'].rolling(window=7).mean()

temp_min = df['temperature_celsius'].min()
temp_max = df['temperature_celsius'].max()
df['temperature_normalized'] = (df['temperature_celsius'] - temp_min) / (temp_max - temp_min)

print("\nTransformed Data:")
print(df.head(10))

df.to_csv('C:/Users/jashw/Desktop/PYTHON PROGRAMS/temperature.csv', index=False)