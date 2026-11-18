import matplotlib.pyplot as plt

# Employee salary data
salary = [25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 100000]

# Create box plot
plt.boxplot(salary)

# Add title and labels
plt.title("Employee Salary Distribution")
plt.ylabel("Salary")

# Display chart
plt.show()


salary = [25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 100000]

plt.boxplot(
    salary,
    patch_artist=True,
    showmeans=True,
    boxprops=dict(facecolor="skyblue"),
    medianprops=dict(color="red"),
    whiskerprops=dict(color="black"),
    capprops=dict(color="green"),
)

plt.title("Employee Salary Distribution")
plt.ylabel("Salary")

plt.show()


# Department-wise salary
IT = [30000, 35000, 40000, 45000, 50000]
HR = [25000, 28000, 32000, 35000, 40000]
Sales = [20000, 30000, 35000, 45000, 60000]

# Create multiple box plots
plt.boxplot([IT, HR, Sales])

plt.title("Department-wise Salary Distribution")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.show()
