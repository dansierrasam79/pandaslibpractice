import pandas as pd

# 1. Create a sample Pandas Series of strings
print("Original Series:")
series_phrases = pd.Series(['hello world', 'python is fun', 'data science rocks'])
print(series_phrases)
print("-" * 50)

# 2. Define a function to count characters in each word of a string
# This function takes a single string (a phrase) as input.
def count_characters_in_words(phrase):
    # Split the phrase into a list of words
    words = phrase.split()
    # Use a list comprehension to get the length of each word
    word_lengths = [len(word) for word in words]
    return word_lengths

# 3. Apply the function to each element of the Series
# The .apply() method is used to call our function on each element of the Series.
# The result will be a new Series where each item is a list of integers
# representing the character counts for each word in the original phrase.
character_counts = series_phrases.apply(count_characters_in_words)

# 4. Print the final result
print("Character counts for each word:")
print(character_counts)