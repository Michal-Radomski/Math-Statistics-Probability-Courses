import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol("x")

f = x**3 - 3 * x**2 + 2

f_num = sp.lambdify(x, f, "numpy")

# Integration interval
a = 0
b = 3

x_values = np.linspace(-1, 4, 500)
y_values = f_num(x_values)

# Values ​​within the integration interval
x_area = np.linspace(a, b, 200)
y_area = f_num(x_area)

# Calculation of the integral
result = sp.integrate(f, (x, a, b))

# Graph
plt.figure(figsize=(10, 6))

plt.plot(x_values, y_values, label="f(x)", color="blue")

plt.fill_between(x_area, y_area, 0, alpha=0.3, color="green", label="Definite integral")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(a, color="red", linestyle="--")
plt.axvline(b, color="red", linestyle="--")

plt.title(f"Integral = {result}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

plt.show()
