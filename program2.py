import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, None, 30, 22, 28],
    'Salary': [50000, 60000, None, 52000, 58000],
    'Department': ['HR', 'IT', 'IT', None, 'Finance']
}

df = pd.DataFrame(data).replace({None: np.nan})
print(df.head())
print("Missing values:\n", df.isnull().sum())
num_imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = num_imputer.fit_transform(df[['Age', 'Salary']])
cat_imputer = SimpleImputer(strategy='most_frequent')
df[['Name', 'Department']] = cat_imputer.fit_transform(df[['Name', 'Department']])
print("\nImputed DataFrame:\n", df)