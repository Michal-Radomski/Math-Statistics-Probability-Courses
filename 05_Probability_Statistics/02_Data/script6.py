import matplotlib.pyplot as plt
import numpy as np

# Data
marks = [20, 40, 60, 80, 100]
frequency = [5, 10, 15, 12, 8]

# Calculate cumulative frequency
cumulative_frequency = []

total = 0

for value in frequency:
    total = total + value
    cumulative_frequency.append(total)

# Create cumulative frequency chart
plt.plot(marks, cumulative_frequency, marker="o", color="blue")

# Add title and labels
plt.title("Cumulative Frequency Chart")
plt.xlabel("Marks")
plt.ylabel("Cumulative Frequency")

plt.grid(True)

plt.show()


# Data
marks = [20, 40, 60, 80, 100]
frequency = [5, 10, 15, 12, 8]

# Calculate cumulative frequency
cf = np.cumsum(frequency)

# Plot chart
plt.plot(marks, cf, marker="o", color="green", linewidth=2)

plt.title("Cumulative Frequency Distribution")
plt.xlabel("Marks")
plt.ylabel("Cumulative Frequency")

plt.grid(True)

plt.show()


# Data
marks = [20, 40, 60, 80, 100]
frequency = [5, 10, 15, 12, 8]

# Cumulative frequency
cf = np.cumsum(frequency)

# Chart size
plt.figure(figsize=(8, 5))

# Plot
plt.plot(marks, cf, marker="o", color="red", linewidth=2, markersize=7)

# Add titles
plt.title("Student Marks - Cumulative Frequency", fontsize=14)

plt.xlabel("Marks")
plt.ylabel("Cumulative Frequency")

# Add grid
plt.grid(axis="both", linestyle="--", alpha=0.5)

plt.show()
