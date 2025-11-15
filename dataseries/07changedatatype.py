import pandas as pd

# Step 1: Create a sample Pandas Series with string data type.
# Notice that the values are numbers, but they are stored as strings.
data = ['10', '20', '30', '40', '50']
series_str = pd.Series(data)

print("Original Series with string data type:")
print(series_str)
print(f"Data type: {series_str.dtype}")
print("\n" + "="*50 + "\n")

# Step 2: Change the data type to integer using astype().
# The .astype() method returns a new Series with the converted data.
series_int = series_str.astype(int)

print("Series after changing data type to integer:")
print(series_int)
print(f"New data type: {series_int.dtype}")
print("\n" + "="*50 + "\n")

# Step 3: Change the data type again, this time to float.
# This works for both the original and the converted Series.
series_float = series_int.astype(float)

print("Series after changing data type to float:")
print(series_float)
print(f"New data type: {series_float.dtype}")