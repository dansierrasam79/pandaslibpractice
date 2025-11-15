import pandas as pd
import numpy as np

# 1. Create a sample Pandas Series with numerical data
# We'll use a range of numbers to clearly demonstrate the statistical measures.
print("Original Series:")
series_data = pd.Series([1, 5, 8, 10, 15, 20, 25, 30, 35, 40, 50, 60, 75, 90, 100])
print(series_data)
print("-" * 40)

# 2. Compute the minimum, quartiles, and maximum using the describe() method
# The describe() method provides a summary of the central tendency, dispersion, and shape of a Series.
# It automatically includes the min, max, median (50th percentile), and quartiles (25th and 75th percentiles).
# The output is a new Series containing the statistical summary.
statistical_summary = series_data.describe()

# 3. Print the results
print("Statistical summary of the Series:")
print(statistical_summary)