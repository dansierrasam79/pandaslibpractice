import pandas as pd

# 1. Create two sample Pandas Series with some common and some unique elements
print("Series 1:")
series1 = pd.Series([10, 20, 30, 40, 50])
print(series1)
print("-" * 30)

print("Series 2:")
series2 = pd.Series([20, 50, 60, 70])
print(series2)
print("-" * 30)

# 2. Find the items in Series 1 that are not present in Series 2
# We use a boolean mask created with the `isin()` method and the `~` (tilde) operator for negation.
series1_unique = series1[~series1.isin(series2)]

# 3. Find the items in Series 2 that are not present in Series 1
series2_unique = series2[~series2.isin(series1)]

# 4. Combine the unique items from both series to get the full symmetric difference
# The pd.concat() function is used to concatenate the two resulting Series.
symmetric_difference = pd.concat([series1_unique, series2_unique])

# 5. Print the result
print("Items that are not common between the two Series:")
print(symmetric_difference)