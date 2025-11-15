import pandas as pd
import sys

def create_and_display_dataframe(data):
    """
    Creates a pandas DataFrame from a dictionary and displays it.

    Args:
        data (dict): The dictionary to convert into a DataFrame.
    """
    try:
        # Create a DataFrame from the dictionary
        df = pd.DataFrame(data)

        # Display the DataFrame
        print("Original dictionary:")
        print(data)
        print("\nDataFrame created from the dictionary:")
        print(df)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

# Sample data provided by the user
sample_data = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}

# Call the function with the sample data
if __name__ == "__main__":
    create_and_display_dataframe(sample_data)
