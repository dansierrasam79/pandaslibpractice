import pandas as pd

# 1. Create a sample Pandas Series of words
print("Original Series:")
series_words = pd.Series([
    'apple',
    'fly',
    'banana',
    'strength',
    'rhythm',
    'education',
    'book'
])
print(series_words)
print("-" * 50)

# 2. Filter the Series to find words with at least two vowels
# The .str accessor allows us to apply string methods to the entire Series.
# The .str.count() method counts the number of non-overlapping occurrences of a pattern.
# We use a regular expression `[aeiouAEIOU]` to match any vowel, case-insensitively.
# This operation returns a new Series of integer counts.
vowel_counts = series_words.str.count(r'[aeiouAEIOU]')
print("Vowel counts for each word:")
print(vowel_counts)
print("-" * 50)

# 3. Create a boolean mask where the count is at least 2
# This mask will be used to filter the original Series.
mask = vowel_counts >= 2
print("Boolean Mask:")
print(mask)
print("-" * 50)

# 4. Apply the mask to the original Series to get the final result
# Only the rows where the mask is True will be included in the new Series.
filtered_series = series_words[mask]
print("Words with at least two vowels:")
print(filtered_series)