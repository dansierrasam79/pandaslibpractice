import pandas as pd
import numpy as np

# Sample Python dictionary data to create the DataFrame
data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Drop the rows with integer labels 2 and 4 (0-indexed, so 1 and 3).
# We are dropping the rows by their default integer index.
new_df = df.drop([1, 3])

print("\nNew DataFrame after dropping rows with indices 1 and 3:")
print(new_df)