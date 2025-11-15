import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1]
}
df = pd.DataFrame(data)

# Create a Series with the same index
s = pd.Series([1, 2, 3, 0], index=[0, 1, 2, 3])

print("Original DataFrame:")
print(df)

print("\nOriginal Series:")
print(s)

# Check inequality over the index axis
result = df.ne(s, axis=0)

print("\nInequality (df != s) over index axis:")
print(result)
