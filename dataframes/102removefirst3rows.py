import pandas as pd

# Sample data
data = {'col1': [1, 2, 3, 4, 7, 11],
        'col2': [4, 5, 6, 9, 5, 0],
        'col3': [7, 5, 8, 12, 1, 11]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Use slicing to select all rows from the 3rd index onwards,
# effectively removing the first 3 rows.
# Python uses 0-based indexing, so df[3:] starts at the fourth row.
new_df = df[3:]

print("\nAfter removing the first 3 rows:")
print(new_df)