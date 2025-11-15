import pandas as pd

# Sample data for the original DataFrame
data = {'col2': [4, 5, 6, 9, 5],
        'col3': [7, 8, 12, 1, 11]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Create a new column 'col1' with data
new_column_data = [1, 2, 3, 4, 7]

# Insert the new column at the first position (index 0)
# Syntax: df.insert(loc, column, value, allow_duplicates=False)
# loc: integer position, 0 for the beginning
# column: name of the new column
# value: the data to insert
df.insert(loc=0, column='col1', value=new_column_data)

print("\nNew DataFrame after inserting 'col1':")
print(df)