import pandas as pd
import numpy as np

# Sample Python dictionary data
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame with the custom index
df = pd.DataFrame(exam_data, index=labels)
print("Original DataFrame with custom index:")
print(df)

# Convert the index into a new column named 'index'
# reset_index() creates a new DataFrame, so we must reassign it.
df = df.reset_index()

print("\nDataFrame after converting the index to a column:")
print(df)

# If you want to hide the index when printing, you can use to_string()
print("\nDataFrame printed without the default index visible:")
print(df.to_string(index=False))