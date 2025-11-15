import pandas as pd
import io

def rename_columns_with_pattern(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renames DataFrame columns by stripping trailing whitespace and converting 
    names to lowercase using string methods on the index.

    Args:
        df: The original DataFrame.

    Returns:
        The DataFrame with cleaned column names.
    """
    # 1. Access the column index (df.columns)
    # 2. Apply the .str accessor to the index
    # 3. Use .str.strip() to remove leading/trailing whitespace
    # 4. Use .str.lower() to convert all names to lowercase
    
    df.columns = df.columns.str.strip().str.lower()
    
    return df

# --- Sample Data Setup ---
# The data uses space-padding in the header to simulate trailing whitespace
data = """Name      Date_Of_Birth     Age 
Alberto Franco 17/05/2002 18.5
Gino Mcneill 16/02/1999 21.2
Ryan Parkes 25/09/1998 22.5
Eesha Hinton 11/05/2002 22.0
Syed Wharton 15/09/1997 23.0"""

# Read the data, ensuring that column names preserve the whitespace for the demonstration
# We use 'delim_whitespace=True' here to read the raw data, but the main operation
# addresses the whitespace in the headers themselves.
df = pd.read_csv(io.StringIO(data), delim_whitespace=True)

# --- Execution ---

print("Original DataFrame")
print(df)
print("\nOriginal Column Names (showing whitespace/casing issues):")
print(df.columns.tolist())
print("-" * 50)

# Perform the renaming operation
df_cleaned = rename_columns_with_pattern(df.copy()) # Use copy to keep original intact

print("\nDataFrame with Cleaned Column Names")
print(df_cleaned)
print("\nCleaned Column Names:")
print(df_cleaned.columns.tolist())