import pandas as pd
import numpy as np

# --- 1. Create a Sample DataFrame ---
data = {
    'Product': [f'Item {i+1}' for i in range(8)],
    'Rating': [3.8, 4.5, 3.1, 4.9, 4.1, 2.5, 4.7, 3.9],
    'Price': [12.50, 35.99, 5.00, 99.99, 18.25, 1.99, 75.00, 15.00]
}
df = pd.DataFrame(data)
df.index.name = 'ProductID'

print("--- Original DataFrame ---")
print(df)
print("-" * 40)

# --- 2. Define the Condition (Boolean Mask) ---
# We want to select products with a Rating greater than 4.0
rating_condition = df['Rating'] > 4.0

# --- 3. Use .loc to Filter Rows Based on the Condition ---
# Syntax: df.loc[row_condition, column_labels]
# Using the ':' for the columns selects ALL columns.
df_highly_rated = df.loc[rating_condition, :]

print("\n--- Filtered DataFrame (Rating > 4.0 using .loc) ---")
print(df_highly_rated)
print("-" * 40)

# --- 4. Advanced Example: Combined Condition and Column Subset ---
# Select products with Rating > 4.0 AND Price < 50, but only show 'Product' and 'Rating'.
combined_condition = (df['Rating'] > 4.0) & (df['Price'] < 50.00)

df_subset = df.loc[combined_condition, ['Product', 'Rating']]

print("\n--- Filtered Subset (Rating > 4.0 AND Price < 50) ---")
print(df_subset)