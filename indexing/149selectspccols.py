import pandas as pd
import numpy as np

# --- 1. Setup: Create a DataFrame with multiple columns ---
data = {
    'X': [10, 20, 30, 40, 50],
    'Y': [1.5, 2.5, 3.5, 4.5, 5.5],
    'Z': ['A', 'B', 'C', 'D', 'E'],
    'W': [100, 90, 80, 70, 60]
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("-" * 30)


# --- 2. Column Selection Logic ---

# To select multiple columns, pass a Python list containing the names
# of the desired columns into the DataFrame's indexing operator ([]).
columns_to_select = ['X', 'Y']
df_selected = df[columns_to_select]


# --- 3. Output the Result ---
print("\n--- DataFrame with only 'X' and 'Y' columns ---")
print(df_selected)