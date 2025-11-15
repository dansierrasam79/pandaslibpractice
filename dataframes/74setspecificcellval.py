import pandas as pd
import numpy as np

# Sample Python dictionary data
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame
df = pd.DataFrame(exam_data, index=labels)

print("Original DataFrame:")
print(df)

# Reset the index to get a default integer index (0, 1, 2, ...)
df = df.reset_index(drop=True)

# Use .loc to set the value for the cell at row index 8, column 'score'
df.loc[8, 'score'] = 10.2

print("\nDataFrame after setting the score in row 8 to 10.2:")
print(df)