import numpy as np

# Scalar (0D tensor)
scalar = np.array(5)

# Vector (1D tensor)
vector = np.array([1, 2, 3])

# Matrix (2D tensor)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# 3D tensor
tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Scalar:", scalar.shape)
print("Vector:", vector.shape)
print("Matrix:", matrix.shape)
print("3D tensor:", tensor_3d.shape)


# Scalar (0D tensor)
scalar = np.array(5)

# Vector (1D tensor)
vector = np.array([1, 2, 3])

# Matrix (2D tensor)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# 3D tensor
tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Scalar:", scalar.shape)
print("Vector:", vector.shape)
print("Matrix:", matrix.shape)
print("3D tensor:", tensor_3d.shape)


A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# Element-wise multiplication
print(A * B)

# Matrix multiplication
print(A @ B)


A = np.ones((2, 3, 4))
B = np.ones((4, 3, 2))

result = np.tensordot(A, B, axes=([2, 1], [0, 1]))

print(result.shape)
