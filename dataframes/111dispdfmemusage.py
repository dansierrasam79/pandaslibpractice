import pandas as pd
import numpy as np

# Sample data
data = {'Name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
        'Date_Of_Birth': ['17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
        'Age': [18.5, 21.2, 22.5, 22.0, 23.0]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Use .info() to get a concise summary of the DataFrame, including total memory usage
print("\nGlobal usage of memory of the DataFrame:")
df.info(memory_usage='deep')

# Use .memory_usage(deep=True) to get the memory usage of each column
# The 'deep=True' parameter is essential for accurate memory usage of object types (like strings)
print("\nThe usage of memory of every column of the said DataFrame:")
print(df.memory_usage(deep=True))