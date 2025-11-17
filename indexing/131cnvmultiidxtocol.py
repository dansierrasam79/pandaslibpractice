import pandas as pd
import io

def convert_multiindex_to_columns(data_string: str) -> pd.DataFrame:
    """
    Creates a MultiIndex DataFrame, then converts specific index levels 
    (1st and 3rd) back into data columns.
    
    Args:
        data_string: String containing the raw data.
        
    Returns:
        The DataFrame after resetting the specified index levels.
    """
    
    # Define the column names for the raw data
    columns = ['student_id', 'class', 'name', 'date_of_birth', 'age', 'street', 't_id']
    
    # 1. Read the data, ensuring it's treated as space-separated
    df = pd.read_csv(io.StringIO(data_string), 
                      sep='\s+', 
                      header=None, 
                      names=columns, 
                      index_col=False)

    # 2. Create the MultiIndex: Indexing by 'student_id', 'class', and 'name'
    # The levels are: 
    # 0: student_id
    # 1: class
    # 2: name
    df_multi = df.set_index(['student_id', 'class', 'name', 'date_of_birth'])
    
    print("Original MultiIndex DataFrame:")
    print(df_multi)
    print("-" * 50)
    
    # 3. Use reset_index() to convert the 1st (index 0) and 3rd (index 2) levels
    #    back into columns.
    # Level 0 = 'student_id'
    # Level 2 = 'name'
    df_converted = df_multi.reset_index(level=[0, 2])
    
    return df_converted

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
df_final = convert_multiindex_to_columns(data)

print("\nDataFrame after converting 1st (student_id) and 3rd (name) Index Levels to Columns:")
print(df_final)
print("-" * 50)
print("Remaining Index Levels:")
print(df_final.index.names)