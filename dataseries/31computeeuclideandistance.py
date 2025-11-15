import pandas as pd
import numpy as np

# 1. Create two sample Pandas Series
# The series must have the same number of elements for the calculation.
print("Series 1:")
series1 = pd.Series([10, 20, 30, 40, 50])
print(series1)
print("-" * 50)

print("Series 2:")
series2 = pd.Series([12, 18, 32, 45, 48])
print(series2)
print("-" * 50)

# 2. Calculate the squared difference between the two series
# This performs element-wise subtraction and then squares each result.
squared_difference = (series1 - series2) ** 2
print("Squared Differences:")
print(squared_difference)
print("-" * 50)

# 3. Sum the squared differences
# The .sum() method efficiently adds up all the values in the new Series.
sum_of_squared_differences = squared_difference.sum()
print(f"Sum of Squared Differences: {sum_of_squared_differences:.2f}")
print("-" * 50)

# 4. Compute the final Euclidean distance
# The Euclidean distance is the square root of the sum of the squared differences.
# We use numpy's sqrt function for this.
euclidean_distance = np.sqrt(sum_of_squared_differences)
print(f"Euclidean Distance: {euclidean_distance:.2f}")