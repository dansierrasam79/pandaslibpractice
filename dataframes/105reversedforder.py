import pandas as pd
import numpy as np

# Sample data
data = {'W': [68, 75, 86, 80, 66],
        'X': [78, 85, 96, 80, 86],
        'Y': [84, 94, 89, 83, 86],
        'Z': [86, 97, 96, 72, 83]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Reverse the column order
# This is done by slicing the columns attribute with [::-1]
df_reversed_columns = df[df.columns[::-1]]
print("\nDataFrame with reversed column order:")
print(df_reversed_columns)

# Reverse the row order
# This is done by using .iloc with a slice [::-1]
df_reversed_rows = df.iloc[::-1]
print("\nDataFrame with reversed row order:")
print(df_reversed_rows)

# Reverse the row order and then reset the index
# We first reverse the rows and then call .reset_index() with drop=True
df_reversed_rows_reset_index = df.iloc[::-1].reset_index(drop=True)
print("\nDataFrame with reversed row order and reset index:")
print(df_reversed_rows_reset_index)