import pandas as pd
import numpy as np

# Sample data
data = {
    'Name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Syed Wharton', 'Laura'],
    'Age': [18, 22, 40, 50, 80, 5]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Define the bins (age ranges) for the categories
# The bins are exclusive on the right by default.
# The rightmost bin is inclusive, so it includes 80.
# We will create bins: (0, 20], (20, 60], (60, inf]
bins = [0, 20, 60, np.inf]

# Define the labels for the age groups
labels = ['kids', 'adult', 'elderly']

# Use pd.cut() to convert the continuous 'Age' column to categorical
# The pd.cut() function will assign each age to the appropriate bin and label.
df['age_groups'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

print("\nDataFrame with the new 'age_groups' column:")
print(df[['Name', 'Age', 'age_groups']])

# Display the new categorical series as requested in the output
print("\nAge groups:")
print(df['age_groups'])