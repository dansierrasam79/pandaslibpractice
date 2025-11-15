import pandas as pd
import numpy as np

# Sample data
data = {'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
        'date_of_birth': ['17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
        'age': [18, 21, 22, 22, 23]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame and shape:")
print(df)
print(df.shape)

# Create the first random subset (60% of the data)
# We set a random_state to ensure reproducibility of the random split.
df_subset1 = df.sample(frac=0.6, random_state=42)

# Create the second subset by dropping the rows from the first subset
df_subset2 = df.drop(df_subset1.index)

print("\nSubset-1 and shape:")
print(df_subset1)
print(df_subset1.shape)

print("\nSubset-2 and shape:")
print(df_subset2)
print(df_subset2.shape)