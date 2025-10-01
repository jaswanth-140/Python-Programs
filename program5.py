import pandas as pd

file_path = "C:/Users/jashw/Desktop/PYTHON PROGRAMS/temperature.csv"
df = pd.read_csv(file_path)
print("Original Data:")
print(df.head())

df = df.drop_duplicates()
df = df.dropna()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

print("\nCleaned Data:")
print(df.head())

df_sorted = df.sort_values(by=df.columns[1])

print("\nSorted Data:")
print(df_sorted.head())

df_agg = df.groupby(df.columns[0]).mean(numeric_only=True)

print("\nAggregated Data:")
print(df_agg.head())

df_sorted.to_csv("sorted_output.csv", index=False)
df_agg.to_csv("aggregated_output.csv")
