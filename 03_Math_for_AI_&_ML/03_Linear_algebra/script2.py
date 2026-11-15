import numpy as np

# Create a 2x3 matrix
A = np.array([[1, 2, 3], [4, 5, 6]])

# Create a 3x2 matrix
B = np.array([[7, 8], [9, 10], [11, 12]])

print(A)
print(B)

print("Shape of A:", A.shape)  # (2, 3)
print("Shape of B:", B.shape)  # (3, 2)


A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# Matrix addition
print(A + B)
# [[ 6  8]
#  [10 12]]

# Matrix subtraction
print(A - B)
# [[-4 -4]
#  [-4 -4]]

# Element-wise multiplication
print(A * B)
# [[ 5 12]
#  [21 32]]

# Matrix multiplication
print(A @ B)
# [[19 22]
#  [43 50]]

# Scalar multiplication
print(A * 3)
# [[ 3  6]
#  [ 9 12]]


A = np.array([[1, 2], [3, 4]])

# Transpose
print(A.T)
# [[1 3]
#  [2 4]]

# Determinant
print(np.linalg.det(A))
# -2.0

# Inverse
print(np.linalg.inv(A))
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Eigenvalues
print(np.linalg.eigvals(A))
# [-0.37228132  5.37228132]

# Matrix rank
print(np.linalg.matrix_rank(A))
# 2

A = np.array([[2, 3], [4, 1]])

b = np.array([8, 6])

# Solve Ax = b
x = np.linalg.solve(A, b)

print(x)
# [1. 2.]


# Matrix filled with zeros
print(np.zeros((3, 3)))

# Matrix filled with ones
print(np.ones((2, 4)))

# Identity matrix
print(np.eye(3))

# Matrix with random values
print(np.random.rand(3, 3))

# Matrix with values from 1 to 9
print(np.arange(1, 10).reshape(3, 3))

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# First row
print(A[0])

# Second column
print(A[:, 1])

# Element at row 2, column 3
print(A[1, 2])

# First two rows and columns
print(A[:2, :2])
