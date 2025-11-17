import pandas as pd

# Test Data (extracted from the user input)
data = {
    'student_id': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'DOB': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [35, 32, 33, 30, 31, 32],
    'street': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    'tag': ['t1', 't2', 't3', 't4', 't5', 't6']
}

# 1. Create the initial DataFrame
df = pd.DataFrame(data)

# 2. Set 'student_id' as the index
# Note: Since 's001' and 's002' are repeated, they will both be used as indices,
# allowing us to modify all rows that match that ID.
df.set_index('student_id', inplace=True)

print("--- Original DataFrame (Indexed by student_id) ---")
print(df)

# --- 3. Set a new value in a specific cell using index label and column name ---

# We want to change the 'age' of the first student 's001' entry (index 0 in the original data)
# To target a specific row when the index is duplicated, we can use the integer position (iloc) 
# or a combination of the index and the column.

# Let's target the *first* occurrence of 's001' and change the age.
# For simplicity and best practice, we'll use iloc here to ensure we target a single row
# based on its *position* (0-based) after setting the index, since 's001' is duplicated.
# To use .loc with a duplicated index, you need to use a single-item list or slice 
# to ensure you're not modifying all rows with the same index label.

# Example 1: Modifying the 'age' of the row at index position 0
row_to_change_position = 0
column_to_change = 'age'
new_value = 40

print(f"\nSetting value at row position {row_to_change_position} ('{df.index[row_to_change_position]}') in column '{column_to_change}' to {new_value}...")
df.iloc[row_to_change_position, df.columns.get_loc(column_to_change)] = new_value

# Example 2: Modifying the 'class' of the row with index label 's003'
target_index_label = 's003'
target_column = 'class'
new_class = 'VII'

print(f"Setting value for index label '{target_index_label}' in column '{target_column}' to '{new_class}'...")
df.loc[target_index_label, target_column] = new_class


print("\n--- DataFrame After Updates ---")
print(df)