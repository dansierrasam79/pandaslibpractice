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

# Select and display rows where the score is between 15 and 20 (inclusive)
# We use boolean indexing with two conditions combined with the '&' (AND) operator.
# The parentheses are crucial for correct evaluation of the conditions.
filtered_data = df[(df['score'] >= 15) & (df['score'] <= 20)]

print("Original DataFrame:")
print(df)

print("\nRows where the score is between 15 and 20 (inclusive):")
print(filtered_data)