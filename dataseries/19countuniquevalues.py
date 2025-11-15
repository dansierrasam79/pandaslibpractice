import pandas as pd
import numpy as np

# 1. Create a sample Pandas Series with duplicate values
# This Series contains a mix of numbers and strings to show flexibility.
print("Original Series:")
series_data = pd.Series([1, 2, 2, 3, 3, 3, 4, 'a', 'b', 'b'])
print(series_data)
print("-" * 30)

# 2. Use the value_counts() method to get the frequency of each unique item
# By default, this method returns a new Series with the unique values as the index
# and their counts as the values, sorted in descending order.
value_counts = series_data.value_counts()

# 3. Print the result
print("Frequency counts of each unique value:")
print(value_counts)