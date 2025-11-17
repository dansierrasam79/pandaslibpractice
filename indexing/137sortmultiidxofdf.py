import pandas as pd
import io

# Define the column names for the raw data
COLUMNS = ['student_id', 'class', 'name', 'score', 'status']

def sort_multiindex_data(data_string: str):
    """
    Creates a MultiIndex DataFrame and demonstrates sorting by the entire index 
    and by specific index levels.
    """
    
    # 1. Read the data
    df = pd.read_csv(io.StringIO(data_string), 
                      sep='\s+', 
                      header=None, 
                      names=COLUMNS, 
                      index_col=False)

    # 2. Create the MultiIndex: (class, student_id)
    # Note: We intentionally keep the index unsorted initially to show the effect.
    index_levels = ['class', 'student_id']
    df_multi = df.set_index(index_levels).sort_index(ascending=False)
    
    print("--- 1. Original (Unsorted) MultiIndex DataFrame ---")
    print("Note the random order of 'class' and 'student_id' labels:")
    print(df_multi)
    print("\nIndex Levels:", df_multi.index.names)
    print("-" * 70)
    
    # --- A. Sorting by the Full Index Hierarchy ---
    # Calling sort_index() without arguments sorts by all levels, from outermost 
    # to innermost ('class' then 'student_id').
    
    df_sorted_all = df_multi.sort_index(ascending=True)
    
    print("--- 2. Sorted by All Levels (Ascending: class then student_id) ---")
    print("The DataFrame is now lexicographically ordered:")
    print(df_sorted_all)
    print("-" * 70)

    # --- B. Sorting by a Specific Index Level ---
    # Sort only by the inner level ('student_id'), regardless of the outer level ('class').
    # This results in blocks of rows where 'student_id' is sorted, but the outer 'class'
    # labels might appear in a non-sequential order if that was not specified first.
    
    df_sorted_level_id = df_multi.sort_index(level='student_id', ascending=True)
    
    print("--- 3. Sorted Only by Level 'student_id' (Inner Level) ---")
    print("All 's001's come first, then 's002's, etc., ignoring the 'class' order:")
    print(df_sorted_level_id)
    print("-" * 70)
    
    # --- C. Sorting by a List of Levels with Mixed Order ---
    # Sort primarily by 'class' descending, then secondarily by 'student_id' ascending.
    
    df_sorted_mixed = df_multi.sort_index(
        level=['class', 'student_id'], 
        ascending=[False, True] # False for 'class', True for 'student_id'
    )
    
    print("--- 4. Sorted by Mixed Order (Class DESC, Student ID ASC) ---")
    print("VI is listed before V, and within VI, student IDs are s001, s002, s003...")
    print(df_sorted_mixed)
    print("-" * 70)

# --- Test Data Setup ---
# Intentionally mixing up the order for demonstration
data = """
0        V    s002  Gino Mcneill    88  Pass
1        VI   s001  Eesha Hinton    92  Pass
2        V    s004  Syed Wharton    75  Pass
3        VI   s003  Ryan Parkes     65  Fail
4        V    s001  Alberto Franco  95  Pass
5        VI   s002  David Parkes    70  Pass
"""

# --- Execution ---
if __name__ == "__main__":
    sort_multiindex_data(data)