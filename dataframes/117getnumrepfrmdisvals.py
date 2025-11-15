import pandas as pd
import io

def factorize_column(df: pd.DataFrame, column_name: str):
    """
    Generates the numeric representation (codes) and the distinct values (unique labels)
    for a given DataFrame column using the factorize() method.

    Args:
        df: The input DataFrame.
        column_name: The name of the column to factorize.
    """
    
    # 1. Use factorize() on the specified column Series.
    # factorize() returns a tuple: (codes, unique_labels)
    codes, unique_labels = df[column_name].factorize()
    
    print("\nNumeric representation of an array by identifying distinct values:")
    print(codes)
    
    print("Distinct Values (The Index/Categories):")
    print(unique_labels)


# --- Sample Data Setup ---

data = """Name,Date_Of_Birth,Age
Alberto Franco,17/05/2002,18.5
Gino Mcneill,16/02/1999,21.2
Ryan Parkes,25/09/1998,22.5
Eesha Hinton,11/05/2002,22.0
Gino Mcneill,15/09/1997,23.0"""

# Read the data, using ',' as the separator since the sample uses names
# that contain spaces, but comma-separated for data structure.
df = pd.read_csv(io.StringIO(data))

# --- Execution ---

print("Original DataFrame:")
print(df)
print("-" * 50)

# Factorize the 'Name' column
factorize_column(df.copy(), 'Name')