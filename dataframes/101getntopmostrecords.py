import pandas as pd
import numpy as np

# Sample data
data = {'group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C'],
        'value': [10, 20, 5, 15, 25, 30, 8, 12, 18, 22]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Get the top 2 records from each group based on 'value'
# The .groupby() method partitions the DataFrame by the 'group' column.
# The .apply() method then runs the specified function on each group.
# The lambda function uses .nlargest(n, 'column') to find the top n values.
'''FutureWarning: DataFrameGroupBy.apply operated on the grouping columns. 
This behavior is deprecated, and in a future version of pandas the grouping columns will be excluded 
from the operation. Either pass `include_groups=False` to exclude the groupings or explicitly 
select the grouping columns after groupby to silence this warning.'''
top_records = df.groupby('group', group_keys=False).apply(lambda x: x.nlargest(2, 'value'))

print("\nTop 2 records within each group:")
print(top_records)