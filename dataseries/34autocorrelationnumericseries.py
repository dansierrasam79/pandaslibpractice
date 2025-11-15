import pandas as pd
import numpy as np

# 1. Create a sample Pandas Series
# Autocorrelation is often used with time series data, so we'll create one.
print("Original Series:")
series_data = pd.Series([10, 12, 15, 14, 18, 17, 20, 22, 25, 24])
print(series_data)
print("-" * 50)

# 2. Calculate the autocorrelation
# Pandas does not have a built-in method for this, so we'll use a NumPy function.
# The `np.correlate` function computes the cross-correlation of two 1-dimensional arrays.
# To compute autocorrelation, we correlate the series with itself, but we first need to
# center the data by subtracting the mean.
centered_series = series_data - series_data.mean()

# The mode='full' argument returns the cross-correlation at all possible lags.
# The `centered_series` must be converted to a NumPy array for this operation.
# The result is symmetric, so we take the second half `[len(series_data)-1:]`
autocorrelation = np.correlate(centered_series, centered_series, mode='full')[len(series_data)-1:]

# 3. Normalize the autocorrelation
# The result needs to be divided by the autocorrelation at lag 0 (which is the variance)
# to normalize it to a range between -1 and 1.
# The variance is the sum of squared centered differences, which is the first value of the unnormalized result.
normalization_factor = autocorrelation[0]
autocorrelation /= normalization_factor

# 4. Print the final result
# The values represent the correlation at different lags (from 0 to n-1).
print("Autocorrelation of the Series:")
print(autocorrelation)