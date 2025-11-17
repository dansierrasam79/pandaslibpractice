import pandas as pd
import numpy as np

# --- 1. Setup: Create a DataFrame with a 3-Level MultiIndex ---

# Define the levels for the hierarchical index: (Quarter, Region, City)
index_tuples = [
    ('Q1', 'East', 'New York'),
    ('Q1', 'West', 'Los Angeles'),
    ('Q2', 'East', 'Boston'),
    ('Q2', 'West', 'Seattle'),
]
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Quarter', 'Region', 'City'])

# Create data
data = {
    'Revenue': np.random.randint(1000, 5000, size=len(multi_index)),
    'Expense': np.random.randint(500, 2500, size=len(multi_index))
}
df = pd.DataFrame(data, index=multi_index)
df = df.sort_index()

print("--- Original DataFrame (Index: Quarter, Region, City) ---")
print(df)
print("-" * 60)

# --- 2. Method A: Swapping Adjacent Levels using swaplevel() ---
# Goal: Swap 'Quarter' (Level 0) with 'Region' (Level 1)
# Resulting Index Order: (Region, Quarter, City)

df_swapped_a = df.swaplevel(i='Quarter', j='Region', axis=0)
# Note: It's good practice to sort the index after a swap
df_swapped_a = df_swapped_a.sort_index()

print("\n--- DataFrame after swaplevel('Quarter', 'Region') ---")
print("New Index Order: (Region, Quarter, City)")
print(df_swapped_a)
print("-" * 60)


# --- 3. Method B: Reordering All Levels using reorder_levels() ---
# Goal: Change the index order to (City, Region, Quarter)
# This is useful when moving a level across multiple other levels.

# New level names in the desired order
new_order = ['City', 'Region', 'Quarter']
df_reordered_b = df.reorder_levels(new_order, axis=0)
df_reordered_b = df_reordered_b.sort_index()

print("\n--- DataFrame after reorder_levels(['City', 'Region', 'Quarter']) ---")
print("New Index Order: (City, Region, Quarter)")
print(df_reordered_b)
print("-" * 60)