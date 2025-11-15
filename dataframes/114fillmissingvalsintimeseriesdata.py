import pandas as pd
import numpy as np

# Sample data with missing values (NaN)
data = {'c1': [120.0, 130.0, 140.0, 150.0, np.nan, 170.0],
        'c2': [7.0, np.nan, 10.0, np.nan, 5.5, 16.5]}

# Create a date range to use as the index
date_index = pd.date_range('2000-01-03', periods=6, freq='D')

# Create the DataFrame
df = pd.DataFrame(data, index=date_index)

print("Original DataFrame:")
print(df)

# Use interpolate() to fill missing values
# The default method is 'linear', which is suitable for many time series
df_interpolated = df.interpolate(method='linear', axis=0)

print("\nDataFrame after interpolate:")
print(df_interpolated)