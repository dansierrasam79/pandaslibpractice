import pandas as pd

# Sample data for the DataFrame
data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Select rows where the value in 'col1' is equal to 4
selected_rows = df[df['col1'] == 4]

print("\nRows for col1 value == 4:")
print(selected_rows)