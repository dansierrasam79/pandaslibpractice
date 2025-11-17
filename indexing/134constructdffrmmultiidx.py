import pandas as pd
import io

def pivot_multiindex_to_dataframe(data_string: str) -> pd.DataFrame:
    """
    Constructs a DataFrame by pivoting one level of a MultiIndex 
    to become the new columns, while the other level remains the index.
    """
    
    # Define the column names for the raw data
    columns = ['student_id', 'class', 'name', 'date_of_birth', 'age', 'street', 't_id']
    
    # 1. Read the data
    df = pd.read_csv(io.StringIO(data_string), 
                      sep='\s+', 
                      header=None, 
                      names=columns, 
                      index_col=False)

    # 2. Select the key columns needed for the pivot: two for the index, one for values.
    # We will use 'student_id' and 'class' as the index levels, and 'age' as the value.
    df_pivot_data = df[['student_id', 'class', 'age']].copy()
    
    # 3. Create a MultiIndex using the desired row and column levels
    df_multi_indexed = df_pivot_data.set_index(['student_id', 'class'])
    
    print("DataFrame with MultiIndex (Index: student_id, class | Value: age):")
    print(df_multi_indexed)
    print("-" * 70)
    
    # 4. Use .unstack() to move the innermost index level ('class') 
    #    to become the new column headers.
    # The 'student_id' level remains as the new single index.
    df_final_pivot = df_multi_indexed['age'].unstack(level='class')
    
    return df_final_pivot

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
df_final = pivot_multiindex_to_dataframe(data)

print("\nResulting DataFrame (student_id is Index | class is Column Header | age is Value):")
print(df_final)
print("-" * 70)
print(f"Final Index Name: {df_final.index.name}")
print(f"Final Column Names: {df_final.columns.tolist()}")