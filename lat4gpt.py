
		import csv
		
		def read_csv_file(file_path):
		data = []
		with open(file_path, 'r') as file:
		reader = csv.reader(file)
		for row in reader:
		data.append(row)
		return data
		
		def display_basic_info(data):
		num_rows = len(data)
		num_columns = len(data[0]) if data else 0
		
		print("Number of rows:", num_rows)
		print("Number of columns:", num_columns)
		
		if data:
		print("\nFirst few rows of data:")
		for row in data[:5]:  # Displaying the first 5 rows
		print(row)
		
		if __name__ == "__main__":
		file_path = "your_file.csv"  # Replace with your CSV file path
		csv_data = read_csv_file(file_path)
		display_basic_info(csv_data)
	
