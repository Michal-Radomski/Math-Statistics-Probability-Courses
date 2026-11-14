import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Euler's number
e = math.e

print("Euler's number:", e)

# Calculate e^2
print("e squared:", e**2)

# Calculate e^5
print("e to the power of 5:", e**5)


x = sp.Symbol("x")

# Define exponential function
f = sp.exp(x)

# Calculate derivative
derivative = sp.diff(f, x)

# Calculate integral
integral = sp.integrate(f, x)

print("Function:", f)
print("Derivative:", derivative)
print("Integral:", integral)

# Evaluate at x = 2
print("f(2):", f.subs(x, 2).evalf())


for n in [10, 100, 1000, 10000, 100000]:
    result = (1 + 1 / n) ** n

    print(f"n = {n:6} | Result = {result}")

print("\nActual value of e:", math.e)


x = np.linspace(-3, 3, 200)

y = np.exp(x)

plt.figure(figsize=(9, 5))

plt.plot(x, y, label="f(x) = e^x", color="blue")

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.title("Euler's Exponential Function")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid(True)
plt.legend()

plt.show()
