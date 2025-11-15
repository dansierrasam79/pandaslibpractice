import pandas as pd
import numpy as np

# 1. Create a sample Pandas Series with unsorted values
# We'll use a mix of positive, negative, and zero values.
print("Original Series:")
series_data = pd.Series([10, -5, 20, 0, 15, -1, 8])
print(series_data)
print("-" * 30)

# 2. Sort the Series in ascending order (default behavior)
# The `sort_values()` method is used for this.
sorted_series_asc = series_data.sort_values()
print("Series sorted in ascending order:")
print(sorted_series_asc)
print("-" * 30)

# 3. Sort the Series in descending order
# We can use the 'ascending=False' parameter.
sorted_series_desc = series_data.sort_values(ascending=False)
print("Series sorted in descending order:")
print(sorted_series_desc)
print("-" * 30)

# 4. Demonstrate sorting with a Series containing non-numeric data
print("Original Series with string data:")
string_series = pd.Series(['cherry', 'apple', 'banana', 'date'])
print(string_series)
print("-" * 30)

# Sort the string Series alphabetically (ascending)
sorted_string_series = string_series.sort_values()
print("String Series sorted alphabetically:")
print(sorted_string_series)