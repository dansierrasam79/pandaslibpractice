import pandas as pd

# Sample data for the DataFrame
data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Select the row at integer index 2 using .iloc
# .iloc is used for integer-location based indexing
# It selects rows and columns by their integer position in the DataFrame,
# starting from 0.
selected_row = df.iloc[2]

print("\nRow at integer index 2:")
print(selected_row)