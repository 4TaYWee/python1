import pandas as pd
		
		def calculate_statistics(csv_file):
		# Load data from CSV file into a pandas DataFrame
		df = pd.read_csv(csv_file)
		
		# Calculate mean
		mean = df.mean()
		
		# Calculate median
		median = df.median()
		
		# Calculate standard deviation
		std_dev = df.std()
		
		return mean, median, std_dev
		
		def main():
		# Path to your CSV file
		csv_file = 'data.csv'
		
		# Calculate statistics
		mean, median, std_dev = calculate_statistics(csv_file)
		
		# Display statistics
		print("Mean:")
		print(mean)
		print("\nMedian:")
		print(median)
		print("\nStandard Deviation:")
		print(std_dev)
		
		if __name__ == "__main__":
		main()
