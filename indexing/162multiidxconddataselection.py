import pandas as pd

# --- 1. Create the MultiIndex DataFrame ---
# Define the index levels: Geography and Time
index_tuples = [
    ('Europe', 'London', 2023), 
    ('Europe', 'Paris', 2023),
    ('Europe', 'London', 2024), 
    ('Europe', 'Paris', 2024),
    ('Asia', 'Tokyo', 2023), 
    ('Asia', 'Seoul', 2023),
    ('Asia', 'Tokyo', 2024), 
    ('Asia', 'Seoul', 2024),
]
multi_index = pd.MultiIndex.from_tuples(
    index_tuples, 
    names=['Continent', 'City', 'Year']
)

# Define the data
data = {
    'Temperature': [15, 20, 25, 22, 30, 32, 28, 35],  # Temperature in Celsius
    'Humidity': [70, 65, 55, 60, 80, 75, 78, 85],
    'Rainfall': [10, 5, 2, 8, 0, 1, 3, 0]
}

df_weather = pd.DataFrame(data, index=multi_index)

print("--- Original MultiIndex DataFrame (Weather Data) ---")
print(df_weather)
print("-" * 65)


# --- 2. Define the Conditions ---

# Condition A: Data-based filter (Temperature is high)
# Select rows where 'Temperature' column value is greater than 25°C.
condition_temperature = df_weather['Temperature'] > 25

# Condition B: Index-based filter (City is Seoul or Tokyo)
# This uses the `get_level_values` method to check the second index level.
condition_city = df_weather.index.get_level_values('City').isin(['Seoul', 'Tokyo'])


# --- 3. Combine Conditions and Apply Filtering ---

# Combine both conditions using the bitwise AND operator (&)
combined_condition = condition_temperature & condition_city

# Apply the combined condition to the DataFrame
filtered_df = df_weather[combined_condition]


# --- 4. Display the Result ---
print("\n--- Filtered DataFrame (Temperature > 25 AND City in [Seoul, Tokyo]) ---")
print(filtered_df)
print("-" * 65)


# --- 5. Example using .loc for Index Slicing after filtering ---

# Now, let's take the filtered result and use .loc to slice only the 2024 data.
# The `filtered_df` now has an index where we can select specific year levels.

# Use a tuple to select the specific index levels:
# (All Continents/Cities, but only Year=2024)
# We use `slice(None)` to represent "select all" for the first two levels.

idx = pd.IndexSlice
final_slice = filtered_df.loc[idx[:, :, 2024], :]

print("\n--- Final Slice: Filtered Data (High Temp in Asia) + Sliced for Year 2024 ---")
print(final_slice)
print("-" * 65)