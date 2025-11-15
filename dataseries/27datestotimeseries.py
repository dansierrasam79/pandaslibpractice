import pandas as pd

# 1. Create a sample Pandas Series with date strings
# These strings are in a common format that Pandas can automatically recognize.
print("Original Series with date strings:")
date_strings = pd.Series([
    '2023-01-01',
    '2023-01-05',
    '2023-01-10',
    '2023-02-15',
    '2023-02-28'
])
print(date_strings)
print("-" * 50)

# 2. Convert the Series to a timeseries (DatetimeIndex)
# The pd.to_datetime() function is the standard and most robust way to do this.
# It parses the strings and converts them into datetime objects.
timeseries = pd.to_datetime(date_strings)

# 3. Print the resulting timeseries and its data type (dtype)
# The dtype will be `datetime64[ns]`, indicating it's a timeseries object.
print("Converted Timeseries:")
print(timeseries)
print("-" * 50)
print(f"Data type of the new Series: {timeseries.dtype}")

# 4. Demonstrate how to handle a different date format
# The `format` parameter can be used to explicitly specify the format.
print("\nOriginal Series with a different date format:")
date_strings_alt = pd.Series([
    '01/01/2023',
    '05/01/2023',
    '10/01/2023'
])
print(date_strings_alt)
print("-" * 50)

# Use the format code '%m/%d/%Y' to parse the month/day/year format
timeseries_alt = pd.to_datetime(date_strings_alt, format='%m/%d/%Y')
print("Converted Timeseries with specific format:")
print(timeseries_alt)