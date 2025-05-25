import pandas as pd

# Create a simple list
data = [1, 2, 3, 4, 5]

# Create a DataFrame from the list
df = pd.DataFrame(data, columns=['Numbers'])

print(df)

# create a loop and run through the data frame
for index, row in df.iterrows():
    print(f"Index: {index}, Value: {row['Numbers']}")