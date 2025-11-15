import pandas as pd

# Create the two original Series
s1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'], dtype=str)
s2 = pd.Series([1, 2, 3, 4, 5], dtype=int)

print("Original Series:")
print("Series 1:")
print(s1)
print("\nSeries 2:")
print(s2)

# Method 1: Combine using the DataFrame constructor with a list of series
# This method results in default integer column names.
print("\nCombine above series to a dataframe:")
df_list = pd.DataFrame([s1, s2]).transpose()
# .transpose() is used to convert rows to columns for the final DataFrame
print(df_list)

# Method 2: Combine using pd.concat()
# The axis=1 argument stacks the Series side-by-side.
print("\nUsing pandas concat:")
df_concat = pd.concat([s1, s2], axis=1)
print(df_concat)

# Method 3: Combine using a dictionary
# This is a very common and flexible method that allows you to specify column names.
print("\nUsing pandas DataFrame with a dictionary, gives a specific name to the columns:")
df_dict = pd.DataFrame({'col1': s1, 'col2': s2})
print(df_dict)
