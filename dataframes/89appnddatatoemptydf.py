import pandas as pd

# Create an empty DataFrame
df = pd.DataFrame(columns=['col1', 'col2'])

print("Original empty DataFrame:")
print(df)

# Data to be appended
new_data = [
    {'col1': 0, 'col2': 0},
    {'col1': 1, 'col2': 1},
    {'col1': 2, 'col2': 2}
]

# Append the data using a loop and .loc
for i, row in enumerate(new_data):
    df.loc[i] = row

print("\nAfter appending some data:")
print(df)