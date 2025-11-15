import pandas as pd
import numpy as np

# Create a sample DataFrame with many columns to demonstrate truncation.
data = pd.DataFrame(np.random.rand(5, 15), columns=[f'col{i}' for i in range(15)])

print("--- Original DataFrame (Truncated) ---")
print(data)

# Set the option to display all columns.
# 'None' removes the display limit, allowing all columns to be shown.
pd.set_option('display.max_columns', None)

print("\n--- DataFrame with Widened Display ---")
print(data)