import pandas as pd
import numpy as np

# Create the original DataFrame from the sample data
data = {
    'col1': [1, 2, 3, 4, 7],
    'col2': [4, 5, 6, 9, 5],
    'col3': [7, 8, 12, 1, 11]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Find the index of the row with the maximum value for each specified column
# The .idxmax() method returns the index of the first occurrence of the maximum value.
max_row_col1 = df['col1'].idxmax()
max_row_col2 = df['col2'].idxmax()
max_row_col3 = df['col3'].idxmax()

print("\nRow where col1 has a maximum value:")
print(max_row_col1)

print("\nRow where col2 has a maximum value:")
print(max_row_col2)

print("\nRow where col3 has a maximum value:")
print(max_row_col3)