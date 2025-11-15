import pandas as pd

# 1. Create a sample Pandas Series with some data
print("Original Series:")
series_data = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'])
print(series_data)
print("-" * 30)

# 2. Define the positions (integer indices) to extract
# We want to extract the items at positions 0, 3, and 5.
positions_to_extract = [0, 3, 5]
print(f"Positions to extract: {positions_to_extract}")
print("-" * 30)

# 3. Use integer-location based indexing to get the items
# The .iloc[] accessor is used to select data by its integer position.
# We pass the list of desired positions to .iloc[].
extracted_items = series_data.iloc[positions_to_extract]

# 4. Print the result
print("Extracted items at the given positions:")
print(extracted_items)