import pandas as pd

# Sample data
data = {'col1': [1, 2, 3, 4, 7, 11],
        'col2': [4, 5, 6, 9, 5, 0],
        'col3': [7, 5, 8, 12, 1, 11]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Use the .head() method to get the first 3 rows
# You can change the number inside the parentheses to get a different number of rows.
first_n_rows = df.head(3)

print("\nFirst 3 rows of the DataFrame:")
print(first_n_rows)