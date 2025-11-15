import pandas as pd

# Original list of lists
data = [[2, 4], [1, 3]]

print("Original list of lists:")
print(data)

# Convert the list of lists into a DataFrame
# The 'columns' parameter is used to specify the column headers
df = pd.DataFrame(data, columns=['col1', 'col2'])

print("\nNew DataFrame:")
print(df)