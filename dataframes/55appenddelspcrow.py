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

print("Original DataFrame:")
print(df)

# Append a new row 'k' with the specified values using .loc
df.loc['k'] = ["Suresh", 15.5, 1, "yes"]

print("\nDataFrame after appending new row 'k':")
print(df)

# Delete the new row 'k' using the .drop() method
df = df.drop('k')

print("\nDataFrame after deleting row 'k' (back to original state):")
print(df)