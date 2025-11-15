import pandas as pd
import numpy as np

# A Pandas Series is a one-dimensional labeled array.
# You can create a Series from a list, a NumPy array, or a dictionary.

# Example 1: Creating a Series from a simple Python list.
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)

print("Series created from a list:")
print(series_from_list)

print("\n" + "="*50 + "\n")

# Example 2: Creating a Series from a NumPy array.
data_array = np.array([1.5, 2.7, 3.1, 4.8])
series_from_array = pd.Series(data_array)

print("Series created from a NumPy array:")
print(series_from_array)

print("\n" + "="*50 + "\n")

# Example 3: Creating a Series with a custom index.
# This shows how a Series is 'labeled'.
data_with_index = [100, 200, 300]
custom_index = ['a', 'b', 'c']
series_with_index = pd.Series(data_with_index, index=custom_index)

print("Series created with a custom index:")
print(series_with_index)
