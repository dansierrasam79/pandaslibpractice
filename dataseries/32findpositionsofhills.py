import pandas as pd

# 1. Create a sample Pandas Series with various integer values
print("Original Series:")
series_data = pd.Series([1, 5, 2, 8, 3, 9, 6, 12, 10, 15, 7])
print(series_data)
print("-" * 50)

# 2. Find the values that are greater than the value before them
# The .shift(1) method moves all values down by one position, allowing for
# an element-wise comparison with the original Series.
greater_than_left = series_data > series_data.shift(1)
print("Is value greater than left neighbor?")
print(greater_than_left)
print("-" * 50)

# 3. Find the values that are greater than the value after them
# The .shift(-1) method moves all values up by one position for the comparison.
greater_than_right = series_data > series_data.shift(-1)
print("Is value greater than right neighbor?")
print(greater_than_right)
print("-" * 50)

# 4. Combine the two conditions to find "hills"
# We use the logical AND operator `&` to find positions where BOTH conditions are True.
# This results in a boolean mask.
hill_mask = greater_than_left & greater_than_right
print("Is value a 'hill' (greater than both neighbors)?")
print(hill_mask)
print("-" * 50)

# 5. Extract the positions (indices) where the mask is True
# We use the boolean mask to filter the Series and then access its index.
hill_positions = series_data[hill_mask].index

# 6. Print the final result
print("Positions of values greater than both neighbors:")
print(hill_positions)