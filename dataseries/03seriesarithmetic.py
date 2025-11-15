import pandas as pd

# Sample Series
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

print("Series 1:")
print(s1)
print("\nSeries 2:")
print(s2)

# Arithmetic operations
print("\nAddition:")
print(s1 + s2)

print("\nSubtraction:")
print(s1 - s2)

print("\nMultiplication:")
print(s1 * s2)

print("\nDivision:")
print(s1 / s2)