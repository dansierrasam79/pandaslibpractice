import pandas as pd
import numpy as np

# 1. Create a sample Series with strings containing whitespace
print("Original Series:")
series_data = pd.Series([
    'a b c',
    'x y z',
    'p q r',
    'a a a'
])
print(series_data)
print("-" * 50)

# 2. Join the series into a single string to find the least frequent character
# The `str.cat(sep='')` method concatenates all strings in the Series into one.
full_string = series_data.str.cat(sep='')
print(f"Combined string: '{full_string}'")
print("-" * 50)

# 3. Get the frequency of each character
# We use a Series from the full string and then `value_counts()` to count the characters.
char_counts = pd.Series(list(full_string)).value_counts()
print("Character counts:")
print(char_counts)
print("-" * 50)

# 4. Find the least frequent character
# The `value_counts()` method sorts by frequency in descending order,
# so the last item in the index is the least frequent character.
least_frequent_char = char_counts.index[-1]
print(f"The least frequent character is: '{least_frequent_char}'")
print("-" * 50)

# 5. Replace the white spaces in the original Series with the least frequent character
# The `str.replace()` method is used to replace all occurrences of a substring.
# We replace a single space ' ' with our found character.
replaced_series = series_data.str.replace(' ', least_frequent_char)

# 6. Print the final result
print("Series after replacing spaces with the least frequent character:")
print(replaced_series)