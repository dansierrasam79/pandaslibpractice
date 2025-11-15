import pandas as pd
import numpy as np

# Sample data
data = {
    'group_id': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'value': [10, 20, 5, 30, 15, 45, 35, 25],
    'data_col': np.random.randn(8)
}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group the DataFrame by 'group_id' and get the lowest 2 records from each group
# based on the 'value' column.
# The `nsmallest()` method efficiently finds the lowest values in each group.
lowest_n_per_group = df.groupby('group_id').apply(lambda x: x.nsmallest(2, 'value'))

print("\nLowest 2 records within each group:")
print(lowest_n_per_group)