import pandas as pd
import numpy as np

# Sample data with infinite values
data = {'col1': [1000, 2000, 3000, -4000, np.inf, -np.inf]}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace infinite values with NaN
# The .replace() method is an efficient way to do this.
df.replace([np.inf, -np.inf], np.nan, inplace=True)

print("\nDataFrame after removing infinite values:")
print(df)