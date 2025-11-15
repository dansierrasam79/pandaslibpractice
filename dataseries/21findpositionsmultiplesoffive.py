import pandas as pd

# 1. Create a sample Pandas Series with various integer values
print("Original Series:")
series_data = pd.Series([25, 12, 10, 4, 30, 8, 5, 15, 23])
print(series_data)
print("-" * 50)

# 2. Find the positions of numbers that are multiples of 5
# We use the modulo operator (%) to check if a number is divisible by 5.
# If the remainder of the division is 0, the number is a multiple of 5.
# This creates a boolean Series (a mask) where True indicates a multiple of 5.
boolean_mask = series_data % 5 == 0
print("Boolean Mask:")
print(boolean_mask)
print("-" * 50)

# 3. Use the boolean mask to get the subset of values and their indices.
# We can then access the index attribute of this subset.
positions = series_data[boolean_mask].index

# 4. Print the final result
print("Positions (indices) of numbers that are multiples of 5:")
print(positions)