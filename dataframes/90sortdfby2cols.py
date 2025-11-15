import pandas as pd
import numpy as np

# Sample Python dictionary data and list labels.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame
df = pd.DataFrame(exam_data, index=labels)
print("Original DataFrame:")
print(df)

# Sort the DataFrame first by 'attempts' and then by 'name'
# The sorting is ascending by default for both columns
df_sorted = df.sort_values(by=['attempts', 'name'])

print("\nDataFrame sorted by 'attempts' and 'name':")
print(df_sorted)