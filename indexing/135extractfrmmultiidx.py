import pandas as pd
import io

# Define the column names for the raw data
COLUMNS = ['student_id', 'class', 'name', 'date_of_birth', 'age', 'street', 't_id']

def extract_from_multiindex(data_string: str):
    """
    Creates a MultiIndex DataFrame and demonstrates single row, multiple row, 
    and specific scalar value extraction.
    """
    
    # 1. Read the data
    df = pd.read_csv(io.StringIO(data_string), 
                      sep='\s+', 
                      header=None, 
                      names=COLUMNS, 
                      index_col=False)

    # 2. Create the MultiIndex: (student_id, class, name)
    # Level 0: student_id, Level 1: class, Level 2: name
    index_levels = ['student_id', 'class', 'name']
    df_multi = df.set_index(index_levels)
    
    print("Original MultiIndex DataFrame:")
    print(df_multi)
    print("\nIndex Levels:", df_multi.index.names)
    print("-" * 60)
    
    # --- A. Extract a Single Row ---
    # We use a complete tuple corresponding to the index levels: 
    # (student_id, class, name)
    single_row_tuple = ('s003', 'VI', 'Ryan Parkes')
    
    print(f"1. Single Row Extraction (Index: {single_row_tuple}):")
    try:
        single_row = df_multi.loc[single_row_tuple]
        print(single_row)
    except KeyError:
        print(f"Error: Row index {single_row_tuple} not found.")
    print("-" * 60)

    # --- B. Extract Multiple Rows using Partial Indexing ---
    # We can use a single label to select all rows belonging to the top level ('s001')
    
    print("2. Multiple Rows Extraction (Top Level 's001'):")
    try:
        multiple_rows = df_multi.loc['s001']
        print(multiple_rows)
        print("\nNote: The 'student_id' index level is automatically dropped in the result.")
    except KeyError:
        print("Error: Top level index 's001' not found.")
    print("-" * 60)

    # --- C. Extract a Specific Scalar Value ---
    # We use the full index tuple and the desired column name.
    
    value_index_tuple = ('s002', 'V', 'Gino Mcneill')
    column_name = 'age'
    
    # To get the 31-year-old entry for s002, we need its specific date_of_birth entry
    # The data shows 's002', 'V', 'Gino Mcneill' appears twice. We must specify the full index tuple.
    
    # Selecting the first occurrence (index 1 in original data)
    target_value_row = ('s002', 'V', 'Gino Mcneill')
    
    print(f"3. Specific Scalar Value Extraction (Index: {target_value_row}, Column: '{column_name}'):")
    
    # Since the index values repeat, we look for the first instance
    # Pandas will return the first match for the partial index.
    # To demonstrate selection of a specific unique row, let's use the unique index ('s003', 'VI', 'Ryan Parkes')
    scalar_index = ('s003', 'VI', 'Ryan Parkes')
    
    try:
        specific_age = df_multi.loc[scalar_index, 'age']
        print(f"Value at {scalar_index} in column 'age': {specific_age}")
    except KeyError:
        print(f"Error: Could not find scalar value at index {scalar_index}.")
    print("-" * 60)
    
# --- Test Data Setup ---
data = """
0        s001     V  Alberto Franco     15/05/2002      35  street1   t1
1        s002     V    Gino Mcneill     17/05/2002      32  street2   t2
2        s003    VI     Ryan Parkes     16/02/1999      33  street3   t3
3        s001    VI    Eesha Hinton     25/09/1998      30  street1   t4
4        s002     V    Gino Mcneill     11/05/2002      31  street2   t5
5        s004    VI    David Parkes     15/09/1997      32  street4   t6
"""

# --- Execution ---
if __name__ == "__main__":
    extract_from_multiindex(data)