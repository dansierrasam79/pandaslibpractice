import pandas as pd

# --- 1. Create a Sample DataFrame ---
data = {
    'ID': list(range(1, 11)),
    'X': [3, 8, 6, 1, 9, 5, 7, 2, 10, 4],  # Values for X
    'Y': [7, 3, 5, 2, 6, 4, 1, 8, 0, 9],  # Values for Y
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A']
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("-" * 50)

# --- 2. Define the Combined Conditional Filter ---
# Condition 1: Column 'X' must be greater than 5 (df['X'] > 5)
# Condition 2: Column 'Y' must be less than 5 (df['Y'] < 5)
# Use the bitwise AND operator (&) to combine the two boolean series.
# The entire combined condition must be enclosed in parentheses.

condition_X = df['X'] > 5
condition_Y = df['Y'] < 5

# The result is a single Boolean Series
combined_filter = (condition_X) & (condition_Y)

# --- 3. Apply the Filter to Select Rows ---
# Pass the combined Boolean Series directly to the DataFrame
filtered_df = df[combined_filter]


# --- 4. Display the Result ---
print("\n--- Filtered DataFrame (X > 5 AND Y < 5) ---")
print(filtered_df)
print("-" * 50)

# You can also do this in one line:
# filtered_df_oneline = df[(df['X'] > 5) & (df['Y'] < 5)]