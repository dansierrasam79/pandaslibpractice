import pandas as pd

# Sample data
data = {'col1': [1, 2, 3, 4, 7],
        'col2': [4, 5, 6, 9, 5],
        'col3': [7, 8, 12, 1, 11]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Select all columns except 'col3'
# The .drop() method with the `columns` parameter is a very
# readable and efficient way to remove one or more columns.
df_filtered = df.drop(columns=['col3'])

print("\nAll columns except 'col3':")
print(df_filtered)