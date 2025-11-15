import pandas as pd

# Sample data for the DataFrame
data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Delete rows where 'col2' is equal to 5.
# We create a boolean mask to select all rows where 'col2' is NOT equal to 5.
# This is a common and efficient way to filter data in Pandas.
df = df[df['col2'] != 5]

print("\nNew DataFrame after deleting rows where 'col2' is 5:")
print(df)