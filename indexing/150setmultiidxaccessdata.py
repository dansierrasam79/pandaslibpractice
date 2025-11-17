import pandas as pd
import numpy as np

# --- 1. Setup: Create a DataFrame with a MultiIndex ---

# Define the levels for the hierarchical index: Region and City
index_tuples = [
    ('East', 'New York'), ('East', 'Boston'),
    ('West', 'Los Angeles'), ('West', 'Seattle')
]
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Region', 'City'])

# Create the corresponding data
data = {
    'Sales': [1000, 1500, 2000, 1200],
    'Expenses': [400, 500, 600, 450],
    'Profit': [600, 1000, 1400, 750]
}
df = pd.DataFrame(data, index=multi_index)

print("--- Original DataFrame with MultiIndex ---")
print(df)
print("-" * 50)


# --- 2. Accessing Data by Index Level (loc) ---

print("\n1. Accessing all data for the top-level index 'East':")
# Pass the desired outer index value
df_east = df.loc['East']
print(df_east)
print("-" * 50)

print("\n2. Accessing a specific row combination ('West', 'Los Angeles'):")
# Pass a tuple containing the full index path
df_la = df.loc[('West', 'Los Angeles')]
print(df_la)
print("-" * 50)

print("\n3. Accessing a single cell (Profit for Boston):")
# Accessing both index (row) and column simultaneously
profit_boston = df.loc[('East', 'Boston'), 'Profit']
print(f"Profit for Boston: {profit_boston}")
print("-" * 50)


# --- 4. Advanced Slicing with pd.IndexSlice ---

# pd.IndexSlice is used to make slicing easier and more readable
idx = pd.IndexSlice

print("\n4. Advanced Slicing: Select all cities in 'West' and only the 'Sales' column:")
# Using idx[outer_level, inner_level]
df_west_sales = df.loc[idx['West', :], 'Sales']
print(df_west_sales)
print("-" * 50)

print("\n5. Slicing across inner index levels (New York through Los Angeles):")
# Note: Slicing works best when the index is sorted!
df_slice = df.loc[idx[:, 'New York':'Los Angeles'], :]
print(df_slice)