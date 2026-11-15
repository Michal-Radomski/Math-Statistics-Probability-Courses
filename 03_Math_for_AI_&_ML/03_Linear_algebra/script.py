import numpy as np
from scipy.spatial.distance import euclidean

# Create vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Vector addition
print(v1 + v2)
# [5 7 9]

# Vector subtraction
print(v1 - v2)
# [-3 -3 -3]

# Scalar multiplication
print(v1 * 2)
# [2 4 6]

# Dot product
print(np.dot(v1, v2))
# 32

# Vector magnitude (length)
print(np.linalg.norm(v1))
# 3.741657...

# Normalize vector
normalized = v1 / np.linalg.norm(v1)
print(normalized)

# 2D vectors
position = np.array([10, 20])
direction = np.array([1, 0])

new_position = position + direction * 5

print(new_position)

a = np.array([1, 0, 0])
b = np.array([0, 1, 0])

# Cross product
cross = np.cross(a, b)

print(cross)


v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

distance = euclidean(v1, v2)

print(distance)
