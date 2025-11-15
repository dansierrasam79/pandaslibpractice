import pandas as pd

# Create the two sample Series with the given data.
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

print("Series 1:")
print(series1)
print("\nSeries 2:")
print(series2)
print("\n" + "="*50 + "\n")

# Perform an element-wise equality comparison.
# This will check if each element in series1 is equal to the
# corresponding element in series2.
print("Check for element-wise equality (Series 1 == Series 2):")
equal_result = series1 == series2
print(equal_result)
# Expected Output:
# 0    False
# 1    False
# 2    False
# 3    False
# 4     True
# dtype: bool

print("\n" + "="*50 + "\n")

# Perform an element-wise greater than comparison.
# This checks if each element in series1 is greater than the
# corresponding element in series2.
print("Check for element-wise 'greater than' (Series 1 > Series 2):")
greater_result = series1 > series2
print(greater_result)
# Expected Output:
# 0     True
# 1     True
# 2     True
# 3     True
# 4    False
# dtype: bool

print("\n" + "="*50 + "\n")

# Perform an element-wise less than comparison.
# This checks if each element in series1 is less than the
# corresponding element in series2.
print("Check for element-wise 'less than' (Series 1 < Series 2):")
less_result = series1 < series2
print(less_result)
# Expected Output:
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# dtype: bool