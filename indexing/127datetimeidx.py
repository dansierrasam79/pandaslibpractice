import pandas as pd

# Test Data (used for the content of the DataFrame)
initial_data = {
    'student_id': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [35, 32, 33, 30, 31, 32],
}

# Create a base DataFrame to use as content
df_content = pd.DataFrame(initial_data)

# --- 1. Create the DatetimeIndex ---
# We use pd.to_datetime to create 6 specific datetime objects, 
# ensuring they include both date and time components.
datetime_labels = pd.to_datetime([
    '2024-09-30 09:00:00',
    '2024-09-30 10:30:00',
    '2024-10-01 11:00:00',
    '2024-10-01 12:45:00',
    '2024-10-02 13:00:00',
    '2024-10-02 14:15:00'
])

print("--- DataFrame with DatetimeIndex ---")

# --- 2. Create the DataFrame using the DatetimeIndex ---
df_datetime_index = pd.DataFrame(
    df_content.values, 
    index=datetime_labels,
    columns=df_content.columns
)

print("\nDataFrame Indexed by Date and Time:")
print(df_datetime_index)

print("\nIndex Type:", type(df_datetime_index.index).__name__)
print("Index Data Type (Dtype):", df_datetime_index.index.dtype)

# --- 3. Demonstrating Slicing with Dates (a key benefit) ---
print("\nDemonstrating selection using a date range (only date '2024-10-01'):")
# Slicing can use date strings, even if the index contains time components.
selected_rows = df_datetime_index.loc['2024-10-01']
print(selected_rows)