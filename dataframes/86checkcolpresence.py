import pandas as pd

# Create the original DataFrame from the sample data
data = {'col1': [1, 2, 3, 4, 7],
        'col2': [4, 5, 6, 9, 5],
        'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Check if 'col4' is in the DataFrame columns
if 'col4' in df.columns:
    print("\n'col4' is present in the DataFrame.")
else:
    print("\n'col4' is not present in the DataFrame.")

# Check if 'col1' is in the DataFrame columns
if 'col1' in df.columns:
    print("'col1' is present in the DataFrame.")
else:
    print("'col1' is not present in the DataFrame.")