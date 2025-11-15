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

# Drop the first two rows (with labels 'a' and 'b') to create a non-consecutive index
df = df.drop(['a', 'b'])

print("\nDataFrame after dropping the first two rows:")
print(df)

# Reset the index, turning the old index into a new column.
df_reset = df.reset_index()

print("\nDataFrame after resetting the index:")
print(df_reset)

# To get a clean new index without keeping the old one, you can use drop=True.
df_clean_index = df.reset_index(drop=True)

print("\nDataFrame with a new index and old index dropped:")
print(df_clean_index)