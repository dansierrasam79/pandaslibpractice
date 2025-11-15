import pandas as pd
import numpy as np

# Create a Pandas Series
s = pd.Series([10, 20, 30, 40, 50])

print("Original Series:")
print(s)

# Convert to NumPy array
arr = s.to_numpy()   # preferred way
# arr = s.values     # older way, still works

print("\nConverted NumPy Array:")
print(arr)

print("\nType of object:", type(arr))