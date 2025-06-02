import pandas as pd

# Demo: Reading a CSV file using different paths

# 1. Relative path (file is in the same folder as this script)
df_relative = pd.read_csv('dummy_data.csv')
print("Relative path (same folder):")
print(df_relative.head())

# 2. Relative path to a subfolder (uncomment if your file is in a subfolder called 'data')
# df_subfolder = pd.read_csv('data/dummy_data.csv')
# print("\nRelative path (subfolder):")
# print(df_subfolder.head())

# 3. Absolute path (update this to your actual file location)
# df_absolute = pd.read_csv(r'C:\Users\dgroom2\OneDrive - NSW Department of Education\Documents\GitHub\Y92025DataScience\dummy_data.csv')
# print("\nAbsolute path:")
# print(df_absolute.head())