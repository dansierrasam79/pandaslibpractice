import pandas as pd
import io

def extract_elements_by_position(data_string: str):
    """
    Creates a DataFrame and demonstrates extracting elements using integer 
    positional indices along both axis 0 (rows) and axis 1 (columns) using df.take().
    """
    
    # Define the data structure
    COLUMNS = ['Name', 'Score_A', 'Score_B', 'Score_C']

    # 1. Read the data
    df = pd.read_csv(io.StringIO(data_string), 
                      sep=',', 
                      header=None, 
                      names=COLUMNS, 
                      index_col=False)

    # Set 'Name' as the index for clarity, but positional indexing ignores index labels.
    df = df.set_index('Name')
    
    print("--- 1. Original DataFrame (5 rows, 3 data columns) ---")
    print("Positional Index (Row) -> [0, 1, 2, 3, 4]")
    print("Positional Index (Column) -> [0, 1, 2]")
    print(df)
    print("-" * 70)
    
    # --- A. Extract Rows by Position (Axis 0) ---
    # We want rows at integer positions 0 (Alice), 3 (David), and 1 (Bob).
    row_positions = [0, 3, 1]
    
    # Use df.take(indices, axis=0) to select rows
    df_rows_extracted = df.take(row_positions, axis=0)
    
    print(f"--- 2. Extract Rows at Positions {row_positions} (axis=0) ---")
    print("The resulting order matches the requested index order:")
    print(df_rows_extracted)
    print("-" * 70)

    # --- B. Extract Columns by Position (Axis 1) ---
    # We want columns at integer positions 2 (Score_C) and 0 (Score_A).
    column_positions = [2, 0]
    
    # Use df.take(indices, axis=1) to select columns
    df_cols_extracted = df.take(column_positions, axis=1)
    
    print(f"--- 3. Extract Columns at Positions {column_positions} (axis=1) ---")
    print("Note the columns are reordered to [Score_C, Score_A]:")
    print(df_cols_extracted)
    print("-" * 70)


# --- Test Data Setup ---
data = """
Alice,88,92,95
Bob,75,80,65
Charlie,90,91,90
David,60,70,80
Eve,99,98,99
"""

# --- Execution ---
if __name__ == "__main__":
    extract_elements_by_position(data)