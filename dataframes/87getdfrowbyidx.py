import pandas as pd

# Sample data to create the DataFrame
data = {'col1': [1, 2, 3, 4, 7],
        'col2': [4, 5, 6, 9, 5],
        'col3': [7, 8, 12, 1, 11]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Select the row at integer index 0
row_0 = df.iloc[0]

print("\nValue of Row 0:")
print(row_0)

# Select the row at integer index 3
row_3 = df.iloc[3]

print("\nValue of Row 3:")
print(row_3)