import pandas as pd
import numpy as np

# Create the first Pandas Series
s1 = pd.Series([100, 200, 'python', 300.12, 400])

# Create the second Pandas Series
s2 = pd.Series([10, 20, 'php', 30.12, 40])

print("Original Data Series 1:")
print(s1)

print("\nOriginal Data Series 2:")
print(s2)

# Combine the two series into a DataFrame.
# We pass a dictionary to the DataFrame constructor where keys become column names.
df = pd.DataFrame({0: s1, 1: s2})

print("\nNew DataFrame combining two series:")
print(df)