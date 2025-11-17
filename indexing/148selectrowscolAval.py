import pandas as pd
import numpy as np

# --- 1. Setup: Create a DataFrame ---
data = {
    'A': [1, 5, 3, 8, 2, 7, 4],
    'B': ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta'],
    'C': [100, 200, 300, 400, 500, 600, 700]
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("-" * 30)


# --- 2. Filtering Logic ---

# 1. Create a boolean Series (mask)
# This Series will have 'True' for rows where 'A' > 4 and 'False' otherwise.
boolean_mask = df['A'] > 4

# Optional: You can view the mask to see which rows were selected:
# print("\n--- Boolean Mask ---")
# print(boolean_mask)
# print("-" * 30)

# 2. Use the boolean Series to select the rows
# Passing the mask to the DataFrame returns only the rows where the mask is True.
df_filtered = df[boolean_mask]


# --- 3. Output the Result ---
print("\n--- Filtered DataFrame (Column 'A' > 4) ---")
print(df_filtered)