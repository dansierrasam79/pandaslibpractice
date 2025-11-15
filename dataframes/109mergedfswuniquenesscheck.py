import pandas as pd
import numpy as np

# Create the first DataFrame
df1 = pd.DataFrame({'Name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
                    'Date_Of_Birth': ['17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
                    'Age': [18.5, 21.2, 22.5, 22.0, 23.0]})

# Create two new DataFrames with overlapping data to demonstrate merging
df2 = df1.iloc[2:].copy()
df3 = df1.iloc[[0, 1, 3, 4]].copy()

print("Original DataFrame:")
print(df1)

print("\nNew DataFrames:")
print("DataFrame 2:")
print(df2)
print("\nDataFrame 3:")
print(df3)

# Merge with 'one_to_one' validation
print('\n"one_to_one": check if merge keys are unique in both left and right datasets:')
# Merging df2 with df3 on common columns ('Name', 'Date_Of_Birth', 'Age')
# Since 'Eesha Hinton' and 'Syed Wharton' appear in both, the merge works.
# The validate='one_to_one' ensures that each key appears at most once in each DataFrame.
# If a key appeared more than once in either df2 or df3, it would raise an error.
try:
    merged_one_to_one = pd.merge(df2, df3, how='inner', on=['Name', 'Date_Of_Birth', 'Age'], validate='one_to_one')
    print(merged_one_to_one)
except pd.errors.MergeError as e:
    print(e)

# Merging df2 with df3 on 'Name' and validate 'one_to_many'
# This checks if the keys in the left DataFrame (df2) are unique.
print('\n"one_to_many" or "1:m": check if merge keys are unique in left dataset:')
try:
    merged_one_to_many = pd.merge(df2, df3, how='inner', on=['Name', 'Date_Of_Birth', 'Age'], validate='one_to_many')
    print(merged_one_to_many)
except pd.errors.MergeError as e:
    print(e)

# Merging df2 with df3 on 'Name' and validate 'many_to_one'
# This checks if the keys in the right DataFrame (df3) are unique.
print('\n"any_to_one" or "m:1": check if merge keys are unique in right dataset:')
try:
    merged_many_to_one = pd.merge(df2, df3, how='inner', on=['Name', 'Date_Of_Birth', 'Age'], validate='many_to_one')
    print(merged_many_to_one)
except pd.errors.MergeError as e:
    print(e)