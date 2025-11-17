import pandas as pd
import numpy as np

# --- 1. Setup: Create a MultiIndex DataFrame ---

# Define the index levels
index_tuples = [
    ('Q1', 'North'), ('Q1', 'South'),
    ('Q2', 'North'), ('Q2', 'South'),
    ('Q3', 'North'), ('Q3', 'South'),
    ('Q4', 'North'), ('Q4', 'South'),
]
row_index = pd.MultiIndex.from_tuples(index_tuples, names=['Quarter', 'Region'])

# Sample data
data = {
    'Revenue_M': [10.5, 8.2, 12.1, 9.5, 11.8, 7.9, 15.0, 10.3],
    'Employees': [120, 95, 130, 105, 125, 100, 140, 110],
    'Status': ['Good', 'OK', 'Excellent', 'Good', 'Good', 'OK', 'Excellent', 'Excellent']
}

df = pd.DataFrame(data, index=row_index)

print("--- Original MultiIndex DataFrame ---")
print(df)
print("-" * 60)


# --- 2. Filtering by Standard Column (e.g., 'Status') ---

# Find rows where 'Status' is 'Excellent'
filter_status = df['Status'] == 'Excellent'
df_filtered_status = df[filter_status]

print("\n--- Filter 1: Rows where 'Status' is 'Excellent' ---")
print(df_filtered_status)
print("-" * 60)


# --- 3. Filtering by MultiIndex Level (using IndexSlice) ---

# We want to select all data for 'Q3' regardless of the Region.
# pd.IndexSlice allows us to specify criteria for specific levels.
idx = pd.IndexSlice

# Select all rows where the first level ('Quarter') is 'Q3'
# The syntax (['Q3', :]) means:
# - Level 1 ('Quarter') must equal 'Q3'
# - Level 2 ('Region') can be anything (represented by :)
df_filtered_level = df.loc[idx['Q3', :], :]

print("\n--- Filter 2: Rows where MultiIndex 'Quarter' is 'Q3' ---")
print(df_filtered_level)
print("-" * 60)


# --- 4. Filtering by Multiple MultiIndex Levels (Complex Filter) ---

# We want to select data for 'Q1' AND where 'Region' is 'South'.
df_filtered_complex = df.loc[idx['Q1', 'South'], :]

print("\n--- Filter 3: Rows where Quarter is 'Q1' AND Region is 'South' ---")
print(df_filtered_complex)
print("-" * 60)