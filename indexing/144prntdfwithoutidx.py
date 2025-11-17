import pandas as pd

# --- 1. Setup: Create a Sample DataFrame ---
data = {
    'Product': ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam'],
    'Price_USD': [1200, 350, 75, 25, 50],
    'In_Stock': [True, True, False, True, True]
}
df = pd.DataFrame(data)

print("--- 1. Original DataFrame (with default index) ---")
print(df)
print("-" * 50)


# --- 2. Print DataFrame without the index ---
# The to_string() method converts the DataFrame to a string representation.
# Setting index=False ensures the row numbers are omitted.
print("--- 2. DataFrame Printed Without Index using to_string(index=False) ---")
print(df.to_string(index=False))
print("-" * 50)


# --- 3. Alternative: Printing for Reporting (without header) ---
# You can also omit the header if you only want the raw data.
print("--- 3. Data Only (No Index, No Header) ---")
print(df.to_string(index=False, header=False))