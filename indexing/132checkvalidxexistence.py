import pandas as pd
import io

# Define the column names for the raw data
COLUMNS = ['student_id', 'class', 'name', 'date_of_birth', 'age', 'street', 't_id']

# --- Core Functions ---

def check_value_in_single_index(df: pd.DataFrame, index_label: str, column_name: str):
    """
    Checks if a single specified label exists in a single-level index.
    """
    # Set the specified column as the index
    df_single_index = df.set_index(column_name)
    
    # Use the 'in' operator, which is highly optimized for Pandas Index objects
    exists = index_label in df_single_index.index
    
    print(f"\n--- Checking Single Index (Index Name: '{column_name}') ---")
    print(f"Checking for label '{index_label}': {exists}")

def check_value_in_multi_index(df: pd.DataFrame, index_levels: list, index_tuple: tuple):
    """
    Checks if a full tuple of labels exists in a MultiIndex.
    """
    # Create the MultiIndex
    df_multi_index = df.set_index(index_levels)
    
    # Use the 'in' operator to check for the complete tuple of index values
    exists = index_tuple in df_multi_index.index
    
    print(f"\n--- Checking MultiIndex (Levels: {index_levels}) ---")
    print(f"Checking for tuple {index_tuple}: {exists}")

# --- Test Data Setup ---
data = """
0        s001     V  Alberto Franco     15/05/2002      35  street1   t1
1        s002     V    Gino Mcneill     17/05/2002      32  street2   t2
2        s003    VI     Ryan Parkes     16/02/1999      33  street3   t3
3        s001    VI    Eesha Hinton     25/09/1998      30  street1   t4
4        s002     V    Gino Mcneill     11/05/2002      31  street2   t5
5        s004    VI    David Parkes     15/09/1997      32  street4   t6
"""

# 1. Read the data
df_original = pd.read_csv(io.StringIO(data), 
                  sep='\s+', 
                  header=None, 
                  names=COLUMNS, 
                  index_col=False)

print("Original DataFrame:")
print(df_original)
print("-" * 60)

# --- Execution ---

# 2. Test Case 1: Single Column Index ('student_id')
check_value_in_single_index(
    df=df_original.copy(), 
    column_name='student_id', 
    index_label='s002' # This value exists
)

# Test Case 1b: Value that does not exist
check_value_in_single_index(
    df=df_original.copy(), 
    column_name='student_id', 
    index_label='s999' # This value does NOT exist
)


# 3. Test Case 2: Multiple Column Index (MultiIndex)
check_value_in_multi_index(
    df=df_original.copy(), 
    index_levels=['student_id', 'class', 'name'], 
    index_tuple=('s003', 'VI', 'Ryan Parkes') # This tuple exists
)

# Test Case 2b: Tuple that does not exist
check_value_in_multi_index(
    df=df_original.copy(), 
    index_levels=['student_id', 'class', 'name'], 
    index_tuple=('s002', 'V', 'Alberto Franco') # This combination does NOT exist
)