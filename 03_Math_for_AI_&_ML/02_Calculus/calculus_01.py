import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# * Derivatives
# Mathematical symbol
x = sp.Symbol("x")

# Function definition
f = x**3 - 3 * x**2 + 2

# First and second derivatives
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f, x, 2)

print("Function:")
print(f)

print("\nFirst derivative:")
print(f_prime)

print("\nSecond derivative:")
print(f_double_prime)

# Converting SymPy functions to NumPy functions
f_num = sp.lambdify(x, f, "numpy")
f_prime_num = sp.lambdify(x, f_prime, "numpy")
f_double_prime_num = sp.lambdify(x, f_double_prime, "numpy")

# Data range
x_values = np.linspace(-2, 5, 500)

# Calculations
y = f_num(x_values)
y_prime = f_prime_num(x_values)
y_double_prime = f_double_prime_num(x_values)

# Plotting graphs
plt.figure(figsize=(12, 7))

plt.plot(x_values, y, label="f(x)", linewidth=2)
plt.plot(x_values, y_prime, label="f'(x)", linestyle="--")
plt.plot(x_values, y_double_prime, label="f''(x)", linestyle=":")

plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)

plt.title("Function and its derivatives")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()


# * Integrals
# Indefinite integral
integral = sp.integrate(f, x)

print("Indefinite integral:")
print("integral:", integral)

# Definite integral from 0 to 3
definite_integral = sp.integrate(f, (x, 0, 3))

print("\nDefinite integral:")
print(definite_integral)

# Numerical result
print("\nNumeric result:")
print(float(definite_integral))
