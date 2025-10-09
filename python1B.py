#How can you create a time series dataset with a date range and random numerical values, and save it as a CSV file using Python?"
import pandas as pd
import numpy as np

date_range=pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
values=np.random.randn(len(date_range))
data={
    'Date': date_range,
    'Value': values
}

df=pd.DataFrame(data)
df.to_csv('Time_series_dataset.csv',index=False)