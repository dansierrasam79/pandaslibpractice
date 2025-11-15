import pandas as pd

# Sample data
data = {'col1': [1, 2, 3, 4, 7],
        'col2': [4, 5, 6, 9, 5],
        'col3': [7, 8, 12, 1, 11]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Get the number of columns using the len() function on df.columns
num_columns = len(df.columns)

print("\nNumber of columns:")
print(num_columns)