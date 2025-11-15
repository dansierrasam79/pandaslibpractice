import pandas as pd
import numpy as np

# Sample data
data = {'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
        'date_of_birth': ['17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
        'age': [18.5, 21.2, 22.5, 22.0, 23.0]}

# Create the original DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nData types of the columns:")
print(df.info())

# Select only the numerical columns
# The np.number type includes both integer and float types.
numerical_columns = df.select_dtypes(include=np.number)
print("\nSelected numerical columns:")
print(numerical_columns)

# Select only the object (string) columns
string_columns = df.select_dtypes(include='object')
print("\nSelected string columns:")
print(string_columns)