import pandas as pd

# Sample data
data = {'col1': ['C1', 'C1', 'C2', 'C2', 'C2', 'C3', 'C2'],
        'col2': [1, 2, 3, 3, 4, 6, 5]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group by 'col1' and aggregate the values of 'col2' into a list
# The .agg(list) method is a concise way to perform this aggregation
grouped_df = df.groupby('col1')['col2'].agg(list)

print("\nGrouped DataFrame:")
print(grouped_df)