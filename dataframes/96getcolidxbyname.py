import pandas as pd

# Sample data
data = {'col1': [1, 2, 3, 4, 7],
        'col2': [4, 5, 6, 9, 5],
        'col3': [7, 8, 12, 1, 11]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Get the integer index of the 'col2' column
# The .get_loc() method is the recommended way to get the integer position
# for a given column label.
col_index = df.columns.get_loc('col2')

print("\nIndex of 'col2':")
print(col_index)