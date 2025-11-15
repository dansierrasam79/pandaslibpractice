import pandas as pd

# 1. Create a sample Pandas Series with year-month strings
print("Original Series with year-month strings:")
series_ym = pd.Series([
    '2023-01',
    '2023-02',
    '2023-03',
    '2023-04',
    '2023-05'
])
print(series_ym)
print("-" * 50)

# 2. Specify the day of the month to add
# We'll use the 15th as an example.
day_of_month = '15'
print(f"Specified day to add: {day_of_month}")
print("-" * 50)

# 3. Concatenate the year-month string with the specified day
# This creates a new Series of full date strings.
full_date_strings = series_ym + '-' + day_of_month
print("New Series with full date strings:")
print(full_date_strings)
print("-" * 50)

# 4. Convert the new Series of strings to a proper timeseries
# We use pd.to_datetime() to parse the strings into datetime objects.
timeseries = pd.to_datetime(full_date_strings)

# 5. Print the final result and its data type
print("Converted Timeseries:")
print(timeseries)
print("-" * 50)
print(f"Data type of the new Series: {timeseries.dtype}")