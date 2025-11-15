import pandas as pd
import numpy as np

# 1. Create two sample Pandas Series
# series_to_find contains the values we want to locate.
# series_to_search contains the values we want to search within.
print("Series with values to find:")
series_to_find = pd.Series(['apple', 'cherry', 'grape', 'banana', 'fig'])
print(series_to_find)
print("-" * 50)

print("Series to search within:")
series_to_search = pd.Series(['banana', 'cherry', 'date', 'apple', 'fig'])
print(series_to_search)
print("-" * 50)

# 2. Get the positions of items from `series_to_find` in `series_to_search`
# The `get_indexer()` method of a Pandas Index is the most efficient way to do this.
# It returns an integer array of positions of the items from one index in another.
# If an item is not found, it returns -1.
positions = pd.Index(series_to_search).get_indexer(series_to_find)

# 3. Print the results
# The resulting `positions` array corresponds to the original items in `series_to_find`.
# For example, 'apple' from series_to_find is at position 3 in series_to_search.
# 'grape' is not found, so its position is -1.
print("Positions of items from the first Series within the second:")
print(positions)