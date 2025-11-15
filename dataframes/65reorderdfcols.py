import pandas as pd

# Sample data for the DataFrame
data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Reorder the columns by passing a new list of column names
df_reordered = df[['col3', 'col2', 'col1']]

print("\nAfter altering col1 and col3:")
print(df_reordered)