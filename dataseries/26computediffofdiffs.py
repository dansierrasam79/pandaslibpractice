import pandas as pd

# 1. Create a sample Pandas Series with numerical data
print("Original Series:")
series_data = pd.Series([10, 15, 23, 34, 48, 65, 85, 108])
print(series_data)
print("-" * 50)

# 2. Calculate the first-order difference
# The diff() method computes the difference between an element and the element before it.
# The result is a new Series with the same length, where the first element is NaN.
first_difference = series_data.diff()
print("First-order difference:")
print(first_difference)
print("-" * 50)

# 3. Calculate the second-order difference (difference of differences)
# We apply the diff() method again to the result of the first difference.
# The result will be the difference between consecutive values in the first_difference Series.
second_difference = first_difference.diff()
print("Second-order difference (difference of differences):")
print(second_difference)