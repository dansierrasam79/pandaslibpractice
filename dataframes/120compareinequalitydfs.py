import pandas as pd
import numpy as np

# Sample data for the first DataFrame
data1 = {'W': [68.0, 75.0, 86.0, 80.0, np.nan],
         'X': [78.0, 85.0, np.nan, 80.0, 86.0],
         'Y': [84, 94, 89, 83, 86],
         'Z': [86, 97, 96, 72, 83]}

# Sample data for the second DataFrame
data2 = {'W': [78.0, 75.0, 86.0, 80.0, np.nan],
         'X': [78.0, 85.0, 96, 80.0, 76],
         'Y': [84, 84, 89, 83, 86],
         'Z': [86, 97, 96, 72, 83]}

# Create the DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("Original DataFrames:")
print("--- DataFrame 1 ---")
print(df1)
print("\n--- DataFrame 2 ---")
print(df2)

# Check for inequality between the two DataFrames
# The '!=' operator performs an element-wise comparison.
# Note: NaN values are considered unequal to each other.
inequality_check = df1.ne(df2)

print("\nCheck for inequality of the said dataframes:")
print(inequality_check)