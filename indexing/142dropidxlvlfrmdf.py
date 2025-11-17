import pandas as pd

def drop_column_index_level(df: pd.DataFrame, level_to_drop: int) -> pd.DataFrame:
    """
    Drops a specified level from the DataFrame's MultiIndex columns.

    Args:
        df: The input DataFrame with MultiIndex columns.
        level_to_drop: The index (0 for top, 1 for next, etc.) or name of the level to drop.

    Returns:
        A new DataFrame with the specified column index level removed.
    """
    print(f"\n--- Dropping column index level: {level_to_drop} ---")
    
    # The droplevel() method removes the specified level from the index/columns.
    # axis=1 ensures we operate on the columns.
    df_single_level = df.columns.droplevel(level=level_to_drop)
    
    # Assign the new, single-level columns back to the DataFrame
    df.columns = df_single_level
    
    return df

# --- 1. Setup: Create a DataFrame with a MultiIndex Column ---

# Define the MultiIndex structure
column_index = pd.MultiIndex.from_tuples([
    ('Financial', 'Revenue'),
    ('Financial', 'Cost'),
    ('Personnel', 'Headcount'),
    ('Personnel', 'Location')
], names=['Category', 'Metric'])

# Create the DataFrame
data = {
    ('Financial', 'Revenue'): [100000, 120000, 95000],
    ('Financial', 'Cost'): [45000, 50000, 40000],
    ('Personnel', 'Headcount'): [150, 165, 140],
    ('Personnel', 'Location'): ['NY', 'SF', 'TX']
}
df_multi = pd.DataFrame(data, index=['Q1', 'Q2', 'Q3'])
df_multi.columns = column_index # Apply the MultiIndex to columns

print("--- Original DataFrame with MultiIndex Columns (Levels: 0=Category, 1=Metric) ---")
print(df_multi)
print("\nColumn Index Structure:")
print(df_multi.columns)
print("-" * 70)


# --- 2. Execution: Drop the top level (Level 0, named 'Category') ---

# We can specify the level by its index (0) or its name ('Category')
df_single_level = drop_column_index_level(df_multi.copy(), level_to_drop=0)

print("\n--- Resulting DataFrame with Level 0 ('Category') Dropped ---")
print(df_single_level)
print("\nNew Column Index Structure:")
print(df_single_level.columns)
print("-" * 70)

# Optional Example: Dropping the bottom level (Level 1, named 'Metric') instead
df_alt_single_level = drop_column_index_level(df_multi.copy(), level_to_drop='Metric')

print("\n--- Alternative Result: Dropping Level 1 ('Metric') ---")
print(df_alt_single_level)
print("\nNew Column Index Structure:")
print(df_alt_single_level.columns)