import numpy as np

# Create matrix
A = np.array([[1, 2], [3, 4]])

# 1. Transposition
transpose = A.T

# 2. Determinant
determinant = np.linalg.det(A)

# 3. Inversion
inverse = np.linalg.inv(A)

# 4. Verify inverse
identity = A @ inverse

print("Original matrix:")
print(A)

print("\nTranspose:")
print(transpose)

print("\nDeterminant:")
print(determinant)

print("\nInverse:")
print(inverse)

print("\nVerification (A @ A_inv):")
print(identity)


A = np.array([[2, 1, 3], [1, 0, 2], [3, 2, 1]])

print("Transpose:")
print(A.T)

print("\nDeterminant:")
print(np.linalg.det(A))

print("\nInverse:")
print(np.linalg.inv(A))
