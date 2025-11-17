import pandas as pd

def insert_new_column(df: pd.DataFrame, position: int, column_name: str, values: list) -> pd.DataFrame:
    """
    Inserts a new column into the DataFrame at a specified integer position.

    Args:
        df: The DataFrame to modify.
        position: The zero-based integer index where the column should be inserted.
        column_name: The name of the new column (a string).
        values: The data for the new column (must match the length of the DataFrame).

    Returns:
        The modified DataFrame (Note: df.insert() modifies the DataFrame in-place).
    """
    print(f"\n--- Inserting column '{column_name}' at position {position} ---")
    
    # df.insert() modifies the DataFrame IN-PLACE (no need to reassign)
    # allow_duplicates=False (default) prevents accidental duplication of column names.
    df.insert(
        loc=position,        # The zero-based index where the column goes (e.g., 0 for first, 1 for second)
        column=column_name,  # The name of the new column
        value=values         # The data for the new column
    )
    
    return df

# --- 1. Setup: Create a Sample DataFrame ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['London', 'Paris', 'Tokyo', 'Berlin']
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("\nOriginal Columns:", df.columns.tolist())
print("-" * 50)


# --- 2. Execution: Insert a column at index 1 (between Name and Age) ---
new_ratings = [4.5, 3.9, 4.8, 4.1]
# We want this to be the SECOND column, so index position is 1
df_modified = insert_new_column(
    df=df, 
    position=1, 
    column_name='Rating', 
    values=new_ratings
)

print("\n--- Resulting DataFrame ---")
print(df_modified)
print("\nNew Columns:", df_modified.columns.tolist())