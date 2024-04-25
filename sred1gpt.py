import pandas as pd

# Create a sample DataFrame
data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
	'Age': [25, 30, 35, 40, 45],
	'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
	'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print()

# Filter the DataFrame to get only people aged 30 and above
filtered_df = df[df['Age'] >= 30]

# Display the filtered DataFrame
print("Filtered DataFrame (Aged 30 and above):")
print(filtered_df)
print()

# Group the DataFrame by Gender and calculate the average age for each gender
grouped_df = df.groupby('Gender').agg({'Age': 'mean'})

# Display the grouped DataFrame
print("Average Age by Gender:")
print(grouped_df)
