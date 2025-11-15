import pandas as pd

# Step 1: Create a sample Pandas Series where each element is a list.
data_with_lists = pd.Series([
    [10, 20, 30],
    [40, 50],
    [60]
])

print("Original Series with lists:")
print(data_with_lists)
print("\n" + "="*50 + "\n")

# Step 2: Use the .explode() method to flatten the Series.
# This will create a new row for each element in the original lists.
flattened_series = data_with_lists.explode()

print("Flattened Series after using explode():")
print(flattened_series)
print("\n" + "="*50 + "\n")

# Note the new index after exploding.
print("Notice how the index is repeated for each exploded value.")
print("This is useful for later joining with other DataFrames.")