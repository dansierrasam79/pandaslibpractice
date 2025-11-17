import pandas as pd
import numpy as np

# --- 1. Create a Sample DataFrame ---
data = {
    'x': [5, 7, 3, 9, 6, 10, 4, 8],
    'y': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'z': np.random.rand(8)
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("-" * 40)

# --- 2. Create the Boolean Mask ---
# The expression `df['x'] > 6` generates a Pandas Series of True/False values.
# True for every row where 'x' is greater than 6, False otherwise.
mask = df['x'] > 6

print("\n--- Boolean Mask (df['x'] > 6) ---")
print(mask)
print("-" * 40)

# --- 3. Apply the Mask using Boolean Indexing ---
# Passing the mask Series inside the square brackets selects only the rows
# corresponding to 'True' values in the mask.
df_filtered = df[mask]

print("\n--- Filtered DataFrame (x > 6) ---")
print(df_filtered)
print("-" * 40)

# --- 4. Combining Steps (Most Common Use) ---
# You can combine steps 2 and 3 into a single, concise line:
df_one_liner = df[df['x'] > 6]

print("\n--- Filtered DataFrame (One-Liner) ---")
print(df_one_liner)