import pandas as pd

# Create a Pandas Series
data = pd.Series([10, 20, 30, 40, 50])

print("Pandas Series:")
print(data)

# Convert to Python list
py_list = data.tolist()

# Print list and its type
print("\nConverted to Python list:")
print(py_list)
print("Type of object:", type(py_list))