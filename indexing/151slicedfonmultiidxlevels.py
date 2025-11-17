import pandas as pd
import numpy as np

# --- 1. Setup: Create a DataFrame with a 3-Level MultiIndex ---

# Define the levels for the hierarchical index
index_tuples = [
    ('Q1', 'East', 'New York'),
    ('Q1', 'West', 'Los Angeles'),
    ('Q2', 'East', 'Boston'),
    ('Q2', 'West', 'Seattle'),
    ('Q3', 'East', 'New York'),
    ('Q3', 'West', 'Los Angeles'),
]
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Quarter', 'Region', 'City'])

# Create data (random sales figures)
data = {
    'Revenue': np.random.randint(1000, 5000, size=len(multi_index)),
    'Units Sold': np.random.randint(50, 200, size=len(multi_index))
}
df = pd.DataFrame(data, index=multi_index)

# IMPORTANT: Always sort the index before slicing for reliable results
df = df.sort_index()

print("--- Original DataFrame (Sorted MultiIndex) ---")
print(df)
print("-" * 60)

# Initialize pd.IndexSlice for cleaner, more flexible slicing
# This is the recommended way to slice inner index levels.
idx = pd.IndexSlice

# --- 2. Slicing Operations using .loc ---

## A. Slicing the Outer Level (Level 0)
print("\n1. Slicing by the Outer Level ('Quarter 2' only):")
# Pass the desired index value directly to .loc
df_q2 = df.loc['Q2']
print(df_q2)
print("-" * 60)


## B. Slicing an Inner Level across ALL values of the Outer Level
print("\n2. Slicing an Inner Level (Region='East') across all quarters:")
# Syntax: df.loc[idx[<Level 0>, <Level 1>, <Level 2>], <Columns>]
# slice(None) or ':' acts as a wildcard for that index level
df_east_all = df.loc[idx[:, 'East', :], :]
print(df_east_all)
print("-" * 60)


## C. Slicing the Deepest Level
print("\n3. Slicing the Deepest Level (City='New York') across all quarters and regions:")
# Using slice(None) for the Quarter and Region levels
df_ny_all = df.loc[idx[:, :, 'New York'], :]
print(df_ny_all)
print("-" * 60)


## D. Slicing a Specific Intersection
print("\n4. Slicing a specific intersection (Quarter 3, Region West):")
# Targeting Q3 in Level 0 and 'West' in Level 1
df_q3_west = df.loc[idx['Q3', 'West', :], :]
print(df_q3_west)
print("-" * 60)


## E. Slicing a Range of Quarters and a specific Column
print("\n5. Slicing a Range of Levels (Q1 through Q2) and selecting only 'Units Sold':")
# This shows how to slice a range of values in the outer index ('Q1':'Q2')
# and simultaneously select a specific column.
df_q1_to_q2_units = df.loc[idx['Q1':'Q2', :, :], 'Units Sold']
print(df_q1_to_q2_units)