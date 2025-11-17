import pandas as pd
import numpy as np

# --- 1. Define Data and Custom Index Parameters ---
# Sample data dictionary (5 rows)
data = {
    'Product': ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam'],
    'Price': [1200, 350, 75, 25, 50],
    'In_Stock': [True, True, False, True, True]
}

# Define the desired starting value for the index
START_VALUE = 100

# Calculate the length of the data to determine the end of the index range
data_length = len(data['Product'])

# --- 2. Generate the Custom Index ---
# Create a custom index using a list or a range object.
# This index will be [100, 101, 102, 103, 104]
custom_index = range(START_VALUE, START_VALUE + data_length)


# --- 3. Create the DataFrame with the Custom Index ---
# Pass the custom_index to the 'index' parameter when creating the DataFrame
df = pd.DataFrame(data, index=custom_index)

# --- 4. Display the Result ---
print("--- DataFrame with Custom Starting Index ---")
print(f"The index starts at: {START_VALUE}")
print("-" * 50)
print(df)
print("-" * 50)
print(f"The index type is: {type(df.index).__name__}")