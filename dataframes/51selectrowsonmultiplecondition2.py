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

# Select rows where 'attempts' is less than 2 and 'score' is greater than 15.
# We use a boolean mask with two conditions combined with the '&' (AND) operator.
# Parentheses are used to ensure the correct order of operations.
filtered_data = df[(df['attempts'] < 2) & (df['score'] > 15)]

print("Original DataFrame:")
print(df)

print("\nRows with less than 2 attempts and a score greater than 15:")
print(filtered_data)