import pandas as pd
import io

def construct_series_from_multiindex(data_string: str):
    """
    Constructs a Series using a DataFrame's MultiIndex levels as the 
    new Series Index and Column (value).
    """
    
    # Define the column names for the raw data
    columns = ['student_id', 'class', 'name', 'date_of_birth', 'age', 'street', 't_id']
    
    # 1. Read the data
    df = pd.read_csv(io.StringIO(data_string), 
                      sep='\s+', 
                      header=None, 
                      names=columns, 
                      index_col=False)

    # 2. Create the MultiIndex (Levels 0, 1, 2, 3)
    # The structure will be: (student_id, class, name, date_of_birth) -> [age, street, t_id]
    df_multi = df.set_index(['student_id', 'class', 'name', 'date_of_birth'])
    
    print("Original MultiIndex DataFrame Structure:")
    print(df_multi.head())
    print("-" * 70)
    
    # 3. Unstack one level to transform it into a column header.
    # We choose to unstack the *innermost* index level: 'date_of_birth' (Level 3).
    # This pivots the index 'date_of_birth' into columns, leaving the other three 
    # levels as a MultiIndex on the rows, and the existing columns ('age', 'street', 't_id')
    # are now a secondary column index.
    df_unstacked = df_multi.unstack(level='date_of_birth')

    # 4. Select a specific column from the unstacked DataFrame to form the final Series.
    # We select the 'age' column. The result is a Series with a MultiIndex 
    # (student_id, class, name) and 'date_of_birth' labels as the final column.
    
    # Note: Selecting a single top-level column ('age') produces a DataFrame.
    # We must select the specific date of birth as the final value we want in the Series.
    # A simpler approach is to select just the first inner column.
    
    # Let's simplify the index creation to the 3 levels we want:
    df_short_multi = df.set_index(['student_id', 'class', 'name'])
    
    # Now, we select a value column (e.g., 'date_of_birth') to create the Series.
    # The resulting Series index is (student_id, class, name)
    result_series = df_short_multi['date_of_birth']
    
    return result_series

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
series_final = construct_series_from_multiindex(data)

print("\nResulting Series (Index Levels: student_id, class, name | Values: date_of_birth):")
print(series_final)
print("-" * 70)
print(f"Series Type: {type(series_final)}")
print(f"Index Names: {series_final.index.names}")