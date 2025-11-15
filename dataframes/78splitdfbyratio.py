import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Create a sample DataFrame with 10 rows and 2 columns of random data.
df = pd.DataFrame(np.random.randn(10, 2))

print("Original DataFrame:")
print(df)

# ---
# Split the DataFrame into a 70% sample and the remaining 30%.
# The `frac` parameter in df.sample() specifies the fraction of rows to return.
# We also use `random_state` to ensure the split is reproducible.
df_70_percent = df.sample(frac=0.7, random_state=200)

# The remaining data is obtained by dropping the indices of the first sample.
df_30_percent = df.drop(df_70_percent.index)

print("\n70% of the DataFrame:")
print(df_70_percent)

print("\n30% of the DataFrame:")
print(df_30_percent)