import pandas as pd
import numpy as np

# -------------------------------------------------------------
# PART 1: Basic .loc on a Simple DataFrame
# -------------------------------------------------------------

# Create a sample DataFrame with named row indices (Cities)
data = {
    'Q1_Revenue': [1000, 1500, 2000, 1200, 1800],
    'Q2_Revenue': [1100, 1600, 2100, 1300, 1900],
    'Units_Sold': [50, 60, 75, 55, 70]
}
index_labels = ['Dallas', 'Boston', 'Seattle', 'Miami', 'Chicago']
df = pd.DataFrame(data, index=index_labels)

print("--- 1. Original DataFrame ---")
print(df)
print("-" * 50)

# --- A. Selecting a single row by label ---
# Syntax: df.loc[row_label]
print("--- 2. Select data for 'Seattle' (single row) ---")
print(df.loc['Seattle'])
print("-" * 50)

# --- B. Selecting multiple rows by list ---
# Syntax: df.loc[[list_of_row_labels]]
print("--- 3. Select data for 'Dallas' and 'Chicago' ---")
print(df.loc[['Dallas', 'Chicago']])
print("-" * 50)

# --- C. Selecting rows and columns simultaneously ---
# Syntax: df.loc[row_label_or_list, column_label_or_list]
print("--- 4. Select Q1_Revenue for 'Boston' and 'Miami' ---")
print(df.loc[['Boston', 'Miami'], 'Q1_Revenue'])
print("-" * 50)

# --- D. Label-based slicing (rows are INCLUSIVE) ---
# Slicing from 'Boston' to 'Miami' *includes* both rows.
print("--- 5. Select rows from 'Boston' to 'Miami' and columns Q1/Q2 ---")
print(df.loc['Boston':'Miami', ['Q1_Revenue', 'Q2_Revenue']])
print("-" * 50)

# -------------------------------------------------------------
# PART 2: Advanced .loc on a MultiIndex DataFrame
# -------------------------------------------------------------

# Create a MultiIndex DataFrame
index_tuples = [
    ('Q1', 'East', 'New York'),
    ('Q1', 'West', 'Los Angeles'),
    ('Q2', 'East', 'Boston'),
    ('Q2', 'West', 'Seattle'),
]
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Quarter', 'Region', 'City'])
data_multi = {'Sales': np.random.randint(500, 900, size=len(multi_index))}
df_multi = pd.DataFrame(data_multi, index=multi_index).sort_index()

print("--- 6. MultiIndex DataFrame ---")
print(df_multi)
print("-" * 50)

# --- E. Selecting all data from the highest level (Quarter) ---
# Syntax: df_multi.loc[level_1_label]
print("--- 7. Select all data for Quarter 'Q1' ---")
print(df_multi.loc['Q1'])
print("-" * 50)

# --- F. Selecting across multiple levels using tuples ---
# Syntax: df_multi.loc[(level_1_label, level_2_label)]
print("--- 8. Select data for Quarter 'Q2' in the 'East' Region ---")
print(df_multi.loc[('Q2', 'East')])
print("-" * 50)