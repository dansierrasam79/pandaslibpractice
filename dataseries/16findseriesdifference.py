import pandas as pd

# 1. Create two sample Pandas Series
# The goal is to find which items in series1 are not in series2.
print("Series 1:")
series1 = pd.Series([10, 20, 30, 40, 50])
print(series1)
print("-" * 30)

print("Series 2:")
series2 = pd.Series([20, 50, 60, 70])
print(series2)
print("-" * 30)

# 2. Find the items in series1 that are NOT present in series2
# We use a boolean mask created with the `isin()` method.
# `series1.isin(series2)` returns a boolean Series (True/False)
# `~` is the tilde operator, which inverts the boolean values (True becomes False, and vice versa).
# We then use this inverted mask to filter series1.
items_not_present = series1[~series1.isin(series2)]

# 3. Print the result
print("Items in Series 1 that are not present in Series 2:")
print(items_not_present)