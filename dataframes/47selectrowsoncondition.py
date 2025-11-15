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

# Select and display rows where 'attempts' is greater than 2
# This is a common method called boolean indexing, where a condition
# is applied to a column to create a boolean Series, which is then used
# to filter the DataFrame.
filtered_data = df[df['attempts'] > 2]

print("Original DataFrame:")
print(df)

print("\nRows where the number of attempts is greater than 2:")
print(filtered_data)