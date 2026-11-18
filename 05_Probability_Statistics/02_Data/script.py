import matplotlib.pyplot as plt

# Data - Line chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 200, 250]

# Create line chart
plt.plot(months, sales, marker="o", color="blue")

# Add title and labels
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

# Display chart
plt.show()


# Data - bar chart
students = ["John", "Alice", "Bob", "David", "Emma"]
marks = [85, 90, 75, 80, 95]

# Create bar chart
plt.bar(students, marks, color="green")

# Add title and labels
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Display chart
plt.show()


# Data - Horizontal bar chart
products = ["Laptop", "Mobile", "Tablet", "Watch"]
sales = [200, 350, 150, 100]

plt.barh(products, sales, color="orange")

plt.title("Product Sales")
plt.xlabel("Sales")
plt.ylabel("Products")

plt.show()
