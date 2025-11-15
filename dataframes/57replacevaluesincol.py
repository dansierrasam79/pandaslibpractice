import pandas as pd
import numpy as np

pd.set_option('future.no_silent_downcasting', True)

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
print("\nData types before replacement:")
print(df.info())

# Replace 'yes' with True and 'no' with False in the 'qualify' column
df['qualify'] = df['qualify'].replace({'yes': True, 'no': False})

print("\nDataFrame after replacement:")
print(df)
print("\nData types after replacement:")
print(df.info())