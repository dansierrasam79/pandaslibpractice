import pandas as pd

# 1. Create a sample Pandas Series with date strings
print("Original Series with date strings:")
date_strings = pd.Series([
    '2023-01-01',
    '2023-01-05',
    '2023-01-10',
    '2023-02-15',
    '2023-02-28',
    '2024-03-01'  # Leap year for day of year
])
print(date_strings)
print("-" * 50)

# 2. Convert the Series to a timeseries object
# This is a critical step that allows us to use the .dt accessor for date operations.
dateseries = pd.to_datetime(date_strings)

# 3. Extract the day of the month
# The .dt.day accessor returns the day of the month (1-31).
day_of_month = dateseries.dt.day
print("Day of month:")
print(day_of_month)
print("-" * 50)

# 4. Extract the day of the year
# The .dt.dayofyear accessor returns the day of the year (1-366).
day_of_year = dateseries.dt.dayofyear
print("Day of year:")
print(day_of_year)
print("-" * 50)

# 5. Extract the ISO week number
# The .dt.isocalendar().week accessor returns the ISO 8601 week number.
# This is a reliable method for week number extraction.
week_number = dateseries.dt.isocalendar().week
print("Week number:")
print(week_number)
print("-" * 50)

# 6. Extract the day of the week name
# The .dt.day_name() accessor returns the name of the day of the week.
day_of_week = dateseries.dt.day_name()
print("Day of week:")
print(day_of_week)