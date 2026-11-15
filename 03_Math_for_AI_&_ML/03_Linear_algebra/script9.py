import numpy as np
import sympy as sp

# Define matrix
A = np.array([[2, 0], [0, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


A = np.array([[4, 2], [1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


A = np.array([[4, 2], [1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

for i in range(len(eigenvalues)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]

    left = A @ eigenvector
    right = eigenvalue * eigenvector

    print(f"\nEigenvalue: {eigenvalue}")

    print("A @ v:")
    print(left)

    print("lambda * v:")
    print(right)

    print("Verification:")
    print(np.allclose(left, right))


A = sp.Matrix([[4, 2], [1, 3]])

# Calculate eigenvalues
eigenvalues = A.eigenvals()

print("Eigenvalues:")
print(eigenvalues)

# Calculate eigenvectors
eigenvectors = A.eigenvects()

print("\nEigenvectors:")
for item in eigenvectors:
    eigenvalue = item[0]
    vectors = item[2]

    print("Eigenvalue:", eigenvalue)
    print("Eigenvector:", vectors)
