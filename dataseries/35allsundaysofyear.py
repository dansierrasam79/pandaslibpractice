import pandas as pd

# 1. Define the year for which we want to find all Sundays
year = 2024
print(f"Finding all Sundays in the year: {year}")
print("-" * 50)

# 2. Create a full date range for the specified year
# The pd.date_range() function is used to generate a sequence of dates.
# The 'freq' parameter is set to 'D' for 'Daily' to get every day of the year.
start_date = f'{year}-01-01'
end_date = f'{year}-12-31'
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
print("Generated a full date range for the year.")
print("-" * 50)

# 3. Create a boolean mask to filter for Sundays
# The .dayofweek attribute returns the day of the week, where Monday=0 and Sunday=6.
# We create a mask where `True` indicates a Sunday.
sundays_mask = date_range.dayofweek == 6

# 4. Use the boolean mask to get the subset of Sundays
# This filters the full date range, keeping only the dates that correspond to a Sunday.
sundays_series = date_range[sundays_mask]

# 5. Print the final result
print(f"All Sundays of the year {year}:")
print(sundays_series)