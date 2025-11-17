import pandas as pd
import numpy as np

# --- 1. Create a Sample DataFrame ---
# Create 10 rows of data
data = {
    'Product': [f'P{i+1}' for i in range(10)],
    'Price': np.random.randint(10, 100, size=10),
    'Stock': np.random.randint(0, 50, size=10)
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("--- Original DataFrame (10 rows) ---")
print(df)
print("-" * 40)

# --- 2. Select the First Three Rows using .iloc ---
# .iloc uses standard Python slicing conventions: [start:stop]
# The 'stop' index (3) is exclusive, so it selects indices 0, 1, and 2.
first_three_rows = df.iloc[0:3]

print("\n--- Filtered DataFrame (First 3 Rows using iloc[0:3]) ---")
print(first_three_rows)
print("-" * 40)

# --- 3. Alternative concise way to select first N rows ---
# Although iloc works, the .head() method is the most idiomatic way
# to select the first N rows in Pandas.
first_three_rows_head = df.head(3)

print("\n--- Comparison: Same result using the idiomatic .head(3) method ---")
print(first_three_rows_head)