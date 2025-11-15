import pandas as pd

# 1. Create two identical Series
print("Series 1 (identical):")
series1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(series1)
print("-" * 50)

print("Series 2 (identical):")
series2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(series2)
print("-" * 50)

# 2. Check for full equality using the .equals() method
# This method checks if the values AND the indices are the same.
# It is the most robust way to check for equality.
are_equal_method = series1.equals(series2)
print(f"Are Series 1 and Series 2 equal? (using .equals()): {are_equal_method}")
print("-" * 50)

# 3. Create a third Series with a different value
print("Series 3 (different value):")
series3 = pd.Series([10, 20, 99, 40], index=['a', 'b', 'c', 'd'])
print(series3)
print("-" * 50)

# 4. Create a fourth Series with a different index
print("Series 4 (different index):")
series4 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'x', 'd'])
print(series4)
print("-" * 50)

# 5. Check for equality against the other Series
print(f"Are Series 1 and Series 3 equal? (using .equals()): {series1.equals(series3)}")
print(f"Are Series 1 and Series 4 equal? (using .equals()): {series1.equals(series4)}")
print("-" * 50)

# 6. Use a direct comparison for element-wise equality
# A direct comparison (e.g., `series1 == series2`) returns a boolean Series
# indicating whether each element is equal. This is different from the overall equality check.
element_wise_comparison = series1 == series2
print("Element-wise comparison of Series 1 and Series 2:")
print(element_wise_comparison)