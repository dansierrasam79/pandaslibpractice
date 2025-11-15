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

# Add a prefix to all column names using the add_prefix() method
# The method returns a new DataFrame with the updated column names.
df_with_prefix = df.add_prefix('A_')
print("\nDataFrame with added prefix 'A_':")
print(df_with_prefix)

# Add a suffix to all column names using the add_suffix() method
# This is applied to the original DataFrame for a clear demonstration.
df_with_suffix = df.add_suffix('_1')
print("\nDataFrame with added suffix '_1':")
print(df_with_suffix)