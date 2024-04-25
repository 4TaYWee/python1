import pandas as pd
import time

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
	'Age': [25, 30, 28, 32],
	'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Measure execution time for following operations
start_time = time.time()

# Print the DataFrame
print(df)

# Get descriptive statistics of the 'Age' column
print(df['Age'].describe())

# Select rows where age is greater than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)

# Add a new column 'State' with default values
df['State'] = 'Unknown'

# Modify 'State' value for specific rows
df.loc[df['City'] == 'Los Angeles', 'State'] = 'California'
print(df)

# Drop the 'City' column
df.drop('City', axis=1, inplace=True)
print(df)

# End time
end_time = time.time()

# Calculate total execution time
total_time = end_time - start_time

# Print execution time
print(f"Total Execution Time: {total_time:.4f} seconds")
