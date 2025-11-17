import pandas as pd

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

df_reset_demo = pd.DataFrame(initial_data)

print("--- Step 1: Original DataFrame and Default Index ---")
print(df_reset_demo)
print("\nDefault Index Type:", type(df_reset_demo.index).__name__)


# --- Step 2: Set a column ('student_id') as the new Index ---

# Create a new DataFrame with 'student_id' as the index
df_indexed = df_reset_demo.set_index('student_id')

print("\n\n--- Step 2: DataFrame after setting 'student_id' as the Index ---")
print(df_indexed)
print("\nNew Index Type:", type(df_indexed.index).__name__)


# --- Step 3: Reset the Index ---

# The reset_index() method moves the current index ('student_id') back 
# to a column and replaces it with a new default RangeIndex.
df_final = df_indexed.reset_index()

print("\n\n--- Step 3: DataFrame after resetting the Index ---")
print(df_final)
print("\nFinal Index Type:", type(df_final.index).__name__)
print("\nNotice that the previous index ('student_id') is now a regular column again.")