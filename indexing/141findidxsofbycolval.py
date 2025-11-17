import pandas as pd
import io
from typing import List, Any

def find_indices_by_column_value(df: pd.DataFrame, column_name: str, target_value: Any) -> List[Any]:
    """
    Finds the index labels of all rows where the specified column matches the target value.

    Args:
        df: The input Pandas DataFrame.
        column_name: The name of the column to search within.
        target_value: The value to match.

    Returns:
        A list of index labels (row identifiers) for the matching rows.
    """
    print(f"\n--- Searching for rows where '{column_name}' == '{target_value}' ---")
    
    # 1. Create a boolean mask: True for rows where the condition is met.
    mask = df[column_name] == target_value
    
    # 2. Apply the mask to filter the DataFrame.
    filtered_df = df[mask]
    
    # 3. Extract the index labels from the filtered DataFrame.
    matching_indices = filtered_df.index.tolist()
    
    return matching_indices

# --- Test Data Setup ---
# Setup the data structure based on the provided input
data = """
0        s001     V  Alberto Franco     15/05/2002      35  street1   t1
1        s002     V    Gino Mcneill     17/05/2002      32  street2   t2
2        s003    VI     Ryan Parkes     16/02/1999      33  street3   t3
3        s001    VI    Eesha Hinton     25/09/1998      30  street1   t4
4        s002     V    Gino Mcneill     11/05/2002      31  street2   t5
5        s004    VI    David Parkes     15/09/1997      32  street4   t6
"""

# Read the data, treating multiple spaces as a single separator
df = pd.read_csv(
    io.StringIO(data), 
    sep=r'\s+', 
    engine='python', 
    header=None,
    skiprows=1 
)

# Assign meaningful column names and set the original integer index
df.columns = ['ID_Num', 'Class', 'Name', 'DOB', 'Age', 'Address', 'Tag']
df.index = [f'Row_{i}' for i in range(len(df))] # Setting custom label indices for clarity

# --- Execution ---

print("--- Original DataFrame (with custom label indices) ---")
print(df)
print("-" * 60)

# Example 1: Find all rows where 'Class' is 'V'
column_1 = 'Class'
value_1 = 'V'
indices_1 = find_indices_by_column_value(df, column_1, value_1)
print(f"Indices for {column_1} = '{value_1}': {indices_1}")
print("-" * 60)

# Example 2: Find all rows where 'ID_Num' is 's001'
column_2 = 'ID_Num'
value_2 = 's001'
indices_2 = find_indices_by_column_value(df, column_2, value_2)
print(f"Indices for {column_2} = '{value_2}': {indices_2}")
print("-" * 60)

# Example 3: Find rows with a value that appears only once
column_3 = 'Name'
value_3 = 'Ryan Parkes'
indices_3 = find_indices_by_column_value(df, column_3, value_3)
print(f"Indices for {column_3} = '{value_3}': {indices_3}")