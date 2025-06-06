import pandas as pd

# Demo: Reading a CSV file using different paths

# 1. Relative path (file is in the 'data' folder inside this script's directory)
# Ensure 'sample_data.csv' exists in the 'data' folder
df_relative = pd.read_csv('data/sub_directory/dummy_data.csv')
print("Relative path (data folder):")
print(df_relative.head())
