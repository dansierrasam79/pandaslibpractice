import pandas as pd

# --- 1. Create a MultiIndex DataFrame ---

# Define the index levels
index_tuples = [
    ('East', 'Boston'), ('East', 'New York'), 
    ('West', 'LA'), ('West', 'Seattle'), 
    ('Central', 'Chicago'), ('Central', 'Houston')
]
multi_index = pd.MultiIndex.from_tuples(
    index_tuples, 
    names=['Region', 'City']
)

# Define the data
data = {
    'Sales': [1000, 1500, 2200, 1100, 950, 1800],
    'Profit': [150, 250, 400, 180, 120, 300],
    'Target_Hit': [True, True, False, True, False, True]
}

df_multi = pd.DataFrame(data, index=multi_index)

print("--- Original MultiIndex DataFrame ---")
print(df_multi)
print("-" * 60)


# --- 2. Basic Slicing: Selecting a single top-level Index ---

# Select all rows where the 'Region' (Level 0) is 'East'
slice_1 = df_multi.loc['East']

print("\n--- Slice 1: Select only 'East' Region (Top Level) ---")
print(slice_1)
print("-" * 60)


# --- 3. Selecting Specific Inner Index Value (Two Levels) ---

# Select the specific row for 'West' Region and 'Seattle' City
# This requires passing a tuple to the row selector
slice_2 = df_multi.loc[('West', 'Seattle')]

print("\n--- Slice 2: Select specific row ('West', 'Seattle') ---")
print(slice_2)
print("-" * 60)


# --- 4. Slicing with Ranges and Specific Columns ---

# Goal: Select all cities in the 'West' and 'Central' regions, 
# and only show the 'Sales' and 'Target_Hit' columns.

# Note: Label slicing is inclusive, so 'West':'Central' includes both.
slice_3 = df_multi.loc['West':'Central', ['Sales', 'Target_Hit']]

print("\n--- Slice 3: Select Region range ('West' to 'Central') and specific columns ---")
print(slice_3)
print("-" * 60)


# --- 5. Advanced Slicing: Selecting a range of Inner Index values for ALL outer levels ---

# If you wanted to select all data where the city is 'Boston' or 'LA' for example, 
# you would generally use boolean indexing, but for slicing across columns or other
# complex selections, the `pd.IndexSlice` object is helpful.

# Using a tuple to slice across multiple levels simultaneously:
# Select rows: East and West regions
# Select columns: 'Sales' and 'Profit'
idx = pd.IndexSlice
slice_4 = df_multi.loc[idx[['East', 'West'], :], ['Sales', 'Profit']]

print("\n--- Slice 4: Select 'East' and 'West' Regions, all Cities, and 'Sales'/'Profit' columns ---")
print(slice_4)
print("-" * 60)