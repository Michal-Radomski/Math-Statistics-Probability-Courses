import matplotlib.pyplot as plt

# Data - Dual Axis Line Chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1000, 1500, 1200, 2000, 2500]
profit = [10, 15, 12, 18, 25]

# Create figure and first axis
fig, ax1 = plt.subplots()

# First Y-axis (Sales)
ax1.plot(months, sales, color="blue", marker="o")
ax1.set_xlabel("Months")
ax1.set_ylabel("Sales ($)", color="blue")

# Create second Y-axis
ax2 = ax1.twinx()

# Second Y-axis (Profit)
ax2.plot(months, profit, color="red", marker="s")
ax2.set_ylabel("Profit (%)", color="red")

# Add title
plt.title("Monthly Sales vs Profit")

# Display chart
plt.show()


# Data - Dual Axis Bar and Line Chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1000, 1500, 1200, 2000, 2500]
profit = [10, 15, 12, 18, 25]

# Create figure
fig, ax1 = plt.subplots()

# Bar chart for sales
ax1.bar(months, sales, color="skyblue", label="Sales")
ax1.set_xlabel("Months")
ax1.set_ylabel("Sales ($)", color="blue")

# Create second axis
ax2 = ax1.twinx()

# Line chart for profit
ax2.plot(months, profit, color="red", marker="o", linewidth=2, label="Profit %")

ax2.set_ylabel("Profit (%)", color="red")

# Add title
plt.title("Sales vs Profit Margin")

# Display chart
plt.show()


# Data - Dual Axis Chart with Legend
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1000, 1500, 1200, 2000, 2500]
profit = [10, 15, 12, 18, 25]

fig, ax1 = plt.subplots()

# First axis
line1 = ax1.bar(months, sales, color="skyblue", label="Sales")

ax1.set_xlabel("Months")
ax1.set_ylabel("Sales ($)")

# Second axis
ax2 = ax1.twinx()

(line2,) = ax2.plot(months, profit, color="red", marker="o", label="Profit %")

ax2.set_ylabel("Profit (%)")

# Combine legends
ax1.legend([line1, line2], ["Sales", "Profit %"], loc="upper left")

plt.title("Monthly Sales and Profit")
plt.show()
