# Import the Pandas Library
import pandas as pd

# Read the CSV file
df = pd.read_csv("logs.csv")

# Print the DataFrame
print(df)

# Grouping and Summing Data
result = df.groupby("ip")["count"].sum() 

#Print Group Result
print("\nGroup and summed counts by IP:")
print(result)

# Sorting the results
sorted_result = result.sort_values(ascending=False)

#Print the Sorted Result
print("\nSorted by counts descending:")
print(sorted_result)