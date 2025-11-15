import pandas as pd
import numpy as np

# Sample Python dictionary data and list labels.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9.1, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.8, 19.13],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame
df = pd.DataFrame(exam_data, index=labels)

print("Original DataFrame:")
print(df)

# Print the data types of the columns
print("\nData types of the columns of the said DataFrame:")
print(df.dtypes)

# Before converting a column to an integer type, you must handle any NaN values.
# Integers in Pandas cannot natively store NaN. We will replace NaNs with 0.
# The astype(int) method will truncate the float values, e.g., 12.5 becomes 12.
df['score'] = df['score'].fillna(0).astype(int)

print("\nNew DataFrame after changing the data type of 'score' column from float to int:")
print(df)

# Print the new data types of the columns to verify the change
print("\nData types of the columns of the DataFrame now:")
print(df.dtypes)