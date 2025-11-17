import pandas as pd

# --- 1. Create a Sample DataFrame with Custom Labeled Index ---

data = {
    'Q1_Sales': [100, 150, 120, 210, 90, 180],
    'Q2_Sales': [110, 145, 130, 205, 95, 175],
    'Inventory': [500, 300, 450, 200, 600, 250],
    'Region': ['East', 'West', 'North', 'South', 'East', 'West']
}

# Use a meaningful index for demonstration
index_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
df = pd.DataFrame(data, index=index_labels)
df.index.name = 'Month'

print("--- Original DataFrame (with Labeled Index) ---")
print(df)
print("-" * 50)

# --- 2. Slicing by Row and Column Labels using .loc ---

# Goal: Select data from February ('Feb') up to May ('May'),
# and only include the columns 'Q1_Sales' and 'Inventory'.

# NOTE on slicing with .loc:
# When slicing with labels (e.g., 'Feb':'May'), the end label ('May') is **INCLUSIVE**.
# This is a key difference from standard Python integer slicing.

df_slice = df.loc['Feb':'May', ['Q1_Sales', 'Inventory']]

print("\n--- Slice 1: Feb to May (Inclusive), Q1_Sales and Inventory Columns ---")
print(df_slice)
print("-" * 50)

# --- 3. Selecting Discontinuous Rows and Continuous Columns ---

# Goal: Select only Jan, Mar, and Jun rows, and all columns from 'Q2_Sales' to the end.

df_discontinuous_rows = df.loc[['Jan', 'Mar', 'Jun'], 'Q2_Sales':]

print("\n--- Slice 2: Discontinuous Rows, Columns from Q2_Sales to End (Inclusive) ---")
print(df_discontinuous_rows)
print("-" * 50)