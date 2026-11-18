import matplotlib.pyplot as plt

# Data
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 55, 65, 75, 80, 90, 95]

# Create histogram
plt.hist(marks)

# Add title and labels
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Display chart
plt.show()


marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 55, 65, 75, 80, 90, 95]

plt.hist(marks, bins=5, color="skyblue", edgecolor="black")

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()


ages = [22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58, 60]

plt.hist(ages, bins=6, color="orange", edgecolor="black", density=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Density")

plt.show()

ages = [22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58, 60]

plt.figure(figsize=(8, 5))

plt.hist(ages, bins=6, color="lightgreen", edgecolor="black", alpha=0.8)

plt.title("Age Distribution", fontsize=15)
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()
