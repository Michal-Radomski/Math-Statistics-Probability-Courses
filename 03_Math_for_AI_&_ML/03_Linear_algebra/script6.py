import torch  # pyright: ignore[reportMissingImports]

# Scalar
a = torch.tensor(5)

# Vector
b = torch.tensor([1, 2, 3])

# Matrix
c = torch.tensor([[1, 2], [3, 4]])

# 3D tensor
d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(a.shape)  # torch.Size([])
print(b.shape)  # torch.Size([3])
print(c.shape)  # torch.Size([2, 2])
print(d.shape)  # torch.Size([2, 2, 2])


A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

B = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Element-wise multiplication
print(A * B)

# Matrix multiplication
print(A @ B)

# Transpose
print(A.T)

# Matrix determinant
print(torch.linalg.det(A))

# Matrix inverse
print(torch.linalg.inv(A))

x = torch.tensor(3.0, requires_grad=True)

# Mathematical function
y = x**2 + 2 * x + 1

# Calculate derivative
y.backward()

print(x.grad)
# 8.0
