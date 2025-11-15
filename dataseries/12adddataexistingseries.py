import pandas as pd

# 1. Create a sample Pandas Series
print("Original Series:")
series = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(series)
print("-" * 30)

# 2. Add a single new value using the append method
# The _append() method returns a new Series with the added data.
# The `name` parameter can be used to label the new Series.
new_series = pd.Series([40], index=['d'])
series_with_single_value = series._append(new_series)
print("Series after adding a single value:")
print(series_with_single_value)
print("-" * 30)

# 3. Add multiple values from a list
# First, create a new Series from the list.
multiple_values = pd.Series([50, 60], index=['e', 'f'])
series_with_multiple_values = series_with_single_value._append(multiple_values)
print("Series after adding multiple values:")
print(series_with_multiple_values)
print("-" * 30)

# 4. Use `pd.concat` to combine two Series
# `pd.concat` is a more general function for combining pandas objects.
# It is often preferred for clarity and flexibility.
series_to_add = pd.Series([70, 80], index=['g', 'h'])
combined_series = pd.concat([series_with_multiple_values, series_to_add])
print("Combined Series using pd.concat:")
print(combined_series)