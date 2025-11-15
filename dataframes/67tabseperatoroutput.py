import pandas as pd

# Sample data for the DataFrame
data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# The name of the output CSV file
output_filename = 'new_file.csv'

# Write the DataFrame to a CSV file with a tab separator.
# 'sep='\t'' sets the tab as the delimiter.
# 'index=False' prevents writing the DataFrame's index to the CSV.
df.to_csv(output_filename, sep='\t', index=False)

print(f"\nDataFrame has been successfully written to '{output_filename}'.")
print("The content of the file will be separated by tabs.")