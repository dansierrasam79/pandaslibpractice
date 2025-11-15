import pandas as pd
import io

def filter_with_local_variable(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters the DataFrame to include rows where the 'W' column value 
    is strictly less than the maximum value found in that same column.
    
    Demonstrates using the '@' symbol within .query() to reference a local variable.
    """
    
    # 1. Calculate the local variable outside of the query scope
    # This variable holds the maximum value of the 'W' column (which is 86 in this sample)
    max_w_value = df['W'].max()
    
    print(f"\nMax 'W' value used for filtering: {max_w_value}")
    
    # 2. Use the .query() method, referencing the local Python variable 
    #    using the '@' symbol. The query string is compiled dynamically.
    filtered_df = df.query('W < @max_w_value')
    
    return filtered_df

# --- Sample Data Setup ---
data_query = """W X Y Z
68 78 84 86
75 85 94 97
86 96 89 96
80 80 83 72
66 86 86 83"""

# Read the data from the string
df_query = pd.read_csv(io.StringIO(data_query), delim_whitespace=True)

# --- Execution ---

print("Original DataFrame")
print(df_query)
print("-" * 50)

# 1. Filter the DataFrame
df_filtered = filter_with_local_variable(df_query.copy())

print("\nValues which are less than maximum value of 'W' column")
print(df_filtered)