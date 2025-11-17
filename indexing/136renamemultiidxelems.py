import pandas as pd
import io

def rename_multiindex_elements(data_string: str) -> pd.DataFrame:
    """
    Constructs a MultiIndex DataFrame and demonstrates renaming of:
    1. Column names.
    2. Specific labels within the MultiIndex levels.
    """
    
    # Define the column names for the raw data
    columns = ['student_id', 'class', 'name', 'date_of_birth', 'age', 'street', 't_id']
    
    # 1. Read the data
    df = pd.read_csv(io.StringIO(data_string), 
                      sep='\s+', 
                      header=None, 
                      names=columns, 
                      index_col=False)

    # 2. Create the MultiIndex: (student_id, class)
    # The levels are: 0: student_id, 1: class
    df_multi = df.set_index(['student_id', 'class'])
    
    print("--- 1. Original MultiIndex DataFrame (Index: student_id, class) ---")
    print(df_multi[['name', 'age']].head(4))
    print("-" * 60)
    
    # --- A. Renaming Column Names ---
    
    # Use the rename() method with the 'columns' parameter.
    column_mapping = {
        'age': 'Current_Age',       # Rename 'age'
        'street': 'Residential_Address' # Rename 'street'
    }
    
    df_renamed_cols = df_multi.rename(columns=column_mapping)
    
    print("--- 2. DataFrame after Column Renaming ---")
    print(df_renamed_cols[['name', 'Current_Age']].head(4))
    print(f"\nNew Column Names: {df_renamed_cols.columns.tolist()}")
    print("-" * 60)
    
    # --- B. Renaming Specific Index Labels ---
    
    # Use the rename() method with the 'index' parameter and the 'level' parameter.
    
    # Rename labels in Level 0 ('student_id')
    # Change 's001' to 'Student_A' and 's002' to 'Student_B'
    index_level_0_mapping = {
        's001': 'A001',
        's002': 'B002'
    }
    df_renamed_labels = df_renamed_cols.rename(index=index_level_0_mapping, level='student_id')

    # Rename labels in Level 1 ('class')
    # Change 'V' to 'Grade_5'
    index_level_1_mapping = {
        'V': 'Grade_5'
    }
    df_renamed_labels = df_renamed_labels.rename(index=index_level_1_mapping, level='class')
    
    print("--- 3. Final DataFrame after Index Label Renaming ---")
    print("Note the index changes for 's001' -> 'A001' and 'V' -> 'Grade_5'")
    print(df_renamed_labels[['name', 'Current_Age']].head(4))
    print("-" * 60)
    
    return df_renamed_labels

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
    df_final = rename_multiindex_elements(data)