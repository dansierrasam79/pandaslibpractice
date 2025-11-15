import pandas as pd
import numpy as np
import string
import random
from datetime import datetime, timedelta

# --- DataFrame 1: Contains random values ---
print("DataFrame: Contains random values:")
# Create a DataFrame with 5 rows and 4 columns of random float values
# A random index is also generated to match the sample output
df_random = pd.DataFrame(np.random.randn(5, 4), 
                         columns=list('ABCD'),
                         index=[''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(5)])
print(df_random)

# --- DataFrame 2: Contains missing values ---
print("\nDataFrame: Contains missing values:")
# Start with a random DataFrame
df_missing = pd.DataFrame(np.random.randn(5, 4), 
                          columns=list('ABCD'),
                          index=[''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(5)])

# Insert a few missing values (NaN)
df_missing.iloc[2:4, 0] = np.nan
df_missing.iloc[0:2, 2] = np.nan
df_missing.iloc[1:3, 1] = np.nan
df_missing.iloc[4, 3] = np.nan
print(df_missing)

# --- DataFrame 3: Contains datetime values ---
print("\nDataFrame: Contains datetime values:")
# Create a date range to use as the index
date_index = pd.date_range('1/1/2000', periods=5)
# Create a DataFrame with random data and the datetime index
df_datetime = pd.DataFrame(np.random.randn(5, 4), index=date_index, columns=list('ABCD'))
print(df_datetime)

# --- DataFrame 4: Contains mixed values ---
print("\nDataFrame: Contains mixed values:")
# Create a dictionary with different data types for each column
mixed_data = {
    'A': np.arange(5),
    'B': np.random.rand(5),
    'C': ['foo1', 'foo2', 'foo3', 'foo4', 'foo5'],
    'D': [datetime(2009, 1, 1), datetime(2009, 1, 2), datetime(2009, 1, 5), datetime(2009, 1, 6), datetime(2009, 1, 7)]
}
# Create the DataFrame from the dictionary
df_mixed = pd.DataFrame(mixed_data)
print(df_mixed)