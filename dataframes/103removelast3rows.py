import pandas as pd

# Sample data
data = {'col1': [1, 2, 3, 4, 7, 11],
        'col2': [4, 5, 6, 9, 5, 0],
        'col3': [7, 5, 8, 12, 1, 11]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Use negative slicing to select all rows except the last 3.
# The slice df[:-3] effectively removes the last 3 rows.
new_df = df[:-3]

print("\nAfter removing the last 3 rows:")
print(new_df)