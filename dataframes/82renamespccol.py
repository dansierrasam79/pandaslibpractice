import pandas as pd

# Create the original DataFrame from the sample data
data = {'col1': [1, 2, 3],
        'col2': [4, 5, 6],
        'col3': [7, 8, 9]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Rename the 'col2' column to 'Column2' using the .rename() method.
# We pass a dictionary to the 'columns' parameter to specify the mapping.
# The 'inplace=True' argument modifies the DataFrame directly.
df.rename(columns={'col2': 'Column2'}, inplace=True)

print("\nNew DataFrame after renaming the second column:")
print(df)