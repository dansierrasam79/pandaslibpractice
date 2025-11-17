import pandas as pd
import numpy as np

# --- 1. Setup: Create a DataFrame with Missing Data (NaN) ---
data = {
    'A': [10, 20, np.nan, 40, 50],
    'B': ['x', 'y', 'z', np.nan, 'w'],
    'C': [1.1, 2.2, 3.3, 4.4, np.nan],
    'D': [100, 200, 300, 400, 500]
}

# The default Pandas index is 0, 1, 2, 3, 4
df = pd.DataFrame(data)

# Introduce a different index (to show the result is the integer row position,
# not the custom label, though it works for both)
# df = pd.DataFrame(data, index=['row_a', 'row_b', 'row_c', 'row_d', 'row_e'])


print("--- Original DataFrame ---")
print(df)
print("-" * 50)


# --- 2. Logic: Finding Row Indices with Missing Data ---

# Step 1: Check for missing values across the whole DataFrame.
# df.isnull() returns a DataFrame of booleans (True where missing).
missing_mask_df = df.isnull()

# Step 2: Check if ANY column in the row has a missing value.
# .any(axis=1) returns a Series of booleans, True if at least one column is True (NaN).
has_missing_data_series = missing_mask_df.any(axis=1)

# Step 3: Get the Index where the Series is True.
# The .index property of the resulting filtered DataFrame/Series gives the row labels.
# Since we used the default integer index (0, 1, 2, 3, 4), the result is the integer index.
indices_with_nan = df[has_missing_data_series].index.tolist()

print(f"Indices of rows containing missing data: {indices_with_nan}")
print("-" * 50)

# --- 3. Verification (Optional) ---
# Display the rows that were found to contain NaN
print("--- Rows with Missing Data (Verification) ---")
for index in indices_with_nan:
    print(f"Index {index}:\n{df.loc[index]}\n")