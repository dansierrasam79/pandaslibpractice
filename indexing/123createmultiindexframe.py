import pandas as pd

# Test Data provided by the user
initial_data = {
    'student_id': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'DOB': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [35, 32, 33, 30, 31, 32],
    'street': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    'tag': ['t1', 't2', 't3', 't4', 't5', 't6']
}

# --- 1. Create a MultiIndex using two columns ('student_id' and 'class') ---

# Create a fresh DataFrame for this operation
df_two_cols = pd.DataFrame(initial_data)

print("--- 1. MultiIndex using two columns ('student_id' and 'class') ---")
print("Original DataFrame (df_two_cols):")
print(df_two_cols)

# Create the MultiIndex by passing a list of column names to set_index()
df_multi_col = df_two_cols.set_index(['student_id', 'class'])

print("\nDataFrame with MultiIndex (student_id, class):")
print(df_multi_col)
print("\nMultiIndex structure:")
print(df_multi_col.index)


# --- 2. Create a MultiIndex using the existing Index and one column ('student_id') ---

# Create another fresh DataFrame for this operation (it has the default RangeIndex)
df_index_and_col = pd.DataFrame(initial_data)

print("\n\n--- 2. MultiIndex using the default Index and one column ('student_id') ---")
print("Original DataFrame (df_index_and_col) with default index:")
print(df_index_and_col)
print("Default Index values (Level 0 of the future MultiIndex):", df_index_and_col.index.to_list())

# The index is always included when a list of columns is passed to set_index().
# To explicitly include the current index as a level, we first reset the index
# and then set the desired columns, OR we use the fact that set_index removes 
# the columns used from the data.

# A common way to promote the existing index to a column and then include it
# in the new index structure is by resetting the index first.
df_reset = df_index_and_col.reset_index().rename(columns={'index': 'original_index'})

# Now, set 'original_index' (the old default index) and 'student_id' as the MultiIndex
df_multi_index_col = df_reset.set_index(['original_index', 'student_id'])

print("\nDataFrame with MultiIndex (original_index, student_id):")
print(df_multi_index_col)
print("\nMultiIndex structure:")
print(df_multi_index_col.index)