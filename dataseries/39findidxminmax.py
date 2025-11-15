import pandas as pd

# 1. Create a sample Pandas Series with numerical data
# We'll include duplicate values to show how the first occurrence is found.
print("Original Series:")
series_data = pd.Series([10, 5, 25, 30, 15, 8, 5, 40, 55, 60])
print(series_data)
print("-" * 50)

# 2. Find the index of the first occurrence of the smallest value
# The .idxmin() method returns the index of the first occurrence of the minimum value.
min_value_index = series_data.idxmin()
print(f"The smallest value is {series_data.min()} and its first index is: {min_value_index}")
print("-" * 50)

# 3. Find the index of the first occurrence of the largest value
# The .idxmax() method returns the index of the first occurrence of the maximum value.
max_value_index = series_data.idxmax()
print(f"The largest value is {series_data.max()} and its first index is: {max_value_index}")