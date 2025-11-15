import pandas as pd

# Create the original DataFrame from the sample data
data = {'col1': [1, 2, 3],
        'col2': [4, 5, 6],
        'col3': [7, 8, 9]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Select the 'col2' column and convert it to a list using the .tolist() method
col2_list = df['col2'].tolist()

print("\n'col2' of the DataFrame to list:")
print(col2_list)