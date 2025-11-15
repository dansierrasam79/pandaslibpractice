import pandas as pd

# 1. Create a sample Pandas Series
print("Original Series:")
series = pd.Series([10, 5, 25, 30, 15, 8, 40, 55, 60])
print(series)
print("-" * 30)

# 2. Create a subset based on a simple condition (values greater than 20)
# This is done by passing a boolean condition inside square brackets.
subset_gt_20 = series[series > 20]
print("Subset with values greater than 20:")
print(subset_gt_20)
print("-" * 30)

# 3. Create a subset based on multiple conditions (values between 10 and 40)
# Multiple conditions must be enclosed in parentheses and combined with `&` (AND) or `|` (OR).
# The parentheses are necessary to ensure the conditions are evaluated correctly before the `&` operator.
subset_between_10_and_40 = series[(series > 10) & (series < 40)]
print("Subset with values between 10 and 40:")
print(subset_between_10_and_40)
print("-" * 30)

# 4. Create a subset of specific values using `isin()`
# This is useful for checking if values are in a list.
subset_in_list = series[series.isin([5, 30, 60])]
print("Subset with values that are in the list [5, 30, 60]:")
print(subset_in_list)