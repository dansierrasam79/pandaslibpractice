import pandas as pd

# 1. Create a sample Pandas Series with a custom index
print("Original Series:")
series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(series)
print("-" * 30)

# 2. Define the new desired order for the index
# Note that we are reordering the existing labels.
new_index_order = ['c', 'a', 'd', 'b']

# 3. Use the reindex() method to apply the new order
# This method returns a new Series with the index reordered.
reindexed_series = series.reindex(new_index_order)
print("Series after changing the order of the index:")
print(reindexed_series)
print("-" * 30)

# 4. Demonstrate what happens with a new index that includes a missing label
# The new label 'e' is not in the original Series, so its value will be NaN.
new_index_with_missing = ['c', 'e', 'd', 'b']
reindexed_with_missing = series.reindex(new_index_with_missing)
print("Series reindexed with a missing label 'e':")
print(reindexed_with_missing)