import pandas as pd

# 1. Create a sample Pandas Series of strings
print("Original Series:")
series_words = pd.Series(['apple pie', 'banana bread', 'cherry tart'])
print(series_words)
print("-" * 50)

# 2. Define a function to process each word
# This function takes a single string (a word) as input.
def capitalize_first_and_last(word):
    # Check if the word is not empty
    if len(word) > 0:
        # Capitalize the first character and the last character.
        # Everything in between remains as it was.
        # For a single-letter word, both will be capitalized.
        return word[0].upper() + word[1:-1] + word[-1].upper()
    return word

# 3. Apply the function to each element of the Series
# The .apply() method is used to call a function on each element of the Series.
# The lambda function splits each phrase into words and then processes each word.
processed_series = series_words.apply(
    lambda phrase: ' '.join(
        [capitalize_first_and_last(word) for word in phrase.split()]
    )
)

# 4. Print the final result
print("Series after capitalizing the first and last characters of each word:")
print(processed_series)