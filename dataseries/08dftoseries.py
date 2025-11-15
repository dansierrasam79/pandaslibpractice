import pandas as pd

# Create a sample DataFrame
data = {
    "col1": [10, 20, 30, 40, 50],
    "col2": [100, 200, 300, 400, 500],
    "col3": [1000, 2000, 3000, 4000, 5000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Convert first column to Series
first_col_series = df.iloc[:, 0]   # Using iloc (0 = first column)

print("\nFirst column as Pandas Series:")
print(first_col_series)

print("\nType of object:", type(first_col_series))