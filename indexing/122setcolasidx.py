import pandas as pd

# Test Data provided by the user
data = {
    'student_id': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'DOB': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [35, 32, 33, 30, 31, 32],
    'street': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    'tag': ['t1', 't2', 't3', 't4', 't5', 't6']
}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. Display the default index
print("\n--- 1. Displaying the Default Index ---")
print("The default index is a RangeIndex:")
print(df.index)
print("\nDefault Index values (first few):", df.index[:5].to_list())

# 2. Set a column ('student_id') as the new Index
# We use inplace=True to modify the DataFrame directly, or we could assign the result: df_new = df.set_index('student_id')
df.set_index('student_id', inplace=True)

print("\n--- 2. DataFrame after setting 'student_id' as the Index ---")
print(df)

# Display the new index
print("\nDisplaying the New Index:")
print(df.index)
print("\nNew Index values (first few):", df.index[:5].to_list())
