import pandas as pd
import numpy as np

# Test Data (used for the content of the DataFrame)
initial_data = {
    'student_id': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [35, 32, 33, 30, 31, 32],
}

# Create a base DataFrame to use as content
df_content = pd.DataFrame({
    'name': initial_data['name'],
    'age': initial_data['age'],
    'class': initial_data['class']
})

print("--- DataFrames with IntervalIndex ---")

# --- 1. Create the IntervalIndex ---
# We use pd.interval_range to define 6 equally spaced intervals 
# between 20 and 50, closed on the right side.
# e.g., (20, 25], (25, 30], (30, 35], etc.
interval_index = pd.interval_range(
    start=20, 
    end=50, 
    periods=6, 
    closed='right',
    name='Age_Group_Bins'
)

print(f"\nCreated IntervalIndex (using closed='right'):")
print(interval_index)


# --- 2. Create the DataFrame using the IntervalIndex ---
# We map the 6 rows of data to the 6 intervals created above.
df_interval = pd.DataFrame(
    df_content.values, # Use the data values
    index=interval_index, 
    columns=df_content.columns
)

print("\n\nDataFrame with IntervalIndex:")
print(df_interval)

print("\nIndex Type:", type(df_interval.index).__name__)
print("Interval Bounds Example (First Index):", 
      df_interval.index[0].left, "to", df_interval.index[0].right)

# Demonstrating selection using a point that falls within an interval:
# The .loc accessor can be used to query based on a value contained in the index interval.
try:
    # 27.5 falls into the first interval: (25.0, 30.0]
    point_to_select = 27.5
    print(f"\nSelecting data using the point {point_to_select} (falls in the interval {df_interval.index[1]}):")
    
    # Note: I adjusted the expected interval index based on the output of interval_range(20, 50, periods=6)
    selected_row = df_interval.loc[point_to_select]
    print(selected_row)
except Exception as e:
    # This might fail if the user only runs the code snippet and not the full environment
    print(f"\nCould not select data by point (Error: {e}).")
    print("To select by point, ensure the point is within one of the defined intervals.")