import pandas as pd
import numpy as np

# --- 1. Create a Sample DataFrame ---
data = {
    'Item': [f'Widget {i+1}' for i in range(10)],
    'Price': [15.99, 55.00, 29.99, 85.50, 4.99, 105.00, 33.30, 75.00, 19.99, 11.50],
    'InStock': [True, True, False, True, True, False, True, True, True, True],
    'Status': ['Regular'] * 10 # Initial status
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("-" * 50)

# --- 2. Conditional Assignment using .loc (Setting a String Value) ---

# Define the condition: Price must be greater than $50
premium_condition = df['Price'] > 50.00

# Use .loc to select the rows matching the condition and set the 'Status' column value
# Syntax: df.loc[row_condition, 'column_label'] = new_value
df.loc[premium_condition, 'Status'] = 'Premium Discount'


# --- 3. Conditional Assignment using .loc (Setting a Numeric Value) ---

# We want to apply a 10% discount to all items marked 'Premium Discount'
discount_condition = df['Status'] == 'Premium Discount'

# Select the rows that match the discount_condition and update their 'Price'
# The assignment must be done on the .loc result to avoid a SettingWithCopyWarning
df.loc[discount_condition, 'Price'] = df['Price'] * 0.90


# --- 4. Print the Modified DataFrame ---
print("\n--- Modified DataFrame (Items > $50 are Discounted by 10%) ---")
print(df)
print("-" * 50)