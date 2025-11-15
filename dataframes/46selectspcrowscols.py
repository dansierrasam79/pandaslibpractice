import pandas as pd
import numpy as np

# Sample Python dictionary data
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# List of index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create a DataFrame with the specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Select the 'name' and 'score' columns for rows at index 1, 3, 5, and 6
# Note: Python uses 0-based indexing, so row 1 is the second row, row 3 is the fourth, and so on.
# We use .iloc to select by integer location for the rows,
# and then use standard column selection for the columns.
selected_data = df.iloc[[1, 3, 5, 6]][['name', 'score']]

print("Original DataFrame:")
print(df)

print("\nSelected 'name' and 'score' columns from rows 1, 3, 5, and 6:")
print(selected_data)