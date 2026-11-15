import numpy as np
from scipy.optimize import fsolve

# Coefficient matrix
A = np.array([[2, 3], [4, 1]])

# Results
b = np.array([8, 6])

# Solve the system
solution = np.linalg.solve(A, b)

print(solution)

# [1. 2.]


A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

C = A @ B

print(C)


vector = np.array([2, 3])

# Scaling matrix
M = np.array([[2, 0], [0, 2]])

result = M @ vector

print(result)
# [4 6]


# Coefficients: x² + 2x - 8
coefficients = [1, 2, -8]

solutions = np.roots(coefficients)

print(solutions)

# [-4.  2.]


def equations(variables):

    x, y = variables

    eq1 = x**2 + y**2 - 25
    eq2 = x * y - 12

    return [eq1, eq2]


solution = fsolve(equations, [3, 4])

print(solution)


x = np.array([0, 1, 2, 3])

y = np.exp(x)

print(y)

# Input vector
x = np.array([1, 2, 3])

# Linear transformation
W = np.array([[1, 2, 0], [0, 1, 1], [2, 0, 1]])

linear_result = W @ x

# Non-linear transformation (ReLU)
nonlinear_result = np.maximum(0, linear_result)

print("Linear:", linear_result)
print("Non-linear:", nonlinear_result)
