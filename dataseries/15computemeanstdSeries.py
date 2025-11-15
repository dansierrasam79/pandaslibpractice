import pandas as pd
import numpy as np

# 1. Create a sample Pandas Series with numerical data
print("Original Series:")
series_data = pd.Series([12, 18, 25, 30, 15, 22, 19, 28])
print(series_data)
print("-" * 30)

# 2. Calculate the mean of the Series
# The .mean() method computes the arithmetic average of the values.
series_mean = series_data.mean()
print(f"Mean of the Series: {series_mean:.2f}")
print("-" * 30)

# 3. Calculate the standard deviation of the Series
# The .std() method computes the standard deviation, which measures the dispersion of the data.
series_std = series_data.std()
print(f"Standard deviation of the Series: {series_std:.2f}")