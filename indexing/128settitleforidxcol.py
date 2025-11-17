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
df.set_index('student_id', inplace=True)

print("--- DataFrame after setting 'student_id' as Index (No custom name yet) ---")
print(df)
print("\nCurrent Index Name:", df.index.name)

# 3. Set a title/name for the index column
df.index.name = 'Enrollment_ID'

print("\n--- DataFrame with Custom Index Name Set ---")
print(df)
print("\nNew Index Name:", df.index.name)

# Alternative method: Setting the index name upon creation
# If you were creating an index from scratch, you can name it directly:
custom_index = pd.Index(
    ['A', 'B', 'C', 'D', 'E', 'F'], 
    name='Custom_Row_Label'
)

df_alt = pd.DataFrame(data, index=custom_index)

print("\n--- DataFrame created with Index Name directly in pd.Index ---")
print(df_alt)
print("\nIndex Name in Alt DF:", df_alt.index.name)