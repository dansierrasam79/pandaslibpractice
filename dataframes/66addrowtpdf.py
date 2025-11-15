import pandas as pd

# Sample data for the DataFrame
data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Add a new row to the DataFrame.
# Using df.loc[len(df)] is a common way to append a row with a new integer index.
df.loc[len(df)] = [10, 11, 12]

print("\nDataFrame after adding one row:")
print(df)