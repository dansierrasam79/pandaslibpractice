import pandas as pd
import numpy as np

# Create the original DataFrame
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df_original = pd.DataFrame(data)

print("Original DataFrame:")
print(df_original)

# Rename the columns using a dictionary
df_renamed = df_original.rename(columns={'col1': 'Column1', 'col2': 'Column2', 'col3': 'Column3'})

print("\nNew DataFrame after renaming columns:")
print(df_renamed)

# Another way to rename columns is by reassigning the .columns attribute,
# but using .rename() is often preferred as it's more explicit
# df_renamed_alt = df_original.copy()
# df_renamed_alt.columns = ['Column1', 'Column2', 'Column3']
# print("\nNew DataFrame after renaming columns (alternative method):")
# print(df_renamed_alt)