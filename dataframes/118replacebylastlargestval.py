import pandas as pd
import numpy as np

# Sample data
data = {'rnum': [23, 21, 27, 22, 18, 30, 25, 33, 15, 34, 19, 31, 32, 19]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Calculate the cumulative maximum of the 'rnum' column.
# This creates a new Series where each value is the largest value seen up to that point.
# The .shift(1) method moves this series down by one row, so each row now holds the
# largest value from all *previous* rows.
last_largest = df['rnum'].expanding().max().shift(1)

# For the first row, there is no "last largest value," so we fill the NaN with a value
# that ensures the first value is not replaced (e.g., the first value itself).
last_largest.iloc[0] = df['rnum'].iloc[0]

# Use a boolean condition to create a new column.
# If the current value in 'rnum' is less than the `last_largest` value,
# the new value is 0; otherwise, it keeps its original value.
df['rnum'] = np.where(df['rnum'] < last_largest, 0, df['rnum'])

print("\nReplace current value in a dataframe column based on last largest value:")
print(df)