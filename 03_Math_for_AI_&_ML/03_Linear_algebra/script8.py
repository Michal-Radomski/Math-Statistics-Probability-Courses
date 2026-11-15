import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def temperature(x, y):
    return x**2 + y**2


print(temperature(2, 3))
# 13


def vector_field(x, y):
    return np.array([x, y])


print(vector_field(2, 3))
# [2 3]


# Define variables
x, y = sp.symbols("x y")

# Define function
f = x**2 + y**2

# Calculate gradient
gradient_x = sp.diff(f, x)
gradient_y = sp.diff(f, y)

print("Gradient:")
print([gradient_x, gradient_y])

# Evaluate at point (2, 3)
result = [gradient_x.subs({x: 2, y: 3}), gradient_y.subs({x: 2, y: 3})]

print("Gradient at (2, 3):", result)

x, y = sp.symbols("x y")

# Define vector field
Fx = x**2
Fy = y**2

# Calculate divergence
divergence = sp.diff(Fx, x) + sp.diff(Fy, y)

print("Divergence:", divergence)

# Evaluate at (2, 3)
print("At (2, 3):", divergence.subs({x: 2, y: 3}))

x, y, z = sp.symbols("x y z")

# Vector field
Fx = -y
Fy = x
Fz = 0

# Calculate curl
curl_x = sp.diff(Fz, y) - sp.diff(Fy, z)
curl_y = sp.diff(Fx, z) - sp.diff(Fz, x)
curl_z = sp.diff(Fy, x) - sp.diff(Fx, y)

curl = [curl_x, curl_y, curl_z]

print("Curl:", curl)

t = sp.symbols("t")

# Circular path
x = sp.cos(t)
y = sp.sin(t)

# Vector field F = (-y, x)
Fx = -y
Fy = x

# Derivatives of the path
dx = sp.diff(x, t)
dy = sp.diff(y, t)

# Dot product F . dr
integrand = Fx * dx + Fy * dy

# Calculate line integral
result = sp.integrate(integrand, (t, 0, 2 * sp.pi))

print(result)

x, y = sp.symbols("x y")

f = x**2 + y**2

laplacian = sp.diff(f, x, 2) + sp.diff(f, y, 2)

print(laplacian)


# Generate coordinates
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)

X, Y = np.meshgrid(x, y)

# Vector field
U = -Y
V = X

# Visualize
plt.figure(figsize=(7, 7))

plt.quiver(X, Y, U, V)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Vector Field: F(x,y) = (-y, x)")

plt.grid()
plt.axis("equal")

plt.show()
