import pandas as pd
import re

# Sample data
data = {'agent': ['a001', 'a002', 'a003', 'a003', 'a004'],
        'purchase': [4500, 7500, '$3000.25', '$1250.35', '9000.00']}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nData Types:")
# Use apply and type to show the individual types in the series
print(df['purchase'].apply(lambda x: type(x)))

# Clean the 'purchase' column using a regular expression to remove non-numeric characters
# The regex r'[^\d.]' matches any character that is NOT a digit or a period.
# The `str` accessor is used to apply string methods to the entire Series.
df['purchase'] = df['purchase'].astype(str).str.replace(r'[^\d.]', '', regex=True)

# Convert the column to a numeric data type (float)
df['purchase'] = pd.to_numeric(df['purchase'])

print("\nNew Data Types:")
print(df['purchase'].apply(lambda x: type(x)))
