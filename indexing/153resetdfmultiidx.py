import pandas as pd
import numpy as np

# --- 1. Setup: Create a DataFrame with a 3-Level MultiIndex ---

index_tuples = [
    ('Q1', 'East', 'New York'),
    ('Q1', 'West', 'Los Angeles'),
    ('Q2', 'East', 'Boston'),
    ('Q2', 'West', 'Seattle'),
]
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Quarter', 'Region', 'City'])

data = {
    'Revenue': np.random.randint(1000, 5000, size=len(multi_index)),
    'Units Sold': np.random.randint(50, 200, size=len(multi_index))
}
df = pd.DataFrame(data, index=multi_index)
df = df.sort_index()

print("--- Original DataFrame (MultiIndex) ---")
print(df)
print(f"\nIndex Type: {type(df.index)}")
print("-" * 60)

# --- 2. Action A: Resetting the ENTIRE MultiIndex ---
# All index levels ('Quarter', 'Region', 'City') become new columns.
# A default integer index is assigned to the DataFrame.

df_reset_all = df.reset_index()

print("\n--- DataFrame after reset_index() (All levels become columns) ---")
print(df_reset_all)
print(f"\nIndex Type: {type(df_reset_all.index)}")
print("-" * 60)

# --- 3. Action B: Resetting a SPECIFIC Index Level ---
# We use the 'level' parameter to specify which index level(s) to reset.
# Goal: Convert only the 'City' level back into a column.

df_reset_city = df.reset_index(level='City')
df_reset_city = df_reset_city.sort_index() # Re-sort the remaining index levels

print("\n--- DataFrame after reset_index(level='City') ---")
print("Only 'City' is now a column; 'Quarter' and 'Region' remain in the MultiIndex.")
print(df_reset_city)
print(f"\nIndex Type: {type(df_reset_city.index)}")
print("-" * 60)