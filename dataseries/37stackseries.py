import pandas as pd

# 1. Create two sample Pandas Series
# We'll use different indices for each to show how stacking handles them.
print("Series 1:")
series1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(series1)
print("-" * 50)

print("Series 2:")
series2 = pd.Series([40, 50, 60], index=['d', 'e', 'f'])
print(series2)
print("-" * 50)

# 2. Stack the Series vertically (row-wise)
# The `pd.concat()` function is the primary tool for this. By default, it stacks vertically.
# This operation adds the elements of series2 as new rows to series1.
vertical_stack = pd.concat([series1, series2])
print("Vertical Stack:")
print(vertical_stack)
print("-" * 50)

# 3. Stack the Series horizontally (column-wise)
# We use `pd.concat()` again, but with the `axis=1` parameter.
# This aligns the series by their indices. Since the indices are different,
# Pandas will use `NaN` to fill in the missing values.
# The `keys` parameter can be used to label the new columns.
horizontal_stack = pd.concat([series1, series2], axis=1, keys=['Series1_values', 'Series2_values'])
print("Horizontal Stack:")
print(horizontal_stack)