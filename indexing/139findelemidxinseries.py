import pandas as pd
import numpy as np

def find_element_position(series: pd.Series, target_value):
    """
    Finds the positional integer index (or indices) of a specific value 
    within a Pandas Series using numpy.where().

    Args:
        series: The Pandas Series to search.
        target_value: The value whose position needs to be found.
    
    Returns:
        A NumPy array containing the 0-based positions (indices) where the 
        target_value was found.
    """
    
    print(f"\nSearching for value: '{target_value}'")
    
    # 1. Compare the series' underlying values (series.values) against the target value.
    # This creates a boolean array (True where the value matches).
    # 2. np.where() returns the indices (positions) where the condition is True.
    positional_indices = np.where(series.values == target_value)[0]
    
    if len(positional_indices) > 0:
        print(f"Found '{target_value}' at positional index(es): {positional_indices.tolist()}")
    else:
        print(f"Value '{target_value}' not found in the Series.")

    return positional_indices.tolist()

# --- Sample Data Setup ---
# Create a sample Series with a custom label index
data = [10, 20, 30, 20, 40, 50, 20, 60]
label_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
scores = pd.Series(data, index=label_index, name='Test_Scores')

print("--- Original Series ---")
print("Positional Index: [0, 1, 2, 3, 4, 5, 6, 7]")
print("Label Index:      [A, B, C, D, E, F, G, H]")
print(scores)
print("-" * 50)

# --- Execution ---

# 1. Find the position of a unique value (e.g., 50)
unique_target = 50
find_element_position(scores, unique_target)

# 2. Find the positions of a repeating value (e.g., 20)
repeating_target = 20
find_element_position(scores, repeating_target)

# 3. Find the position of a non-existent value (e.g., 99)
non_existent_target = 99
find_element_position(scores, non_existent_target)