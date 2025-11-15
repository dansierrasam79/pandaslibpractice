import pandas as pd

# Sample data as a list of dictionaries
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(exam_data)

print("Iterating over rows of the DataFrame:")
# Iterate over each row using iterrows() and print the name and score
for index, row in df.iterrows():
    print(f"{row['name']} {row['score']}")