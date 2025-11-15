import pandas as pd
import numpy as np

# Step 1: Create a sample NumPy array.
# We will use np.array() to create a one-dimensional array of integers.
numpy_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Original NumPy Array:")
print(numpy_array)
print(f"Data type of the original object: {type(numpy_array)}")
print("\n" + "="*50 + "\n")

# Step 2: Convert the NumPy array to a Pandas Series.
# The pd.Series() constructor can take the NumPy array as its first argument.
pandas_series = pd.Series(numpy_array)

print("Converted Pandas Series:")
print(pandas_series)
print(f"Data type of the new object: {type(pandas_series)}")