import pandas as pd

# 1. Create a sample Pandas Series
# We'll use a custom index to clearly demonstrate how it becomes a new column.
print("Original Series:")
series = pd.Series([100, 200, 300, 400], index=['apple', 'banana', 'cherry', 'date'])
print(series)
print("-" * 50)

# 2. Convert the Series to a DataFrame
# The .to_frame() method is the simplest way to do this.
# It creates a DataFrame with one column (named '0' by default) and the original index.
df_from_series = series.to_frame()
print("DataFrame created from the Series (before resetting index):")
print(df_from_series)
print("-" * 50)

# 3. Convert the index into a new column
# The .reset_index() method is perfect for this task.
# It takes the Series' index and turns it into a regular column.
# The `inplace=True` argument can be used to modify the DataFrame directly.
df_with_index_as_column = df_from_series.reset_index()

# 4. Print the final DataFrame
# The original index is now a column named 'index' by default.
print("Final DataFrame with the index as a new column:")
print(df_with_index_as_column)

# 5. Optional: Change the column names
# You can easily rename the columns to be more descriptive.
df_with_index_as_column.columns = ['fruit', 'value']
print("-" * 50)
print("Final DataFrame with custom column names:")
print(df_with_index_as_column)