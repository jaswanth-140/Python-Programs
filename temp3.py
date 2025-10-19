import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
print("\nFirst 5 rows of dataset: ")
print(df.head())

print("Last 5 rows of dataset: ")
print(df.tail())

print("Summary statistics: ")
print(df.describe())

print("Missing values in dataset: ")
print(df.isnull().sum())

