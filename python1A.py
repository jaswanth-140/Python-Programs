#"How can you create a DataFrame from a dictionary containing personal data, and save it as a CSV file using Python?"
import pandas as pd

data = {
    'Name': ['Alice','Bob','Charlie','David'],
    'Age': [24,30,28,35],
    'City': ['New York','Los Angeles','Chicago','Houston'],
    'Occupation': ['Engineer','Doctor','Artist','Chef']
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
print(df)
