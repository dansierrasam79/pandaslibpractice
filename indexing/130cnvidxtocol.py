import pandas as pd

# Test Data
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

# 2. Set 'student_id' as the index and name it (optional, but good practice)
df.set_index('student_id', inplace=True)
df.index.name = 'Enrollment_Key' # Give the index a distinct name

print("--- DataFrame 1: After setting 'student_id' as the Index ---")
print(df)
print("\nIndex name before conversion:", df.index.name)

# 3. Convert the Index into a column using reset_index()
# This creates a new DataFrame (df_new) with the old index becoming a column
# and a new default RangeIndex being assigned.
df_new = df.reset_index()

print("\n--- DataFrame 2: After using reset_index() ---")
print(df_new)
print("\nNew column created from index:", df_new.columns[0])
print("New index name:", df_new.index.name)