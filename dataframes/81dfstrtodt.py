import pandas as pd

# Sample data with dates as strings
data = {'String Date': ['3/11/2000', '3/12/2000', '3/13/2000']}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nData types before conversion:")
df.info()

# Convert the 'String Date' column to datetime objects
df['String Date'] = pd.to_datetime(df['String Date'])

print("\nDataFrame after converting 'String Date' to datetime:")
print(df)
print("\nNew data types:")
df.info()