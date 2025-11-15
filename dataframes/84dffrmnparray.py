import pandas as pd
import numpy as np

# Create a NumPy array with 15 rows and 3 columns, filled with zeros.
# This mimics the structure of the sample output.
data = np.zeros((15, 3))

# Define custom index labels for the rows.
index_labels = ['Index' + str(i) for i in range(1, 16)]

# Define custom column headers.
column_headers = ['Column1', 'Column2', 'Column3']

# Create the DataFrame, passing the NumPy array, index, and column names.
df = pd.DataFrame(data=data, index=index_labels, columns=column_headers)

# Display the resulting DataFrame.
print("DataFrame from NumPy array:")
print(df)