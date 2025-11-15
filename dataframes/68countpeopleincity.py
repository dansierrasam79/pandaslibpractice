import pandas as pd

# Sample data for the DataFrame
data = {'city': ['California', 'Georgia', 'Los Angeles', 'California', 'California', 
                 'Georgia', 'Los Angeles', 'California', 'Los Angeles', 'Los Angeles'],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 
                 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group the DataFrame by the 'city' column and count the number of people in each city.
# The size() method is used to get the number of rows in each group.
city_counts = df.groupby('city')['name'].size().reset_index(name='Number of people')

print("\nCity-wise number of people:")
print(city_counts)
