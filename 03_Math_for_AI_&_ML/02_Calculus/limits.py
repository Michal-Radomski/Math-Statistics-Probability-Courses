import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Define variable
x = sp.Symbol("x")

# Define function
f = x**2 + 3 * x + 1

# Calculate limit as x approaches 2
result = sp.limit(f, x, 2)

print("Function:", f)
print("Limit:", result)


x = sp.Symbol("x")

f = (x**2 - 4) / (x - 2)

# Calculate limit
result = sp.limit(f, x, 2)

print("Function:", f)
print("Limit:", result)


x = sp.Symbol("x")

f = sp.Abs(x) / x

# Left-hand limit
left_limit = sp.limit(f, x, 0, dir="-")

# Right-hand limit
right_limit = sp.limit(f, x, 0, dir="+")

print("Left-hand limit:", left_limit)
print("Right-hand limit:", right_limit)


x = sp.Symbol("x")

f = (3 * x**2 + 2 * x + 1) / (x**2 + 5)

result = sp.limit(f, x, sp.oo)

print("Limit at infinity:", result)


# Define function
def f(x):
    return (x**2 - 4) / (x - 2)


# Generate values, excluding x = 2
x1 = np.linspace(0, 1.99, 200)
x2 = np.linspace(2.01, 4, 200)

# Plot function
plt.figure(figsize=(9, 6))

plt.plot(x1, f(x1), color="blue", label="f(x)")
plt.plot(x2, f(x2), color="blue")

# Mark the limit point
plt.scatter(2, 4, color="red", zorder=5, label="Limit = 4")

plt.axvline(2, color="gray", linestyle="--", alpha=0.6)

plt.axhline(4, color="gray", linestyle="--", alpha=0.6)

plt.title("Visualizing a Mathematical Limit")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.legend()
plt.grid(True)
plt.show()
