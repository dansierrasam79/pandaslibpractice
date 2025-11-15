import pandas as pd

# Sample dictionary
data = {"a": 100, "b": 200, "c": 300, "d": 400, "e": 500}

print("Dictionary:")
print(data)

# Convert dictionary to Pandas Series
series = pd.Series(data)

print("\nConverted Pandas Series:")
print(series)