import pandas as pd
import io

# The data below is for demonstration purposes.
# To use this program, you must first copy your desired
# table data from a spreadsheet (like Excel or Google Sheets)
# to your clipboard.

# Create a sample string that represents the data copied from the clipboard
# This is for testing the code without having to manually copy-paste.
clipboard_data = """1\t2\t3\t4\n2\t3\t4\t5\n4\t5\t1\t0\n2\t3\t7\t8"""

# Use io.StringIO to simulate reading from the clipboard
# In a real-world scenario, you would simply use pd.read_clipboard()
# to read directly from the clipboard.
df = pd.read_csv(io.StringIO(clipboard_data), sep='\t', header=None)

# In a real-world scenario, you would use this line instead of the two above:
# df = pd.read_clipboard(header=None)

print("Data from clipboard to DataFrame:")
print(df)