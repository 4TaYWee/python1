import matplotlib.pyplot as plt

# Sample data (replace with your own data)
x_data = ["Cat", "Dog", "Bird"]
y_data = [5, 3, 2]

# Choose between bar chart or line chart
chart_type = "bar"  # Change to "line" for line chart

# Create the plot
plt.figure(figsize=(8, 6))  # Adjust figure size as desired
if chart_type == "bar":
plt.bar(x_data, y_data)
else:
plt.plot(x_data, y_data)

# Customize the plot
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Sample Chart")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability (optional)

# Display the chart
plt.tight_layout()
plt.show()
