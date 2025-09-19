import pandas as pd
data = {
    'outlook': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy',
                'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
    'temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool',
                    'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'humidity': ['high', 'high', 'high', 'high', 'normal', 'normal',
                 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'windy': [False, True, False, False, False, True,
              True, False, False, False, True, True, False, True],
    'play': ['no', 'no', 'yes', 'yes', 'yes', 'no',
             'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

df=pd.DataFrame(data)
print("\n===Head(First 5 rows)===\n")
print(df.head())
print("\n===Tail(Last 5 rows)===\n",df.tail())
print("\nDimensions")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[0]}")
print("\ncoloumn:",df.columns.tolist())
print("\n===Datasets.tolist===")
print(df.info())
print("\n Missing values")
print(df.isnull().sum())
print("\nStatistical information")
print(df.describe(include='all'))