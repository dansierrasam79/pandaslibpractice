import pandas as pd
import numpy as np

# Test Data
initial_data = {
    'student_id': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'DOB': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [35, 32, 33, 30, 31, 32],
    'street': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    'tag': ['t1', 't2', 't3', 't4', 't5', 't6']
}

# --- 1. Creating an Index with 64-bit Integers (Int64Index) ---

# We define the labels as a list of integers. Pandas automatically uses Int64Index 
# for standard integer labels. Using large numbers helps emphasize the 64-bit nature.
int_labels = [100000000001, 100000000002, 100000000003, 100000000004, 100000000005, 100000000006]

df_int_index = pd.DataFrame(
    initial_data, 
    index=pd.Index(int_labels, dtype=np.int64) # Explicitly define the index and dtype
)

print("--- DataFrame with 64-bit Integer Index (Int64Index) ---")
print(df_int_index)
print("\nIndex Type:", type(df_int_index.index).__name__)
print("Index Data Type (Dtype):", df_int_index.index.dtype)


# --- 2. Creating an Index with Floating-point Numbers (Float64Index) ---

# We define the labels as a list of floating-point numbers.
float_labels = [0.1, 0.2, 1.1, 1.2, 2.1, 2.2]

df_float_index = pd.DataFrame(
    initial_data, 
    index=pd.Index(float_labels, dtype=np.float64) # Explicitly define the index and dtype
)

print("\n\n--- DataFrame with Floating-point Number Index (Float64Index) ---")
print(df_float_index)
print("\nIndex Type:", type(df_float_index.index).__name__)
print("Index Data Type (Dtype):", df_float_index.index.dtype)