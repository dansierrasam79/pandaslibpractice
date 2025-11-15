import pandas as pd
import numpy as np

# 1. Create a sample Pandas Series with duplicate values
print("Original Series:")
series_data = pd.Series([10, 20, 20, 30, 30, 30, 40, 50, 50, 50, 50])
print(series_data)
print("-" * 40)

# 2. Find the most frequent value in the Series
# The value_counts() method returns a new Series sorted by frequency in descending order.
# We can access the most frequent value (the first one) using .index[0].
most_frequent_value = series_data.value_counts().index[0]
print(f"The most frequent value is: {most_frequent_value}")
print("-" * 40)

# 3. Create a copy of the Series to avoid modifying the original
modified_series = series_data.copy()

# 4. Replace all values that are NOT the most frequent with the string 'Other'
# We use a boolean mask (modified_series != most_frequent_value) to select
# all elements that are not equal to the most frequent value.
# Then, we assign the string 'Other' to those selected elements.
modified_series[modified_series != most_frequent_value] = 'Other'

# 5. Print the resulting Series
print("Series after replacing all other values with 'Other':")
print(modified_series)